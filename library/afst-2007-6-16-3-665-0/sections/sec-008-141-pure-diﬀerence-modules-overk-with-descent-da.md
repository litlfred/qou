---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-008-141-pure-diﬀerence-modules-overk-with-descent-da
section_title: "Pure diﬀerence modules overK∞ with descent data"
section_number: 1.4.1
pages: 11-13
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
K∞ denotesthealgebraicclosureof K andGal denotestheGaloisgroup
of K∞/K. LetM be a diﬀerence module overK∞. Descent dataD for M
means a mapσ ∈Gal ↦→D(σ) satisfying:
D(σ)i sa σ-linear bijection onM,D(σ) commutes with Φ,
D(σ1)D(σ2)= D(σ1σ2) and the stabilizer of anym ∈ M, i.e., the group
{σ ∈Gal |D(σ)m=m}, is an open subgroup ofGal.
One associates to a diﬀerence moduleN overK the moduleM :=K∞ ⊗
N with descent data given byD(σ)(f ⊗n)= σ(f) ⊗n for allf ∈K∞ and
n ∈N. This induces a functor from the category of the diﬀerence modules
over K to the category of the diﬀerence modules overK∞ provided with
descent data.
Proposition 1.9.— N ↦→(K∞ ⊗N,D) is an equivalence of Tannakian
categories.
Proof.— The essential thing to prove is that any pair (M,D) is isomor-
phic to (K∞ ⊗N,D) for some diﬀerence moduleN overK.
Take a basise1,...,e r of M over K∞. Let the open subgroupH :=
{σ ∈Gal |σ(ej)= ej for allj} have indexm inGal. ThenKH
∞ =Km and
MH = Kme1 + ··· +Kmer. The cyclic groupGal/H = Gal(Km/K) acts
on MH. This action induces an element ofH1(Gal(Km/K),GL(r,Km)).
By Hilbert 90, this cohomology set is trivial. It follows thatMH contains
a basisf1,...,f r overKm, consisting ofGal-invariant elements. NowN :=
Kf1 ⊕···⊕ Kfr isequalto MGal andthenaturalmap K∞ ⊗KN →M isan
isomorphism. Since Φ commutes with the action ofGal, one has Φ(N)= N.
ThusN is a diﬀerence module overK and clearly induces the pair (M,D).
– 674 –
Galois theory ofq-diﬀerence equations
The tensor product of two pairs (M1,D 1), (M2,D 2) is deﬁned as
(M1 ⊗K∞ M2,D 1 ⊗D2). We note that the tensor productD1(σ) ⊗D2(σ)o f
twoσ-linear maps makes sense. It is easily seen that the above equivalence
respects tensor products. □
For a pure diﬀerence moduleN over K of slopeλ, the moduleM =
K∞ ⊗N is also pure with slopeλ and has the formK∞ ⊗C V, whereV is
a ﬁnite dimensionalC-vector space provided with an elementA ∈ GL(V).
The action of Φ onM is given by Φ(f ⊗v)= zλφ(f) ⊗A(v).
The subspaceV is not unique. By changingV, the eigenvalues ofA are
multiplied by arbitrary, rational powers ofq. We normalizeA and V as
follows.
Choose a Q-linear subspaceL ⊂ C such thatL ⊕ Q = C. One requires
thateveryeigenvalue cofAhastheform e2πi(a0(c)+a1(c)τ ) witha0(c),a 1(c) ∈
R anda1(c) ∈L.
After this normalization the subspaceV of M is unique. Indeed,V is
the direct sum of the kernels of (z−λΦ −c)s with s>> 0 andc ∈ C∗ with
a1(c) ∈L.
We note that the use of this subspaceL is somewhat artiﬁcial. It can
be avoided at the cost of verifying that formulas that we will produce are
independent of certain choices.
One observes thatV is invariant underD(σ) for allσ ∈Gal. The group
Gal is identiﬁed with ˆZ and the action ofGal is expressed byσ(z
λ)=
e2πiλσzλ. For the operatorsA and D(σ), restricted to V, one ﬁnds the
equalityAD(σ)= e2πiλσD(σ)A. Thus we have associated to a pure diﬀer-
ence moduleN overK a tupledata(N): =(λ,V,A, {D(σ)}) with
• λ ∈ Q.
• V a vector space overC of ﬁnite dimension.
• A ∈GL(V) with eigenvalues in the subgroup
{c=e2πi(a0(c)+a1(c)τ )|a0(c) ∈ R,a 1(c) ∈L} of C∗.
• a homomorphismσ ∈Gal ∼= ˆZ ↦→D(σ) ∈GL(V) satisfying
AD(σ)= e2πiλσD(σ)A.
On the other hand an object (λ,V,A, {D(σ)}) as above deﬁnes a pure
module N overK of slopeλ in the following way. ConsiderM :=K∞ ⊗V
with Φ given by Φ(f ⊗v)= zλφ(f) ⊗A(v) and with descent data given by
D(σ)(f ⊗v)= σ(f) ⊗D(σ)v. ThenN :=MGal.
– 675 –
Marius van der Put, Marc Reversat
Consider a morphismf :N1 →N2,f ⁄= 0 between pure modules. Then
N1,N 2 have the same slopeλ andf induces a morphism fromdata(N1)t o
data(N2), i.e., a linear mapF between the twoC-vector spaces equivariant
for the maps of the data. On the other hand, aC-linear mapF, equivariant
for the maps of the data, comes from a unique morphismf :N1 →N2.
Thus N ↦→data(N) is an equivalence between the category of the pure
modules overK and the category of tuples(λ,V,A, {D(σ)}) deﬁned above.
One observes the following useful properties.
For pure diﬀerence modulesNi withdata(Ni)=( λi,Vi,Ai, {Di(σ)}) for
i=1,2 one has the nice formula
data(N1 ⊗N2)=( λ1 +λ2,V 1 ⊗V2,A 1 ⊗A2, {D1(σ) ⊗D2(σ)}).
Let the pure modulesN have data(N)=( λ,V,A, {D(σ)}). Then the
dual moduleN ∗ has data (−λ,V ∗,B, {E(σ)}), whereV ∗ is the dual ofV;
B =(A−1)∗ andE(σ)=( D(σ)−1)∗.
The Φ-equivariant pairingN ×N ∗ → K, given by (n,𝓁) ↦→𝓁(n) ∈ K
translates for the data ofN and N ∗ into the usual pairingV ×V ∗ → C,
given by (v,𝓁) ↦→𝓁(v) ∈ C. This pairing is equivariant with respect to the
prescribed actions onV andV ∗.
