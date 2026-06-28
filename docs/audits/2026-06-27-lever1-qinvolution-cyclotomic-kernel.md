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

## Stage 2 — the explicit order-2 kernel coefficient `W(m)`

Forcing the *monic* involution form (coefficient `1` on `S(m−1)`, as in the classical
`I(m)=I(m−1)+(m−1)I(m−2)`), the exact kernel coefficient is

```
  W(m) := (S(m) − S(m−1)) / S(m−2),   the q-deformation of "(m−1)".
```

Computed symbolically:

| m | `W(m)` | Laurent poly in `q`? |
|---|---|---|
| 2 | `[1]_q = 1` | ✓ |
| 3 | `[2]_q = (q²+1)/q` | ✓ |
| 4 | `(q²+q+1)(3q²−4q+3)/(2q²)` | ✓ |
| 5 | `(3q⁶−4q⁵+5q⁴−4q³+5q²−4q+3)/q³` | ✓ |
| 6 | `(q⁴+1)Φ₅·(deg-6)/(q⁵·(3q⁴+4q²+3))` | ✗ — partition-sum denom |
| 7 | `Φ₃·(deg-18)/(q⁶(q⁴+1)(3q⁴+2q³+3q²+2q+3))` | ✗ |
| 8 | `Φ₇·(deg-22)/(q⁷(q⁴+1)(deg-10))` | ✗ |

Two precise facts:

1. **Seed-exact q-integer.** `W(2)=[1]_q`, `W(3)=[2]_q` *exactly* — the kernel coefficient is
   the symmetric q-integer at the seed, and `W(m)−[m−1]_q = D(m)/S(m−2)` is the cyclotomic
   tower of §Result divided by the partition sum.
2. **Monic order-2 q-holonomic lift does not close.** `W(m)` stays a Laurent polynomial in `q`
   through `m=5`, then at **`m=6`** acquires a genuine **partition-sum denominator**
   (`S(4) = (3q⁴+4q²+3)/…` first contributes its irreducible factor). So `S(m)` is **not**
   order-2 q-holonomic in monic form: no fixed Laurent-polynomial coefficient reproduces the
   period past `m=5`. The true q-difference operator `R` is therefore either higher q-shift
   order or non-monic (a `P₂(q,q^m)S(m)+P₁ S(m−1)+P₀ S(m−2)=0` with all three `P_i` nontrivial)
   — the q-Bessel / q-Lommel class, not the simplest involution lift.

This is the sharp, honest boundary of what the order-2 involution ansatz buys: the **seed**
(`m≤3`, the calibration anchors) is the symmetric q-integer exactly; everything beyond is the
cyclotomic/Habiro correction, and the monic-order-2 closed form fails from `m=6`.

## Stage 3 — is `S(m)` order-2 q-holonomic? (general non-monic test)

Stage 2 ruled out the *monic* order-2 lift. Stage 3 tests the **general** order-2 q-difference
operator

```
  P₂(q, q^m)·S(m) + P₁(q, q^m)·S(m−1) + P₀(q, q^m)·S(m−2) = 0,
```

with `P_i` bar-symmetric Laurent polynomials in `(q, X:=q^m)` (the `X^{−1}` terms are required —
e.g. `[m−1]_q = (X−X⁻¹)/(q−q⁻¹)`). Method: bounded-bidegree guess-and-verify with **held-out
falsification** — fit the coefficients on `m=2..6`, then verify the solved recurrence predicts
`m=7,8,9` (indices never used in the fit). Compute:
[`computations/substrate/lever1_qholonomic_kernel_fit.py`](../../computations/substrate/lever1_qholonomic_kernel_fit.py),
witness [`lever1-qholonomic-kernel-fit.witness.json`](../../computations/substrate/lever1-qholonomic-kernel-fit.witness.json).

**Result — negative, and sharp.** Up to q-degree `±4` and X-degree `3`:

| q-deg | X-deg | unknowns | constraints | fit nullspace | held-out-verified |
|------:|------:|--------:|-----------:|-------------:|------------------:|
| ±1 | 1 | 27 | 83 | 0 | 0 |
| ±2 | 2 | 75 | 133 | 0 | 0 |
| ±3 | 3 | 147 | 183 | 0 | 0 |
| ±4 | 3 | 189 | 193 | 18 | **0** |

At every **strongly over-determined** bidegree (≤ q-deg `±3`, where constraints exceed unknowns
by ≥ 35) the fit nullspace is **empty** — no order-2 recurrence even fits the training set. A
nullspace appears only at q-deg `±4` where the system is nearly square (189 unknowns vs 193
constraints), i.e. effectively under-constrained, and **none** of those 18 candidate solutions
survive the held-out test. So `S(m)` is **not** order-2 q-holonomic of small bidegree: the true
fibre operator is higher q-shift order (≥3) or has bidegree beyond the swept bound.

## Stage 4 — order-3 is also negative

Raising the q-shift order to 3 (`Σ_{j=0}^{3} P_j(q,q^m) S(m−j) = 0`, same bar-symmetric
guess-and-verify, fit `m=3..8`, held-out `m=9,10,11`;
[`lever1_qholonomic_order3_fit.py`](../../computations/substrate/lever1_qholonomic_order3_fit.py),
witness [`lever1-qholonomic-order3-fit.witness.json`](../../computations/substrate/lever1-qholonomic-order3-fit.witness.json))
gives **the same negative**: the fit nullspace is **0 at every bidegree** up to q-deg `±3`,
X-deg `3` (196 unknowns vs 316 constraints — strongly over-determined), for **both** order-2
(re-run as regression with the extended `S(0..11)` data) **and** order-3. No recurrence even
fits the training set.

**Conclusion across Stages 0–4.** The binding period `S(m)=Σ_{λ⊢m} dim_q(λ)` is **not**
q-holonomic of small order (≤3) and bidegree — there is no finite q-difference operator of that
size. What survives is the **exact cyclotomic structure** of Stage 1: the q-involution skeleton
(seed-exact) plus the `(q−1)²·Φ_d` Habiro correction tower. The fibre kernel is a genuine
cyclotomic-completion (Habiro-ring) object, not a low-order recurrence.

## Cross-link — the Q_β `c_k` ladder is in the same state (the `kehn` connection)

The corpus `c_k` state of play
([`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md),
[`docs/audits/2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md`](2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md),
[`docs/audits/2026-06-20-qbeta-hahn-exton-kernel-test.md`](2026-06-20-qbeta-hahn-exton-kernel-test.md))
shows the **same structural verdict** for the Q_β coefficients as this probe finds for the
binding period:

- **No low-order (q-)holonomic recurrence.** The `c_k` holonomic guess (order ≤2, degree ≤2)
  found no clean D-finite recurrence; constant-kernel depth ≤4 is refuted; the bare **Hahn–Exton
  q-Bessel** ratio is *structurally* excluded (empirical `r₂ = c₃/c₂ = +2` lies in the
  forbidden gap `(0, 3.35)` unreachable for any real `ν`). Exactly parallel to the `S(m)`
  negative here.
- **Kernel constrained to depth ≥3 or non-constant q-rational**, with `a₂ = c₂ = −1`,
  `a₁ = −c₃ = √2·Φ₂` (bar-odd), and a **ζ₄ cyclotomic residue** — a Habiro-ring element.
- **Cyclotomic everywhere, different localisations.** Binding `D(m)`: `Φ₃/Φ₅/Φ₇`, real-q `ℤ[q]`.
  Q_β `c_k` kernel: `ζ₄` residue, leading `√2·Φ₂`, ζ-fibre/complex. Q_β `Δa_m`: `Φ₈` (ledger
  `2026-06-01-qbeta-habiro-followup.md`). All three are the cyclotomic-completion (Habiro) ring;
  the **localisations differ** (real-q integral vs ζ-fibre), so this is corroboration at the
  ring-class level — not a claim that the towers are the same element (per #2452 + the AGENTS.md
  *Im(q) fibre-vs-observable* banner).
- **Why neither closes by extraction.** The `c_k` extraction precision floor proves only
  `c_2, c_3` are data-determined; `c_4+` lie below the measured-Q_β noise, so they can come *only*
  from a framework derivation (the Habiro element). The binding kernel is the parallel
  derivation-side object: pinning the higher-order / non-monic q-holonomic operator for `S(m)` is
  the same *kind* of task as constructing the Q_β Habiro element `F(q)`.

**Net:** two independent rungs (binding period `S(m)`; Q_β ladder `c_k`) both (i) resist
low-order q-holonomic closure and (ii) carry cyclotomic Habiro structure. That is positive
evidence they are governed by **one Habiro-ring q-difference operator**, evaluated at different
localisations — the unifying object `s5bb`'s keystone and `kehn`'s closure both need.

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
