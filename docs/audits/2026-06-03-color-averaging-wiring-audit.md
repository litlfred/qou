# Color-averaging wiring audit — mass + binding pipelines

**Status:** AUDIT + WIRE (in progress). Owner directive 2026-06-03: wire the
color-averaged (`bring_color_weighted`) inter-nucleon interface **everywhere**
it is missing in the mass + binding compute — even where it is not today's
dominant error (it will matter later). Aligns production with the standing
2026-06-01 directive that `bring_color_weighted` is canonical/default.

## The convention

The p-n interface averaged crossing has two forms:

| convention | crossing `(c, d)` | color |
|------------|-------------------|-------|
| `strict_averaged` | `(1, −h/2)` | **blind** |
| `bring_color_weighted` (default) | `(1, −h·(1/2 − δ/4))`, δ = `flavor_split_subleading(q₀)` ≈ 1.4e-3 | weighted |

The p-p (`(1, 0)` = σ) and n-n (`(1, −h)` = σ⁻¹) interfaces are already
isospin-distinct and carry no extra color weight.

## Audit finding — the entire production pipeline was color-blind

The canonical braid builder `mass_at_3A_proper.py::atom_braid_word_3A` (the
single source of truth feeding 50+ consumers) hardcoded the p-n interface as
color-blind `(1, −h/2)`. `closed_form_tau_M.py` implemented and defaulted to
`bring_color_weighted`, but every production script overrode it back to
`strict_averaged` / `chi_lambda_braid`. So the master site was the one
high-leverage wire point.

## Wired (this PR)

- **MASTER — `mass_at_3A_proper.py::atom_braid_word_3A`**: added
  `pn_convention="bring_color_weighted"` (default); the p-n crossing is now
  `(1, −h·(1/2 − δ/4))` with cached δ from `flavor_split_subleading(q₀)`.
  `strict_averaged` retained for empirical-pipeline validation callers. All
  50+ downstream consumers (binding_canonical, binding_depth_stratified,
  compute_atom_chi_rust, canonical_tr_m_via_branching, binding_via_interface_knot,
  rho_k_h3a_refinement, …) inherit color-weighting automatically.

**Verification:** `binding_canonical.py` now color-weighted by default;
`|tr_atom|` shifts at the ~1e-4 (δ/4 ≈ 3.4e-4) scale (D: 3.882864e-01 →
3.883572e-01), B_pred essentially unchanged, no breakage. The shift is the
expected Δm_pn-scale (0.14 %) correction — small, as
[`2026-06-03-color-vs-charge-crossing-tn3he.md`](2026-06-03-color-vs-charge-crossing-tn3he.md)
established (color is the Δm_pn-scale refinement, not the dominant binding
residual). Single-nucleon masses (m_p, m_n — the anchors) are unaffected
(no inter-nucleon interface at A=1).

## Witness regeneration (color-blind → color-weighted)

The cached χ / tr_M witnesses inherit the master site and need regeneration:

- `atom-chi-rust-{d,t,3he,4he}.witness.json` (via `compute_atom_chi_rust.py` + `pyhecke_native`)
- `binding-canonical.witness.json` (regenerated this PR)
- `atomic-tr-m-helium4-canonical`, `binding-via-interface-knot`,
  `atomic-braid-recipe-{d,4he}`, and ~10 more — follow-up sweep.

## Symbolic-path fix (the master flip's downstream regression)

Flipping the master default exposed a real regression: the symbolic
`(gen, ctype)` character path **discards the numeric d** and rebuilds the
`"averaged"` ctype as the color-blind `−h/2`, so (a) `classify_crossing` /
`canonical_braid_marshalling` *threw* on the unrecognised color-weighted
`d ≈ −0.10446`, and (b) `chi_lambda_numerical` silently dropped the weight
(B_pn stuck at the color-blind 2.3043). Fixed:

- `canonical_braid_crossings.classify_crossing` + `canonical_braid_marshalling`
  now **accept** the color-weighted averaged crossing (`−h·(1/2 − δ/4)`),
  not just `−h/2`.
- `habiro/habiro_coefficients_interpolate.chi_lambda_numerical` d_map maps
  `"averaged"` to the color-weighted `−h·(1/2 − δ/4)` (centralized δ via
  `_avg_color_delta`). B_pn now shifts 2.3043 → **2.3048** (color-weighted),
  consistent with `binding_canonical` and the Rust χ cache.

**Gate held:** the 1ppb cross-check (`cross_check_trM_1ppb --strict`) stays
**green (0 divergent)** — it validates the Hoefsmit / markov_peel / chi-cache
/ Habiro backbone against each other, none of which routes through
`chi_lambda_numerical`, so the fix does not destabilize the validation
backbone. The color weight is a production-path refinement (Δm_pn scale,
~3.4e-4); the cross-check backbone validates structural agreement.

## Remaining (follow-up)

- Flip the explicit production overrides that bypass the default:
  `binding_canonical.py` (`strict_averaged`), `atomic_tr_m_helium4_canonical.py`
  (`chi_lambda_braid`) — after confirming each is production, not validation.
- Leave validation-only callers (`closed_form_tau_M_verification_phase5q.py`)
  on `chi_lambda_braid` (they match the empirical pipeline by design).
- Regenerate the remaining cached witnesses.

## Per the canonical-chain discipline

This touches the canonical derivation chain (interface operator → tr_M). The
matching `alg:`-block under `appendix-mass-binding-algorithms/` should note
the color-weighted interface as the default. Flagged for the appendix sync.
