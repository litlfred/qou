---
doc_id: arxiv-math-0409393v1
doc_title: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS Jacques Sauloy"
section_id: sec-001-3-algebraic-summation
section_title: "Algebraic summation"
section_number: 3
pages: 15-25
source_pdf: 0409393v1.pdf
source_sha256: 2107d961f6065539
doc_brief: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS Jacques Sauloy — — The local analytic classiﬁcation of irregular linear q-diﬀerence equa- tions has recently"
---
3.1. The algorithm. — We keep the notations M0, A0, AU of 2.1.1 and 2.1.2 and
the corresponding conventions from section 2.1. Also, we shall, for 1 ≤ i < j ≤ k, use
the abreviation: µi,j = µi − µj ∈ N∗.
Deﬁnition 3.1 . — (i) A summation divisor adapted to A0 is a family (Di,j )1≤i<j≤k
of eﬀective divisors over the elliptic curve Eq, each Di,j having degree µi,j , the family
satisfying moreover the following compatibility conditio n:
∀i, l, j such that 1 ≤ i < l < j ≤ k , D i,j = Di,l + Dl,j .
Obviously, it amounts to the same thing to give only the k − 1 divisors Di,i +1, i =
1, . . . , k− 1.
(ii) We say that the adapted summation divisor (Di,j )1≤i<j≤k is allowed if it satisﬁes
the following conditions:
∀i, j such that 1 ≤ i < j ≤ k , ev Eq (Di,j ) ⁄∈(−1)µ i,j
Sp(Ai)
Sp(Aj) .
Here, for S, T ⊂ C∗, we put S
T = { s
t / s ∈ S, t ∈ T }; X and evEq were deﬁned in the
introduction.
16 J. SAULOY
Note that, for an adapted summation divisor, the condition of being allowed is a
generic one.
Example 3.2 . — A special case is that of an adapted summation divisor concen -
trated on a point α ∈ Eq, that is, each Di,j = µi,j [α]. Then the condition that D is
allowed is equivalent to:
∀i, j such that 1 ≤ i < j ≤ k , µ i,j α ⁄∈Sp(Ai) − Sp(Aj).
It is generically (that is, over a non empty Zariski open subs et) satisﬁed by α ∈ Eq.
Now, let ( Di,j )1≤i<j≤k be a summation divisor adapted to A0. We choose points
al ∈ C∗ for µk < l ≤ µ1 such that, for 1 ≤ i < j ≤ k,
Di,j =
∑
µ j <l≤µ i
[al].
These certainly exist. We then put:
ti = θµ k
q
∏
µ l<l≤µ i
θq, −al .
Lemma 3.3 . — (i) The functions t1, . . . , tk ∈ M(C∗) are such that:
(i1) For i = 1, . . . , k, σqti = αizµ iti, where αi ∈ C∗.
(i2) For 1 ≤ i < j ≤ k, divEq (ti) − divEq (tj) = Di,j (the notation is explained in the
course of the proof ).
(i3) For 1 ≤ i < j ≤ k, the function ti,j = σ qti
tj
belongs to O(C∗).
(ii)If the summation divisor (Di,j )1≤i<j≤k is moreover allowed, for 1 ≤ i < j ≤ k,
the spectra of αiAi and αjAj have empty intersection on Eq:
Sp(αiAi) ∩ Sp(αjAj ) = ∅.
Proof. -
It is an immediate consequence of the properties recalled in the intro duction that
these functions ti indeed satisfy (i1). Moreover, the functional equation implies that
the divisor divC∗ (ti) of zeroes and poles of ti on C∗ is invariant under the action of
qZ, so that it makes sense to consider it as a divisor div Eq (ti) on Eq (alternatively,
one can consider ti as a section of a line bundle over Eq and the notation is then
classical). Again because of the properties of theta-functions, o ne clearly gets (i2).
Assertion (i3) comes from the equalities:
ti,j = σqti
ti
× ti
tj
= αizµ i × a function with positive divisor .
The function θµ i
q
θq
θq,α i
satisﬁes the same functional equation as ti, which means that
their quotient is elliptic so that its divisor on Eq has trivial evaluation. Therefore:
divEq (ti) = (−1)µ i
αi
.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS17
The conclusion (ii) then follows from the deﬁnition of an allowed divisor. □
We now introduce a temporary and slightly ambiguous notation. For a n adapted
summation divisor D = ( Di,j )1≤i<j≤k, we write Θ D for the following block-diagonal
matrix:
Θ D =


t1Ir1 . . . . . . . . . . . .
. . . . . . . . . 0 . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . t kIrk


.
Of course, it does not only depend on D, but on a particular choice of the functions
t1, . . . , tk whose existence has just been established. However, the summat ion process
that we are deﬁning will produce a result that only depends on D. For a family of
recangular blocks U ′
I,j , we shall use the following abreviation:
A′
U ′ =


A′
1 . . . . . . . . . . . .
. . . . . . . . . U ′
i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . A ′
k


,
Lemma 3.4 . — (i) The eﬀect of the gauge transformation Θ D is to ”regularize” the
diagonal blocks of A = AU : Θ D[A] = A′
U ′ , where, for 1 ≤ i < j ≤ k, U ′
i,j = ti,j Ui,j ∈
Mri,r j (O(C∗, 0)) and, for i = 1 , . . . , k, A′
i = αiAi ∈ GLri(C). If moreover the
adapted summation divisor D is allowed, then, for 1 ≤ i < j ≤ k, Sp(A′
i)∩Sp(A′
j ) = ∅.
(ii) Suppose we started with AU in polynomial normal form. Then we get A′
U ′ such
that U ′
i,j ∈ Mri,r j (O(C∗)).
Proof. - The computations are immediate. □
We shall now take two matrices AU and AV in the formal class of A0, ﬂatten their
slopes through the gauge transformation Θ D, and then link the resulting matrices
A′
U ′ and A′
V ′ by an isomorphism deﬁned over C∗. This relies on the following
Proposition 3.5 . — (i) Let
A′
U ′ =


A′
1 . . . . . . . . . . . .
. . . . . . . . . U ′
i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . A ′
k


and A′
V ′ =


A′
1 . . . . . . . . . . . .
. . . . . . . . . V ′
i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . A ′
k


,
where, for i = 1 , . . . , k, A′
i ∈ GLri(C) are such that, for 1 ≤ i < j ≤ k, Sp(A′
i) ∩
Sp(A′
j) = ∅ and, for 1 ≤ i < j ≤ k, U ′
i,j , V ′
i,j ∈ Mri,r j (O(C∗, 0)). Then, there exists
18 J. SAULOY
a unique F ′ ∈ G(O(C∗, 0)) such that F ′[A′
U ′ ] = A′
V ′.
(ii) If , for 1 ≤ i < j ≤ k, U ′
i,j , V ′
i,j ∈ Mri,r j (O(C∗)), then F ′ ∈ G(O(C∗))
Proof. - We have to solve inductively the system of equations:
(
σqF ′
i,j
)
− A′
iF ′
i,j = V ′
i,j − U ′
i,j +
∑
i<l<j
V ′
i,l F ′
l,j −
∑
i<l<j
(
σqF ′
i,l
)
U ′
l,j .
The induction is the same as the one we met when buliding normal polyno mial forms.
The proposition then follows from the following lemma.
Lemma 3.6 . — (i) Let B ∈ GLs(C) and C ∈ GLt(C) be invertible complex matrices
such that Sp(B) ∩ Sp(C) = ∅. Then, for Y ′ ∈ Mt,s (O(C∗, 0)), the equation:
(σqX ′) B − CX ′ = Y ′
has a unique solution X ′ ∈ Mt,s (O(C∗, 0)).
(ii) If Y ′ ∈ Mt,s (O(C∗)), then X ′ ∈ Mt,s (O(C∗)).
Proof. - We write the Laurent series:
X ′ =
∑
n∈Z
X ′
nzn and Y ′ =
∑
n∈Z
Y ′
nzn.
By identiﬁcation, we obtain X ′
n = Φ −1
qnB,C (Y ′
n), where Φ qnB,C is the automorphism
M ↦→M (qnB) − CM of Mt,s (C); that it is indeed an automorphism comes from
the assumption that qnB and C have non intersecting spectra. For n → +∞,
Φ −1
qnB,C ∼ q−nΦ −1
B, 0 and, for n → −∞ , Φ −1
qnB,C → Φ −1
0,C . Taking ] r, R[×eıR to be the
annulus of convergence of Y ′, we conclude that the annulus of convergence of X ′ is
]r, |q|R[×eıR. Annuli of deﬁnition actually grow, again an illustration of the good
regularity properties of the homological equation. □
Putting it all together, we now get our ﬁrst fundamental theorem .
Theorem 3.7. — (i) Let AU , AV be deﬁned as above, in the formal class of A0.
Then, there exists a unique F ∈ G(M(C∗, 0)) such that F [AU ] = AV and, for 1 ≤
i < j ≤ k, div Eq (Fi,j ) ≥ −Di,j (the notation is explained in the course of the proof ).
(ii) If AU , AV are in polynomial normal form, F ∈ G(M(C∗)).
Proof. - We put A′
U ′ = Θ D[AU ] and A′
V ′ = Θ D[AV ], then F [AU ] = AV is equiva-
lent to F ′[A′
U ′ ] = A′
V ′, where F ′ = Θ DF Θ −1
D . The matrices F and F ′ together are
upper-triangular with diagonal blocks Ir1, . . . , Irk and their over-diagonal blocks are
related by the relations: Fi,j = tj
ti
F ′
i,j . This implies the unicity of F ∈ G(M(C∗, 0))
(resp. G(M(C∗))) subject to the constraint that the coeﬃcients of Fi,j belong to
tj
ti
O(C∗, 0) (resp. tj
ti
O(C∗)). Since divEq (ti) − divEq (tj) = Di,j , this proves (and
explains) the given condition. □
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS19
As a matter of notation, we shall write FD(U, V ) for the F obtained in the
theorem: it does indeed depend solely on D. We see it as the canonical resummation
of ˆF (U, V ) along the “direction” D. We shall write in particular FD(U ) = FD(0, U).
Let us call GD(M(C∗, 0)) (resp. GD(M(C∗))) the subset of G(M(C∗, 0)) (resp.
of G(M(C∗))) deﬁned by the constraints: for 1 ≤ i < j ≤ k, div Eq (Fi,j ) ≥ −Di,j .
Corollary 3.8 . — FD(U, V ) = FD(V )FD(U )−1.
Proof. - Actually, GD(M(C∗, 0)) = Θ DG(O(C∗, 0))Θ −1
D and GD(M(C∗)) =
Θ DG(O(C∗))Θ −1
D , so that these subsets are subgroups. Then the statement follo ws
from the unicity property in the theorem. □
Corollary 3.9 . — The conclusion of the theorem still holds if one only assumes that
U = (Ui,j ) ∈ ∏
1≤i<j≤k
Mri,r j (O(C∗, 0)).
Proof. - This immediately follows from corollary 2.10. □
Remark 3.10 . — It is not diﬃcult to prove that ˆF (U, V ) is the aymptotic expansion
of FD(U, V ) in the sense of section 2.2. One ﬁrst has to extend the deﬁniti ons so as
to allow for a pole at 0.The proof then proceeds in two steps.
1. First, one proves that, in its domain of deﬁnition, FD(U, V ) is a section of the
sheaf zdB for some d ∈ Z. This is done using only the functional equation that
it satisﬁes, and studying inductively its upper diagonal bl ocks Fi,j .
2. Then, one proves that the operator F ↦→ A−1
V (σqF ) AU , sends G(zdB) to
G(zd+1B). Starting from FD(U, V ) and iterating yields the conclusion.
Actually, in [15], a stronger result is proved. It relies on a reﬁned deﬁnition of asymp-
totics taking in account the position of poles; this is essen tial to get summation by
discrete integral formulas.
Remark 3.11 . — To give our theorem its functorial meaning, one should proce ed as
follows. One generalizes the construction of a vector bundl e FM from a q-diﬀerence
module M . This deﬁnes a ﬁbre functor ω over Eq. Then, for each D, if one restricts
to an appropriate subcategory of E (0)
1 , M↝ FD(M ) is an isomorphism from the ﬁbre
functor ω ◦ gr to ω. On the other hand, endowing FM with the ﬁltration coming from
that of M , one deﬁnes an enriched functor and the underlying principl e of all our
uses of the homological equation is that this functor is full y faithful. This is exploited
in [23].
3.2. Applications to classiﬁcation. —
20 J. SAULOY
One direction of summation . — Let AU , AV be deﬁned over C({z}). Suppose AU
and AV are analytically equivalent. Then the power series ˆF (U, V ) is convergent and
satisﬁes the conclusion of theorem 3.7, so that, by unicity, FD(U, V ) = ˆF (U, V ) for
any allowed summation divisor. Conversely:
Proposition 3.12 . — Suppose FD(U, V ) ∈ G(O(C∗, 0)). Then AU and AV are
analytically equivalent (and all the above holds).
Proof. - The gauge transform F = FD(U, V ) is obtained by solving the system of
equations:
z−µ j (σqFi,j ) Aj − z−µ iAiFi,j = Vi,j − Ui,j +
∑
i<l<j
Vi,l Fl,j −
∑
i<l<j
(σqFi,l ) Ul,j .
By induction, we are reduced to the following lemma:
Lemma 3.13 . — Let µ > µ ′ in Z, A ∈ GLr(C),A′ ∈ GLr′(C) and Y ∈
Mr,r ′(C({z})). Let X ∈ M r,r ′(O(C∗, 0)) be a solution of the equation:
(σqX) (z−µ ′
A′) − (z−µ A)X = Y.
Then, one actually has X ∈ M r,r ′(C({z})).
Proof. - Going to the Laurent series and identifying coeﬃcients, one ﬁnds:
∀n ∈ Z , q n+µ ′
Xn+µ ′ A′ − AXn+µ = Yn.
Since Y ∈ M r,r ′(C({z})), Yn = 0 for n << 0. Therefore, for n << 0, writing
d = µ − µ′ ∈ N∗, one has Xn = q−nAXn+dA′−1. Since |q| > 1, either Xn = 0 for
n << 0, or the coeﬃcients of X are rapidly growing for indices near −∞ prohibiting
convergence and contradicting the assumption that X ∈ M r,r ′(O(C∗, 0)). □
In order to make this a statement about classiﬁcation, we introduc e one more
notation. We write:
GA0
D (M(C∗, 0)) = {F ∈ GD(M(C∗, 0)) / F [A0] ∈ GLn(C({z}))}.
Clearly, the subset GA0
D (M(C∗, 0)) of the group GD(M(C∗, 0)) is stable under the
action by left translations of the subgroup G(O(C∗, 0)). Now, the above proposition
immediately entails:
Proposition 3.14 . — Mapping AU to FD(U ) yields a bijection:
F (M0) → G(O(C∗))/downslopeGA0
D (M(C∗, 0)).
□
This is strikingly similar to the corresponding “formal modulo analytic” description
in proposition 2.3.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS21
Varying the direction of summation . — Let D = ( Di,j )1≤i<j≤k be an allowed
summation divisor for M0, A0. We consider as its support and write Supp(D)
the union ⋃
1≤i<j≤k
Supp(Di,j ) and deﬁne the following Zariski open subset of Eq:
VD = Eq \ Supp(D). We also write UD for the preimage of VD in C∗. Thus, the
elements of GD(M(C∗, 0)) are holomorphic germs over ( UD, 0).
Now let D′ be another allowed summation divisor. Then, for any AU in the formal
class of A0, the gauge transformation FD,D ′ (U ) =
def
FD(U )−1FD′ (U ) sends A0 to
itself. It is holomorphic on the open subset ( UD ∩ UD′ , 0). We call UD,D ′ the sector
UD ∩ UD′, which is the preimage of the open subset VD,D ′ = VD ∩ VD′ of Eq. Note
that, if D and D′ have non intersecting supports (which is easy to realize), then UD
and UD′ cover C∗ and VD and VD′ cover Eq.
Lemma 3.15 . — FD,D ′ (U ) is a section of the sheaf Λ I (M0) over VD,D ′ .
Proof. - One only has to prove that the upper-diagonal part of F = FD,D ′ (U ) is
ﬂat. But its rectangular blocks satisfy: ( σqFi,j ) (z−µ j Aj) = ( z−µ iAi)Fi,j . This is a
pure system of slope µi,j > 0, hence Fi,j is indeed ﬂat by lemma 2.7. □
We now call U (resp. V) the covering of C∗ (resp. of Eq) by the open subsets UD
(resp. VD), where D runs among all the allowed summation divisors for A0, M0. The
following is immediate.
Corollary 3.16 . — The family (FD,D ′ (U ))D,D ′ is a Cech cocycle of the sheaf
Λ I (M0) for the covering V of Eq.
□
Proposition 3.17 . — Mapping AU to the cocycle (FD,D ′ (U )) deﬁnes a one-to-one
mapping:
F (M0)֒→Z 1(V, Λ I (M0)).
Proof. - If AU is analytically equivalent to AV , we have AV = F [AU ] for a unique
F ∈ G(C({z})) and it is clear (by unicity) that FD(V ) = F FD(U ) for all allowed
divisors D, whence FD,D ′ (V ) = FD,D ′ (U ) by immediate computation. This shows
that the above mapping is well deﬁned.
Conversely, just assume that FD,D ′ (V ) = FD,D ′ (U ) for two allowed divisors with
non intersecting supports. This equality gives FD(U, V ) = FD′ (U, V ). Hence, both
sides are holomorphic over UD ∪UD′ = C∗ (near 0), and we already saw in proposition
3.12 that this implies the analytic equivalence of AU and AV . □
We now come to the second fundamental result of this paper.
22 J. SAULOY
Theorem 3.18. — The above mapping yields a bijective correspondance:
F (M0) ≃ H 1(Eq, Λ I (M0)).
Proof. - Let AU and AV have the same image in H 1(Eq, Λ I (M0), hence in
H 1(V, Λ I (M0) (in Cech cohomology, the H 1 of a covering embeds into the direct
limit). There is, for each allowed divisor D, a matrix G(D) ∈ G(O(UD)) ∩ Aut(M0)
in such a way that:
∀D, D′ : FD,D ′ (U ) = ( G(D))−1 FD,D ′(V )G(D′).
One draws that FD(V )G(D) (FD(U ))−1 does not depend on D, so that it is holo-
morphic on ⋃ UD = C∗; call Φ their common value. As a gauge transformation, it
sends AU to AV . By proposition 3.12, AU and AV are analytically equivalent, which
proves the injectivity.
We now prove that our mapping from F (M0) to H 1(V, Λ I (M0)) is onto. For
that, we take (Φ D,D ′ )D,D ′ ∈ Z 1(V, Λ I (M0)). By deﬁnition of the sheaf Λ I(M0),
each component Φ D,D ′ is an element of G(O(UD,D ′ )), so that our cocycle can be
considered as describing a vector bundle over C∗, trivialized by the covering U and
with structural group in G. By [ 19], theorem 1.0 (see also [ 18]) it is trivial in the
following sense: there is, for each D, a Φ D ∈ G(O(UD)) in such a way that, for all
D, D′, Φ D,D ′ = Φ −1
D Φ D′ . Since the Φ D,D ′ are automorphisms of A0, the Φ D[A0] are
all equal to a same matrix AU ′ . Moreover, this is holomorphic over C∗. By corollary
2.10, there is a Ψ ∈ G(O(C∗, 0)) such that AU = Ψ[ AU ′ ] is meromorphic at 0. Then
ΨΦ D is holomorphic on ( UD, 0) and sends A0 to AU . Put GD = FD(U )−1ΨΦ D.
This is a section of Λ I(M0) over VD. The equalities FD(U )GD = ΨΦ D entail
Φ −1
D Φ D′ = G−1
D FD,D ′ (U )GD′ , that is, the cocycle (Φ D,D ′)D,D ′ is equivalent to the
cocycle ( FD,D ′ (U ))D,D ′ which ends the proof of our statement.
There remains to check that the natural mapping from H 1(V, Λ I (M0)) to
H 1(Eq, Λ I(M0)) is onto (we already said it was one-to-one). This is the content of
proposition 4.4, to be proved after the discussion on the q-Gevrey ﬁltration of the
Stokes sheaf the in next chapter. □
4. The q-Gevrey ﬁltration on the Stokes sheaf
The sources of inspiration for the contents of this chapter are [ 12], [ 1], [ 9], [ 25]
and [ 6].
4.1. The ﬁltration for the Stokes sheaf of a tamely irregular module. —
We stick to the conventions of section 2.1, in particular, the notatio ns of 2.1.1 and
2.1.2.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS23
Conditions of ﬂatness . — Let F be a section of the sheaf Λ I(M0). Then, for 1 ≤ i <
j ≤ k, the block Fi,j is solution of the equation:
σqFi,j
(
z−µ j Aj
)
=
(
z−µ iAi
)
Fi,j .
¿From this and lemma 2.7, we draw that Fi,j is ( µi − µj)-ﬂat and that, if it is t-ﬂat
for some t > µ i − µj, then it vanishes.
We now introduce a ﬁltration of the Stokes sheaf and a ﬁltration of t he sheaf of
its Lie algebras. For real nonnegative t, we call λt
I (M0) the subsheaf of λI (M0) made
of t-ﬂat sections and Λ t
I (M0) the subsheaf In + λt
I (M0) of Λ I (M0). The latter is a
sheaf of unipotent subgroups, while the former is the sheaf of its L ie algebras (see the
discussion in section 2.2). Both ﬁltrations are decreasing and exhau stive (the 0-term
is the total sheaf, the t-term is the trivial sheaf for t > µ 1 − µk).
¿From the previous argument, we see that λt
I (M0) has a very simple concrete
description in terms of matrices: its sections have non trivial blocks only over the
“curved over-diagonal” consisting of those ( i, j)-blocks such that µi − µj = t. There is
a similar description for Λ t
I(M0) (taking in account the block-diagonal of identities).
We shall however have use for a more intrinsic deﬁnition of these ﬁltr ations. We ﬁrst
describe the ﬁltration of λI (M0).
Proposition 4.1 . — (i) The sheaf λI (M0) is the sheaf of sections of the vector bun-
dle associated (see section 2.1) to the tamely irregular mod ule End>0(M0).
(ii) The above ﬁltration on the sheaf λI (M0) is the decreasing ﬁltration associated to
the graduation inherited from End>0(M0).
Proof. - We have M0 = P1 ⊕ · · · ⊕ Pk, whence:
End(M0) =
⨁
1≤i,j ≤k
Hom(Pj, Pi).
The internal Hom Hom(Pj , Pi) is a pure module of slope µi − µj. Therefore,
End>0(M0) is the sum of those Hom(Pj , Pi) such that µi > µ j, i.e. i < j .
On the other hand, the vector bundle associated to Hom(Pj , Pi) has as sections
on an open subset V of Eq the morphisms from Pj to Pi that are holomorphic on the
preimage U of V in C∗. This implies that the sheaf of sections of the vector bundle
associated to the module End>0(M0) is indeed λI (M0); that it is the direct sum of its
subsheaves λ(t)
I (M0), where λ(t)
I (M0) is the sheaf of sections of the pure vector bundle
associated to the pure module
End(t)(M0) =
⨁
µ i−µ j =t
Hom(Pj , Pi);
24 J. SAULOY
and that λt
I (M0) is the direct sum of the λ(t′)
I (M0) for all t′ ≥ t. □
Actually the whole structure only depends on the ﬁltrations and the properties of
internal Homs, so that it can be extended to an arbitrary tannakia n category.
Proposition 4.2 . — Let t be a nonnegative integer.
(i) Λ t
I (M0) is a sheaf of normal subgroups of Λ I (M0).
(ii) The map f ↦→1 + f induces an isomorphism:
λ(t)
I (M0) ≃ Λ t
I (M0)
Λ t+1
I (M0) .
Proof. - Actually, these are purely algebraic properties: for a nilpotent two sided
ideal I of a non commutative algebra A, the subgroups 1 + I t of the unit group
are normal and their successive quotients are isomorphic to the qu otient modules
I t/I t+1. □
We now are in position to reconstruct the Stokes sheaf by success ive exact se-
quences:
(4.2.1) 1 → Λ t+1
I (M0) → Λ t
I (M0) → λ(t)
I (M0) → 0.
Note also that, again from general algebraic considerations, we ha ve a sequence of
central extensions:
(4.2.2) 0 → λ(t)
I (M0) → Λ I(M0)
Λ t+1
I (M0) → Λ I (M0)
Λ t
I (M0) → 1.
4.2. Cohomological consequences. —
Lemma 4.3 . — Let V be a proper open subset of Eq. Then H 1(V, Λ I (M0)) is trivial.
Proof. - We apply theorem I.2 of [ 8] to the exact sequence 4.2.1. This gives an
exact sequence of pointed sets:
H 1(V, Λ t+1
I (M0)) → H 1(V, Λ t
I (M0)) → H 1(V, λt
I (M0)).
If the extreme terms are trivial, so must be the central one (this, by the very deﬁnition
of an exact sequence of pointed sets). The rightmost term is the ﬁ rst cohomology
group of a vector bundle (after proposition 4.1) over an open Riema nn surface. Such
a bundle being a trivial bundle, its H 1 is trivial. The leftmost term is trivial for
t > µ 1 − µk. By descending induction, the inner term is trivial for all t, hence for
t = 0. □
Proposition 4.4 . — The covering V is good.
ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR q-DIFFERENCE EQUATIONS25
This means that the map from H 1(V, Λ I (M0)) to H 1(Eq, Λ I (M0)) is an isomor-
phism. After [ 1], cor. 1.2.4, p. 113, this follows from the lemma. □
Note that this ends the proof of theorem 3.18.
4.3. The Stokes sheaf of a general module. — We brieﬂy sketch here how
the previous results extend to the Stokes sheaf of a module M . We take M in the
formal class of M0 and identify it with ( C({z})n, AU ), according to the conventions
of section 2.1.
The mapping Φ ↦→FD(U )Φ FD(U )−1 deﬁnes an isomorphism from Λ I (M0) to
Λ I (M ) over VD. Therefore, the two sheaves are locally isomorphic. Actually, the
latter is obtained from the former by the operation of twisting by th e cocycle
(FD,D ′ (U ))D,D ′ , described in [ 8], prop. 4.2 (also see [ 1], II.1 or [ 25], pp. 30-31).
