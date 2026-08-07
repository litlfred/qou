---
# qou-c1wr
title: 'C1 connection work is invisible to the manifest graph and has no consumer'
status: todo
type: task
priority: high
created_at: 2026-08-07T22:20:00Z
updated_at: 2026-08-07T22:20:00Z
---

**Corpus-grep result (2026-08-07).** The entire C1 connection arc lives in
`computations/qbeta/c3_w2_c1_*.py` (9 scripts + witnesses) and
`content/.../lean/QOU/QBeta/C1*.lean` (3 files). **No `.ts` content block
carries any of it** — not the connection matrix, not the pole divisor, not the
closed form for `χ`. Nothing `uses[]` it; no dependency edge reaches it.

This is the **same structural gap** as bean `qou-7ylg`
(`dtEuler_eq_deltaLambda_unconditional`, sorry-free and general-`n`, also with
no content block). Two instances now — worth treating as a pattern, not a
one-off: substantial verified work accumulating outside the manifest graph.

**The natural home already exists:** `conj:qdifference-kernel-prolongation-symbol`
(`mass-theory/`). Its 2026-07-20 author notes already record
*"numeric connection-matrix theta-growth `q^{m²/4}`"*, *"C1 pure isoclinic"*
(citing RSZ Thm 2.2.1/2.2.4/5.5.7), and *"unipotent part trivial, U→I"*. So the
C1 connection results belong attached to, or cited by, that block.

**But that block is itself a leaf** — `grep` for anything `uses[]`-ing
`conj:qdifference-kernel-prolongation-symbol` returns **nothing**. So wiring C1
into it does not by itself give the work a consumer; it only stops it being
invisible.

**Two separable actions:**
1. Author content block(s) for the C1 connection matrix / invariant closed form,
   with `lean.ref` to `QOU.QBeta.C1ConnectionPoles`.
2. **Owner decision:** does anything downstream actually consume C1 connection
   data? If not, say so explicitly in the block rather than leaving it implied.

Relates: `qou-wgnx`, `qou-7ylg`.
