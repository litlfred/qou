---
# qou-8p1b
title: 'qou-8pl1/b: find an invariant separating Klein from the other S_4-admitting genus-3 curves'
status: todo
type: task
created_at: 2026-08-07T00:00:00Z
updated_at: 2026-08-07T09:20:00Z
---

Parent: `qou-8pl1`. Depends on `qou-8p1a` (know the competitor set first).

## The gap

The chapter's colour route needs the normalization of the pinched Bring surface
to BE the Klein quartic. Two arguments have now failed:

1. The Hurwitz-bound argument (withdrawn): an upper bound is not a selection
   principle, and the generic genus-3 curve has small Aut.
2. The S_4 bridge (refuted, `s4_genus3_competitor_fermat.py`): S_4 embeds in the
   automorphism group of at least two distinct genus-3 curves.

So a **separating invariant** is required — something the pinch determines that
differs between Klein and every competitor.

## Candidate separators, cheapest first

* **Full automorphism group order.** Klein 168 vs Fermat 96. If the pinch
  determines |Aut| of the normalization, this alone separates them. Requires
  computing what the pinch actually preserves beyond S_4 — is there more
  symmetry that survives?
* **The 2-torsion / theta characteristics.** Genus-3 curves are separated by
  their 28 bitangents and the associated theta structure; Klein and Fermat have
  different bitangent configurations under their automorphism groups.
* **Weierstrass points / gap sequences.** Cheap and discrete.
* **The quotient genus data.** For each subgroup of Aut, the genus of the
  quotient — a discrete signature that differs between the two.
* **Period matrix.** Decisive but needs the heavy stack — see `qou-8p1c`.

## Constraint from the pinch side

Whatever separator is chosen, it must be **computable from the degeneration
data**, not just from the two candidate curves. Knowing that Klein and Fermat
differ in bitangent structure is useless unless the pinched Bring surface
determines its normalization's bitangent structure. State that link explicitly
before investing in any separator.


---

## RE-SCOPE (2026-08-07, from `qou-8p1a`) — the task has changed

`qou-8p1a` closed: the S_4-admitting genus-3 curves are an infinite **pencil**
`C_t : x^4+y^4+z^4 + t(x^2y^2+y^2z^2+z^2x^2)`, smooth for all `t` outside
`{2,-2,-1}`, Fermat being `t = 0`.  (`t`, not `lambda` — `lambda` is the
partition symbol in that chapter.)

**This bean as written is void.**  "Find an invariant separating Klein from
Fermat" is trivially satisfiable — `|Aut|` alone does it, 168 against 96 — and
settles nothing: it says nothing about the rest of the pencil, and nothing
whatever about which member the pinch produces.  Any invariant computed from a
shortlist of candidate targets has this defect.

## The correct task: an invariant the DEGENERATION determines

Read the invariant off the pinch data — the cycle being pinched and the nodal
curve — not off candidate answers.

## A sharpening that may do most of the work

The chain in the chapter is written

    Bring Sigma_4 (genus 4)  --pinch-->  nodal, geometric genus 3  --normalize-->  Sigma_3

and then asks "is `Sigma_3` the Klein quartic?".  But pinching **one
non-separating** cycle on a genus-4 curve yields a one-node curve of arithmetic
genus 4 whose normalization has genus 3 **with two marked points** — the two
preimages of the node (arithmetic genus `3 + 1 = 4`, consistent).  So the object
the degeneration actually produces is not a bare genus-3 curve but a

    genus-3 curve together with an S_4-stable unordered pair of points  (Sigma_3, {p,q}).

That is strictly more data, hence strictly more rigid, and it is determined by
the degeneration rather than chosen after the fact.

**Concrete probe (unverified — this is the proposal, not a result):** compute
the S_4-orbit structure on the pencil members and ask which `C_t` admit an
S_4-stable pair of points at all.  If that condition cuts the pencil down to a
finite set — ideally to Klein — it is exactly the separator this bean was
looking for, and it comes from the right side of the problem.  If it does not
cut it down, that is also informative: it says the marked points carry no
selecting power either, and the pinch must be pinned by the cycle class itself.

## Then, and only then

Only after the target class is genuinely narrowed does a period-matrix
computation (`qou-8p1c`) become the decisive step rather than an expensive way
to compare two curves nobody has shown are the candidates.

## Prerequisite for the probe

Classify the S_4-invariant 1-cycles on the Bring surface up to the S_5 action
(`H_1(Sigma_4, Z)` has rank 8, `S_5` acts).  Different invariant cycles may
pinch to different members — in which case the chain as written is
under-determined and needs to say WHICH cycle.
