# Δ_λ parity exclusion (GAP-1) + three ties to the Δ_λ frontier

**Date:** 2026-08-01 · **Branch:** `claude/deltalambda-parity-exclusion-2026-07-26` · **PR:** #4399 ·
**Builds on:** #4387 (deuteron signed conjugation parity) · **Axis:** Δ_λ binding — μ₀ −9% closure ·
**Tier:** scope-(b) structural exclusion (Lean-proved) + 30-dps classification + three frontier ties
(**no fit**; nothing wired).

## 1. The exclusion (the GAP-1 result)

From #4387, the deuteron binding `B = m_e Σ_{λ⊢6} T_λ Δ_λ` (`T_λ = w_λ χ^λ`) splits by *signed*
conjugation parity, `T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q)`. For the deuteron `n = 6` (sgn `= −1`) the
bar-even total is `∝ Σ_λ T_λ (Δ_λ − Δ_{λ'})`, so:

> **Any conjugation-symmetric dressing `Δ_λ = Δ_{λ'}` gives `g₂ = 0`.** Since `g₂ ≈ 1 ≠ 0`, no
> conjugation-symmetric `Δ_λ` can produce the deuteron's bar-even binding — a scope-(b) exclusion
> (proved invariant: conjugation symmetry ⇒ zero bar-even).

Lean-proved sorry-free
([`ConjugationSymmetricDeltaExcluded.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationSymmetricDeltaExcluded.lean):
`barEvenTotal_symmetric_zero_deuteron`, `barEven_nonzero_implies_asymmetric`). Verified 30 dps
([probe](../../computations/deltalambda/deltalambda_conjugation_symmetric_excluded_probe.py)): the
**Markov weight `w_λ`**, **classical `dim(λ)²`**, and **hook-form q-dimension** are all
conjugation-symmetric ⇒ **excluded**; the conjugation-**covariant Wenzl principal specialization**
survives.

## 2. Tie A — consistency with the W_λ q-Plancherel refutation (n-parity regimes)

The A=3 magnitude work ([`2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md),
Route 1) refuted `W_λ = d_q(λ)²/[n]_q!` (q-Plancherel) as the H₉ re-weight — it overshoots `33×`. There
is **no conflict** with this exclusion: A=3 is `n = 9`, `sgn = (−1)^{8} = +1`, the *opposite* parity
regime, where a conjugation-symmetric `Δ` does **not** kill the bar-even channel. The exclusion here is
specifically the **even-A** statement (deuteron `n=6`, helium `n=12`; `sgn = −1`). The two findings are
complementary, not contradictory — and both point away from the symmetric q-Plancherel weight toward
the covariant principal specialization (`y_λ`, the production weight).

## 3. Tie B — the weight bar-sign IS the Milnor-parity deficit sign `(−1)^{A−1}`

The weight bar-sign is `sgn = (−1)^{n-1}` at `n = 3A`, and `(−1)^{3A−1} = (−1)^{A−1}` — **exactly** the
A-indexed deficit sign of the Milnor-parity sign law
([`2026-07-27-deltalambda-milnor-parity-sign-law.md`](2026-07-27-deltalambda-milnor-parity-sign-law.md),
#4389: A=3 → `+`, A=4 → `−`). Verified `A = 2,3,4`:

| A | n=3A | weight bar-sign `(−1)^{n-1}` | Milnor deficit `(−1)^{A−1}` |
|---|------|------------------------------|------------------------------|
| 2 | 6 | `−` | `−` |
| 3 | 9 | `+` | `+` |
| 4 | 12 | `−` | `−` |

**Scope (honest, scope-(a)):** this is a **structural convergence**, not (yet) a proved derivation. The
weight bar-sign governs the bar-parity of the Wedderburn sum `tr_M`; the Milnor deficit sign governs
the leading coefficient of the A-body cluster deficit `1 − τ_A`. That both equal `(−1)^{A−1}` is a
strong hint that the cluster sign law *descends from* the `(q−q⁻¹)^{n-1}` Markov-weight parity — a
candidate derivation of the sign #4389 left **measured** for A=4. It is recorded as an observation and
a derivation target; it is **not** claimed proved.

## 4. Tie C — independent geodesic-side parity constraint (#4401 winding-parity)

Per sibling coordination on this PR, #4401 (merged) supplies an *independent* parity constraint on the
same Δ_λ search from the **geodesic/winding side**: `prop:winding-lattice-norm-form` +
`rem:winding-parity-sign-transport` + Lean `QOU.QBeta.WindingLatticeNormForm` (incl.
`norm3_ne_neg_one`, a disc-12 structural exclusion). Both constraints **select against symmetric
candidates**; their natural meeting point is the surviving **Wenzl principal specialization**. This
audit cross-cites #4401 as requested; the two parity mechanisms (partition-side conjugation here;
geodesic-side winding there) are complementary scope-(b) narrowings.

## 5. Net + scope

| statement | status |
|---|---|
| conjugation-symmetric `Δ_λ` ⇒ `g₂ = 0` (even-A) | **Lean-proved, scope-(b)** |
| Markov `w_λ` / `dim²` / hook-q-dim excluded; principal specialization survives | **verified 30 dps** |
| consistency with the W_λ q-Plancherel refutation (opposite n-parity at A=3) | **confirmed** |
| weight bar-sign `= (−1)^{A−1} =` Milnor deficit sign | **convergence (scope-(a)); candidate derivation, not proved** |
| independent winding-parity constraint (#4401) meets at principal specialization | **cross-cited** |
| the `Δ_λ` **magnitudes** | **OPEN — Track-A gate** |

The exclusion narrows the `Δ_λ` search (symmetric families out; covariant class in) and now sits
inside a coherent multi-constraint picture (partition parity + winding parity + the A-indexed sign
law), all pointing at the Wenzl principal specialization. No fit; nothing wired; the magnitudes remain
the gate.

Refs: probe
[`deltalambda_conjugation_symmetric_excluded_probe.py`](../../computations/deltalambda/deltalambda_conjugation_symmetric_excluded_probe.py);
Lean [`ConjugationSymmetricDeltaExcluded.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationSymmetricDeltaExcluded.lean),
[`ConjugationParitySplit.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationParitySplit.lean);
#4387 (signed conjugation parity); #4389 (Milnor-parity sign law); #4401 (winding-parity); the A=3
three-walls magnitude audit.
