---
doc_id: arxiv-math-0409593v1
doc_title: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in represent"
section_id: sec-009-42-link-with-bimodules
section_title: "Link with bimodules"
section_number: 4.2
pages: 12-13
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
doc_brief: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in representation theory, for co"
---
4.2.1. We start by recalling results of Soergel [Soe1, Soe2, Soe3] r elating the category O to
modules over the coinvariant algebra.
Let Λ ∈ h∗/P . We denote by CΛ = A/(A · AWΛ
+ ) the coinvariant algebra of ( WΛ , SΛ )
and pΛ : A → CΛ the canonical surjection. Let λ ∈ Λ +. We denote by tλ : A → A the
translation by λ, given by f ↦→(z ↦→f (z + λ)) We have Soergel’s Endomorphismensatz [Soe1,
Endomorphismensatz 7] :
Theorem 4.1. The image of the composite morphism Z
h
− →A ˙W֒→A
tλ
− →A
pΛ
− →CΛ is C Wλ
Λ
and the canonical morphism Z → End(P (w0 · λ)) factors through this morphism Z → C Wλ
Λ .
The induced morphism σλ : C Wλ
Λ
∼
→ End(P (w0 · λ)) is an isomorphism.
Let us now recall Soergel’s Struktursatz [Soe1, Struktursatz 9] :
Theorem 4.2. The functor Hom(P (w0 · λ), −) : Oλ-proj → C Wλ
Λ -mod is fully faithful.
Let µ ∈ Λ be regular ( i.e., with trivial stabilizer in WΛ ).
There is an isomorphism φ : T µ
λ P (w0 · λ)
∼
→ P (w0 · µ). Any such isomorphism φ induces a
commutative diagram [Soe1, Bemerkung p.431]
C Wλ
Λ
σλ
/d15/d15
inclusion /d47/d47 CΛ
σµ
/d15/d15
End(P (w0 · λ))
φ∗T 0
λ /d47/d47 End(P (w0 · µ))
CATEGORIFICATION OF THE BRAID GROUPS 13
This gives us an isomorphism, via the adjunction ( T µ
λ , T λ
µ ) :
ResCΛ
C
Wλ
Λ
Hom(P (w0 · µ), ?)
∼
→ Hom(T µ
λ P (w0 · λ), ?)
∼
→ Hom(P (w0 · λ), T λ
µ (?))
between functors Oµ → C Wλ
Λ -mod. So, we have a commutative diagram, with fully faithful
horizontal functors
Oµ-proj
T λ
µ
/d15/d15
Hom(P (w0·µ),?) /d47/d47 CΛ -mod
Res
/d15/d15
Oλ-proj
Hom(P (w0·λ),?) /d47/d47 C Wλ
Λ -mod
4.2.2. From the last commutative diagram, we deduce
Proposition 4.3. There is a commutative diagram with fully faithful horizont al arrows
K b(O0-proj)
Hom(P (w0),−) /d47/d47
Fs
/d15/d15
K b(C-mod)
Fs
/d15/d15
K b(O0-proj)
Hom(P (w0),−) /d47/d47 K b(C-mod)
So, we deduce from Theorem 3.5 the following : given v ∈ BW and v = t1 · · ·tm = u1 · · ·un
two decompositions in elements of S ∪ S−1, there is an isomorphism Ft1 · · ·Ftm
∼
→ Fu1 · · · Fun
between functors on Db(O0) coming by restriction from the isomorphism between functors on
K b(A-modgr). These form a transitive system of isomorphisms, i.e.
Theorem 4.4. The functors Fs induce an action of BW on Db(O0).
More precisely,
Theorem 4.5. There is a monoidal functor from BW to the category of self-equivalences of
Db(O0) sending Gs to Fs.
Remark 4.6. One has a similar statement for the deformed category O.
Note that we deduce from §3.3.3 that there is also a right action of BW on Db(O0). We
leave it to the reader to check that this corresponds to the action s using Zuckerman functors,
or equivalently, Arkhipov functors.
In the graded setting (mixed perverse sheaves for example), the left and right actions of
BW should be swapped by the self-Koszul duality equivalence, cf [BerFr eKhov] (and [BeiGi,
Conjecture 5.18] for an analog in the equivariant case).
Various constructions have been given of weak actions of braid gro ups on Db(O0), cf [AnStr,
Ar, KhomMaz, MazStr, Str].
