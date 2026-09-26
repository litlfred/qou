---
# gm4q
title: 'Author input needed on generator-volume-decomposition: Binding energy scales exponentially to physically absurd values instead of saturating (e.g. 8.25x10^13 for Bi-210)'
status: in-progress
type: task
priority: normal
created_at: 2026-06-28T23:02:55Z
updated_at: 2026-09-04T02:27:55Z
---

**Answered 2026-09-04** (branch `claude/q407-self-assuming-projections-2026-08-21`).
The mechanism is now derived, and it is not specific to the generator-volume
pipeline: **`tr_M` is multiplicative along the chain and binding energy is
extensive, so any law of the form `B = constant x (a product over nucleons)`
grows exponentially and cannot saturate.**

The Markov-trace pipeline shows the same symptom at different magnitude — the
closed form gives `Q_beta.Delta_tr(210Bi) = 13 121 MeV` against 1 644.8 measured
(8.0x), and 19.6x for 238U — so the `8.25e13` figure recorded here is the
generator-volume version of one defect, not a second one. The two numbers are
not comparable; the shape of the failure is.

Measured over the 2548 AME2020 nuclides with MEASURED binding energies, at the
law's own OPTIMAL scale: p5-p95 spread **1592x**, full range 4.21 decades. No
scale rescues it (`qbeta_no_regime_of_validity_probe.py`).

**The replacement is the log of the same derived numbers**, and `log` is the
unique map carrying multiplicative to additive, so it is forced rather than
chosen:

    B = E_0 . log(tr_M(free)/tr_M(atom))
      = E_0 . [(Z-1)(-ln b_pp) + (-ln b_pn) + (N-1)(-ln b_nn)]

p5-p95 spread **1.225x** on the same 2548 nuclides — a 1300x gain from changing
the FUNCTIONAL, not the constant. Already implemented as
`computations/binding_log_free_energy.py` (bean `lkpl`), never before scanned
against the full table.

Open: the derived `E_0 = m_e/(q0(q0-1)) = 4.186 MeV` is **2.656x** below the best
single scale, and the law is a pure volume term (no surface/Coulomb/symmetry/
pairing), so predicted `B/A` has no peak. Recorded as targets, not searched on.

Full options analysis, pros and cons, and the six open avenues:
`docs/audits/2026-09-04-binding-law-options-decision-frame.md`.
Producer: `computations/qbeta/qbeta_binding_law_options_probe.py` (10/10).

**Needs the owner**, and the ask is now specific rather than open: adopt the
additive law (Option B in that note), or say why not. This bean stays open until
that decision lands on every surface stating `B = Q_beta . Delta_tr` — a
correction is not landed until it reaches every surface stating the old claim.
