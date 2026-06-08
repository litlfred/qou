# 2026-06-08 — QOU Lean red: Mathlib PosSemidef.sqrt API drift

## Summary

The `qou` Lean package (lib `QOU`) fails to build on current `main`.
Two files are red, both byte-identical to their base — the cause is
upstream **Mathlib API drift**, not repo content:

- `content/quantum-observable-universe/lean/QOU/MathlibExt/PosSemidefTraceZero.lean`
- `content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Formal.lean`

## Reported symptom

`Matrix.PosSemidef.sqrt` dot-notation (`hA.sqrt` where `hA : A.PosSemidef`)
"now resolves to non-existent `And.sqrt`". PSD-square-root API names in
use: `hA.sqrt`, `hA.sq_sqrt`, `hA.posSemidef_sqrt`.

## Status

WIP — reproducing and pinning the exact old→new rename.
