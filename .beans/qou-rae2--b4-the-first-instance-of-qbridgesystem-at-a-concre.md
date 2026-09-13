---
# qou-rae2
title: 'B4: THE FIRST INSTANCE of QBridgeSystem at a concrete object'
status: scrapped
type: task
priority: normal
created_at: 2026-09-07T06:35:12Z
updated_at: 2026-09-07T07:16:01Z
---

**SCRAPPED (2026-09-07) — superseded on both halves; neither is this bean.**

B4 asked for "the first instance of `QBridgeSystem` at a concrete object". Two
things were conflated:

1. **A concrete algebraic instance already exists** — `polyQEulerSystem` on
   `R[X]` (dilation `X -> cX`, Euler operator `X d/dX`), plus
   `polyUnipotentSystem` for the mixed/non-semisimple case. Both in
   `QAlienBridgeEquation.lean`, both sorry-free. Done before this bean existed.
2. **An instance arising from a RESURGENT q-SERIES** is what is actually open,
   and it already has a bean: **`qou-vkg5`**. The file header says so verbatim —
   "exhibiting one from a resurgent q-series is untouched. Bean `qou-vkg5`."

So this bean is a duplicate of `qou-vkg5` on the half that is open, and
already-satisfied on the half that is not. Work `qou-vkg5`.

Hard constraint carried over, still valid: do NOT target C1. `qou-wgnx` line 16
records that C1's multipliers are TRIVIAL — the target dissolved rather than
being computed — so an instance built there would be trivially satisfied.
