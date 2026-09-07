---
# qou-q2q7
title: 'Magnus Omega2 option A: adopt the Wenzl y_lambda as the pairing'
status: todo
type: task
created_at: 2026-09-07T11:44:22Z
updated_at: 2026-09-07T11:44:22Z
---

# RECOMMENDED (as headline, with option C kept as a guard)

Make the Wenzl-weighted value the reported `P_total` in all three sign probes.

## Why

- **Cross-A comparability, the decisive argument.** The programme's target claim
  is a *sign change in A*. Sign is scale-invariant so existing gates are safe,
  but any cross-A *magnitude* statement is meaningless under Plancherel, whose
  normalisation drifts 600× between A=2 and A=4. Wenzl fixes `tr(1)=1`.
- **The code would match its own derivation.** The docstrings already call the
  pairing `tr_M` and invoke "Markov trace of a commutator vanishes by
  cyclicity". Adopting Wenzl is a smaller repair than rewriting that derivation.
- **A nucleus is a link.** The Markov trace is the one invariant under
  stabilisation, so the answer depends on the nucleus rather than on the braid
  word chosen to present it.
- **Consistency.** Production `tr_M` uses this weight everywhere else.

## Against, and it is real

Discards the entire ≥3-row sector: 62 % of the A=2 contribution, 70 of 77 shapes
at A=4. Defensible only because the row cap is a corpus-wide commitment already —
if it is wrong it is wrong everywhere, which is `qou-fq0f`'s question, not this
probe's. ⁴He magnitude nearly doubles.

## Work

- [ ] Add a Wenzl-weighted `P_total_wenzl` alongside the existing value in all
      three sign probes, and make it the headline.
- [ ] Re-run; confirm every sign gate (including the he4→triton cross-atom
      assert) still passes.
- [ ] Update the docstrings' pairing line to the weight actually used.

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
