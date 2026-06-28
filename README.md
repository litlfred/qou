# lake-cache addon — RepresentationTheory + SimpleModule (Wedderburn–Artin) oleans

**Toolchain:** `leanprover/lean4:v4.24.0` · **Mathlib:** `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`

Eleven Mathlib oleans **not** in the base QOU dependency closure, built from the
pinned-commit source. Needed by
`content/quantum-observable-universe/lean/QOU/BraidKnot/{MaschkeSnSemisimple,WedderburnSn}.lean`
(`Mathlib.RepresentationTheory.{Basic,Maschke}`,
`Mathlib.RingTheory.SimpleModule.{WedderburnArtin,Isotypic,IsAlgClosed}` + cone deps:
`RingTheory.{Artinian.Module,FiniteLength,Jacobson.Semiprimary,SimpleRing.Congr}`,
`Order.CompleteSublattice`, `Data.SetLike.Fintype`).

This is an **ADDON** to the base `lake-cache/qou-v4-24-0` restore — fetch + extract it
*after* the base restore, so a future rep-theory/OV session does not rebuild these ~11
modules from source (~5 min).

## Restore (after the base `lake-cache/qou-v4-24-0` restore)

```bash
ROOT=$(git rev-parse --show-toplevel); T=$(mktemp)
git fetch --depth=1 origin lake-cache/qou-v4-24-0-repthy-wedderburn
git show FETCH_HEAD:addon-oleans.tgz > "$T"
tar xzf "$T" -C "$ROOT"   # extracts straight over .lake/packages/mathlib/.lake/build/lib/lean/
```
