function Ranking(X: List<int64>): List<int64>;
begin
  var S := X.Sorted().ToList();
  Result := new List<int64>;
  foreach var V in X do
    Result.Add(S.BinarySearch(V) + 1);
end;

begin
  var N: int64;
  N := ReadlnInteger();
  
  var X := new List<int64>;
  var Y := new List<int64>;
  
  loop N do
  begin
    var (A, B) := ReadlnInteger2();
    X.Add(A);
    Y.Add(B);
  end;
  
  var XRanks := Ranking(X);
  var YRanks := Ranking(Y);
  
  var Sigma := XRanks.Zip(YRanks, (A, B) -> Sqr(A - B)).Sum();
  var P := 1 - 6 * Sigma / N / (Sqr(N) - 1);
  Writeln(P:0:9);
end.