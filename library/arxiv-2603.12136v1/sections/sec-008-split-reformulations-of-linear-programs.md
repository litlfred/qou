---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-008-split-reformulations-of-linear-programs
section_title: "Split reformulations of linear programs"
section_number: null
pages: 14-15
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
In both papers [2] and [41], the authors reduce the problem of finding reflection
symmetries to finding permutation symmetries by adding both the original and the
complemented variables to the auxiliary graph used for symmetry detection. For linear
programs, a similar effect can be achieved by splitting each variablexasx=x+−x−,
wherex + represents the positive domain ofxandx − corresponds to the negative
domain ofx. We introduce the notion of asplit reformulationto achieve such a
reformulation.
Definition 6LetF(A,b,ℓ,u,c)be any linear program withA∈R V×W ,b∈R V,c∈R W
and vectorsℓ,uwithℓ w∈R∪{−∞}andu∈R∪{∞}for allw∈W. Ifℓ≤0andu≥0
hold, we define thesplit reformulationofF(A,b,ℓ,u,c)to be the following linear program
with variablesx +∈RW andx−∈RW:
minc ⊺x+−c ⊺x−
Ax+−Ax− =b
−Ax+ +Ax− =−b
0≤x +≤u
0≤x −≤−ℓ
(FS(A,b,ℓ,u,c)))
We useF S(A,b,ℓ,u,c)to denote the linear program that is the split reformulation of
F(A,b,ℓ,u,c), and we useP S(A,b,ℓ,u)to denote its feasible region. Furthermore, we use
cM=
 A−A
−A A

∈R (bV +∪bV−)×(cW +∪cW−), to denote the constraint matrix andbV := bV +∪bV−
and cW :=cW +∪cW− to denote the row and column index sets.
14
Note that the split reformulationF S(A,b,ℓ,u)includes the constraints
−Ax+ +Ax− =−b, indexed bybV2, which are redundant as they are directly implied
by negatingAx +−Ax− =b. Thus, they may be left out without changing the feasi-
ble region. Previous works do not consider the duplication of constraints. However,
we will see that these redundant equations may be useful for the derivation of coarse
equitable partitions. In particular, they may help to establish equitable partitions
that arise if a subset of the rows are multiplied by−1.
In Lemma 7, we show that the split reformulation of any linear program is
equivalent to its original linear program.
Lemma 7LetA∈R V×W ,b∈R V,c∈R W and vectorsℓ,u,withl w∈R≤0∪{−∞}and
uw∈R≥0∪{∞}for allw∈W. Then, the following hold:
(i) Ifx∈P(A,b,ℓ,u), then forx + := max(x,O)andx − := max(−x,O)it holds that
(x+,x−)∈P S(A,b,ℓ,u)andc ⊺x=c ⊺x+−c ⊺x−.
(ii) If(x +,x−)∈P S(A,b,ℓ,u)then forx :=x +−x− it holds thatx∈P(A,b,ℓ,u)and
c⊺x=c ⊺x+−c ⊺x−.
ProofTo prove (i), letx∈P(A,b,ℓ,u)be given and considerx + = max(x,O)andx − =
max(−x,O). Then, we have:
Ax+−Ax− =A(x +−x−) =A(max(x,O)−max(−x,O)) =Ax
(a)
=b,
where (a) follows sincex∈P(A,b,ℓ,u)holds. It follows directly that also−Ax + +Ax− =
−(Ax+−Ax−) =−bholds. Furthermore, note thatx +≥0andx −≥0hold by definition of
themaxoperator. The upper boundsx +≤uandx −≤−ℓfollow fromx≤uand−x≤−ℓ
which are satisfied sincex∈P(A,b,ℓ,u)holds. Then, sinceℓ≤0andu≥0, it follows that
(x+,x−)is feasible forPS(A,b,ℓ,u). Finally, note thatc⊺x=c ⊺(max(x,O)−max(−x,O)) =
c⊺x+−c ⊺x− shows that the objectives are equal.
To prove (ii), let(x+,x−)∈P S(A,b,ℓ,u)be given and considerx :=x +−x−. Then,
Ax=Ax +−Ax− =bholds since(x +,x−)∈P S(A,b,ℓ,u). Sincex +≥0andx −≥0hold in
PS(A,b,ℓ,u), we also have thatx=x +−x−≤u+O=uandx=x +−x−≥O−−ℓ=ℓ,
which shows thatℓ≤x≤uholds, and thus it follows thatx∈P(A,b,ℓ,u). Finally, we have
by definition ofxthatc ⊺x=c ⊺(x+−x−) =c ⊺x+−c ⊺x−.□
First of all, we note thatℓ≤0andu≥0are necessary conditions to guarantee
that the split reformulation exists in the proof of Lemma 7. For any linear programs
withℓ w≤u w for variablexw, one can achieve this by transformingxw intox′
w using
x′
w =x w +δw for anyδw that satisfiesℓw≤δ w≤u w. Ifℓw≤u w does not hold, then
the linear program is clearly infeasible.
For the detection of reflection symmetries, previous approaches detect reflection
symmetries by detecting permutation symmetries on a mixed-integer linear program
obtained from a split reformulation. Thus, a logical next step is to consider the
application of DRCR to a split reformulationFS(A,b,ℓ,u,c)for any linear program
F(A,b,ℓ,u,c)withℓ≤Oandu≥O. To do so, we first need to understand some of
