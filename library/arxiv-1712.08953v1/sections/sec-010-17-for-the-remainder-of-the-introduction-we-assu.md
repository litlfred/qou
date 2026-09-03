---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-010-17-for-the-remainder-of-the-introduction-we-assu
section_title: "For the remainder of the introduction , we assume that k is a ﬁeld and z =q−q−1"
section_number: 1.7
pages: 6-8
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
---
for q∈ k ×\{± 1}. The next theorem describes K0( ˙OS (z,t )) in all semisimple cases.
It is also possible to compute the irreducible characters h(χλ )∈ k [un,vn|n≥ 1] by an
algorithm involving Starkey’s rule [Ge].
To state the theorem, let Bip = ∐
r,s≥0 Bipr,s where Bipr,s consists of bipartitions
λ = (λ↑,λ↓) for λ↑⊢ r and λ↓⊢ s. Let Sym be the ring of symmetric functions and
denote the Schur function associated to a partition λ by χλ. The structure constants
for this basis of Sym are the Littlewood-Richardson coeﬃcients: χµχν =∑
λLRλ
µ,νχλ.
Let λt denote the conjugate partition to λ.
Theorem 1.5. The category ˙OS (z,t ) is semisimple if and only if q is not a root of
unity and t /∈{±qn|n∈ Z}. Assuming this is the case, the isomorphism classes of inde-
composable objects in ˙OS (z,t ) are parametrized in a canonical way by Bip. Moreover,
the rings K0( ˙OS (z,t )) and Sym⊗Z Sym may be identiﬁed so that the isomorphism
class of the indecomposable indexed by λ∈ Bipr,s identiﬁes with
χλ :=
∑
0≤d≤min(r,s)
µ∈Bipr−d,s−d
N λ
µ χµ↑⊗χµ↓ where N λ
µ := (−1)d∑
ν⊢d
LRλ↑
µ↑,νLRλ↓
µ↓,νt. (1.9)
The standard technique to prove Theorem 1.5 is to deduce it from Th eorem 1.3
by similar arguments to [De, Proposition 10.6]; see also [CW, Theorems 4 .8.1 and
7.1.1]. In other words, one uses Schur-Weyl duality and well-known p roperties of
RepUq(gln) for suﬃciently large n. We will take a completely diﬀerent approach to
the proof of Theorem 1.5 and the representation theory of OS (z,t ) in general (even
in positive characteristic or at roots of unity) based on the simple ob servation that it
has a triangular decomposition. This allows us to adapt the usual arguments of highest
weight theory in a way that is reminiscent of the general framework of [HN, BT].
In this triangular decomposition, the “Cartan subalgebra” OS◦(z,t ) is the monoidal
subcategory consisting of all objects, and morphisms spanned by diagrams contain-
ing neither caps nor cups in which all upward propagating strands pa ss underneath
downward propagating strands. The “positive Borel subalgebra” OS♯(z,t ) is deﬁned
similarly, allowing also cups but no caps. Inﬂation from OS◦(z,t ) toOS♯(z,t ) followed
by induction from there to OS (z,t ) deﬁnes an exact standardization functor
∆ : Mod- OS◦(z,t )→ Mod-OS (z,t ). (1.10)
ORIENTED SKEIN CATEGORY 7
Moreover, there is an obvious equivalence of categories
Mod-OS◦(z,t )≈
∏
r,s≥0
Mod-Hr⊗Hs. (1.11)
Since the Hecke algebra is semisimple when q is not a root of unity, the semisimplicity
part of Theorem 1.5 is a consequence of the following more general r esult.
Theorem 1.6. If t /∈{±qn|n∈ Z} then ∆ is an equivalence of categories.
The other basic observation used to compute K0( ˙OS (z,t )) as a ring is:
Theorem 1.7. The inclusion OS◦(z,t )→OS (z,t ) induces a ring isomorphism
K0( ˙OS◦(z,t ))
∼
→K0( ˙OS (z,t )).
Now we describe K0( ˙OS (z,t )) for all choices of q and t. There are four cases.
• Suppose ﬁrst that q is not a root of unity. Up to isomorphism, the irreducible
representations of the (semisimple) Hecke algebra Hr are the Specht modules
parametrized by partitions ofr. Using the Morita equivalence (1.11), we deduce
that the irreducible OS◦(z,t )-modules are parametrized by bipartitions; we
denote them {S(λ )| λ ∈ Bip}. Their standardizations give us a family of
OS (z,t )-modules{∆( λ )| λ∈ Bip}.
– When t /∈{± qn|n∈ Z} (so that ˙OS(z,t ) is semisimple), the modules
∆( λ ) give a full set of pairwise inequivalent indecomposable OS (z,t )-
modules. This is the labelling from Theorem 1.5: in the identiﬁcation of
K0( ˙OS (z,t )) with Sym⊗Z Sym we have that
[∆( λ )]↔χλ. (1.12)
– When t = ±qn for n ∈ Z, we will show that Mod- OS (z,t ) has the
structure of an upper-ﬁnite highest weight category with standard mod-
ules{∆( λ )| λ∈ Bip}. This is a slight generalization of the usual notion
of highest weight category; e.g., see [EL, §6.1.2]. Each standard module
∆( λ ) has a unique irreducible quotient L( λ ), and these give a full set of
pairwise inequivalent irreducibleOS (z,t )-modules. Moreover, the projec-
tive cover P( λ ) of ∆( λ ) has a ﬁnite ∆-ﬂag with multiplicities satisfying
BGG reciprocity; however, unlike for usual highest weight categor ies, stan-
dard modules have inﬁnite length. In this situation, the Grothendiec k ring
K0( ˙OS (z,t )) is identiﬁed with the same ring Sym⊗Z Sym as for generic t
so that
[P(µ )]↔
∑
0≤d≤min(r,s)
λ∈Bipr−d,s−d
[∆( λ ) : L( µ )]χλ (1.13)
for µ ∈ Bipr,s. It remains to compute the numbers [∆( λ ) : L( µ )]. This
turns out to be quite straightforward: they are all either 0 or 1 an d can be
computed using the cup diagrams of [BS]. The combinatorics is discuss ed
in detail elsewhere; e.g., see [CW, EHS] (with Theorem 1.12 in mind).
• Now suppose that q2 is a primitive eth root of unity for e > 1. Then the
situation is more complicated as the Hecke algebras are no longer sem isimple.
Lete-Bip =∐
r,s≥0e-Bipr,s be the set of e-restricted bipartitions. By [DJ1] and
(1.11), the “Specht module” S( λ ) has irreducible head D( λ ) if λ ise-restricted,
and the modules {D(λ )| λ ∈ e-Bip} give a full set of pairwise inequivalent
irreducibleOS◦(z,t )-modules. Also let Y( λ ) be a projective cover of D( λ ).
Applying the standardization functor to D( λ ) and Y( λ ) gives us OS (z,t )-
modules denoted ¯∆( λ ) and ∆( λ ), respectively.
