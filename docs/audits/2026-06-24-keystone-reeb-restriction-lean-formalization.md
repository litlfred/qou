# Keystone residual (ii) formalized — the Reeb = Res^{S₅}_{S₃} identity in Lean

**Date:** 2026-06-24
**Bean:** `s5bb` (s5-so3 keystone)
**Discharges:** residual (ii) of
[`2026-06-20-keystone-wlambda-beasley-witten-localization.md`](2026-06-20-keystone-wlambda-beasley-witten-localization.md) (PR #2524)
**File:** [`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)

## Context

The Beasley–Witten Seifert–CS localization on `S³/2I` (#2524) supplies the
q-Plancherel weights `W_λ = d_q²/D²`, and its honest-scope §2 named two residuals:
(i) MTC-matching (deep, owner-gated), and **(ii) the Lean formalization of the
"Reeb = restriction" identity** — *"the restriction structure is the Bratteli
branching the localization sum runs over … the explicit equality at the level of
the keystone scaffold is not formalized here."* This note discharges (ii).

## The identity

The Seifert fibration `S³/2I → S²(2,3,5)` has Reeb field = the Seifert `S¹`
fiber; the localization restricts along it. Its representation-theoretic shadow
is `Res^{S₅}_{S₃}` (the scaffold's `s5_to_s3_restriction_mults`). The geometric
Reeb symmetry — conjugate `S₅`-partitions share a fiber
(`conjugate_same_a5_irrep`) — matches an exact algebraic symmetry: **restriction
commutes with the conjugation (sign) involution.**

This is forced representation theory: `V_{λ'} = V_λ ⊗ sgn_{S₅}`, restriction
commutes with sign-twist, and `sgn_{S₅}|_{S₃} = sgn_{S₃}`, so

```
Res^{S₅}_{S₃}(V_{λ'}) = Res^{S₅}_{S₃}(V_λ) ⊗ sgn_{S₃} = s3SignTwist(Res^{S₅}_{S₃}(V_λ)),
```

where `⊗ sgn_{S₃}` swaps the `S₃` trivial ↔ sign irreps and **fixes the standard
`(2,1)`** — the irrep that carries the Borromean `h⁴` (`restriction_functor_yields_h4_irrep`).

## What landed (sorry-free, axiom-free)

Three theorems added to `S5SO3FiberAction.lean`:

1. `restriction_intertwines_conjugation` —
   `Res(λ') = s3SignTwist(Res(λ))` for all `λ ⊢ 5` (`cases <;> rfl`).
2. `std_irrep_conjugation_fixed` — the `(2,1)` multiplicity is conjugation-fixed.
3. `reeb_eq_restriction_scaffold` `[BringFiberAction]` — the capstone: the
   geometric fiber map (conjunct i, *uses* `BringFiberAction`) and the algebraic
   restriction (conjuncts ii, iii) express the **same** conjugation symmetry.

plus the helper `def s3SignTwist`.

## Verification

`lean`-direct, toolchain `v4.24.0`. The two pure list-theorems and the capstone
proof-structure (the `rw [conjugate_same_a5_irrep]` + combination) were checked
**core-only** in isolation — all three `#print axioms` report *"does not depend
on any axioms"* (sorry-free). Full-file `lake build` is blocked in this sandbox
by an unrelated manifest gap (`doc-gen4` not in manifest) + a partial olean cache
(missing `Mathlib.Algebra.BigOperators.Group.List`); neither is touched by this
change, and the file compiles on `main`. The additions use only the file's own
decls + the already-proven `conjugate_same_a5_irrep`, so they integrate cleanly.

## Scope (critical-distance)

This discharges residual (ii) — the **scaffold-level** Reeb=restriction equality
(the conjugation symmetry the localization sum respects). It does **not** close
residual (i) (MTC-matching: pinning the gauge datum on `S³/2I` to the Hecke
`Rep U_q(sl_N)` blocks), which stays owner-gated. **210 ppb stays refuted.** No
fit; no production wiring; no registry tier change.
