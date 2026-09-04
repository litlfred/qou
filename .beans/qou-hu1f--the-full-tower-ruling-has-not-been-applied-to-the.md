---
# qou-hu1f
title: The full-tower ruling has not been applied to the mass/binding surface, where H_3 is the whole object
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T20:54:56Z
updated_at: 2026-09-04T21:06:22Z
---

Audit: [`2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md`](../docs/audits/2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md)

## The gap

The owner ruled on 2026-09-03 that derivations must be carried on the **full
tower** (both senses: all `n`, all orders in `q`).
[`2026-09-03-sm-26-term-status.md` §10] applies that ruling to the
**standard-model** surface only. It says nothing about mass, binding, or the
nuclear chain -- and that is the surface where bean `qou-tower` has already
measured that **there is no tower**.

Worse, the collapse finding has no durable home: `build_atom_nf_mp` appears in
**zero** files under `docs/` or `content/`. One bean, five probes.

## Re-measured here (a bean is not a primary source)

Direct against `compound_shift_nf.build_atom_nf_mp`:

| nucleus | nominal strands `n = 3A` | NF components |
|---|---|---|
| hydrogen A=1 | 3 | **6** |
| 4He A=4 | 12 | **6** |
| **16O A=16** | **48** | **6** |

16O is a case `qou-tower` never tested and is the sharpest instance.

## Scope correction to qou-tower, which does NOT rescue the tower

`qou-tower` says "the production chain". Measured, `build_atom_nf_mp` has seven
consumers: five probes plus `all_nuclides_sdp_admissibility_mp.py` and
`qbeta_level_k_binding_operator_probe`. It is **not** the canonical mass path.

But `binding_canonical.py` is H_3 too, by a **different mechanism** -- it calls
its own path `tower_binding_full (H_3 tower)` (:37), builds from "the H_3
building blocks tr_M^3(p), tr_M^3(n)" (:324), and bridges at H_3 (:341). So:

- **NF route** -- the tower is built and destroyed (reduced to 6 per crossing);
- **canonical route** -- the tower is never built (per-nucleon H_3 traces are
  composed).

Do not conflate them; `qou-tower`'s argument covers only the first.

## The measurable next step, which nobody has run

`qou-tower`'s full-tower walk measured **distributional** quantities (top-block
share, participation ratio, argmax partition) against magic numbers. It never
compared **a binding energy**. So the obvious question is open:

> Does the A <= 4 full-tower walk reproduce the canonical H_3 binding numbers?

If yes, H_3 is a faithful order-zero rendering and the ruling is satisfied in
substance. If no, the two routes disagree and that gap is the finding. Either
answer is worth having, and A <= 4 is reachable (A=5 needs `max_d^2` = 686 GB).


---

## 🛑 CORRECTION (same day) — I was wrong about the canonical route, and it was the important half

The entry above says `binding_canonical` is H_3 too and that on the canonical
route "the tower is never built". **False.** Its DEFAULT path
(`use_transfer=True`) is the fine-Bratteli transfer matrix and sums the Frobenius
pairing over EVERY partition of `3A`. Measured, not read:

| nucleus | `n = 3A` | `n_partitions` | `p(3A)` |
|---|---|---|---|
| 2H  | 6  | **11** | 11 |
| 3He | 9  | **30** | 30 |
| 4He | 12 | **77** | 77 |

Exact at every level. **The canonical binding path is full-tower in `n`** and
already satisfies that half of the 2026-09-03 ruling.

**The trap, because it is reusable.** I cited `binding_canonical.py:37`, `:324`
("the H_3 building blocks tr_M^3(p), tr_M^3(n)") and `:341` (Wenzl bridge at
H_3). Those lines exist — but **:324 and :341 are inside the
`use_closed_form=True` branch**, a non-default alternative kept for one caller
family. Three grep hits naming H_3, and I inferred the default from them without
checking which branch they sat in. **A grep hit inside a branch that does not run
is not evidence about the path that does.**

### What survives, and it is sharper than what I claimed

- `build_atom_nf_mp` really does collapse to 6 components at every A — measured
  here at hydrogen, 4He and **16O** (nominal `H_48` carried as six numbers).
- The 2026-09-03 ruling has still been applied to **neither** route in any doc.
- But the two routes are **different objects**: canonical = full tower in `n`;
  NF = no tower at all. So the live question is not "does the mass surface
  honour the ruling" — it is **do the two routes agree**, and any probe that
  reasons from `build_atom_nf_mp` to a claim about *the framework's* binding is
  reasoning about the wrong object.


## The agreement test: RAN, and it is NOT yet interpretable — the two routes trace DIFFERENT WORDS

Compared the NF route's Markov trace (`Σ_i nf[i]·TR_M[i]`, with
`TR_M = [1, z, z, z², z², h·z²+z]` from `compound_shift_nf.tr_m_weights_mp`)
against the canonical `tr_M_atom` (`Σ_{λ⊢3A} y_λ χ^λ`, all `p(3A)` partitions).
mpmath end to end at 50 dps, proton pin both sides:

| nucleus | A | NF trace (6-dim) | canonical tr_M_atom | rel diff |
|---|---|---|---|---|
| 1H  | 1 | 1.14633769063500507 | 1.14575969245730087 | **5.0e-4** |
| 2H  | 2 | 0.404361815683575801 | 0.575172243917771871 | 0.297 |
| 3He | 3 | 0.687073324770033545 | 0.40376703685142817 | 0.702 |
| 3H  | 3 | 0.853070865421924793 | 0.229310102104556507 | 2.72 |
| 4He | 4 | 1.58467953221993593 | 0.160974145442407382 | **8.84** |

**🛑 Do NOT read this as "the H_3 reduction is unfaithful".** Checked before
believing it, and the comparison is not apples-to-apples: `tr_m_atom_zn`'s
docstring says **"Canonical color-weighted p-n convention"**, and
`compound_shift_nf.py` contains **zero** references to `m_pp` / `m_pn` / `m_nn`
or colour at all. The two routes therefore build different words, and colour
weighting enters exactly on the **interfaces**, which exist only for `A >= 2`
and grow as `O(A²)` — which is also the shape of the divergence. So the growth
with A is consistent with the convention difference alone and is not evidence
about the tower.

This is the same trap `qou-82mc` records against itself ("I nearly compared the
corpus mu3/mu4 signs against Ursell b3/b4 as if they were the same family").

### The one convention-independent number, and it is the interesting one

**At A=1 there are no interfaces**, so colour weighting cannot apply and both
sides trace the same 3-strand word in the same algebra — `n = 3`, so `H_{3A}` IS
`H_3` and the "collapse" is not a collapse. They should agree to the arithmetic,
~1e-50. They differ by **5.0e-4**, about 46 orders above the floor.

That residual is small, real, and unexplained. It is the cheap, well-posed
question this comparison actually produced, and it is worth more than the big
numbers beside it.

### What the test needs before it can answer the original question

Run the NF route with the canonical colour convention (or the canonical with
colour off, `m_pp=m_pn=m_nn` neutralised in whatever sense makes the words
identical), so that the only difference left is the H_3 reduction. Until then
the A>=2 rows measure the convention, not the tower.
