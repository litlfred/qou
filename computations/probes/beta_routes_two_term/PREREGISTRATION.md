# Pre-registration — the β-decay routes re-run under the covariant two-term trace

Written 2026-11-21, before any number in this directory was computed. Bean `qou-99qc`.
Owner (2026-11-21 04:57): update "the routes that you were trying" to use the TWO-TERM
Lagrangian trace. Every route below used only the one-term trace (convention-D Markov trace at
`z_D = q³/(q²+1)` = the quantum trace `Tr(K^{⊗N} ρ(X))/[2]_q^N`).

Routes re-run (their words copied verbatim from the branches, provenance in the probe):
P1/P4 (#8681, `beta_gs_reduction_n_gammagamma`), P2 (#8680, family D and the split words),
P3 (#8682, index character), route L (#8693, held by the owner; read-only), N2 (#8636).

## The two-term object (what is scored on `main`, and what is generalised here)

Scored on `main`: `two_term_covariant_all_pairs_qtrace` — the permutation-complete charge
insertion `Q_pair = Σ_{i<j} Q_i Q_j` (`Q_i` diagonal: `u ↦ +2/3`, `d ↦ −1/3`), projected onto
the braid-covariant commutant (#8552 T5/T6), connected part = minus its scalar part on the
weight space, quantum-trace weighted `Tr(K^{⊗N} · )/[2]_q^N`. On the nucleon weight spaces it is
0 (`deltaT_allPairs_connected_eq_zero`), so the scored two-term rows equal the one-term rows.

Generalisation to N strands with lepton strands (fixed now):

* **Strand charges.** Quark strand `Q = T³ + 1/6`; lepton strand `Q = T³ − 1/2` (`ν = u ↦ 0`,
  `e⁻ = d ↦ −1`). This is the P4/N2 "C-lep" convention (lepton strand = a second doublet in the
  same `V`), **an assumption carried over, not derived**. Photon-pair strands of P1/P4 have no
  derived charge: two colourings are reported, **A** (lepton) and **B** (neutral, `Q = 0`).
  Colouring **U** (every strand quark-type) is the uncoloured Hecke reading.
* **Covariant projection.** Each total-weight space `W_m` of `V^{⊗N}` is `H_N(q)`-invariant and,
  by quantum Schur–Weyl, multiplicity-free: `W_m = ⊕_λ S^λ` over two-row `λ`. The central
  idempotents `P_λ` are obtained by Lagrange interpolation in the full twist `Δ²` (eigenvalue
  `q^{2c(λ)}`, `c` = content sum), checked numerically to be idempotent, complete and
  eigen. `E(Q) = Σ_λ (tr(Q P_λ)/tr P_λ) P_λ` (the #8552 expectation, N strands).
* **Connected part.** `E(Q)^conn = E(Q) − (tr_{W_m} Q / dim W_m)·1` on each `W_m`.
* **Two-term coefficient.** `t₂(X) = Σ_m Tr_{W_m}(K E(Q)^conn ρ(X)) / [2]_q^N`; the two-term
  trace is `t₁ + c_em·t₂` with `c_em` NOT derived (its scale is a selection, #8524). Every row
  reports `t₂` and `t₂/t₁` (= d log t / d c_em at c_em = 0), so no scale is chosen.
* **Comparisons (labelled, never scored).** (i) raw connected `Q − scalar` without `E`
  (not braid-covariant); (ii) sector-connected (traceless on each joint eigenspace of the
  quark-block and lepton-block `T³`).

## Quantities per route

* P1: `t₁, t₂` of W0–W7, W4b, W1², W2b, W5 at the two photon points of #8681; cross term
  `R = t(W)/(t(β)t(Γ)t(bridge))` one-term, and its first-order two-term shift
  `δ log R = t₂/t₁(W) − Σ t₂/t₁(pieces)`.
* P4: sector traces `τ_{n⊗ν}`, `τ_{p⊗e⁻}` (K-weighted, dimension-normalised, as #8681) with the
  insertion `E(Q)^conn`; does the two-term term separate n from p where one-term did not (W0)?
* P2: `t₂/t₁` for p, n (nuc11), e⁻ = σ³, ν̄, and the 12 family-D words; two-term shift of
  `C = t(W) − t(p)t(e)t(ν̄)`.
* P3: the index character `χ` (trivial summand, weight space `u…u`).
* L: shift of `Q/κ = log t_n − log t_p − log t_e` and of each P1/P2 `C_log`, per unit `c_em`.
* N2: report which two-term quantity, if any, the reading-3 selection used.

## Priors (stated before computing)

* **PR1 (99 %).** Colouring U: `t₂ ≡ 0` for every word, every N — `Q_pair` is a polynomial in
  the total `T³`, hence scalar on every `W_m`. Scope (b), invariant: the pair-sum identity.
* **PR2 (97 %).** Sector-connected comparison ≡ 0 for every word and colouring (`Q_pair` is
  constant on each sector).
* **PR3 (95 %).** Raw connected (non-covariant) is non-zero on colourings A/B for every word,
  including the split W0 (it is a static sector reweighting, not an exchange term).
* **PR4 (70 %).** Covariant `E(Q)^conn` is non-zero for colourings A/B once N ≥ 2 contains a
  quark and a lepton strand, at order ≥ (q−1)¹; it vanishes at q = 1 (q = 1 isotypic projectors
  are S_N-symmetric, so `tr(T_l P_λ)/tr P_λ` is λ-independent).
* **PR5 (60 %).** In P4 the covariant two-term sector difference `n⊗ν − p⊗e⁻` is non-zero on W0
  (where the K-weighted one-term difference is 0).
* **PR6 (90 %).** P3 index character: two-term connected term 0 (one-dimensional space).
* **PR7 (85 %).** No route moves into agreement with CODATA `Q_β` by the two-term term without
  choosing `c_em`; the scale stays a selection.

CODATA appears only as a comparison row. Nothing is wired. No value is chosen by its residual.
