---
# qou-a3qo
title: 'AGENTS/cheat-sheet: "the lambda_A fit artifact" cites an audit measured 6-of-7 ROBUST'
status: completed
type: task
priority: normal
created_at: 2026-09-14T18:32:11Z
updated_at: 2026-09-14T18:38:45Z
---

## 2026-09-14 — the finding, the fix, and the two things NOT touched

Raised by the owner: *"corpus conclusion maybe b/c bad compute - be wary."* Checking
what I had just relayed to them found this, which is not bad compute but bad
citation — the same failure class one level up.

### The defect

Four sites in `docs/canonical-derivation-cheat-sheet.md` (lines 51, 63, 371, 385)
read *"the +2.89-3.86% absolute-mass gap was the lambda_A FIT ARTIFACT"*, citing
`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`.

**Citation defect.** That audit is about whether lambda_A-baselined REFUTATIONS
were artifacts — the owner's 2026-06-24 hypothesis, *"Lots of refutations of
binding / shell quadratic corrections [were reached] bc using the wrong
density."* It closes with *"This audit does not yet claim any refutation is an
artifact — it localizes the 7 candidates and sets the re-run protocol."*

The re-runs DID land: 2026-07-17, bean `qou-sqgf`, 7 scripts + 7 witnesses
committed, `docs/audits/2026-07-17-perknot-density-rerun-execution-and-frame-reassessment.md`.
Verdict **6 of 7 ROBUST, 1 partially artifact** (the additive `S(K)` refutation,
whose sign-flip disappears on the per-knot base). So the hypothesis the cited
audit was testing LARGELY DID NOT HOLD, and a reader following the link lands on
the opposite-signed result.

**Implication defect.** "Artifact" invites "remove the fit and the gap closes".
From the cited audit's own §Critical nuance:

    global lambda_A (the fit)   m_p 966  m_n 967   +2.96 %
    per-knot tr_M(K)            m_p 406  m_n 352   -57 % / -62 %

    "neither density reproduces the absolute nucleon mass;
     the true density sits ~2.46 between them."

Removing the fit makes the miss ~20x LARGER in the other direction.

### The fix (PR #7389, issue #7388)

The half that was right is kept — the number is produced by a fitted form
(`Vol(B3).lambda_A/hbar_q^2`, lambda_A CODATA-implied), deprecated for absolute
mass 2026-06-24, and is not a live discrepancy a wire-up would close. Added: the
per-knot swap does not fix it (-57 %), and the refutation-artifact question is
separate and measured 6/7 robust. Citations re-pointed at
`docs/canonical-mass-formula-guardrail.md` (the actual resolution doc), with the
2026-07-17 execution audit named where the 6/7 is quoted.

### NOT touched — measured, not assumed

- **`AGENTS.md` does NOT carry this claim.** Zero hits for the phrase. I had told
  the owner it was live there; **that was wrong.** What AGENTS.md carries at 2406
  is a different (and separately superseded) sentence about the "2.89% m_p gap"
  vs a `lambda_scale` closure.
- **`docs/canonical-mass-formula-guardrail.md` is CORRECT as written** —
  *"DEPRECATED Vol(B3).lambda_A/hbar_q^2 wrong form — a purged fit. Not a real
  discrepancy"*, citing the audit as a *resolution* audit. Misstates nothing.
- **Dated audit docs keep the old figures** as records of their own analyses,
  per the `qou-3nva` precedent.

### The trap worth carrying

**A citation is a claim, and it decays independently of the sentence it
supports.** Both halves of this sentence were written in June and only one aged:
the *number* stayed correctly described as fitted, while the *audit it points at*
was superseded a month later by its own re-run protocol. Nothing in the corpus
flags a citation whose target reached the opposite conclusion — the link still
resolves, the audit still exists, and the grep still matches. The discriminator
is to open the cited doc and read its conclusion, not its title.

**And "3 sites" was wrong before it was measured.** I told the owner ~3; it is 4,
all in one file, and zero in the file I named first. Measure the surface before
quoting its size, including when the surface is prose.
