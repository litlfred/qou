---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-004-13-the-slope-ﬁltration
section_title: "The slope ﬁltration"
section_number: 1.3
pages: 6-7
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
We describe here the slope ﬁltration and give references for more details
and proofs. It is well known that any diﬀerence module M over K contains
a cyclic vector. This means that there exists an element e ∈M such that the
homomorphism K[Φ, Φ−1] →M, given by  anΦn → anΦn(e), is surjec-
tive (compare Lemma 4.1). Thus M is isomorphic to K[Φ, Φ−1]/K[Φ, Φ−1]L
for some L of the form Φd+ad−1Φd−1+· · ·+a0, with all ai ∈K and a0̸ = 0.
The diﬀerence operator L has a Newton polygon. For completeness we re-
call its deﬁnition. Let ord :
K →Z ∪{+∞} denote the order function
on K∗extended by ord(0) = +∞. In R2 one considers the convex hull of
d
i=0{(i, −ord(ai) + x2)| x2 ⩽0}. The ﬁnite part of the boundary of this
convex set is the Newton polygon of L.
The module M (over K or over K) is called pure if this Newton polygon
has only one slope. As in the case of diﬀerential operators, one can factorize
L, viewed as an element of K[Φ, Φ−1], according to the slopes in any order
that one chooses. This gives a unique decomposition of K ⊗K M as direct
sum N1 ⊕N2 ⊕· · · ⊕Nr of pure diﬀerence modules over K with slopes
λ1 < λ2 < · · · < λr. The rule Φzn = qnznΦ and |q| < 1 imply that the
slope factorization L1 · L2 · · · Lr of L where Li has slope λi for i = 1, . . . , r
is convergent, i.e., all Li are in K[Φ, Φ−1].
One deduces from this the ascending slope ﬁltration of M by submod-
ules 0 = M0 ⊂M1 ⊂M2 ⊂· · · ⊂Mr = M such that each Mi/Mi−1 is
pure of slope λi and moreover K ⊗Mi/Mi−1 ∼= Ni. The slope ﬁltration is
unique. The graded module gr(M) associated to M is ⊕r
i=1Mi/Mi−1. We
note that the above facts on slope ﬁltration are already present in the work
of G.D. Birkhoﬀ, P.E. Guenther and C.R. Adams, see [Bir]. A modern proof
is provided in [Sau3]. The diﬀerence module M over K is called split if M is
isomorphic to gr(M) (in other words, M is a direct sum of pure modules).
Fix a direct sum A = ⊕r
i=1Ai of pure modules with slopes λ1 < · · · < λr. In
section 3 we will construct a ﬁne moduli space for the equivalence classes of
the pairs (M, f), consisting of a diﬀerence module over K and an isomor-
phism f : gr(M) →A.
– 669 –
Marius van der Put, Marc Reversat
