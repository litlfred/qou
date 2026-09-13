---
# qou-94yt
title: 'Magnus Omega2 option B: keep the Plancherel measure, rename and justify it'
status: todo
type: task
created_at: 2026-09-07T11:44:23Z
updated_at: 2026-09-07T11:44:23Z
---

# NOT RECOMMENDED on its own

Keep `d_q²/[n]_q!`, finish naming it, and write the justification the corpus
currently lacks.

## For

Uses the whole algebra — discards nothing, including the sector carrying 62 % of
the A=2 contribution. Plancherel is the canonical measure induced by the regular
representation, i.e. the natural "average over the algebra". Cheapest option: the
naming half already landed under `qou-za3q`.

## Against

- Not `tr_M`. The docstring derivation must be **rewritten**, not just renamed —
  the cyclicity argument survives (any non-negative combination of block traces
  is a trace) but the Markov attribution does not.
- **Leaves the cross-A defect in place** while implying it is fixed. This is the
  reason it is not recommended alone.
- Not Markov-invariant, so the result is a function of the braid presentation
  rather than of the nucleus.

## Work

- [ ] Rewrite the three docstrings' derivation so no Markov property is claimed.
- [ ] State positively why a Plancherel average is the right contraction for Ω₂,
      or record that it is a convenience.
- [ ] Either adopt option D's normalisation or document that magnitudes are not
      comparable across A.

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
