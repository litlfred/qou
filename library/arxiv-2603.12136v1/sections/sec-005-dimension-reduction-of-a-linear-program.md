---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-005-dimension-reduction-of-a-linear-program
section_title: "Dimension Reduction of a Linear Program"
section_number: null
pages: 8-10
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Throughout this work, we consider the following linear program in standard form.
minc ⊺xs.t.Ax=b, ℓ≤x≤u(F(A,b,ℓ,u,c))
withA∈R V×W ,b∈R V,ℓ w∈R∪{−∞}andu∈R∪{∞}such thatℓ w≤u w
for allw∈W. We useF(A,b,ℓ,u,c)to denote the linear program, and we define
its feasible region asP(A,b,ℓ,u) :={x∈R W |Ax=b,ℓ≤x≤u}. For the linear
programF(A,b,ℓ,u,c)and a partitionPofVand a partitionQofW,(P,Q)is an
equitable partition ofF(A,b,ℓ,u,c)if(P,Q)is an equitable partition ofA,Pis an
equitable partition ofb, andQis an equitable partition ofℓ,u, andc. The key result
necessary for DRCR is given in [11, Lemma 7.1] and shows that a linear program
that has an equitable partition(P,Q)can be reduced to a linear program with a
constraint matrix with dimension|P|×|Q|. We show a variation of this result which
has essentially the same proof, but which produces a slightly different but equivalent
linear program whose variables and constraints are scaled differently. The motivation
for deviating from [11] in Proposition 3 will become clear in Section 4, where we
consider mixed-integer linear programs.
Proposition 3(Grohe, Kersting, Mladenov and Selman [11] )For givenA∈R V×W ,b∈
RV,c∈R W and vectorsℓ,uwithℓ w∈R∪{−∞}andu w∈R∪{∞}such thatℓ w≤uw holds
for allw∈W, consider the linear programF(A,b,ℓ,u,c). Let(P,Q)be an equitable partition
ofF(A,b,ℓ,u,c). DefineA ′ := Π⊺
PAgΠQ,b′ := Π⊺
Pb,ℓ′ := Π⊺
Qℓ,u′ := Π⊺
Quandc ′ :=gΠQ
⊺
c,
and consider the reduced linear programF(A′,b′,ℓ′,u′,c′). Then, the following hold:
(i) Ifx∈R W is feasible forP(A,b,ℓ,u), theny := Π⊺
Qxis feasible forP(A ′,b′,ℓ′,u′)and
c′⊺y=c ⊺xholds.
(ii) Ify∈R Q is feasible forP(A′,b′,ℓ′,u′), thenx :=gΠQyis feasible forP(A,b,ℓ,u)and
c⊺x=c ′⊺yholds
ProofLet us prove the first point. Letx∈P(A,b,ℓ,u)be given and considery := Π ⊺
Qx.
First of all, we show that for eachQ∈Q,ℓ′
Q≤y Q≤u′
Q holds. Note thatℓ′
Q = (Π⊺
Pℓ)Q =P
w∈Qℓw andu′
Q = (Π⊺
Pu)Q =P
w∈Quw andy Q =P
w∈Qxw hold. Then,ℓ′
Q≤y Q≤u′
Q
is equivalent toP
w∈Qℓw≤P
w∈Qxw≤P
w∈Quw, which is clearly valid by summing the
inequalitiesℓ w≤x w≤u w for allw∈Q. Then, we show thatyis feasible by showing that
the equationA′y=b ′ holds. The following equations hold.
A′y= Π ⊺
PAgΠQΠ⊺
Qx
(a)
= Π ⊺
PgΠPΠ⊺
PAx
(b)
= Π ⊺
PAx= Π ⊺
Pb=b ′
The equality in (a) follows from the fact that(P,Q)is an equitable partition ofA, which
implies that(gΠPΠ⊺
P,gΠQΠ⊺
Q)is a fractional automorphism ofAusing Proposition 2. The
equality in (b) follows from Proposition 1(i). Thus,y∈P(A′,b′,ℓ′,u′)holds, andyis indeed
feasible. Finally, sinceQis an equitable partition ofcit follows thatc′⊺y=c ⊺gΠQΠ⊺
Qx=c ⊺x,
where we use Proposition 1(iii) in the final step.
8
Next, we proceed with the proof of second point. Lety∈P(A′,b′,ℓ′,u′)be a given feasible
point, and considerx :=gΠQy. First, note that sinceQis an equitable partition ofℓandu,
that for anyQ∈Qwe haveℓ ′
Q =|Q|ℓw for allw∈Qandu ′
Q =|Q|uw, since thelw andu w
entries must be identical for allw∈Qand are summed by definition ofΠ ⊺
Q. Additionally,
note that for eachw∈W, there exists exactly oneQ∈Qsuch thatx w = 1
|Q|yQ. Then, we
have for everyw∈WandQ∈Qwithw∈Qthatℓ ′
Q≤y Q≤u′
Q holds, which implies
that 1
|Q|ℓ′
Q≤ 1
|Q|yQ≤ 1
|Q|u′
Q holds. By substituting usingℓ′
Q =|Q|ℓ w,u′
Q =|Q|u w and
xw = 1
|Q|yQ, we see thatℓw≤xw≤uw holds for allw∈W.
Then, similar to the proof of the first point, we considerAxand show that it equalsb.
Ax=A gΠQy
(c)
=A gΠQΠ⊺
QgΠQy
(d)
= gΠPΠ⊺
PAgΠQy= gΠPA′y= gΠPb′ =gΠPΠ⊺
Pb
(e)
=b
Here, (c) holds by Proposition 1(i) and (d)holds since(P,Q)is an equitable partition of
A, which implies a fractional automorphism using Proposition 2. Additionally, (e) follows
by Proposition 1(iii) and the factPis an equitable partition ofb. Thus,xis feasible for
P(A,b,ℓ,u). Finally, note thatc ⊺x=c ⊺gΠQΠ⊺
Qx=c ′⊺yholds, where the first equality follows
from Proposition 1(iii) and the fact thatQis an equitable partition ofc.□
Occasionally, we will use the notationR P,Q(F(A,b,ℓ,u,c)) :=
F(Π ⊺
PAgΠQ,Π ⊺
Pb,Π ⊺
Qℓ,Π ⊺
Qu,gΠQ
⊺
c)to denote the reduced linear program in
Proposition 3.
The key difference in the proof of Proposition 3 compared to the proof in [11,
Lemma 7.1] is that we use the fractional automorphism(fΠPΠ⊺
P,gΠQΠ⊺
Q), instead of
(ΠPfΠP
⊺
,ΠQgΠQ
⊺
), which leads to different variable and constraint scaling in the
reduced linear programs and in the mappings from and to the original linear program.
Although we present our results in standard form, equitable partitions can also be
applied to linear programs in inequality form by first introducing slack variables and
turning them into equality form. In Proposition 4 we show that this procedure does
not affect equitability of the constraint matrix.
Proposition 4Let(P,Q)be an equitable partition ofA∈R V×W . Then(P,Q∪P)is an
equitable partition of

A I

.
ProofConsider any block(P,Q)∈P×(Q∪P). IfQ∈Q, then

A I

PQ =APQ holds, and
APQ satisfies the equitability conditions (1) and (2) since(P,Q)is an equitable partition
ofA. Otherwise, forQ∈P, we have that

A I

PQ =I P,P′ for someP ′∈P. IfP=P ′,
thenI P,P is aP×Pidentity matrix, which satisfies (1) and (2). Otherwise, ifP̸=P ′, then
IP,P′ is an all-zero matrix, which also satisfies (1) and (2). Thus,P×(Q∪P)is an equitable
partition of

A I

.□
Note that the introduced slack variables will all have identical bounds and do not
participate in the objective, so the equitability conditions for the variable bounds and
objective are also satisfied under the addition of slack variables. However, the stan-
dard form may have additional reductions compared to inequality form if the slack
variables can be aggregated with non-slack variables. In [37] the authors observe that
additional reductions on the slack variables in equality form lead to large running
time improvements for algorithms that enumerate all non-symmetric solutions of
9
certain MILP. Intuitively, this can be explained by the fact that certain relationships
between the slack of the constraints and the variables become more explicit upon
adding the slack variables. Thus, we consider the more general standard form in the
remainder of this work.
The authors of [11] show that DRCR is advantageous primarily because it is fast
to compute and because it generalizes permutation symmetries. We have not yet
discussed one of its more relevant downsides, which is that a basic optimal solution to
the reduced LP is not necessarily mapped to a basic solution of the original LP. This is
particularly relevant for branch-and-bound approaches that utilize an LP relaxation,
as for these the reduction for the LP may not be valid for the MILP, and thus we need
to obtain a solution to the original LP. For MILP, basic linear programming solutions
are necessary in an efficient branch-and-cut implementation, which relies heavily on
the dual simplex algorithm to branch quickly and to efficiently find cutting planes
such as those formulated by Gomory [38] from the simplex tableau. For DRCR, the
original solution obtained from the the reduced solution may lie in the interior of
the optimal face of the original LP. Then, to obtain a basic solution, one has to run
a crossover procedure for the original problem to obtain a feasible vertex from the
interior point [39]. In some cases, the crossover procedure has a runtime that may be
orders of magnitude larger than solving the reduced linear program. For example, for
problems with a transitive symmetry group, the linear program computed by DRCR
consists of a single variable and is easily solved, but the crossover procedure may be
as expensive as solving the original linear program.
