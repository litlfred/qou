---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane P. Bieliavsky G´ eom´ etrie et Physique math´ ematique Universit´ e Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louva"
section_id: sec-006-deformation-quantization
section_title: "Deformation Quantization"
section_number: null
pages: 11-13
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane P. Bieliavsky Géométrie et Physique mathématique Université Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louvain-la-Neuve, Belgium — We"
---
3.1 The space of star products on the Poincar´ e orbit M := SO(1, 1)× R2/R
It is proven in [30] that every Poincar´ e invariant star product on M is realized as a formal asymptotic
expansion in powers of ℏ of an oscillatory integral expression in terms of the geometrical quantities deﬁned
above:
u ⋆ℏ,P v (x0) = 1
ℏ2
∫
M×M
√
JacΦ(x0,x 1,x 2)e
i
ℏS(M)
can(x0,x1,x2)P(a0−a1)P(a2−a0)
P(a1−a2) u(x1)v(x2) dx1 dx2 ;
where dx denotes the Liouville symplectic measure onM and whereP is an essentially arbitrary nowhere van-
ishing complex-valued one variable function possibly depending smoothly in the real deformation parameter
ℏ. The function P therefore being the only degree of freedom (see [30] for details).
We now brieﬂy recall how the above result is obtained. The key point relies in the fact that the global
Darboux coordinate system ( a,𝓁 ) on S enjoys a property of compatibility with the hyperbolic action of
G :=SL2(R) on D = S.
In the case L is a Lie group with Lie algebra l that acts on a symplectic manifold ( M,ω ) in a Hamiltonian
manner, a (not necessarily L-invariant) star product ⋆ on (M,ω ) is called l-covariant if, denoting by
λ : l−→C∞(M) :X↦→λX (42)
the associated (dual) moment mapping, the following equalities hold:
i
ℏ [λX, λY ]⋆ := i
ℏ (λX ⋆λY−λY ⋆λX) = {λX, λY} = λ[X,Y ] (43)
for all X,Y ∈ l.
In this situation, one has a representation of l on C∞(M)[[ℏ]] by derivations of the star product ⋆:
ρℏ : l −→ Der(⋆) (44)
ρℏ(X)u := i
ℏ [λX, u]⋆ . (45)
It turns out that in coordinates (a,𝓁 ) the Moyal product (5) is sl2(R)-covariant with respect to the hyperbolic
action of G :=SL2(R) on the hyperbolic plane D = S [34]. Precisely, presenting the Lie algebra g := sl2(R)
as generated over R byH,E and F satisfying:
[H,E ] = 2E , [H,F ] =−2F , [E,F ] =H, (46)
11
the moment map associated with the action of G on D =G/K = S reads:
λH =
√
k𝓁 ; λE =
√
k
2 e−2a ; λF =−
√
k
2 e2a(1 +𝓁2). (47)
The associated fundamental vector ﬁelds are given by:
H⋆ =−∂a; E⋆ =−e−2a∂𝓁; F⋆ =e2a(𝓁∂a− (k +𝓁2)∂𝓁). (48)
At last, the representation of g by derivations of ⋆0
ℏ admits the expression:
ρℏ(H) = −∂a (49)
ρℏ(E) = −e−2a
ℏ sin(ℏ∂𝓁) (50)
ρℏ(F ) = e2a
( ℏ
4 sin(ℏ∂𝓁)∂2
a +𝓁 cos(ℏ∂𝓁)∂a− (k +𝓁2)sin(ℏ∂𝓁)
ℏ
)
. (51)
We now consider the partial Fourier transform in the 𝓁-variable
F(ϕ)(a,ζ ) =
∫ ∞
−∞
e−iζ𝓁ϕ(a,𝓁 )d𝓁 , (52)
and denote by ˜S :={(a,ζ )} the space where the Fourier transformed F(g) is deﬁned on. Deﬁning the
following one-parameter family of diﬀeomorphisms of ˜S:
φℏ(a,ζ ) =
(
a, sinh(ℏζ)
ℏ
)
, (53)
and denoting by ˜S (resp. S) the space of Schwartz test functions S(˜S) (resp. S(S)) on ˜S ={(a,ζ )} (resp.
onS(S) of S ={(a,𝓁 )}), one observes the following inclusions:
φ⋆
ℏ ˜S ⊂ ˜S and ˜S ⊂(φ−1
ℏ )⋆ ˜S ⊂ ˜S′ . (54)
Therefore, every data of (reasonable) one parameter smooth family of invertible functions Pℏ =Pℏ(b) yields
an operator on the Schwartz space S(S) of S ={(a,𝓁 )}:
T−1 :S(S)−→S (S) (55)
deﬁned as
T−1ϕ(a0,𝓁 0) = 1
2π
∫
eiζ𝓁0Pℏ(ζ)e
−i
ℏ 𝓁 sinh(ℏζ)ϕ(a0,𝓁 ) d𝓁 dζ . (56)
More generally, denoting byMf the pointwise multiplication operator by f, the operator:
T :S(S)−→S′(S) (57)
deﬁned as
T := F−1◦ (φ−1
ℏ )⋆◦M 1
P
◦F (58)
is a left-inverse of T−1. Intertwining Moyal-Weyl’s product by T yields the above product as ⋆ℏ,P =T (⋆0
ℏ).
Observe that the latter closes on the range space Eℏ := TS yielding a (non-formal) one parameter family
of associative function algebras: ( Eℏ,⋆ ℏ,P). Asymptotic expansions of these non-formal products produce
genuine Poincar´ e-invariant formal star products onM [39].
For genericP the above oscillatory integral product deﬁnes, for all real value of ℏ, an associative product
law on some function space (as opposed to formal power series space) on M. The most remarkable case
being probably the one where P is pure phase. In the latter case, the above product formula extends (when
ℏ⁄= 0) to the space L2(M) of square integrable functions as a Poincar´ e invariant Hilbert associative algebra.
The star product there appears to be strongly closed: for all u and v in L2(M), u ⋆ℏ,P v belongs to L1(M),
and one has: ∫
M
u ⋆ℏ,P v =
∫
M
uv .
The contracted situation is therefore, to some extent, relatively well understood.
12
