begin
  var (N, M, K) := ReadlnInteger3();
  var C := ReadArrInteger(N);
  
  var Groups := Range(1, M).Select(I -> new List<Integer>).ToList();
  C.Numerate().ForEach(T -> begin Groups[T[1] - 1].Add(T[0]) end);
  
  var AllGroups := new List<Integer>;
  Groups.ForEach(Group -> AllGroups.AddRange(Group));
  
  var Buckets := Range(1, K).Select(I -> new List<Integer>).ToList();
  
  SeqGen(N, 0, B -> (B + 1) mod K)
    .ZipTuple(AllGroups)
    .ForEach(T -> begin Buckets[T.Item1].Add(T.Item2) end);
  
  foreach var Bucket in Buckets do
  begin
    Print(Bucket.Count);
    Bucket.Sorted().Println();
  end;
end.