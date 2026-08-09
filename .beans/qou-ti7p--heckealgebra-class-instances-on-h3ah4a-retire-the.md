---
# qou-ti7p
title: HeckeAlgebra class instances on H3A/H4A; retire the redundant InstanceH3/H4 carriers
status: todo
type: task
created_at: 2026-08-09T15:01:49Z
updated_at: 2026-08-09T15:01:49Z
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
