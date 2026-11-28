# Removal of the convention-C dressed-mass fit (2026-11-28)

## What was removed

| File | Removed | Why |
|---|---|---|
| `QOU/MassTheory/HadronicMass.lean` | `dressed_mass_up := 311.10`, `dressed_mass_down := 312.39` | chosen under the retired convention-C pair formula so that the pair Skein sums reproduce `m_p`, `m_n` (selection against the target) |
| `knots-particles-confinement/knot-particle-generation.lean` | `mu_up := 311.10`, `mu_down := 312.39`; convention-C `pairSkeinMass` (denominator `√q + 1/√q`) | same fit; the formula is replaced by the derived convention-D form |
| `mass-theory/mass-from-generators.lean` | `qou_hydrogen_1` … `qou_iron_56` (12 rows); `hydrogen_agreement`, `deuterium_agreement`, `helium_4_agreement` | rows computed from the fitted dressed masses; the theorems compared them with CODATA inside Lean |

The pair Skein masses and nucleon sums now take μ_u and μ_d as parameters.

## Authority

- Carl, 2026-11-27: "Derive the convention D. Formula. Go ahead and migrate the convention D" (PR #9862), plus the standing rules "derive what you can" and "no fitting".
- Removal of the atom rows: coordinator relay on 2026-11-28 applying Carl's standing pick (take the recommended option). Carl may override.

## Status: open

No derivation of μ_u or μ_d from the aether is on record. Under convention D the nucleon map `(μ_u, μ_d) ↦ (m_p, m_n)` is a bijection (determinant 3κ², `QOU.MassTheory.PairSkeinNucleon`). So measured nucleon masses fix the dressed masses only by a change of variables. The conjectured flavour split `conj:flavor-split-aether-mass` fixes at most `μ_d − μ_u`.

## Not changed

The legacy Python generators `computations/all-elements-knot-table.py`, `first-20-elements.py` and `generate-appendix-table-v2.py` still hardcode 311.10 / 312.39. The docstring of `categorical_q_decay_ba_low_isotopes.py` also lists them.
