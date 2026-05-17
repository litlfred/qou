**Iwahori-Hecke algebra $H_n(R, q)$ type scaffold (Item 2 of `rem:post-pr665-open-rd-inventory`).**

The full Mathlib lift of $H_n(R, q)$ as a unital associative algebra
with generators $\sigma_0, \ldots, \sigma_{n-2}$ modulo the three
defining relations (R1: quadratic, R2: far commute, R3: braid cubic)
is the substantive R&D content for item 2. This block provides the
**Lean scaffolding** — abstract generator types, formal-word lists,
and class hypotheses for the defining relations and Wedderburn
decomposition.

## Types

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
4. Per-block Wedderburn decomposition (q-deformed Schur-Weyl)

Steps 1-2 are Mathlib-routine; step 3 requires careful quotient
construction; step 4 is genuinely substantive ($n \to \infty$
inductive-limit infra plus Murphy's seminormal form).

Until that infrastructure lands, the **class scaffolds** here
provide downstream hooks: any theorem requiring $H_n(q)$ properties
takes `[HeckeRelations n q]` and `[HeckeWedderburn n q]` as
hypotheses, and the per-n discharges plug in when ready.

## Per-$n$ discharge status

| $n$ | Status | Discharge source |
|---:|---|---|
| 2 | trivial (cyclic) | `Braid2 := ℤ` in `rem:braid-link-types` |
| 3 | partial | `hoefsmit-V21-cos-symmetrization.lean` covers Hecke quadratic (proved) + YB cubic (anomaly: requires d_1↔d_2 swap per `rem:post-pr665-open-rd-inventory`) |
| 6, 12 | open | needed for di-baryon (B_6) and α-particle (B_12) physics |

## Status

**Scaffolding-tier Lean infrastructure.** No `sorry`s introduced
(all class fields use the explicit-residual pattern from
PR #665's Gemini batch); per-$n$ instances remain follow-up.
