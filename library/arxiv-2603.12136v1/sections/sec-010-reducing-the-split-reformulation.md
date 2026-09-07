---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-010-reducing-the-split-reformulation
section_title: "Reducing the split reformulation"
section_number: null
pages: 22-28
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Now that we have a good understanding of the equitable partitions of split refor-
mulations, we can consider how they can be used to reduce their dimension. In
this section, we consider a linear programF(A,b,ℓ,u,c)and its split reformulation
FS(A,b,ℓ,u,c). We apply Proposition 3 to the split reformulation using a symmetric
equitable partition(bP, bQ)to obtain a smaller linear program.
To clarify the effect of the symmetric equitable partition onFS(A,b,ℓ,u,c), we
partition the row and variable sets into 3 sets each. Letγ∈{−1,1}VU,λ∈{−1,1} WU
andPU andQU begeneratedbythesymmetricequitablepartition( bP, bQ).Weconsider
the corresponding partition ofbVand cWinto bVγ
U :=S
P∈bPγ
U
P, bV−γ
U :=S
P∈bP−γ
U
Pand
22
bVB.Similarly,thecolumnpartitionisdefinedby cWλ
U :=S
Q∈bQλ
U
Q,cW−λ
U :=S
Q∈bQ−λ
U
Q
and cWB. Then, we consider the variable partition(bxcWλ
U
,bxcW−λ
U
,bxcWB
)for the split
reformulationFS(A,b,ℓ,u,c).Duetothesymmetricdefinitionof cM,rearrangingofthe
variablescWinto cWλ
U andcW−λ
U can be achieved by multiplying byΛ:= diag(λ)from
the right. Similarly, rearrangingbVinto bVγ
U and bV−γ
U can be achieved by multiplying
byΓ := diag(γ)from the left. Furthermore, we remark that rowsv∈ bVB have right-
hand side0and that variablesw∈W B have objective0and have identical bounds
uw =−ℓ w forw + andw− by Lemma 12.
To denote the variable bounds for the unipolar variables, we define thebound
selector vectorbs(ℓ,u,λ)∈R W such that thatbs(ℓ,u,λ)w :=
(
uw ifλ w = 1
−ℓw ifλ w =−1. By
permuting the variables ofFS(A,b,ℓ,u,c)and applying the mentioned substitutions,
we obtain the following linear program:
minc ⊺
WU ΛbxcWλ
U
−c ⊺
WU ΛbxcW−λ
U
(7a)


ΓA1Λ−ΓA 1Λ cM1
−ΓA1Λ ΓA 1Λ− cM1
cM2 −cM2 cM3




bxcWλ
U
bxcW−λ
U
bxcWB

 =


ΓbWU
−ΓbWU
O

 (7b)
O≤bx cWλ
U
≤bs(ℓ,u,λ) WU (7c)
O≤bx cW−λ
U
≤bs(ℓ,u,−λ) WU (7d)
O≤bx cWB
≤

uWB
uWB

(7e)
where we useA1 :=A VU,WU, cM1 := Γ
AVU,WB −AVU,WB

, cM2 :=
 AVB,WU
−AVB,WU

Λand
cM3 :=
 AVB,WB −AVB,WB
−AVB,WB AVB,WB

.
We useby∈RbQ to denote the transformed variables, where we let(bybQλ
U
,bybQ−λ
U
,bybQB
)
be the reduced variable sets corresponding to the variables(bxcWλ
U
,bxcW−λ
U
,bxbQB
)in
FS(A,b,ℓ,u,c).
Then, we are almost ready to apply the equitable partition(bP, bQ)to (7). Since we
determined thatbPconsisted of the partitionsbPγ
U,bP−γ
U and bPB,Π bP is a block diagonal
matrix consisting of the blocksΠbPγ
U
,Π bP−γ
U
andΠ bPB
. Moreover, note that sincebPγ
U
and bP−γ
U arise from the same underlying partitionPU of the rowsVU, we have that
ΠbPγ
U
= Π bP−γ
U
= ΠPU. Similarly,Π bQ is a block diagonal matrix consisting of the
blocksΠ bQλ
U
,Π bQ−λ
U
andΠ bQWB
, whereΠ bQλ
U
= ΠbQ−λ
U
= ΠQU holds. In Corollary 10 we
observed that equitable bipolar parts have zero row and column sums. In Lemma 16,
we show that this implies that the matricescMi fori= 1,2,3transform into all-zero
matrices once we apply Proposition 3. Then, the reduction ofFS(A,b,ℓ,u,c)in the
reordered form (7) is given by (8).
23
Lemma 16Let( bP, bQ)be a symmetric equitable partition ofFS(A,b,ℓ,u,c), where cMis the
constraint matrix ofFS(A,b,ℓ,u,c). Then,Π ⊺
bPB
cMbVB,⋆ =Oand cM⋆,cWB
]ΠbQB
=Ohold.
ProofFor anyP∈ bPB and anyw∈Wwe have that:(Π ⊺
bPB
cMbVB,⋆)P,w =P
v∈P cMv,w = 0,
where the final equality follows from Corollary 10. Similarly, for anyQ∈bQB and anyv∈V
we have that(cM⋆,cWB
]ΠbQB
= 1
Q
P
w∈QcMv,w = 0holds by Corollary 10.□
min (gΠQu
⊺
ΛcWU )⊺bybQλ
U
−( gΠQu
⊺
ΛcWU )⊺bybQ−λ
U
(8a)


Π⊺
PU ΓA1Λ]ΠQU −Π⊺
PU ΓA1Λ]ΠQU O
−Π⊺
PU ΓA1Λ]ΠQU Π⊺
PU ΓA1Λ]ΠQU O
O O O




bybQλ
U
bybQ−λ
U
bybQB

 =


Π⊺
PU ΓbWU
−Π⊺
PU ΓbWU
O

 (8b)
O≤by bQλ
U
≤Π ⊺
QU bs(ℓ,u,λ) WU (8c)
O≤by bQ−λ
U
≤Π ⊺
QU bs(ℓ,u,−λ) WU (8d)
0≤bybQB
≤2Π ⊺
QBuWB (8e)
There are a few things to note about the system (8). First of all, the rows cor-
responding to the bipolar rows clearly become redundant, and the columnsby bQB
corresponding to the bipolar variables become independent of the other variables.
Indeed, (8a)-(8d) and (8e) are the Cartesian product of two polyhedra. SincebybQB
does not appear in the objective, we may arbitrarily fixbybQB
= 0. Furthermore, the
system (8a)-(8d) still has the redundancies introduced by the split reformulation of
F(A,b,ℓ,u,c). In fact, the linear program on the variablesbQλ
U∪ bQ−λ
U in (8a)-(8d) is
exactlythesplitreformulationofanotherlinearprogram!Onecanverifythat(8a)-(8d)
is equivalent to split reformulationGS of the following linear program:
G :=F(Π ⊺
PU ΓA1Λ]ΠQU,Π ⊺
PU ΓbWU,Π ⊺
QU bs(ℓ,u,λ) WU,−Π ⊺
QU bs(ℓ,u,−λ) WU, ]ΠQU
⊺
ΛcWU ).
Proposition 17Let( bP, bQ)be a symmetric equitable partition ofF S(A,b,ℓ,u,c), and let
λ,γ,PandQbe generated by( bP, bQ). Then the reduced linear program can be defined as:
R
bP,bQ(FS(A,b,ℓ,u,c)) :=GS×{bybQB
∈R
bQB|O≤by bQB
≤2Π ⊺
QB
uWB}.
ProofBy reordering the variables and rows ofFS(A,b,ℓ,u,c)according to the signsλandγ
for the unipolar variables we can obtain the form (7), where we implicitly use Lemma 12 to
show that bipolar rows have zero right-hand side and bipolar variables have zero objective
and identical upper and lower variable bounds.
Then, the reduced formRbP,bQ(FS(A,b,ℓ,u,c))is given by (8), where we use Lemma 16
to show that the bipolar rows and variables have only zero coefficients. Then, note that
the feasible region of the linear program (8) is exactly the Cartesian product ofGS and
{bybQB
∈R bQB |O≤by bQB
≤2Π ⊺
QB
uWB}on the unipolar and bipolar parts, respectively,
where we use that the all-zero rows with right-hand side zero in (8b) are redundant.□
24
Note that the linear programGis obtained fromF(A,b,ℓ,u,c)by taking the linear
program induced byVU andWU, scaling the rows and columns withΓandΛ, applying
the equitable partition(PU,QU)and then computing the split reformulation. Thus,
application of the symmetric equitable partition to the split reformulation can also be
viewed as taking the unipolar rows and variables in the original linear program, scaling
the rows and variables by±1factors, computing an equitable partition and then
applying the split reformulation. The final step that computes the split reformulation
is not helpful computationally, asGhas less variables thanGS and is equivalent to
GS. Thus, we wish to reduce the linear programs into the form ofG. We can obtain
Gfrom (8) by reversing the split reformulation as described in Lemma 7. We use
yQU :=bybQλ
U
−bybQ−λ
U
to define the variables ofG. Then,Gis given by the following
linear program.
min (gΠQu
⊺
ΛcWU )⊺yQU (9a)
Π⊺
PU ΓAVU,WU Λ]ΠQUyQU = Π⊺
PU ΓbWU (9b)
−Π⊺
QU bs(ℓ,u,−λ) WU≤yQU≤Π ⊺
QU bs(ℓ,u,λ) WU (9c)
Note thatGis obtained only through transformations that preserve the feasibility
and optimality of the linear program. In particular, both the split reformulation
and the dimension reduction via color refinement preserve feasibility and optimal-
ity. Thus, we can reduce any linear programF(A,b,ℓ,u,c)to the form ofGin (9)
through a series of reformulations.
One small assumption in our analysis was that we requiredℓ≤0andu w ≥
0to hold so that the split reformulations are well-defined. For any feasible linear
programℓ≤umust hold, and it is then possible to chooseδ∈R W such that
ℓ≤δ≤uholds. Then, one can apply an affine transformationx=x ′ +δto the
linear programF(A,b,ℓ,u,c). By doing so, one obtains the equivalent linear program
F(A,b−Aδ,ℓ−δ,u−δ,c), where the objective function has an additional constant
offset ofc ⊺δ. Clearly,ℓ−δ≤0andu−δ≥0hold, so the split reformulation is well
defined.
In Definition 18, we formulate the concept of areflection reduction, which rep-
resents the pair of linear programs given byF(A,b,ℓ,u,c)and its reduced form
obtained by computing a symmetric equitable partition ofFS(A,b−Aδ,ℓ−δ,u−δ,c)
for anyℓ≤δ≤u. In Theorem 19, we show that the symmetric equitable partitions
ofF S(A,b−Aδ,ℓ−δ,u−δ,c)imply the existence of a reflection reduction.
In order to simplify the notation, we definecomp(λ,δ,ℓ,u)∈R W to be a vector
such thatcomp(λ,δ,ℓ,u) w :=
(
ℓw−δw ifλ w = 1
δw−uw ifλ w =−1 holds for allw∈W, where
we define that∞+k=∞for all finitek∈Rand similarly that−∞+k=−∞.
The vectorcomp(λ,δ,ℓ,u)corresponds to the complemented variable lower bounds.
Note that swappingℓanduimmediately also gives the complemented variable upper
bounds usingcomp(λ,δ,u,ℓ). For the variable bound pair(ℓ,u), we will primarily use
25
the shorthand notationℓδ,λ := comp(λ,δ,ℓ,u)andu δ,λ := comp(λ,δ,u,ℓ). One can
verify thatℓδ,λ =−bs(ℓ−δ,u−δ,−λ)andu δ,λ = bs(ℓ−δ,u−δ,λ)hold.
Definition 18(Reflection reduction)Consider the linear programF(A,b,ℓ,u,c)withA∈
RV×W ,b∈R V,c∈R W and vectorsℓ,uwithℓ w∈R∪{−∞}andu w∈R∪{∞}such
thatℓ w≤u w holds for allw∈W. LetV U⊆VandW U⊆W, and defineW B :=W\W U.
Consider a partition(P,Q)wherePis a partition ofV U andQis a partition ofW U, and
letγ∈{−1,1} VU,λ∈{−1,1} Wu and letδ∈R W be such thatℓ≤δ≤uholds. Then,
defineA ′ := Π ⊺
PΓAVU,WU ΛgΠQ,b ′ := Π ⊺
PΓ(b−Aδ) VU,ℓ ′ := Π ⊺
Qℓλ,δ
WU
,u ′ := Π ⊺
Quλ,δ
WU
and
c′ :=gΠQ
⊺
ΛcWU. We say that(P,Q,γ,λ,δ,V U,WU)is areflection reductionofF(A,b,ℓ,u,c)
if the following hold.
(i) For everyx∈P(A,b,ℓ,u),y := Π ⊺
QΛ(xWU−δWU )is feasible forP(A ′,b′,ℓ′,u′)and
c⊺x=c ′⊺y+c ⊺δholds.
(ii) For everyy∈P(A ′,b′,ℓ′,u′),x := (ΛgΠQy+δ WU,δWB)is feasible forP(A,b,ℓ,u)and
c′⊺y+c ⊺δ=c ⊺xholds.
The main use of reflection reductions is that they show that one can equivalently
solve the linear programF(A′,b′,ℓ′,u′,c′)which has reduced dimension compared to
the original linear programF(A,b,ℓ,u,c). Then, our main result shows that symmet-
ric equitable partitions imply reflection reductions. Its proof relies strongly on the
equivalent linear programming relations defined by the split reformulation and the
DRCR reduction.
Theorem 19Consider the linear programF(A,b,ℓ,u,c)withA∈R V×W ,b∈R V,c∈R W
and vectorsℓ,uwithℓ w∈R∪{−∞}andu w∈R∪{∞}such thatℓ w≤u w holds for all
w∈W, and letδ∈R W be given such thatℓ≤δ≤uholds. Let( bP, bQ)be a symmetric
equitable partition ofFS(A,b−Aδ,ℓ−δ,u−δ,c), and letγ∈{−1,1} VU,λ∈{−1,1} WU,
PandQbe generated by( bP, bQ). Then,(P,Q,γ,λ,δ,V U,WU)is a reflection reduction of
F(A,b,ℓ,u,c).
ProofWe useΛ := diag(λ),Γ := diag(γ),A ′ := Π ⊺
PΓAVU,WU ΛgΠQ,b′ := Π ⊺
PΓ(b−Aδ) VU,
ℓ′ := Π⊺
Qℓλ,δ
WU
,u′ := Π⊺
Quλ,δ
WU
andc′ :=gΠQ
⊺
ΛcWU as in Definition 18.
First, let us prove Definition 18(i). Letxbe a feasible solution forF(A,b,ℓ,u,c). Then,
we have the following series of linear programs with feasible solutions:
xis feasible forF(A,b,ℓ,u,c)
(a)
=⇒x′ :=x−δis feasible forF(A,b−Aδ,ℓ−δ,u−δ,c)
(b)
=⇒bx:= (max(x′,O),max(−x ′,O))is feasible forF S(A,b−Aδ,ℓ−δ,u−δ,c)
(c)
=⇒by:= Π⊺
bQbxis feasible forR
bP,bQ(FS(A,b−Aδ,ℓ−δ,u−δ,c))
(d)
=⇒(bybQU
,bybQB
)is feasible forP S(A′,b′,ℓ′,u′)×{bybQB
∈R
bQB|O≤by bQB
≤2Π ⊺
QB
(u−δ) WB}
(e)
=⇒yQU :=bybQλ
U
−bybQ−λ
U
is feasible forF(A′,b′,ℓ′,u′,c′)
26
where (a) a holds by Proposition 5, (b) holds by Lemma 7(i) and (c) holds by Proposition 3(i).
The implication in (d) holds by Proposition 17, and (e) follows from Lemma 7 and since the
polyhedron for the bipolar variables is related only by the Cartesian product. ForQ∈QU,
consider that
yQ = (byQλ
U
)Q−(byQ−λ
U
)Q =
X
w∈Q
bxwλ−bxw−λ
(f)
=
X
w∈Q
λwx′
w,
where (f) follows since
bxwλ−bxw−λ =
(
max(x′w,0)−max(−x ′w,0)ifλ w = 1
max(−x′w,0)−max(x ′w,0)ifλ w =−1 =
(
x′w ifλ w = 1
−x′w ifλ w = 1 =λwx′
w.
Thus,y QU = Π ⊺
QU
Λx′
WU = Π ⊺
QU
Λ(xWU−δ WU )is feasible forF(A ′,b′,ℓ′,u′,c′), which
establishes the feasibility of Definition 18(i) for(P,Q,γ,λ,δ,V U,WU).
For the objective, we have
c⊺x−c ⊺δ
(g)
=c ⊺x′ (h)
=c ⊺(bx+
WU−bx−
WU )
(i)
=c′⊺(bybQλ
U
−bybQ−λ
U
)
(j)
=c′⊺y
where (g) follows from Proposition 5, (h) follows from Lemma 7(i) and the bipolar variables
having zero objective by Lemma 12, (i) follows from Proposition 3 and the reordering of the
variables described in Proposition 17 and (j) follows from Lemma 7(ii). This establishes the
objective in Definition 18(i).
To show Definition 18(ii), lety∈P(A′,b′,ℓ′,u)be a feasible solution. Then, we have the
following series of linear programs with feasible solutions.
yis feasible forF(A ′,b′,ℓ′,u′,c′)
(k)
=⇒bybQU
= (bybQλ
U
,bybQ−λ
U
) := (max(yQU,O),max(−y QU,O))is feasible forF S(A′,b′,ℓ′,u′,c′)
(l)
=⇒by:= (bybQU
,O bQB
)is feasible forP S(A′,b′,ℓ′,u′)×{bybQB
∈R
bQB|O≤by bQB
≤2Π ⊺
QB
(u−δ) WB}
(m)
=⇒byis feasible forR
bP,bQ(FS(A,b−Aδ,ℓ−δ,u−δ,c))
(n)
=⇒bx:=gΠbQbyis feasible forFS(A,b−Aδ,ℓ−δ,u−δ,c)
(o)
=⇒x′ :=bx+−bx− is feasible forF(A,b−Aδ,ℓ−δ,u−δ,c)
(p)
=⇒x :=x′ +δis feasible forF(A,b,ℓ,u,c)
Here, (k) follows from Lemma 7(i) and (l) holds since taking the Cartesian product
preserves feasibility and sinceOis clearly feasible. Moreover, (m) follows from Proposi-
tion 17, (n) follows from Proposition 3(ii), (o) follows from Lemma 7(ii) and (p) follows from
Proposition 5.
Next, let us expressyin terms ofx. Ifw∈W U holds, then we have the following for
Q∈Q U such thatw∈Q
x′
w =bxw+−bxw− = (gΠbQby)w+−(gΠbQby)w+
(q)
= λw
|Q|(byQλ−byQ−λ) = λw
|Q|yQ = (Λ ]ΠQUy)w
where (q) holds because we have by the reordering of the variables that
(gΠbQby)w+−(gΠbQby)w− =
( 1
|Q|(byQλ−byQ−λ)ifλ w = 1
1
|Q|(byQ−λ−byQλ)ifλ w =−1 = λw
|Q|(byQλ−byQ−λ).
27
Forw∈W B, then forQ∈ dQB such thatw∈Qwe have the following:
x′
w =bxw+−bxw− = (gΠbQby)w+−(gΠbQby)w− = 1
|Q|(byQ−byQ) = 0.
Note that this equation does not depend on the value ofbyQ, so in fact the choice to assign
yQB =Ois arbitrary as its values always cancel when they are transformed intox′
WB. Then,
we have thatx=x ′ +δ= (Λ ]ΠQUy,O) +δ= (Λ ]ΠQUy+δ WU,δWB), which shows that the
feasibility in Definition 18(ii) is satisfied. For the objective, we have similar reductions as in
the first part of the proof but in reverse order:
c′⊺y
(s)
=c′⊺(bybQλ
U
−bybQ−λ
U
)
(t)
=c′⊺x′
WU
(u)
=c ⊺x′ (v)
=c ⊺x−c ⊺δ,
where(s)followsfromLemma7(i),(t)holdsbytherelationbetweenbxandbythatweexplained
above, (u) holds since bipolar variables have zero objective by Lemma 12 and (v) holds by
Proposition 5. Then, the objective in Definition 18(ii) is also satisfied.
Thus, we have established that(P,Q,γ,λ,δ,VU,WU)satisfies Definition 18, which shows
that it is a reflection reduction ofF(A,b,ℓ,u,c).□
