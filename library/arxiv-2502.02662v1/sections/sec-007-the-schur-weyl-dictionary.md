---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-007-the-schur-weyl-dictionary
section_title: "The Schur-Weyl Dictionary"
section_number: null
pages: 10-12
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
---
Our aim in this section is to review how the Schur-Weyl duality can be leveraged to explicitly
rewrite the observables of two-dimensional Yang-Mills theory in terms of symmetric group
quantities [2,3,5,22]. Our goal is to claim that a certain sector of two-dimensional Yang-Mills
theory at large N is captured by a deformed Hurwitz theory.
We recall that representations of the symmetric group Sd are indexed by Young diagrams
with exactly d boxes, and representations of the unitary group U(N) relevant to the study of
two-dimensional Yang-Mills theory are indexed by Young diagrams with at most N rows [5].
The Schur-Weyl duality relates various quantities of unitary group and symmetric group
representations indexed by the same Young diagram. Consider first the equation for the
quadratic Casimir of a representation of the unitary groupU(N) indexed by a Young diagram
λ with d boxes :
c2(λ) =dN + 2f2(λ). (3.5)
The function f2(λ) denotes the Fourier transform of the conjugacy class of transpositions, as
defined in equation (2.1). The exponential term may then be split into two parts and the
correlators can be rewritten as
Z[MG,Ui] =
X
d
qd
X
λ∈Yd
N
sλ(U1)··· sλ(Uk)
(dimWλ
N)2g−2+k exp

−g2
YMA
N f2(λ)

, (3.6)
where q := e−
g2
YM A
2 . Next, we write the dimensions of the unitary group representation Wλ
N
as
dimWλ
N = Nd
d! Ω 1
N
(λ)dλ, (3.7)
9
where dλ is the dimension of the irreducible representation of the symmetric group indexed
by λ. The function Ω s is the Fourier transform of the exponential distance operator defined
as [22] 9
Ωs :=
X
η⊢d
s|η|Cη (3.8)
=Ce +sC2 +s2(C3 +C2,2) +O(s3) , (3.9)
where|η| denotes the charge of the permutationη, namely we have|η| :=d−l(η). The operator
Ωs depends on a free parameter s. For generic values of the parameter s, the exponential
distance operator is invertible. Indeed, if one writes Ω s =Ce +sω, then
Ω−1
s =Ce−sω +s2ω2 +... (3.10)
This series can be shown to converge absolutely when s̸= 1,...,d − 1 [22]. Conversely, if
the parameter s takes one of these values, then the operator Ω −1
s becomes singular. The
value of the operator Ω −1
s on partitions of length smaller than N is still well-defined but it
diverges for partitions of length larger than N. This is merely a consequence of the fact
that we take fictitious representations of U(N) to have vanishing dimension, as can be seen
from equation (3.7). The explicit algebraic description of the operators Ω ±1
s provides a direct
hands-on description of the computational consequences of the compactification of Hurwitz
spaces suggested in [5].
To complete the Schur-Weyl dictionary, we discuss how insertions in Yang-Mills translate
to the Hurwitz theory. We have the identity
sλ(U) = dλ
d!
X
α∈Yd
pα(U)fα(λ) (3.11)
where the power-sum polynomials pα(U) are defined as
pα(U) =
l(α)Y
i=1
trUαi. (3.12)
One recognizes in equation (3.11) the change of basis that relates Schur functions and power
sum polynomials. Substituting all of these identities in the partition function of the Yang-Mills
theory we obtain
Z[MG,Ui] =
X
d
(qN 2−2G−k)dZd[MG,Ui], (3.13)
where we defined the fixed-degree result
Zd[MG,Ui] :=
X
λ∈Yd
N
dλ
d!
2−2G kY
i=1
 X
α∈Yd
pα(Ui)fα(λ)· Ω−1
1/N(λ)
!
(Ω1/N(λ))2−2G exp

−g2
YMA
N f2(λ)

. (3.14)
9In practice, we often think of Ω as a linear combination of conjugacy classes. Nevertheless, one can think
instead of its Fourier transform Ω(λ) which is an operator on the set of representations ofSd [22]. Our notation
does not differentiate these two perspectives on Ω.
10
Note that this definition of Zd differs from the one introduced in section 3.1 by a factor
qdN (2−2G−k)d. From now on,Zd will always denote the factored out fixed-degree correlator. We
stress that equation (3.13) is an exact expression for the correlators of the full two-dimensional
Yang-Mills theory in terms of symmetric group quantities.
