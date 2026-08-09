---
# qou-dq4k
title: 'GAP: is the Q_β ladder-in-u literally an Ohtsuki expansion-in-(q−1)? (gates the formal-Habiro exclusion)'
status: todo
type: task
priority: normal
tags:
    - qbeta
    - habiro
    - registry
created_at: 2026-08-09T02:30:00Z
updated_at: 2026-08-09T02:30:00Z
---

Salvaged from closed PR #4140 (its closing note claimed "no unique content
remains" — inaccurate; see `docs/audits/2026-08-09-stalled-pr-dispensation-4371-4373-4140.md`).

`QOU.Mass.QbetaC3Habiro` (landed sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`) proves the growth dichotomy
`geometric_not_superGeometric` outright, and derives `False` from the
conjunction of two §3b-cond class hypotheses:

- `QbetaLadderGeometric c` — KC8: the ladder `g(u) = Σ c_k u^k` has a simple
  pole at `u_substrate`, so geometric growth (rate ≈ 117.409).
- `FormalHabiroQOneExpansion c` — literature: a formal Habiro-ring element's
  `q=1` (Ohtsuki) expansion is Gevrey-1, hence super-geometric.

**The open step.** Both premises are asserted of the *same* indexed sequence
`c`. But `c_k` are coefficients in `u = b·ℏ_q²`, while the Ohtsuki expansion is
in `(q−1)`. If the ladder-in-`u` is a *re-expansion* of an Ohtsuki
series-in-`(q−1)` rather than literally the same sequence, the growth classes
need not transfer and the exclusion does not bite. Nothing in the corpus
establishes the identification either way.

**Why it matters (decision-relevant).** `docs/coordination/ck-dk-canonical-registry.md`
§9 currently reads the Habiro framing as *correct but unconstructed* (line ~33)
and lists the element `F(q)` as an **OPEN keystone** (line ~75). If the
identification holds, that keystone is closed negatively and any agent
dispatched to "construct `F(q)` whose Ohtsuki coefficients are the `c_k`" is
chasing something impossible given KC8 — wasted effort of exactly the kind the
corpus-grep discipline exists to prevent. If it fails, the keystone stays open
and the Lean is a constraint on the combination only.

**Next honest step.** Settle whether the ladder variable `u` and the Ohtsuki
variable `(q−1)` index one sequence. Then either (a) add a registry row
recording the negative closure and re-scope lines 33/75, or (b) record the
non-transfer and leave the keystone open. Do **not** cite
`qbeta_ck_not_formal_habiro` as "the Q_β Habiro element is refuted" until this
is settled — that is the `conditional-proved ≠ premise-established` failure
mode.
