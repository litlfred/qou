---
# qou-smvw
title: 'Magnus Omega2 option C: report both weight families permanently'
status: todo
type: task
created_at: 2026-09-07T11:44:23Z
updated_at: 2026-09-07T11:44:23Z
---

# RECOMMENDED as a permanent guard alongside option A

Report both contractions in the same witness, labelled, forever.

## For

- Makes the weight-dependence **visible instead of implicit** — which is the
  actual defect `qou-za3q` found.
- Costs almost nothing: the per-λ traces are shared and only the contraction
  differs, so the second arm is a re-contraction, not a re-derivation.
- If the row cap is ever revised (`qou-fq0f`), the evidence needed to
  re-evaluate these probes is already recorded rather than needing a re-run —
  this is the specific reason to keep it beside option A.
- Any downstream claim can then state which arm it rests on.

## Against

Defers the decision if adopted *alone*. Two numbers where the physics wants one,
and it invites citing whichever arm is convenient — so it should be paired with a
named headline, not offered as a choice.

## Work

- [x] Standalone measurement exists:
      `computations/deltalambda/magnus_omega2_weight_family_robustness_probe.py`.
- [ ] Fold both arms into each sign probe's own witness so the pair travels with
      the result rather than living in a separate file.

Option from the decision analysis in [`docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md`](../docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md).
Parent question: `qou-za3q`. Sibling options: `qou-q2q7` (A), `qou-94yt` (B),
`qou-smvw` (C), `qou-ia4w` (D), `qou-gba1` (E).

**Shared measured context** (none of this is fitted):

- `tr(1) = Σ_λ w(λ)·d_λ` — Wenzl gives exactly **1.0** at n = 6, 9, 12;
  Plancherel gives **11.139 / 184.233 / 6751.541**. Plancherel is not a
  normalised trace and its scale grows ~600× from A=2 to A=4.
- Plancherel puts **81.8 %** of its H₆ mass on ≥3-row shapes; the Wenzl row cap
  (level r = 2, `qou-fq0f`) puts **0 %** there. **62.4 %** of the Plancherel
  |contribution| at A=2 comes from shapes Wenzl annihilates.
- The **sign is robust**: P_total < 0 under both, on all three atoms — and not
  trivially, since the per-λ traces are mixed-sign (+4/−5, +13/−15, +26/−49).
- **Magnitude is not robust** and not monotone: deuteron −15.1 → −6.9, triton
  −108.1 → −60.0, but ⁴He −57.8 → **−100.8**.
- The probes' stated control (`ρ=I ⇒ tr(Ω₂)=0`) holds **blockwise** — every
  per-λ control trace is exactly 0 — so it is weight-blind and provides no
  evidence either way.

No published conclusion depends on the choice, so this is a correctness-of-object
question, not an emergency.
