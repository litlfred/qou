---
# qou-n1dj
title: 'GAP: does the MASS fibre functor land in Rep(SU_q(2))~TL or full H_3(q)? (corpus self-contradiction, D vs C, 197 ppm on m_p)'
status: todo
type: task
created_at: 2026-08-08T09:50:22Z
updated_at: 2026-08-08T09:50:22Z
---

Spun out of [`qou-3qrv`](qou-3qrv--class-i-is-the-borromean-trace-convention-forced-o.md)
on 2026-08-08 (branch `claude/3qrv-borromean-trace-convention-2026-08-08`), which
answered everything *except* this. Full analysis:
[`docs/audits/2026-08-08-borromean-trace-convention-forcing.md`](../docs/audits/2026-08-08-borromean-trace-convention-forcing.md).

## The one open question

> Does the Archimedean / fibre functor for the **mass** channel land in
> `Rep(SU_q(2)) ≃ TL₃`, or in the full `H₃(q)`?

Everything else is settled. This is a **categorical** question, and it must not
be answered by reading off which value matches CODATA — that is precisely the
failure mode `qou-3qrv` was opened to test for.

## Why it matters — 197 ppm on m_p, and the corpus disagrees with itself

Two normalised Markov traces on H₃(q) sit 195 ppm apart on `β_Bor`:

| | weight vector `(y_(3), y_(2,1), y_(1³))` at q₀ | `tr_M(β_Bor)` |
|---|---|---|
| **D** — Jones / Temperley–Lieb | `(0.505404, 0.247298, 0)` | 0.998562163836787 |
| **C** — full-Hecke Ocneanu / Wenzl z-trace | `(0.415396, 0.280930, 0.022745)` | 0.998366622585716 |

Both are legitimate (`Σ_λ y_λ d_λ = 1` for both) — two members of the Ocneanu
one-parameter family at different `z`.

- **Production uses D**: `canonical_mass.py:108` → `F_Bor` →
  `m_p_substrate_identity_50dps.trM_borromean`.
- **The paper says C**: the scope note of `prop:h3-markov-wenzl-weights`
  ([`h3-markov-wenzl-weights-context.md`](../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md))
  states verbatim that the mass and binding computations use the **full-Hecke
  Ocneanu** trace at `z = 1/(q^{1/2}+q^{-1/2})`.

Switching production D→C moves m_p by **−197 ppm** (2026-07-03 impact probe),
destroying the CODATA match. So the two statements cannot both stand.

## What is already proved (do not re-derive)

`QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean` (sorry-free, no `sorryAx`,
generic `[CommRing R] [IsDomain R]`, division-free): the TL condition
`y_(1³)(z) = 0` has exactly two roots — `z = q`, degenerate (weights `(1,0,0)`,
not faithful on TL₃), and `z = q³/(q²+1)`, which **is** convention D. So:

> **TL ⟹ D, uniquely.** The implication is closed. Only the premise is open.

## Sub-tasks

1. **Find or write the independent argument** that the mass channel's fibre is
   2-dimensional (spin-½ / `Rep(SU_q(2))`) rather than the full Hecke module.
   In-tree hooks not yet chased: `QOU/Knots/KauffmanTL3.lean`,
   `conj:s5-so3-fiber-action`, `QOU/MathlibExt/WenzlSchurElement.lean`.
2. **Reconcile the two corpus statements.** The closed-form proof block and
   `h3-markov-wenzl-weights-context.md` §Scope disagree about which trace feeds
   mass. One is wrong; decide which and fix it.
3. **Correct the false sensitivity claim.** The same scope note says the two
   traces coincide on writhe-0 / π=id braids so "every physical mass prediction
   is insensitive to the distinction". `β_Bor` is writhe-0 with π=id and
   `D − C = 1.9554e-4` there **exactly** (nonzero rational function). The claim
   is refuted by a probe already in this corpus.
4. **Do not re-open the 6.7 %** — `qou-3qrv` settled it: `tr_M_atomic(1,0)`
   traces a different (11-crossing atomic) braid word, not `β_Bor`.

## Scope

Honest-gap bean per AGENTS §"When you can't close it". This is **not** a claim
that m_p is fitted or that D is wrong — D is a canonical, uniquely
characterised object. It is the narrower claim that D's *selection over C* does
not currently rest on an established premise, and that the corpus is
self-inconsistent about it.

