---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-069-2-we-will-denote-by-ρiσ-the-restriction-of
section_title: "We will denote by ¯ρi,Σ the restriction of"
section_number: 2
pages: 95-96
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
¯ρi :π1(Mi)→ SL2(k) to π1(Σ) through the mapπ1(Σ)→π1(Mi) induced by inclu-
sion. Similarly, we will denote by¯ρ2,∂M2 the restriction of ¯ρ2 to π1(∂M2), and ¯ρ2,γ
the restriction of¯ρ2 to any curveγ, in particularγ =∂Σ.
We need to prove that the torsion has a pole at the ideal pointx. Denote byv the
valuation associated tox, that means that the determinant of the map
θ :H1(M1,ρ 1)⊕H1(M2,ρ′
2)
∼
− →H1(Σ,ρ Σ)
(Z1,Z 2)↦→ (Z1−UnZ2)|Σ
has positive valuation. Consider thek-linear map ¯θ : H1(M1, ¯ρ1)⊕H1(M2, ¯ρ2)→
H1(Σ, ¯ρΣ) which isθ modulo t, it maps(z1,z 2) ontoz1|Σ−
( 0
y2|Σ
)
.
Lemma 3.3.7.The torsion has a pole atx iﬀ¯θ is not an isomorphism.
Proof. It is clear from the fact thatdet(¯θ) = (det θ)(0), that isv(det(θ))≥ 0 iﬀ
det(¯θ) = 0.
Let us prove thatdet(¯θ) = 0. Let∂M2 be the boundary ofM2, andγ =∂Σ⊂∂M2
the union of boundary curves ofΣ. Since Σ is incompressible and∂Σ⊂ ∂M, all
the components of∂Σ are parallel in∂M because it is a torus, in particular they
deﬁne the same free homotopy class. Assumption 3 implies that¯ρ2(γ) = ( 1∗
0 1 ), hence
H1(γ, ¯ρ2,γ) is not trivial. The long exact sequence for the coeﬃcients ofC∗(γ, ¯ρ2,γ)
ends with
... →H1(γ, ¯ρ2,γ)
pγ
−→H1(γ,k )→ 0
There are two possibilities, namelyρ2(γ) = Id or not, but in any case, the map
pγ :H1(γ, ¯ρ2,γ)→H1(γ,k ) is not zero.
On the other hand, the inclusionΣ⊂∂M2 provides the sequence
H1(∂M2, Σ; ¯ρ2,∂M2)→H1(∂M2, ¯ρ2,∂M2)→H1(Σ, ¯ρ2,Σ)→H2(∂M2, Σ; ¯ρ2,∂M2)→ 0
(3.1)
Denote byA the union of small annulus neighborhood of the components ofγ in
∂M2. By excision, we have H2(∂M, Σ; ¯ρ2,∂M2) ≃ H2(A,∂A ; ¯ρ2,γ). Now Poincaré-
Lefschetz duality implies that it is the same thatH0(A, ¯ρ2,γ), and by homotopy this
is H0(γ, ¯ρ2,γ). Again by duality we obtainH1(γ, ¯ρ2,γ).
We summarize that in the following commutative diagram :
94
H1(M2, ¯ρ2)
H1(∂M2, ¯ρ2,∂M2)
H1(Σ, ¯ρ2,Σ)H1(Σ,λ ) H1(Σ,λ−1)
H1(γ, ¯ρ2,γ)) H1(γ,k )
0
0
0
i∂M2
iΣ
p2i2
i∂Σ
pγ
i∂Σ
F
Lemma 3.3.8. The composition mapF : H1(M2, ¯ρ2)
i∂M2
− −− →H1(∂M2, ¯ρ2,∂M2)
iΣ
− →
H1(Σ, ¯ρ2,Σ)
p2
− →H1(Σ,λ−1) is not an isomorphism.
Proof. Theﬁrstobservationisthat dimH1(M2, ¯ρ2) = dimH1(Σ,¯ρ2,Σ)
2 = dimH1(Σ,λ−1).
Thus it suﬃces to prove that the mapF is not onto. But if it was, it would have a
non-trivial image inH1(γ,k ) through the mapi∂Σ. On the other hand, the vertical
sequence H1(∂M2, ¯ρ2,∂M2)
i∂M2
− −− →H1(Σ, ¯ρ2,Σ)
i∂Σ
−−→H1(γ, ¯ρ2,γ) is exact by equation
(3.1), and the commutativity of the diagram shows thati∂Σ◦F = 0, and the lemma
is proved.
Proof of Theorem 3.0.2.Wejusthavetoobservethat ¯θ :H1(M1, ¯ρ1)⊕H1(M2, ¯ρ2)→
H1(Σ, ¯ρ1,Σ) is the direct sum of
1. the injective mapH1(M1, ¯ρ1)→H1(Σ, ¯ρ1,Σ) induced by inclusion
2. the mapH1(M2, ¯ρ2)→ H1(Σ, ¯ρ2,Σ)
p2
− →H1(Σ,λ−1)
i1
− →H1(Σ, ¯ρ1,Σ) which is
i1◦F.
The ﬁrst map has maximal rank−χ(Σ), but the second has rank smaller than−χ(Σ)
by Lemma 3.3.8. Hence¯θ is not onto, hencedet(¯θ) = 0. By Lemma 3.3.7 we conclude
that the torsion vanishes atx, and the theorem is proved.
