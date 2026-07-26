# Δ_λ μ₃: the Borromean (Brunnian) irreducible 3-body cluster supplies the
# forbidden `+` sign — a derived positive-sign LEAD (scope-(a)), not a closure

**Date:** 2026-07-26
**Branch:** `claude/deltalambda-borromean-3body-cluster-2026-07-26` · PR #4360
**Verdict:** **DERIVED POSITIVE-SIGN LEAD (scope-(a))** — 0 free parameters.
The Borromean irreducible 3-body cluster `c₃^Borr > 0` supplies exactly the
`μ₃ = +0.4708 > 0` sign that the *multiplicative* pairwise route provably
**cannot** (#4354). **Not** a Δ_λ closure: the sign is fixed, the per-λ
magnitude is not (bare-`H₃` scale `~0.006 MeV` ≪ target). Machine-checked
sorry-free.

---

## 1. The one open door (#4354)

`QOU.MassTheory.Mu4RhoFCluster` (#4354, sorry-free) proved a 3-body **sign wall**:
the beyond-pairwise (Ursell) content of *any* multiplicative interface product
`1 − ∏ᵢ fᵢ`, `fᵢ ∈ [0,1]`, is `≤ 0` (`pairwise_3body_content_nonpos`), and the
only escape `fᵢ > 1` is foreclosed by `markovParam_le_half` (`z ≤ ½ < 1 ∀ q>0`).
Yet the Δ_λ residual simplex (#4320, `AdditiveResidualSimplex`) needs

    μ₂ = 0,   μ₃ = +0.4708  (> 0),   μ₄ = −4.591.

The **derived** pairwise `ρ_F` cluster is `c₃ < 0` (⟨T,³He⟩ = −1.59 MeV,
`three-body-joint-trace-a3.witness.json`). Surviving door: a
**non-multiplicative, enhancing** 3-body operator.

## 2. The candidate — the Borromean irreducible operator (0 free params)

The Borromean rings `𝓑₃` are the archetype of a **Brunnian** 3-body object:
three components, every 2-sub-link *trivial* (unlinked), yet the whole genuinely
3-body linked. Consequences, both structural:

1. **Non-multiplicative by construction.** Every pairwise sub-link is trivial, so
   the pairwise (multiplicative) binding vanishes — matching the #4354 wall
   exactly — and the *whole* binding content is the irreducible 3-body cluster.
2. **Parameter-free.** It is not a tunable ansatz: it is *the* `𝓑₃` object, the
   mass formula's `Vol(𝓑₃)·ρ` trace, GAP-A-4 Lean closed form
   (`QOU.BraidsAndKnots.BorromeanMarkovTrace`):

       τ_Borr(h) = (4 + h² − 3h⁴ − h⁶)/(h² + 4),   h = q − q⁻¹.

## 3. The Ursell decomposition for a Brunnian object

Connected 3-body cluster, binding units (framework `B = E₀·(tr_free − tr_atom)`,
positive when a link *reduces* the trace):

    c₃ = joint − pair_sum − 1body_baseline.

For Borromean, every 2-sub-link is trivial ⇒ `B_a = B_b = B_c = 0` (pairwise
binding vanishes) ⇒ the connected 3-body cluster is the **full** irreducible
content against the 3-component unlink `τ_free = τ(0) = 1`:

    c₃^Borr = E₀·(τ_free − τ_Borr) = E₀·(1 − τ_Borr).

**Closed form** (probe + Lean `one_sub_tauBorromean`):

    1 − τ_Borr = (3h⁴ + h⁶)/(h² + 4) = h⁴(3 + h²)/(h² + 4)  ≥ 0  ∀ real h,

strictly `> 0` for `h ≠ 0` (`q ≠ 1`). This positivity is **unconstrained by the
`markovParam z ≤ ½` argument** — that bounds *multiplicative* pairwise products;
the Borromean object is irreducible, not a product of pairwise `fᵢ`.

## 4. Compute (0-fit, q₀-only)

`computations/deltalambda/borromean_3body_cluster_sign_probe.py`
(`borromean-3body-cluster-sign.witness.json`), q₀ = 1.10997858…, E₀ = 4.18598 MeV:

| quantity | value | sign |
|---|---|---|
| τ_Borr | 0.99856216 (matches recompute's 0.9986 < 1) | — |
| 1 − τ_Borr = h⁴(3+h²)/(h²+4) | 0.00143784 | — |
| **c₃^Borr (raw-trace)** = E₀·(1−τ_Borr) | **+0.006019 MeV** | **+** |
| c₃^Borr (Li₂^q g-channel) | +0.001042 MeV | + |
| pairwise ρ_F c₃ (⟨T,³He⟩) | −1.587 MeV | − (#4354 wall) |
| target μ₃ | +0.4708 | + |

**Sign gate (normalization-free — the honest gate):** `c₃^Borr > 0` **matches**
`μ₃ > 0`; the pairwise route's `c₃ < 0` does not (proved #4354).

**Magnitude (honest, NOT the gate — μ₃ dimensionless, c₃ in MeV):** bare-`H₃`
`c₃^Borr ≈ 0.006 MeV` is `~78×` below `+0.4708` (read as MeV) and `~264×` below
the `ρ_F ~1.5 MeV` scale. So the operator supplies the *sign*, not the *scale*.

## 5. Formalize-first (machine-checked sorry-free)

`QOU/MassTheory/BorromeanThreeBodyCluster.lean` — verified `lean`-direct
(exit 0, lean-v4.24.0, restored `lake-cache/qou-v4-24-0` Mathlib.Tactic cone):

| lemma | content |
|---|---|
| `one_sub_tauBorromean` | `1 − τ_Borr = h⁴(3+h²)/(h²+4)` |
| `tauBorromean_le_one` / `_lt_one` | `τ_Borr ≤ 1` (`< 1` for `h ≠ 0`) |
| `borromean_cluster_nonneg` / `_pos` | `c₃ = E₀·(1−τ_Borr) ≥ 0` (`> 0` physical) |
| `mu3_sign_compatible_with_borromean_cluster` | `μ₃ > 0 ∧ c₃ > 0` (same side) |

This is the **forward complement** of `Mu4RhoFCluster.pairwise_3body_content_nonpos`
(`≤ 0`): *multiplicative ⇒ cluster ≤ 0; Brunnian-irreducible ⇒ cluster ≥ 0.* The
`μ₃ > 0` sign therefore **selects** the Brunnian (non-multiplicative) operator.
`μ₃`'s numerical value enters neither statement nor proof — sign only.

## 6. Verdict + discipline (STRICT)

**DERIVED POSITIVE-SIGN LEAD (scope-(a)).** `c₃^Borr = E₀·(1 − τ_Borr) > 0` from
the parameter-free `𝓑₃` trace (0 fit) supplies the `μ₃ > 0` sign the pairwise
multiplicative route provably cannot. Being non-multiplicative, its sign is not
bounded by the `z ≤ ½` wall.

**NOT a closure.** The bare-`H₃` magnitude `~0.006 MeV` is far below the
`+0.4708`/`~1.5 MeV` target scale. Any level-lift or enhancement factor tuned to
hit the target would be a **FIT** — not made, not wired. Δ_λ remains **open**
(per-λ, 2 anchors, sign ≠ full magnitude). The "no seventh fit-based ansatz" gate
and the PROBE-4 KL-positivity prune stand.

**Anti-fit note.** `τ_Borr` is q₀-only, 0 free parameters (it *is* the `𝓑₃`
object). `μ₃` enters only as the target sign; no normalization is wired. Nothing
downstream consumes this result.

## 7. What this changes / what remains open

- **Changed:** the standing "the 3-body cluster sign is open" statement is now
  *resolved for the Brunnian operator* — its sign is `+`, proved. The enhancing
  operator #4354 left open is **identified** (the Borromean/Brunnian irreducible
  cluster) and its sign is the one `μ₃` needs.
- **Open:** the **magnitude**. The bare-`H₃` Brunnian cluster is `~78×` too small.
  A derived level-lift (`H_9` embedding / the `g`-channel at the physical strand
  count, the s5-so3 `W_λ` index) *might* raise the scale — but only a **derived**
  lift qualifies; a tuned one is a fit. This is the next derive-or-refute target,
  co-scoped with `option-e` (magnitude side) and the s5-so3 keystone.

## Cross-references
- Wall complemented: `QOU/MassTheory/Mu4RhoFCluster.lean` (#4354), audit
  `docs/audits/2026-07-26-…` (the #4354 μ₄ redirect / 3-body sign exclusion split)
- Residual moments: `QOU/MassTheory/AdditiveResidualSimplex.lean` (#4320)
- Borromean closed form: `QOU/BraidsAndKnots/BorromeanMarkovTrace.lean` (GAP-A-4)
- Δ_λ magnitude side: `docs/coordination/option-e.md`
- Probe/witness: `computations/deltalambda/borromean_3body_cluster_sign_probe.py`
  · `borromean-3body-cluster-sign.witness.json`
