function SumDifferences(Self: List<Int64>): Int64; extensionmethod;
begin
  var L := Self.Count;
  Result := Range(-L + 1, L + 1, 2).Zip(Self, (Coef, I) -> Coef * I).Sum() * 2;
end;

begin
  var (K, N) := ReadlnInteger2();
  var NumsInCat := Range(1, K).ToDictionary(K -> K, V -> new List<Int64>);
  var AllNums := new List<Int64>;
  
  loop N do
  begin
    var (X, Y) := ReadlnInteger2();
    NumsInCat[Y].Add(X);
    AllNums.Add(X);
  end;
  
  AllNums.Sort();
  for var I := 1 to K do
    NumsInCat[I].Sort();
  
  var Whole := AllNums.SumDifferences();
  var Inner := NumsInCat.Values.Select(Cat -> Cat.SumDifferences()).Sum();
  Inner.Println();
  (Whole - Inner).Println();
end.