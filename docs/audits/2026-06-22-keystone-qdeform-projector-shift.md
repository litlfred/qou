# The q-deformed E_λ-projected shift is non-null but O(1) and bar-mixed — not the 210 ppb muon mechanism

> **🛑 CORRECTED 2026-08-30 — `y_(3,1,1)^{H5}` is EXACTLY ZERO, not 0.0167666.**
> The figure below came from `ph.trace_weights_n(5, float(q))`, whose `float(q)`
> downgraded the 50-dps pin to 53 bits; the routine is float64 internally, so the
> result was then dressed as 50 dps by `mpf(str(w))`. Recomputed in exact
> arithmetic (`y_lambda_wenzl_bridge_numeric`), **four of the seven `y_λ` are
> exactly 0** — (3,1,1), (2,2,1), (2,1,1,1), (1⁵) — while the three nonzero ones
> agree to 14 digits. The zeros are structural: `y_λ = 0` iff λ has **more than
> two rows**, the SU(2)/N=2 truncation.
>
> Consequence for what is below: the "electron home-block" (3,1,1) carries **no
> Markov weight at all**, so `T_electron = 0` exactly and `δ = T_μ` trivially.
> Any (3,2)-vs-(3,1,1) shift computed here is `T_μ` under another name. The
> producer is fixed; the numbers in this document are left as the historical
> record. Beans `qou-j3u0` (the finding) and `qou-bake` (the witness has no
> producer and cannot self-refresh).
>
> **Re-derived under `W_λ` (2026-08-30, `computations/probes/keystone_wlambda_vs_ylambda_projected_shift.py`).**
> The keystone's own block weight `W_λ = d_q(λ)²/[n]_q!` is nonzero on all seven
> blocks and conjugation-symmetric (the Lean-proved C2), and it is what the
> C1/C2/C6 obligations are stated over. With it the muon/electron comparison is
> well-posed on both sides:
>
> | | `W_λ` | `χ^λ(β_Bor)` | `T = W·χ` |
> |---|---|---|---|
> | muon (3,2) | 0.207542204506 | 4.9883716259599 | 1.0352976441462 |
> | electron (3,1,1) | 0.294668956300 | 5.9883716259599 | 1.7645872169611 |
>
> `δ = T_μ − T_e = −0.72928957281492`, `δ/T_μ = −0.7044250288`, and
> `|δ/T_μ| / 210 ppb = 3.3544e6×`.
>
> **Of the two legs of the #2584 refutation, one survives and one does not.**
> The magnitude leg **survives** (3.35e6×, ~6.5 orders). The bar-parity leg
> **fails**: `δ(q) − δ(1/q) = 4.0091471e-50` at dps = 50, i.e. the shift is
> **exactly bar-EVEN**, not bar-mixed. The "bar-mixed" reading came from this
> document's `y_λ`-derived numbers, which are the float64-corrupted ones
> (`qou-j3u0`).




**Date:** 2026-06-22
**Branch:** `claude/keystone-qdeform-projector-shift-2026-06-22`
**Status:** Negative / sharpening — the last well-posed "remaining" object from the
first-crack doc is run and refuted as the 210 ppb mechanism. No fit, nothing wired.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md) (q-deformed closure)
**Tool:** `pyhecke_native` v0.9.0 (built in-sandbox, ~42 s, PR #2511 recipe)
**Follows:** [`2026-06-20-keystone-branching-shift-first-crack.md`](2026-06-20-keystone-branching-shift-first-crack.md)
**Script:** [`scripts/keystone_qdeform_projector_shift_probe.py`](scripts/keystone_qdeform_projector_shift_probe.py)

## What was run

The functor-resolution doc
([`2026-06-13`](2026-06-13-s5-so3-fiber-action-functor-resolution.md)) §4 step 2 asks
for the shift in the Borromean Markov trace through the muon projector `E_(3,2)` (ℓ=2)
versus the electron projector `E_(3,1,1)` (ℓ=1). The **first-crack** probe weighted the
h⁴-bearing (2,1) channel by the *generation-independent* H₃ weight `y_ν^{H3}` × the
classical branching multiplicity 2, so the (2,1) term was identical in both generations
and **cancelled** — and explicitly flagged the remaining object:

> whether the q-deformed Wenzl projector weights `w_λ(q)` — as opposed to classical
> multiplicities — break the (2,1) symmetry between the H₅ blocks.

This probe runs that object: the **E_λ-projected H₅ Markov trace** of the Borromean
braid embedded in B₅,

$$T_g = \mathrm{tr}_M^{H_5}\!\big(E_{\lambda_g}\,\iota(\beta_{\mathrm{Bor}})\big)
      = y_{\lambda_g}^{H_5}\cdot\chi^{\lambda_g}\!\big(\iota(\beta_{\mathrm{Bor}})\big),
\qquad \beta_{\mathrm{Bor}}=(\sigma_1^{-1}\sigma_2)^3 .$$

The branching is automatic inside `χ^λ`; the (2,1)/h⁴ channel is present in both
generations but weighted by the **differing** H₅ home-block weights.

## Results (q₀ = 1.1099785955541805, dps = 50)

**Branching cross-check (validates the Rust H₅ character):**

| identity | residual |
|----------|----------|
| `χ^(3,2)(β)   − [χ_(3) + 2χ_(2,1)]` | 9.6 × 10⁻⁵⁰ |
| `χ^(3,1,1)(β) − [χ_(1,1,1) + 2χ_(2,1) + χ_(3)]` | 9.6 × 10⁻⁵⁰ |

So `pyhecke_native`'s 5-strand `χ^λ` reproduces the S₅→S₃ branching to machine zero —
`χ^(3,2)=4.98837`, `χ^(3,1,1)=5.98837` (the latter's extra `+1` is the (1,1,1) sign
channel), with `χ_(2,1)=2−3h⁴−h⁶=1.99419` carrying the Borromean h⁴.

**The projected traces and their shift:**

| quantity | value |
|----------|-------|
| `y_(3,2)^{H5}` / `y_(3,1,1)^{H5}` | 0.0617237 / 0.0167666 |
| `T_muon = y_(3,2)·χ^(3,2)` | 0.3079008 |
| `T_electron = y_(3,1,1)·χ^(3,1,1)` | 0.1004047 |
| `δ = T_μ − T_e` | **0.2074961** |
| `δ / T_μ` | 0.6739 |
| `δ / T_e` | 2.0666 |

**Magnitude vs the 210 ppb target (not a fit):**

| shift | / 210 ppb |
|-------|-----------|
| `δ/T_μ` | 3.21 × 10⁶ × too large |
| `δ/T_e` | 9.84 × 10⁶ × too large |

**Bar-parity (q ↦ q⁻¹):** `δ(q₀)=0.20750`, `δ(1/q₀)=0.36549`;
`δ(q)+δ(1/q)=0.573 ≠ 0`, `δ(q)−δ(1/q)=−0.158 ≠ 0` ⇒ **bar-MIXED** (neither even nor odd).

## Verdict — non-null mechanism, but not the 210 ppb shift

1. **The mechanism is real (positive structural finding).** Unlike the first-crack
   Model A, the q-deformed E_λ-projected trace does **not** cancel the (2,1)/h⁴ channel:
   weighting by the home-block weight `y_λ^{H5}` (0.062 vs 0.017) breaks the symmetry the
   classical multiplicity preserved. So the "q-deformed projector weight" object the
   first-crack doc flagged as not-yet-run is **non-trivial** — `δ ≈ 0.207`.

2. **But it is O(1), not 210 ppb.** The shift is 67 % of `T_μ` (or 2.07× `T_e`) — **6–7
   orders of magnitude too large** to be the 210 ppb muon figure. It is also neither the
   207× generation ratio (`T_μ/T_e ≈ 3.07`, not 207) — so the projected trace does not by
   itself reproduce `m_μ/m_e` either.

3. **bar-MIXED disqualifies it as a fine correction.** The first-crack doc requires any
   sub-ppm correction candidate to be **bar-even**. `δ` is bar-mixed, so even setting
   magnitude aside it cannot be the bar-even fine correction.

**Net:** the operator-valued projector weighting — the last well-posed object the
first-crack doc left open — is **non-null but is not the 210 ppb mechanism** (wrong by
6–7 orders, bar-mixed, and not the generation ratio). This **confirms the anchor-shift
framing once more**: 210 ppb is a re-pin artifact, not a block-selection / projector-weight
effect. The q-deformed closure of `conj:s5-so3-fiber-action`, if it exists, is **not** at
the projector-weight level — every Markov-trace-level object (multiplicity, home-block
weight, projected trace) is now either cancelling or O(1)-and-bar-mixed.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored. The owner closes the bean (§4a).

## What remains (for the record, not run here)

The Markov-trace surface is exhausted for this mechanism. Any surviving q-closure
route would have to leave the Markov-trace weighting entirely — e.g. a Reeb/Casimir
geometric level functional (cf. the `Reeb-Casimir level ⊕ chirality` Lean separation of
the five A₅ irreps, main `8f343e10`) acting *before* the trace, not a reweighting of it.
That is a different object and is not in scope here.

## Cross-references

- [`2026-06-20-keystone-branching-shift-first-crack.md`](2026-06-20-keystone-branching-shift-first-crack.md) — the first crack; flagged this object as remaining.
- [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md) §4 — the spec.
- [`2026-06-20-pyhecke-native-build-unblocked.md`](2026-06-20-pyhecke-native-build-unblocked.md) — the tool build.
- [`computations/keystone-qdeform-projector-shift.witness.json`](../../computations/keystone-qdeform-projector-shift.witness.json) — machine-readable result.
