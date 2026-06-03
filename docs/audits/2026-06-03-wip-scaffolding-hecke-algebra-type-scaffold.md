# WIP scaffolding — Iwahori–Hecke algebra type scaffold (open R&D item 2)

> **Provenance.** Primary content of the former content block
> [`rem:hecke-algebra-type-scaffold`](../../content/quantum-observable-universe/mass-endomorphism/hecke-algebra-type-scaffold.md),
> moved here in PR #1767 per the
> `canonical-no-negative-result-in-paper` discipline criterion
> (PR #1766 refinement: `["scaffolding", "open-rd-item-*"]` tag
> pair → audit-class content). The chapter block is retained as a
> forward-reference; the Lean class scaffolding stays in place at
> [`mass-endomorphism/hecke-algebra-type-scaffold.lean`](../../content/quantum-observable-universe/mass-endomorphism/hecke-algebra-type-scaffold.lean).

The full Mathlib lift of $H_n(R, q)$ as a unital associative algebra
with generators $\sigma_0, \ldots, \sigma_{n-2}$ modulo the three
defining relations (R1: quadratic, R2: far commute, R3: braid cubic) is
the **substantive R&D content for item 2** of the post-PR-#665 open
R&D inventory. This audit records the **Lean scaffolding** — abstract
generator types, formal-word lists, and class hypotheses for the
defining relations and Wedderburn decomposition.

## Types (Lean classes)

| Lean object | Role |
|---|---|
| `HeckeGen n` | Abstract generator $\sigma_i$ with index $i \in \mathrm{Fin}(n-1)$ |
| `HeckeWord n` | $\mathrm{List}\ (\mathrm{HeckeGen}\ n \times \mathrm{Bool})$ — formal words with signs |
| `HeckeRelations n q` | Class encoding R1, R2, R3 as scalar residuals (explicit-residual pattern) |
| `HeckeWedderburn n q` | Class encoding the Plancherel completeness $\sum_\lambda y_\lambda = 1$ |

## Why scaffold rather than full type

The full $H_n(R, q)$ type needs:

1. A free $R$-module on $B_n$ (Mathlib-able)
2. A multiplication structure (concatenation in $B_n$)
3. Quotient by the three relations (substantive — Mathlib lift)
4. Per-block Wedderburn decomposition (q-deformed Schur–Weyl)

Steps 1–2 are Mathlib-routine; step 3 requires careful quotient
construction; step 4 is genuinely substantive ($n \to \infty$
inductive-limit infra plus Murphy's seminormal form).

Until that infrastructure lands, the **class scaffolds** here provide
downstream hooks: any theorem requiring $H_n(q)$ properties takes
`[HeckeRelations n q]` and `[HeckeWedderburn n q]` as hypotheses, and
the per-$n$ discharges plug in when ready.

## Per-$n$ discharge status

| $n$ | Status | Discharge source |
|---:|---|---|
| 2 | trivial (cyclic) | `Braid2 := ℤ` in `rem:braid-link-types` |
| 3 | partial | `hoefsmit-V21-cos-symmetrization.lean` covers Hecke quadratic (proved) + YB cubic (anomaly: requires $d_1 \leftrightarrow d_2$ swap per `rem:post-pr665-open-rd-inventory`) |
| 6, 12 | open | needed for di-baryon ($B_6$) and α-particle ($B_{12}$) physics |

## Status

**Scaffolding-tier Lean infrastructure.** No `sorry`s introduced (all
class fields use the explicit-residual pattern from a prior review
batch); per-$n$ instances remain follow-up.

## See also

- [`rem:post-pr665-open-rd-inventory`](../../content/quantum-observable-universe/mass-endomorphism/post-pr665-open-rd-inventory.md) — parent R&D inventory; item 2 is this type scaffold
- [`markov-trace-operator-construction` audit](2026-06-03-wip-scaffolding-markov-trace-operator-construction.md) — item 4 (Markov trace operator construction) companion
- [`hecke-algebra-type-scaffold.lean`](../../content/quantum-observable-universe/mass-endomorphism/hecke-algebra-type-scaffold.lean) — Lean class scaffolding (stays in place; imported by downstream Lean files)
- Murphy 1981, Wenzl 1988 — seminormal form + Plancherel completeness
