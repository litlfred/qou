---
# qou-ahbz
title: 'DEFECT: mba-step09b cites a producer-less witness whose numbers contradict the live pipeline by 38-226%'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T16:34:31Z
updated_at: 2026-10-04T15:18:40Z
parent: qou-5vkl
---

## Verified 2026-08-25 (PR #5765)

`folio/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.ts`
declares:

    computation: { script: "qou-mass/src/qou_mass/api.py",
                   witness: "computations/canonical-mass-table-242ppb.witness.json",
                   status: "experimental" }

Three separate problems, in increasing order of severity.

### 1. The script<->witness link is fictional
`grep -rln "canonical-mass-table-242ppb" --include=*.py computations/ tools/` returns
**zero producers**. The named script (`qou_mass/api.py`) is the external-researcher
facade and does not emit this witness. The witness says so itself:

> "Hand-authored summary witness: no producer script was run to generate this file,
> so it carries none of the standard provenance fields (scriptFile, scriptHash,
> scriptCommitSha, computedAt). The per-isotope B(K) values are carried from a
> prior-session mass-table sweep and have NOT been regenerated in this environment."

The AGENTS.md STRICT rule for this appendix requires `computation.script` and
`computation.witness` to stay in sync with the actual compute. They are not.

### 2. The numbers contradict the live canonical pipeline, in the opposite SIGN
Fresh `mass_binding_dashboard.py --group low` this container vs the witness:

| iso | witness B_pred | witness err | live B_sym | live err (B_AME/B_sym) |
|---|--:|--:|--:|--:|
| D   |  2.735 |  +23.0% over |  2.83 | 0.79 (over) |
| T   |  8.992 |   +6.0% over |  6.14 | 1.38 (**under 38%**) |
| 3He |  8.739 |  +13.2% over |  5.37 | 1.44 (**under 44%**) |
| 4He | 29.317 |   +3.6% over |  8.68 | 3.26 (**under 226%**) |
| 6Li | 33.526 |   +4.8% over | 14.53 | 2.20 |
| 7Li | 40.776 |   +3.9% over | 17.84 | 2.20 |

The witness claims per-isotope binding good to +3-6% for A>=3 and OVER-binding
throughout; the live canonical compute UNDER-binds by 38-226% for the same nuclei.
Caveat, stated so this is not over-read: `B_pred` may be a different *form* than
`B_sym` (the witness's `nucleon_source` is "substrate identity + Path C (242 ppb)"),
so this is not necessarily the same quantity mis-computed. It is still the case
that the paper's per-isotope binding block presents accuracy figures that nothing
in the tree reproduces.

### 3. Prior triage under-scoped it
`docs/audits/2026-08-19-tier-e-orphan-triage.md:284` lists it as an orphan and calls
it "honestly labelled" on the strength of `status: "experimental"`. That label is
fair and is NOT the defect. The defect the triage did not record is that the
numbers are now demonstrably inconsistent with the live pipeline and that the
`script` field names a file that cannot produce the witness.

### Disposition (not yet decided - for the work plan)
Either regenerate from a real producer at the canonical convention-D / proton pin,
or retire the witness and have the block cite the live dashboard forms. Do NOT
hand-edit the numbers.

In-progress in Round 99 PR litlfred/qou#8444.
