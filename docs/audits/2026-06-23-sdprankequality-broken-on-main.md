# SDPRankEquality.lean — non-building on `main` (diagnosis + partial verified fix)

**Date:** 2026-06-23
**Session:** `claude/idle-backlog-drain-2026-06-23` (bean `8ehe` — "Resolve
placeholders/TODOs in qou/lean/MathlibExt")
**Verification method:** lean-direct against restored
`lake-cache/qou-v4-24-0` oleans (2951 Mathlib + 197 QOU). The Lean LSP /
search MCP and Mathlib *source* were unavailable this session (oleans
only), so the residual blocker below could not be resolved by lemma
lookup.

## Finding

[`QOU/MathlibExt/SDPRankEquality.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean)
does **not compile** at `main` (31496f5c). Its olean is correctly absent
from the restored cache (it fails to build). The file's own docstring on
`kernel_disjoint_of_range_spans` ("proof body still contains 2 small
`dotProduct_mulVec` adjoint sub-sorries … Treated as TODO until Lean build
verifies the exact lemma names") was **accurate**, not stale — the honest
placeholder counter reports `sorry:0 todo:1` because it counts only the one
literal `TODO` token, but the file has **six** compile errors.

This is consistent with the repo's `continue-on-error` Lean CI (broken
decls are tracked in `proof-objects.json`, not blocking), i.e. this is part
of the known Lean-incompleteness backlog, **not a new regression**.

## The six errors (three distinct causes)

| Line(s) | Cause | Status |
|---|---|---|
| 312 | `rw [← Matrix.mulVec_mulVec, …]` — wrong direction. In this Mathlib `mulVec_mulVec : A *ᵥ B *ᵥ x = (A * B) *ᵥ x`, so the `←` searches for `(M*N) *ᵥ v` (absent). | **FIXED + verified** — drop the `←`. |
| 406 | After `dotProduct_mulVec` the goal carries the `v ᵥ* M` (vecMul) form, so the Hermitian `Mᵀ = M` rewrite finds no `Mᵀ`. | **FIXED + verified** — prepend `← Matrix.mulVec_transpose, ← Matrix.mulVec_transpose` to convert `v ᵥ* M → Mᵀ *ᵥ v`. |
| 467, 470, 555, 558, 563, 566 | `Matrix.rank_eq_finrank_range_toLin'` is an **unknown constant** (used to rewrite `M.rank = finrank ℝ (range M.toLin')`). | **BLOCKER** — needs the correct Mathlib lemma. |
| 440, 499 | "unsolved goals" (`… .rank + … .rank ≤/= n`). | Downstream of the unknown-constant rewrites; should clear once the rank lemma is fixed. |

The first two fixes were applied and re-checked with lean-direct: both
original errors disappeared, leaving only the `rank_eq_finrank_range_toLin'`
errors (and their downstream unsolved goals). The fixes were then **reverted**
to keep `main` pristine (no half-fixed red file committed).

### Verified fixes (apply verbatim)

```lean
-- L312, theorem range_spans_of_dualSlack_posDef
-- before:
  rw [← Matrix.mulVec_mulVec, Matrix.mul_nonsing_inv _ h_isUnit, Matrix.one_mulVec]
-- after:
  rw [Matrix.mulVec_mulVec, Matrix.mul_nonsing_inv _ h_isUnit, Matrix.one_mulVec]
```

```lean
-- L406, theorem kernel_disjoint_of_range_spans
-- before:
    rw [show sc.Φstar.transpose = sc.Φstar from h_Φ_herm,
        show (sdp.dualSlack sc.ystar).transpose = sdp.dualSlack sc.ystar from h_S_herm,
        h_Φv, h_Sv, zero_dotProduct, zero_dotProduct, add_zero]
-- after:
    rw [← Matrix.mulVec_transpose, ← Matrix.mulVec_transpose,
        show sc.Φstar.transpose = sc.Φstar from h_Φ_herm,
        show (sdp.dualSlack sc.ystar).transpose = sdp.dualSlack sc.ystar from h_S_herm,
        h_Φv, h_Sv, zero_dotProduct, zero_dotProduct, add_zero]
```

## Remaining blocker — the rank lemma

Six call sites do `rw [show M.rank = Module.finrank ℝ (LinearMap.range M.toLin')
from Matrix.rank_eq_finrank_range_toLin' M]`. `Matrix.rank_eq_finrank_range_toLin'`
does not exist (unknown constant — version-independent: an absent name is
absent regardless of Mathlib pin). `Matrix.rank` is defined as
`finrank R (range A.mulVecLin)`, so the intended fact is almost certainly
available via either the `mulVecLin` form or the basis-specialised
`Matrix.rank_eq_finrank_range_toLin` (with `Pi.basisFun`). An LSP-equipped
session can confirm in one `lean_loogle`/`lean_leansearch` query
(`Matrix.rank`, `finrank`, `LinearMap.range`, `mulVecLin`).

## Caveat (drift)

Verification used the restored `lake-cache/qou-v4-24-0` oleans; if `main`'s
pinned Mathlib differs from the cache's, a *signature* mismatch could in
principle differ — but the load-bearing error here is an **unknown constant**,
which genuine absence (not drift) best explains. Definitive confirmation
needs a build against `main`'s exact Mathlib pin.

## Recommended next step

An LSP/Mathlib-source-equipped session: apply the two verified fixes above,
resolve `rank_eq_finrank_range_toLin'` to the real lemma, and re-run
lean-direct (or `lake build QOU`) to confirm `SDPRankEquality` green — which
also de-axiomatises nothing new but turns a red module green, removing 6
errors from the QOU `proof-objects.json` error set.
