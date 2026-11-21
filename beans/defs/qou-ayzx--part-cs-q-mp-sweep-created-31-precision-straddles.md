---
# qou-ayzx
title: 'Part C''s Q_MP sweep created 31 PRECISION STRADDLES: mpmath side moved to 70 digits, sympy side left at 50'
status: todo
type: task
created_at: 2026-11-21T04:30:36Z
updated_at: 2026-11-21T06:35:00Z
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

### 2026-11-21 — option D VALIDATED end-to-end; the tie fix verified against over-grouping

**The chain settles the cross-witness half.** With the straddle closed in both probes and `gamma-gamma-nn-pn-selection-probe` refreshed:

| check | upstream it reads | before | after |
|---|---|---|---|
| `H6_traces_match_nn_pn_witness` | `nn_pn` (refreshed) | FAIL | **pass** |
| `D2_log_matches_template_witness` | `nn_pn` (refreshed) | FAIL | **pass** |
| `D4_ratios_match_isospin_witness` | `isospin` (**timed out**) | FAIL | FAIL |

Every check whose upstream was refreshed passes. D4 fails only because `gamma_gamma_isospin_channel_probe` hit its 600 s budget at **49/72** (it needs ~860 s), so its witness was never written.

**An accidental control arm confirmed it.** A later run reverted `nn_pn` to the committed version *before* the probe read it (upstreams are read after the 144-character computation), and H6 and D2 failed again — same code, stale upstream → FAIL; refreshed upstream → PASS. The dependence is established in both directions, not inferred.

**`log_and_mayer_orders_identical` now passes** (`fb278110687`), and `L_log` / `L_mayer` are identical at all four D3 vertices with ties explicit: `nn = pn > pp`, `pp > nn = pn`, `nn > pn = pp`, `pn = pp > nn`.

**The tolerance was checked against over-grouping — the obvious way this fix could have been a weakening.** Every pair the tie-aware `order_desc` grouped, with its relative gap:

| vertex | law | pair | relative gap |
|---|---|---|---|
| V1 | `L_log` | `nn=pn` | `1.27758e-58` |
| V1 | `L_mayer` | `nn=pn` | `0.0` |
| V2 | `L_log` | `nn=pn` | `5.33149e-59` |
| V2 | `L_mayer` | `nn=pn` | `0.0` |
| V3 | `L_log` | `pn=pp` | `0.0` |
| V3 | `L_mayer` | `pn=pp` | `7.11406e-60` |
| V4 | `L_log` | `pn=pp` | `5.42074e-60` |
| V4 | `L_mayer` | `pn=pp` | `1.25658e-59` |

The loosest is **7.8e+7× tighter** than the `1e-50` bound, and the smallest genuine gap in the probe is `0.0132` — 48 orders the other way. So the bound is doing none of the work; the separation is.

**And the fix surfaced ties I had not found.** My hand analysis identified the V1/V2 `nn=pn` pair; V3 and V4 carry `pn=pp` ties as well, so there are **8 tied pairs** across the four vertices, not 2. The strict order was hiding real structure, which is the strongest argument for the fix being a correction rather than a relaxation.

**Remaining for this bean:** `pyhecke_native` built for the python 3.13 that now has sympy, then refresh `gamma_gamma_isospin_channel_probe` under it with a budget above 860 s. That should close D4 and let all three witnesses land provenance-clean. The nine confirmed-mixing straddles (taint analysis above) are the separate tranche.

### 2026-11-21 — the straddle tranche is 7 confirmed, and SEVERITY-RANKED

**36 straddles → 7 confirmed genuine mixes**, reached by taint analysis plus four rounds of false-positive elimination. Each round was found by **reading a flagged site**, not by improving the pattern in the abstract, and each removed a distinct class:

| round | count | class removed |
|---|---:|---|
| raw taint | 10 | — |
| exclusion 1 | — | a name tainted BOTH ways (a reassignment, or `p` as a loop variable in a path-bridge comprehension) carries no information |
| exclusion 2 | 9 | display-only sites (`print`, `_log`) |
| exclusion 3 | 8 | the enclosing call of an f-string: excluding a `JoinedStr`'s *descendants* does not exclude the `check(cond, f"… {H0} …")` that walks into it — `qbeta_gamma_gamma_crossing_energy_probe`'s `H0` occurs **solely** in a message |
| reading | **7** | a *deliberate* sympy-vs-mpmath cross-check whose inner `BinOp` was flagged while the enclosing `abs(...)` was the real node — `qbeta_per_block_chi_borromean_closed_forms_probe`'s own print says *"independent-path cross-check at q0"* |

**The 7, ranked by whether the mix can actually move a verdict:**

| severity | file | the mix | tolerance it meets |
|---|---|---|---|
| **can flip an assertion** | `delta_lambda_binding_reading_probe` | `abs(tr[p]["W.s"] − z·tr[p]["W"]) < tol` | **`1e-50`** — same shape *and* same tolerance as the one already fixed |
| touches a published number | `qbeta_option_e_required_level_probe` | `(abs(aug_S)·E0/MP_QB − 1)·100` | `0.001` on a figure AGENTS.md quotes as **+12.470 %** |
| wrong, unasserted | `colour_weighting_markov_universality_probe` | `d_for_ctype("averaged_weighted", h, delta=delta)` | — |
| wrong, unasserted | `deuteron_interface_colour_weighting_probe` | same `d_for_ctype` shape | — |
| wrong, unasserted | `diproton_response_closed_form_probe` | `r_val = h2 · c_val` | — |
| wrong, unasserted | `long_braid_limit_dominant_line_probe` | `abs(y21n·chi / (y3n·q0^{2N}))` | — |
| wrong, unasserted | `two_nucleon_bond_response_arity_probe` | `B = −alpha · mp.log(ratio_v)` | — |

**`delta_lambda_binding_reading_probe` is the one to do next**: it is the same `abs(tr − z·tr) < 1e-50` construction as the probe whose three checks broke, so it is the candidate most likely to be a *live* failure rather than a latent one. The other six mix at `2.1e-50` against tolerances of `1e-38`, `0.001` or nothing, so they are wrong numbers that nothing currently asserts tightly enough to catch — exactly the population this bean exists for.

**A caveat on the one deliberate cross-check**, worth a line because it is not a defect but is weaker than it looks: `qbeta_per_block_chi_borromean_closed_forms_probe` compares its two routes at tolerance `1e-38` while the routes themselves sit at *different* `q` (sympy 50-digit vs `Q_MP`, `2.1e-50` apart). It passes, and it would pass whatever the routes disagreed about below `1e-38` — the q difference is not what limits it, but the cross-check cannot see anything finer than its own tolerance either.
