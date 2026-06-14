# Lean vacuous-proof audit — self-assuming projections

**Date:** 2026-06-14
**Branch:** `claude/keen-keller-cvlt61`
**Skill:** [`lean-proof-vacuity-audit`](../../.claude/skills/local/lean-proof-vacuity-audit.md)
**Trigger:** PR #2284 (`gauge-coupling-uniqueness.lean`) — discovered that the
owner's batch commit `e138518a` ("fix 12 proof-statement-integrity failures")
discharged a false axiom by wrapping the conclusion in a `structure` field and
projecting it, producing a **vacuous self-assuming projection** (the theorem
assumes its own conclusion). The fix passes `proof-statement-integrity` (no
`sorry`/axiom, signature unchanged) yet proves nothing.

## The anti-pattern

```lean
structure D (S) where
  hyp1 : ...                                   -- decoration, NEVER used
  exists_lambda : ∃ λ, ∀ r, phi r = λ * psi r  -- ← the CONCLUSION, as a field
theorem foo (S) (d : D S) :
    ∃ λ, ∀ r, d.phi r = λ * d.psi r := d.exists_lambda   -- ← P ⊢ P, vacuous
```

`proof-statement-integrity` is `automated: false` and checks only
signature-stability + an axiom sweep — both satisfied here. Vacuity is a
*semantic* property of the proof term, so it needs a separate agent-checked
criterion: **`proof-no-self-assuming-projection`** (added to
`content/pipeline/qa-criteria-registry.ts`, `PROOF` domain).

## Findings — 12 HIGH-confidence instances

All follow the exact shape `theorem foo (d : D) : Conclusion := ⟨d.field1,
d.field2, …⟩` where the goal is the conjunction of the carrier's
conclusion-typed fields and **no** sibling hypothesis is used in a derivation.

### From batch commit `e138518a` (6)

| # | File | Decl | Carrier ← projected fields |
|---|------|------|----------------------------|
| 1 | `predicted-spectra/cs-evaluation-faithfulness.lean` | `CSEvaluationFaithful` | `CSEvaluationFaithfulData` ← `kappa_n_nonzero`, `phi_n_nonzero` |
| 2 | `predicted-spectra/knot-operator-selection.lean` | `knot_operator_selection` | `KnotOperatorSelectionData` ← `is_frobenius_dual`, `selects_knot_operator` |
| 3 | `predicted-spectra/metallic-character-knot.lean` | `metallic_character_knot` | `MetallicCharacterKnotData` ← `is_incomplete_sub_hopf_link`, `has_metallic_character` |
| 4 | `predicted-spectra/noble-gas-characterization.lean` | `noble_gas_characterization` | `NobleGasCharacterizationData` ← `is_full_shell`, `is_full_curl` |
| 5 | `quantum-observable-universes/fai-projector-coadjoint-orbit.lean` | `fai_projector_coadjoint_orbit` | `ProjectorCoadjointOrbit` ← `sigma_involution`, `is_coadjoint_orbit` |
| 6 | `quantum-observable-universes/fibre-functor-atlas.lean` | `fibre_functor_atlas` | `FibreFunctorAtlasData` ← `is_affine_chart`, `is_g_torsor`, `cocycle_condition`, `is_g_gerbe` |

### Independent of `e138518a` (6)

| # | File | Decl | Carrier ← projected fields |
|---|------|------|----------------------------|
| 7 | `predicted-spectra/beta-decay-skein.lean:242` | `beta_decay_locality` | `BetaMinusDecay` ← `daughter.p`, `daughter.n`, `daughter.A` |
| 8 | `quantum-observable-universes/emergence-to-quantum-flat.lean:57` | `emergence_to_quantum_flat` | `QuantumFlatnessEmergence` ← `instanton` |
| 9 | `lean/QOU/LiftingDescent/ccg_cosimplicial_identities.lean:47` | `ccg_cosimplicial_identities` | `CcgCosimplicialIdentitiesContext` ← `claim_face_face`, `claim_deg_deg` |
| 10 | `lean/QOU/Encounter/MostowRigidity.lean:153` | `mass_rigidity_of_mostow` | `MostowRigidity` ← `volume_nonneg`, `mostow_gap_pos` |
| 11 | `lean/QOU/LiftingDescent/ccg_crossed_module_structure.lean:46` | `ccg_crossed_module_structure` | `CrossedModuleContext` ← `peiffer`, `boundary_compat` |
| 12 | `lean/QOU/BraidKnot/geom_yekutieli_alignment.lean:85` | `geom_yekutieli_per_block_alignment` | `GeomYekutieliAlignmentContext` ← `claim_iv_holonomy_equals_trM`, `claim_v_mass_factor_per_block` |

## Exemplar (already fixed)

`predicted-spectra/gauge-coupling-uniqueness.lean` (PR #2284,
`claude/funny-hawking-qeyqa2`) — superseded with a genuine proof that `obtain`s
the `e₊+e₋=1`, `e₊·e₋=0` decomposition from `em_spectral_completeness`, *derives*
idempotency, and proves uniqueness with witness `λ = c·u⁻¹`. The import is now
load-bearing. This is the **recipe-1 (genuine proof)** template for the drain.

## Excluded — legitimate conditional-class proofs (6)

Correctly NOT flagged (proof composes/derives from fields): `self_dual_eq_b_field`
(linarith over 3 fields), `categorical_self_duality` (constructor-with-derivation),
`qDirac` (rw composition), `q_0_well_defined` (genuine existential witness),
`CategoricalQConnection.exists` (witness + `rfl`), `q_codifferential_formula`
(conditional-class axiom delegation).

## Drain plan

Per the skill's fix recipe, classify each instance during the drain:

1. **Genuine proof** — restructure carrier fields into hypotheses / `obtain` from
   upstream and derive. (Expected for categorical identities: #9, #11, #12,
   possibly #5, #6.)
2. **§3b-cond conditional-class** — for conjecture-dependent results.
3. **Honest named axiom `-- Ref:`** — for legitimate external inputs.
4. **Demote `theorem` → `conjecture`** — for genuinely-unproved claims. **Claim
   change — requires owner sign-off; do NOT auto-commit.**

Commit per file (or per small directory batch); verify each with `lean`-direct
against restored `lake-cache/qou-<toolchain-slug>` oleans. Backfill
`proof-no-self-assuming-projection` sidecars via `qa-sweep` on each drained block.

## Resolution (2026-06-14)

**Batch-6 (the `e138518a` files) — RESOLVED (commit `af008b68`).** These are
**sibling-resolution stubs**: the genuine formalisations already exist in the QOU
library tree (`lean/QOU/Archimedean/{HyperbolicVolumeTranscendence,
knot_operator_selection, metallic_character_knot, noble_gas_characterization}.lean`,
`lean/QOU/QuantumObservableUniverse/{fai_projector_coadjoint_orbit,
fibre_functor_atlas}.lean`). The 6 siblings were reverted to the honest
`: True := trivial` stub form (matching ~207 other siblings); the deceptive
`True ∧ True` projection is gone. Not formalised here — already formalised in the
library.

**Sibling-stub exemption.** `proof-no-self-assuming-projection` /
`proof-no-trivial-true` now EXEMPT sibling-resolution stubs (they target the
library decl the block resolves to, not the stub).

**Systemic finding — stub-shadow manifest (2026-06-14).** 219 `Sibling-resolution
stub` files. The resolver (`content/pipeline/export-json.ts:resolveLeanFilePath`)
checks the sibling **before** the library decl-path, so a trivial `: True` sibling
shadows the real library proof. Manifest classification:

| Class | Count | Action |
|-------|-------|--------|
| **SHADOW** | 147 | delete — `lean.ref` decl-path resolves to a real library decl |
| **MISMATCH** | 25 | align — decl in a mis-named library file |
| **NEEDED** | 19 | flag — no library formalisation; genuinely unformalised `: True` |
| **NOREF** | 25 | inspect — `.ts` has no `qou:` ref |
| **definition** | 3 | keep — sibling required |

Codified as the **no-shadowing-stubs** directive in CLAUDE.md §0a. Deleting the
147 SHADOW stubs makes those blocks resolve to their real library proofs (honest
formalisation status); the 19 NEEDED placeholders are the genuine integrity gap.

**Real drain targets — the independent-6** (genuine vacuity in real files, not
stubs): `beta-decay-skein.lean:242`, `emergence-to-quantum-flat.lean:57`,
`ccg_cosimplicial_identities.lean:47`, `MostowRigidity.lean:153`,
`ccg_crossed_module_structure.lean:46`, `geom_yekutieli_alignment.lean:85`.
Per-file classification + honest fixes in progress.
