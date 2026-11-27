# Pre-registration: the down quark as a strand object, and what γγ production says about u and d

**Date:** 2026-11-27 · **Beans:** `qou-myts`, `qou-99qc` · **Branch:** `claude/nucleon-down-quark-strand-2026-11-27`
Written and committed before the probe was run.

## Questions (in this order)

1. **Owner, 2026-11-27:** *"what does γγ production say for u and d quarks. track full tower"*.
   What does the γγ construction (words built from the pair-production vertex `σᵢσᵢ₊₁⁻¹`, photon
   `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`, `GammaGammaWordSelection.lean`) force for the up strand, for the
   down strand, whether the two differ, and what it cannot reach — on every `H_n`, every `λ ⊢ n`.
2. Fork F1 of `2026-11-27-nucleon-down-strand-self-energy.md`: does the corpus make the down
   strand a different strand object from the up strand (up = unknot strand, owner ruling
   2026-11-20), so that a flavour self energy `θ_d ≠ θ_u` exists?

## Corpus facts fixed before computing

* `def:down-quark` (`knots-particles-confinement/down-quark.{md,lean}`): the down quark is the
  **same unknot** as the up quark (`down_quark_is_unknot`) with the **opposite crossing
  orientation** (`quark_crossing_asymmetry`). No distinct object, colour or twist is defined.
* Hecke `H_n(q)` has one strand type; the only one-strand datum is framing (a Markov stabilisation
  curl), and the only one-letter datum is the through-strand parity `q^{±1}`.

## Candidate family (enumerated, none chosen)

| id | down strand = | one-strand factor u / d | source |
|---|---|---|---|
| C0 | up strand (same object, same framing) | 1 / 1 | `def:down-quark` |
| CT | up strand, flavour = through-parity of its letter | `q` / `q⁻¹` | `gg_quark_letters_tl` |
| CM | up strand with one stabilisation curl, sign = orientation | `z_D` / `z̄_D` | Markov property, conv. D |

## Selection rule

γγ production (owner ruling `qou-ales`) plus confinement SDP reading 3 at the proton `q₀`.
A candidate is **forced** only if γγ+SDP assigns a different one-strand factor to u and to d.
**No candidate is selected or ranked by closeness to CODATA `m_n − m_p`.** If none is forced the
enumerated survivors are reported and the probe stops.

## Observable

`Δm = E·log(f_u/f_d)` (Gibbs map of PR #9475), at the proton `q₀`, for both `E₀` (order zero and
tower-summed, `qbeta_e0`). CODATA appears only in a final comparison column.

## Full-tower checks

* A: the two one-dimensional characters of `H_n` on every γγ word (exact, symbolic `q`); for
  `n = 3..6` and up to 4 vertices, which γγ words are pure braids and the signed crossing count
  of each strand (does γγ ever split strands into opposite-orientation classes?).
* B: exact `z̄_D = z_D − (q − q⁻¹)`, `z_D/z̄_D`, bar swap; the `K`-weighted partial trace
  (`NucleonSplitFullTower`) of `Ř` and `Ř⁻¹` on one pair.
