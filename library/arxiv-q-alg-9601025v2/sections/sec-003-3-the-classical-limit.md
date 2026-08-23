---
doc_id: arxiv-q-alg-9601025v2
doc_title: "The hyperbolic volume of knots from the quantum dilogarithm"
section_id: sec-003-3-the-classical-limit
section_title: "The classical limit"
section_number: 3
pages: 3-5
source_pdf: 9601025v2.pdf
source_sha256: 369b0a1a92ce67a8
doc_brief: "The hyperbolic volume of knots from the quantum dilogarithm — The invariant of a link in three-sphere, associated with the cyclic quantum dilogarithm, depends on a natural number N ."
---
Here we calculate explicitly the leading asymptotics at N → ∞ of the
invariant for the hyperbolic knots from section 2 and justify formu la
(1.1).
3
First, for a positive real γ and complex p with
|Re p| < π + γ, (3.1)
deﬁne two functions
fγ (p) = Sγ (γ − π )/S γ (p), f γ (p) = Sγ (−p)/S γ (π − γ), (3.2)
where
Sγ (p) = exp 1
4
∫ +∞
−∞
epx
sinh(πx) sinh(γx)
dx
x , (3.3)
the singularity of the integrand at x = 0 being put below the contour
of integration. In [13] the function (3.3) is shown to be a particular
solution to the functional equation:
(1 + eip)Sγ (p + γ) = Sγ (p − γ). (3.4)
Via this functional equation the deﬁnition of the function Sγ (p) can
be extended to the whole complex plane.
For ﬁxed p the leading asymptotics of Sγ (p) at γ → 0 is given by
Euler’s dilogarithm:
Sγ (p) ∼ exp 1
2iγ Li2(−eip), γ → 0, (3.5)
where
Li2(z) = −
∫ z
0
log(1 − u)
u du. (3.6)
For numerical calculations the following formula will be useful (see, f or
example, [21]) :
Im Li 2(reiθ ) = ϕ log(r) + Λ( ϕ ) + Λ( θ) − Λ( ϕ + θ), (3.7)
where 0 < r ≤ 1,
ϕ = ϕ (r, θ ) = arctan
( r sin θ
1 − r cos θ
)
, (3.8)
and
Λ( θ) = −
∫ θ
0
log |2 sin φ| dφ, (3.9)
is Lobachevsky’s function.
From (3.2) and (3.4) it is easy to see that fγ (p) and f γ (p) are
analytic continuations of the symbols ( ω )k and ( ω )∗
k in the sense that
(ω )k = fγ (−π + γ + 2kγ ), (ω )∗
k =
f γ (−π + γ + 2kγ ), (3.10)
4
where
γ = π/N. (3.11)
Formulae (3.10) enable us to rewrite the summations in (2.2), (2.3),
(2.4) as contour integrals, one has just to replace symbols ( ω )k and
(ω )∗
k by their analytic continuations, and each summation, by a contour
integral:
∑
k
→ i
4γ
∮
dp tan
( π 2 + πp
2γ
)
(3.12)
with an appropriately chosen contour.
In what follows γ will be assumed to be speciﬁed as in (3.11).
