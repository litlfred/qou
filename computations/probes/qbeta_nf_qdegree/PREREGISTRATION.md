# P3 pre-registration: β-decay energy as a change of normal-form q-degree / Bruhat length

Bean `qou-99qc`. Owner (Carl, 2026-11-20 20:52): β-decay is an interaction and a
Gröbner–Shirshov calculation; earlier he asked whether one side sits "at a higher q power".
P3, selected by the owner as a cheap diagnostic: read an energy off the change of a
normal-form q-degree or Bruhat length between the initial and final states of n → p e⁻ ν̄.

Written and committed **before** any invariant was evaluated on a nucleon or lepton element,
and before any q₀ or MeV number was computed. Not blind in one respect, disclosed here: I have
read PR #8632 (R3), which records that the quadratic-step count of (σ₁σ₂)⁵ is 25 leftmost-first
and 30 rightmost-first, and the corpus forms of B_p, B_n (short typed-crossing model, R3
probe), Δ_S = (h²/2, −h/2, −h/2, 0, 0, 0), and the γγ base V³ (PR #8586 audit). I have not
evaluated any invariant below on any of them.

## Corpus-grep (paths 1–6), summary

- `predicted-spectra/beta-decay-skein-properties.md` is the only corpus rule that reads an
  energy off a rewrite count ("the 7 re-reduction crossings change the R2 step count between
  parent and daughter normal forms. This dominates the Q-value"). R3 (#8632) showed the count is
  rewrite-order dependent and the scale is convention-C. No other energy-from-length,
  energy-from-q-degree, or crossing-budget energy rule was found in `folio/`, `computations/`,
  `docs/audits/`, beans.
- The length-weighted map T_w ↦ q^{ℓ(w)} appears in the corpus only as the trivial (index)
  character χ_(n) of H_n(q) (`spectral-decomposition-qvalue-*`, `h3-frobenius-casimir-markov-trace-proof`,
  `convention-d-kills-antisymmetriser-proof`), never as an energy.

## Objects (all in H_n(q), σ² = hσ + 1, h = q − q⁻¹, basis T_w, w ∈ S_n)

- N_S(p) = σ₁σ₂ − (h/2)σ₁, N_S(n) = σ₁σ₂ − hσ₁ − (h/2)σ₂ + h²/2 (short model; n − p = Δ_S).
- N_L(p), N_L(n): the 11-letter typed-crossing words of `pyhecke.atom.nucleon_word_letters`
  (default "borromean" order), symbolic q.
- V³ = (σ₁σ₂⁻¹)³ = β_Bor core: the γγ-selected element, the same for p and n.
- Leptons: e⁻ = trefoil σ₁³ in H₂ (corpus lepton), alternative γγ coordinate e⁻ = σ₁σ₂σ₁ in H₃
  (#8638 note); ν̄ = the smoothing, the unit 1.

## Invariants (functions of the T_w coefficient vector only)

1. ℓ_lead(x) = max{ℓ(w) : c_w ≠ 0} (leading Bruhat length).
2. ℓ_min(x) = min{ℓ(w) : c_w ≠ 0}.
3. q-degree span of the coefficients: deg⁺ = max_w maxdeg_q c_w, deg⁻ = min_w mindeg_q c_w.
4. χ(x) = Σ_w c_w q^{ℓ(w)} (length-weighted functional) and its q-degree range.
5. N(x) = Σ_w |c_w(q₀)| q₀^{ℓ(w)} (length-weighted norm, proton pin, 70 dps).
6. |supp x|.

For a final state p ⊗ e⁻ ⊗ ν̄ on disjoint strands: ℓ and q-degrees add, χ and N multiply.
Δ := final − initial for additive invariants; log_q of the ratio for χ, N.

## Predictions (stated before computing)

P-a. Every invariant above is rewrite-order independent, because it is a function of the
     coefficient vector in the T_w basis and that vector is unique. Lean: the left-regular
     σ₁, σ₂ action on Fin 6 → R satisfies the quadratic and braid relations, so every rewrite
     sequence of a word ends at one vector. Contrast: the quadratic-step count is not a
     function of that vector (R3: 25 vs 30 on one word).
P-b. χ is an algebra homomorphism (the index character χ_(n)), χ(σ) = q, χ(σ⁻¹) = q⁻¹, so on a
     braid word χ = q^{writhe}. Hence on the γγ base V³ (writhe 0) χ = 1 for both nucleons.
P-c. On V³, every invariant gives Δ_nucleon = 0 (same element for p and n). Any non-zero Δ
     then comes from the lepton alone: Δℓ_lead = ℓ_lead(e⁻) = 1 (trefoil in H₂) or 3 (σ₁σ₂σ₁).
P-d. On the typed models, Δℓ_lead(nucleon) = 0 is expected (both nucleons reach the same top
     length); χ(n) − χ(p) is the χ_(3) value of Δ_S, non-zero.
P-e. No scale per unit q-degree is derived by anything here. The required scale
     κ = Q / Δ will be reported as a ratio to m_e against two reference values, the
     experimental Q-value 0.78233341 MeV and the scored cell 0.325434 MeV (#8586), as a
     comparison only. Not tuned, not wired.

## Pass/fail

The diagnostic "passes" (energy readable from a normal-form invariant with no chosen scale)
only if some invariant has Δ ≠ 0 for n → p e⁻ ν̄ **and** the required κ equals a corpus-derived
scale without selection. P-e predicts it does not.
