---
# qou-lw3v
title: Formalise rem:eigenbasis-structural-lemmas items 1-3 in Lean (parity, conjugation duality, framing rational)
status: todo
type: task
created_at: 2026-08-09T00:06:19Z
updated_at: 2026-08-09T00:06:19Z
---


Opened 2026-08-08 (PR #4834) while supplying the agent-judgement sidecar
verdicts for this block under `qou-w2d7`.

**Finding.** The block's title ended `"(Lean)"`, but nothing formalises its
three items. It has no `.lean` sibling and no `lean.ref`, and
`QOU.BraidKnot.CrossingEnergyBarParity` — the nearest Lean from the same PR
(#4826) — is about the crossing-energy Laurent scalar `E_cross` / `eSym` /
`eAsym`, not about characters. The title was corrected rather than left
advertising a formalisation that does not exist.

**To formalise** (all three currently rest on symbolic probes only):

1. **Parity** — `chi_lambda(beta)(-q) = (-1)^L chi_lambda(beta)(q)` for a
   braid word of length `L`.
2. **Conjugation duality** — `sigma_i -> -sigma_i^{-1}` is an algebra
   automorphism of `H_n(q)` swapping the seminormal eigenvalues
   `q <-> -q^{-1}`, giving `chi_lambda(-1/q) = chi_{lambda'}(q)`; the signed
   form is then a corollary of item 1, not an independent input.
   The automorphism half is a short algebraic check: with `s^2 = h s + 1`,
   `(-s^{-1})^2 = h(-s^{-1}) + 1` — the same identity as
   `QOU.BraidKnot.hecke_inv_eq_sub`, which is already proved and reusable.
3. **Framing rational** — framing by `m` full twists scales `chi_lambda` by
   `theta_lambda^m`, so the tower is `chi_lambda(beta)/(1 - t theta_lambda)`
   with its sole pole at `t = q^{-2c(lambda)}`.

Backing witness (symbolic, 132 braid words on `H_2`/`H_3`, no substrate pin):
`computations/hecke-conjugation-duality-sign.witness.json`.

`c(lambda)` is the content sum `Sum (j - i)` —
`QOU.MathlibExt.Partition.contentSum`, now named in the block prose.
