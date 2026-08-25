---
# xbz1
title: 'q-Casimir classical limit: qNumberSym_classical_limit'
status: completed
type: task
priority: normal
created_at: 2026-06-20T00:00:00Z
updated_at: 2026-08-23T00:00:00Z
---

<!-- front-matter added 2026-08-23. This file had none, so it carried no id,
     no status and no title, and was invisible to the tracker. Original note
     preserved verbatim below. -->

## Original note (undated)

# qNumberSym_classical_limit

The theorem `qNumberSym_classical_limit` in `q-casimir-classical-limit.lean` requires evaluating the limit of `qIntBalZ` as `q \to 1`. Since `qIntBalZ q n` is `(q^n - q^{-n})/(q - q^{-1})`, this is a L'Hopital rule application or a geometric series expansion.
This proof requires limits over polynomials or geometric series which are currently not straightforward without additional Mathlib infrastructure.

## Verified closed 2026-08-23 — `content/quantum-observable-universe/braids-and-knots/q-casimir-classical-limit.lean`

`qNumberSym_classical_limit` is **proved** (`cases n` into the `ofNat` case's
`qNumberSym_classical_limit_nat` and a `negSucc` reduction through
`qIntBalZ_neg`). The file has 0 code-level `sorry` and 0 `axiom`.
