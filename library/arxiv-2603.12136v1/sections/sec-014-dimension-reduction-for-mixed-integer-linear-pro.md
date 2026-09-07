---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-014-dimension-reduction-for-mixed-integer-linear-pro
section_title: "Dimension Reduction for Mixed-Integer Linear Programs"
section_number: null
pages: 37-44
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Programs
Throughout this section we consider a mixed-integer linear program given by a
linear programF(A,b,ℓ,u,c)withA∈R V×W ,b∈R V,ℓ,u,c∈R W and integer
variablesW I ⊆W. For any partitionQofWthat is compatible withW I, we use
QI :={Q∈Q|Q⊆W I}to denote the corresponding partition over the integer
variables.
Let us consider the effect of DRCR in context of mixed-integer linear programs. For
the mixed-integer linear program given byF(A,b,ℓ,u,c)and integrality constraints
x∈MI WI, we consider thereduced problemR P,Q(F(A,b,ℓ,u,c))with integrality
constraintsy∈MI QI fory∈R P,Q(F(A,b,ℓ,u,c)). For the linear programming
relaxations, Proposition 3 establishes a correspondence between the original and
the reduced problem. Let us consider how these mappings interact with integrality.
For a solutionx∈F(A,b,ℓ,u,c)∩MI WI, we can observe thaty := Π ⊺
Qxsatisfies
the integrality constraints for the reduced problem, since theny Q := P
w∈Qxw
is integral for anyQ∈ Q I as it is the sum of integral values. Linear feasibility
and optimality are guaranteed already by Proposition 3. Thus, every mixed-integer
solution for the original problem maps to a mixed-integer solution of the reduced
problem. However, for the other direction integrality is not preserved, since for
y∈R P,Q(F(A,b,ℓ,u,c))∩MI QI the original solution is given forw∈Wwithw∈Q
byx w := 1
|Q|yQ, which is not necessarily integral. In particular, this is an issue if the
reduced problem contains integer solutionsy∈R P,Q(F(A,b,ℓ,u,c))∩MI QI that
do not map to integer solutions of the original problem. Previous works on Orbital
Shrinking [8–10] deal with this limitation by solving a feasibility subproblem, which
checks if the provided mixed-integer solution for the reduced problem can be mapped
to a mixed-integer solution of the original problem. For any fixed mixed-integer
37
y-solution, these subproblems can be formulated by adding the constraintsΠ⊺
Qx=y
to the original MILP. This subproblem is a mixed-integer linear program of reduced
size with no objective, and the DRCR procedures defines a point that is feasible
for its LP relaxation. Frequently, this subproblem is solved using techniques such as
constraint programming that exploit the specific structure of the subproblem [9, 25].
In this work, we take a different approach compared to previous works on Orbital
Shrinking by characterizing when each solution of the reduced problem corresponds
to a solution of the original model. In terms of orbital shrinking, one can think of
our approach asExact Orbital Shrinking, where the orbital shrinking subproblem is
given by a perfect formulation of a mixed-integer linear program. In this case, the
orbital shrinking subproblem can be solved via linear programming. One of the main
advantages of our approach is that it guarantees a tight correspondence between the
mixed-integer solutions of the original and the reduced problem, and that the sub-
problems can be solved easily via linear programming. This correspondence comes at
a cost: the main downside of our approach is that it cannot handle all symmetries.
Due to the requirement that the subproblem is a perfect formulation, our approach
cannot in general handle the complete symmetry group of the MILP, and instead
only handles a subgroup of the symmetry group that generates subproblems that are
perfect formulations.
In Theorem 26, we characterize when reflection reductions, which generalize the
DRCR procedure, can be used to reduce the dimension of a mixed-integer linear
program.
Theorem 26Let(P,Q,γ,λ,δ,V U,WU)be a reflection reduction ofF(A,b,ℓ,u,c)such that
δ∈MI WI∩WU holds andWI∩WU is compatible withQ. We formulate the reduced mixed inte-
ger program usingA′ := Π⊺
PΓAVU,WU ΛgΠQ,b′ := Π⊺
PΓ(bVU−AVU,WUδWU ),ℓ′ := Π⊺
Qℓλ,δ
WU
,
u′ := Π⊺
Quλ,δ
WU
andc′ :=gΠQ
⊺
ΛcWU. If the following equation holds
conv({x∈P(A,b,ℓ,u)|(Π ⊺
QΛx)QI∈ZQI}) = conv(P(A,b,ℓ,u)∩MI WI )(13)
then the following hold:
(i) For anyx∈P(A,b,ℓ,u)∩MI WI, theny := Π⊺
QΛ(xWU−δWU )∈P(A ′,b′,ℓ′,u′)∩MIQI
andc ⊺x=c ′⊺y+c ⊺δhold.
(ii) For anyy∈P(A ′,b′,ℓ′,u′)∩MIQI there exists a solutionx∈P(A,b,ℓ,u)∩MI WI such
thatc ⊺x≤c ′⊺y+c ⊺δhold.
ProofFirst, consider the proof of the first point. By Definition 18(i), it follows thaty∈
P(A′,b′,ℓ′,u′)andc ⊺x=c ′⊺y+c ⊺δhold. Thus, it is sufficient to show thaty∈MIQI holds.
First, sincex∈MI WI andδ∈MI WI∩WU hold we have thatxWU−δWU∈MIWI∩WU. Then,
for anyQ∈Q I, we have thatyQ = (Π ⊺
QΛ(xWU−δWU ))Q = P
w∈Qλw(xw−δw). Since
Q∈Q I holds, it follows that allw∈Qsatisfyw∈W I. Thus, this implies thatxw andδ w
must be integral by the given conditions. Then, sinceλw is also integral, it follows thatyQ
is integral. Since this holds for anyQ∈QI, we havey∈MI QI.
38
We proceed with the proof of the second point. Lety∈P(A′,b′,ℓ′,u′)∩MIQI be given.
Then, by Definition 18(ii) we have forx′ := (ΛgΠQy,O) +δthatx ′ ∈P(A,b,ℓ,u)and
c′⊺y+c ⊺δ=c ⊺x′ hold. Then, we observe that for eachQ∈Q, we have the following for
Π⊺
QΛx′:
(Π⊺
QΛx′)Q =
X
w∈Q
λwx′
w =
X
w∈Q
λw(λwyQ
|Q| +δw) =
X
w∈Q
yQ
|Q| +λwδw =yQ +
X
w∈Q
λwδw.
Then, forQ∈Q I,y Q is integral by assumption, and allw∈Qlie inW I by definition,
which shows thatP
w∈Qλwδw is integral sinceδ∈MI WI∩WU holds. Thus, we have that
x′∈conv({x∈P(A,b,ℓ,u)|(Π ⊺
QΛx)QI∈ZQI})holds. By the equality in (13) we have that
x′∈conv(P(A,b,ℓ,u)∩MI WI )holds.Sinceconv(P(A,b,ℓ,u)∩MI WI )isa convexpolyhedron,
there exists somex∈P(A,b,ℓ,u)∩MI WI such thatc⊺x≤c ⊺x′ holds. Thenc ⊺x≤c ′⊺y+c ⊺δ
follows, which completes the proof.□
Theorem 26 differs from reflection reductions in a few subtle but important ways.
First of all, the new and crucial condition (13) in Theorem 26 states for each part
Q∈Q I that the integrality of all variables inQmust be implied by the integrality of
the sumP
w∈Qλwxw∈Z. We will later elaborate on a few different methods to detect
this fact. Additionally, note that the partitionQmay not have parts that contain
both integer and continuous variables and thatδWI∩WU must be integral.
In the second point of Theorem 26 we only show existence of a better solution in
the original problem, rather than proving that a direct mapping exists, as was done in
Proposition 3. This is due to the fact that the mapped solution,x′ in the proof, does
not necessarily satisfy all the integrality constraints forWI, even though it is feasible
for the linear relaxation. This raises an important issue; it is not yet clear how, given
arbitraryx′∈P(A ′,b′,ℓ′,u′), if one can obtain in polynomial time a solution solution
xto the original problem that also satisfies the integrality constraints. Intuitively,
one may suspect that it is sufficient to consider the affine subspace generated by
x= Π ⊺
QΛ(xWU−δWU )in the original problem and recover an original solution. This
approach is also taken in Orbital Shrinking [10]. However, we show in Example 27
that it may be the case that there exists no solutionx∈P(A,b,ℓ,u)∩MI WI such
thatx ′ = Π ⊺
QΛ(xWU−δ WU )holds, even though the conditions of Theorem 26 and
x′∈MIQI hold. This fact is an important limitation for Orbital Shrinking [10] as it
may be difficult to recover integral solutions for the original integer program.
Example 27Consider the integer program given by polyhedronP={(x,y)∈R 2|−x+2y≤
2,2x−y≤2,x≥0,y≥0}andx∈Z,y∈ZandnotethatP= conv(P∩Z 2) = conv({(x,y)∈
P|x+y∈Z})holds and that Theorem 26 is applicable to the standard representation of
the integer program, whereλ=γ=1,V U =VandW U =Whold. See Figure 1a for the
geometric representation ofP. For the reduced integer programP′ ={z∈R|z≤4,z≥
0}∩Z,z= 3is a feasible integer solution. However, there exists no solution(x,y)∈Psuch
thatx+y= 3,x∈Zandy∈Zhold.
Finally, Theorem 26 clarifies the need to prove the variant of Proposition 3 com-
pared to that in [11]. In [11], the mapping from the original to the reduced problem
is scaled, which makes it so that integrality of the original solution does not imply
39
(a)Pfrom Example 27 (thin) and its sub-
set induced byx+y= 3(thick).
(b) A symmetric integral polyhedronP
(thin) with a totally unimodular con-
straint matrix whosexandyfibers are
integral, but for which the fiber defined by
x+y= 2(thick) is not integral.
Fig. 1: Examples of symmetric integral polyhedra with non-integral affine fibers
integrality of the mapped solution in the reduced problem. Instead, we require the
scaling as in Proposition 3 in Theorem 26 to ensure that we can map integral solu-
tions between the original and the reduced problem. A similar scaling is also used in
Orbital Shrinking [10].
Next, we will consider several methods to detect that (13) is satisfied. For each
method, we additionally show that a solution to the original problem can be recovered
in polynomial time from a solution to the reduced problem.
First, we show in Lemma 28 that an equitable partition where each integer variable
is contained in its own part of size1satisfies (13). This result seems to already be
known as a folklore result within the integer programming solver community1, but to
the best of our knowledge it was never documented in public. This idea also extends
naturally to reflection reductions.
Lemma 28Ifδ∈MI WI and if for eachw∈W I,{w}∈Qholds, then(13)is satisfied.
Additionally, for everyy∈P(A ′,b′,ℓ′,u′)∩MIQI,x′ := (ΛgΠQy,O) +δlies inP(A,b,ℓ,u)∩
MIWI.
ProofFor the first point, note that(Π ⊺
QΛx)QI ∈ZQI ⇐⇒(Λx) WI ∈Z WI ⇐⇒x WI ∈
ZWI holds, where the first equivalence follows since everyw∈WI is a part of size one. The
second equivalence holds sinceΛis a unimodular matrix. Thus, this directly establishes that
(13) holds.
For the second point, note that for all{w}=Q∈ Q I,x w = ((ΛgΠQy,O) +δ) w =
λwyQ +δw holds since|Q|= 1holds. The latter expression is integral sincey Q,δ w andλ w
are all integral, which shows thatx∈MI WI. By Definition 18(ii),x∈P(A,b,ℓ,u)holds,
which completes the proof.□
ItisimplicitinLemma28thatallbipolarpartsmustconsistofcontinuousvariables
only by the condition that eachw∈WI has{w}∈Q. This condition is not required
in Theorem 26.
1Developers of both Gurobi and FICO Xpress mentioned this idea in personal communication.
40
The condition in Lemma 28 that each integer variable is in its own partition class
can be easily enforced during detection by modifying the initial partitionQ0 of the
refinement algorithm. The condition also implies a strong condition on the rows by
the requirement that the partition is equitable for the constraint matrix. In particu-
lar, this implies that for anyP∈PthatA v1,w =A v2,w holds for anyv1,v 2∈Pand
w∈W I. In other words, for any two rowsv1,v 2 that are in the same row partition,
the rows must be identical in the column submatrixA⋆,WI. Another perspective is
that we are considering DRCR for a parametric set of LPs, whose right-hand sides
depend on the fixed integer values for thexWI variables. Since the right-hand sides
for two rows in the same row-block need to be identical under all fixed integer values
ofx WI, their rows inA⋆,WI must be identical.
Although Lemma 28 is very useful, the detection of (13) is mostly seen as an
afterthought and is done by making the partition much finer. Thus, we investigate
more sophisticated methods to detect (13) which do not require every integer variable
to be in its own part, so that we may also aggregate integer variables. In the context
of detecting equivalent mixed-integer formulations as we have in (13), there are two
works that are relevant to the current work. Recall that a matrixAis said to be
totally unimodularifdet(A ′) =±1holds for every nonsingular square submatrixA′ of
A. A famous result by Hoffman and Kruskal [43] shows that{x∈Rn|Ax≤b,x≥0}
defines an integral polyhedron for allb∈Z m if and only ifAis totally unimodular.
First of all, the author has previously investigated the phenomenon ofimplied inte-
grality[29], which is said to occur whenconv(P∩MIW ) = conv(P∩MI W′
)holds for
someW ′⊆W. There, implied integrality is detected by detecting totally unimodular
submatrices within the constraint matrix.
In their work, Bader, Hildebrand, Weismantel and Zenklusen [30] investigate meth-
ods to detect matricesT∈Z k×n wherek < nsuch thatconv({x∈P|Tx∈
Zk}) = conv(P∩Z n)holds. They investigate the case whereTis totally unimodu-
lar and formulate the notion of anaffine totally unimodular decomposition(affine TU
decomposition) to detect such cases.
Definition 29(Bader, Hildebrand, Weismantel & Zenklusen[30])A matrixA∈Z m×n
admits ak-row affine totally unimodular decompositionif there exist matricesS∈Z m×n,
U∈Z m×k andT∈Z k×n such that
S
T

is totally unimodular andA=S+UTholds.
In particular, they show that affine TU decompositions can be used to remove and
reformulate integrality constraints.
Proposition 30([30])LetA=S+UT∈Z m×n withT∈{−1,0,1} k×n be ak-row affine
TU decomposition andb∈Z m andℓ∈(Z∪{−∞}),u∈(Z∪{∞}withℓ≤u. Then for
P={x∈R n|ℓ≤x≤u,Ax≤b}it holds thatconv({x∈P|Tx∈Z k}) = conv(P∩Z n).
41
Note that the matrixΠ⊺
QΛin (13) is totally unimodular as it contains at most one
±1entry in every column. Thus, the notion of an affine TU decomposition is very
suitable for our setting.
One idea which is central to the proof of Proposition 30 and the detection of
implied integrality, is to show that everyfiberdefined by a linear subspace ofPgiven
byTx=dfor somed∈Z Q is (mixed)-integral. Although this is not a necessary
condition for the possibility of a mixed-integer formulation (see Fig. 1a), it is practical
to detect and exploit this condition. In our setting, imposing the requirement that the
fibers have to be integral has the additional benefit that an integral solution to the
original problem may be recovered in polynomial time, avoiding the issue in Figure 1a.
We adapt Lemma 31 from the proof of Proposition 30 in [30] to work in a slightly
more general mixed-integer setting.
Lemma 31(Generalized from [30])LetP⊆R W be a rational polyhedron, letWI ⊆W
denote the integer variables. LetT∈Z k×WI be any integral matrix and consider the affine
fiberH d :={x∈P|Tx WI =d}for any fixedd∈Z k. IfHd isW I-integral for everyd∈Z k,
thenconv({x∈P|Tx WI∈Zk}) = conv(P∩MI WI )holds.
ProofLetG := conv({x∈P|Tx WI∈Zk}). First, we show thatGis a rational polyhedron.
This is relatively easy to see, since it is the projection of the rational mixed integer program
given byG′ := conv({(x,d)∈MI WI×Zk|x∈P, Tx WI =d}). By Meyer’s theorem [44],
G′ is a rational polyhedron. Then, since the projection of a rational polyhedron is again a
polyhedron andG= proj x(G′),Gis also a rational polyhedron.
Then the following holds:
G= conv({x∈P|Tx WI∈Zk}) = conv(
[
d∈Zk
Hd)
(a)
= conv(
[
d∈Zk
conv(Hd∩MIWI ))
= conv(
[
d∈Zk
Hd∩MIWI )
(b)
= conv(P∩MI WI ).
The equality in (a) follows from the fact thatHd isW I-integral. For (b) note thatTis an
integral matrix, which implies for allx∈MIWI thatTx WI =dholds for somed∈Z k. Then,
the equalityS
d∈ZkHd∩MIWI =P∩MI WI holds since anyx∈P∩MI WI must be contained
inH d∩MIWI for somed∈Z k, which implies thatP∩MI WI ⊆S
d∈ZkHd∩MIWI holds.
The reverse inclusion follows easily sinceHd⊆Pholds.□
Then, using Lemma 31, we show that one can recover solutions to the original
problem from solutions to the reduced problem in polynomial time.
Theorem 32Consider the setting of Theorem 26 and letQ′⊆Q I. If for eachd∈Z Q′
,
Hd :={x∈P(A,b,ℓ,u)|(Π ⊺
QΛx)Q′ =d}is anMI WI-integral polyhedron then(13)holds
andH ′
d′ :={y∈P(A ′,b′,ℓ′,u′)|y Q′ =d′}is aQ I-integral polyhedron for eachd′∈ZQ′
.
Moreover, for everyy∈P(A ′,b′,ℓ′,u′)∩MIQ′
there exists a feasible solutionx∈Hdy∩MIWI
withd y := (y+ Π ⊺
QΛδWU )Q′ that can be found in polynomial time, wherec⊺x≤c ′⊺y+c ⊺δ
holds.
42
ProofForG=P(A,b,ℓ,u), we have that
{x∈G|(Π ⊺
QΛx)Q′∈ZQ′
}⊆{x∈G|(Π ⊺
QΛx)QI∈ZQI}⊆G∩MI WI,
where the first inclusion follows sinceQ ′ ⊆ QI holds and the latter inclusion since
(Π⊺
QΛx)QI∈ZQI holds for allx∈MI WI. Then, by monotonicity of the convex hull we have:
conv({x∈G|(Π ⊺
QΛx)Q′∈ZQ′
})⊆conv({x∈G|(Π ⊺
QΛx)QI∈ZQI})⊆conv(G∩MI WI ).
Since the conditions of Lemma 31 are satisfied forQ′, we have equality throughout, which
shows that (13) holds.
Secondly, lety∈P(A ′,b′,ℓ′,u′)∩MI Q′
be a feasible solution to the reduced problem.
By Definition 18(ii) it holds forx′ := (ΛgΠQy,O WB) +δthatx ′∈P(A,b,ℓ,u)andc ⊺x′ =
c′⊺y+c ⊺δ. Then, we have forQ∈Q′ that:
(Π⊺
QΛx′)Q =
X
w∈Q
λwx′
w =
X
w∈Q
λw(λw
yQ
|Q| +δw) =yQ+
X
w∈Q
λwδw = (y+Π ⊺
QΛδWU )Q =dy
Q,
whered y
Q is integral by integrality ofyQ,Λandδ WI∩WU. Note that we implicitly use that
Q⊆W U holds, which is implied byQ∈Q′. Since this holds for anyQ∈Q′, it follows that
x′∈H dy holds. SinceH dy isW I-integral and nonempty sincex′∈H dy holds, the linear
programmin{c ⊺x|x∈H dy}contains a solutionx∈H dy∩MIWI in its minimal face such
thatc ⊺x≤c ⊺x′. Such a solution can be found in polynomial time using the ellipsoid method
[45], see [46] and [47] for an explanation on how the optimal minimal face can be identified.
Proposition 6.1 in [29] provides a proof of howxcan be determined from the minimal face
in polynomial time. Furthermore, note thatc⊺x≤c ⊺x′ =c′⊺y+c ⊺δholds.
Finally, let us show thatH ′
d′ is anQ I-integral polyhedron for anyd ′ ∈Z Q′
. First,
note that we obtainedP(A′,b′,ℓ′,u′)through the affine mapκ:R WU →R Q defined as
κ(xWU ) := Π⊺
QΛ(xWU−δWU)that was applied toP(A,b,ℓ,u). Thus, the preimage ofH′
d′ in
P(A,b,ℓ,u)consists of thosex∈P(A,b,ℓ,u)such that(Π ⊺
QΛ(xWU−δWU ))Q′ =d′. Then,
ford :=d′ + (Π⊺
QΛδWU )′
Q the preimage ofH′
d′ is exactlyHd. As we have|Q|≤|WU|,κis a
surjective affine transformation and standard theory shows that the preimage of any faceF′
ofH′
d′ contains some minimal faceFofH d (see e.g. [48, Lemma 7.10]). SinceHd isMI WI-
integral, there exists somex∈F∩MI WI. Then, note thaty := Π⊺
QΛ(xWU−δWU )∈MI QI
holds, which we show in the proof of Theorem 26(i). Then, sincey∈F ′ holds, it follows
that any minimal faceF ′ ofH ′
d′ contains aQ I-integral point, which shows thatH ′
d′ is
QI-integral. □
In Theorem 32, we also show thatH′
d is integral. By Lemma 31, this directly
implies thatconv(P(A ′,b′,ℓ′,u′)∩MI Q′
) = conv(P(A ′,b′,ℓ′,u′)∩MI QI )holds for
the reduced problem. Thus, any variablesQ∈ QI\Q′ are implied integer in the
reduced problem. One may hypothesize that the conditionQ′⊆Q I is unnecessary
and that the integrality of the fibers forQ′ implies the integrality for the fibers of
QI. The example in Figure 1b shows that this is not the case, and that the condition
Q′ ⊆Q I can indeed be helpful when the the fibers obtained by fixing the matrix
with respect toQI are not integral.
Given Theorem 32, we are motivated to investigate methods to determine when
the affine fibersH d are integral. Although Proposition 30 is useful for integer pro-
grams, we cannot apply it directly to mixed-integer programs, as they do not satisfy
its conditions. Thus, we generalize affine TU decompositions to mixed-integer linear
programs to deal with this limitation.
43
