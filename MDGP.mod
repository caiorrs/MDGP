/* programa para resolucao do mdgp em mathprog*/

/* numero de individuos */
param M integer > 0;
/* numero de grupos */
param G integer > 0;
/* tipo de grupo - ss/ds - same size/different size */
param TYPE symbolic;

param LIMITS;

/*param ARCS;*/

set INDIVIDUALS := 1..M;
set GROUPS := 1..G;

display INDIVIDUALS;
display GROUPS;

/*display 'individuals ', INDIVIDUALS;*/

/*set ARCS within (INDIVIDUALS cross INDIVIDUALS);
display ARCS;*/

/*
param DIFFERENCE := {ARCS}*/



/*
var x{i in ARCS, for g : m}

maximize diversity: sum{g=1 to m} sum{i in VERTICES} sum{j in VERTICES and i <> j} d(i,j)*y(i,j,g)

s.t. A: sum{g=1 to m} x(i,g) = 1
s.t. B: sum{i in VERTICES} x(i,g) >= a(g)
s.t. B: sum{i in VERTICES} x(i,g) <= b(g)
s.t. B: x(i,g) + x(j,g) - 1 <= y(i,j,g)
s.t. B: sum{j in VERTICES and i <> j} y(i,j,g) >= (a(g) - 1) * x(j,g)
s.t. B: sum{j in VERTICES and i <> j} y(i,j,g) <= (b(g) - 1) * x(j,g)
s.t. B: x(i,g) >= 0
s.t. B: x(i,g) <= 1
s.t. B: y(i,j,g) >= 0
s.t. B: y(i,j,g) <= 1
*/
