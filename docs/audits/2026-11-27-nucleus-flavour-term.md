# The flavour term of an A-nucleon nucleus (ledger gap G4)

Date: 2026-11-27. Beans: `qou-tcl4` (gap G4), `qou-myts` (accuracy epic).
Ledger: `docs/audits/2026-11-27-term-completeness-ledger.md` (#9658), §5 row G4.
Lean: `QOU/Nuclear/NucleusFlavourTerm.lean` (commutative ring / integral domain, no measured value);
`QOU/Transcendental/Nuclear/NucleusFlavourTermLog.lean` (the `Real.log` instance only).

## 1. Short answer

The flavour column of the ledger at level `3A` is closed with **no new coefficient**. For a
nucleus of `A` disjoint nucleon blocks with `Z` protons and `N` neutrons,

    M_flav(Z, N) = M₀ − Z·δ,     equivalently     M_flav = (M₀ − A·δ/2) − δ·T_z,   2T_z = Z − N,

where `δ = 2E₀·log q` is the nucleon `K`-weight cell (ruling A, framing-corrected trace) and
`M₀ = −E₀·log ∏ᵢ τ_n(Xᵢ)` is the mass reading of the all-neutron tagging. `M₀` holds every
isoscalar piece (the braid entries and any flavour rank-0 piece together); this reading does not
separate them. The whole `Z`-dependence is the flavour rank-1 term. So:

* the rank-1 flavour entry `(flavour, T, r = 1)` has reduced coefficient `δ` on **every** block,
  the same number as the nucleon (`flavourMass_two_mul`);
* the term depends only on `Z`, not on which blocks are protons (`flavourMass_isobar`);
* one β⁻ step along an isobar, `(Z, N) → (Z+1, N−1)`, lowers the flavour mass by exactly `δ`,
  at every `A` (`flavourMass_beta_step`; with `Real.log`, `flavourMass_beta_step_log`). This is
  the flavour piece of `Q_β`, equal to the free-neutron value;
* the second difference along an isobar is zero (`flavourMass_second_difference`). Flavour is
  rank 1 only and supplies no isobaric parabola. The `T_z²` term must come from `em` rank 2 (G3)
  and the block-dependent braid coefficient (G2).

## 2. Derivation

1. **Blocks multiply.** The `K`-weight is grouplike (`Δ(K) = K ⊗ K`), so the weight of a tagging
   `c : Fin A → {p, n}` on `3A` strands is the Kronecker product of the per-block weighted
   projectors. For a product of disjoint block elements the weighted trace is then the product of
   block traces: `kronPi_mul`, `trace_kronPi`, `tauNuc_eq_prod` (any `A`, any commutative ring).
2. **The nucleon cell on each block.** Each block satisfies `τ_p = q²·τ_n`. This is the input: the
   exponent 2 is forced by the Markov condition (`NucleonSplitFullTower.markov_forces_K`), and
   #9663 proves that flavour-typed letters of every γγ word `Vᵏ` give a factor exactly 1 on top
   (`typed_V_pow_tau_ratio`, raw and corrected). Hence `τ(c) = q^{2Z}·∏ τ_n(Xᵢ)` (`tauNuc_eq_pow`).
3. **Mass reading.** With `M = −E₀·ℓ(τ)` for any logarithm-like `ℓ` (the reading of
   `gibbs_split_full_tower`), `M(c) = M₀ − Z·2E₀·ℓ(q)` (`flavourMass_eq`). Over a generic field
   `ℓ` is a hypothesis (`LogLike`); `Real.log` is supplied only in `QOU/Transcendental/`.

## 3. Effect on Q_β along isobars

`Q_β⁻ = M(Z, N) − M(Z+1, N−1) − m_e`. The flavour summand contributes `+δ` to every such
difference, the same at every `A` and in every multiplet. It shifts all isobaric `Q_β` by one
constant and cannot by itself make a composite transition exothermic or endothermic in a
`T_z`-dependent way: the curvature that selects the stable isobar is G2 + G3.

No number is computed or compared here. The numeric value of `δ` (0.8735 / 0.8822 MeV for order-
zero / tower `E₀`) is that of `docs/audits/2026-11-27-nucleon-split-full-tower.md` and is not used
in any proof.

## 4. Relation to formulas on record (do not double count)

* **Closed form** `tr_M(𝓑_K) = τ_p^Z τ_n^N ∏ f_i` (`computations/closed_form_tau_M.py`) is already
  linear in `Z` through `τ_p^Z τ_n^N`. Its `τ_p`, `τ_n` come from two different words (its
  docstring: `τ_p = 1.14576`, `τ_n = 0.98774`), not from the `K`-weight cell, so its per-nucleon
  ratio is not `q²`. The derived rank-1 flavour term **replaces** that ratio by `q²` on one word;
  it is not added on top. Swapping the ratio is a separate change to the producer, not made here.
* **Chain bond layer** (sibling thread "Fix the Q_β ladder sign", probe
  `composite_beta_sign_decomposition_probe.py`): the `pp/pn/nn` junction volumes form an exact
  arithmetic progression, so the bond term `α·ln(f_pp/f_nn)` is also linear in `Z`. It is a
  two-strand interface term between blocks, i.e. the word axis (G5), not the one-body flavour
  entry. The `K`-weight cell must be counted once per nucleon block, and the bond term, if kept,
  is a separate interface summand whose rank-1 coefficient is unruled. Counting `δ` both in a
  per-swap `m_n − m_p` line and again inside `τ_p/τ_n` would double count it.

## 5. Scope and what is not claimed

* **Disjoint blocks.** Interface letters between nucleon blocks make the block sum element-
  dependent (`nucleon-split-full-tower` §3), and the nuclear interface word is not ruled (#7876).
  That is the word axis G5, outside the ledger. Within it, the result holds for every block
  element that satisfies the nucleon cell.
* **Ruling A** fixes the trace as framing-corrected; the result needs only `τ_p = q²·τ_n` per
  block, which #9663 proves under both readings, so it does not depend on that choice.
* The identification of the flavour term with the ledger entry `(flavour, T, r = 1)` uses
  `2T_z = Z − N` and the Wigner–Eckart reading of the ledger; the Clebsch–Gordan input cited
  there is not proved here either.

## 6. Ledger update (G4)

| entry | before | after |
|---|---|---|
| `(flavour, T, r = 0)` at level `3A` | missing | folded into the isoscalar `M₀ − A·δ/2` with the braid entries; not separated by this reading |
| `(flavour, T, r = 1)` at level `3A` | missing | `−δ·T_z`, coefficient `δ` on every block, derived |

G4 is closed for disjoint blocks. G1 (EM rank 1 on the nucleon), G2, G3 and G5 are untouched.
