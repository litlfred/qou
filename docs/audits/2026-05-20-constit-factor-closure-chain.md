# 2026-05-20 — Constit-factor closure chain (Phase 5k.2 + 5l + 5l.1)

Companion audit to PR #854 documenting the supplementary witnesses
that do not wire into a single content block but support the
combined constit-factor closure chain.

## Witnesses covered

| Witness | Phase | Role |
|---|---|---|
| `constit-factor-varying-q-phase5k2.witness.json` | 5k.2 | Falsification probe: $(2q - 1)$ form holds at $q_0$ to 0.033 % but diverges 28-33 % away. Bridge to identifying the actual closed form. |
| `tau-M-proton-closed-form-phase5l1.witness.json` | 5l.1 | Symbolic-probe: explicit $\chi_\lambda(\mathcal{B}_p, q)$ closed forms for $\lambda \vdash 3$. Combined with Wenzl-bridge $y_\lambda(q)$ gives a Laurent expression for $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ modulo normalization (Phase 5l.2 queued). |

## Primary content block

[`prop:constit-factor-tau-M-proton-identity`](../../content/quantum-observable-universe/braids-and-knots/constit-factor-tau-M-proton-identity.md)
— the rigorous structural identity $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$,
wired to `rho-constit-equals-tau-M-proton-phase5l.witness.json` via
the proposition's `computation` field.

## Why audit-only

The 5k.2 and 5l.1 witnesses are **supporting witnesses** for the
chain, not the primary computational backing of any single content
block:

- **5k.2** is a falsification audit of `conj:constit-factor-2q-minus-1`
  (the historical conjecture). The conjecture's primary computation
  is the original Phase 5g categorical search (`constit_factor_and_volhyp_test.py`,
  pre-existing wiring). 5k.2 is supplementary historical context.

- **5l.1** is a probe-style symbolic exploration. The y_λ normalization
  between symbolic and numeric Wenzl bridge implementations doesn't
  match yet (queued as Phase 5l.2). The probe's χ_λ closed forms are
  clean (Laurent rationals) but the combined tr_M expression has a
  normalization gap that needs Phase 5l.2 reconciliation before
  promoting to a `prop:` block.

Both are tracked here so the witness-wiring audit doesn't flag them
as orphan claims.

## Reference

- PR #854: combined Phase 5l + 5l.1 (this audit doc lives in #854)
- PR #853: Phase 5n notation refactor (provides $\mathcal{B}_K, \mathrm{tr}_M, \mathfrak{E}, \bowtie_K$, etc.)
- PR #819: source of `prop:interface-knot-markov-z` (companion proposition)
- PR #831 (merged): Phase 5g categorical search (the original $(2q - 1)$ conjecture)
