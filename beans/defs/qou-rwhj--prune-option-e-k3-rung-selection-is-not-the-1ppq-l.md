---
# qou-rwhj
title: 'PRUNE: Option E k>=3 rung-selection is NOT the 1ppQ lever — ladder is C-frame-unmoored under D, and the digit budget is ~2 at c_3 / 0 beyond'
status: todo
type: task
created_at: 2026-08-16T13:32:51Z
updated_at: 2026-08-16T13:32:51Z
---


## Why this prunes (2026-08-16)

I proposed Option E to the owner as "the next step for 1ppQ" — a canonical,
non-fitted rung-selection rule extending the tau_M derivation to k>=3, displacing
the k=2 truncation. Then I ran the corpus-grep checklist before starting, and it
does not survive. TWO INDEPENDENT grounds, either sufficient:

### 1. The ladder is convention-C end to end, and D is now canonical

`docs/audits/2026-08-16-ck-ladder-red-team.md` §(c), landed on main the same day
(bean qou-cds1), is unambiguous:

  > "No. Under the now-canonical convention D the entire ladder is unmoored, and
  >  this is not repairable by substitution."

z_C sits at `qbeta_utils.py:124` and again in the KC21/KC22 D(u-tilde) core and
ZBarParity. AGENTS.md already warns the re-derivation "is not a z-swap" —
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame ladder
and the mass channel's three-row forcing MUTUALLY EXCLUSIVE. So extending a
C-frame ladder to k>=3 builds on an object the corpus has already declared
non-canonical. There is no defined D-frame target to extend yet.

### 2. The information is not there — this is a formalize-first entropy prune

Even granting a perfect derivation, the VALIDATION budget is nearly empty:

    c_3       ~2 reliable digits
    k >= 4    ZERO reliable digits (extraction amplifies sigma(Q_beta) by 1/u^k)
    sigma(c_3) = +-1.262, i.e. 61 % of |c_3|
    c_4 reproduces as IDENTICALLY ZERO when c_3 is extracted exactly

The audit's accounting: "the ladder has as many free parameters as it has rungs
and one datum to fit." Q_beta^exp is ONE measured scalar per anchor; c_3, c_4, …
are not independent observables but a residual expansion of that one scalar. So a
derived c_k>=4 cannot be confirmed OR refuted against Q_beta — it is
unfalsifiable, not merely unproven.

This is the same shape as the PSLQ entropy bound that killed the 12-constant
basis (AGENTS.md §Formalize-first): a structural argument that prunes the class
BEFORE the expensive search. Cost avoided: a multi-session crystal derivation
whose output could not have been validated past ~2 digits.

### What this does NOT say (scope (a), not (b))

NOT excluded: that a canonical rung-selection rule exists, or that Option E is
wrong mathematics. NOT excluded: Option E under a *re-derived D-frame ladder*.
What is excluded is Option E **as the next 1ppQ step, against the current
C-frame ladder** — the target is unmoored and the check is unfalsifiable.

### Consequence for the 1ppQ path

Q_beta, m_n and Delta_pn are ONE gap, not three (m_n and Delta_pn propagate
Q_beta; misses cluster 152-177x). That gap runs through the ladder. So the
PREREQUISITE for the 1ppQ work on all three is qou-cds1 — re-derive the ladder
under D — not an extension of the C-frame one.

The fourth miss, m_mu at 970x, is NOT a precision deficit at all: it is the
mu-p pin artifact (proton-pinned => m_mu is a prediction carrying the ~11.5 ppb
theory residual). More digits cannot move it.
