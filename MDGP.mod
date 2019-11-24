/* programa para resolucao do mdgp em mathprog*/

/* numero de individuos */
param M integer > 0;

/* numero de grupos */
param G integer > 0;

/* tipo de grupo - ss/ds - same size/different size */
# @alberto não precisa representar essa informação.
#param TYPE symbolic;

# @alberto Movi para cima.
set INDIVIDUALS := 0..(M-1);
set GROUPS := 1..G;

# @alberto Os limites de mínimo e máximo são parâmetros do problema, e existe
# um par de limites para cada grupo. Veja abaixo a minha sugestão.
#set LIMITS;
#display LIMITS;
param LIM_MIN {g in GROUPS} integer > 0;
param LIM_MAX {g in GROUPS} integer > 0;

# @alberto Fiz a geraçao automática do conjunto ARCS aqui.
#set ARCS within (INDIVIDUALS cross INDIVIDUALS);
set ARCS dimen 2 := INDIVIDUALS cross INDIVIDUALS;

# @alberto Esse parâmetro que é o 'd' da formulação, lá na função objetivo.
param difference{ARCS};

# @alberto Isso não deveria ser variável, e sim um parâmetro. Além disso, está
# redundante com 'difference'.
#var d{(i,j) in ARCS} >= 0;

# @alberto Faltou o binary.
var y{(i,j) in ARCS, g in GROUPS} binary;

# @alberto Faltou as variáveis x.
var x {i in INDIVIDUALS, g in GROUPS} binary;

# @alberto Não sei bem o que significam. Por via das dúvidas, comentei.
# set IN_OUT := 0..1;
# display IN_OUT;

# @alberto Ajustei a expressão para simplificar e usar o difference.
#maximize diversity: sum{g in GROUPS} sum{i in INDIVIDUALS} sum{j in INDIVIDUALS} d[i,j] * (if i != j then y[i,j,g] else 1);
maximize diversity: (sum{g in GROUPS} sum{i in INDIVIDUALS, j in INDIVIDUALS: j > i} difference[i,j] * y[i,j,g]);

# @alberto O uso de GROUPS e INDIVIDUALS está trocado em algumas restrições.

# @alberto Restrições (4).
#s.t. W1{g in GROUPS} : sum{i in INDIVIDUALS} d[i,g] = 1;
s.t. W1{i in INDIVIDUALS} : sum {g in GROUPS} x[i,g] = 1;

# @alberto Restrições (7).
#s.t. W4{g in GROUPS, i in INDIVIDUALS, j in (i+1)..M} : d[i,g] + d[j,g] - 1 <= y[i,j,g];
s.t. W4{g in GROUPS, i in INDIVIDUALS, j in INDIVIDUALS: i != j} : x[i,g] + x[j,g] - 1 <= y[i,j,g];

# @alberto Restrições (8).
# Está muito estranha a formulação. Reescrevi conforme está no modelo do artigo.
#s.t. W5{g in GROUPS, i in INDIVIDUALS, k in INDIVIDUALS} : 0-(sum{j in (i+1)..M} y[i,j,g]) <= (5 /*a[g]*/ - 1) * d[k,g];
s.t. W5{g in GROUPS, j in INDIVIDUALS}: sum{i in INDIVIDUALS: i != j} y[i,j,g] <= (LIM_MIN[g] - 1) * x[j,g];

# @alberto Restrições (9).
# Mesmo problema da W5.
#s.t. W6{k in INDIVIDUALS, i in INDIVIDUALS, g in GROUPS} : sum{j in INDIVIDUALS} y[i,j,g] <= (5 /*b[g]*/ - 1) * d[k,g];
s.t. W6{g in GROUPS, j in INDIVIDUALS} : sum{i in INDIVIDUALS: i != j} y[i,j,g] <= (LIM_MAX[g] - 1) * x[j,g];


/*s.t. W7{i in INDIVIDUALS, g in GROUPS} : d[i,g] in IN_OUT;
s.t. W8{i in INDIVIDUALS, g in GROUPS, j in (i+1)..M} : y[i,j,g] in IN_OUT;*/

# @alberto Restrições (5).
/*s.t. W2 : 0-sum{i in INDIVIDUALS, g in GROUPS} d[i,g] <= a[g];*/
s.t. W2 {g in GROUPS}: sum{i in INDIVIDUALS} x[i,g] <= LIM_MIN[g];

# @alberto Restrições (6).
/*s.t. W3 : sum{i in INDIVIDUALS, g in GROUPS} d[i,g] <= b[g] ;*/
s.t. W3 {g in GROUPS}: sum {i in INDIVIDUALS} x[i,g] >= LIM_MAX[g];

end;
