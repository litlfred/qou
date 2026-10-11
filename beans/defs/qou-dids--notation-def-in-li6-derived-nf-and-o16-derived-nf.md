---
# qou-dids
title: 'NOTATION: |def| in li6-derived-nf and o16-derived-nf is an undefined synonym for the formally-defined |dem| (demand magnitude); the Li6 ''table order'' complaint does not reproduce'
status: completed
type: task
priority: normal
tags:
    - 8f-decide
    - reorg-2026-10-04
    - split-from-6766
created_at: 2026-10-10T08:13:13Z
updated_at: 2026-10-10T10:18:49Z
parent: qou-8lxd
---

Split out of `qou-6766` on 2026-10-10 (seven findings packed into one title).
This is residual item (2) of four — **and the item as originally stated does not
reproduce.** Recording both halves, because the negative is the more useful one.

## The original complaint, "Li6 table order", is NOT reproducible

Checked `folio/quantum-observable-universe/nuclear-interactions/li6-derived-nf.md`
against its sibling `li6-derived-nf-table-data.md`. The narrative and the table
agree on every orderable claim:

| narrative says | table row |
|---|---|
| "He-4 core is built by Regime I → II operators" | `A = 2` I, `A = 3,4` II |
| "The fifth nucleon still uses a Hopf link" | `A = 5` -> `L_-` (mirror Hopf), II |
| "the sixth nucleon transitions to the bare mixed crossing `C_pn` (Regime III)" | `A = 6` -> `C_pn`, **III** |

Build order `p -> pp -> ppn -> ppnn -> pppnn -> pppnnn` terminates at `3p3n`,
which is Li-6 (`Z = 3, N = 3, A = 6`). **Surface searched:** both `.md` siblings
in full, the `.ts` manifests, and the regime labels. If there is an ordering
defect it is not in the step sequence, the regime assignment, or the narrative's
three ordinal claims. State what observation would separate them before
re-opening this half.

## What IS there: `|def|` is an undefined synonym for the defined `|dem|`

`def:demand-profile`
(`folio/quantum-observable-universe/nuclear-interactions/demand-profile.md`)
formally defines

```
dem(A) = {(w, c_w) : c_w < 0}        |dem| = Σ_{c_w < 0} |c_w|
```

i.e. **the demand magnitude is the sum of the negative coefficients.** Two blocks
then write `|\mathrm{def}|` for exactly that quantity:

- `li6-derived-nf.md:18` — `|def| = 0` justified by *"(all coefficients
  positive)"*, which is literally `|dem| = 0` under the definition above;
- `o16-derived-nf.md:23` — *"minimizes `|def|` among all `A = 16` isotopes … the
  doubly-magic nucleus attains `|def| = 0`"*, same quantity, same reading.

Counts, corpus-wide in `.md`: `\mathrm{dem}` in **5** files (including the three
`demand-*` blocks that define and use it), `\mathrm{def}` in **2** — the two
above. **Neither symbol appears in `notation/notation-register.md`.**

So this is one quantity under two names, the minority name having no definition
anywhere, in a corpus whose §7aa register is meant to be authoritative.

## Options

1. **`|def| -> |dem|` in the two blocks** and add the symbol to the notation
   register. Cost: 2 one-token prose edits + 1 register row. Risk: near zero —
   both sites' surrounding text already states the demand reading.
2. **Keep `|def|` and define it**, as a deliberately distinct notion (e.g.
   deficit = demand restricted to some letter class). Cost: a new definition
   block; requires that a distinction actually exists, which this bean found no
   evidence for.
3. **Nothing.**

**Recommendation (agent judgement):** (1). It is the narrowest change that makes
the two sites agree with the definition they are already using, and it is the
kind of fix that the register exists to make unnecessary.

**Default if unanswered: (3), nothing changes.** Two blocks keep an undefined
symbol; no number moves, nothing downstream reads either name.

**Blast radius:** `ex:li6-derived-nf`, `ex:o16-derived-nf`, and
`notation/notation-register.md`. No compute, no Lean, no witness.


## ENACTED 2026-10-10 — owner picked it; option 1, as recommended

`|\mathrm{def}|` → `|\mathrm{dem}|` at both sites (`li6-derived-nf.md:18`,
`o16-derived-nf.md:23`), and a new **"Demand magnitude: always $|\mathrm{dem}|$,
never $|\mathrm{def}|$"** section in
`folio/quantum-observable-universe/notation/notation-collisions.md`. Measured
after: **zero** `mathrm{def}` occurrences remain anywhere in the content tree.

It went to the collisions file rather than a per-chapter register table because
`nuclear-interactions` has no register table of its own, and because a
same-quantity-two-names defect is a *collision*, which is that file's stated
subject.

**One thing the register entry is careful about**, and it is the part to keep:
the prose word **"deficit" is not banned**. *deficit-free*, *deficit closure*
and *the periodic table deficit conjecture* are English for the same condition
and are fine. Only the undefined **symbol** is banned, because a reader meeting
it has nothing to resolve it against.

**Verification, including a self-caught regression.** The first draft of the
register section tripped `voice-editorializing` (the word *naturally*) — a
**new** minor on a block whose measured baseline was 1 critical / 2 major /
**0 minor**. The adverb was dropped and the block is back to exactly that
baseline, so this edit adds **zero** findings. The pre-existing critical
(`voice-unicode-crash`, line 137) and two majors (lines 21, 26) are untouched
and are not in the new section.
