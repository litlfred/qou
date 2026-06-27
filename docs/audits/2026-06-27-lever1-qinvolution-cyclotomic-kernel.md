# Lever-1 fibre kernel: the q-involution skeleton + its cyclotomic (Habiro) correction

**Date:** 2026-06-27
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)` for the binding genfun)
**Compute:** [`computations/substrate/lever1_qinvolution_kernel_test.py`](../../computations/substrate/lever1_qinvolution_kernel_test.py)
**Witness:** [`computations/substrate/lever1-qinvolution-kernel-test.witness.json`](../../computations/substrate/lever1-qinvolution-kernel-test.witness.json)
**Serves:** `kehn` (Q_β / m_n c_k closure via a Habiro element), `s5bb` (the Habiro-element keystone blocker)

## Background — what was already known

The binding selection-rule values `lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q(λ)` were posited
to be the prolonged periods `a_D^(n)` of a fixed `2×2` `SL₂` monodromy `B` with
`τ = tr B = 3(3q⁴+8q²+3)/(4q(q+1)²)`, i.e. a **depth-2 constant-coefficient
(C-finite) recurrence** `R(q,x) = x²−τx+1`. That model was **falsified beyond the
`n≤4` seed** ([`lever1-lw-depth2-recurrence-test.witness.json`](../../computations/substrate/lever1-lw-depth2-recurrence-test.witness.json)):
the windowed kernel drifts (`τ_{2,3,4}=2.6424` vs `τ_{3,4,5}=2.6505`), so `lw` is not
`φ(Mⁿv₀)` for any fixed `M` (Cayley–Hamilton). `θ_binding = arccosh(τ/2) = 0.7815`
is a 3-point seed-fit artifact, not a derived rate.

The Lean skeleton [`QOU/QBeta/QBesselContiguityRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean)
explains *why*: the true fibre kernel is **q-holonomic** — a first-order q-recurrence
with `q^k`-dependent coefficients (Hahn–Exton / Jackson q-Bessel) — of which C-finite
is only the `q→1` rational degeneration. So the right question is not "which constant
`τ`?" but "which **q^k-dependent** recurrence?".

## The formalize-first probe (parameter-free, no fit)

Rather than a wide coefficient search, this probe q-deforms a **proved classical
identity**. Let `S(m) := Σ_{λ⊢m} dim_q(λ)` (so `lw(c) = S(c+1)/(c+1)`). At `q=1`,
`dim_q → f^λ` and the RSK / Schützenberger identity gives

```
  S(m) │_{q=1} = Σ_{λ⊢m} f^λ = I(m) = #{involutions in S_m} = 1,1,2,4,10,26,76,232,764,…
```

a classical **order-2 holonomic (P-recursive)** sequence:

```
  I(m) = I(m−1) + (m−1)·I(m−2).
```

The natural q-deformation (symmetric q-integer `[k]_q = (qᵏ−q⁻ᵏ)/(q−q⁻¹)`):

```
  (H1)   S(m) =?  S(m−1) + [m−1]_q · S(m−2).
```

`(H1)` is parameter-free and falsifiable at every `m`. Three q-integer conventions
were tested (symmetric, asymmetric/Gaussian `(1−qᵏ)/(1−q)`, top-power `q^{m−1}`).

## Result

| check | outcome |
|---|---|
| `q=1` limit = involution numbers (m=0..8) | **✓** (skeleton is correct) |
| `(H1)` exact at seed `m=2,3` | **✓** |
| `(H1)` exact for all `m≤8` (any convention) | **✗** (drifts: rel-residual 0.32%→4.8%) |
| correction `D(m)` has a double root at `q=1`, all `m` | **✓** |

The bare q-involution recurrence is **exact at the seed and drifts beyond** — the same
seed-deep signature as the SL₂ kernel. But the correction term

```
  D(m) := S(m) − ( S(m−1) + [m−1]_q · S(m−2) )
```

is **not noise**. Symbolically (sympy, exact in `q`):

```
  D(2) = D(3) = 0
  D(4) = (q−1)² (q²+q+1) / q²
  D(5) = 2 (q−1)² (q+1)² (q²−q+1) (q²+q+1) / q⁴
  D(6) = (q−1)² Φ₅ · (deg-8 cofactor) / q⁷
  D(7) = 4 (q−1)² (q²+q+1)² (q⁴+q³+q²+q+1) · (palindromic deg-10) / q¹⁰
  D(8) = (q−1)² Φ₃ Φ₅ Φ₇ · (deg-14 cofactor) / q¹⁴
```

Two structural facts, both derived and parameter-free:

1. **Universal `(q−1)²` prefactor.** Every `D(m)` vanishes to second order at `q=1`,
   so the deviation from the classical involution recursion is `O((q−1)²) = O(h²)`.
   The C-finite involution skeleton is therefore *exact* in the classical limit; the
   correction is a pure **fibre / q-deformation** effect.

2. **Cyclotomic factor tower.** The leading factors of `D(m)` are cyclotomic
   polynomials `Φ_d`, and the tower deepens with `m` (`Φ₃`, then `Φ₂Φ₃Φ₆`, `Φ₅`,
   `Φ₃²Φ₅`, `Φ₃Φ₅Φ₇`). `(q−1)²` + cyclotomic is the **Habiro-ring** (cyclotomic
   completion `ℤ[q]^` / `Ẑ[q]`) signature.

## Interpretation and scope (AGENTS.md refuted-claim discipline)

- **(a) scope-limited negative** on the *bare* ansatz: `(H1)` alone does not reproduce
  `S(m)` beyond the seed in any of the three conventions.
- **Positive structural finding** on the *correction*: the lever-1 fibre kernel is the
  q-involution operator **dressed by a cyclotomic (Habiro-class) correction**. This is
  exactly the `q^k`-dependent (q-holonomic) shape `QBesselContiguityRecurrence.lean`
  predicts and the C-finite SL₂ lacked.

This does **not** refute the q-holonomic / Habiro kernel class — it *constrains* it: the
`D(m)` cyclotomic tower is a derived, parameter-free target that any candidate kernel
must reproduce. I explicitly do **not** claim `D(m)` is *purely* cyclotomic — `D(8)`
carries a non-cyclotomic degree-14 cofactor; the witness records the exact
factorizations so the full structure is auditable.

## Why this serves all three levers

- **`z2bn`** (this bean): replaces the falsified C-finite `R(q,x)` with a sharply
  characterized q-holonomic target (involution skeleton + cyclotomic correction).
- **`kehn`** (Q_β / m_n): the c_k closure needs a **Habiro element** `F(q)` whose
  archimedean evaluation supplies the c_k (cf. the α_EM precedent `[2]_q(1−h²α)`,
  PR #1511). The binding-kernel correction landing in the *same* cyclotomic/Habiro
  ring is direct evidence the two closures share an object.
- **`s5bb`** (geometric W_λ): the Habiro-element identification is the medium-term
  keystone blocker; this isolates its ring.

## Next decidable steps (not run here)

1. Fit the `D(m)` cyclotomic cofactors to a **single** q-hypergeometric / Habiro
   element (the contiguity ratio `r_k = −qᵏ/[(1−q^{k+1})(1−a qᵏ)]` template), and
   verify on held-out `m` (the honest q-holonomic guess-and-verify, not a fit).
2. If a single Habiro element reproduces the tower, formalize it as the lever-1 kernel
   alongside `QBesselContiguityRecurrence.lean`, and test whether its archimedean
   evaluation at `q₀` supplies the canonical `c_k` (the `kehn` cross-link).
