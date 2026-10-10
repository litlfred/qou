---
# qou-orjl
title: The charge-type menu is a singleton too, but six of the seven coefficients are not hook products at all
status: completed
type: task
priority: normal
created_at: 2026-09-05T15:29:25Z
updated_at: 2026-09-05T15:36:48Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Tests whether
`qou-ld2a`'s selection principle generalises past the Wigner row. **It does. The
coefficients do not.**

## 1. The principle transfers — the charge class is a singleton

For a two-row shape `(a,b)`, `2.c(a,b) = a(a-1) + b(b-3)`. The second row never
drags that below `-2` (since `(b-1)(b-2) >= 0`) and `a >= 2` already contributes
`+2`, so `c < 0` forces `a <= 1`. **`(1,1)` at `n = 2` is the entire charge-type
class the row cap admits.** So under convention D:

| class | members | count |
|---|---|---:|
| `c < 0` charge | `{(1,1)}` | **1** |
| `c = 0` isospin | `{(1), (2,1), (2,2)}` | 3 |
| `c > 0` volume | everything else | infinite |

Two of the three classes are essentially singletons. "Charge-type at its level"
forces a partition exactly as "isospin-type at the quartet level" did.

## 2. But the singleton gives the wrong number

    m_e H_q((1,1)) = m_e [2]_q  = 1.0276 MeV   vs a_C ~ 0.711   +44.5 %
    corpus lambda_C = h [6]_q m_e = 0.68244 MeV  vs a_C ~ 0.711    -4.0 %

The corpus's Coulomb coefficient is a **different object** from what the block's
own form and its own selection rule produce.

## 3. And six of the seven coefficients are not hook products at all

`unified-iterative-correction-proof.md` states `C_lambda = m_e . H_q(lambda)` —
the q-hook product — as *"the universal constant determined by the partition
algebra"*, with no restriction to a family. Swept against **every partition with
n <= 14 (507 of them)**:

| row | form | hook product? |
|---|---|---|
| lambda_V | `2[2][7]` | no |
| lambda_S | `2[4]^2` | no |
| lambda_C | `h[6]` | no |
| a_asym | `3[2][7]` | no |
| delta_P | `[3][7]` | no |
| lambda_ex | `[3]/[2]` | no |
| **delta_S** | `[2]^2[3]` | **`(2,2)`** |

The six carry integer prefactors (2, 2, 3), a bare `h = q - 1/q`, or a quotient.
None can be a product of `[h]_q`: `2` is not a q-integer (nearest is
`[2]_q = 2.0109`), `h` is not a `[h]_q`, and no hook product is a quotient.

## 🛑 A GAP, NOT A REFUTATION

The same block's `(2,1) |- 3` clause says the volume / surface / Coulomb
coefficients arise *"through their image under the Wedderburn embedding"* — an
unspecified transformation that could in principle carry one `C_lambda` to
several table entries. So the universal form claim and the table cannot both be
read at face value, **but the bridge between them is unspecified rather than
contradicted.** Recorded as a gap; specifying that embedding is the successor.

## What it settles

`(2,2)` was **not** fortunate-but-typical. It is the one row that actually has
the shape the block claims for all seven — which sharpens
`mass-formula-regime-switching-table1-data`'s fit-shape QA note rather than
answering it. The remaining six cannot be rescued by a better partition choice,
because they are not of the form at all.

## Artifacts

`QOU/Hecke/IsospinClassSingleton.lean` grows 5 -> 8 decls: `contentDoubled`,
`two_le_row_two_content`, `contentDoubled_nonneg_of_two_le`,
`contentDoubled_neg_iff`. Kept in `ℤ` with the content doubled so no division
enters. `lean`-direct exit 0, no warnings.
`computations/qbeta/qbeta_charge_class_singleton_probe.py` (5/5, 30 dps).


## 2026-09-05 (later) — the bridge is unavailable, and mechanically so

`qou-qb7p`. The "image under the Wedderburn embedding" this bean recorded as an
unspecified gap turns out to be worse than unspecified:

- the corpus's only formalised embedding, `wedderburnEmbed`, is declared
  `opaque` — "keeps the embedding opaque pending concrete construction";
- it registers as a **fourth axiom** in `#print axioms`, beside `propext`,
  `Classical.choice` and `Quot.sound`, so anything routed through it is not
  axiom-clean by this corpus's own standard;
- its type assembles blocks into one matrix; the clause needs one block's scalar
  split into three coefficients — wrong direction and wrong arity;
- and no other `wedderburn*` object is a map of algebras.

The `(2,1)` clause is now annotated as an open obligation. So the six
coefficients this bean found are not hook products have **no derivation at all**
pending a construction of the embedding.
