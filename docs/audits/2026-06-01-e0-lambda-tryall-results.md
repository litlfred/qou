# E₀^λ "try-all": testing 5 substrate-derived χ^λ → M_λ maps (2026-06-01)

**Branch:** `claude/e0-lambda-tryall-lean-2026-06-01`
**Harness:** [`computations/e0_lambda_tryall.py`](../../computations/e0_lambda_tryall.py)
**Witness:** `computations/e0-lambda-tryall.witness.json`
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

## The test (corrected after a vacuous first pass)

A candidate provides a per-block **energy scale** `E₀^λ` as a function of the
partition λ **only** (substrate-derived, parameter-free). The prediction is

> `M(particle) = C · Σ_λ E₀^λ · m^λ(particle)`

where `m^λ(particle)` is the genuine per-block **structural mass** from
`_deprecated/per_block_phi_q.mass_per_block` (the same object the deprecated
fit scales against). These structural masses differ across particles because
the braid words differ. **One** global positive constant `C` is permitted (it
is the overall MeV unit / m_e scale — not a per-block freedom). `C` is pinned
from the proton; the **electron and neutron residuals are the falsification
test**.

- **PASS** — one positive `C` fits e⁻, p, n within 1%.
- **LATENT-FIT** — nucleons fit but the electron (a different Hecke order)
  needs a separate scale (a hidden per-order parameter).
- **FAIL** — one `C` fails even on the nucleons, or `C ≤ 0`.

*(A first scoring pass compared a proton-pinned `C` to a neutron-pinned `C`
using identical per-block y_λ for both; that test reduced to "is m_p ≈ m_n?"
— trivially yes for every candidate, spread = m_n/m_p − 1 = 1.378e-3. It was
vacuous and is replaced by the cross-particle test above, which uses the
electron as the real discriminator.)*

## Candidate results

Run: `python3 computations/e0_lambda_tryall.py`
(witness: `e0-lambda-tryall.witness.json`). Residuals are relative; proton
is 0 by the pin.

| # | Candidate | E₀^λ {(3),(2,1),(1³)} | e⁻ resid | n resid | Verdict |
|---|-----------|------------------------|----------|---------|---------|
| 1 | Archimedean per-block (`VolDensity·χ^λ`) | 2121, 3216, −1722 | +929× | −0.78 | **FAIL** |
| 2 | q-dimension `dim_q(λ)` | 10.67, 8.26, 1.0 | +862× | −0.37 | **FAIL** |
| 2b | q-dimension² | 113.8, 68.3, 1.0 | +983× | −0.33 | **FAIL** |
| 3 | ρ_w energy functional (`Σ a_T²`) | 2.46, 2.58, 1.62 | +617× | −0.36 | **FAIL** |
| 4 | Casimir content-sum | 3, 0, −3 | +7363× | −0.0021 | **LATENT-FIT** |
| 4b | Casimir q-exp `q^{Σc}` | 1.368, 1.0, 0.731 | +726× | −0.29 | **FAIL** |
| 5 | Ribbon twist `θ_λ=q^{2Σc}` | 1.870, 1.0, 0.535 | +883× | −0.26 | **FAIL** |

**No candidate PASSES.** Candidate 4 (Casimir) is the only one whose per-block
shape happens to fit the **nucleons** (n residual 0.21%) with one C — but its
electron residual is +7363×, the largest of all. Every candidate's electron
residual is ~+600× to +7000×.

### Candidate-specific findings

- **1 — Archimedean.** `VolDensity(𝓑₃, q₀)` is a **single knot-level scalar**
  (`Vol(𝓑₃)/ℏ_q² × linking_weight`), with `m(K) = m_e·VolDensity(K)`. It has
  **no per-block decomposition** — the only per-block object in `_li_2_q_util.py`
  is the *exploratory* spectral correction, which reads one block's character
  χ^(2,1). So "VolDensity restricted to block λ" does not exist as a function of
  λ; the charitable reading `w_λ = VolDensity·χ^λ` fails.
- **3 — ρ_w energy functional.** This was the subtle one. The plain crystal
  trace `Σ_w ρ_w = χ^λ` (proved #1592) carries no new degree of freedom. We
  built a genuinely **non-linear** per-vertex functional `Σ_{T∈SYT(λ)} Σ_i a_{T,i}²`
  (L² of the seminormal eigenphases `a_T = h/(1−q^{−2ρ})`), which IS a different
  scalar from the linear trace. It still FAILS — the eigenphase energy is a
  function of λ only and so inherits the same mass-ratio blindness as every
  other per-partition quantity.
- **4 — Casimir.** Fits the nucleons (their per-block structural masses are
  nearly equal, since the p,n braids differ by one crossing), but is the worst
  on the electron — confirming the obstruction is the cross-Hecke-order bridge,
  not the within-nucleon split.

## Bottom line

**The substrate-derived χ^λ → M_λ map is not achievable from per-partition
data via any of the 5 candidates — and the obstruction is structural, not a
matter of finding a 6th construction.**

The reason is sharp and is the key finding of this probe:

> The electron's per-block structural masses (sym 1.57e8, std 4450, alt 4522)
> are **comparable in magnitude to the proton's** (sym 1.97e8, std 1.60e8, alt
> 1.57e8), yet `m_e` is **1837× lighter** than `m_p`. A per-block energy scale
> `E₀^λ = f(λ)` is, by construction, the **same function of λ for every
> particle**. So the only particle-dependent input is the per-block structural
> mass `m^λ(particle)` — and the electron/proton mass ratio is **not encoded**
> in the per-block (per-partition) data. It is encoded in the **braid word**:
> the number of strands (Hecke order n) and the crossing pattern. The
> per-partition projection (χ^λ, dim_q, content-sum, ribbon twist, seminormal
> eigenphases) **discards exactly the information that fixes the mass scale.**

This is precisely *why* χ^λ (a dimensionless trace over a fixed-n algebra)
does not determine `M_λ` (a dimensional MeV component): the missing dimensional
information is the Hecke-order / strand-count, which lives upstream of the
Wedderburn block decomposition. Any genuine χ^λ → M_λ map must therefore carry
an n-dependent (Hecke-order) scale — which is **not** parameter-free unless that
n-dependence is itself derived from the substrate. That derivation is the
Borromean-tower / brane-tower level-selection programme (GAP-A-3 / GAP-A-4),
**not** a per-partition closure ansatz, and it borders Subgoal-2 (the q₀-from-
substrate derivation the coordination ledger declined on 2026-05-08).

**Consequence for L2-Subgoal-1.** The gap does not close by finding the right
per-block energy functional — all five "obvious" candidates (archimedean,
q-dim, Casimir, ribbon, and even the genuinely-new ρ_w energy functional) are
mass-ratio-blind. The productive direction remains GAP-A-3/A-4 (categorical
brane-tower level selection) and Option E at the crystal level, **not** a 7th
per-partition fit. This is a negative result of the kind the Δ_λ-gate context
doc anticipated.

**Lean status.** Per the task discipline, NO candidate passed → **no Lean
identity is authored** (there is no parameter-free per-block energy identity to
state). The structural obstruction (per-partition data is mass-ratio-blind /
Hecke-order-blind) is documented here rather than formalised, since stating it
in Lean would require formalising the whole per-block-mass functor — out of
scope for this probe and bordering Subgoal-2.

## Files

- Harness: [`computations/e0_lambda_tryall.py`](../../computations/e0_lambda_tryall.py)
- Witness: [`computations/e0-lambda-tryall.witness.json`](../../computations/e0-lambda-tryall.witness.json)
- Anchor source (deprecated, read-only): `computations/_deprecated/per_block_phi_q.py`
- Substrate χ caches consumed: `chi-neutron-h3-at-q0-50dps.witness.json`, `chi-proton-h3-at-q0-50dps.witness.json`
