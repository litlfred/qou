# Strand-doubling Φ_{2^{k+1}} prediction FALSIFIED (2026-06-01)

> Track 3 of PR #1618 ([`docs/coordination/2026-06-01-qbeta-habiro-followup.md`](../coordination/2026-06-01-qbeta-habiro-followup.md))
> tested the falsifiable predictions from the [Φ_8 categorical interpretation
> audit](2026-06-01-qbeta-habiro-phi8-interpretation.md) (on main, post PR #1579):
>
> | Pair (atomic step) | Predicted | Predicted strand count |
> |---|---|---|
> | (³He − D), A=2 → A=3 | `Φ_16 = u^8 + 1` | 8 (B_8) |
> | (⁴He − ³He), A=3 → A=4 | `Φ_32 = u^16 + 1` | 16 (B_16) |
> | (D − n), A=1 → A=2 (reference) | `Φ_8 = u^4 + 1` | 4 (B_4) — confirmed in #1579 |
>
> **The predictions are FALSIFIED.** Both (³He − D) and (⁴He − ³He) carry **Φ_8²**, the SAME factor that appears in (D − n) — not the powers-of-two cyclotomic doubling chain.

## TL;DR

The "strand-doubling cyclotomic chain `Φ_{2^{k+1}}`" hypothesis is **WRONG**. All three atomic-step pairs (D−n), (³He−D), (⁴He−³He) carry `Φ_8² = (u^4+1)²` as their cyclotomic prefactor. The cyclotomic structure is **universal across atomic steps**, not indexed by atomic number via strand doubling.

The Φ_8 categorical interpretation in [`2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md) needs revision:

- The interpretation "Φ_8 = 4-strand B_4 deuteron-specific structure" is too specific — Φ_8² appears for ALL atomic-step pairs tested.
- The structural meaning of Φ_8 is more likely a UNIVERSAL atomic-step / nucleon-pair-binding signature, not a per-atomic-number strand count.
- The algebraic identity `Φ_8(u) = Φ_4(u²)` (Lean-proved in `cyclotomic-strand-doubling.lean`) remains TRUE as an algebraic fact, but its **categorical interpretation as a strand-doubling chain is refuted**.

## Evidence

[`computations/_helium_habiro_coefficient_extract.py`](../../computations/_helium_habiro_coefficient_extract.py) extracted the Habiro coefficients for ³He (M=16) and ⁴He (M=20) via the Phase 5q closed forms:

- `tr_M(³He, q) = τ_p² · τ_n · z(q)²`
- `tr_M(⁴He, q) = τ_p² · τ_n² · z(q)² · (z − h)(q)`

Witnesses:
- [`habiro-coefficients-helium-3.witness.json`](../../computations/habiro-coefficients-helium-3.witness.json)
- [`habiro-coefficients-helium-4.witness.json`](../../computations/habiro-coefficients-helium-4.witness.json)

The cross-pair factorization on these witnesses gave:

| Pair | Σ_m Δa_m·(u;u)_m factorization | Expected (strand-doubling) | Verdict |
|---|---|---|---|
| (D − n) | `−u^15·(u−1)(u+1)·P_8(u)` (from PR #1579) | `Φ_8 = u^4+1` | matches in some sense ✓ |
| **(³He − D)** | **contains `(u^4+1)² = Φ_8²`** | `Φ_16 = u^8+1` | **FALSIFIED** |
| **(⁴He − ³He)** | **contains `(u^4+1)² = Φ_8²`** | `Φ_32 = u^16+1` | **FALSIFIED** |

## What this means structurally

The cyclotomic-prefactor framework documented in PR #1579 needs revision:

**Before (predicted, NOW FALSIFIED):**

| Pair class | Predicted prefactor |
|---|---|
| Single nucleon | Φ_4(u) = u²+1 |
| Isospin doublet (n − p) | Φ_1·Φ_2 = u²−1 |
| A=k → A=k+1 atomic step | Φ_{2^{k+1}} = u^{2^k} + 1 |

**After (observed):**

| Pair class | Observed prefactor |
|---|---|
| Single nucleon | Φ_4(u) = u²+1 (in denominator, still valid) |
| Isospin doublet (n − p) | Φ_1·Φ_2 = u²−1 (classical-limit kill, still valid) |
| A=k → A=k+1 atomic step | **Φ_8² universally** (for k=1, 2, 3 — only tested) |

The categorical content of `Φ_8` is NOT "k=1 step's strand count = 4" but rather a universal feature of nucleon-binding atomic-step differentials. The structural significance of `Φ_8` needs new interpretation.

## Possible re-interpretations

1. **Φ_8 = universal "binding-energy cyclotomic"** independent of atomic number. The 4 primitive 8th roots of unity {ζ_8, ζ_8⁻¹, ζ_8³, ζ_8⁻³} parameterize the nucleon-nucleon interface (2 bar-conjugate pairs = 2 nucleons in the bound state), regardless of how many nucleons are in the bound state.

2. **Φ_8² arises from the z(q)² factor in the Phase 5q closed forms**:
   - `tr_M(D) ∝ z(q)¹`
   - `tr_M(³He) ∝ z(q)²`
   - `tr_M(⁴He) ∝ z(q)²`
   The Pochhammer extraction of `Δa_m` from a `z(q)²`-containing closed form might naturally produce `Φ_8²` regardless of the upstream τ_p, τ_n structure. The `z(q) = 1/(u + u⁻¹)` factor squared = `1/(u + u⁻¹)² = u²/(u² + 1)²` — its denominator is **Φ_4(u)² = (u²+1)²**, which under the substitution u → u² becomes **Φ_8² = (u^4+1)²** in the Habiro-extracted coefficients.

3. **The strand-doubling interpretation collapses to a deuteron-specific accident**: Φ_8² in (D−n) is structural ONLY because the deuteron has 2 nucleons, but for (³He − D) and (⁴He − ³He), the appearance of Φ_8² is an artifact of the Phase 5q closed form's z(q)² factor, not a categorical strand-count statement.

Option (2) is the most likely re-interpretation. The Φ_8² is a **Phase-5q-formula-induced cyclotomic** arising from the z(q)² interface factor, NOT a strand-count signature.

## Implications

1. The Lean theorem `cyclotomic_8_eq_cyclotomic_4_comp_X_sq` in [`content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean`](../../content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean) is **algebraically correct** (`Φ_8(X) = Φ_4(X²)` is a true identity).

2. The categorical interpretation in [`cyclotomic-strand-doubling.md`](../../content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.md) (strand-doubling B_2 → B_4) is **WRONG**. It needs revision to reflect that Φ_8² is a universal binding-energy cyclotomic, not a strand-count.

3. The Φ_16 / Φ_32 falsifiable predictions are **REFUTED**. The cyclotomic-prefactor framework as a "powers-of-two strand-doubling chain" is wrong.

4. The convention-resolution question (Track 1) is now LESS critical: even in the Habiro-witness convention, the strand-doubling chain doesn't work, so the Phase 5q vs Habiro-witness convention question shifts from "does Φ_8² survive" to "is Φ_8² universally present for atomic-step pairs in BOTH conventions".

## Next-action priorities

1. **Revise the Φ_8 audit and the Lean content block** to drop the strand-doubling interpretation and replace it with the more accurate "z(q)² interface-factor cyclotomic" framing.
2. **Test option (2) above**: derive `Φ_8²` from `z(q)² / D_u` algebraically, confirming it arises mechanically from the Phase 5q formula structure.
3. **Re-think the categorical meaning** of Φ_8 in the nucleon-binding framework. It's not strand-doubling; what is it?

## Cross-references

- Falsified hypothesis: [`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md)
- Lean cornerstone (algebra still TRUE): [`content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean`](../../content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean)
- PR #1618 ledger: [`docs/coordination/2026-06-01-qbeta-habiro-followup.md`](../coordination/2026-06-01-qbeta-habiro-followup.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
