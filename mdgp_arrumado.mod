/* programa para resolucao do mdgp em mathprog*/

/* numero de individuos */
param M integer > 0;

/* numero de grupos */
param G integer > 0;

set INDIVIDUALS := 0..(M-1);
set GROUPS := 1..G;

param LIM_MIN {g in GROUPS} integer > 0;
param LIM_MAX {g in GROUPS} integer > 0;

set ARCS dimen 2 := INDIVIDUALS cross INDIVIDUALS;

param difference{ARCS};

var y{(i,j) in ARCS, g in GROUPS} binary;

var x {i in INDIVIDUALS, g in GROUPS} binary;

maximize diversity: (sum{g in GROUPS} sum{i in INDIVIDUALS, j in INDIVIDUALS: i != j} difference[i,j] * y[i,j,g])/2;


s.t. W1{i in INDIVIDUALS} : sum {g in GROUPS} x[i,g] = 1;

s.t. W2 {g in GROUPS}: sum{i in INDIVIDUALS} x[i,g] >= LIM_MIN[g];

s.t. W3 {g in GROUPS}: sum {i in INDIVIDUALS} x[i,g] <= LIM_MAX[g];

s.t. W4{g in GROUPS, i in INDIVIDUALS, j in INDIVIDUALS: i != j} : x[i,g] + x[j,g] - 1 <= y[i,j,g];

s.t. W5{g in GROUPS, j in INDIVIDUALS}: sum{i in INDIVIDUALS: i != j} y[i,j,g] >= (LIM_MIN[g] - 1) * x[j,g];

s.t. W6{g in GROUPS, j in INDIVIDUALS} : sum{i in INDIVIDUALS: i != j} y[i,j,g] <= (LIM_MAX[g] - 1) * x[j,g];

s.t. W7 {g in GROUPS, i in INDIVIDUALS, j in INDIVIDUALS}: y[i,j,g] = y[j,i,g];

end;