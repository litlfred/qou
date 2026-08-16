---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-068-2-the-complement-of-anyσi-in-m-is-the-disjoint-u
section_title: "The complement of anyΣi in M is the disjoint union of two handlebodies"
section_number: 2
pages: 92-95
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
M1 and M2.
3. The eigenvalue of¯ρ(∂Σ) is the trivial root of unity1.
Remark 3.3.1. This assumptions are motivated by the fact that it is the way it
appears in simple examples we can produce : for instance consider the ﬁgure-eight
knot’s classical diagram in Figure 3.3, and the non-orientable surfaceˇΣ obtained by
a "checkerboard" coloring. The boundary of its neighborhood is an orientable surface
Σ, which turns out to be incompressible. It is detected by the point{x =∞,y = 2}
of the component of irreducible type of the character variety of the ﬁgure-eight
knot. It easy to see on the picture that its complement is the union of two genus
2 handlebodies, and a computation shows that the root of unity associated to the
boundary curve∂Σ =uv−1u−1vuv−1u−2v−1uvu−1v−1u−1 is 1.
We have performed numerous computations in the case of a two-holed torus with
the help of the software SageMath. We have produced reducible representations of
the free group on three generators, that come from irreducible representations of
the closed genus two surface obtained by gluing together the boundary components.
We have observed that the torsion will vanish whenever the image of the boundary
curve has eigenvalues equal to 1 (and we proved the theorem in this case), on the
other hand we produced several examples with eigenvalue -1 where the torsion did
not vanish.
Recall from Section 1.3.6 that we have the splittingM = M1∪Σ M2, it induces
the following exact sequence of complexes ofk(X)-vector spaces 0→ C∗(M,ρ )→
C∗(M1,ρ 1)⊕C∗(M2,ρ 2)→C∗(Σ,ρ Σ)→ 0.
91
ˇΣ
v u
Figure 3.3 – The ﬁgure-eight knot, with a non orientable checkerboard surfaceˇΣ,
and generating loopsu,v of its fundamental group
Notation. Since we have picked a base pointp∈ Σ1 in Section 1.3.6, we will abuse
of the notationπ1(Σ) to designateπ1(Σ1). In the same way, we denote byC∗(Σ,ρ Σ)
the twisted cohomological complex ofΣ1.
Lemma 3.3.2.One has the following isomorphism ofk(X)-vector spaces :
d :H1(M1,ρ 1)⊕H1(M2,ρ 2)
∼
− →H1(Σ,ρ Σ)
Proof. Recall thatC∗(M,ρ ) is acyclic andHj(Mi,ρi) ={0} for anyj≥ 2,i = 1, 2
because Mi have the same homotopy type that a one-dimensional CW complex.
Now ¯ρi are irreducible by Lemma 1.3.15, henceρi are irreducible and in particular
there isγi∈ π1(Mi) such that Tr(ρi(γi))⁄= 2. ThusH0(Mi,ρi) ={0}. The lemma
follows now from the Mayer-Vietoris sequence.
Lemma 3.3.3. TheOv-modules H1(M1,ρ 1)v,H 1(M2,ρ′
2)v,H 1(Σ,ρ Σ)v are free of
rank−χ(Σ1),−χ(Σ1) and−2χ(Σ1) respectively.
Proof. The Mayer-Vietoris sequence of Lemma 3.3.2 implies thatH0(Σ,ρ Σ) ={0}
since H0(Mi,ρi) =H0(M,ρ ) ={0}, and similarlyH2(Σ,ρ ) ={0}. NowH1(Σ,ρ Σ)v
is free of rank−2χ(Σ), and the lemma follows.
92
We pick bases of the complexes ofk(X)-vector spacesC∗(M1,ρ 1), C∗(M2,ρ 2) and
C∗(Σ,ρ Σ) and of their homology groupsH1(M,ρ 1), H1(M2,ρ 2) and H1(Σ,ρ Σ). We
also pick a basis for the acyclic complexC∗(M,ρ ). We have the following formula
due to Milnor [Mil66], that does not depends on the choices :
Proposition 3.3.4. The torsion of the complexC∗(M,ρ ) can be expressed as
tor(M,ρ ) = tor(M1,h 1) tor(M2,h 2)
tor(Σ,h Σ) tor(H,h 1,h 2,h Σ)∈k(X)∗
whereH is the Mayer-Vietoris sequence of Lemma 3.3.2.
The following is identical to Proposition 2.4.4, hence we refer to it for a proof.
Proposition 3.3.5. The terms tor(M1), tor(M2) and tor(Σ) lie inO∗
v
Remark 3.3.6. As a consequence of this proposition, it is enough to compute the
term tor(H,h 1
1,h 1
2,h 1
Σ), which is just the inverse of the determinant of the following
map (see Section 1.5.3) :
θ :H1(M1,ρ 1)⊕H1(M2,ρ′
2)
∼
− →H1(Σ,ρ Σ)
(Z1,Z 2)↦→ (Z1−UnZ2)|Σ
that isθ is the composition ofd with φ. We compute nowdet(θ).
For this purpose we observe that the relation∀γ ∈ π1(Σ),ρ 1(γ) = Unρ′
2(γ)U−1
n
implies that the corresponding residual representations have the following form,
when restricted toπ1(Σ) :
¯ρ1(γ) =
(
λ(γ) 0
λ(γ)u1(γ) λ−1(γ)
)
, ¯ρ2(γ) =
(
λ(γ) λ−1(γ)u2(γ)
0 λ−1(γ)
)
for someu1∈H1(Σ,λ−2),u 2∈H1(Σ,λ 2). Consequently one has the splittings
0→H1(Σ,λ−1)
i1
− →H1(Σ, ¯ρ1,Σ)
p1
− →H1(Σ,λ )→ 0
0→H1(Σ,λ )
i2
− →H1(Σ, ¯ρ2,Σ)
p2
− →H1(Σ,λ−1)→ 0
More precisely, if sayz1∈ H1(Σ, ¯ρ1) has the formz1(γ) =
(
x1(γ)
y1(γ)
)
then the ﬁrst
splitting is given explicitly by the morphismsi1(y1) =
( 0
y1
)
and p1((x1
y1 )) =x1.
93
Notation. Here, and in the sequel, we will denote by¯ρ1 and ¯ρ2 the residual re-
presentations obtained from ρ1 and ρ′
