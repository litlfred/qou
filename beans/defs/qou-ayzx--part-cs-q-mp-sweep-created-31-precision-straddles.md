---
# qou-ayzx
title: 'Part C''s Q_MP sweep created 31 PRECISION STRADDLES: mpmath side moved to 70 digits, sympy side left at 50'
status: todo
type: task
created_at: 2026-11-21T04:30:36Z
updated_at: 2026-11-21T05:05:00Z
parent: qou-9nnz
---


**Owner ruling 2026-11-21: option D — fix at the producers, not by widening a tolerance.** Recorded on the card that offered A (carve the file out), D, B (leave it red) and a tolerance widen; the owner chose **D**.

## What the sweep did

`e925b93b8fb` ("carry q at 70 digits, not 50, in the 588 non-deliberate consumers") rewrote `mp.mpf(Q_50_DIGIT_STR)` → `Q_MP` in 588 files. Its patcher keyed on the **mpmath** spelling and was blind to the **sympy** one. Measured tree-wide (excluding `fsh-guts/`, `qou-mass/`):

| population | files |
|---|---:|
| build a sympy value from `Q_50_DIGIT_STR` (`sp.Rational` / `sp.Float` / `sp.sympify`) | **115** |
| of those, **no** `Q_MP` — self-consistent at 50 digits, not a defect | 74 |
| of those, **also** `Q_MP` — a **STRADDLE** | **37** |
| of those straddles, **created by this sweep** (it added the `Q_MP`) | **31** |

So each of 31 files previously carried `mp.mpf(Q_50_DIGIT_STR)` **and** `sp.Rational(Q_50_DIGIT_STR)` — consistent at 50 digits. The sweep moved only the mpmath side to 70, so each now computes **one quantity from two different values of `q`**, a `2.13e-50` gap. That is the defect AGENTS.md names under the two-layer convention: *"Never straddle the two layers inside one quantity … a defect regardless of its size."*

## Why only one of 588 "failed"

`computations/probes/two_nucleon_binding_law_comparison_probe.py` is the only one whose assertions are tight enough to notice. It cross-checks freshly-computed values against two committed witnesses at a hardcoded `tol = 1e-50`, and three checks broke: `H6_traces_match_nn_pn_witness`, `D2_log_matches_template_witness`, `D4_ratios_match_isospin_witness`.

**There is no physics disagreement.** The two sides agree to **48–49 significant digits** (`pp` reads `2.071041492871493336856` on both) and differ by `4.3e-49`, against a `1e-50` **absolute** tolerance on quantities of magnitude 0.2–3.8 — i.e. it demands ~51 significant digits.

**Attribution is measured.** Reverting *only* the one `q = Q_MP` line gives **8/8 pass, exit 0**. Of the 5 patched files with a tolerance ≤1e-50, only **2** also read a committed witness, and the other (`delta_lambda_mirror_symmetry_probe`) passes 15/15 because its checks are exact symmetry equalities.

## Two attempted fixes, both measured, both insufficient

- **Refresh the upstream witnesses so both sides share the 70-digit frame.** *Improves* D2 (`4.3e-49 → 1.5e-49`) but pushes `tr_free[pp]` across the line (`4.59e-50 > 1e-50`) and **breaks H6**. No refresh order makes all three pass.
- **Close the straddle in the comparison probe alone** (`QV` built from `mp.nstr(Q_MP, DPS+10)`; round-trip gap to `Q_MP` goes `2.13e-50 → 2.87e-71`). Makes it **worse**: 4 failures, with `log_and_mayer_orders_identical` additionally breaking — because a fully-70-digit probe is *further* from the stale 50-digit-era template.

So the fix is the **whole chain**: close the straddle in the comparison probe **and** in `gamma_gamma_isospin_channel_probe.py` (same pattern, line 169), then refresh both upstream witnesses. `gamma_gamma_nn_pn_selection_probe.py` has **no** sympy route and is already 70-digit throughout.

## 🛑 And the chain cannot be COMMITTED from this container

Both upstream witnesses are among the **7 py3.13 provenance-blocked** producers (`qou-oiz3`): refreshing them here records `python 3.13.16 → 3.11.18`, `numpy 2.5.3 → 2.4.6`, `scipy 1.18.1 → 1.17.1`. Python 3.13.18 **is** installed, but `sympy` and `pyhecke_native` have no metadata under it, so moving there **drops** two keys — a *stripped* field, which ranks worse than a downgrade. **So this bean is blocked on installing `sympy` + `pyhecke_native` for python 3.13**, which is the same blocker as the three provenance refusals in `qou-oiz3`.

## Open items

1. Install `sympy` + `pyhecke_native` under python 3.13 so the upstream refreshes record no regression. (`pyhecke_native` is unpublished — build with `maturin build --release` from `tools/pyhecke-native/`.)
2. Close the straddle in all **31** files, not just the 2 in this chain. The other 29 are silent today because nothing asserts at 1e-50 — they are wrong numbers waiting for a tight enough check.
3. **Do NOT widen any tolerance** to close this. AGENTS.md: a bound sized to its own miss is a fit.
4. Decide whether a sweep like Part C's should refuse to patch a file that also carries a sympy path, rather than creating the straddle silently. The classifier already carves out 207 deliberate 50-digit consumers; this is the same idea one spelling over.

### CORRECTION, same day — "each computes one quantity from two values of q" was an OVERCLAIM

The section above states that each of the 31 *"now computes **one quantity** from two different values of `q`"*. **Only one of them is confirmed to do that.** What is measured is that each file *carries* both values; whether they MEET inside a single computed quantity is a per-file question I checked on exactly one.

Re-measured from `HEAD` (so my own working-tree edits do not contaminate it):

| | files |
|---|---:|
| straddles at HEAD (carry a sympy 50-digit `q` **and** `Q_MP`) | **37** |
| of those, the sympy branch is converted into mpmath somewhere (`to_mp` / `mp.mpf(str(` / `sp.N(`) — the **necessary** condition for the two to meet | **34** |
| of those, it is not — the two stay in parallel pipelines | 3 |
| **confirmed** to mix inside one quantity | **1** |

The confirmed one is `two_nucleon_binding_law_comparison_probe`: its `tr`/`ph` come from `QV` (sympy, 50 digits) and are combined with `E0`, `me`, `h`, `z` from `Q_MP` (70 digits) inside `laws()`. That is a genuine single-quantity straddle and it is why three 1e-50 checks broke.

**"Crosses into mpmath" is necessary, not sufficient**, so the other 33 are *candidates*, not established defects — a file could convert the sympy value and still never combine it with a `Q_MP`-derived one. Do not quote 31 or 34 as a defect count; quote them as the population to triage, with 1 confirmed.

This matters for prioritisation: if most of the 33 turn out to keep the two values in separate quantities, the fix is small. If they mix, each one is a wrong number at the 1e-50 level that nothing currently asserts tightly enough to catch.
