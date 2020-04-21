type
  Entity = record
    Features: List<Double>;
    Target: Double;
    Dist: Double;
  end;

function GetKernel(Name: String): Func<Double, Double>;
begin
  case Name of
    'uniform': Result := (U: Real) -> Abs(U) < 1 ? 0.5 : 0;
    'triangular': Result := (U: Real) -> Abs(U) < 1 ? 1 - Abs(U) : 0;
    'epanechnikov': Result := (U: Real) -> Abs(U) < 1 ? 0.75 * (1 - U ** 2) : 0;
    'quartic': Result := (U: Real) -> Abs(U) < 1 ? 15 / 16 * (1 - U ** 2) ** 2 : 0;
    'triweight': Result := (U: Real) -> Abs(U) < 1 ? 35 / 32 * (1 - U ** 2) ** 3 : 0;
    'tricube': Result := (U: Real) -> Abs(U) < 1 ? 70 / 81 * (1 - Abs(U ** 3)) ** 3 : 0;
    'gaussian': Result := (U: Real) -> 1 / Sqrt(2 * Pi) * Exp(-0.5 * U ** 2);
    'cosine': Result := (U: Real) -> Abs(U) < 1 ? Pi / 4 * Cos(Pi / 2 * U) : 0;
    'logistic': Result := (U: Real) -> 1 / (Exp(U) + 2 + Exp(-U));
    'sigmoid': Result := (U: Real) -> 2 / Pi * 1 / (Exp(U) + Exp(-U));
  end;
end;

function GetDistance(Name: String): Func2<List<Double>, List<Double>, Double>;
begin
  case Name of
    'manhattan': Result := (X, Y: List<Double>) -> X.Zip(Y, (A, B) -> Abs(A - B)).Sum();
    'euclidean': Result := (X, Y: List<Double>) -> X.Zip(Y, (A, B) -> Sqr(A - B)).Sum().Sqrt();
    'chebyshev': Result := (X, Y: List<Double>) -> X.Zip(Y, (A, B) -> Abs(A - B)).Max();
  end;
end;

begin
  Reset(Input, 'input.txt');
  var (N, M) := ReadlnInteger2();
  var Data := new List<Entity>;
  loop N do
  begin
    var Point := new Entity();
    Point.Features := ReadArrReal(M).ToList();
    Point.Target := ReadlnReal();
    Data.Add(Point);
  end;
  
  var Query := new Entity;
  Query.Features := ReadArrReal(M).ToList();
  Readln();
  var Dist := GetDistance(ReadlnString());
  var Kernel := GetKernel(ReadlnString());
  var Window := ReadlnString();
  var H := ReadlnReal();
  
  for var I := 0 to N - 1 do
  begin
    var Test := Data[I];
    Test.Dist := Dist.Invoke(Data[I].Features, Query.Features);
    Data[I] := Test;
  end;
  
  if Window = 'variable' then
  begin
    Data := Data.OrderBy(X -> X.Dist).ToList();
    H := Data[H.Round()].Dist;
  end;
  
  var Overall := Data.Sum(X -> X.Target) / N;
  if H = 0 then
  begin
    var Same := Data.Where(X -> X.Features = Query.Features).Select(X -> X.Target);
    Query.Target := Same.Count > 0 ? Same.Average : Overall;
  end
  else begin
    Var (SumUp, SumDown) := (0.0, 0.0);
    foreach var Point in Data do
    begin
      var KF := Kernel.Invoke(Point.Dist / H);
      SumUp += Point.Target * KF;
      SumDown += KF;
    end;
    Query.Target := SumDown <> 0 ? SumUp / SumDown : OverAll;
  end;
  
  Query.Target.Println();
end.