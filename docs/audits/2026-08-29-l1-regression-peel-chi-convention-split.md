# L1 (1 ppQ) is NOT MET on `main`: markov_peel ⟷ chi-cache disagree at 2.9e-7 — a convention split, likely recoverable

**Date:** 2026-08-29 · **Method:** cross-witness forensics on `origin/main`, read-only, with an independent `Decimal(60)` recomputation from the two source witnesses · **Tier:** measured fact (two committed witnesses disagree at 2.9e-7) + a **stated, unproven** root-cause hypothesis (convention split) · **Beans:** resolves `qou-wgaw`; confirms `qou-mj1o`'s 2026-08-29 falsification comment; root cause tracked at `qou-3zby`.

## Headline

The framework's **L1 leg** — internal cross-method agreement of `tr_M(β_atom)`
at `q₀` to **1 ppQ = 10⁻¹⁵** — is **NOT demonstrated on `origin/main` HEAD.** The
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

## Root cause (hypothesis, not proved here)

The 2026-08-15 owner ruling made convention **D** canonical and excised **C**.
The migration is incomplete across these two producers: bean `qou-3zby`
(2026-08-21) documents `markov_peel` computing in **convention C** while
`chi-cache` computes in **convention D** at the muon pin. Two methods on two
different Markov-trace conventions will not agree, and the A-growth is consistent
with a per-bond convention factor accumulating with braid length. This is stated
as the **likely** cause; it is not proved in this document.

## What is and is not claimed

- **Claimed (measured fact):** the corpus as committed on `origin/main` HEAD does
  **not** demonstrate L1 at 1 ppQ; it demonstrates a 2.9e-7 peel⟷chi
  disagreement. An agreement not present in the artifacts is not a certification.
- **NOT claimed:** that the framework is mathematically **incapable** of 1 ppQ
  here. This is very likely a *recoverable* mid-migration convention split, not an
  intrinsic method disagreement. A same-convention (both D, same pin)
  regeneration may restore the 2026-07-13-era ~1e-50 agreement. Until that number
  exists in the corpus, L1 is **uncertified**, not **refuted** (scope-(a)).
- The **χ-engine closed-form anchor** (`character_closed_form_anchor.worst_delta =
  5.88e-50`) is a **different, healthy** check — it verifies the character engine
  is internally correct, not that peel and chi-cache agree. Do not cite it as the
  peel⟷chi agreement.

## The fix (owned convention-D work — do NOT do it here)

The fix is at the producer, and it belongs to the convention-D migration
(`qou-cds1` / `qou-cdx1`), **not** to a dashboard edit:

1. Put `markov_peel` and `chi-cache` on the **same convention (D)** at the **same
   pin**, then regenerate both witnesses.
2. If a clean same-convention run restores ~1e-50, L1 is recovered — update the
   cert audit and the precision-goals headline then, from the regenerated number.

**Do NOT** widen the `1e-9` tolerance (`onepb_status_dashboard.py:377`) or edit any
baseline to force green — the producer's own comment (`:367-371`) forbids it
("baselines drain, never grow"). `allPassed=false` should **stay red** until the
convention split is fixed at the producer.

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
