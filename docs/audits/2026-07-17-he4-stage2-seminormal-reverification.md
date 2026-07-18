# ⁴He stage-2 reverification on the seminormal engine — λ*(K)=(9,3) survives, tr_M(K) corrected, (8,4) near-degenerate

**Date:** 2026-07-17 · **Axis:** A=4 binding (stage-2 structural certificate) ·
**Tier:** measurement (scope-(a); audit-only; no fit; nothing wired). **Branch:**
`claude/focused-euler-ez3iu4`.
**Probe:** [`he4_binding_k_stage2_probe.py`](../../computations/deltalambda/he4_binding_k_stage2_probe.py)
(full both-leg) + new fast companion
[`he4_stage2_ranking_seminormal_xcheck.py`](../../computations/deltalambda/he4_stage2_ranking_seminormal_xcheck.py).

## The open item this closes

[`2026-07-14-gp-kernel-bug-and-he4-stage2.md`](2026-07-14-gp-kernel-bug-and-he4-stage2.md)
found that the Rust Geck–Pfeiffer character path (`chi_lambdas_via_gp`) returns
**wrong χ on some plain braid words**, and that the committed
`he4-binding-k-stage2.witness.json` — whose Leg A ranked the dominant binding
channel **λ*(K) = (9, 3)** — was produced on that buggy GP path. The audit left
the ranking *"unverified until the seminormal rerun confirms or replaces it."*
The probe **source** was rewritten to the seminormal engine, but the **witness
was never regenerated** (its `computedAt` = 2026-07-13T22:03, engine
`pyhecke_native(GP)`), so the open item stood for three days.

This audit regenerates the witness on the seminormal engine and adds an
independent fast ranking cross-check.

> **Upstream note (2026-07-17/18).** The GP kernel bug itself was subsequently
> **fixed on `main`** — the Geck–Pfeiffer cyclic-shift completion
> (`61c401a610`, bean `qou-b2ie` resolved). That fix and this reverification are
> complementary and mutually corroborating: this audit corrects the *committed
> witness* (which `main`'s GP fix did **not** regenerate — `main` still carries
> the stale GP-legged `he4-binding-k-stage2.witness.json`, tr_M 0.06768,
> xcheck 2.09), while the engine fix means the GP path is now available as an
> independent *third* character engine to cross-check the seminormal result on
> the K word. This reverification does not depend on it — it used the
> always-correct seminormal path throughout.

> **Status (2026-07-18).** **Complete.** The full 50-dps both-leg run finished
> under per-block checkpointing (7 sandbox sessions; caches self-cleaned) and the
> official `he4-binding-k-stage2.witness.json` is regenerated on the seminormal
> engine (`computedAt` 2026-07-18T04:55, `allPassed: True`, all 77 blocks). Every
> number below is from that committed witness.

## What was done

1. **Environment.** Built the `pyhecke_native` Rust wheel from
   `tools/pyhecke-native` (the stage-2 probe's seminormal engine
   `chi_lambda_all_partitions_mpfr` / `_f64` is a compiled extension, not
   importable from source).
2. **Wording bug fix.** The probe's `verdict` string and witness `description`
   still read *"Leg A (exact GP χ)"* / *"exact GP characters"* — stale from the
   GP→seminormal switch (the `engine` field already correctly said *"GP path
   NOT used"*). Fixed both so the regenerated witness is labelled by the engine
   that actually produced it. Code path unchanged.
3. **Fast ranking cross-check** (new committed companion, ~50 s): χ_λ(K) for all
   77 blocks of H₁₂ via the **seminormal-f64** engine, ranked by |y_λ·χ_λ(K)|,
   entirely independent of the GP kernel.
4. **Full regeneration** (both Wedderburn legs, 50 dps): seminormal-mpfr Leg A
   (exact χ + operator-selection LP with duals) + f64 Leg B (per-block PSD
   spectra) with the per-block Leg-A/Leg-B trace cross-check.

## Findings

**1. The dominant channel survives the engine fix: λ*(K) = (9, 3), CONFIRMED.**
Both the independent seminormal-f64 companion and the 50-dps full Leg A rank
(9, 3) first. The GP bug did **not** change the dominant channel — the buggy GP
ranking happened to agree with the correct seminormal ranking on the top slot.

**2. …but (9, 3) and (8, 4) are near-degenerate — the "dominant channel" reading
is marginal.** The top two channels by receptivity |y_λ·χ_λ(K)| are:

| rank | λ | \|y_λ·χ_λ(K)\| (f64) |
|---|---|---|
| 1 | **(9, 3)** | 0.01129954 |
| 2 | (8, 4) | 0.01126835 |
| 3 | (10, 2) | 0.00762069 |

The (9, 3) lead over (8, 4) is only **0.276 %**. The *order* is numerically
robust (0.276 % ≫ f64 noise, and the 50-dps run confirms it), but the two
channels are **near-equally receptive** — any downstream reading that treats
(9, 3) as *the* binding channel should carry (8, 4) as a co-dominant partner.
This nuance was invisible in the committed witness (which reported only the
single dominant λ).

**3. tr_M(K) was corrupted by the GP bug (~15 %), even though the ranking
survived.** The scalar trace tr_M(K) = Σ_λ y_λ χ_λ(K):

| engine | tr_M(K) |
|---|---|
| committed (GP-legged, buggy) | 0.0676801479901 |
| seminormal-f64 (companion) | 0.0572284369457 |
| **seminormal-mpfr 50 dps (full probe)** | **0.057228436945653579716** |

The 50-dps value confirms the f64 companion (agree to ≈ 1e-14) and the LP
duality gap closes at 4.58e-14. The GP bug inflated tr_M(K) by **≈ 15.4 %**
(0.06768 vs 0.05723). So the bug's impact was on the *magnitude* channel, not
the *ordering* channel — a useful calibration of the GP-kernel blast radius on
this word.

**4. The leg cross-check confirms the fix.** The committed run reported a worst
Leg-A/Leg-B trace cross-check of **2.09** (GP Leg A vs f64-seminormal Leg B —
they disagreed because GP was wrong). With both legs seminormal, the worst
cross-check drops to **8.08e-15** (worst across **all 77 blocks** at 50 dps).
The two independent engines — seminormal-mpfr Leg A and pure-python f64 Leg B —
now agree at the f64 floor, the positive confirmation the GP path lacked.

**5. PSD / binding-stability certificate (Leg B, f64 diagnostic).** Min
symmetrized eigenvalue **−10.477** (block λ = (5,3,2,2)), so **α_gap = 10.477**,
**PSD-within-tol False** — K(⁴He) is **not** positive-semidefinite. This matches
the committed (GP-legged) Leg B verdict exactly, as expected: Leg B is the
pure-python f64 seminormal path and was never on the GP kernel, so only Leg A's
scalar (tr_M, ranking) moved under the fix; the PSD certificate did not.

## Interpretation (scope-(a))

The stage-2 object K(⁴He) = T·cp⁻¹ is unchanged; only the character engine was
corrected. The A≤3 "binding stability" reading is the per-block PSD verdict; at
A=4 the committed (GP) run already reported it non-PSD (min symmetrized
eigenvalue −10.477), i.e. the A≤3 stability certificate does **not** extend
naively to ⁴He — a finding the seminormal reverification preserves (the PSD
certificate lives on the GP-independent Leg B). Nothing here is wired to
production, uses AME input, or is fitted; this is a structural reverification on
the certified convention.

## Cross-references

- GP kernel bug: [`2026-07-14-gp-kernel-bug-and-he4-stage2.md`](2026-07-14-gp-kernel-bug-and-he4-stage2.md)
- Witnesses: `computations/deltalambda/he4-binding-k-stage2.witness.json`
  (full, regenerated), `he4-stage2-ranking-seminormal-xcheck.witness.json` (fast companion)
- Program context: [`2026-07-17-1ppq-program-ownership-map.md`](../coordination/2026-07-17-1ppq-program-ownership-map.md)
  §"genuinely-uncontended capacity" (this was one of the named support-layer items).
