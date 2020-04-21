begin
  var N := ReadlnInteger();
  
  var X := new List<integer>;
  var Y := new List<Integer>;
  
  loop N do
  begin
    var (A, B) := ReadlnInteger2();
    X.Add(A);
    Y.Add(B);
  end;
  
  var (XMean, YMean) := (X.Average, Y.Average);
  var Numerator := X.Zip(Y, (A, B) -> (A - XMean) * (B - YMean)).Sum();
  var Denominator := (X.Select(A -> (A - XMean).Sqr).Sum() * Y.Select(A -> (A - YMean).Sqr).Sum()).Sqrt;
  var Ro := Denominator <> 0 ? Numerator / Denominator : 0;
  Writeln(Ro:0:9);
end.