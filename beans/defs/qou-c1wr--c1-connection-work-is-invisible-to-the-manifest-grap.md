---
# qou-c1wr
title: C1 connection work is invisible to the manifest graph and has no consumer
status: completed
type: task
priority: high
created_at: 2026-08-07T22:20:00Z
updated_at: 2026-09-26T11:03:15Z
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

## 2026-08-07 — action 2 answered for the *divisor*: nothing consumes it

Owner asked directly ("settle (5) — does anything consume this?"). Re-grepped
`content/**/*.ts` for connection matrix / pole divisor / theta-canonical /
connection invariant / `C1ConnectionPoles`:

* **One** block mentions the arc: `conj:qdifference-kernel-prolongation-symbol`.
* It is consumed by `predicted-spectra/schwinger-measure-computational-time.ts`
  (`uses[]`) and listed in `mass-theory/mass-theory.ts` — so it is **not** a leaf
  after all; the earlier note above is wrong on that point and is corrected here.
* But what that block consumes from C1 is route **(B) "numeric
  connection-matrix theta-growth `q^{m²/4}`"** — a *growth rate* — plus the
  isoclinicity result. **Not** the pole divisor, not `χ`, not the closed form,
  not `α = t₂/T`.

So the answer splits:

| C1 result | consumed? |
|---|---|
| theta-growth `q^{m²/4}`, isoclinicity | **yes**, via `conj:qdifference-kernel-prolongation-symbol` → schwinger-measure block |
| connection matrix, pole divisor, `χ` closed form, `α = t₂/T`, order 2 | **no**, by anything |

That makes the divisor and the invariant closed form genuinely orphaned work,
not merely unwired work. Recorded in `qou-c1ln` as the reason not to spend the
argument principle on row 5. Action 1 (authoring a block) is still worth doing
for the *record* — the results are correct and expensive to re-derive — but it
should say plainly that nothing downstream consumes them, rather than implying
a dependency that does not exist.

Relates: `qou-wgnx`, `qou-7ylg`, `qou-c1ln`.

## 2026-08-08 — action 1 done: the arc has a content block

`prop:c1-theta-zero-locus-and-pole-divisor`
(`mass-theory/c1-theta-zero-locus-and-pole-divisor.{ts,md}`), wired into
`sec:hoefsmit-qdifference-prolongation` alongside the keystone, with
`lean.ref` to `QOU.QBeta.C1Poles.qTheta_neg_zpow_eq_zero`.

It `uses[]` exactly one thing — `conj:qdifference-kernel-prolongation-symbol`,
the arc's actual context — and **says in its own prose that nothing consumes
it**, per action 2. It claims deliberately less than the computations do: the
vanishing, holomorphy, functional equation, winding step and series convergence
are stated as proved; the converse zero locus, the divisor, `χ`, `α = t₂/T` and
the closed form are stated as numerical or open, with the single missing lemma
named (argument principle, bean `qou-argp`).

So the arc is no longer invisible to the manifest graph, and it is recorded at
its true epistemic weight rather than upgraded by being written down. Both
actions of this bean are now discharged; what remains is not a wiring question
but the mathematics, tracked in `qou-argp` and `qou-c1ln` rows 4/6.
