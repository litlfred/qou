# Pre-registration — route L: an ADDITIVE log-trace energy for β decay

Written 2026-11-21, before this probe computed anything. Bean `qou-99qc`. Owner selected route L
(derive an additive energy functional) after P1/P4 (#8681), P2 (#8680) and P3 (#8682) all met one
wall: the Markov-trace mass channel `E ∝ |tr|·[N]_q!/q^N` is multiplicative on split and
connected-sum words, so it is not an energy balance.

**Disclosure of what I had already seen.** Before writing this file I read the published P1 and P2
witnesses and audit notes, so I know several trace VALUES at q₀ (P2: tr(nuc11 p) ≈ 0.6293,
tr(nuc11 n) ≈ 0.4751, tr(σ₀³) ≈ 0.8485; P1: the bare-photon tr(W) and cross terms of W0–W7). The
log-energies below are arithmetic on those values, so the priors that concern them are not blind.
The priors that are blind are the structural ones (PR1–PR4).

## Corpus position (grep, before computing)

* The additive log-trace functional **already exists** in the corpus as the binding channel:
  `B_sym = α·ln(tr_free/tr_atom)`, α = E₀ = m_e/(q₀(q₀−1)) (CAL-1 scale), additive over chain bonds
  (`QOU.BraidKnot.BsymLinearChain`, `QOU.Mass.ChainTraceFactor.neg_log_prod`,
  `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md`). Sign: B = −α·log μ, i.e. a state
  energy E = +α·log tr.
* Its free-energy reading has no energy spectrum (`QOU.Mass.FreeEnergyReadingIsSigned`): the
  identification "α·L is an energy" is named, not derived.
* The volume conjecture enters the corpus only as τ-side naming of Vol(4₁)
  (`skein-mass-relation-proof`: "not a derivation input"). It is a statement about coloured Jones
  at e^{2πi/N}, N → ∞, not about the fundamental Markov trace at real q₀.
* Owner ruling 2026-09-05: the Q_β scale E₀ is the tower-summed form E₀/(1 − ℏ_q²).

## Definitions (fixed now)

* `tr` = Ocneanu–Markov, convention D, z = q³/(q²+1), tr(1) = 1. No `[N]_q!/q^N` strand factor
  (that factor is not multiplicative under disjoint union: [N₁+N₂]! ≠ [N₁]![N₂]!, so it would destroy
  additivity; dropping it is part of the route, stated).
* `E_κ(X) := κ·log|tr X|`. Cross term of a word W built from pieces X_i:
  `C_log(W) = log|tr W| − Σ log|tr X_i| = log|tr W / Π tr X_i|`.
* Decay balance: `Q/κ = log|tr(initial)| − log|tr(final)|`, final = p ⊗ e⁻ ⊗ ν̄ (split) or the
  entangled word itself.

## Outputs

1. Lean (sorry-free): log|tr| additive on any pair for which tr is multiplicative; instantiated on
   the unconditional one-strand law `tr_mul_adjoin_gen` and on the `TowerSpan`-conditional disjoint
   law; the cross-term formula; P3's χ-ratio log = 2 ln q; and the sign lemma below.
2. Exact (ℚ(q)) ratios `tr W / Π tr` for P1 W0–W7 (bare photon Γ = 1) and P2 family D, their logs
   at the proton q₀ (70 dps), their q → 1 limits.
3. P2 decay balance with nuc11 p, n; e⁻ = σ₀³; ν̄ = identity strand.
4. κ: report Q for each corpus-supplied κ (E₀ order zero, E₀ tower-summed, each with both signs),
   and the κ each word would need for CODATA Q_β (comparison only). κ is never chosen by residual.

## Priors

* **PR1 (99 %)** log-additivity on split / one-strand words is a theorem; cross term 0 there.
* **PR2 (90 %)** the corpus does NOT derive κ; α = E₀ is a posited normalisation.
* **PR3 (90 %)** the volume conjecture cannot fix κ at real q₀ (wrong evaluation point and colour;
  log|J_N(q)| at real q > 1 grows like N², not N).
* **PR4 (95 %)** P3's sign problem survives the log: E = κ·log χ = κ·writhe·ln q gives p − n and the
  electron the same sign, so no κ of either sign makes p lighter than n and m_e > 0.
* **PR5 (not blind, 80 %)** on P2's words, E = κ·log tr with the corpus sign κ = +E₀ makes β⁻
  endothermic (Q < 0) and gives the electron negative energy; the opposite sign makes both
  orderings right, i.e. the corpus binding sign and the decay sign disagree.
* **PR6 (70 %)** P1 wrapping-word log cross terms are O(h⁵)–O(h⁶) at q₀, ≪ 1, so κ·C_log ≪ Q_β
  for κ ~ E₀ except W7.
