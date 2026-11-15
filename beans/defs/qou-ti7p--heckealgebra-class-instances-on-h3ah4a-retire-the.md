---
# qou-ti7p
title: HeckeAlgebra class instances on H3A/H4A; retire the redundant InstanceH3/H4 carriers
status: completed
type: task
priority: normal
created_at: 2026-08-09T15:01:49Z
updated_at: 2026-08-09T18:36:30Z
---


Follows qou-awp7. `QOU/Hecke/FullRankFromWedderburn.lean` now proves
`IsHeckeOfFullRank K 3 (H3A K h)` and `IsHeckeOfFullRank K 4 (H4A K h)` as
instances. What is missing on those same carriers is the other half:

```lean
instance : HeckeAlgebra K 3 q (H3A K (q - q⁻¹))
instance : HeckeAlgebra K 4 q (H4A K (q - q⁻¹))
```

Everything they need is already proved on those bases:

| field | source |
|---|---|
| `quadratic` | `HeckeH3AlgebraLaws.mulσ₁_hecke`; `HeckeH4StabilizationRung.mulσ₀/₁/₂_hecke` |
| `braid` | `HeckeH3AlgebraLaws.braid_operator`; `…braid_σ₀σ₁`, `…braid_σ₁σ₂` |
| `farCommute` | vacuous at `n = 3`; `…far_commute_σ₀σ₂` at `n = 4` |
| `spans` | basis decomposition — `HeckeH4AlgebraLaws.basis_decomp₄` and the word actions |

The work is transporting each from the coordinate form (`mulσₖ h v = …`) to the
ring form the class asks for (`embed i * embed i = (q - q⁻¹) • embed i + 1`),
through the `H3A`/`H4A` wrappers, and picking out the generator elements.

## Then retire the duplicates

`QOU/Hecke/InstanceH3.H3Alg` and `QOU/Hecke/InstanceH4.H4Alg` were built without
knowing `H3A`/`H4A` existed. Once the class instances sit on the real carriers,
those two are redundant carriers carrying nothing the tree needs:

- `InstanceH3` — `H3.mul_assoc` and the `Ring`/`Algebra` on `H3Carrier` duplicate
  `HeckeH3AlgebraInstance`. Genuinely its own: the relations restated over an
  arbitrary field in ring form (the `QOU.Mathlib.HeckeAlgebra` originals are
  `ℝ`-only and in generator-action form). Keep those, drop the carrier.
- `InstanceH4` — the six relation lemmas are on `MarkovTraceH4`'s **ASCII** basis,
  which is a different table from the subscript basis `HeckeH4StabilizationRung`
  proves them on, and which nothing else checks. That is worth keeping on its own
  terms. The operator algebra `H4Alg` and its `HeckeAlgebra` instance are the
  redundant part.

Do not delete either file wholesale; separate what is duplicated from what is not.

## DONE (both instances) — `QOU/Hecke/InstanceOnH3A.lean`, `QOU/Hecke/InstanceOnH4A.lean`

`instHeckeAlgebraH3A : HeckeAlgebra K 3 q (H3A K (q - q⁻¹))` and
`instHeckeAlgebraH4A : HeckeAlgebra K 4 q (H4A K (q - q⁻¹))`, both axiom-clean.
Paired with `isHeckeOfFullRank_H3A` / `_H4A` these are the first objects for which
both halves hold of the same carrier: the relations **and** the dimension.

### Keeping `spans` cheap at `n = 4`: the word tree

The naive route needs every basis vector as a word, and the longest is
`σ₀σ₁σ₀σ₂σ₁σ₀` — six letters. Expanding six nested `mulσ`s per basis vector is
what took the analogous attempt on the ASCII basis to ~8.7 GB (qou-awp7).

Avoidable, because right multiplication by a generator is a **single** `mulσ`:
`mulNF₄_e_right` gives `u · b_j = wordAction j u`, and the generators sit at basis
indices `1`, `2`, `6`, whose word actions are exactly `mulσ₀`, `mulσ₁`, `mulσ₂`.
So each basis vector is its parent times one generator and every step is depth 1
on a literal vector:

    b_j = b_{parent j} * σ_{last letter of word j}

The 23 non-unit basis vectors form a tree under that relation — checked, not
assumed: every parent word is itself in the basis list. Generated from
`wordAction`'s own word list so it cannot drift. **Whole file: 73 seconds.**

### One real snag, worth remembering

The braid relations cannot be quoted at `v = (s0).v`. `braid_σ₀σ₁ h v` is
`mulσ₀(mulσ₁(mulσ₀ v)) = mulσ₁(mulσ₀(mulσ₁ v))` — three deep — while the product
`s0 * s1 * s0` reduces to two. The fix is to quote it at `v = γ` and supply
`mulσ₀ h unitNF₄ = (s0).v` etc. (`mulσ₀_unit`, `mulσ₁_unit`, `mulσ₂_unit`).
Quoting it at the wrong `v` also drives `isDefEq` past its heartbeat limit rather
than failing cleanly.

### DONE: the duplicate carriers are retired

`QOU/Hecke/InstanceH3.lean` and `QOU/Hecke/InstanceH4.lean` are **deleted**.
Nothing imported either — the only references anywhere in the tree were three
docstring lines, now repointed. What was genuinely theirs moved to where it
belongs, which in both cases is next to the table it is about, not next to the
class it was fed to.

| was | is now | why there |
|---|---|---|
| `InstanceH3.H3.mul_assoc`, `H3.mul_one` | `QOU/Mathlib/HeckeAlgebra.lean`, right after `H3.one_mul` | they are the ring laws of `H3.mul`, which is defined nine lines above; `one_mul` without `mul_one`/`mul_assoc` was conspicuously partial |
| `H3.sigma1_sq_carrier`, `H3.sigma2_sq_carrier`, `H3.braid_carrier` | same file, renamed `H3.sigma1_sq_mul` / `H3.sigma2_sq_mul` / `H3.braid_mul` | the arbitrary-field, `H3.mul`-form counterparts of the ℝ-only generator-action `H3.sigma1_sq_eq` / `H3.sigma2_sq_eq` / `H3.braid_relation` sitting thirty lines above them |
| `InstanceH4.mulσ_sq0/1/2`, `mulσ_braid01/12`, `mulσ_farcomm02`, the `e0` noncommutativity witness | new `QOU/Machinery/H4AsciiPresentation.lean`, namespace `QOU.Machinery.H4` | they are the Hecke presentation on `MarkovTraceH4`'s **ASCII** table, which nothing else checks |

Dropped outright, as pure carrier scaffolding: `H3.mul_add`, `H3.add_mul`,
`H3.zero_mul`, `H3.mul_zero`, `H3.smul_mul`, `H3.mul_smul` (existed only to fill
`Ring`/`Algebra` fields); `H3Alg` and its instances; `sigma1_sq` / `sigma2_sq` /
`braid` / `sigma1_mul_sigma2` / `sigma2_mul_sigma1` /
`sigma1_mul_sigma2_mul_sigma1` / `decompose` / `embed3` / `instHeckeAlgebraH3` /
`finrank_H3Alg` / `instIsHeckeOfFullRankH3`; `L0` / `L1` / `L2` and their
`Module.End` relation transports, `H4Alg`, `embed4`, `instHeckeAlgebraH4`.

### `mulσ_farcomm02` was a literal duplicate

`H4BasisBridge` had proved it a second time — same statement, same table, same
four-line proof — because it needs `σ₀σ₂ = σ₂σ₀` on the ASCII generators to
normalise the six words where the two bases differ. That copy is gone; the bridge
imports `H4AsciiPresentation`. This is the only place in the retirement where two
proofs were genuinely the same proof.

### Base ring widened on the way out

The six ASCII relations were stated over `[Field R]` only because `InstanceH4`'s
carrier needed a field for the `Algebra` structure. None of them inverts anything,
so in `H4AsciiPresentation` they are `[CommRing R]`; the noncommutativity witness
adds `[Nontrivial R]` and nothing else. (Related: qou-yax5.)

### The point of the exercise, stated plainly

`instHeckeAlgebraH4` was a real `HeckeAlgebra R 4 q` instance whose **dimension was
never pinned** — `IsHeckeOfFullRank R 4 (H4Alg R q)` was left open, and the module
said so. `InstanceH3` had both halves but on a carrier with no Wedderburn
decomposition and no Markov trace. The pairs that now carry the load —
`instHeckeAlgebraH3A` + `isHeckeOfFullRank_H3A`, `instHeckeAlgebraH4A` +
`isHeckeOfFullRank_H4A` — hold of the same carriers that also carry `wedderburn₃` /
`wedderburn₄` and, at `n = 3`, `markovTraceH3A`. That is the whole reason to prefer
them, and the reason these two files had to go rather than sit alongside.
