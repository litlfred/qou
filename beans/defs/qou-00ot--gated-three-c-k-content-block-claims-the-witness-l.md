---
# qou-00ot
title: 'GATED: three c_k content-block claims the witness layer already scopes and the paper does not'
status: completed
type: task
priority: high
created_at: 2026-09-14T08:02:26Z
updated_at: 2026-09-14T18:11:17Z
---

Found 2026-09-14 while tracing the D2 convention finding (PR #7343, qou-cds1)
into the content layer. **The machine-readable layer is correctly scoped; the
paper layer is not.** per-observable-100x-status.witness.json carries, in
fields:

    convention_frame_qbeta/status                            = INHERITED_C
    convention_frame_qbeta/canonical                         = D
    convention_frame_qbeta/reproducible_under_canonical_convention = False
    convention_frame_qbeta/tracked_by                        = qou-cds1
    functional_admissibility_qbeta/status                    = INADMISSIBLE_FUNCTIONAL
    functional_admissibility_qbeta/scored_prediction_rests_on_z = 1

None of that reaches the blocks below. Each needs a determination I may not
make under the 2026-09-07 ASK-THE-OWNER directive (neither a precision increase
nor corpus-derived: the corpus does not fix WHICH value or WHICH wording
replaces them).

**FIXED already, not part of this bean:** appendix-qvalues/
per-observable-100x-status-dashboard.md named beats_100x_count (2/7) where
AGENTS.md STRICTLY requires beats_100x_scoreable / scoreable_total (1/6).
That one WAS corpus-derived -> exemption 2, PR #7343 commit 5585ab883d.

---

**1. appendix-qvalues/qbeta-ck-truncation-canonical.md — scoped on the wrong
axis.** This is the block whose stated purpose is recording each rung's
epistemic status, and it does that carefully: c_2 'structural' with the
(1 - b^2 hbar^4)-is-a-definition caveat and the ctilde_2 = -9/8 normalisation
trap; c_3 'near-match' with the anchor-dependence caveat. It says NOTHING about
the Markov convention. Sizes, from qbeta-c3-ladder-trace-convention-sensitivity
.witness.json (main since 2026-09-05, 10/10 PASS):

    anchor swing (the caveat it DOES carry):   0.0495
    convention shift (the one it does not):  972.36     ~ 20000x larger

    c_3 proton   -2.069342577 (C)  ->  -974.4318877 (D)
    implied c_2  -1.017623798 (C)  ->    -9.29886287 (D)

Determination needed: add a convention tier, or restate the existing tiers as
C-frame. Author call — it is a restatement of published epistemic status.

**2. mass-endomorphism/conj-qbeta-c-k-closed-forms.md:45 — a stale c_3.**
Reads 'c_3 extracted = -2.0098'. That matches NO live corpus value:

    proton (C)            -2.069342577
    muon CODATA-2022 (C)  -2.019860312
    muon CODATA-2018 (C)  -2.020200233
    block                 -2.0098

It is ~the pre-#1422 superseded muon -2.0097 that AGENTS.md explicitly flags as
retired. Determination needed: the block does not state its anchor, so which
of the three replaces it is not fixed by the corpus. (Its c_5 = -1.2229 IS
current — do not sweep the whole table.)

**3. mass-endomorphism/conj-qbeta-c-k-closed-forms.md:35 — claims the L2 target
is MET.** 'already achieves a +6.02 ppb residual at N=3, satisfying the 7.8 ppb
accuracy target ... exceeding experimental requirements by two orders of
magnitude.' Live dashboard row, same target:

    Q_beta  err_ppb 1.668e+8   target 7.797   miss 2.139e+7x

HONEST NUANCE, state it whenever citing this: these are different objects. The
block's +6.02 ppb is the C-frame z=1 published cell; the dashboard's figure is
the RULED z_D base with zero c_k rungs. The block is not arithmetically wrong
about its own cell. What it lacks is any signal that (a) that cell is the z=1
one the 2026-09-08 owner ruling retired as inadmissible, (b) the frame is C,
(c) the dashboard scores this observable as the LARGEST miss in the table. A
reader meets an unqualified 'target met'.

Determination needed: this is the qou-58zw Class 2 shape (a block reporting a
retired cell as a live achievement) and is an author call.

---

Blast radius: all three are rendered paper content. #3 is the one a referee
reads as a headline precision claim. 12 of the 15 content blocks mentioning
J_Hopf carry zero convention-scope markers; the other 3 are definition-index,
mba-step11 and markov-pair-z2.

## ENACTED 2026-09-14 — owner picked A, B and C (PR #7343, commit 66bd7adc0f)

All three done. Verification and the deliberate non-fixes:

**A** — qbeta-ck-truncation-canonical.md gains a *Convention frame* section
carrying the C→D re-extraction table, the one-rung localisation, the z-swap
invalidity, and the one convention-IMMUNE pillar (swing ratio 1.00522). Sidecar
clean: 92 criteria, 84 pass / 8 n/a, **zero non-pass**.

**B** — c_3 = -2.0098 marked SUPERSEDED in place with the three live
convention-C extractions; proton named as the one to read. Also recorded,
measured: the other five entries have **no live producer** anywhere under
computations/. c_5 deliberately untouched (it is current).

**C** — the '+6.02 ppb, satisfying the 7.8 ppb target' claim rewritten to give
both figures and state plainly that they are different objects (ruled z_D base
with zero rungs vs five-rung ladder on the retired z = 1 cell).

**Also fixed in passing** — trap-negation-contrast (major) fired on the block I
was editing: 'are not arbitrary fits. They are tautologically determined' was
assert-by-denying; restated plainly.

**Sec 4d compliance** — every date, ruling reference and PR number was stripped
from prose and moved to authorNotes on both .ts siblings.
voice-author-notes-pollution went 1 (A) + 3 (B) → 0.

## NOT cleared, deliberately — read before re-running the sweep

trap-superlative and trap-negation-contrast are still result=fail in B's
sidecar. Both are **agent** verdicts (agent:q16, 2026-08-15, sha b038f72bacf)
written against text this commit changes:

- trap-superlative's quoted evidence now has **zero occurrences** in the file.
- trap-negation-contrast's sentence is rewritten to the wording its own evidence
  points at in the sibling block.

I did not append a pass. Clearing a criterion that flagged my own prose is
self-certification, which is the shape the anti-laundering discipline warns
about. Both are checkable with a grep; a fresh agent pass should re-verdict.

voice-editorializing (minor, line 29) is script-authored, live, and
**byte-identical to main** — pre-existing, out of scope.

## Left open elsewhere

The block's filename says conj- while its kind is `proposition`
(prop:qbeta-c-k-closed-forms) and its body calls its own contents conjectures.
Noted, not touched — a kind change is a Sec 3b propagation question, not part of
this bean.
