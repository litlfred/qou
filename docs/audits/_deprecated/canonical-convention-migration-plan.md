> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# Canonical-convention migration plan (atomic braid words)

*Status: planning doc.  Audit run 2026-05-09.*

## Goal

Per repo-owner directive, **all production pipeline scripts should use
the canonical operator-valued convention** for atomic braid words —
i.e. consume words from `canonical_braid_crossings.atom_canonical_crossings(Z, N)`
in the `(gen_idx, ctype)` format with `ctype ∈ {sigma, sigma_inv,
averaged}` rather than the legacy bare-int `[1, 2, -1, …]` form.

The canonical convention adds **averaged crossings** `I_g := σ_g −
(h/2)·1` (where `h = q − q⁻¹`) which encode the operator-valued
interface of `prop:hecke-branching-trace-decomposition` and are
SDP-confirmed canonical by PR #608's
[`r5_full_canonical_knot_solver`](../../computations/r5_full_canonical_knot_solver.py)
for D and ³He.  These cannot be expressed in the legacy bare-int form.

## Current state (post-PR #606)

### Already canonical (via re-export alias)

PR #572 made `hecke_character_symbolic.atomic_braid_to_crossings` a
backward-compat re-export of `canonical_braid_crossings.atom_canonical_crossings`.
14 active scripts importing the legacy name therefore consume
canonical underneath.

### Already canonical (direct)

19 active scripts call `atom_canonical_crossings` directly (e.g.
`build_markov_trace_assembly_neutron_chain.py`,
`build_markov_trace_assembly_deuteron_chain.py`,
`r5_full_canonical_knot_solver.py`, the 4 canonical
atomic-braid-recipe builders).

### True legacy hold-outs (active)

| File | Convention | Blocker |
|---|---|---|
| [`atomic_braid_gb_filtration_extension.py`](../../computations/atomic_braid_gb_filtration_extension.py) | bare-int `ATOMIC_BRAIDS` registry | `gb_filtration_jet_tracker.reduce_braid` accepts only bare-int |
| [`term7_alpha5_crystal_derivation.py`](../../computations/term7_alpha5_crystal_derivation.py) | bare-int `ATOMS` registry | `crystal_chi_lambda` defined only for σ / σ⁻¹ |
| [`build_atomic_braid_recipe_4he_chain.py`](../../computations/build_atomic_braid_recipe_4he_chain.py) | bare-int leaf | parity with above |
| [`build_term7_s_crystal_4he_chain.py`](../../computations/build_term7_s_crystal_4he_chain.py) | bare-int leaf | inherits from `crystal_chi_lambda` |

The two underlying tools — `gb_filtration_jet_tracker.reduce_braid`
and `term7_alpha5_crystal_derivation.crystal_chi_lambda` — are
mathematically defined only on σ / σ⁻¹ words.  Migrating their
consumers to canonical is **blocked on extending these tools to
averaged crossings**.

## The two math blockers

### Blocker A — Crystal limit of averaged crossings

`crystal_chi_lambda(shape, word)` computes χ_λ(β) at q → 0 via the
sign-of-axial-distance permutation rule on SYTs.  This rule is
defined on σ_g (signed) and σ_g⁻¹ (involutive at q = 0); for an
averaged crossing `I_g = σ_g − (h/2)·1` the q → 0 limit
diverges (h → −∞) and the standard signed-permutation eigenvalue
formula `T ↦ sign(ρ_T(g)) · T` does not extend.

**To resolve**: define a "crystal-limit χ for averaged crossings"
either by

1. taking the q → 0 limit of the symmetric eigenspace projection
   (the +q-eigenvalue half of σ — this would give `I` the same
   crystal action as σ minus the trivial trace), or
2. routing through the canonical form `I_g · 2 = 2σ_g − h·1` and
   using `[2]_q I = q⁻¹·1 + q·σ` plus the q → 0 limit of `[2]_q`,
   or
3. defining a separate functor (the "averaged crystal limit")
   that carries the projection-to-symmetric channel structurally.

Each path is research; **the right answer is not obvious** and may
require new theory (likely tied to `conj:crystal-graph-realization`).

### Blocker B — GS filtration on averaged crossings

`gb_filtration_jet_tracker.reduce_braid(name, n, word, expected)`
walks the GS reduction system on a list-of-int word.  Its inner
loop applies σ_i / σ_i⁻¹ commutation/braid moves; an averaged
generator `I_i` does not have its own GS rewrite rule in the current
tracker.

**To resolve**: extend the tracker with rewrite rules for the
averaged generator (e.g. `I_i · I_j = I_j · I_i` when |i − j| ≥ 2,
plus the I-form of the braid relation; both follow from the σ
relations + linearity but need to be encoded).

This is a substantial change to the tracker; estimate ~few days
of focused work to add and validate.

## Migration steps (in priority order)

| Step | Cost | Ships in |
|---|---|---|
| 1. **DONE** — write canonical companions for `atomic-braid-recipe-{p,n,d}` | shipped PR #606 | merged |
| 2. **DONE** — write canonical companion for `atomic-braid-recipe-4he` | shipped batch 1 | this PR |
| 3. **DONE** — add deprecation notices to legacy `atomic_braid_gb_filtration_extension` and `build_atomic_braid_recipe_4he_chain` | shipped batch 1 | this PR |
| 4. Resolve **Blocker B** (extend `gb_filtration_jet_tracker` with averaged rewrites); migrate `atomic_braid_gb_filtration_extension` to canonical | research + ~3-5 days | future |
| 5. Resolve **Blocker A** (define crystal limit of averaged crossings); migrate `term7_alpha5_crystal_derivation.crystal_chi_lambda` to canonical | open math research | future |
| 6. Once steps 4-5 land, replace legacy `atomic-braid-recipe-4he.derivation.json` and `term7-s-crystal-4he.derivation.json` with their canonical equivalents; delete the legacy builders. | follow-up | future |

## Why two conventions coexist (the pragmatic answer)

The canonical convention carries **strictly more information** than
legacy: averaged crossings I = σ − h/2·1 are a structural ingredient
visible only in the operator-valued form.  A legacy bare-int word is
the **decay product** when averaged crossings are forgotten; for
specific combinatorial tools (crystal limit, GS jet tracker) that
depend on the σ/σ⁻¹ split, the legacy form is currently the only
mathematically-defined input.

Eliminating legacy from the codebase requires extending those tools
to handle averaged crossings — that's the math research work in
blockers A and B.  Until then, **legacy is a feature, not a bug**:
it is the input format of pre-canonical tools.  This document
records the migration intent so the work happens incrementally.
