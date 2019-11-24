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

maximize diversity: sum{g in GROUPS} sum{i in INDIVIDUALS} sum{j in (i+1)..M /*in INDIVIDUALS*/} d[i,j]; /* *y[i,j,g]*/

s.t. W1{g in GROUPS} : sum{i in INDIVIDUALS} d[i,g] = 1;
s.t. W4{g in GROUPS, i in INDIVIDUALS, j in (i+1)..M} : d[i,g] + d[j,g] - 1 <= y[i,j,g];
s.t. W5{g in GROUPS, i in INDIVIDUALS, k in INDIVIDUALS} : 0-(sum{j in (i+1)..M} y[i,j,g]) <= (5 /*a[g]*/ - 1) * d[k,g];
s.t. W6{k in INDIVIDUALS, i in INDIVIDUALS, g in GROUPS} : sum{j in INDIVIDUALS} y[i,j,g] <= (5 /*b[g]*/ - 1) * d[k,g];
s.t. W7{i in INDIVIDUALS, g in GROUPS} : d[i,g] in 0..1;
s.t. W8{i in INDIVIDUALS, g in GROUPS, j in (i+1)..M} : y[i,j,g] in 0..1;

end;


/*s.t. W2 : 0-sum{i in INDIVIDUALS, g in GROUPS} d[i,g] <= a[g]*/;
/*s.t. W3 : sum{i in INDIVIDUALS, g in GROUPS} d[i,g] <= b[g] */;
