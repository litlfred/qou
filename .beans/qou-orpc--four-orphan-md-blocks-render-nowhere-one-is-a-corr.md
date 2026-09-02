---
# qou-orpc
title: Four orphan .md blocks render nowhere; one is a c₃ correction the corpus later retracted work for not having
status: completed
type: task
priority: normal
tags:
    - content
    - orphan
    - c3
created_at: 2026-08-22T07:05:00Z
updated_at: 2026-08-24T13:25:29Z
---

Two independent trap-drain batches (`pq_06`, `pq_08`) each flagged a content
`.md` with no `.ts` sibling. Measured the class corpus-wide rather than
collecting instances:

```
3553  .md under content/quantum-observable-universe/
   5  have no .ts sibling
   5  are referenced by no .ts anywhere under content/
```

**The class is bounded at four**, not open-ended — the fifth,
`lean/AUDIT-REPORT.md`, is generated output and not a content block. The two
batches between them found all four. Nothing is hiding here.

| file | what it is |
|---|---|
| `mass-theory/q-beta-c3-continuum-geometry.md` | **a correction — see below** |
| `mass-theory/q-clt-jsj-mass-scaling.md` | q-CLT / JSJ volume scaling for heavy isotopes |
| `mass-theory/qbeta-fmap-structural-form.md` | structural form of the f-map |
| `predicted-spectra/spectral-decomposition-qvalue-interpretation.md` | the only prose referencing `tbl:spectral-decomposition-qvalue-table1-data`, which **is** in the manifest — so that table renders unreferenced |

## The one that matters

[`q-beta-c3-continuum-geometry.md`](../content/quantum-observable-universe/mass-theory/q-beta-c3-continuum-geometry.md)
opens with a correction banner dated **2026-07-11** retiring the
`c₃ → −Vol(4₁)` identification from "exact / rigorous" to **scope-limited**:

> `−Vol(4₁) ≈ −2.02988` is **anchor-blind** and misses **both** substrate
> anchors (muon **+0.479%**, proton **−1.907%**) while the actual `c₃` **swings
> 2.43%** … So the "continuum limit is exactly −Vol(4₁), rigorously banishing
> all algebraic truncations" claim is **not** supported.

**Every number in it verifies.** Recomputed at 30 dps from `Cl₂` and the live
anchors (`c₃(μ) = −2.0202002328`, `c₃(p) = −2.0693425728`):

| block | recomputed |
|---|---|
| `Vol(4₁) ≈ 2.02988` | `2.02988321282` |
| `V(π/3) ≈ 1.01494` | `1.01494160641` |
| muon `+0.479%` | `+0.479308%` |
| proton `−1.907%` | `−1.90685%` |
| swing `2.43%` | `2.43255%` (muon-normalised) |
| `Vol(4₁)/π ≈ 0.6461318` | `0.646131894` — printed value is a **truncation**, not a rounding |

And the content is not duplicated anywhere that renders: grepping its
distinctive phrases returns the orphan itself plus two blocks that merely share
vocabulary.

## Why this is worth more than a cleanup ticket

AGENTS.md carries a STRICT section, **"Defined residual ≠ derived
decomposition"**, added **2026-08-08**, whose worked case is an agent building
a c₃ candidate filter on `S_leak := c₃ + Vol(4₁)` — i.e. on the very
identification this block corrects — publishing it to a sibling PR, and having
to retract it. The author caught it with one question: *"this is not derived?"*

So the sequence, as facts:

1. A numerically sound correction to that identification existed in the tree on
   **2026-07-11**.
2. It renders nowhere and is reachable only by opening the file directly.
3. Four weeks later the corpus retracted work built on the uncorrected claim.

**(3) following from (1)+(2) is an inference, not established** — nobody has
said they looked for this and missed it. But the standing corpus-grep checklist
tells agents to search `content/`, and a `grep -rl` over `content/` *does* find
this file. What it does not do is tell you the file is unreachable to a reader,
which is the failure mode: the block looks like corpus, and is not.

## Disposition

Not attempted here — giving a block a `.ts` decides where it renders and under
what `kind` and `label`, which is an editorial call about the chapter's
structure, not a mechanical fix. Concretely what has to be decided per file:

- **`q-beta-c3-continuum-geometry`** — this is the urgent one. Either wire it in
  (the banner is §4d `authorNotes` material; the body is a `remark` interpreting
  the ladder), or fold its correction into whichever block currently states the
  identification. Leaving a live correction unreachable is the worst of the
  three options.
- **`spectral-decomposition-qvalue-interpretation`** — cheapest. Its content
  already survives in `-proof.md` + `-geometric.md`; wiring it back also fixes
  a table that currently renders with no in-text reference. `pq_06` noted its
  longer subordinated sentences read as the pre-split originals of their
  choppier counterparts, so it is also the reference copy for repairing that
  sweep damage.
- The other two — decide whether they are content or working notes. If notes,
  they belong outside `content/`.

## Note on `qou-0vbv`

That bean's two items are both stale, checked just now:
`ns-kummer-specialisation-divisibility` **no longer exists anywhere** (no `.md`,
no `.ts`, no manifest reference), and the `\pic_s` / `\pic_q` sites in
`acoustic-horizon-thermodynamics.md` were fixed in this campaign along with the
sixteen compound-macro stubs that made them render wrongly rather than fail
loudly. Its third item — the `leray-profile-construction` wording — is
untouched and still needs an author. Left open rather than closed; that is the
author's call.

## Resolved 2026-08-24 — all four, but the "bounded at four" claim did not hold

### The four

| file | outcome |
|---|---|
| `q-beta-c3-continuum-geometry.md` | `.ts` written — the c₃ correction renders |
| `q-clt-jsj-mass-scaling.md` | `.ts` written |
| `spectral-decomposition-qvalue-interpretation.md` | `.ts` written |
| `qbeta-fmap-structural-form.md` | deleted outright |

Fixed on `main`, not by me — three got manifests and one was deleted, which is
the split this bean argued for: it warned that deleting was wrong for the c₃
correction specifically, and that one was kept.

`run-validate` on the merged tree: **`✓ Valid — 26 issues, 0 errors`**. The
four `✗` these produced are gone.

### The class was not bounded

This bean stated: *"The class is bounded at four, not open-ended … Nothing is
hiding here."* Re-measured today: **3571 `.md`, 18 with no `.ts` sibling.**

That claim was a point-in-time measurement presented as a structural fact, and
it has been falsified. The breakdown is reassuring but the framing was not:

- **13** live under `*/audit/` — probe write-ups, a deliberate non-block
  convention, not orphan content.
- **1** is `lean/AUDIT-REPORT.md`, generated, which this bean already excluded.
- **3** are genuinely unmanifested prose, and they are new since:
  `PieceACornerInduction.md`, `PieceASpechtCharacter.md`, `bring_tetraplectic.md`.

So the *content-block* class really is small — but it refills, and a bean that
says "nothing is hiding here" invites nobody to look again. Follow-up:
`qou-os3o`.

### Not the same defect as `qou-efzm` item 2

Worth separating, because the two beans were being treated as one problem.
`qou-efzm`'s `section-title-audit.qa.json` files are **live paper-level audit
output** misfiled under a block-sidecar extension — fixed in the checker
(`folio-assistant@8835ee6`), not by deletion. These four were genuinely
unmanifested prose. Same symptom, opposite remedies.
