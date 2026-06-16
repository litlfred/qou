# Ingredient-4 geometric existence — a Schur-Weyl constraint forces the 5-strand fibre (colour ℂ³, not spin ℂ²)

**Date:** 2026-06-16
**Branch:** `claude/s5so3-reeb-geometric-existence-2026-06-16`
**Status:** verified constraint on the open geometric leg of `conj:s5-so3-fiber-action`
**Discipline:** formalize-first (a representation-theoretic invariant narrows the geometric search before
any contact/spin-geometry construction).

## Context

The merged #2352/#2361 closed out the keystone's algebra: geometry settled (ingredients 1–3), the
commuting square's algebraic leg concrete, ingredient 5 (210 ppb muon) refuted, and the sole remaining
open object localized to the **geometric existence** of a $2I$-equivariant 5-strand Reeb realization whose
Markov trace is the (Ocneanu-consistency-forced) $H_5(q)$ trace. This note attacks that open object with a
formalize-first prune and finds a sharp constraint.

## The constraint (verified — `scripts/s5so3_ingredient4_fibre_schur_weyl.py`, exit 0)

Schur-Weyl duality for $\mathrm{gl}_d$ on a 5-strand tensor space:
$$
(\mathbb{C}^d)^{\otimes 5} \;=\; \bigoplus_{\substack{\lambda\,\vdash\,5\\ \mathrm{rows}(\lambda)\le d}}
S^\lambda \otimes W^{\mathrm{gl}_d}_\lambda ,
$$
so an $S_5$ irrep $\lambda$ appears on the 5-strand fibre **iff** $\mathrm{rows}(\lambda)\le d$.

| per-strand fibre | $\dim$ | $S_5$ blocks hosted | electron $(3,1,1)$? | muon $(3,2)$? |
|---|---|---|---|---|
| **spinor $\mathbb{C}^2$** (the $2I$ / SU(2) spin rep) | $2^5=32$ | $(5),(4,1),(3,2)$ only | **ABSENT** (3 rows > 2) | present |
| **colour $\mathbb{C}^3$** (SU(3) colour) | $3^5=243$ | $(5),(4,1),(3,2),(3,1,1),(2,2,1)$ | **present** | present |

(Dimension counts close: $1\!\cdot\!6+4\!\cdot\!4+5\!\cdot\!2=32$; $\sum=243$ for $d=3$.)

On the **spinor** $\mathbb{C}^2$ the Hecke algebra acts through its **Temperley–Lieb** quotient
($\mathfrak{sl}_2$ Schur-Weyl), which **annihilates every $\ge 3$-row partition** — in particular the
electron block $(3,1,1)$.

## What this forces for ingredient 4

1. **The 5-strand fibre cannot be the spinor ℂ².** If it were, the electron generation block $(3,1,1)$
   (verified bridge: electron $\ell{=}1\to T_1\subset(3,1,1)$) would not exist on the module — Temperley–Lieb
   kills it. Only the muon $(3,2)$ (2 rows) would survive. A spinor-strand realization hosts the muon but
   **not** the electron.
2. **The strands must carry a ≥3-dim fibre — colour ℂ³.** On $\mathbb{C}^3$ the electron $(3,1,1)$, muon
   $(3,2)$, and $(2,2,1)$ all survive (≤3 rows). This matches the corpus's **"3 colour tubes per nucleon"**
   (SU(3) colour): the strand fibre is colour, not spin.
3. **Two spaces must be kept distinct (catches a possible ingredient-1 conflation).** Ingredient 1 settled
   that the icosahedral rotation lifts to $2I\subset\mathrm{SU}(2)$ on a **ℂ²** — but that ℂ² is the
   **spin/state-bundle fibre over the divisor sphere** $\mathbb{CP}^1=\mathbb{P}(\mathbb{C}^2_{\mathrm{spin}})$,
   the *geometric arena*. It is **not** the per-strand module fibre, which must be colour ℂ³. Conflating
   "2I acts on ℂ²" with "the strands carry ℂ²" produces the false obstruction that the electron cannot exist.
   The geometric leg must thread **colour-ℂ³** strands over a **2I-symmetric divisor sphere**.

## Net for the open problem

The geometric-existence target is sharpened: a $2I$-equivariant Reeb realization on the Bring spin bundle whose
**strands carry colour ℂ³** (hosting the ≤3-row generation blocks incl. the electron) and whose **divisor-sphere
fibre carries the $2I$ spin lift**. The Schur-Weyl bound also explains why the generation tower stops being
"clean" beyond the ≤3-row blocks: $(2,1,1,1)$ and $(1^5)$ need $d\ge4,5$ — absent on a 3-colour fibre. This is a
genuine narrowing (it rules out the spinor-strand realization and pins the fibre to colour ℂ³), not a
construction; the geometric existence itself remains open, owner-gated, multi-session.

## Cross-references

- [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md) — the 5-ingredient program + ingredient-4 formalize-first prune
- [`2026-06-16-s5so3-branching-backbone-verified.md`](2026-06-16-s5so3-branching-backbone-verified.md) — verified backbone + bridge (electron $(3,1,1)$, muon $(3,2)$)
- `scripts/s5so3_ingredient4_fibre_schur_weyl.py` — this constraint (exit 0)
- `content/.../brings-surface/` — "3 colour tubes per nucleon" (colour ℂ³ strand fibre)
