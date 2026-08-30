---
# qou-rwhv
title: Is the corpus b3 an Ursell function? The alternating-sign theorem says the sign obstruction is the positivity hypothesis
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:39:42Z
updated_at: 2026-08-30T09:40:16Z
---

## Where this came from

The owner uploaded six cluster-expansion PDFs on 2026-08-30 (commit `a12f83c4cd`)
after being asked whether the b3 question needed literature. Ingested by PR #6152.

## The finding

`library/s10955-022-02992-6/` (Jansen & Kolesnikov, *Cluster Expansions:
Necessary and Sufficient Convergence Conditions*, J. Stat. Phys. 189:33, 2022)
carries in §3.1 the classical **alternating-sign property of the Ursell
functions**, `phi^T_n = (-1)^n |phi^T_n|`, valid for a **non-negative (purely
repulsive) pair potential** — two independent proofs of the multi-rooted
generalisation. At n = 3 that is `phi^T_3 <= 0`.

`QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos` reaches the same conclusion from
a different argument (`b3 <= 3*fpn - 2` from `P3 >= 0`, with the framework's
`fpn = z_D = 0.6126880` against the 2/3 threshold).

## The question — and it is genuinely open

**Is the corpus's b3 an Ursell function in the theorem's sense?** They are NOT
the same theorem: the classical object is the third Ursell function of a
grand-canonical activity expansion of a genuine pair potential, the corpus's is
an inclusion-exclusion cumulant of a binding functional; the hypotheses are
`U >= 0` pointwise on the potential vs `P3 >= 0` on a product of bond factors.

- **If yes** — the obstruction is far broader than the `1 - prod f` assembly. No
  change of assembly escapes it; `PairwiseCumulantVanishing` and
  `MayerThreeBodySign` become two shadows of one classical fact, and only the
  hypothesis is left.
- **If no** — `MayerThreeBodySign`'s Mayer/Ursell vocabulary outruns its content
  and should be scoped.

## Why the hypothesis is the interesting half either way

The escape is named in the same 47 pages: the paper's own result is a convergence
condition for **possibly negative** pair potentials, iff in the non-negative case.
That is the class `b3 > 0` needs.

## What would settle it

Exhibit the polymer / cluster model whose activity expansion has the corpus's b3
as its third Ursell coefficient — name the polymer set, the weight, and the
compatibility relation. Then the classical theorem applies, or provably does not.
`rebenko2022virial` is the relevant setting note: it works the **canonical**
(fixed particle number) ensemble, which is what matches a nucleus, where the
grand-canonical activity expansion does not.

## Flagged, not asserted

Under a Boltzmann reading `f = e^{-beta U}`, `f < 1 <=> repulsive`, and all three
corpus bond factors lie in (0,1); an attractive channel would be a bond factor
> 1, of which there is none. But the corpus's f are Markov factors built from z,
and **nothing in the corpus identifies them with an exponentiated potential**.
That identification is the concrete next measurement.

## Scope

Scope-(a). A literature identification and a question. No derivation, no
refutation, no magnitude — the 6-14x gap on `b3_sym` (qou-9v7t) is untouched.

Audit: `docs/audits/2026-08-30-ursell-alternating-sign-and-the-b3-obstruction.md`
Parent question: `qou-brng` (the linking-vs-self-energy amplitude assignment).
