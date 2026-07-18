# `_avg_color_delta()` is anchor-adaptive — a *fragile-guard* pattern, not a live mixed-pin bug (self-correction)

**Date:** 2026-07-18 · **Axis:** q₀-anchor convention / L1 precision hygiene ·
**Tier:** finding + guidance (scope-(a); no code behavior change; no witness
rewritten). **Branch:** `claude/focused-euler-ez3iu4`.

> **Self-correction.** An earlier version of this audit (and the #3906 PR body /
> the #3891 Correction box) claimed `_avg_color_delta()` is *"proton-pinned"* and
> flagged a *"mixed-pin hazard."* **Both over-stated the problem.** The 5.86e-11
> I measured came from my *diagnostic* running standalone **without**
> `QOU_Q0_ANCHOR=ideal`, not from any consumer. Verified below; a background
> classification of all ~40 consumers finds **0 live mixed-pin bugs**. This
> version is the corrected record.

## What is actually true

`_avg_color_delta()` = `flavor_split_leading(mp.mpf(str(q_parameter.Q)))`, and
`q_parameter.Q` is **anchor-adaptive** (`tools/qou-substrate/.../q_parameter.py`):

| context | `_avg_color_delta()` | δ error vs 50-dps muon |
|---|---|---|
| default (no anchor) | 0.001375710807027… (**proton** pin) | 3.2e-7 |
| `QOU_Q0_ANCHOR=ideal` (or producer in `q0_anchor_manifest.json` `ideal_muon`) | 0.0013757112499766… (**muon** pin) | **5.0e-16** |

Under the ideal anchor the accessor **redefines `q_parameter.Q` from the muon
witness**, so a script whose trace and δ both flow from `q_parameter` stays
pin-consistent. `flavor_split_leading(q) = (q−1)²(1−q⁻⁴)/3` is the **exact**
closed form either way (= `markov_peel._color_delta`'s δ_symbolic to 2.6e-54 at a
fixed q₀); the only variable is which q₀ it is evaluated at.

So the 5.86e-11 residual is **not** intrinsic to `_avg_color_delta()` — it is what
you get **only** if a muon-q₀ trace is color-weighted by a **default-anchor**
(proton) δ. No production consumer does that.

## The genuine finding — a fragile guard + a precision ceiling

1. **Fragile guard.** A muon-q₀ 1ppQ compute is correct **only because** it (or
   the manifest) sets `QOU_Q0_ANCHOR=ideal`. Drop that env-var / manifest entry
   and δ silently reverts to proton → 5.86e-11. That is exactly the trap my own
   standalone diagnostic fell into. The 4 watch-list files below carry the guard;
   an edit removing it would create a real MIXED-PIN-1ppQ.
2. **Precision ceiling under the anchor.** Even correctly muon-anchored,
   `_avg_color_delta()` is δ to only **~5e-16** (it reads the **f64** `q_parameter.Q`,
   not the 50-dps `Q_50_DIGIT_STR`) → tr_M to ~1e-16, inside 1ppQ but only ~10×.
   For **deep**-1ppQ, evaluate the closed form at the 50-dps muon q₀:
   `flavor_split_leading(q0_muon_50dps)` (or `markov_peel._color_delta`). The new
   L1 third method (`cross_check_trM_cw_seminormal_leg.py`) does exactly this and
   lands at ~7e-49 — the robust pattern, independent of the ambient anchor.

## Consumer classification (40 files)

Background sweep of every `_avg_color_delta` / `flavor_split_leading` consumer:

| bucket | count | meaning |
|---|---|---|
| **MIXED-PIN-1ppQ (live bug)** | **0** | none |
| **MIXED-PIN-scopeA** | **0** | none |
| **CONSISTENT** | **34** | pin-aligned (see breakdown) |
| **N/A** (witness `.json`) | 6 | data, not code |

**CONSISTENT breakdown**
- **C1 — muon-trace + `_avg_color_delta`, mitigated by `QOU_Q0_ANCHOR=ideal`
  (4, the *watch list*):** `deltalambda/he4_binding_k_presentation_correction_probe.py`,
  `deltalambda/he4_binding_k_stage2_probe.py`,
  `deltalambda/he4_stage2_ranking_seminormal_xcheck.py`,
  `cross_check_trM_cw_seminormal_leg.py` (this one uses the **exact symbolic δ**,
  not `_avg_color_delta` — robust by construction).
- **C2 — trace + δ both from anchor-adaptive `q_parameter`, move as a unit
  (17):** incl. `markov/markov_peel.py` (the L1 peel reference; δ + trace at the
  same `q_parameter.Q` — the correct pattern), `chi_at_q0_via_hoefsmit_mpfr.py`
  (tol 1e-12, not 1ppQ), `mass_at_3A_proper.py` (couples q → both proton or both
  muon), and 14 further probes.
- **C3 — δ is a *physical flavor-split observable* (Δm/M_N), not a trace weight;
  local q throughout (9):** `_li_2_q_util` (definer), `closed_form_tau_M`, and 7
  `flavor_split_*` / `charge_symmetry` probes.
- **C4 — threshold / harness / comment / drift-tool (4):**
  `canonical_braid_crossings` (classify threshold + definer),
  `chi_monotone_transfer` (a harness that *compares* the two δ functions),
  `binding_combiner_markov_peel_fallback` (comment-only), `fr_pullback_borromean_h3a_test`
  (the muon/proton δ delta **is** its deliverable).

## Actions taken (guidance only — no behavior change, no migration)

- **In-code note** on `_avg_color_delta()`: it is anchor-adaptive; muon-q₀
  callers must set `QOU_Q0_ANCHOR=ideal` (or be in the manifest), and deep-1ppQ
  callers should use `flavor_split_leading(local_q0_50dps)`.
- **No mass migration** (owner-gated per AGENTS.md §"q₀ anchor convention"); no
  witness rewritten. `markov_peel` self-aligns to its caller's anchor — worth a
  guard only if ever run standalone as a muon-1ppQ reference.

## Cross-references

- L1 third method (corrected framing): [`2026-07-18-l1-third-method-cw-seminormal.md`](2026-07-18-l1-third-method-cw-seminormal.md)
- q₀ convention: AGENTS.md §"q₀ anchor convention (STRICT)"; bean `tnjb`
- δ closed form: `computations/_li_2_q_util.py::flavor_split_leading` (`prop:flavor-split-substrate`)
