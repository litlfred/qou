---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-009-4-review-on-the-nonabelian-reidemeister-torsion
section_title: "Review on the non–abelian Reidemeister torsion and twisted polynomial torsion"
section_number: 4
pages: 14-16
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
tion gives a detailed review of the constructions made in [Dub05, Section 6]. In particular,
we shall explain how to construct distinguished bases for the twisted homology groups of
knot exteriors.
14
Canonical homology orientation of knot exteriors. We equip the exterior of K with its
canonical homology orientation deﬁned as follows (see [Tur02, Section V .3]). We have
H∗(EK; R) = H0(EK; R)⊕ H1(EK; R)
and we base this R-vector space with {[ [pt] ], [ [µ] ]}. Here [ [ pt] ] is the homology class of
a point, and [ [µ] ] is the homology class of the meridian µ of K. This reference basis of
H∗(EK; R) induces the so–called canonical homology orientation of EK. In the sequel, we
let o denote the canonical homology orientation of EK.
How to construct natural bases of the twisted homology.Let ρ be a regular SL2(C)-representation
of Π(K) and ﬁx a generator Pρ of Hρ
0(∂EK) (i.e. Pρ is an element in sl2(C) such that
Adρ(g)(Pρ) = Pρ for all g∈ π1(∂EK)).
The canonical inclusion i: ∂EK→ EK induces (see [Por97, Corollary 3.23]) an isomor-
phism i∗ : Hρ
2(∂EK)→ Hρ
2(EK). Moreover, one can prove that (see [Por97, Proposition
3.18])
Hρ
2(∂EK) /simequalH2(∂EK; Z)⊗ C.
More precisely, let [ [∂EK] ]∈ H2(∂EK; Z) be the fundamental class induced by the orienta-
tion of ∂EK, one has Hρ
2(∂EK) = C [[ [∂EK] ]⊗ Pρ].
The reference generator of Hρ
2(EK) is deﬁned by
(25) hρ
(2) = i∗([[ [∂EK] ]⊗ Pρ]).
Let ρ be a λ-regular representation of Π(K). The reference generator of the ﬁrst twisted
homology group Hρ
1(EK) is deﬁned by
(26) hρ
(1)(λ) = ι∗
([[ [λ] ]⊗ Pρ]) .
Remark 10. The generator hρ
(1)(λ) of Hρ
1(EK) depends on the orientation ofλ. If we change
the orientation of the longitude λ in Eq. (26), then the generator is change into its reverse.
Remark 11. Note that Hρ
i (EK) is isomorphic to the dual space of the sl2(C)ρ-twisted coho-
mology Hi
ρ(EK) = Hi(EK; Ad◦ ρ). Reference elements deﬁned in Eqs. (25) and (26) are
dual from the ones deﬁned in [Dub06, Section 3.4].
The Reidemeister torsion for knot exteriors. Let ρ: Π(K)→ SL2(C) be a λ-regular repre-
sentation. The Reidemeister torsion TK
λ at ρ is deﬁned to be
(27) TK
λ (ρ) = TOR
(
EK; sl2(C)ρ,{hρ
(1)(λ), hρ
(2)}, o
)
∈ C∗.
It is an invariant of knots. Moreover, if ρ1 and ρ2 are two λ-regular representations
which have the same character then TK
λ (ρ1) = TK
λ (ρ2). Thus, TK
λ deﬁnes a map on the
set Xirr
λ (Π(K)) ={χ∈ Xirr(Π(K))| χ is λ-regular} of λ-regular characters.
Remark 12. The Reidemeister torsion TK
λ (ρ) deﬁned in Eq. (27) is exactly the inverse of
the one considered in [Dub06].
In the following remark we discuss sign properties of the torsion TK
λ .
Remark 13. (1) The torsion TK
λ does not depend on the orientation of K (see [Dub06,
Proposition 3.4]).
(2) Let K∗ denote the mirror image of K, and λ∗ be its preferred longitude as deﬁned
in Section 2. The character varieties of EK and EK∗ are same and TK∗
λ∗ = TK
λ .
Indeed, if we take the mirror image of K, then the orientation of the ambient
3-sphere is reversed, so the orientation of EK∗ is the opposite of the one of EK.
As a consequence the generator of Hρ
2(EK∗) deﬁned in Eq. (25) is the opposite of
the one of Hρ
2(EK). On the other hand, the meridian µ∗ of K∗ is the inverse of
the one of K whereas longitudes are same. So, the homology orientation o f K∗ is
the opposite of the one of K whereas generators of the twisted H1 are same. As a
consequence TK∗
λ∗ = TK
λ .
15
