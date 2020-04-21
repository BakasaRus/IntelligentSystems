begin
  var (KX, KY) := ReadlnInteger2();
  var N := ReadlnInteger();
  
  var CountX := Range(1, KX).ToDictionary(K -> K, V -> 0);
  var CountY := Range(1, KY).ToDictionary(K -> K, V -> 0);
  var CountXY := new Dictionary<KeyValuePair<Integer, Integer>, Integer>;
  
  for var I := 1 to N do
  begin
    var (X, Y) := ReadlnInteger2();
    CountX[X] += 1;
    CountY[Y] += 1;
    var XY := KV(X, Y);
    if CountXY.Keys.Contains(XY) then
      CountXY[XY] += 1
    else
      CountXY.Add(XY, 1);
  end;
  
  var X0 := Range(1, KX).ToDictionary(K -> K, V -> N);
  var S := 0.0;
  foreach var XY in CountXY do
  begin
    var Count := XY.Value;
    var (X, Y) := (XY.Key.Key, XY.Key.Value);
    var P := CountX[X] / N * CountY[Y];
    S += (Count - P).Sqr / P;
    X0[X] -= CountY[Y];
  end;
  
  for var X := 1 to KX do
    S += X0[X] / N * CountX[X];
  
  Writeln(S:0:9);
end.