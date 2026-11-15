---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-011-43-classification-of-fiber-functors-for-rephp
section_title: "Classification of fiber functors for Rep(Hp)"
section_number: 4.3
pages: 13-18
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
4.3. Classification of fiber functors for Rep(Hp). The only subgroups in Theo-
rem 3.6 are J = {e} and J = C2. The first gives the C2-orbits of fiber functors on Cp.
In the second, Corollary 3.7 requires an indecomposable rank-two Cp-module category
with a free transitive C2-action on its simples.
Lemma 4.1. The Tt-invariant indecomposable rank-two Cp-module categories are as
follows. If p ≡3 (mod 4), there are none. If p ≡1 (mod 4), there is exactly one
equivalence class.
Proof. With the convention fixed above, the map [µ] 7→Alt(µ) identifies H2(Ap, k×)
with the alternating bicharacters on Ap.
Tambara uses the reciprocal convention
in [Tam00, Proposition 2.6], which gives the same parametrization.
By [Nik08, Lemma 4.3], every indecomposable rank-two Cp-module category is of
the form
Nµ = ModCp(R(Ap, µ)),
where [µ]̸ = 0 in H2(Ap, k×). Since Ap has dimension two, every non-zero alternating
form on Ap is nondegenerate. Thus there is a unique λ ∈F×
p such that
Alt(µ) = λJ.
We first determine the equivalence class of Nµ. By [Nik08, Remark 4.5], restriction
to the pointed subcategory gives
Nµ|VecAp ≃M(Ap, µ) ⊕M(Ap, µ′),
where, if S is the matrix of the symmetric bicharacter χp, the automorphism ιµ defined
in that remark satisfies
λJ ιµ = S,
µ′(x, y) = µ−1(ιµ(x), ιµ(y)).
Since ιµ = −λ−1JS and STJS = det(S)J, we obtain
Alt(µ′) = ιT
µ(−λJ)ιµ = −det(S)
λ
J.
This is also the specialization of the translate formula in [MM12, Lemma 9.1]. For
the hyperbolic form χp,
S =

0
1
1
0

,
det(S) = −1,
and hence
Alt(µ′) = λ−1J.
Consequently, the restriction of Nµ is encoded by the unordered pair
{λ, λ−1}.
This unordered pair is a complete invariant. Indeed, an equivalence of Cp-module cat-
egories restricts to an equivalence of VecAp-module categories and therefore identifies
the two indecomposable summands, possibly after interchanging them. Conversely,
let x, y be the two simple objects of Nµ, with End(x) ≃R(Ap, µ). The restriction for-
mula identifies the neutral part of End(y) with R(Ap, µ′). The fusion rules in [Nik08,
14
C. GALINDO, C. GALLEGO, AND Y. MORALES
Lemma 4.3] give m⊗y ≃px, so the non-trivial graded component of End(y) vanishes.
Therefore
End(y) ≃R(Ap, µ′).
Internal-Hom reconstruction [Nik08, Section 2.1] now gives
Nµ ≃ModCp(R(Ap, µ′)) = Nµ′.
Since the cohomology class of a cocycle on Ap is determined by its alternating form,
the unordered pair is both necessary and sufficient. Thus the equivalence classes are
parametrized by
{λ, λ−1},
λ ∈F×
p .
The autoequivalence Tt, induced by t(x, y) = (y, x), sends Nµ to Ntµ. Since
tTJt = −J,
it sends λ to −λ. Hence Nµ is Tt-invariant if and only if
{λ, λ−1} = {−λ, −λ−1}.
As p is odd and λ̸ = 0, this is equivalent to
λ = −λ−1,
or equivalently
λ2 = −1.
If p ≡3 (mod 4), there is no solution. If p ≡1 (mod 4), the two solutions i and
−i determine the same unordered pair because i−1 = −i. Hence there is exactly one
Tt-invariant equivalence class.
□
Lemma 4.2. Let s denote the non-trivial element of the acting group C2; it acts on
Cp by Tt. In the semidirect product D = Cp ⋊C2, let
em = [m, s],
E∆= ⟨[a, e] (a ∈Ap), em⟩.
Then E∆is a Tambara–Yamagami fusion subcategory
E∆≃TY(Ap, eχp, p−1),
eχp(a, b) = χp(a, t(b)).
In coordinates,
eχp((x1, x2), (y1, y2)) = ξx1y1+x2y2.
Thus eχp is hyperbolic if and only if p ≡1 (mod 4).
Proof. Using the strict semidirect-product convention [X, g]⊗[Y, h] = [X⊗g∗(Y ), gh],
we obtain

a, e

⊗[b, e] = [a + b, e],

a, e

⊗em ≃em ≃em ⊗[a, e],
em ⊗em ≃
M
a∈Ap
[a, e].
Moreover, [a, e]∗= [−a, e] and em∗≃em. Thus E∆has Tambara–Yamagami fusion
rules.
FIBER FUNCTORS OF EQUIVARIANTIZATIONS
15
The action used to form the semidirect product is strict with identity tensor struc-
ture [Nik08, Proposition 2.10], so the relevant associators are inherited from Cp. For
a, b ∈Ap, they are
α [a,e], em, [b,e] = χp(a, t(b)) id em,
α em,[a,e], em =
M
b∈Ap
χp(a, t(b)) id[b,e],
(α em, em, em)a,b = p−1χp(a, t(b))−1.
Here we used that t preserves χp. These are precisely the associativity data of
TY(Ap, eχp, p−1),
eχp(a, b) = χp(a, t(b)).
In coordinates,
eχp((x1, x2), (y1, y2)) = ξx1y1+x2y2,
so eχp is represented by the identity matrix. It is hyperbolic precisely when x2
1+x2
2 = 0
has a nonzero solution, or equivalently when −1 is a square in Fp. This is equivalent
to p ≡1 (mod 4); if i2 = −1, the two Lagrangian lines are ⟨(1, i)⟩and ⟨(1, −i)⟩.
□
Proposition 4.3. Assume that p ≡1 (mod 4). The unique Tt-invariant indecompos-
able rank-two Cp-module category admits a C2-equivariant structure whose non-trivial
element acts freely on its two simple objects. Moreover, the case J = C2 contributes
exactly one equivalence class of fiber functors on CC2
p .
Proof. Let
D = Cp ⋊C2.
We use the faithful grading
K := Z/2Z × C2,
where the first factor is the Tambara–Yamagami grading of Cp and the second is the
semidirect-product grading. Put
∆= {(0, e), (1, s)} ⊂K,
γ = (0, s),
and let
E∆= D(0,e) ⊕D(1,s).
By Lemma 4.2,
E∆≃TY(Ap, eχp, p−1),
eχp(a, b) = χp(a, t(b)).
Since p ≡1 (mod 4), the form eχp is hyperbolic. If i2 = −1 in Fp, its two Lagrangian
lines are
L+ = ⟨(1, i)⟩,
L−= ⟨(1, −i)⟩.
Tambara’s classification [Tam00, Propositions 4.1 and 4.2] therefore gives exactly
two rank-one E∆-module categories, denoted N+ and N−, corresponding to the two
ordered decompositions Ap = L+ ×L−and Ap = L−×L+. Fix either one and denote
it by N.
Consider the induced D-module category
f
M := IndD
E∆(N) = D ⊠E∆N.
16
C. GALINDO, C. GALLEGO, AND Y. MORALES
By [Gal12, Propositions 3.5 and 3.7], the induced category is graded by the two right
cosets ∆and γ∆. Accordingly, as a right E∆-module category,
D = E∆⊕Dγ∆.
The object
u = [1, s] ∈Dγ
is invertible, and left tensoring by u gives an equivalence of right E∆-module categories
E∆−→Dγ∆,
X 7−→u ⊗X.
Consequently,
f
M ≃N ⊕N
as a semisimple category. In particular, f
M has exactly two simple objects, one in
each coset summand. The invertible object u exchanges these two summands, so f
M
is indecomposable as a D-module category.
Let
H = Z/2Z × {e} ⊂K;
DH = Cp.
The homogeneous component of degree (1, e) sends the coset ∆to (1, e)∆= γ∆and
conversely. Hence the action of the non-zero object [m, e] ∈D(1,e) sends either simple
object of f
M to a non-zero multiple of the other. It follows that
ResD
Cp( f
M)
is an indecomposable rank-two Cp-module category.
A module category over Cp⋊C2 is equivalently a C2-equivariant Cp-module category.
Thus the restricted module category is Tt-invariant, and Lemma 4.1 identifies it with
the unique such rank-two Cp-module category. Moreover, the non-trivial element of
C2 acts through u = [1, s], which exchanges the two simple objects. The action is
therefore free and transitive.
Since H2(C2, k×) = 0, Corollary 3.7 shows that its
equivariantization has rank one, and hence defines a fiber functor on CC2
p .
It remains to prove uniqueness in the case J = C2. Let M be any C2-equivariant
indecomposable rank-two Cp-module category whose non-trivial element acts freely
on simple objects, and regard M as a D-module category. Let x, y be its two simple
objects. By the fusion-rule calculation in [Nik08, Lemma 4.3], every a ∈Ap fixes
both x and y, whereas the non-invertible component of Cp interchanges them. Thus
the restriction of M to
D(0,e) = VecAp
has two indecomposable rank-one summands, generated by x and y. The degree (1, e)
component interchanges these summands, and so does the degree (0, s) component
because the given C2-action is free. Their product degree (1, s) therefore stabilizes
each summand. Hence the stabilizer in K of either VecAp-summand is precisely ∆.
The Clifford theorem for graded fusion categories [Gal12, Corollary 4.4] now gives
M ≃D ⊠E∆N,
FIBER FUNCTORS OF EQUIVARIANTIZATIONS
17
where N is a E∆-module category whose restriction to VecAp is one of the two rank-
one summands above. In particular, N itself has rank one, so it is equivalent to N+
or N−.
Finally, the coset degree γ = (0, s) normalizes ∆. Conjugation by u = [1, s] acts
on E∆by t on Ap and fixes em = [m, s]. Since
t(L+) = L−,
t(L−) = L+,
the translated module category
Dγ∆⊠E∆N+
is equivalent to N−as an E∆-module category. The equivalence criterion for induced
module categories [Gal12, Proposition 4.6] therefore implies
D ⊠E∆N+ ≃D ⊠E∆N−.
Thus the case J = C2 contributes exactly one equivalence class of fiber functors on
CC2
p .
□
Theorem 4.4. Let p be an odd prime, and let Hp be Nikshych’s semisimple Hopf
algebra of dimension 4p2, so that
Rep(Hp) ≃CC2
p
as tensor categories. Then Rep(Hp) has one equivalence class of fiber functors if p ≡3
(mod 4), and two equivalence classes of fiber functors if p ≡1 (mod 4).
Proof. Since every subgroup of C2 is cyclic, its second cohomology with coefficients
in k× is trivial. Hence Corollary 3.7 applies.
We distinguish the two possible subgroups J ⊆C2.
First let J = {e}.
In this case the relevant data are the fiber functors of Cp,
modulo the action of C2. By Tambara’s classification, the two fiber functors of Cp =
TY(Ap, χp, p−1) correspond to the two ordered Lagrangian decompositions
Ap = L1 × L2
and
Ap = L2 × L1.
The involution t(x, y) = (y, x) exchanges L1 and L2, and hence exchanges these two
ordered decompositions. Therefore the case J = {e} contributes one equivalence class
of fiber functors on CC2
p .
Now let J = C2. Since H2(C2, k×) = 0, the rank-one condition in Corollary 3.7
requires a C2-equivariant indecomposable Cp-module category whose non-trivial ele-
ment acts freely and transitively on its simple objects. Thus the underlying Cp-module
category must have rank two.
If p ≡3 (mod 4), Lemma 4.1 shows that there is no Tt-invariant indecomposable
rank-two Cp-module category. Hence the case J = C2 contributes no fiber functor,
and the single class from the case J = {e} is the whole list.
If p ≡1 (mod 4), Proposition 4.3 shows that the unique Tt-invariant indecompos-
able rank-two Cp-module category admits a C2-equivariant structure whose non-trivial
element acts freely on its two simple objects, and that the case J = C2 contributes
exactly one equivalence class of fiber functors.
18
C. GALINDO, C. GALLEGO, AND Y. MORALES
Finally, the two classes just obtained for p ≡1 (mod 4) are not identified with each
other: they come from the subgroups {e} and C2, respectively, and these subgroups
are not conjugate in C2. By Theorem 3.6, they therefore define distinct equivalence
classes. Thus Rep(Hp) ≃CC2
p
has one equivalence class of fiber functors if p ≡3
(mod 4), and two if p ≡1 (mod 4).
□
