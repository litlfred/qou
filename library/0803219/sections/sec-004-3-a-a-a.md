---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-004-3-a-a-a
section_title: "A ∧ A ∧ A"
section_number: 3
pages: 6-9
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
)
∈ C (mod Z),
where [ ρ ] means the conjugacy class. Note that every representation is induced
as the holonomy representation of a ﬂat connection.
P. Kirk and E. Klassen [33] gave a formula to calculate the SL(2; C) Chern–
Simons invariant if W is given as the union of two three-manifolds whose bound-
aries are tori.
Let M be an oriented three-manifold with boundary ∂M a torus. Given a
representation ρ of π 1(M ) at SL(2; C), one can deﬁne the Chern–Simons function
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 225
csM as a map from the SL(2; C)-character variety X(M ) of π 1(M ) to a circle
bundle E(∂M ) over the character variety X(∂M ) of π 1(∂M ) ∼= Z ⊕ Z [33], which
is a lift of the restriction map X(M ) → X(∂M ).
To describe cs M , we consider a map
p : Hom( π 1(∂M ), C) → X(∂M )
deﬁned by
p(κ ) :=
[
γ ↦→
(
exp(2π √ − 1κ (γ )) 0
0 exp( − 2π √ − 1κ (γ ))
)]
for γ ∈ π 1(∂M ), where the square brackets mean the equivalence class in X(∂M ).
Note that κ and κ ′deﬁne the same element in X(∂M ) if and only if
cos(2π
√
− 1κ (γ )) = cos(2 π
√
− 1κ ′(γ )) for any γ ∈ π 1(∂M ).
Now ﬁx a generator system ( µ, λ ) of π 1(∂M ) ∼= Z ⊕ Z, and take its dual basis
(µ ∗, λ ∗) of Hom( π 1(∂M ), C). If κ = αµ ∗ + βλ ∗ and κ ′ = α ′µ ∗ + β ′λ ∗, then
p(κ ) = p(κ ′) if and only if
kα + lβ = ± (kα ′+ lβ ′) (mod Z),
for any integers k and l. This means that p is invariant under the following
actions on Hom( π 1(∂M ); C):
x ·(α, β ) := ( α + 1, β ),
y ·(α, β ) := ( α, β + 1),
b ·(α, β ) := ( − α, − β ).
Note that these actions form the group
G := ⟨x, y, b |xyx−1y−1 = bxbx = byby = b2 = 1⟩
and that in fact the quotient space Hom( π 1(∂M ), C)/G can be identiﬁed with
the SL(2; C)-character variety X(∂M ).
Next let us consider the following actions on Hom( π 1(∂M ), C) × C∗.
x ·[α, β ; z] := [ α + 1, β ; z exp(2π
√
− 1β )],
y ·[α, β ; z] := [ α, β + 1; z exp(− 2π
√
− 1α )],
b ·[α, β ; z] := [ − α, − β ; z].
We denote the quotient space (Hom( π 1(∂M ), C) × C∗)/G by E(∂M ). Then
E(∂M ) becomes a C∗-bundle over X(∂M ). The Chern–Simons function cs M is
a map from X(M ) to E(∂M ) such that the following diagram commutes, where
q is the projection q : E(∂M ) → X(∂M ) and i∗ is the restriction map
E(∂M )
X(M ) X(∂M )
?
q
3csM
-i∗
.
226 HITOSHI MURAKAMI
More precisely, given a representation ρ , then
csM ([ρ ]) :=
{ [
α, β ; exp(2π √ − 1 csM (A))
]
, if i∗(ρ ) is diagonalizable,[
− a/ 2, − b/ 2; exp(2π √ − 1 csM (A))
]
, otherwise.
Here in the ﬁrst case
ρ (µ ) =
(
exp(2π √ − 1α ) 0
0 exp( − 2π √ − 1α )
)
,
ρ (λ ) =
(
exp(2π √ − 1β ) 0
0 exp( − 2π √ − 1β )
)
,
and
A =
(√ − 1α 0
0 − √ − 1α
)
dx +
(√ − 1β 0
0 − √ − 1β
)
dy
near ∂M , and in the second case
ρ (µ ) = ( − 1)a
(
1 c
0 1
)
,
ρ (λ ) = ( − 1)b
(
1 d
0 1
)
,
and
A =
(
− √ − 1a/ 2 c exp
(√ − 1(ax + by)
)
/ (2π )
0 √ − 1a/ 2
)
dx
+
(
− √ − 1b/ 2 d exp
(√ − 1(ax + by)
)
/ (2π )
0 √ − 1b/ 2
)
dy
near ∂M for a, b ∈ Z and c, d ∈ C, where ( x, y ) is the coordinate such that
(x, y ) ↦→ (exp(√ − 1x), exp(√ − 1y)) is the universal cover R2 → ∂M . See [33,
Section 3] for more details.
If a closed three-manifold W is given as M1 ∪ M2 by using two three-manifolds
M1 and M2 whose boundaries are tori, where we identify ∂M 1 with − ∂M 2. We
give the same basis for π 1(∂M 1) and π 1(− ∂M 2) and let ρ i be the restriction to
π 1(Mi) of a representation ρ of π 1(W ) ( i = 1, 2). Then we have
csW
(
[ρ ]
)
= z1z2,
where cs Mi ([ρ i]) = [ α, β, z i] with respect to the common basis [33, Theorem 2.2].
For a three-manifold M with hyperbolic metric one can deﬁne the ( SO(3))
Chern–Simons invariant CS( M ) as follows [5]. Let A be the Levi-Civita connec-
tion (an so(3)-valued 1-form) deﬁned by the hyperbolic metric. Then pu t
cs(M ) := 1
8π 2
∫
M
tr
(
A ∧ dA + 2
3 A ∧ A ∧ A
)
∈ R (mod Z).
