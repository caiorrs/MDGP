/* programa para resolucao do mdgp em mathprog*/


set VERTICES;
set ARCS within (VERTICES cross VERTICES);

/* difference between 2 individuals -> arc's weight */
param diff{ARCS};

var x{i in ARCS, g in /* range*/ m}

maximize diversity: sum{g=1 to m} sum{i in VERTICES} sum{j in VERTICES and i <> j} d(i,j)*y(i,j,g)

s.t. sum{g=1 to m} x(i,g) = 1
s.t. sum{i in VERTICES} x(i,g) >= a(g)
s.t. sum{i in VERTICES} x(i,g) <= b(g)
s.t. x(i,g) + x(j,g) - 1 <= y(i,j,g)
s.t. sum{j in VERTICES and i <> j} y(i,j,g) >= (a(g) - 1) * x(j,g)
s.t. sum{j in VERTICES and i <> j} y(i,j,g) <= (b(g) - 1) * x(j,g)
s.t. x(i,g) in {0,1}
s.t. y(i,j,g) in {0,1}
