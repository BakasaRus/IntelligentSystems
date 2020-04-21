begin
  var M := ReadlnInteger();
  var LayersNum := (2 ** M).Trunc();
  var F := ReadArrInteger(LayersNum);
  
  Println(2);
  Println(LayersNum, 1);
  
  for var I := 0 to LayersNum - 1 do
  begin
    var Bin := System.Convert.ToString(I, 2).PadLeft(M, '0').Select(C -> C.ToDigit()).ToList();
    var BinSum := 0.5 - Bin.Sum();
    Bin := Bin.Select(Digit -> Digit = 1 ? 1 : -1).ToList();
    Bin.Print();
    Write(' ');
    BinSum.Println();
  end;
  
  F.Print();
  Write(' ');
  (-0.5).Print();
end.