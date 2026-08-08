---
# qou-ql2a
title: Migrate the remaining 68 C-form z sites after the convention-D ruling — per-file channel call, not a sweep
status: todo
type: task
created_at: 2026-08-08T23:52:19Z
updated_at: 2026-08-08T23:52:19Z
---


Follows the 2026-08-08 owner ruling adopting **convention D** for the Markov
stabilisation parameter (PR #4834, audit
[`2026-08-08-markov-z-convention-d-ruling.md`](../docs/audits/2026-08-08-markov-z-convention-d-ruling.md)).

That PR changed the three **definitional pins** (`markov-axioms-primitive`,
`jones-markov-trace`, the notation register). 68 further files still carry
`z = 1/(q^{1/2}+q^{-1/2})`.

**This is not a find-and-replace.** The C form appears in three distinct
roles, and flipping role 1 would change binding numbers:

1. **Genuinely C-specific, load-bearing on binding — MUST STAY C.**
   `y-lambda-closed-form-wenzl-bridge*`, `centered-hecke-variance-positive*`
   (its statement *is* the Wenzl positivity regime `q^{1/2}+q^{-1/2} > 2`),
   `h3-markov-wenzl-weights*`.
2. **Mass-channel definitional — should follow the pin to D.**
   e.g. `markov-trace-factorization`, `markov-trace-frobenius-selection`,
   `mass-endomorphism-tower`.
3. **Convention-neutral — wants a label, not a changed formula.** Blocks
   using `z` symbolically that merely illustrate it with the C form.

For role 3 the registry's own rule applies — *"convention-silent trace values
are not comparable"* — so the correct output is an explicit convention label.

By chapter: `mass-theory` 26, `lean/QOU` 21, `mass-endomorphism` 7,
`braids-and-knots` 4, `appendix-transfer-matrices` 4, `observations` 3,
`stochastic-mechanics` 1, `predicted-spectra` 1, `content/values/registry.ts` 1.

Regenerate the live list with:

```bash
grep -rln 'z = 1/(q^{1/2}\|z = \\frac{1}{q^{1/2}\|z := 1/(q^{1/2}\|z = 1 / (q^{1/2}\|z(q) = \\dfrac{1}{q^{1/2}\|z(q) = 1/(q^{1/2}\|z = 1/(\\check{q}' \
  --include=*.md --include=*.lean --include=*.ts content/
```

**Gate.** Every batch runs
`docs/coordination/trace_convention_registry_validate.py --selftest --lint-docs`
(baseline: PASS, 0 errors, 21 warnings) and states which channel each touched
file was assigned to. Do not let the warning count rise.

Compute-side twin: the 21 open R5 warnings — Borromean tracers under
`computations/` that declare no convention.
