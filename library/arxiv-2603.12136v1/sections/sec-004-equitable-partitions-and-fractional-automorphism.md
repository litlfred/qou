---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-004-equitable-partitions-and-fractional-automorphism
section_title: "Equitable partitions and fractional automorphisms"
section_number: null
pages: 6-8
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
First, we introduce equitable partitions of linear programs as presented in [11]. Given
a matrixA∈R V×W , DRCR iteratively computes partitionsPi andQ i ofVandW,
the rows and columns ofA. LetP0 ={V}andQ 0 ={W}. A partition(P,Q)of the
rows and columns ofAis said to beequitableif for allP∈P,Q∈Qit holds that
X
w∈Q
Av,w =
X
w∈Q
Av′,w for allv,v ′∈P(1)
X
v∈P
Av,w =
X
v∈P
Av,w′ for allw,w′∈Q.(2)
In words, for every block ofAdefined byP,Q, the row sums and columns sums
restricted to elements in the block must be equal. For a vectorb∈RV, we similarly
say thatPis anequitable partitionofbifb v =b v′ holds for allv,v′∈Pfor allP∈P.
If for(P,Q)∈P×Qboth (1) and (2) hold, we also say that(P,Q)defines anequi-
table blockofA. A partitionP 1 is said torefinea partitionP 2 if for everyP1∈P 1
there exists someP2∈P 2 such thatP 1⊆P 2. Color refinement works by iteratively
refiningP i andQ i, by splitting any classesP∈P i orQ∈Q i into multiple classes in
6
Pi+1 andQ i+1 if they do not satisfy the conditions (1) and (2) respectively. For some
iterationi, this iterative process satisfiesP i =P i+1 andQ i =Q i+1. For thisi, the
partition(P∞,Q∞) := (Pi,Qi)is known as thecoarsest equitable partitionofA. The
authors of [11] adapt the well-known fast color refinement algorithm by Paige and
Tarjan [35], that is based on ideas by Hopcroft [36], to compute the coarsest equitable
partition. Forn=|V|+|W|and the total bitlengthmof the entries ofA, they show
that one can compute the coarsest equitable partition inO((n+m) logn)time.
Given a partitionPof a setV, itspartition matrixis denoted byΠP∈{0,1} V×P ,
for which(Π) vP = 1⇐⇒v∈Pholds for allv∈VandP∈ P. Ascaled
partition matrix fΠP is a normalized partition matrix defined such that(fΠP)vP =(
1
|P| ifv∈P
0otherwise
holds for allv∈VandP∈P. Proposition 1 summarizes a few
identities for partition matrices and scaled partition matrices that are established and
used in [11].
Proposition 1([11])Given a partitionPof a setV, the following hold:
(i) gΠP
⊺
ΠP = Π⊺
PgΠP =IP×P.
(ii) Forv,v ′∈V,( gΠPΠ⊺
P)v,v′ = (ΠPgΠP
⊺
)v′,v =
( 1
|P| ifv,v ′∈Pfor someP∈P
0otherwise.
(iii) IfPis an equitable partition ofb∈R V, thenb= gΠPΠ⊺
Pb= ΠPgΠP
⊺
bholds.
ProofFor (i), consider anyP,P ′ ∈ Pand note that( gΠP
⊺
ΠP)P,P′ =(P
v∈P
1
|P| ifP=P ′
0otherwise
=I P×P holds. The identity in (i) follows sinceI P×P =
(gΠP
⊺
ΠP)⊺ = Π ⊺
PgΠP holds. The proof of (ii) follows by the definition of matrix trans-
pose and multiplication. For (iii) we have forv∈VandP∈ Psuch thatv∈Pthat
(gΠP
⊺
ΠPb)v = P
v′∈P
1
|P|bv′ =b v, where the last equality holds sincePis an equitable
partition ofb, which implies thatbv =bv′ holds for allv′∈P.□
A matrixA∈R V×W is said to bestochasticif it is nonnegative andP
w∈W Av,w =
1for allv∈V, and it isdoubly stochasticif bothAandA ⊺ are stochastic. For a matrix
A∈R V×W , a pair(X,Y)∈R V×V ×RW×W of doubly stochastic matrices is said to
be afractional automorphismofAifXA=AYholds. One of the key insights made
by the authors of [11] is given in Proposition 2, and relates fractional automorphisms
ofAto its equitable partitions.
Proposition 2([11]) If(P,Q)is an equitable partition of a matrixA∈R V×W , then
(ΠPgΠP
⊺
,ΠQgΠQ
⊺
)is a fractional automorphism ofA.
In Proposition 2, it can be easily checked thatΠPfΠP
⊺
andΠQgΠQ
⊺
are both doubly
stochastic due to Proposition 1(ii). From Proposition 1(ii) and Proposition 2 it also
7
follows that if(P,Q)is an equitable partition, that( fΠPΠ⊺
P,gΠQΠ⊺
Q)is a fractional
automorphism ofA.
