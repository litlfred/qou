---
# qou-cds2
title: 'S2 (SCIENCE): pyhecke.gram.z and the Gram singularity — the ruling answers the convention, not the singularity'
status: todo
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-15T00:00:00Z
---

Parent: `qou-cdx1`. Predecessor: `qou-wgta` item 11. **Highest-risk item in the
plan.** Blocks `qou-cdh2`.

## The state the ruling inherits

`trace-convention-registry.json → blocked_migrations[0]` was the registry's only
`owner_decision_required: true`:

> `tools/pyhecke/python/pyhecke/gram.py::z` **stays C**, because
> `G_INV = np.linalg.inv(G)` runs at **module import**, and under D the
> Markov–Gram form on the `H₃(q)` NF basis is **SINGULAR** — exactly one null
> direction (the row-cap one).

Measured at the proton pin: bilinear eigenvalues
`−0.752702, 0, +0.752702 ×3, +4.230339`; `det 3.998e-17`; `cond 4.9e16`.
**numpy raises nothing** — it returns entries up to `7.6e15` with
`‖G·G_INV − I‖ = 1.64`. Switching that one line silently corrupts every consumer
of `G_INV`.

**The 2026-08-15 ruling removes the convention question. It does not remove the
singularity.** That is the whole content of this bean.

## Corank accounting

`n=3` corank 1; `n=4` corank 10 (`3²+1²`); `n=5` corank 78 (`6²+5²+4²+1²`).

## The named repair

Quotient by the radical — `QOU/QBeta/GramSignature.lean`. Post-retraction the
quotient is a genuine **positive-definite** inner product, so the repair is more
attractive than it first looked. The supporting Lean already exists in
`QOU/QBeta/MarkovGramDegenerate.lean`:

1. `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the pin forces `y_(1³) = 0`
2. `block_mem_radical` — a zero-weight block lies in the trace radical
3. `gram_det_eq_zero_of_radical_combination` — hence `det G = 0`
4. `TemperleyLiebTower.traceRadical_two_sided` — the quotient is a ring
5. `pairing_descends` — the pairing is constant on radical cosets
6. `mem_radical_of_pairing_zero` — and is non-degenerate on the quotient

## Signature caveat — quote only the post-retraction statement

Quote `QOU.QBeta.GramSignature` **only after** its in-file retraction (commit
`748ba9b1`). The original *"(5,1) under C, (4,1)+null under D, LORENTZIAN"* used
the **bilinear** pairing and is **WITHDRAWN**. The Hecke `*`-structure is
`T_w* = T_{w⁻¹}`, giving C `(6,0,0)` positive definite and D `(5,0,1)` positive
semidefinite. The **singularity** under D is common to both pairings and is the
only thing the dependent blocks rely on.

## Blast radius

`G_INV` is **exported at import**, so every consumer of `pyhecke.gram` is
affected — that is the 13 re-exporters + 13 consumers of `qou-cdh2`, plus
whatever imports `gram` directly.
