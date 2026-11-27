# The γγ lepton pair word reduces by braid-group relations only (W5)

Thread "β-decay Gröbner–Shirshov reduction", 2026-11-23. This is row W5 of the L2 1-ppQ plan.

- Pre-registration (committed before any computation):
  [`computations/probes/qbeta_gg_pair_gb/PREREGISTRATION.md`](../../computations/probes/qbeta_gg_pair_gb/PREREGISTRATION.md).
- Lean (lean-direct exit 0, no `sorryAx`):
  [`QOU/QBeta/GammaGammaPairReduction.lean`](../../folio/quantum-observable-universe/lean/QOU/QBeta/GammaGammaPairReduction.lean).
- Probe (20/20 checks):
  [`qbeta_gg_pair_gb_probe.py`](../../computations/probes/qbeta_gg_pair_gb/qbeta_gg_pair_gb_probe.py).

Photon (owner ruling 2026-11-20): γᵢ(φ₀, φ₁, φ₀₁) = 1 + φ₀σᵢ + φ₁σᵢ₊₁ + φ₀₁σᵢσᵢ₊₁⁻¹. The
vertex letter is Vᵢ = σᵢσᵢ₊₁⁻¹.

## The three questions and the answers

**1. Which word is the decay element, the unreduced or the reduced one?** Both, because they
are the same element. V₀V₁V₂V₀V₃ becomes σ₀²σ₁⁻¹σ₄⁻¹ through three free cancellations
σᵢ⁻¹σᵢ = 1 and two far commutations. The Hecke quadratic relation is never used.

- `pairWord_braidEq_reduced` proves the reduction.
- `eval_pairWord` proves the two words have the same value in every group whose elements satisfy
  the braid relations. The invertible Hecke generators form such a group for every q.
- So every trace, module action and energy that factors through the element gives the same
  value on both words.

Asking "unreduced or reduced" therefore does not choose between two elements.

**2. What does that make the 2E₀·ln q ≈ 0.873537 MeV cell?** Neither Q_β nor m_n − m_p, on
the strength of this reduction.

- The words have six lepton and photon strands and no nucleon strand.
- The reduction leaves exactly one q-independent number, the count of cancelled pairs.
- To turn that count into MeV you would need an energy per cancelled pair. The corpus derives
  no such quantity.
- Fixing one so that 3 × (energy per pair) hits a target would be a fit.

The cell needs a word that couples the pair to a nucleon, and the corpus does not fix that
word. It is an owner input.

This is a statement about what the reduction contains, not a refutation of the cell.

No MeV figure is produced here, so neither electron unit is used. The units are τ_e and
ℏ_q², which differ by about 70.4 (flagged from W6, PR #9165).

**3. Does any term survive at q = 1?** Not from the reduction. The difference between the
unreduced and reduced words is 0 for every q, including q = 1.

`QBetaErrorBudget.lean` proves R(q) ≤ 3/4 for q ≥ 1, so the missing factor of about 2.04 has
to survive at q = 1. It cannot come from the unreduced-versus-reduced choice.

Scope (b): the invariant is the braid-group identity. This holds for every functional that
factors through the braid group element.

## The cancellation count is a property of the braid

Let c_{ab}(w) be the signed number of crossings between strands a and b.

- Every braid relation leaves c_{ab}(w) unchanged (`run_invariant`).
- Each letter changes exactly one entry by ±1.
- So every word w for a braid has ℓ(w) ≥ Σ_{a<b} |c_{ab}|.
- The braid relations also preserve the parity of the length (`length_even`).

For V₀V₁V₂V₀V₃ the nonzero entries are c₀₁ = 2, c₁₂ = −1 and c₄₅ = −1, which gives a bound
of 4. The word σ₀²σ₁⁻¹σ₄⁻¹ has 4 letters, so the bound is attained.

A reduction to a shortest word therefore cancels (10 − 4)/2 = **3** pairs, whatever order it
cancels in (`cancellation_count`). The probe also tried 200 random cancellation orders per
word, and each one cancelled the predicted number of pairs.

| word | reduced | c (nonzero) | ℓ → ℓ_min | pairs cancelled |
|---|---|---|---|---|
| V₀V₁V₀ | σ₀σ₂⁻¹σ₀σ₁⁻¹ | 01: 2, 13: −1, 23: −1 | 6 → 4 | 1 |
| V₁V₂V₁ | σ₁σ₃⁻¹σ₁σ₂⁻¹ | 12: 2, 24: −1, 34: −1 | 6 → 4 | 1 |
| V₂V₃V₂ | σ₂σ₄⁻¹σ₂σ₃⁻¹ | 23: 2, 35: −1, 45: −1 | 6 → 4 | 1 |
| V₀V₁V₂V₀V₃ | σ₀²σ₁⁻¹σ₄⁻¹ | 01: 2, 12: −1, 45: −1 | 10 → 4 | 3 |
| V₀V₁V₂V₃V₀ | same braid | same | 10 → 4 | 3 |
| V₂V₀V₃V₁V₀ | same braid | same | 10 → 4 | 3 |
| V₂V₃V₀V₁V₀ | same braid | same | 10 → 4 | 3 |
| V₀V₁V₀V₁V₂ | σ₀σ₂⁻¹σ₀σ₃⁻¹ | 01: 2, 23: −1, 24: −1 | 10 → 4 | 3 |
| V₁V₂V₁V₂V₃ | σ₁σ₃⁻¹σ₁σ₄⁻¹ | 12: 2, 34: −1, 35: −1 | 10 → 4 | 3 |

Every prediction in the pre-registration held.

Four of the five-vertex words turn out to be **one braid**, σ₀²σ₁⁻¹σ₄⁻¹. These are the four
five-vertex words with the "Hopf photon × single crossing" factorisation of Round 12, §12.3 of
`2026-11-21-proton-q3-kl-coordinate.md` (two cells each). So those 8 factorising cells are
cells of one element.

The other two five-vertex words carry the "full twist × two negative crossings" pattern. Each
is a separate braid.

## What is checked where

- **Lean** proves the identity and the excess for V₀V₁V₂V₀V₃, and the identity for
  V₀V₁V₂V₃V₀.
- **The probe** checks every row. It confirms each reduction by equal Burau matrices over
  Q(t), plus equal crossing data and permutation. The Burau check is an independent check, not
  a proof of braid equality. For each row the reduction itself uses group relations only.

## What this does not settle

- **The decay element.** The nucleon–pair coupling word is not fixed, so the decay element is
  not fixed either.
- **Hecke-level reductions.** A reduction that does use the quadratic relation σ² = hσ + 1
  changes the element. That is the H₄ asymmetry work in §14–17 of the spectator audit, which is
  order- and word-dependent (scope (a)). It is not this question.
