---
# z3a2
title: 'Compute infra: factor shared Young-diagram/dim_q/S(m) machinery into reusable cached module'
status: todo
type: task
priority: normal
created_at: 2026-06-28T06:54:32Z
updated_at: 2026-09-13T12:08:45Z
---


**Progress 2026-06-28:** young_qdim shared module merged (#2952). Migrated 3/7 probes to import from it, verified equivalent (lever1_binding_habiro_qexponential re-run → byte-identical L_m; lever1_qholonomic_kernel_fit + lever1_qholonomic_order3_fit use only q+S, proven-identical via S(3)=(q+1)²/q). Remaining 4 have per-probe quirks (lever1_qinvolution_kernel_test: qint_asym; binding_qaskey_product_probe: qpoch; wlambda_identity_i_structure_probe: classical f_lambda; lever1_lw_depth2: pre-existing) — partial migration (symmetric machinery only), follow-on.



**2026-06-28:** lever1_lw_depth2 migrated (lw via S). 4/7 probes now migrated; remaining 3 (qinvolution qint_asym, qaskey qpoch, wlambda f_lambda) are symmetric-only partials — follow-on.

**2026-06-28 (cont.):** lever1_qinvolution_kernel_test migrated — symmetric machinery (qint/qfact/dim_q/partitions/S) now imported from young_qdim; the probe-specific qint_asym (Gaussian) kept local. Verified: probe re-run → witness BYTE-IDENTICAL (stored values are q0 numeric evals + sp.factor canonical strings, form-independent). Source −35 lines (10 ins / 45 del). **5/7 migrated**; remaining 2 symmetric-only partials: binding_qaskey_product_probe (qpoch), wlambda_identity_i_structure_probe (classical f_lambda).

**2026-06-28 (cont.):** binding_qaskey_product_probe migrated — qint/qfact/dim_q/partitions/S from young_qdim; qpoch (q-Pochhammer) kept local. Witness BYTE-IDENTICAL (stores booleans + sp.factor strings). Source −35 lines. **6/7 migrated**; remaining 1: wlambda_identity_i_structure_probe (entangles classical f_lambda with partitions/hook — needs care, follow-on).

**2026-06-28 (cont.) — 7/7 COMPLETE.** wlambda_identity_i_structure_probe migrated (conservative): the q-side (qint/qfact/dim_q) now from young_qdim; the classical SYT/hook combinatorics (f_lambda, conj, cells, arm, leg, hook, content + list-form partitions) kept LOCAL because (a) their hook/leg arg order differs from young_qdim and (b) the W_λ witness keys embed list-form partitions. dim_q called as dim_q(tuple(lam)). Witness BYTE-IDENTICAL; source −22 lines. **All 7 z3a2 probes now import the shared young_qdim module** (lever1_binding_habiro_qexponential, lever1_qholonomic_kernel_fit, lever1_qholonomic_order3_fit, lever1_lw_depth2, lever1_qinvolution_kernel_test, binding_qaskey_product_probe, wlambda_identity_i_structure_probe). Bean ready to close (human-only §4a).


---

## Measured 2026-09-13 (found while reading `qou-qrsp`'s largest re-padder)

`grep "^\s*def dim_q("` over the tracked corpus, excluding `_deprecated`:

- **36** functions named exactly `dim_q`
- in **23 distinct signatures**
- **60** including the variants (`dim_q_sym`, `dim_q_numeric`, `dim_q_at_q0`,
  `dim_q_V_lambda`, `dim_q_partition`, `dim_q_num`, `dim_q_hook_content`, …)

The signature spread is the part worth acting on, more than the count:

```
6   def dim_q(lam)
3   def dim_q(shape, n)
3   def dim_q(p, q)
3   def dim_q(lam, q)          <-- partition first
3   def dim_q(lam, n)
2   def dim_q(q, lam)          <-- q first.  SAME NAME, ARGUMENTS REVERSED.
2   def dim_q(shape, q=None)
2   def dim_q(shape, q, n_fac_q)
...23 in total
```

**`dim_q(lam, q)` and `dim_q(q, lam)` both exist.** One mathematical object,
one name, two opposite calling conventions. Nothing checks which one a file
means; an author moving code between producers has a one-in-two chance of
silent nonsense, and only the type mismatch (tuple vs mpf) is likely to save
them.

**The centralisation this bean proposes was already attempted and did not
take.** `hecke_characters.specht_dim`'s docstring records it: *"Centralised
here (next to `young_hooks` / `dim_q`, reusing the single `young_hooks`
implementation) so binding / observe-last consumers share one hook-length
routine instead of re-deriving it (Gemini review, PR #2408)."* There are 36
copies. Whatever is done here has to account for why that one didn't stick —
most likely that the library signature (`dim_q(shape, q=None)`) does not serve
callers who already hold `n_fac_q` and do not want it recomputed per partition.

**Precision is the live risk, not just duplication.** Each copy is an
independent decision about whether the q-integers are exact. Spot-checked
`chirality_avg_content_atomic.py:77` (`def dim_q(shape, q, n_fac_q)`): exact —
`mpf(1)`, `q_int(hook, q)` products, one division, no float. That is the good
case, and nothing in the repo asserts it stays that way; the NO-FLOAT64 gates
audit witnesses and module-level constants, not 36 copies of one formula.

Cross-ref: `qou-6p3b` ("qfac/dim_q threading: 12 decisions, not 133 edits")
scopes the threading question, and `qou-uk8o` sweeps the 23 producers still
weighting by `dim_q^2/[n]_q!`. This note is the census the three share.
