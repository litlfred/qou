# qou-qnnq: internal derivation of `A_ω = 3` — sharpening the target to the q-exact symmetry constant

**Date:** 2026-08-02 · **Bean:** `qou-qnnq` (G3 Stokes keystone, internal-derivation leg) ·
**Branch:** `claude/fibre-observable-functor-integer-2026-08-02` ·
**Tier:** synthesis + formalize-first (Lean, sorry-free) · **Scope:** (a);
nothing fitted; nothing wired; L2 unchanged; no tier change.

> **Status: DRAFT (stub).** Being filled in on the branch above. See the
> one-line verdict below.

## One-line verdict (headline)

**Structurally-open (scope-(a)).** No QOU categorical driver supplies a short
structural argument that *forces* the figure-eight Stokes integer `A_ω = 3`
internally. This PR (i) sharpens the open target — the physics-relevant integer
is the **q-exact GGM symmetry constant** (eq 65: `S₁₂ + S₂₁ = 3·S₁₁`), a
*different and simpler* object than the full resurgent DT spectrum `{3,4}`;
(ii) connects the two existing sorry-free bricks
(`StokesQZeroDTCount` ↔ `StokesSymmetryConstant`) at the q→0 base point with a
new decidable brick; and (iii) names the precise missing ingredient. It does
**not** derive `3` from the 13 drivers — that stays open (`qou-qnnq`), and is
neither axiomatized nor fitted.
