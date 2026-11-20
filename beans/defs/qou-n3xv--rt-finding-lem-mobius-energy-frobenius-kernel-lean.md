---
# qou-n3xv
title: 'RT finding: lem:mobius-energy-frobenius-kernel — Lean is a composition of two class fields; narrative restates the claim; qou-15oa was completed on a projection'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B04).

- Lean: `folio/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean`. The proof is `rw [← ctx.killing_eq_inverse_square …]; exact ctx.kernel_tendsto_killing …`, which composes two fields of `MobiusFrobeniusKernelContext`. The only instance in the file is degenerate (K constant in q). RT-1A and RT-2B both flagged it as assumption-carries-conclusion.
- The narrative proof asserts the q → 1 limit and derives nothing. In particular it never derives a distance kernel 1/r² from the Killing form, which is distance-independent.
- Bean qou-15oa ("PROVE(lean): mobius_frobenius_kernel") is `completed` on this projection. The completion over-states what was proved.
- Related: vta3 (derive explicit K_FH), qou-kkja. Class-field debt is W10 scope (qou-c8p8).
