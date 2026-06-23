# The cross-atom binding-overshoot trend is REAL (and the "≤2.5% value-band" framing was wrong)

**Date:** 2026-06-23
**Branch:** `claude/binding-overshoot-robustness-2026-06-23`
**Status:** Positive/self-correcting robustness check on the #2635 overshoot trend. No fit; no P_λ.
**Bean:** [`cbnf`](../../.beans/cbnf--categorical-binding-wiring-no-fitting.md)
**Follows:** [`2026-06-23-gap-a3-cross-atom-overshoot.md`](2026-06-23-gap-a3-cross-atom-overshoot.md) (#2635)
**Script:** [`computations/gap_a3_overshoot_robustness_check.py`](../../computations/gap_a3_overshoot_robustness_check.py)

## Why this check

#2635 found the binding overshoot `O(K) = A(K)·tr_M(β_K)/(−B/m_e)` grows with A
(`2.05 → 2.86 → 3.36`). Before any `P_λ` is *derived* to explain that growth, the honest question
(per critical distance): **is the trend real, or an `A(K)` calibration artifact?**

## Correction of an earlier framing

#2631/#2635 reported "overshoot ∈ band from A(D)'s ≤2.5%", treating ≤2.5% as a **value-uncertainty**
on `A(K)`. **That is wrong.** `A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` —
every factor is **exact** at the pinned `q₀` (`[8]_q`, `[3]_q`, `(q^{1/2}+q^{-1/2})` are exact
q-integers; `Vol_hyp(K)` is an exact hyperbolic volume given the knot). So **`A(K)`'s value is exact
and the overshoot is an exact consequence of the canonical inputs.** The "≤2.5%" is the Phase-4
*modeling* accuracy (`A(K) ≈ |Δ_λ*(K)|` — how well the Phase-4 amplitude models the empirical per-block
amplitude), **not** a value-uncertainty. This audit corrects that framing.

## Robustness under the modeling error (treated honestly anyway)

| atom | exact O | per-atom ±2.5% | per-factor indep (±%) | per-factor worst (±%) |
|------|---------|----------------|------------------------|------------------------|
| D | 2.050 | [2.00, 2.10] | [1.92, 2.18] (6.1%) | [1.74, 2.36] (15%) |
| ³He | 2.861 | [2.79, 2.93] | [2.66, 3.06] (7.1%) | [2.29, 3.43] (20%) |
| ⁴He | 3.364 | [3.28, 3.45] | [3.07, 3.66] (8.7%) | [2.35, 4.37] (30%) |

(Per-factor amplification: the ≤2.5% modeling error, if carried *per factor-instance*, compounds
through the exponents `[3]_q^{2(Z-1)}·(q^{1/2}+q^{-1/2})^{4N}` — `n_fac = 6, 8, 12` instances for
D/³He/⁴He; reported under both the independent `√n·ε` and worst-case `n·ε` models.)

- **per-atom ≤2.5%:** all three bands disjoint ⇒ trend fully robust.
- **per-factor, independent:** `D < ³He < ⁴He` both disjoint ⇒ trend robust.
- **per-factor, worst-case linear:** `D→³He` robust; `³He→⁴He` bands overlap ⇒ that step marginal.

## Knot-ID / Vol_hyp sensitivity

`O ∝ Vol_hyp`, so to **flatten** the trend to `O = 2.05` would require:

| atom | Vol_hyp shift |
|------|---------------|
| ³He | 12.554 → 8.99 (**−28%**) |
| ⁴He | 12.554 → 7.65 (**−39%**) |

Such shifts are far beyond any plausible knot-ID ambiguity (the Z-clustering `Vol(D)=Vol(T)`,
`Vol(³He)=Vol(⁴He)` is a structural finding; nearby-knot volumes differ `< 20%`). ⇒ the trend is
**robust against knot-ID / Vol_hyp uncertainty**.

## Verdict

The overshoot is **exact** given the canonical inputs (the `≤2.5% value-band` framing is corrected to
Phase-4 *modeling* accuracy). Its **growth with A is robust** — `D→³He` under every error model and
against Vol_hyp; only the `³He→⁴He` step is marginal under worst-case per-factor amplification. So the
**atom-dependence is a real structural feature, not a calibration artifact** — a future `P_λ`
derivation has a genuine trend to explain (an A-growing net suppression). Deriving that `P_λ` remains
the open GAP-A-3 core; fitting a closed form to it is still the forbidden 7th ansatz.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-23-gap-a3-cross-atom-overshoot.md`](2026-06-23-gap-a3-cross-atom-overshoot.md) — the trend this validates (#2635).
- [`2026-06-22-gap-a3-deuteron-A-D-overshoot.md`](2026-06-22-gap-a3-deuteron-A-D-overshoot.md) — the deuteron overshoot whose "≤2.5% band" framing this corrects (#2631).
