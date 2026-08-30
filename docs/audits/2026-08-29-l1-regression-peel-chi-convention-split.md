# L1 (1 ppQ) regression: the chi-cache combiner was wrong by 2.9e-7 — RESOLVED 2026-08-30

> **✅ RESOLVED 2026-08-30 — L1 is MET again: 6/6 atoms certified, `onepb allPassed = True`.**
> This document is kept as the **record of a silent regression and its repair**, not as a
> live defect.
>
> **⚠ SCOPE OF EVERYTHING BELOW THIS BANNER.** The remainder of this file is the
> **2026-08-29 measurement, preserved verbatim as it was recorded that day** — it is a
> historical snapshot of the RED state, not a description of the corpus now. Its
> present-tense statements (*"is NOT demonstrated on `origin/main` HEAD"*, *"the corpus does
> not demonstrate L1"*, the 2.9e-7 deltas) were true **on 2026-08-29** and are **false as of
> 2026-08-30**. Read every claim below as carrying an implicit *"as measured on
> 2026-08-29"*. For the current state, read only this banner.
>
> **Root cause (both halves were pin straddles, not convention C):**
> 1. The chi combiner's numerical χ cache was pinned at the **proton** q₀ while the muon
>    cross-check combined it with **muon**-pinned `y_λ` (PR #6091).
> 2. `habiro-coefficients-extended.witness.json` was proton-pinned, so the cross-check's own
>    guard `SystemExit`'d before the gate could even run (PR #6100, `qou-3zby` DEFECT 2).
>
> **Fixes:** a pin-straddle guard in `canonical_tr_m_via_chi_cache.py` (falls back to the
> pin-correct symbolic χ when the cache pin ≠ runtime pin, but only where the symbolic cache
> is complete); **pin-specific numerical χ cache filenames** (`-{anchor}` suffix; proton keeps
> the legacy name); Habiro regenerated at muon; and the `onepb` gate re-pointed at the
> **color-weighted** `exact_method_rel_delta` instead of `rel_delta_max`, which had been
> failing on the informational color-blind legs (⁴He `rel_delta_max` ≈ 4.6 vs its
> color-weighted ≈ 6e-50). **No tolerance was widened and no baseline grown.**
>
> **Final measured state** — `peel_vs_chi`, all six at 1 ppQ: proton 8.6e-50, neutron 6.1e-50,
> deuteron 1.2e-49, tritium 8.7e-50, ³He 7.4e-50, ⁴He 6.2e-50.
>
> **The lesson worth carrying:** L1 was certified 2026-07-13 and broke *silently* during the
> convention-D migration window; the gate that should have caught it was pointed at the wrong
> quantity, and before that at a key (`rel_delta`) **no delta entry has ever carried**, so it
> could not fail at all. A green L1 gate is only as good as the field it reads — re-check the
> gated quantity, not just its boolean.

**Date:** 2026-08-29 (root cause **corrected 2026-08-30** — see the box below) · **Method:** cross-witness forensics + **fresh producer recomputation** of both methods at the muon pin · **Tier:** measured fact (L1 not met; the culprit is chi-cache, established by fresh recompute) · **Beans:** resolves `qou-wgaw`; confirms `qou-mj1o`'s falsification comment.

> **🛑 ROOT-CAUSE CORRECTION (2026-08-30).** The first version of this document
> (2026-08-29) blamed the L1 red on a **convention split with `markov_peel` on
> convention C**, carried from bean `qou-3zby` (dated 2026-08-21). **That is
> wrong, and I am correcting my own claim.** Fresh recomputation settles it:
>
> - **`markov_peel` is convention D and CORRECT.** Its executable path routes
>   through `markov_trace_canonical.tr_M_element` → `hecke_symbolic.z_markov =
>   q³/(q²+1)` (convention D, migrated C→D 2026-08-09, bean `qou-wgta`). Recomputing
>   `tr_M(proton)` fresh from the current producer reproduces the **committed peel
>   witness to 3.0×10⁻⁵⁰** — current, not stale, and not convention C.
> - **`chi-cache` is the outlier, and it is a REAL bug, not a stale witness.**
>   Fresh recomputation of the `Σ_λ y_λ·χ^λ` chi producer reproduces the
>   **committed chi value exactly** (`1.14575969303…`), which sits **7.84×10⁻⁸
>   below** peel. Two independent methods — peel (Markov recursion) and Hoefsmit
>   (seminormal) — agree to **5×10⁻¹⁰**; chi disagrees with both.
> - So the L1 failure is a **defect in the chi-cache combiner** (its `y_λ` or
>   `χ^λ` inputs), NOT a peel convention split, and it is **not** fixed by
>   regenerating peel. The `qou-3zby` "peel=C" measurement was of a
>   *then-stale* committed witness; the code was already D.
>
> The **measured L1-not-met fact below still stands** (and is now stronger: peel
> verified correct, chi reproducibly wrong). Only the mechanism changed.

## Headline

The framework's **L1 leg** — internal cross-method agreement of `tr_M(β_atom)`
at `q₀` to **1 ppQ = 10⁻¹⁵** — was **NOT demonstrated on `origin/main` HEAD as measured on
2026-08-29** (repaired 2026-08-30; see the banner above). The
two float-clean, color-weighted methods the certification *explicitly rests on*,
`markov_peel` and `chi-cache`, **disagree at 2.9×10⁻⁷** (⁴He) — 2.9×10⁸ times the
1 ppQ target. `computations/onepb-status-dashboard.witness.json` `allPassed=false`
is a **true red**, and it agrees with `cross-check-trM-1ppb.witness.json`'s 6/6
`within_1ppb=False`.

This **corrects** three currently-live corpus statements:

- AGENTS.md §Precision-goals and `docs/precision-goals.md` state L1 is **met /
  certified 6/6** — stale since the 2026-08-15 convention-D migration.
- `docs/audits/2026-07-13-l1-4he-certification-complete.md:24` prose "peel +
  chi-cache agree exactly" was true on 2026-07-13 and is **false on the current
  witness** (6/6 DIVERGE).
- `cross-check-trM-1ppb.witness.json` `parameters.description` still claims peel⟷chi
  "agree at q₀ (~1e-50)", **contradicted by its own committed `data.deltas`**
  (2.9e-7).

## The measurement (the discriminator that rules out "mis-gate")

An earlier read of this session hypothesised the failure was a *mis-gate*: the
dashboard aggregates `rel_delta_max`, a max over **all** method pairs including
the color-blind (sign-only) Hoefsmit/Habiro legs that are declared
"informational, not gated." That hypothesis is **wrong**, because the
color-weighted-**only** delta is numerically identical:

| atom | `exact_method_rel_delta` (peel⟷chi, color-weighted ONLY) | `rel_delta_max` (max over ALL pairs) |
|---|---|---|
| ⁴He | **2.9066298e-7** | 2.9066306e-7 |
| ³He | 2.4780267e-7 | 2.4780273e-7 |
| tritium | 1.9208634e-7 | 1.9208638e-7 |
| deuteron | 1.4920161e-7 | 1.4920163e-7 |
| proton | 7.8426e-8 | 7.8426e-8 |
| neutron | 6.9557e-8 | 6.9557e-8 |

The two columns differ only in the 8th significant figure. **Re-pointing the gate
at the pure color-weighted `exact_method_rel_delta` still fails 1 ppQ by
~2.9×10⁸.** The gate's field choice is *slightly* impure but immaterial.

Independent `Decimal(60)` recomputation straight from the source witnesses
(`markov/markov-peel-atomic-tr-m-muon.witness.json`,
`canonical-tr-m-via-chi-cache-muon.witness.json`), ⁴He:
`peel = 0.16097419354781…` vs `chi = 0.16097414675857…` — agreeing to only ~7
significant figures. **Both legs carry the identical muon `q₀`** (`q0Anchor:
muon`, `q0Value` byte-equal) and are 50-dps exact strings, so this is **neither a
pin straddle nor the float64 floor.**

The disagreement **grows monotonically with mass number A**
(p/n ≈ 7e-8 → D ≈ 1.5e-7 → ⁴He ≈ 2.9e-7) — the signature of a **convention
split**, not numerical noise.

## Root cause (established 2026-08-30 by fresh recomputation)

The culprit is the **chi-cache combiner** `canonical_tr_m_via_chi_cache.py`
(`tr_M = Σ_λ y_λ(q₀)·χ^λ`), not `markov_peel`. Evidence (proton, muon pin, all
values `mpmath` 50-dps):

| method | value `tr_M(proton)` | vs peel |
|---|---|---|
| `markov_peel` (Markov recursion, conv. D) | `1.1457597828869253…` | — |
| Hoefsmit (seminormal, independent) | `1.1457597823152389…` | 5.0×10⁻¹⁰ |
| **`chi-cache` (Σ_λ y_λ·χ^λ)** | **`1.1457596930289873…`** | **7.84×10⁻⁸** |

- **Fresh peel = committed peel to 3.0×10⁻⁵⁰** ⇒ peel is current and correct (D).
- **Fresh chi = committed chi exactly** ⇒ chi is **not stale**; it reproducibly
  computes a value 7.84×10⁻⁸ too small.
- peel and Hoefsmit are two independent constructions and agree to 5×10⁻¹⁰;
  **chi is the lone outlier**, so the defect is in chi's inputs — its `y_λ`
  (from `wedderburn_jones_markov.y_lambda_at`) or its `χ^λ` cache
  (`chi-<atom>-h<n>.witness.json`) — or the color-weighting in the combiner.
- The disagreement grows with A (p/n 7.8e-8 → ⁴He 2.9e-7), consistent with a
  per-block factor accumulating in the `Σ_λ` over the larger partition set — a
  next-step localization (`y_λ` vs `χ^λ` per partition of n=3A) will pin it.

The A-growth is **not** the C→D ratio (which is 1.481, a 48% split); 7.84e-8 is a
small residual, so this is a normalization/pin defect in the character path, not
a wholesale convention swap.

## What is and is not claimed

- **Claimed (measured fact):** the corpus as committed on `origin/main` HEAD does
  **not** demonstrate L1 at 1 ppQ; it demonstrates a 2.9e-7 peel⟷chi
  disagreement. An agreement not present in the artifacts is not a certification.
- **NOT claimed:** that the framework is mathematically **incapable** of 1 ppQ
  here. peel and Hoefsmit already agree to 5×10⁻¹⁰ — two methods *do* meet the
  target; the chi-cache combiner is the one that does not. Fixing chi's inputs
  should restore ~1e-50 agreement. Until that number exists in the corpus, L1 is
  **uncertified**, not **refuted** (scope-(a)).
- The **χ-engine closed-form anchor** (`character_closed_form_anchor.worst_delta =
  5.88e-50`) is a **different, healthy** check — it verifies the character engine's
  1-dim-irrep closed forms, **not** that the full `Σ_λ y_λ·χ^λ` combiner agrees
  with peel. Do not cite it as evidence the chi combiner is correct — it is exactly
  the check that passes while the combiner fails.

## The fix (at the chi-cache combiner)

The fix is at `canonical_tr_m_via_chi_cache.py` (and its `y_λ`/`χ^λ` inputs), **not**
at `markov_peel` (correct) and **not** at the dashboard:

1. Localize the 7.84e-8 defect: for the proton (n=3, partitions of 3), compare
   `y_lambda_at(3, q₀)·χ^λ` **per partition** against the peel decomposition to
   find whether it is a `y_λ` normalization/pin, a `χ^λ` cache pin, or the
   color-weighting. The A-growth says it accumulates over `Σ_λ`.
2. Fix at the producer and regenerate `canonical-tr-m-via-chi-cache-*.witness.json`;
   confirm chi then agrees with peel/Hoefsmit at ~1e-50, restoring L1.

**Do NOT** widen the `1e-9` tolerance (`onepb_status_dashboard.py:377`) or edit any
baseline to force green — the producer's own comment (`:367-371`) forbids it
("baselines drain, never grow"). `allPassed=false` should **stay red** until the
chi-cache defect is fixed at the producer.

## Naming staleness (secondary, `qou-wgaw`)

The witness stems `cross-check-trM-1ppb` / `onepb-status-dashboard` and the fields
`within_1ppb` / `all_within_1ppb` / `max_rel_delta` all read "1ppb" while the L1
target was upgraded to **1 ppQ (1e-15)** on 2026-05-26. The producer already
acknowledges this (`onepb_status_dashboard.py:206-213` `l1_target_note`, with
`within_1ppQ` / `all_within_1ppQ` aliases). Cosmetic — not the substance of the
failure.

## Files (origin/main)

- Dashboard producer / aggregation + failing gate: `computations/onepb_status_dashboard.py` (lines 175, 195, 374–378)
- Cross-check producer / delta construction: `computations/cross_check_trM_1ppb.py` (lines 404–405, 418–419, 474–476; convention-split evidence in comments 210–289)
- Witnesses: `computations/onepb-status-dashboard.witness.json` (`allPassed=false`), `computations/cross-check-trM-1ppb.witness.json` (6/6 `within_1ppb=False`)
- Color-weighted source legs (both muon pin): `computations/markov/markov-peel-atomic-tr-m-muon.witness.json`, `computations/canonical-tr-m-via-chi-cache-muon.witness.json`
- Stale headline: `docs/audits/2026-07-13-l1-4he-certification-complete.md` (line 20 = anchor 5.6e-50; line 24 = the now-false "agree exactly" prose)
