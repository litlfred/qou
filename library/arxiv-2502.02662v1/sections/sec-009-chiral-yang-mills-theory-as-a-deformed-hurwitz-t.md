---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-009-chiral-yang-mills-theory-as-a-deformed-hurwitz-t
section_title: "Chiral Yang-Mills Theory as a Deformed Hurwitz Theory"
section_number: null
pages: 13-15
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
---
We have all the necessary tools in hand to define a deformed Hurwitz theory that is manifestly
dual to two-dimensional chiral Yang-Mills theory. As suggested at the end of section 3.1, we
will focus on the degree d sector of chiral Yang-Mills theory and postpone the discussion of
the sum over degrees. Firstly, we consider the fixed-degree correlators of the chiral theory in
the strict large N limit:
Z+
d (U1,...,U k) =
X
α1,...,αd∈Yd
 kY
i=1
pαi(Ui)
!X
λ∈Yd
dλ
d!
2−2g kY
i=1
fαi(λ) (3.16)
=Hd
 X
α
pα(U1)Cα,...,
X
α
pα(Uk)Cα
!
. (3.17)
The subscript + denotes the chiral correlators. The sum over Young diagrams on the right-
hand side is manifestly a linear combination of Hurwitz number with coefficients that are
polynomials in the holonomies. As a result, the degree d sector reduces in the strict large
N limit to a Hurwitz theory with gauge group Sd. The dictionary of observables sends a
holonomy classU in the Yang-Mills theory to an operatorP
αpα(U)Cα in the Hurwitz theory.
11A non-perturbative definition of the chiral theory can perhaps be achieved by restricting the sum over
degrees d in equation (3.6) to degrees bounded above by d≤N.
12The only observables which are not affected by this divergence are the partition functions on the sphere
and the torus, as well as the one and two point functions on the sphere.
13Nevertheless, our prescription to regularize the asymptotic expansion holds, at least on Riemann surfaces
of genus G >1, because diagrams with N boxes or more are exponentially suppressed by factors N −N, as
explained above.
12
When the 1/N corrections are turned on, the right-hand side of equation (3.14) features
additional terms compared to the limit (3.16): simple branch points on the one hand, and Ω op-
erators on the other. One difficulty in establishing a correspondence between two-dimensional
Yang-Mills theory and Hurwitz theory lies in the treatment of these Ω factors.
The novelty in our approach will consist in treating these factors as arising from a defor-
mation of Hurwitz theory.14 There is a modification of the moduli space captured by a factor
Ω2−2G in the partition function [5]. The renormalization of the observables accounts for the
additional Ω−k factor that appears in the Gross-Taylor expansion.
We proceed to define the appropriate deformations of Hurwitz theory. We first incorporate
the single branch points by adding the extra term
L→L− gst·C2 (3.18)
to the exponent of the path integral measure formally represented by a Lagrangian L. The
factor gs denotes the string coupling constant in the dual theory and is identified with 1 /N.
It is featured in the perturbation to ensure that the deformation is small for small values
of t. Indeed, as we shall see in section 4.3, whether the deformation parameters are large
or small is determined by their value relative to the string coupling. Furthermore, factoring
out gs allows us to interpret the parameter t as the area of the target space in units of the
Yang-Mills coupling gYM . We now introduce the Ω deformation. Recall that the operator Ω
has a natural expression as a linear combination of conjugacy classes. Furthermore, we have
the first order estimate Ω gsu = 1 +O(gsu), which implies that the logarithm of the operator
is well-defined perturbatively. We write
L→L + log Ω2−2G
gsu . (3.19)
We have introduced the parameter u to highlight the need to implement the regularization
description of the inverse exponential distance operator described in section 3.3. In terms ofu,
the prescription consists in evaluating the correlators at u = 1−ϵ, dropping the exponentially
suppressed terms from the expansion, then taking the limit ϵ→ 0.
The above symbolic representations can be made precise by stating that the correlators of
the deformed Hurwitz theory at order d read
⟨
kY
i=1
Cαi⟩t,u
d =⟨
 kY
i=1
Cαi
!
e−gstC2 Ω2−2G
gsu ⟩d, (3.20)
where the superscript t,u on the left-hand side indicates that the parameters of the defor-
mation are t and u, respectively. To simplify the notations, we shall use a superscript def to
denote the Hurwitz theory deformed by the parameters t =g2
YMA andu = 1, up to a regular-
ization procedure. Comparing with the expression for the fixed-degree Yang-Mills correlators
in the large N limit (3.14), we find that agreement between the correlators of both theories
necessitates that the operators of the Hurwitz theory be renormalized as
Cα→ ˆCα := Ω−1
gsuCα. (3.21)
14The papers [5, 6] have treated area terms in the Yang-Mills partition function by perturbing the conjec-
tured dual string theory by an area operator. We modify the treatment and extend the strategy to the Ω
points. Furthermore, we note that the Yang-Mills point in theory space corresponds to finite deformations by
transpositions and Ω points.
13
The inverse exponential distance operator Ω −1
gsu is an element of the conjugacy class algebra
Cd. Therefore, the renormalized class ˆCα is a well-defined operator in this algebra.
We may finally equate the perturbative expansion of the correlators on both sides of the
chiral theory
Z+
d [MG,Ui] =⟨
Y
i
 X
α⊢d
pα(Ui) ˆCα
!
⟩def
d , (3.22)
and conclude that the large N limit of the degree d sector of chiral Yang-Mills theory is dual
to the deformed Hurwitz theory for deformation parameters equal to t = g2
YMA and u = 1.
The dictionary of observables sends a holonomy insertion U in the Yang-Mills theory to an
operatorP
α⊢dpα(Ui) ˆCα in the Hurwitz theory.
