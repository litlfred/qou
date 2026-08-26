---
doc_id: arxiv-math-0203003v2
doc_title: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in represe"
section_id: sec-002-2-exchange-representations
section_title: "Exchange Representations"
section_number: 2
pages: 4-8
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
doc_brief: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in representation the ory in t"
---
Let g be a ﬁnite dimensional simple Lie algebra, and ˆg the corresponding aﬃne Lie algebra. Let
q ∈ C∗, |q| ⁄= 1, and let Uq(ˆg) be the associated quantum aﬃne algebra (we will use the deﬁn ition
given in [EFK98]). Let Repf(Uq(ˆg)) be the category of ﬁnite dimensional (type 1) representat ions
of Uq(ˆg). For any V ∈ Repf(Uq(ˆg)) and z ∈ C∗ we can consider the shifted representation V (z)
where all the Chevalley generators act as before except for e0 and f0 which now act by ze0 and
z−1f0 respectively.
We will need the following theorem.
Theorem 2.1. (Kazhdan-Soibelman, [KS95], Section 5) Let V,W ∈ Repf(Uq(ˆg)), and RV W (z)
be the series obtained by evaluating the universal R-matrix in V (z) ⊗W . Then RV W (z) is an
analytic function near zero, that extends meromorphically to C.
We will give a new proof of this result (a bit simpler than the o ne in [KS95]) in the appendix.
Now let h denote a Cartan subalgebra of g, and ˆh = h ⊕ C the corresponding Cartan subalegbra
in ˆg. We denote the elements of ˆh∗ by ˆλ = (λ,k ). Then we can deﬁne the fusion matrix
JV,W (u, ˆλ) : V (e−2πiu ) ⊗W →V (e−2πiu ) ⊗W,
which is a formal power series in e2πiu with coeﬃcients being End( V ⊗W )-valued rational functions
of q(ˆλ,α i), where α i are the simple roots. (see [ES98] and also [EFK98]). Namely, let Mˆλ be the
Verma module over Uq(ˆg) with highest weight ˆλ, and let xλ be its highest weight vector. Let v ∈V
be a homogeneous vector, and Φ v
ˆλ (u) : Mˆλ →Mˆλ −weight(v) ˆ⊗V (z) be the intertwining operator such
that the matrix coeﬃcient ( x∗
ˆλ −weight(v), Φ v
ˆλ (z)xλ ) equals v (here x∗
ˆµ is the lowest weight vector of
M ∗
ˆµ ). Then for any homogeneous vectors v ∈V , w ∈W ,
JV,W (u, ˆλ) := (x∗
ˆλ −weight(v)−weight(w), (Φ v
ˆλ −weight(w)(e−2πiu ) ⊗ 1)Φ w
ˆλ (1)xλ ).
Let m be the ratio of the squared lengths of long and short root s of g (m = 1, 2 or 3), and h∨
be the dual Coxeter number of g.
Proposition 2.2. The coeﬃcients of the series JV,W (u, ˆλ) have an expansion into a power series
in p :=q−2m(k+h∨ ), and the sequence of these coeﬃcients tends to 0 in the p-adic norm.
Proof. This follows from the ABRR equation for the fusion matrix [ES 99] (which in our case is
equivalent the qKZ equation of Frenkel and Reshetikhin [FR9 2],[EFK98]).
Proposition 2.2 implies that one may consider the fusion ope ratorJV,W (ˆλ) := JV,W (0, ˆλ ), which
is a power series in p.
Proposition 2.3. The series JV,W (ˆλ) is convergent when |p| << 1, and the sum of this series
extends to a meromorphic function in the region {(λ,k ) : |p|< 1}.
Proof. This follows from the qKZ equation [FR92],[EFK98] and Theor em 2.1.
Now deﬁne the exchange matrix with spectral parameter
RV,W (u, ˆλ) = JV,W (u, ˆλ)−1R21
W,V (e2πiu )J 21
W,V (−u, ˆλ).
4
It follows by the arguments sketched above that both JV,W (u, ˆλ) and RV,W (u, ˆλ) are meromorphic
functions on C × U, where the open set U ⊂ ˆh∗ is deﬁned by the condition |q−2m(k+h∨ )| < 1.
Moreover, these arguments actually show that the divisor of singularities of these functions is a
union of hyperplanes of the form u −bk =c, <x,λ> −bk =c, where b,c ∈ C,x ∈ h.
Example 2.1. Let g = sln. When V = Cn, the formula for RV,V was obtained in [M01].
Theorem 2.4.
1. [ES99] The fusion matrix satisﬁes the dynamical twist equ ation
J 12, 3
V ⊗W,U (ˆλ)J 12
V,W (ˆλ −h(3)) = J 1, 23
V,W ⊗U (ˆλ)J 23
W,U (ˆλ) (2.1)
2. [ES98] For any three ﬁnite dimensional representations V1,V 2,V 3 ofUq(ˆg) the exchange matrix
satisﬁes the quantum dynamical Yang-Baxter equation
R12
V1,V 2(u1 −u2, ˆλ −h(3))R13
V1,V 3(u1 −u3, ˆλ)R23
V2,V 3(u2 −u3, ˆλ −h(1))
=R23
V2,V 3(u2 −u3, ˆλ)R13
V1,V 3(u1 −u3, ˆλ −h(2))R12
V1,V 2(u1 −u2, ˆλ). (2.2)
In particular, for any V ∈ Repf(Uq(ˆg)) the function RV,V (u, ˆλ) is a quantum dynamical
R-matrix with spectral parameter and step 1.
Remark: Strictly speaking, the last statement of the theorem contai ns an abuse of terminology,
since RV,V is a meromorphic function not on C × ˆh∗, but on its open subset C × U. In this paper,
we will ignore this terminological problem.
Let V be a ﬁnite dimensional representation of Uq(ˆg) and deﬁne RV = RV,V . It follows from
theorem 2.4 that for any W ∈ Repf(Uq(ˆg)), the pair ( W,R V,W (u, ˆλ)) is a representation of RV . It
is called the exchange representation of RV associated to W .
Now let us explain the main construction of this paper. Let V ∈ Repf(Uq(ˆg)). Denote by M
the ﬁeld of meromorphic functions on U and let MV ⊂ M be the subﬁeld of functions periodic
under the weights of V . Set C(V ) = Repf(Uq(ˆg)) ⊗CMV . It is easy to see then that the assignment
W → (W,R V,W ) provides an exact, faithful functor F V : C(V ) → Repf(RV ).
One of our main results is the following theorem, which shows that for a nontrivial V , the
category C(V ) (which is obtained from Repf(Uq(ˆg)) by extension of scalars) is a full subcategory
in Repf(RV ).
Theorem 2.5. The functor F V : C(V ) → Repf(RV ) is a tensor functor. Furthermore, if V is
nontrivial, then this functor is fully faithful.
Proof. We start with the following lemma.
Lemma 2.6.
R12
V,W (u, ˆλ −h(3))R13
V,U (u, ˆλ) = J 23
W,U (ˆλ)−1R1, 23
V,W ⊗U (u, ˆλ)J 23
W,U (ˆλ −h(1)) (2.3)
Proof. To shorten the notation we will write V [u] instead of V (e−2πiu ). Let R21
W,V [u] = R21|W ⊗V [u]
5
(analogously for other pairs of indices). Then
l.h.s. =J 12
V,W (u, ˆλ −h(3))−1R21
W,V [u]J 21
W,V (−u, ˆλ −h(3))J 13
V,U (u, ˆλ)−1R31
U,V [u]J 31
U,V (−u, ˆλ) =
J 12
V [u],W (ˆλ −h(3))−1R21
W,V [u]
(
J 21
W,V [u](ˆλ −h(3))J 13
V [u],U (ˆλ)−1
)
R31
U,V [u]J 31
U,V [u](ˆλ)
(2.1)
=
J 12
V [u],W (ˆλ −h(3))−1R21
W,V [u]
(
J 21, 3
W ⊗V [u],U (ˆλ)−1J 2, 13
W,V [u]⊗U (ˆλ)
)
R31
U,V [u]J 31
U,V [u](ˆλ) =
(
J 12
V [u],W (ˆλ −h(3))−1J 12, 3
V [u]⊗W,U (ˆλ)−1
)
R21
W,V [u]R31
U,V [u]
(
J 2, 31
W,U ⊗V [u](ˆλ)J 31
U,V [u](ˆλ)
) (2.1)
=
(
J 23
W,U (ˆλ)−1J 1, 23
V [u],W ⊗U (ˆλ)−1
)
R21
W,V [u]R31
U,V [u]
(
J 23, 1
W ⊗U,V [u](ˆλ)J 23
W,U (ˆλ −h(1))
)
= r.h.s.
The fourth equality is clear while the last follows from the h exagon axiom for the R-matrix.
Remark: A more general version of this lemma in the non-aﬃne situatio n is used in [EV00].
Now let us prove that F is a tensor functor. To do this, deﬁne the tensor structure
F V (W ) ⊙ F V (U ) → F V (W ⊗U ) to be given by
JW,U (ˆλ) : (W,R V,W ) ⊙ (U,R V,U ) → (W ⊗U,R V,W ⊗U )
It follows from Lemma 2.6 that JW,U is a morphism (in fact an isomorphism) and from (2.1) that
it satisﬁes the properties of a tensor structure on a functor , as required.
The rest of the section is dedicated to the proof of the full fa ithfulness of F in the case when
V is nontrivial.
Following the conventions of [EFK98], set L+
W (z) := R21
W,V (z).
Lemma 2.7. One has Hom Uq(ˆg)(W,U ) = {A ∈ HomUq(ˆh)(W,U ); L+
U (z)−1(1 ⊗A)L+
W (z) is of zero
weight in both components }.
Proof. It is clear that the ﬁrst space is a subspace in the second one. For the converse it is enough to
prove that, if A :W →U is such that L+
U (z)−1(1 ⊗A)L+
W (z) is of zero weight in both components,
then A ∈ HomUq(ˆg)(W,U ). To do this, recall that the universal R-matrix on modules w ith central
charge 0 can be written as
R =q
∑ xi⊗xi
(
1 +
∑
i≥0
(qi −q−1
i )ei ⊗fi +...
)
where xi form an orthonormal basis for h and the remaining terms are in Uq(ˆn+) ⊗Uq(ˆn−) and
correspond to other weights. This means that for nontrivial V , the condition that the expression
L+
U (z)−1(1 ⊗A)L+
W (z) is of zero weight in both components implies that A is of zero weight, and
fi|V ⊗ [ei,A ] = 0 ∀i ≥ 0 (one just needs to look at the terms corresponding to simple roots in the
expression of the universal R-matrix). It follows that [ ei,A ] = 0. Hence A is an interwiner over
Uq(ˆb+). But it is proved in Proposition 4.1.3 of [KS95] that the ima ges of Uq(ˆb+) and Uq(ˆg) in
the endomorphism algebra of any ﬁnite dimensional Uq(ˆg)-module are the same. Hence, A is an
intertwiner over the whole Uq(ˆg), as desired.
Let M(W,U ) := Hom Uq(ˆg)(W,U ) ⊗C MV be the space of morphisms between W and U in
the category C(V ), and let ~M(W,U ) := M(W,U ) ⊗MV M . Lemma 2.7 implies that ~M(W,U ) is
the space of solutions over M of the system of linear algebraic equations in ﬁnitely many v ari-
ables (entries of A), expressing the condition that L+
U (z)−1(1 ⊗A)L+
W (z) is of zero weight in both
components.
6
Now let N (W,U ) = Hom Repf(RV )(F (W ), F (U )). Below we will show that the space ~N (W,U ) :=
N (W,U ) ⊗MV M is contained in the space of solutions over M of a deformation of this system of
linear algebraic equations. This will imply that dim N (W,U ) ≤ dimM(W,U ), which immediately
implies that the injective map M(W,U ) → N (W,U ) deﬁned by F is actually an isomorphism, i.e.,
F is fully faithful.
To do this, we need the following lemma.
Lemma 2.8. Let LW,L U be the exchange operators RV,W ,R V,U and ~M ′(W,U ) = {A(ˆλ) ∈
HomUq(ˆh)(W,U ) ⊗CM ;LU (u, ˆλ)−1(1 ⊗A(ˆλ ))LW (u, ˆλ) is of zero weight in both components }. Then
the natural map ξ : N (W,U ) ⊗MV M → ~M ′(W,U ) is injective.
Proof. We need to show that any MV -linearly independent set {a1,...,a m} ⊂ N (W,U ) is also
linearly independent over M . Assume it is false and take a counterexample with the smalle st
length. We can assume that am =g1a1 + · · · +gm−1am−1 with gi ∈M but not all of them in MV .
Then
am(ˆλ −h(1)) = LU (u, ˆλ)−1(1 ⊗am(ˆλ))LW (u, ˆλ)
=
∑
gi(ˆλ)LU (u, ˆλ)−1(1 ⊗ai(ˆλ))LW (u, ˆλ) =
∑
gi(ˆλ)ai(ˆλ −h(1))
Let v ∈V be homogeneous of weight µ . Then, applying the last equality to v ⊗ Id, we have
am(ˆλ −µ ) =
∑
gi(ˆλ)ai(ˆλ −µ ) ⇔ am(ˆλ) =
∑
gi(ˆλ +µ )ai(ˆλ)
Hence, for some µ , ∑ (
gi(ˆλ) −gi(ˆλ +µ )
)
ai(ˆλ) is a non-trivial (since not all gi are in MV ) vanishing
linear combination of an even smaller length. Contradictio n.
Now it remains to prove that LW (u, ˆλ) is a deformation of L+
W (z), where z =e2πiu .
Let κ =k +h∨ and p =q−2mκ . We will write k → ∞ to mean p → 0 keeping q ﬁxed.
Lemma 2.9. Let JV,W (λ) be the fusion matrix corresponding to the the “ﬁnite dimens ional”
quantum group Uq(g). Then lim k→∞JV,W (u, ˆλ) = JV,W (λ).
Proof. Letv andw be homogeneous vectors in V and W respectively and consider the correlation
function [EFK98] ψ (z, ˆλ) = z∆ JV,W (u, ˆλ)(v ⊗w) where ∆ depends on the weights of v and w and
on ˆλ. It is easy to see that
ψ (z, ˆλ) = z∆ ∑
m≥0
ψ m(ˆλ)zm
and that ψ 0(ˆλ) = JV,W (λ)(v ⊗w). Furthermore, ψ satisﬁes the q-Knizhnik-Zamolodchikov equa-
tions, from which we get
ψ (pz, ˆλ) = R21
W,V (pz)qΛ
(2)ψ (z, ˆλ )
where Λ depends only on λ and the weights of v,w (not on k). Writing R21
W,V (z) = ∑
j≥0 R21
j zj we
ﬁnd
p∆ ∑
m≥0
ψ m(ˆλ)pmzm =
( ∑
j≥0
R21
j pjzj
)
qΛ
(2)
( ∑
i≥0
ψ i(ˆλ)zi
)
Actuallyp∆ is some constant c depending only on q,λ and the weights of v,w . We collect the term
in zl in both sides to get
(cpl − R21
0 qΛ
(2))ψ l =
l∑
m=1
R21
mpmqΛ
(2)ψ l−m
from where we conclude by induction that ψ l → 0 as k → ∞ for all l> 1, as stated.
7
Now assume that |q| < 1 and let λ → −∞ mean Re(λ,α i) → −∞ , where α i are the simple
roots. Then, by [EV00], JV,W (λ) → 1 as λ → −∞, and we conclude that LW (u, ˆλ) → R21
W,V (z) and,
therefore, LW (u, ˆλ) is a deformation of L+
W (z). One can proceed analogously for |q|> 1. Theorem
2.5 is proved.
