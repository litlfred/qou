# Plan: full periodic table + all isotopes (real and theoretical)

**Date:** 2026-05-18
**Branch:** `claude/canonical-mass-table-extension`
**Status:** Drafting plan for the atlas extension to cover every atom and isotope under a single registry, with per-step knot-operator documentation.

## Scope

| Layer | Coverage target |
|---|---|
| Layer 1 — light isotopes (A ≤ ~7) | **Canonical Σ y_λ · χ^λ pipeline** (Rust χ + mpmath y_λ). Per-isotope braid word + per-step knot operator catalogued. |
| Layer 2 — α-cluster nuclei (A = 4·n_α, recursive) | **Recursive on ⁴He** + α–α coupling correction c_αα. Knot operators: ⁴He cluster braid (H_12 closure) + α–α fusion interface. |
| Layer 3 — non-α nuclei (5 ≤ A ≤ 40, intermediate) | Hybrid: nearest-α-cluster + valence-nucleon attachment via canonical interface operator. |
| Layer 4 — heavy nuclei (A > 40) | Brane-tower asymptotic + LP-active-set ansatz. Knot operators here are coarse-grained (Wedderburn-block level). |
| Layer 5 — theoretical / hypothetical isotopes | Same Layer-1/Layer-3 machinery; canonical braid word determined by atom-knot-recipe even when AME has no measurement. Flagged as `prediction-only`. |

## Per-isotope record schema (proposed)

For each (Z, N) entry the atlas should record:

| Field | Source / type | Purpose |
|---|---|---|
| `Z, N, A` | integer | atom identification |
| `n_strands = 3·A` | integer | braid-group strand count |
| `braid_word_canonical` | list of (sign, gen_index) tuples | canonical Hecke element T_w ∈ H_n(q_0); from `mass_at_3A_proper.atom_braid_word_3A(Z,N)` |
| `markov_closure` | identifier (knot/link name + crossing count) | knot-theoretic closure $\widehat{T_w}$ |
| `intra_nucleon_blocks` | per-nucleon list of (gen_index, ctype) | the σ_0 g_0 + σ_1 g_1 intra-strand blocks per nucleon |
| `inter_nucleon_interfaces` | list of (k → k+1, channel, ctype) | each pp/nn/pn interface at gen 3k+2; ctype ∈ {sigma, sigma_inv, averaged} |
| `wedderburn_blocks_used` | list of partitions λ ⊢ n with nonzero y_λ · χ^λ | which Wedderburn components carry the trace |
| `tr_M_q0_canonical` | mpf decimal string (50 dps) | canonical |tr_M(β_atom, q_0)| via Σ y_λ · χ^λ |
| `prediction_method` | tag | `canonical-trace` / `alpha-cluster` / `hybrid` / `volume-match-deprecated` |
| `prediction_MeV` | mpf decimal string | binding-energy prediction in MeV |
| `B_AME_MeV` | float | AME 2020 reference (when measured) |
| `err_MeV`, `err_pct`, `err_ppb` | float | derived |
| `derivation_chain_witness` | path to `.derivation.json` | provenance |

## Knot-operator catalogue (atlas additions)

Per the user direction "make sure atlas has all info about knot operators used at each step":

The atlas should document the **canonical knot-operator library** used in the recursive structure:

1. **Intra-nucleon operators** (H_3 building blocks)
   - Proton intra: σ₀ σ₀ σ₀ → trefoil closure
   - Neutron intra: σ₀⁻¹ σ₀⁻¹ σ₀⁻¹ → mirrored trefoil
   - Vortex `ρ`: vacuum-drag closed cycle (free quark)

2. **Inter-nucleon interfaces** (single-strand crossings at gen 3k+2)
   - pp coupling: σ at gen 3k+2 (pure positive crossing)
   - nn coupling: σ + (-h)·𝟙 (h-shifted crossing per the canonical convention)
   - pn coupling: σ - (h/2)·𝟙 (averaged half-shift)

3. **Closure topology operators**
   - Hopf link: σ₁² closure
   - Borromean baryon B_3: (σ₁ σ₂⁻¹)³ closure
   - Trefoil 3_1: σ₁³ closure
   - Figure-eight 4_1: (σ₁ σ₂⁻¹)² closure
   - Connected sum #_K K': for composite atoms

4. **Fusion operators** (α–α and α–nucleon couplings)
   - α–α fusion `c_αα`: interface between two ⁴He clusters
   - α–N attachment: ⁴He cluster + valence nucleon

Each atom's atlas entry should explicitly cite which of these operators it uses, in what sequence, with explicit gen-index slots.

## Atom registry — coverage map

Real atoms / isotopes by element (Z = 1..118), where the framework
has anything to say:

| Z | element | known isotopes A range | strategy |
|---|---|---|---|
| 1 | H | 1, 2, 3 (4-7 short-lived) | Layer 1 (canonical for A=1..3) |
| 2 | He | 3, 4 (5-10 short-lived) | Layer 1 for A=3; Layer 2 for A=4; Layer 3 hybrid for A>4 |
| 3 | Li | 6, 7 (4-12 unstable) | Layer 1 (canonical) for A=6,7 once Rust scales; Layer 3 hybrid otherwise |
| 4 | Be | 7-12 (most short-lived) | Layer 2 ⁸Be (recursive ⁴He+⁴He+c_αα); Layer 3 for odd-A |
| 5 | B | 8, 10, 11, 12, ... | Layer 3 hybrid |
| 6 | C | 11-15 (¹²C stable) | Layer 2 ¹²C = 3α; Layer 3 ¹³C, ¹⁴C |
| 7 | N | 13-15 (¹⁴N stable) | Layer 3 hybrid |
| 8 | O | 13-19 (¹⁶O = 4α stable) | Layer 2 ¹⁶O = 4α; Layer 3 ¹⁷O, ¹⁸O |
| 9–20 | F–Ca | many isotopes | Layer 2 for magic (²⁰Ne=5α, ²⁴Mg=6α, …, ⁴⁰Ca=10α); Layer 3 otherwise |
| 21–82 | Sc–Pb | hundreds of isotopes | Layer 4 (brane-tower) |
| 83+ | Bi onwards | mostly radioactive | Layer 4 |

Theoretical / hypothetical isotopes (e.g. neutron stars, superheavy
Z>118, exotic ¹⁰¹H one-neutron-rich, etc.) follow the same per-Z, N
machinery — flagged as `prediction-only` in the atlas.

## Execution sequence

Phase 1 — light isotopes canonical (A ≤ 7):

1. Verify Rust + mpmath pipeline works for {⁴He, ⁵Li, ⁶Li, ⁷Li}
   - Background ⁴He run in flight (task `bbjigmoln`)
   - ⁵Li (n=15, 176 partitions): expected ~minutes
   - ⁶Li (n=18, 385 partitions): expected ~10+ min; first attempt OOM'd
   - ⁷Li (n=21, 792 partitions): may not be feasible in this session
2. For each, emit atom-record per the schema above

Phase 2 — extend the atlas content block:

1. Add per-step knot-operator detail under each atom entry
2. Add a top-level "Knot-operator catalogue" section listing the primitives
3. Add the Layer-1/2/3/4/5 prediction-method classification

Phase 3 — registry script:

1. New `computations/atom_knot_atlas_registry.py`
2. Iterates over all real (Z, N) pairs (chart-of-nuclides slice)
3. Routes each to the appropriate Layer
4. Emits `atom-knot-atlas-registry.witness.json` with per-atom records

Phase 4 — atlas render:

1. Extend `recursive_atom_knot_atlas_render.py` to consume the new registry
2. Auto-generate the atlas .md sections from the registry

Phase 5 — Lean class for the recursive structure:

1. `class AtomKnotAtlas` axiomatising the recipe Z, N → braid word + closure
2. Instance proving the recipe for the canonical cases

## Feasibility risks

| Risk | Mitigation |
|---|---|
| Rust Hoefsmit OOM at H_18+ | Reduce parallel partition workers; or use sparse Hoefsmit; or fall back to the chi-cache path with mpmath |
| y_λ generation slow past n=24 | mpmath fast path already scales to ~10s for n=24; beyond that may need Rust port |
| Atom registry combinatorial explosion (~3000 known isotopes) | Layer 4 brane-tower is closed-form (no per-isotope Hoefsmit); only ~50 atoms need explicit canonical compute |

## Open questions for the user

- Q1: Does "all theoretical isotopes" include single-isotope predictions beyond the drip lines (Z > 120, neutron-rich one-nucleon-states)?
- Q2: For Layer 4 (heavy), should the atlas record the brane-tower formula PER isotope, or just per element + neutron-count parametrically?
- Q3: Priority order — extend Layer 1 (canonical light) first, or sketch Layer 4 (heavy) infrastructure first?
