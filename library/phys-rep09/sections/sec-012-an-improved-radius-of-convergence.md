---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-012-an-improved-radius-of-convergence
section_title: "An improved radius of convergence"
section_number: null
pages: 18-19
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The previous results on the convergence of the Magnus series have been established for n × n real matrices: if A(t) is a
real n× n matrix, then (67) gives a condition for Y(t) to have a real logarithm. In fact, under the same condition, the Magnus
series (40) converges precisely to this logarithm, i.e., its sum Ω(t) satisfies exp(Ω(t)) = Y(t) [71].
One should have in mind, however, that the original expansion was conceived by requiring only that A(t) be a linear
operator depending on a real variable t in an associative ring (Theorem 1). The idea was to define, in terms of A, an operator
Ω(t) such that the solution of the initial value problem Y ′ = A(t)Y, Y(0) = I, for a second operator Y is given as Y = exp Ω.
The proposed expression for Ωis an infinite series, satisfying the condition that ‘‘its partial sums become Hermitian after
multiplication by i if iA is a Hermitian operator’’ [4]. As this quotation illustrates, Magnus expansion was first derived in the
context of quantum mechanics, and so one typically assumes that it is also valid when A(t) is a linear operator in a Hilbert
space. Therefore, it might be desirable to have conditions for the convergence of the Magnus series in this more general
setting. In [31], by applying standard techniques of complex analysis and some elementary properties of the unit sphere,
the bound rc = π has been shown to be also valid for any bounded normal operator A(t) in a Hilbert space of arbitrary
dimension. Next we review the main issues involved and refer the reader to [31] for a more detailed treatment.
Let us assume that A(t) is a bounded operator in a Hilbert space H, with 2 ≤dim H ≤∞. Then we introduce a new
parameter ε ∈C and denote by Y(t; ε) the solution of the initial value problem
dY
dt = εA(t)Y,
Y(0) = I,
(70)
where I now denotes the identity operator in H. It is known that Y(t; ε) is an analytic function of ε for a fixed value of t. Let
us introduce the set Bγ ⊂C characterized by the real parameter γ ,
Bγ =

ε ∈C : |ε|
Z t
0
∥A(s)∥ds < γ

.
Here ∥.∥stands for the norm defined by the inner product on H, i.e., the 2-norm introduced in Section 1.2.
If t is fixed, the operator function ϕ(ε) = log Y(t; ε) is well defined in Bγ when γ is small enough, say γ < log 2,
as an analytic function of ε. As a matter of fact, this is a direct consequence of the results collected in Section 2.7.2: if,
in particular, |ε|
R t
0 ∥A(s)∥ds < log 2, the Magnus series corresponding to (70) converges and its sum Ω(t; ε) satisfies
exp(Ω(t; ε)) = Y(t; ε). In other words, the power series Ω(t; ε) coincides with ϕ(ε) when |ε|
R t
0 ∥A(s)∥ds < log 2, and so
the Magnus series is the power series expansion of ϕ(ε) around ε = 0.
Theorem 6. The function ϕ(ε) = log Y(t; ε) is an analytic function of ε in the set Bπ, with
Bπ =

ε ∈C : |ε|
Z t
0
∥A(s)∥ds < π

.
If H is infinite dimensional, the statement holds true if Y is a normal operator.
In other words, γ = π. The proof of this theorem is based on some elementary properties of the unit sphere S1 in a Hilbert
space. Let us define the angle between any two vectors x̸ = 0, y̸ = 0 in H, Ang{x, y} = α, 0 ≤α ≤π, from
cos α =
Re⟨x, y⟩
∥x∥∥y∥,
where ⟨·, ·⟩is the inner product on H. This angle is a metric in S1, i.e., the triangle inequality holds in S1.
The first property we need is given by the next lemma [67].
Lemma 7. For any x ∈H, x̸ = 0, Ang{Y(t; ε)x, x} ≤|ε|
R t
0 ∥A(s)∥ds.
Observe that if Y is a normal operator in H, i.e., YY Ď = Y ĎY (in particular, if Y is unitary), then ∥Y Ďx∥= ∥Yx∥for all x ∈H
and therefore Ang{Y Ďx, x} = Ang{Yx, x}.
The second required property provides useful information on the location of the eigenvalues of a given bounded operator
in H [72].
Lemma 8. Let T be a (bounded) operator on H. If Ang{Tx, x} ≤γ and Ang{T Ďx, x} ≤γ for any x̸ = 0, x ∈H, where T Ď
denotes the adjoint operator of T, then the spectrum of T, σ(T), is contained in the set
∆γ = {z = |z|eiω ∈C : |ω| ≤γ }.
Proof (of Theorem 6). Let us introduce the operator T ≡Y(t; ϵ), with ε ∈Bγ , γ < π. Then by Lemma 7, Ang{Tx, x} ≤γ for
all x̸ = 0, and thus, by Lemma 8,
σ(T) ⊂∆γ .
(71)
If dim H = ∞and we assume that Y(t; ϵ) is a normal operator, then (71) also holds.
S. Blanes et al. / Physics Reports 470 (2009) 151–238
169
From Eq. (70) in integral form,
Y(t; ε) = I + ε
Z t
0
A(s)Yds,
one gets ∥Y∥≤1 + |ε|
R t
0 ∥A(s)∥∥Y∥ds, and application of Gronwall’s lemma [73] leads to
∥Y(t; ε)∥≤exp

|ε|
Z t
0
∥A(s)∥ds

.
An analogous reasoning for the inverse operator also proves that
∥Y −1(t; ε)∥≤exp

|ε|
Z t
0
∥A(s)∥ds

.
In consequence,
∥T∥≤eγ
and
∥T −1∥≤eγ .
If λ̸ = 0 ∈σ(T), then |λ| ≤∥T∥[74] and therefore |λ| ≤eγ . In addition, 1
λ ∈σ(T −1), so that |λ| ≥e−γ . Equivalently,
σ(T) ⊂{z ∈C : e−γ ≤|z| ≤eγ } ≡Gγ .
(72)
Putting together (71) and (72), one has
σ(T) ⊂Gγ ∩∆γ ≡Λγ .
Now choose any value γ ′ such that γ < γ ′ < π (e.g., γ ′ = (γ +π)/2) and consider the closed curve Γ = ∂Λγ ′. Notice that
the curve Γ encloses σ(T) in its interior, so that it is possible to define [75] the function ϕ(ε) = log Y(t; ε) by the equation
ϕ(ϵ) =
1
2πi
Z
Γ
log z (zI −Y(t; ϵ))−1 dz,
(73)
where the integration along Γ is performed in the counterclockwise direction. As is well known, (73) defines an analytic
function of ε in Bγ ′ [75] and the result of the theorem follows.
■
Theorem 9. Let us consider the differential equation Y ′ = A(t)Y defined in a Hilbert space H with Y(0) = I, and let A(t) be a
bounded operator in H. Then, the Magnus series Ω(t) = P∞
k=1 Ωk(t), with Ωk given by (51) converges in the interval t ∈[0, T)
such that
Z T
0
∥A(s)∥ds < π
and the sum Ω(t) satisfies exp Ω(t) = Y(t). The statement also holds when H is infinite-dimensional if Y is a normal operator
(in particular, if Y is unitary).
Proof. Theorem 6 shows that log Y(t; ε) ≡ϕ(ε) is a well defined and analytic function of ε for
|ε|
Z t
0
∥A(s)∥ds < π.
It has also been shown that the Magnus series Ω(t; ε) = P∞
k=1 εkΩk(t), with Ωk given by (51), is absolutely convergent
when |ε|
R t
0 ∥A(s)∥ds < ξ = 1.0868 . . . and its sum satisfies exp Ω(t; ε) = Y(t; ε). Hence, the Magnus series is the power
series of the analytic function ϕ(ε) in the disk |ε| < ξ/
R t
0 ∥A(s)∥ds. But ϕ(ε) is analytic in Bπ ⊃Bξ and the power series
has to be unique. In consequence, the power series of ϕ(ε) in Bπ has to be the same as the power series of ϕ(ε) in Bξ, which
is precisely the Magnus series. Finally, by taking ε = 1 we get the desired result.
■
