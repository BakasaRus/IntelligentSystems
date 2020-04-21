begin
  Reset(Input, 'input.txt');
  Rewrite(Output, 'output.txt');
  var K := ReadlnInteger();
  var Penalties := ReadArrInteger(K);
  var (Alpha, N) := ReadlnInteger2();
  
  var ClassCount := Range(1, K).ToDictionary(K -> K, V -> 0.0);
  var Classes := Range(1, K).ToDictionary(K -> K, V -> new Dictionary<String, Double>());
  var Classes2 := Range(1, K).ToDictionary(K -> K, V -> new Dictionary<String, Double>());
  var Alphabet := new HashSet<String>();
  
  for var I := 1 to N do
  begin
    var (CurClass, Size) := ReadInteger2();
    var Words := ReadlnString().ToWords().ToHashSet();
    ClassCount[CurClass] += 1;
    foreach var W in Words do
    begin
      if not (W in Alphabet) then
      begin
        Alphabet.Add(W);
        for var J := 1 to K do
          Classes[J][W] := 0.0;
      end;
      Classes[CurClass][W] += 1;
    end;
  end;
  
  foreach var CC in Classes do
  begin
    var (CurClass, Words) := (CC.Key, CC.Value);
    foreach var W in Alphabet do
      if W in Words then
      begin
        Words[W] += Alpha;
        Words[W] /= ClassCount[CurClass] + 2.0 * Alpha;
        Classes2[CurClass][W] := Log(1 - Words[W]);
        Words[W] := Log(Words[W]);
      end;
    ClassCount[CurClass] /= N;
  end;
  
  var M := ReadlnInteger();
  for var I := 1 to M do
  begin
    var Size := ReadInteger();
    var KnownWords := ReadlnString().ToWords()
                                    .Where(W -> W in Alphabet)
                                    .ToHashSet();
    var CountMask := ClassCount.Values.Select(V -> V > 0).ToArray();
    var P := ClassCount.Keys.ToDictionary(K -> K, V -> 0.0);
    foreach var X in ClassCount do
      P[X.Key] := X.Value > 0 ? Log(X.Value) : 1.0;
    foreach var W in Alphabet do
    begin
      var ClassesSource := W in KnownWords ? Classes : Classes2;
      foreach var CC in ClassesSource do
      begin
        var (CurClass, Words) := (CC.Key, CC.Value);
        P[CurClass] += Words[W];
      end;
    end;
    var PMax := P.Values.Max();
    var L := P.Values
              .Numerate(0)
              .Select(T -> CountMask[T.Item1] ? Exp(T.Item2 - PMax) : 0.0)
              .Zip(Penalties, (Weight, Penalty) -> Weight * Penalty)
              .ToArray();
    var S := L.Sum();
    L.Select(X -> X / S).Println();
  end;
end.