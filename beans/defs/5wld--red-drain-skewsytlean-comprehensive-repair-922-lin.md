---
# 5wld
title: 'Red-drain SkewSYT.lean — comprehensive repair (922 lines): λ→lam rename unmasks 23 deeper errors across whole file'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:23:38Z
updated_at: 2026-06-28T05:57:59Z
---

`content/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean` is red
on main. Two layers:

**Layer 1 (mechanical, done-able in 1 step):** the file uses reserved `λ` as
the partition-variable identifier in 213 places (v4.24 made `λ` a reserved
token). All lambda abstractions use `fun`, so a global rename is safe:
`perl -i -pe 's/λ/lam/g' SkewSYT.lean` (verified: 0 `lam` collisions, 0
letter-adjacent λ). This clears all the `unexpected token 'λ'` parse errors.

**Layer 2 (the real work):** the rename *unmasks* 23 deeper errors the parse
barrier had hidden — spread across the whole file (lines 98→904), not one
root:
- ~7 cascade parse errors `unexpected token '/--'/'/-!'; expected 'lemma'`
  (505, 583, 615, 749, 794, 853, 904)
- `failed to synthesize Decidable (∀ i ∈ Finset.range …)` (98)
- ~5 `Application type mismatch` (130, 132, 491) — hi/hj index hyps
- ~3 `unsolved goals` (206, 208, 216)
- 2 `mod_cast` type errors (772, 826), 2 `unfold skewSYTCount failed` (284, 421),
  `rewrite pattern not found`, etc.

This is genuine per-declaration authoring across a 922-line combinatorics file
(skew SYT counting), not a mechanical drain — defer to a focused session.

**Tooling note (this session):** lemma archaeology works WITHOUT loogle — fetch
the Mathlib **source** at the pinned manifest rev via codeload
(`curl …codeload.github.com/leanprover-community/mathlib4/tar.gz/$REV`) and grep
it. CAVEAT: the restored `lake-cache/qou-v4-24-0` oleans are an OLDER mathlib rev
than the manifest source — some lemmas in the source (`sinh_pos_iff`) are absent
from the olean; verify lemma availability empirically with `lean`-direct, don't
trust source presence alone. (This is how the sibling BarSymmetric red-drain in
the same PR was fixed.)
