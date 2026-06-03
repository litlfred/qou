# Color-averaging witness regeneration sweep (2026-06-03)

Mechanical sweep: regenerate committed witnesses affected by the
color-averaging master flip merged on main (PR #1754).

## What changed (the canonical spec)

`mass_at_3A_proper.atom_braid_word_3A` now defaults to
`pn_convention="bring_color_weighted"`: the inter-nucleon **p-n interface**
("averaged" crossing) is now `σ − h·(1/2 − δ/4)·𝟙` instead of the color-blind
`σ − h/2·𝟙`. Symbols (see
[`coulomb-charge.md`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md)
and `docs/audits/2026-06-03-color-averaging-wiring-audit.md`):

- **σ** — the Hecke generator (braid crossing) at the interface gen.
- **h** = `q₀ − q₀⁻¹ ≈ 0.10998` — the substrate Hecke differential.
- **δ** = `flavor_split_subleading(q₀) ≈ 1.38e-3` — the substrate
  `(m_n − m_p)/M_N` flavor split (`_li_2_q_util.flavor_split_subleading`).
- **p-n interface** — the inter-nucleon "averaged" crossing between a proton
  block and a neutron block (gen `3k+2`); p-p (σ) and n-n (σ⁻¹) interfaces are
  isospin-distinct and unchanged.

The numerical effect is at the Δm_pn scale (`δ/4 ≈ 3.4e-4`).

## Regenerated witnesses (12)

`atom-chi-rust-{d,t,3he,4he}`, `atomic-mass-via-rho-k`,
`atomic-tr-m-mpfr-50dps`, `binding-depth-stratified`,
`binding-via-interface-knot`, `mass-endomorphism`, `rho-k-h3a-refinement`,
`sublemma-2-1-deuteron-branching`, `tr-m-q-hecke-seminormal`.

Generators that ran clean but produced no committed-witness change (already
at the color-weighted value from #1754, or single-nucleon / unaffected) are
not listed. Validation generators that intentionally pass `strict_averaged`
/ `chi_lambda_braid` were excluded (they stay color-blind by design).

## Caveat — env/precision churn rides along (CI was billing-down)

The witness-pipeline CI (the canonical regeneration env) was billing-down, so
the owner directed regenerating here. Regenerating in this container also
flips each witness's `environment` block (Python `3.12.3 → 3.11.15`) and
bumps `precisionMetadata` (`compute_dps 65→70`, `output_dps 50→60`, etc., as
these witnesses predate a precision-default change). These ride along with the
~1e-4 color-weighting shift. **CI will normalize the `environment` block when
billing clears** (it re-runs in the canonical env). This sweep prioritizes
value-correctness (color-weighted χ/tr_M) over env-metadata fidelity.

## Verification

`cross_check_trM_1ppb.py --strict` → **green, 0 divergent** (the
Hoefsmit / markov_peel / chi-cache / Habiro backbone stays mutually
consistent after the regen).
