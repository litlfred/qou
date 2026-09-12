---
# qou-gba1
title: 'Magnus Omega2 option E: derive the Omega2 pairing from what Omega2 is'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T11:44:24Z
updated_at: 2026-09-12T11:52:27Z
---

# The only option that ANSWERS the question rather than choosing

Derive the correct contraction from what Ω₂ is, instead of picking a weight
family and defending it.

## For

Ω₂ = ½ Σ_{i<j} [A_i, A_j] is a curvature-like object built from germs
`A_g = q(∂_q σ_g)σ_g⁻¹`. The right pairing should fall out of whatever
variational principle produces a binding energy — and if it does, it settles the
row-cap objection to option A **on principle** rather than by convention, which
no other option can do.

## Against

Open-ended research with no bounded cost. The arc already has a usable sign
result, and the sign does not depend on the choice, so this blocks nothing.

## Work

- [ ] Identify the functional whose stationarity gives the binding correction.
- [ ] Read off the induced pairing on `H_n(q)` and compare with both families.
- [ ] Should NOT block option A; if it lands, it supersedes whichever was chosen.

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


## 🟧 PROMOTED 2026-09-12 by owner ruling — this is now the live route

Owner, verbatim: *"qou-za3q formalize and derive first.  probably adopt wenzl"*.

Option E (this bean) is the **derive** half and is now the priority. The
Formalize-first policy applies in full: Lean structure before any Python.

**The target.** Derive the Omega2 pairing weight family from the
characterisation of the Markov trace, with the Markov parameter already fixed:

    (i)   cyclicity            tr(ab) = tr(ba)
    (ii)  Markov property     tr_{n+1}(x sigma_n) = z * tr_n(x),  x in H_n
    (iii) normalisation       tr(1) = 1
    (iv)  z = z_D = q^3/(q^2+1)   ALREADY FIXED (owner ruling 2026-08-15, R1)

If (i)-(iv) force the family, the pairing is derived from a ruling the corpus
already holds rather than chosen, and `qou-q2q7`'s Wenzl adoption becomes a
conclusion instead of a premise. That is the whole point of doing it this way.

**What the existing evidence can and cannot do.** The probes' `rho = I` control
is **weight-blind**: `tr(Omega2_lambda) = 0` for each lambda separately by
cyclicity, so `Sum_lambda w(lambda) * 0 = 0` for ANY `w`. It tests cyclicity and
says nothing about the weight. Two facts do bear on it, both already measured:
Wenzl's `tr(1)` is exactly `1.0` at n = 6, 9, 12, and the Plancherel measure
gives `11.139 / 184.233 / 6751.541`, failing (iii) and drifting ~600x across A.

**NOT yet claimed:** that (i)-(iv) are jointly sufficient, or that the forced
family is the row-capped Wenzl one. Both are to be proved. Classical
Markov-trace uniqueness is Jones/Ocneanu, so part of this may be a CITATION
rather than a derivation — a corpus-grep is establishing which, because
re-deriving a held result would be waste and passing a citation off as a
derivation would be worse.
