---
# qou-smvw
title: 'Magnus Omega2 option C: report both weight families permanently'
status: completed
type: task
priority: normal
created_at: 2026-09-07T11:44:23Z
updated_at: 2026-09-13T16:17:11Z
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
- [x] Fold both arms into each sign probe's own witness so the pair travels with
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
- 🛑 **CORRECTED 2026-09-13. This block said "the **sign is robust**: P_total
  < 0 under both, on all three atoms". THAT IS FALSE**, and it is the premise
  every option below was weighed against. It was measured on 2026-09-07 from a
  robustness run whose triton and ⁴He sources predated the 2026-09-05 ordering
  ruling (`qou-hu1f`). Regenerated on the canonical borromean word:

      atom      Plancherel      Wenzl (headline)     agree?
      deuteron   -15.095          -6.921              yes
      triton      +2.470         -13.931              NO
      ⁴He        +34.126         -20.466              NO

      Plancherel  -, +, +   one sign change, deuteron -> triton
      Wenzl       -, -, -   no sign change anywhere in A = 2,3,4

  So the two families do not merely disagree on a number: **they disagree on
  whether the programme's target A-dependent sign change is present at all.**
  Per-λ traces are mixed-sign at every A (+4/−5, +14/−14, +33/−42), so the sum
  is a genuine cancellation and the sign was free to move.
- **Magnitude is not robust** either, and not monotone. The figures that stood
  here (triton −108.1 → −60.0, ⁴He −57.8 → −100.8) were the same pre-ruling
  run; the canonical values are in the table above.
- The probes' stated control (`ρ=I ⇒ tr(Ω₂)=0`) holds **blockwise** — every
  per-λ control trace is exactly 0 — so it is weight-blind and provides no
  evidence either way.

🛑 **CORRECTED 2026-09-13.** This read *"No published conclusion depends on the
choice, so this is a correctness-of-object question, not an emergency."* Both
halves are now false. The choice of weight family decides whether the
A-dependent sign change — the programme's target — is exhibited, so a published
sign statement DOES depend on it. Choosing the family because it yields the
wanted sign would be selection against the target (AGENTS.md), which is why the
honest reading is that under the production Markov weight the sign change is
**not** exhibited in A = 2, 3, 4.


---

## 2026-09-07 — implemented

All three sign probes now accumulate `P_wenzl` via
`y_lambda_wenzl_bridge_numeric` alongside the Plancherel `P_total`, and emit
`headline_pairing: "P_total_wenzl"` with the value and its sign.

**`P_total` keeps its name and Plancherel meaning, deliberately.** Gate 2 of the
he4 sparse probe does a NUMERICAL dense-vs-sparse check against the committed
`P_total`, and `he4_magnus_mpfr_probe.py` reads it too — silently re-meaning the
field would compare a Wenzl-weighted sparse value against a Plancherel-weighted
committed one and break a real check. Adding the truth rather than re-meaning an
existing key is the same fix this arc used for the `y_lambda` column and the
missing `scriptFile`. A hard rename stays available, but must migrate those
numerical checks in lockstep.

Deuteron regenerated and verified: `P_total_wenzl = -6.9212506529727351`,
matching the independent offline re-weighting exactly; control assertion still
passes. Triton and he4 are slow (>10 min and worse) and pick up the fields on
their next run — no arithmetic changed, only what is additionally recorded.

Remaining on this bean: re-run triton and he4 so their witnesses carry the
headline fields, and confirm the cross-atom sign gate still passes end to end.

---

# SUBSUMED — OWNER RULING 2026-09-13: Wenzl adopted

Reporting both families is already what the probes do — each emits P_total (Plancherel) and P_total_wenzl, with headline_pairing naming the adopted arm and weight_family declared beside every y_lambda column. This option asked for a practice that landed under option A; the ruling settles which arm is authoritative, which is what C deliberately left open.

Full ruling, its basis and its consequence: parent bean `qou-za3q`.

**The consequence travels with the ruling.** Under the adopted Wenzl weight the
programme's target A-dependent sign change is **not** exhibited in A = 2, 3, 4
(−, −, −); it appeared only under the rejected measure (−, +, +). Anyone citing
the Magnus sign result must state that.
