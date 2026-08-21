---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-017-42-the-whitehead-link-exterior-let-l-be-the-whit
section_title: "The Whitehead link exterior. Let L be the Whitehead link and choose the"
section_number: 4.2
pages: 13-14
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — W e study a computational method of the hyperbolic Reidemeister torsion (also called in the"
---
following Wirtinger presentation of the Whitehead link group:
π1(EL) = ⟨a, b | awa−1w−1⟩ where w = bab−1a−1b−1ab.
Figure 3. The Whitehead link with meridians
Hilden, Lozano and Montesionos has shown an explicit description of t he character
variety of the Whitehead link group in [HLMA92]. Trace functions play t he role of local
coordinates in this description. We set x, y and v as x = Ia, y = Ib and v = Iab, where
Iγ : X(EL) → C is again given by Iγ(χ) = χ(γ). Then the character variety of X(EL) is
expressed as
X(EL) = {(x, y, v) ∈ C3 | p(x, y, v)q(x, y, v) = 0 },
where
p(x, y, v) = xy − (x2 + y2 − 2)v + xyv2 − v3,
q(x, y, v) = x2 + y2 + v2 − xyv − 4.
The component of irreducible characters is given by
X irr(EL) = {(x, y, v) ∈ C3 | p(x, y, v) = 0 } \ R
where R = {x = ±2, v = ±y}∪{ y = ±2, v = ±x}. We consider an SL 2(C)-representation
ρ of π1(EL) whose character is contained in X irr(EL).
Let ρ : π1(EL) → SL2(C) be an irreducible representation and consider the abelian-
ization ϕ of π1(EL): ϕ : π1(EL) → Z2 = ⟨t1, t2 | t1t2 = t2t1⟩ deﬁned by ϕ(a) = t1 and
ϕ(b) = t2.
13
Using irreducibility of ρ, we can suppose that the pair of ρ(a) and ρ(b) are expressed
as (after taking conjugation with eigenvectors of ρ(a) and ρ(b) if necessary):
ρ(a) =
(
α 1
0 1 /α
)
ρ(b) =
(
β 0
γ 1/β
)
.
Note that we have set the local coordinates ( x, y, v) as x = α + α−1, y = β + β−1 and
v = γ + αβ + α−1β−1.
By using formula in [Mil68, Kit96, KL99], the polynomial torsion is expres sed as
∆ ϕ⊗Ad◦ρ
EL (t1, t2) = τ0 · det Φ
( ∂
∂b awa−1w−1)
det Φ( a − 1)
where Φ is the linear extension of ϕ ⊗ Ad ◦ ρ−1 on Z[π1(EL)]. The Fox diﬀerential turns
into
∂
∂b
(
awa−1w−1)
= (a − 1)(1 − bab−1 − bab−1a−1b−1 + bab−1a−1b−1a).
Therefore the polynomial torsion ∆ ϕ⊗Ad◦ρ
EL (t1, t2) turns out
∆ ϕ⊗Ad◦ρ
EL (t1, t2) = τ0 · det Φ(1 − bab−1 − bab−1a−1b−1 + bab−1a−1b−1a).
So that, with det Adρ(a)−1 = det Adρ(b)−1 = 1 in mind,
∆ ϕ⊗Ad◦ρ
EL (t1, t2) = τ0 · det Φ(1 − bab−1 − bab−1a−1b−1 + bab−1a−1b−1a)
= τ0 · det Φ
(
(bab−1a−1)(aba−1b−1 − a − b−1 + b−1a)
)
= τ0 · det Φ( aba−1b−1 − a − b−1 + b−1a).
When we choose the basis {E, H, F } in sl2(C), the adjoint actions Adρ(a)−1 and
Adρ(b)−1 are represented by the following upper and lower triangular matrice s
Adρ(a)−1 =


1/α2 2/α −1
0 1 −α
0 0 α2

 and Adρ(b)−1 =


1/β2 0 0
γ/β 1 0
−γ2 −2βγ β 2

 .
Calculating the determinant and reducing the degree of γ by using the following iden-
tity p(α + α−1, β + β−1, γ + αβ + α−1β−1) = 0, we can see that the polynomial torsion
is expressed as
∆ ϕ⊗Ad◦ρ
EL (t1, t2)
(13)
= τ0 · (t1 − 1)(t2 − 1)
t3
2
(
−2xyvt1t2 + x2t1(t2 + 1)2 + y2(t1 + 1)2t2 − (t1 + 1)2(t2 + 1)2)
.
