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

## RE-SCOPE REQUIRED (2026-08-07, from `qou-8p1a`)

`qou-8p1a` closed: the S_4-admitting genus-3 curves are an **infinite pencil**,
not `{Klein, Fermat}`.  **This bean as written is therefore no longer
sufficient to settle `qou-8pl1`.**  An invariant that separates Klein from
Fermat says nothing about the rest of the family -- and worse, an invariant
computed only from two hand-picked curves does not constrain which member the
pinch produces.

Re-scope to: find an invariant **the pinch itself determines**.  The question
is no longer "what tells Klein and Fermat apart" (many things do -- `|Aut|`
alone, 168 vs 96) but "what does the Bring degeneration actually pin down about
the normalization".  Until that is posed, computing invariants is measuring the
wrong thing.
