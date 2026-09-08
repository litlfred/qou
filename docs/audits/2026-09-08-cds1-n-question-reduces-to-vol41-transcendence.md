# The route-5 N question is not undecidable — it is the transcendence of Vol(4₁)

**Date:** 2026-09-08
**Bean:** `qou-cds1`, route 5
**Supersedes the framing of:** [#6755](https://github.com/litlfred/qou/pull/6755)
(`qbeta_fibre_unit_circle_opens_route5_probe`) — its arithmetic stands; its
verdict "not a question a measurement can answer" is too weak.
**Probe:** `computations/qbeta/qbeta_n_question_arithmetic_reduction_probe.py` (6/6)
**Scope:** **(b)** on two of three branches, each citing a named classical
invariant. The third branch is open and is not closed here.

## What #6755 established, and where it stopped

The fibre locus for route 5 is exactly `|q| = 1`: matching the Kohno–Drinfeld
holonomy to the Hecke eigenvalues forces `ħ = 2 ln q`, so `det A = −(ln q)²`,
which is positive iff `ln q` is purely imaginary. On that locus the eigenphase
is `θ = |arg q|`, and a root of unity `q = e^{2πik/N}` supplies it **iff `θ/2π`
is rational**, with

    θ/2π = 0.009010923285895504…

#6755 called that undecidable, because "every real has rational approximations
of arbitrary accuracy". **That is true of the decimal expansion and false of the
question.** Asking whether a real is rational by inspecting its digits is
hopeless; asking whether it is rational by inspecting *how it is built* is often
easy, and here it is.

## The reduction

Write `R = cos θ = Q_β^exp / (Q_A·(1 − u²))`, the quantity #6755 takes an
`arccos` of.

### 1. `R` is a rational function of `q₀` over ℚ — the square root cancels

`u = b·ħ²` carries `b = √((h²+3)/(h²+4))`, but only `u² = b²ħ⁴` ever appears,
and `b²` is rational in `q`. Verified symbolically (sympy) and numerically to
61 digits:

$$
R \;=\; \frac{-2\,Q_\beta\, q^{7}\,(q^{2}+1)^{2}}
{m_e\,(q+1)\,(q^{2}-2q-1)\,\bigl(4q^{7}-5q^{6}+8q^{5}-7q^{4}+8q^{3}-7q^{2}+4q-1\bigr)}
$$

Degree 11 over 10, **no radical**, coefficients in ℚ — `m_e` and `Q_β` are
CODATA decimals, hence exactly rational.

### 2. Niven closes the rational branch

The only rational values of `cos(2πr)` at rational `r` are `{0, ±1/2, ±1}`
(Mathlib: `Mathlib.NumberTheory.Niven.niven`). Measured,
`R = 0.998397668719255188542…`, whose nearest member of that set is `1`, at
distance **1.60e-3**. So **if `q₀` is rational — making `R` rational by step 1 —
no `N` exists at all**, for any `k`, any `N`.

### 3. Algebraic integrality closes the transcendental branch

`2cos(rπ)` is an **algebraic integer** for every rational `r` (Mathlib:
`isIntegral_two_mul_cos_rat_mul_pi`). A non-constant rational function with
rational coefficients maps transcendentals to transcendentals: if `R` were
algebraic, `q₀` would be a root of `P(x) − R·Q(x)`, a nonzero polynomial over
the algebraic numbers. Contrapositively, **`q₀` transcendental ⟹ `R`
transcendental ⟹ `2R` is not an algebraic integer ⟹ `R ≠ cos(2πk/N)` for any
`k`, `N`.**

### 4. `q₀`'s arithmetic nature is `Vol(4₁)`'s

The proton pinning identity is `m_p/m_e = 2·(Vol/ħ_q²)·F_Bor(q) − 12` with
**every** factor a rational function of `q`:

    h = q − 1/q,   ħ_q = 1 − 1/q,
    tr_M = |(4 + h² − 3h⁴ − h⁶)/(h² + 4)|,   qf3 = (q² + 1 + q⁻²)(q + 1/q)

so solving for `Vol` expresses it as a rational function of `q₀` with rational
coefficients. Round-tripped in the probe: `Vol` recovered from `q₀` matches
`2·Cl₂(π/3)` to **1.87e-60** at 60 dps. Hence **`q₀` algebraic ⟹ `Vol(4₁)`
algebraic**, and contrapositively `Vol(4₁)` transcendental ⟹ `q₀` transcendental.

## The result — a trichotomy, two branches closed

| `q₀` | consequence | verdict |
|---|---|---|
| rational | `R` rational; Niven forces `R ∈ {0,±½,±1}`; measured 1.60e-3 away | **no `N`** |
| transcendental | `R` transcendental, but `2cos(2πk/N)` is an algebraic integer | **no `N`** |
| algebraic irrational | `2R` must be an algebraic integer of degree exactly `φ(N)/2`, generating `ℚ(ζ_N)⁺` | the only survivor |

and by step 4 the surviving branch requires **`Vol(4₁) = 2·Cl₂(π/3)` to be an
algebraic number**.

**So the N question *is* the question of whether the figure-eight knot's
hyperbolic volume is algebraic.** That is a hard open problem — widely
conjectured transcendental, not proved — but it is a *named* open problem about
a single classical constant, not an unanswerable question about a decimal
expansion. **If `Vol(4₁)` is transcendental, the Kashaev sublocus is empty for
every `N`, and route 5 does not close through a root of unity at all.**

## What the surviving branch actually demands

If `θ = 2πk/N` with `gcd(k,N) = 1`, then `2cos θ` generates the maximal real
subfield `ℚ(ζ_N)⁺` and has degree exactly `φ(N)/2`. For the candidates #6755
had already recorded — **reported, not selected**:

| `k/N` | `φ(N)` | required `deg(2R)` |
|---|---|---|
| 1/110 | 40 | 20 |
| 1/111 | 72 | **36** |
| 42/4661 | 4524 | 2262 |
| 1145/127068 | 42352 | 21176 |

The open branch is therefore not *"find `N`"* but *"is `2R` an algebraic
integer, and of what degree"* — a question about `R`'s minimal polynomial, which
is decidable in principle, unlike the rationality of `θ/2π` read off digits.

## 🛑 No search on the target was run

`N = 111` is never used, tested, or scored in the derivation. Steps 1–4 never
consult which `N` is numerically near `θ/2π`; the degree table above reports
candidates #6755 had already recorded and selects among none of them. That
order — invariant first, target never searched — is the discipline this arc
committed to, and it is what makes the result a derivation rather than a fit.

## 🛑 This is not the trefoil dilogarithm trap

AGENTS.md records Bloch–Wigner / dilog-transcendence arguments as a recurrent
re-pitch failure mode. **The objection does not transfer**, and the reason is
specific: there the defect was that the *trefoil* complement is Seifert-fibered,
so `D(z) = 0` and the argument had no object to be about. Here the constant is
`Vol(4₁)`, the **figure-eight**, which is hyperbolic, is already the framework's
CAL-2 input, and enters through the pinning identity rather than through an
ansatz introduced to make an argument work. Different knot, different role.

## What this does not do

It does not prove `Vol(4₁)` transcendental, does not close route 5, and does not
produce a fibre element on `|q| = 1`. It converts one undecidable-looking
question into one named open problem plus two proved exclusions.

## Formalisation

Both classical inputs are already in Mathlib, sorry-free —
`Mathlib.NumberTheory.Niven.niven` and `isIntegral_two_mul_cos_rat_mul_pi` — so
the two closed branches are formalisable without new infrastructure. Step 1 (the
radical cancels) is a `field_simp`/`ring` identity. Not attempted here.
