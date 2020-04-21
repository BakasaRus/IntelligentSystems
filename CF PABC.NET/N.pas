begin
  var (KX, KY) := ReadlnInteger2();
  var N := ReadlnInteger();
  
  var Count := Range(1, KX).ToDictionary(K -> K, V -> new Dictionary<Integer, Integer>);
  var CountX := Range(1, KX).ToDictionary(K -> K, V -> 0);
  var XY := Range(1, KX).ToDictionary(K -> K, V -> new HashSet<Integer>());
  
  loop N do
  begin
    var (X, Y) := ReadlnInteger2();
    CountX[X] += 1;
    if XY[X].Contains(Y) then
      Count[X][Y] += 1
    else begin
      Count[X].Add(Y, 1);
      XY[X].Add(Y);
    end;
  end;
  
  var S := 0.0;
  for var X := 1 to KX do
  begin
    var PS := 0.0;
    foreach var Y in XY[X] do
    begin
      var Temp := Count[X][Y] / CountX[X];
      PS -= Temp * Log(Temp);
    end;
    S += CountX[X] / N * PS;
  end;
  
  S.Println();
end.