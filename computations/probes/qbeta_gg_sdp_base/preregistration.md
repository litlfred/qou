# qbeta_gg_sdp_base — pre-registration (committed before any number below is computed)

Beans `qou-ales` (owner ruling 2026-09-08: every canonical braid word is selected by
γγ construction + the confinement SDP at q₀, never by census) and `qou-vd7j`.
Session 2026-11-20, branch `claude/qbeta-gg-sdp-base-2026-11-20`.

## Rulings this applies, verbatim sources

- Selection: γγ words only (`QOU.Mass.GammaGammaWordSelection.GammaGammaWord`, products of
  vertices `σ_i σ_{i+1}⁻¹`).
- Confinement SDP = **reading 3** (owner 2026-09-12): `χ_λ(w) ≥ 0` on every block with
  `y_λ > 0` (`FrobeniusFeasible`). Whole word (owner 2026-09-13). At **every level of the
  tower** (owner 2026-10-11, option 3): a nucleon in `H_3`, `A` nucleons in `H_{3A}`.
- ε is the Markov trace at `z_D = q³/(q²+1)` (owner 2026-09-08); `Q_β = |ε(W_n − W_p)|·E₀`
  with `E₀ = qbeta_e0.canonical` (tower-summed, the 2026-09-03 full-tower ruling).

## Candidate sets (fixed now, not tuned)

- Nucleon (`p`, `n`), `H_3`: the γγ words of `H_3` are exactly `V^k`, `V = σ₀σ₁⁻¹`
  (`gammaGamma_inH3_eq_vertexPow`). `k = 0..10`, the bound of step 7 (`GammaGammaSelectionTen`).
  The γγ grammar on three strands carries no flavour index, so the `p` and `n` candidate sets
  are the same set; this is stated, not chosen.
- Two nucleons (`²H`, `pp`, `nn`), `H_6`: `W = V_L^a · V_R^b · B` with `V_L = σ₀σ₁⁻¹`,
  `V_R = σ₃σ₄⁻¹`, `a, b` ranging over the non-zero `H_3` survivors with `k ≤ 10`, and
  `B ∈ {none} ∪ {P^m : m = 1..6}` for the four interface placements of step 11
  (`P1 = σ₂σ₃⁻¹`, `P2 = σ₃σ₂⁻¹`, `P3 = σ₁σ₂⁻¹`, `P4 = σ₂σ₁⁻¹`). `P2`, `P3` are not γγ vertices
  in the `vertex i` sense (inverse on the first letter); they are carried as a control and
  reported separately. Every-level admissibility = reading 3 at `H_6` AND at `H_3` on each
  nucleon sub-word.

## Predictions (stated before running)

1. `H_3`: survivors are exactly `3 | k` (step 7, proved on `1 < q ≤ 10/9`).
2. `p` and `n` survivor sets are identical (no flavour in the grammar). Hence the cost-minimal
   selection (crossing count) gives `W_p = W_n = V³` and `Q_β = 0` exactly at every `z`.
3. Over unequal survivor pairs `Q_β ≠ 0`; I make no prediction of its size and will not rank.
4. vd7j: under convention D the net row is satisfiable (`1ᵀv ≠ 0`); the Gram-demand formulation
   `Gx = nf(W)` is infeasible for every γγ word because `⟨v, nf(W)⟩ = altChar(W) = 1 ≠ 0`.

## Discipline

mpmath only (≥ 60 dps), proton pin `Q_50_DIGIT_STR`, convention D. Nothing reads AME. CODATA
`Q_β` is read only after every `Q_β` value is fixed, as a labelled comparison column; it plays
no part in any selection. `m_e` (CAL-1) sets the MeV unit.
