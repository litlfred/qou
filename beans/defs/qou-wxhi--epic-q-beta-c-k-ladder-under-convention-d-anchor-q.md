---
# qou-wxhi
title: 'EPIC: Q_beta c_k ladder under convention D (anchor qou-cds1)'
status: todo
type: epic
priority: high
created_at: 2026-11-15T17:33:01Z
updated_at: 2026-11-15T17:34:40Z
parent: qou-10v9
---

Epic opened 2026-11-15 on owner request (project thread "Re-derive the c_k ladder under convention D").

**Goal.** Re-derive the Q_beta c_k correction ladder under convention D: the decay
functional is the Markov trace at z_D = q^3/(q^2+1) (owner ruling 2026-09-08, D7),
and the mass trace sits at the proton pin. Anchor bean: `qou-cds1`.

**What is known at opening (carried from the precision and Q_beta threads, not re-measured here):**
- No convention-D c_k ladder exists. `qou-cds1` shows it is not a z-swap:
  `decayLadder_zC_threeRow_ne_zero` (sorry-free, PR #5111) forbids keeping the C-frame ladder
  under the two-row forcing. The current extractor fed z_D returns c_3 ~ -974; that is a
  sensitivity number, not a value.
- Delta_pn, Q_beta and m_n are off by 10-17% from one root cause: the base element
  nuc11_interleaved fails the confinement SDP on its (2,1) block.
- LadderFactorBound.lean caps the N=2 factor below 1; the ruled base needs ~1.20.
- The replacement base element is an open owner decision (`qou-99qc`).
- Muon c_3 pin in use: -2.02020024 (CODATA-2018 era; see AGENTS.md proton c_3 note).
- `qou-a613`: the canonical c_k compute does not run / records no c_k under D.

**Discipline.** Formalize-first; no fitting; no empirical numbers inside Lean proofs.
A ladder that lands on a nice number by search is a fit.

**Children (core derivation):** cds1, a613, q2oa, pmkh, zuva, vuaj, cds2.
**Downstream (stay in the Q_beta queue qou-avtq, now marked blocked-by cds1):** the 23
beans listed as "blocked on cds1" in the 2026-11-15 Q_beta verification CSV.



**Baseline (from the Q_beta thread, 2026-11-15, not re-measured here):** n-p splitting alpha*|Phi(udd)-Phi(uud)| is +0.65% under convention C (z = 4993/10000) and 1.054 MeV (-18.5%) under convention D. This is a diagnostic to report against, NOT a target to tune toward (no-fitting rule).



Tracking issue: litlfred/qou#7939.



Correction from the Q_beta thread (2026-11-15): the -18.5 % is the all-pairs strand reading in level1-qvalues.py; the adjacent-crossing reading gives -2.9 % under D. Which reading is intended is an open owner card in the Q_beta thread. Both are diagnostics only.
