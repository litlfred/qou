---
# vwarn
title: The 4 remaining validate warnings are content gaps, not metadata defects — and the tempting fix would manufacture vacuity
status: todo
type: task
priority: medium
tags:
    - verification
    - lean
    - reorg-2026-10-04
    - qa
created_at: 2026-08-08T17:10:00Z
updated_at: 2026-10-04T15:26:09Z
parent: qou-5vkl
---

`✓ Valid — 5 issue(s)`, down from `✗ Invalid — 32`. Every cross-reference
warning is gone. What is left is four, in two classes, and **neither is fixable
by editing metadata.**

## Three propositions with no Lean declaration

`provable-lean-warning` (`schemas/constraints.ts:874`) warns for any
theorem/lemma/proposition/corollary carrying no `lean` field. Exactly three fire
corpus-wide:

    prop:meson-octet-decomposition   eightfold-way/
    prop:borromean-decuplet          eightfold-way/
    prop:tm-gs-normal-form           appendix-transfer-matrices/

None has a `lean` field at all — this is not a mis-pointed ref like the nine
just repaired. Three out of the corpus's several hundred provable blocks are
unformalised, and closing them means writing the mathematics: an SU(3) octet
decomposition, a Borromean decuplet derivation, and a Gröbner–Shirshov normal
form.

**The tempting fix is the dangerous one.** Adding a stub declaration to silence
the warning — `theorem meson_octet_decomposition … : ∃ x, x = e := ⟨_, rfl⟩` —
would manufacture precisely the vacuity class made detectable the same day in
`vrfw`: a `lean` field pointing at a declaration that asserts nothing, with the
block then reporting formal backing it does not have. A truthful warning is
strictly better than a false clean bill.

## One remark with no formal backing, because there is none

`remark-interprets` warns for a remark with no `interprets` field (glossary-tagged
remarks exempt). One fires: `rem:einstein-ether-substrate`.

It is a **historical remark** — Einstein's 1920 Leiden characterisation of the
ether read against the QOU substrate. Its substantive claim is that `q_0` is
fixed by `H^1(Bring) = 2W` rather than by any mechanical medium.

Searched for a provable block to point at: **none exists.** `H^1(Bring) = 2W`
appears only in prose (`epistemic-status-of-calibrations`,
`three-calibration-discipline`, and this remark). No proposition, theorem or
lemma establishes it.

So the warning is accurate: the remark has no formal backing because the thing
it interprets has none. Inventing an `interprets` target would fabricate exactly
the formal-backing edge the field exists to record.

## Recommended

Leave both classes warning until the underlying content exists. They are `⚠`,
the gate is green, and each is a true statement about the corpus. If the
warnings are ever to reach zero, the route is: formalise the three propositions,
and give `H^1(Bring) = 2W` a provable block — not adjust the metadata.
