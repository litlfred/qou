---
# qou-ia4w
title: 'Magnus Omega2 option D: normalise the Plancherel form to tr(1)=1'
status: todo
type: task
created_at: 2026-09-07T11:44:23Z
updated_at: 2026-09-07T11:44:23Z
---

# NOT RECOMMENDED

Divide the Plancherel contraction by `Σ_λ w(λ)·d_λ` so that `tr(1)=1`.

## For

Fixes cross-A comparability for one line of code while keeping full-algebra
support. Strictly better than option B on the measurement that matters most
(11.139 / 184.233 / 6751.541 → 1 / 1 / 1).

## Against

Still not Markov, so still not a link invariant — the result remains a function
of the braid word. A normalised non-Markov trace is a perfectly good object but
an **unmotivated** one here: it would be chosen because it is convenient, which
is precisely the move this corpus is careful about. It buys the symptom
(comparability) without the reason.

## Work

- [ ] Only if option A is rejected. Then: normalise, and state in the witness
      that the object is a normalised non-Markov trace with no derivation behind
      the choice.

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
