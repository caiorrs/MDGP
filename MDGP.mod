/* programa para resolucao do mdgp em mathprog*/

/* numero de individuos */
param M integer > 0;

/* numero de grupos */
param G integer > 0;

/* tipo de grupo - ss/ds - same size/different size */
param TYPE symbolic;

set LIMITS;
display LIMITS;

set INDIVIDUALS := 0..(M-1);
set GROUPS := 1..G;

set ARCS within(INDIVIDUALS cross INDIVIDUALS);
param difference{ARCS};

var d{(i,j) in ARCS} >= 0;
/*var y{(i,j) in ARCS, g in GROUPS};*/
var x{}

maximize diversity: sum{g in GROUPS} sum{i in 1..(M-1)} sum{j in (i+1)..M} d[i,j]*x[i,g]*x[j,g];

s.t. sum{g in G, i in INDIVIDUALS} x[i,g] = 1;
s.t. sum{i in M} x[i,g] >= LIMITS /*a[g]*/;
s.t. sum{i in M>} x[i,g] <= LIMITS /*b[g] */;
s.t. x[i,g] in {0, 1};

end;
