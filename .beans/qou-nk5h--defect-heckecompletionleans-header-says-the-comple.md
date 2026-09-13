---
# qou-nk5h
title: 'DEFECT: HeckeCompletion.lean''s header says the completed-system GS basis is NOT established, 18,663 lines above the theorem that proves it'
status: todo
type: bug
created_at: 2026-09-13T14:03:26Z
updated_at: 2026-09-13T14:03:26Z
---

## The defect

`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeCompletion.lean`
opens with a section headed **"What is not established here"**. At **line 60**
it still lists:

```
* * that the completed system **is** a Gröbner–Shirshov basis. That is the whole
  of Bokut & Shiao's theorem, and it needs the overlap analysis re-run against
  the completed rule set — a strictly larger set of compositions, since the new
  family overlaps itself. Resolving the one overlap that refutes the
  uncompleted system is necessary, not sufficient.
```

**That statement is proved, in this same file, 18,663 lines below it.**
`heckeCompleted_isGrobnerShirshovBasis` at **line 18723** is unconditional —
the `_of_deep` variant at 17280 carries the `hdeep` hypothesis and
`deep_selfOverlap_resolves` (18576) discharges it. Bean `qou-auq3` records the
verification on 2026-08-24: `[propext, Classical.choice, Quot.sound]`, sorry-free,
for every `n` and every `HeckeParams`. A `grep` for a real `sorry` across the
whole `UGB/GrobnerShirshov/` tree returns **zero**.

## Why this is worth fixing rather than shrugging at

A file header is what a reader reads. This one tells them the file's headline
result is **not** established, when the file proves it — the reader concludes the
opposite of the truth and stops. That is the same class as every other staleness
trap in this corpus, with the aggravating factor that the correct answer is in
the same file.

**The malformed bullet is the tell.** The list item reads `* * that the completed
system…` — a doubled marker. Its sibling immediately above was updated in place
to `* **DONE (§4h).** The general leading monomial …`, and this one was not: the
`**DONE** ` was spliced onto the wrong line, leaving `* *` behind. So the header
was *partially* maintained, which is worse than not maintained at all — a reader
sees one item marked DONE and reasonably infers the unmarked one is still open.

## What the repair is

Mark the item done, pointing at `heckeCompleted_isGrobnerShirshovBasis` (line
18723) and `deep_selfOverlap_resolves` (18576), and fix the `* *` bullet.

Keep the **third** tier honest while doing it, because it is a real distinction
and the header is the right place for it:

| claim | status |
|---|---|
| completed system is a GS basis | **unconditional**, sorry-free |
| completed system has unique normal forms | `heckeCompleted_normalForm_unique` (18766) routes through `normal_form_unique`, which rides on the Diamond-Lemma **axioms** `reduction_well_founded` (`Basic.lean:800`) and `local_confluence` (`CompositionLemma.lean:77`, Bergman 1978 §3 Thm 1.2) |

The GS-basis criterion does **not** depend on those two axioms; the uniqueness
corollary does. `qou-auq3`'s closing note already states this correctly, so the
wording can be lifted from there.

## Scope

NOT done in the `qou-43co` fix that found it: different paper
(`unital-groebner-bases`, not `quantum-observable-universe`) and out of that
bean's scope. Editing an 18.8k-line Lean file's header also wants a `lean`-direct
re-verify of the file, which is its own cost.

## How it was found

Writing the corrected `def:hecke-normal-form` block (`qou-43co`). The header was
read first and taken at face value — the block was about to say the `H_n(q)`
completion theorem is not established in this folio, which would have been a
false "open" declaration in a content block. The corpus-grep checklist caught it:
bean `qou-auq3` is `completed` and its body names the theorem.
