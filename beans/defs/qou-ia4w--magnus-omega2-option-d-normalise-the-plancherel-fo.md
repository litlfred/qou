---
# qou-ia4w
title: 'Magnus Omega2 option D: normalise the Plancherel form to tr(1)=1'
status: scrapped
type: task
priority: normal
created_at: 2026-09-07T11:44:23Z
updated_at: 2026-09-13T16:17:01Z
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

# REFUSED — OWNER RULING 2026-09-13: Wenzl adopted

Normalising the Plancherel measure is refused. Normalisation would fix tr(1)=1 but not the stabilisation axiom, which is the one that matters here because stabilisation is the move that changes n, and n = 3A: a cross-A statement IS a statement across stabilisations. A normalised Plancherel still has no z.

Full ruling, its basis and its consequence: parent bean `qou-za3q`.

**The consequence travels with the ruling.** Under the adopted Wenzl weight the
programme's target A-dependent sign change is **not** exhibited in A = 2, 3, 4
(−, −, −); it appeared only under the rejected measure (−, +, +). Anyone citing
the Magnus sign result must state that.
