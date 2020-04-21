begin
  var (K, N) := ReadlnInteger2();
  var Count := Range(1, K).ToDictionary(K -> K, V -> new Dictionary<Integer, Integer>());
  var CountX := Range(1, K).ToDictionary(K -> K, V -> 0);
  var XY := Range(1, K).ToDictionary(K -> K, V -> new HashSet<Integer>());
  
  for var I := 1 to N do
  begin
    var (X, Y) := ReadlnInteger2();
    CountX[X] += 1;
    if Y in XY[X] then
      Count[X][Y] += 1
    else begin
      Count[X][Y] := 1;
      XY[X] += [Y];
    end;
  end;
  
  Range(1, K).Sum(X -> begin
    var eY, eY2: Double;
    XY[X].ForEach(Y -> begin
      var R := Count[X][Y] * 1.0 / CountX[X];
      eY += R * Y;
      eY2 += R * Y * Y;
    end);
    Result := (eY2 - eY ** 2) * (CountX[X] * 1.0 / N);
  end).Println();
end.