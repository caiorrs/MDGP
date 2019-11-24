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
var y{(i,j) in ARCS, g in GROUPS};

param g := 1;

maximize diversity: /*sum{g in G}*/ sum{i in INDIVIDUALS} sum{j in INDIVIDUALS} /*d[i,j]*y[i,j,1]*/ 1;

/*s.t. A: sum{g in G} d[i,g] = 1;*/
s.t. B: sum{i in INDIVIDUALS} d[i,g] >= LIMITS /*a[g]*/;
s.t. B: sum{i in INDIVIDUALS} d[i,g] <= LIMITS /*b[g] */;
s.t. B: d[i,g] + d[j,g] - 1 <= y[i,j,g];
s.t. B: sum{j in INDIVIDUALS and i <> j} y[i,j,g] >= (LIMITS /*a[g]*/ - 1) * d[j,g];
s.t. B: sum{j in INDIVIDUALS and i <> j} y[i,j,g] <= (LIMITS /*b[g]*/ - 1) * d[j,g];
s.t. B: d[i,g] >= 0;
s.t. B: d[i,g] <= 1;
s.t. B: y[i,j,g] >= 0;
s.t. B: y[i,j,g] <= 1;

end;
