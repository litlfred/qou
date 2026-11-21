---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-006-141-pure-diﬀerence-modules-over-kwith-descent-da
section_title: "Pure diﬀerence modules over K∞with descent data"
section_number: 1.4.1
pages: 11-13
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
K∞denotes the algebraic closure of K and Gal denotes the Galois group
of K∞/K. Let M be a diﬀerence module over K∞. Descent data D for M
means a map σ ∈Gal →D(σ) satisfying:
D(σ) is a σ-linear bijection on M, D(σ) commutes with Φ,
D(σ1)D(σ2) = D(σ1σ2) and the stabilizer of any m ∈M, i.e., the group
{σ ∈Gal | D(σ)m = m}, is an open subgroup of Gal.
One associates to a diﬀerence module N over K the module M := K∞⊗
N with descent data given by D(σ)(f ⊗n) = σ(f) ⊗n for all f ∈K∞and
n ∈N. This induces a functor from the category of the diﬀerence modules
over K to the category of the diﬀerence modules over K∞provided with
descent data.
Proposition 1.9. — N →(K∞⊗N, D) is an equivalence of Tannakian
categories.
Proof. — The essential thing to prove is that any pair (M, D) is isomor-
phic to (K∞⊗N, D) for some diﬀerence module N over K.
Take a basis e1, . . . , er of M over K∞. Let the open subgroup H :=
{σ ∈Gal | σ(ej) = ej for all j} have index m in Gal. Then KH
∞= Km and
M H = Kme1 + · · · + Kmer. The cyclic group Gal/H = Gal(Km/K) acts
on M H. This action induces an element of H1(Gal(Km/K), GL(r, Km)).
By Hilbert 90, this cohomology set is trivial. It follows that M H contains
a basis f1, . . . , fr over Km, consisting of Gal-invariant elements. Now N :=
Kf1⊕· · ·⊕Kfr is equal to M Gal and the natural map K∞⊗K N →M is an
isomorphism. Since Φ commutes with the action of Gal, one has Φ(N) = N.
Thus N is a diﬀerence module over K and clearly induces the pair (M, D).
– 674 –
Galois theory of q-diﬀerence equations
The tensor product of two pairs (M1, D1), (M2, D2) is deﬁned as
(M1 ⊗K∞M2, D1 ⊗D2). We note that the tensor product D1(σ) ⊗D2(σ) of
two σ-linear maps makes sense. It is easily seen that the above equivalence
respects tensor products.
□
For a pure diﬀerence module N over K of slope λ, the module M =
K∞⊗N is also pure with slope λ and has the form K∞⊗C V , where V is
a ﬁnite dimensional C-vector space provided with an element A ∈GL(V ).
The action of Φ on M is given by Φ(f ⊗v) = zλφ(f) ⊗A(v).
The subspace V is not unique. By changing V , the eigenvalues of A are
multiplied by arbitrary, rational powers of q. We normalize A and V as
follows.
Choose a Q-linear subspace L ⊂C such that L ⊕Q = C. One requires
that every eigenvalue c of A has the form e2πi(a0(c)+a1(c)τ) with a0(c), a1(c) ∈
R and a1(c) ∈L.
After this normalization the subspace V of M is unique. Indeed, V is
the direct sum of the kernels of (z−λΦ −c)s with s >> 0 and c ∈C∗with
a1(c) ∈L.
We note that the use of this subspace L is somewhat artiﬁcial. It can
be avoided at the cost of verifying that formulas that we will produce are
independent of certain choices.
One observes that V is invariant under D(σ) for all σ ∈Gal. The group
Gal is identiﬁed with Z and the action of Gal is expressed by σ(zλ) =
e2πiλσzλ. For the operators A and D(σ), restricted to V , one ﬁnds the
equality AD(σ) = e2πiλσD(σ)A. Thus we have associated to a pure diﬀer-
ence module N over K a tuple data(N) := (λ, V, A, {D(σ)}) with
• λ ∈Q.
• V a vector space over C of ﬁnite dimension.
• A ∈GL(V ) with eigenvalues in the subgroup
{c = e2πi(a0(c)+a1(c)τ)|a0(c) ∈R, a1(c) ∈L} of C∗.
• a homomorphism σ ∈Gal ∼= Z →D(σ) ∈GL(V ) satisfying
AD(σ) = e2πiλσD(σ)A.
On the other hand an object (λ, V, A, {D(σ)}) as above deﬁnes a pure
module N over K of slope λ in the following way. Consider M := K∞⊗V
with Φ given by Φ(f ⊗v) = zλφ(f) ⊗A(v) and with descent data given by
D(σ)(f ⊗v) = σ(f) ⊗D(σ)v. Then N := M Gal.
– 675 –
Marius van der Put, Marc Reversat
Consider a morphism f : N1 →N2, f̸ = 0 between pure modules. Then
N1, N2 have the same slope λ and f induces a morphism from data(N1) to
data(N2), i.e., a linear map F between the two C-vector spaces equivariant
for the maps of the data. On the other hand, a C-linear map F, equivariant
for the maps of the data, comes from a unique morphism f : N1 →N2.
Thus N →data(N) is an equivalence between the category of the pure
modules over K and the category of tuples (λ, V, A, {D(σ)}) deﬁned above.
One observes the following useful properties.
For pure diﬀerence modules Ni with data(Ni) = (λi, Vi, Ai, {Di(σ)}) for
i = 1, 2 one has the nice formula
data(N1 ⊗N2) = (λ1 + λ2, V1 ⊗V2, A1 ⊗A2, {D1(σ) ⊗D2(σ)}).
Let the pure modules N have data(N) = (λ, V, A, {D(σ)}). Then the
dual module N ∗has data (−λ, V ∗, B, {E(σ)}), where V ∗is the dual of V ;
B = (A−1)∗and E(σ) = (D(σ)−1)∗.
The Φ-equivariant pairing N × N ∗→K, given by (n, ℓ) →ℓ(n) ∈K
translates for the data of N and N ∗into the usual pairing V × V ∗→C,
given by (v, ℓ) →ℓ(v) ∈C. This pairing is equivariant with respect to the
prescribed actions on V and V ∗.
