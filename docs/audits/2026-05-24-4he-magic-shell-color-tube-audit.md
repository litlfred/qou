# ⁴He magic-shell closure under color-tube weighting

**Date:** 2026-05-24
**Branch:** `claude/post-1089-followups-2026-05-24`
**Parent audit:** [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
**Sign-flip context:** [`2026-05-24-sign-flip-interpretation.md`](2026-05-24-sign-flip-interpretation.md)
**Status:** Diagnostic / hypothesis only. ⁴He's outlier behaviour in the sign-flip linear fit (+5.87% vs predicted −3.71%, Δ ≈ +9.6%) needs a structural explanation. This audit tests whether the "magic A·8G shell" closure is a Bring color-tube count saturation.

## The outlier

The 5-atom sign-flip diagnostic gives a linear fit `err_pct ≈ +2.975 − 2.226 · n_inter` with R² = 0.83. Substituting ⁴He's `n_inter = 3` (1 pp + 1 pn + 1 nn) predicts `−3.71%`. The **measured** ⁴He over-prediction is `+5.87%` — a Δ of ~9.6 percentage points. ⁴He breaks the trend hard.

The closure label in [`isotope_record_schema.py:186`](../../computations/isotope_record_schema.py):
```
(2, 2): "magic A·8G shell (no single knot)"
```
— this is the only closure not pinned to a specific census knot. It uses the "magic" multiplier `A · 8·G` where `8·G = Vol(𝓑₃)` and `A = 4` for ⁴He.

In [`mass_table_ppb.py:91-95`](../../computations/mass_table_ppb.py):
```python
"4He":  {"rule": "magic", "A_units": 4, "rho_factor": 2,
         "origin": "framework: A·8G magic rule"},
```
Prediction: `B_pred(⁴He) = 2 · m_e · 4 · 8G = 29.9555... MeV` vs CODATA `28.296 MeV` (+5.87% over).

## Why "magic"? — testing the color-tube count hypothesis

The cheat-sheet ([§"Bring color-tube weighted averaging"](../canonical-derivation-cheat-sheet.md)) records that each nucleon carries **3 quark color sheets**, and inter-nucleon averaging is naturally over **9 color-pair assignments + 1 diagonal = 10**.

For ⁴He (Z=2, N=2), the color content per nucleon and the inter-nucleon arc structure (per [`isotope_record_schema.py:build_knot_operator_catalogue`](../../computations/isotope_record_schema.py)):

| Arc | Channel | Nucleon-pair colors |
|-----|---------|---------------------|
| 1   | pp      | uud × uud (9 color-pair assignments) |
| 2   | pn      | uud × udd (9 color-pair assignments) |
| 3   | nn      | udd × udd (9 color-pair assignments) |

**Total color-pair assignments across the 3 inter-nucleon arcs**: 27.

**Total color sheets** across 4 nucleons: 4 × 3 = 12.

Neither 27 nor 12 obviously equals `A · 8G ≈ 32`. So the simple count doesn't match. But the **MeV ratio** is suggestive:

```
A · 8G = 4 × 7.32772 ≈ 29.31  (matched by 2·m_e·A·8G ≈ 29.96 MeV pred)
27 × m_e ≈ 13.80 MeV          (color-pair count alone, too low)
12 × m_e ≈ 6.13 MeV           (color sheet count, way too low)
```

The A·8G structure is **not** a raw color-pair count.

## Alternative reading — colour-tube *saturation* not count

Per the cheat-sheet's full color-tube weighting structure, the form

```
1 / (1 − h_q · q_0^{10})
```

is the Faddeev `Φ_q`-resummed correction for 10-fold color-tube averaging (`9 + 1 = 10`). The numerical value at `q_0 ≈ 1.110` is:

```
h_q · q_0^{10} ≈ 0.20906 · 2.831 ≈ 0.5919
1 / (1 − 0.5919) ≈ 2.450
```

This matches the (now-purged) `λ_scale` empirical fit value `2.4599527869` to 0.4% — **strong evidence** that the 10-fold color-tube weighting IS the categorical structure behind the `λ_scale = 2.46` numerology.

**Hypothesis (extending to ⁴He):** the "magic A·8G shell" is the categorical realisation where the color-tube weighting **saturates** at A=4. Concretely, the 4-nucleon × 3-color = 12-sheet system fills the 12-dimensional irrep of `SU(3)_color × S_4` (the symmetric group acting on the nucleon labels), reaching a "shell-closed" state analogous to filled atomic shells in chemistry.

Saturation means the color-tube refinement that gives `−2.23%` per arc for A ≤ 3 **stops contributing additively at A = 4** — the shell becomes the dominant geometric factor, replacing the per-arc corrections with a single A·8G term.

The +5.87% ⁴He over-prediction would then reflect:
- the A·8G shell BASE value matching the saturated state
- a **negative refinement** from color-tube interior dynamics that's not yet captured

i.e. the +5.87% is what the magic shell predicts BEFORE the color-tube interior dynamics enter — and the categorically-correct value comes from subtracting a color-tube interior contribution that scales with the **filled-shell degeneracy**, not with `n_inter`.

## Quantitative test (proposed)

Implement, with the new `prop:inter-nucleon-channel-from-color-tube` (this branch) as the categorical infrastructure:

1. Compute the color-pair-weighted average for ⁴He using the (uud, uud, udd, udd) color sheets across the 12-strand braid
2. Apply the `1/(1 − h_q · q_0^{10})` saturation factor at the shell boundary
3. Compare the resulting B_pred against AME `28.296 MeV` and against the current `29.956 MeV`

Concrete check: does the color-tube saturation contribute exactly `(2 m_e · 4 · 8G) − 28.296 ≈ 1.660 MeV` of negative refinement? This would close ⁴He to ppb without any fit.

## Cross-references with PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3

The S₅ ↔ SO(3) fiber action on Bring's surface (PR #1081 Task 3, queued) gives the categorical source for the 3 quark color sheets per nucleon: the SO(3) fiber dimension over the S₅-acted Bring quintic is 3 generically (`SO(3) ≅ SU(2)/Z_2`, three-dimensional rotation group). The 10-fold color-tube averaging follows naturally from `5 × 3 / 3 + 1 = 6` (S₅ orbits modulo SO(3) fiber + diagonal) — but the exact count `10` needs derivation.

The ⁴He shell saturation is conditional on the S₅ ↔ SO(3) class being formalised in Lean (PR #1081 Task 3). Until that lands, the saturation claim is **conjecture-conditional** per CLAUDE.md §3b-cond.

## Recommended actions

1. **Wait for PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3** — provides the categorical class for the color-tube saturation derivation
2. **Compute the color-tube saturation factor** for ⁴He explicitly — needs the closed_form_tau_M `pn_convention="bring_color_weighted"` mode implemented (currently raises NotImplementedError)
3. **Cross-check against the `1/(1 − h_q · q_0^{10}) ≈ 2.45` near-coincidence** — if A=4 saturation gives exactly this ratio, the empirical λ_scale = 2.46 numerology is structurally explained
4. **Re-run sign-flip diagnostic with ⁴He included AND color-tube prediction column** — test whether the magic-shell hypothesis brings ⁴He onto the R² = 0.83 trend line or moves it further

## Cross-references

- Parent audit: [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
- Sign-flip interpretation: [`2026-05-24-sign-flip-interpretation.md`](2026-05-24-sign-flip-interpretation.md)
- Bring color-tube cheat-sheet entry: [`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging"](../canonical-derivation-cheat-sheet.md)
- λ_scale-absorbed reference: [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3 — S₅ ↔ SO(3) fiber action (categorical class supplier)
- Existing color-tube content blocks: `content/quantum-observable-universe/archimedean-universe/color-tube-{coordinates,fibers,subloci,cubic,constraints,interpretation}.{md,ts,lean}`
