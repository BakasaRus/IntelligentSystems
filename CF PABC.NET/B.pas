begin
  var K := ReadlnInteger();
  var CM := new List<List<integer>>;
  var Total := 0;
  
  loop K do
  begin
    var Row := ReadlnString().ToWords().Select(X -> X.ToInteger()).ToList();
    CM.Add(Row);
    Total += Row.Sum();
  end;
  
  var Stats := new List<System.Tuple<Integer, Integer, Double>>();
  var (RecallW, PrecisionW) := (0.0, 0.0);
  for var I := 0 to K - 1 do
  begin
    var Count := CM[I].Sum();
    var Predicted := Range(0, K - 1).Select(J -> CM[J][I]).Sum();
    var Precision := Count > 0 ? CM[I][I] / Count : 0;
    var Recall := Count > 0 ? CM[I][I] / Predicted : 0;
    var FScore := (Precision + Recall) > 0 ? 2 * Precision * Recall / (Precision + Recall) : 0;
    Stats.Add((Count, Predicted, FScore));
    
    RecallW += CM[I][I] / Total;
    PrecisionW += Predicted > 0 ? CM[I][I] / Predicted * Count / Total : 0;
  end;
  
  var MacroF := 2 * PrecisionW * RecallW / (PrecisionW + RecallW);
  var MicroF := Range(0, K - 1).Select(I -> Stats[I][0] * Stats[I][2]).Sum() / Total;
  Writeln(MacroF:0:9);
  Writeln(MicroF:0:9);
end.