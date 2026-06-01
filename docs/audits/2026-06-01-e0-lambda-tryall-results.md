# E₀^λ "try-all": testing 5 substrate-derived χ^λ → M_λ maps (2026-06-01)

**Branch:** `claude/e0-lambda-tryall-lean-2026-06-01`
**Harness:** [`folio-assistant/computations/e0_lambda_tryall.py`](../../folio-assistant/computations/e0_lambda_tryall.py)
**Witness:** `folio-assistant/computations/e0-lambda-tryall.witness.json`
**Sibling (do not touch):** `claude/e0-lambda-map-options-2026-06-01` (scoping doc)

## The precisely-delimited problem

The L2-Subgoal-1 gap reduces to ONE missing object: a **parameter-free map
χ^λ(K) → M_λ(K)** (substrate-derived per-block energies E₀^λ, in MeV).

- The binding operator K is substrate-fixable without B_AME (PR #1598).
- K's substrate content is its **character** χ^λ(K) (dimensionless).
- The mass formula `prop:rho-k-h3a-refinement` needs the per-block **mass-functor
  component** M_λ(K) (MeV). **χ^λ does not determine M_λ** — the character is a
  dimensionless trace; the mass component carries a dimensional scale χ^λ cannot
  supply.

## The falsification anchors

The only existing χ^λ → M_λ map is the **deprecated** LSQ fit
`_deprecated/per_block_phi_q.py::fit_three_E0`. It fits three per-block scales
(E₀^sym, E₀^std, E₀^alt) by linear least squares against CODATA masses, using
per-block **cat-unit structural masses** m^b (computed from the particle braid
words via per-block Φ_q). The fitted scales are:

| Fit | E₀^sym | E₀^std | E₀^alt |
|-----|--------|--------|--------|
| 3-obs {e⁻,p,n} (exact) | `+3.0755e-09` | `−7.0936e-09` | `+5.9647e-06` |
| 5-obs (overdetermined LSQ) | `+1.7721e-06` | `−2.9202e-07` | `+2.6007e-06` |

The per-block cat-unit structural masses m^b (the χ^λ-derived quantities a
substrate map would have to scale into MeV):

| particle | m^sym | m^std | m^alt | obs (MeV) |
|----------|-------|-------|-------|-----------|
| electron | 1.5739e8 | 4450.3 | 4521.8 | 0.510999 |
| proton   | 1.9664e8 | 1.5956e8 | 1.5739e8 | 938.272 |
| neutron  | 1.9664e8 | 2.0790e5 | 1.5742e8 | 939.565 |

**Two anchor pathologies, visible before any candidate is run:**

1. **E₀^std is negative** in the 3-obs fit (`−7.09e-9`). A per-block *energy*
   scale must be ≥ 0 (it is a mass-functor component). A negative best-fit scale
   is a regression artefact, not a physical substrate quantity.
2. **The fit is ill-conditioned.** E₀^sym swings by 575× (3.08e-9 → 1.77e-6)
   between the 3-obs and 5-obs fits; E₀^std flips sign-magnitude. A genuine
   substrate scale would be stable under adding observables.

These two facts mean the anchors are **not** a clean target: any candidate that
hit them exactly would be reproducing a regression artefact. The honest test is
therefore: does a candidate produce **stable, positive, per-block E₀^λ that map
the structural m^b into the observed MeV across all three anchors with one (or
zero) global constant**? That is the PASS bar.

## Candidate results

(filled in per-commit as each candidate lands)

| # | Candidate | Verdict | Notes |
|---|-----------|---------|-------|
| 1 | Archimedean per-block | — | |
| 2 | q-dimension (+ variants) | — | |
| 3 | Option-E ρ_w energy functional | — | |
| 4 | Casimir (content-sum) | — | |
| 5 | Ribbon twist θ_λ | — | |

## Bottom line

(filled in at end)
