---
# qou-c46w
title: prop:brings-smoothness-resolution is a PROPOSITION whose cited Lean proof was True AND True AND True -- owner decision needed on the block kind
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T12:19:32Z
updated_at: 2026-10-04T15:15:01Z
parent: qou-6qbv
---

## The finding (2026-09-12, PR #7208)

`folio/quantum-observable-universe/brings-surface/brings-smoothness-resolution.lean`
carried, until this PR:

```lean
structure BringSurfaceSmoothness where
  transverse : Prop
  intrinsic_resolution : Prop
  regular_foliation : Prop

theorem brings_smoothness_resolution :
    ∃ S : BringSurfaceSmoothness, S.transverse ∧ S.intrinsic_resolution ∧ S.regular_foliation :=
  ⟨⟨True, True, True⟩, trivial, trivial, trivial⟩
```

**The smoothness of the Bring surface was "proved" by `True ∧ True ∧ True`.**

## Why this one is worse than the other 18 `prop-universe-field` carriers

- The block is **`prop:brings-smoothness-resolution`** — a `proposition`, **not** a
  `conjecture`. §3b's conjecture carve-out does not apply.
- Its `.md` states the claim flatly: *"The three power-sum constraints are transverse in
  `ℙ⁴`, so `𝒮` is smooth."*
- Its `.ts` cites this declaration as the proof: `lean: { ref:
  "qou:QOU.BringsSurface.brings_smoothness_resolution" }`.
- It is indexed as a proposition in `index-of-definitions/definition-index.md:785`.

So a proposition the paper carries, and indexes, was backed by a proof term with no
mathematical content. That is a `proof-statement-integrity` failure, not merely a vacuity
smell.

## What was fixed, and what deliberately was not

**Fixed:** the three conditions are now **parameters** and the fields carry actual proofs,
so `⟨True, True, True⟩` no longer type-checks and the triviality cannot hide inside the
carrier. The declaration keeps its name (the `.ts` `lean.ref` resolves to it) and its
docstring says plainly that it is an accessor and must not be cited as a proof of the
block's claim. `lean`-direct exit 0.

**NOT fixed, and it is the owner's call:** the block's claim is *still not proved*, and it
cannot be stated in that file at all — it imports only `Mathlib.Data.Complex.Basic` and has
no Bring surface, no `ℙ⁴`, no Jacobian. The honest dispositions under AGENTS.md §1a are
(a) prove it, which needs the surface formalised; (b) state the real proposition with
`sorry` + `-- Ref:`, which also needs the surface; or (c) **demote the block from
`proposition` to `conjecture`**.

Only (c) is available today, and demoting a block's kind is an author decision with
`.ts` / `.md` / sidecar consequences, so it is not taken here.

## Prior art

The carrier's triviality was demonstrated by name — `BringSurfaceSmoothness` reproduced
verbatim — in `docs/audits/2026-08-23-free-prop-field-triviality-probe.lean` on 2026-08-23.
What that probe did not record is that the carrier backs a **`proposition`** block rather
than a conjecture, which is what makes it the sharpest instance of the pattern rather than
one of nineteen.
