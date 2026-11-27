# When is a list of mass, binding or decay terms complete?

Date: 2026-11-27. Bean: `qou-myts` (accuracy epic), child bean filed with this PR.
Lean: `QOU/Nuclear/TermCompleteness.lean` (generic ring/field, no measured value).

Carl, 2026-11-27: *"how do we know that we have all the terms when doing mass/binding/decay
etc? we should be able to determine when we are complete, where to identify the gaps … are all
repn and characters covered? all partitions?"*

## 1. The answer in one paragraph

An observable on `n` strands (`n = 3A` quark strands for mass number `A`) is a finite sum over
an index set with three coordinates: the **block** (a two-row partition `λ = (n−k, k)` of `n`,
i.e. an isospin `T = (n−2k)/2`), the **tensor rank** `r` of the operator inside that isospin
multiplet, and the **channel** that supplies an operator of that rank. A formula is complete when
it has a term, with its own free coefficient, for every index entry. Then a gap is a missing
summand that can be named (`residual_eq_missing`), and each one is detected by a single test
vector (`complete_iff_no_residual`).

## 2. Why this index set and no other

**Blocks.** The convention-D trace gives weight `0` to every partition with three or more rows
(`TemperleyLiebTower.conventionD_kills_antisymmetriser`; at `n = 7, 8` in
`CrossNucleonPairWedderburnZRemoval`; the premise is `FibreDimensionForcesTL`). It gives every
two-row block the weight `[n−2k+1]_q/[2]_qⁿ`, which is strictly positive for `q > 1`
(`braid_block_weight_pos`, from `TemperleyLiebTower.yw_pos`). These weights sum to 1 at every
`n` (`TwoRowNormalisation.levelSum_eq_one`, `QDimNormalisation.qdim_normalisation_general`).
So, to answer "all partitions?": the partitions that must have a term are exactly the two-row
ones, and none of them may be dropped. The three-row ones are excluded by a proved invariant, so
leaving them out is not a gap. There are `⌊n/2⌋ + 1` of them (`card_blocks`), which grows
linearly in `n`.

**Characters.** Within a block, a trace needs the full character `χ_λ(β)` of the word. At
`n = 3` both live characters are in `WeightSpaceMarkov` (`χ₍₃₎`, `χ₍₂,₁₎`), and #9636, #9645
and #9650 show that the three weights `y₃`, `y₂₁` and `y₁₁₁ = 0` are traces of the central
idempotents `p₃`, `p₂₁` and `p₁₁₁`. So at `n = 3` every representation and every character is
covered. At `n = 3A` none of the production formulas evaluates a level-`3A` character (§4).

**Ranks (Wigner–Eckart).** The Hecke algebra acts as the commutant of `U_q(sl₂)` on
`V^{⊗n}` (Schur–Weyl). So every braid-word operator is an isospin scalar (rank `0`) and has the
same trace on every `T_z` sector of a multiplet. This is proved at `n = 3` for every word
(`braid_channel_has_no_np_split`, from `BlockChargeSectorTrace.sectorTrace_eq`; for two blocks,
`BlockSectorRestriction.readout_pp_eq_nn`). Any dependence on `T_z`, which covers `n − p`,
`Q_β` along an isobar and Coulomb, has to come from a non-scalar operator. A `b`-body operator
carries ranks `r ≤ b`, and a multiplet of isospin `T` supports only ranks `r ≤ 2T`. This gives
three channels:

| channel | operator | max rank | appears as |
|---|---|---|---|
| `braid` | convention-D trace of a braid word | 0 | the common mass of a multiplet, block by block |
| `flavour` | one-body `u`/`d` label | 1 | `b·T_z` |
| `em` | two-body `Σ_{i<j} Q_iQ_j` | 2 | `a + b·T_z + c·T_z²` |

With the EM row, the `T_z` dependence of a multiplet's mass is a polynomial of degree ≤ 2. This
is the classical isobaric-multiplet structure, derived here from the rank cap and not imported as
a phenomenological form. **Distinct entries carry independent reduced matrix elements**, so each
needs its own coefficient. In particular each needs its own energy scale.

**Scope.** The ledger certifies completeness *for a given word*. Which braid word represents a
nucleus (the chain versus a 3D plaquette) is a separate axis, and the ledger cannot see it. The
two known word-level facts are `ChainBindingNoSaturationPeak` and `AmeBindingNotPairwise`
(`b₃ ≠ 0`). The rank caps of `flavour` and `em` are encoded as data (`Channel.maxRank`) and are
not proved in Lean. That braid traces have rank 0 is proved at `n = 3` only.

## 3. The index set at the levels in use

| level | blocks (isospin) | entries | Lean |
|---|---|---|---|
| `n = 3` (one nucleon) | `(3)` T=3/2, `(2,1)` T=1/2 | 11 | `card_index_three` |
| nucleon block, rank 1 | — | **2**: `flavour`, `em` | `nucleon_rank_one_entries` |
| nucleon block, rank 2 | — | none (T = 1/2) | `nucleon_no_isotensor` |
| `n = 36` (A = 12) | **19** | — | `card_blocks_A12` |

## 4. Audit of the formulas on record

"Covered" means the formula has a term with a free coefficient for that entry.

### 4.1 Nucleon masses and `m_n − m_p`

* **Mass facade** (`canonical_mass`: `m_p = 2(m_μ F_Bor − 6m_e)`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`)
  covers the braid entries at `n = 3`, on both blocks, with full characters. With the flavour
  split `δ` (PR #690) it also covers `(flavour, T=1/2, r=1)`.
  **Missing: `(em, T=1/2, r=1)`** (`massFacade_misses_em`). This is the EM piece Carl asked
  about, and it is a named summand, not a residual.
* **`T³` weight-trace `Q_β` split** (conditional C1–C3) is trace-only. On one word its `n`−`p`
  split is identically `0` (`braid_channel_has_no_np_split`). The nonzero value it reports
  comes from giving `p` and `n` different words. In the ledger's terms, that choice is an
  isospin-breaking operator inserted by hand, and it can only realise one of the two rank-1
  entries.
* **PR #9654 (one scale for flavour and EM)** covers both rank-1 entries but ties their
  coefficients with one map `E`. The ledger says they are independent reduced matrix elements,
  so the tie is an extra relation the structure does not supply. That is why the forced ratio
  (85.8 against a literature 1.95–3.22, comparison only) fails. **What is missing is a second
  coefficient, not a second term.**

### 4.2 Binding

* **Closed form** `tr_M(𝓑_K) = τ_p^Z τ_n^N ∏_i f_i` (`closed_form_tau_M.py`) is trace-only.
  `ln tr` is linear in `Z`, `N` and the interface counts. At level `3A` the braid channel has one
  coefficient per block (`3A/2 + 1` of them, one per isospin). This formula has no dependence on
  the block, so it has no `T(T+1)` term.
  **Missing:** the block-dependent braid coefficients (the symmetry term), every `em` entry
  (Coulomb: no `Z²`-type term), and the `flavour` entries above `A = 1`.
* **Q-CLT proxy** (`try_binding_q_clt_proxy`) uses level-3 weights at every `A`. Its own caveat
  says so (audit 2026-05-25 `h3-vs-h3a`). It covers a level-3 ledger, reused `A` times. Level 3
  already misses blocks of level 6 (`level_three_misses_level_six`).
  **Correction to that caveat:** it says the correct level-`3A` sum runs over `p(3A)` partitions
  and is "infeasible beyond A ≈ 12 (p(36) ≈ 18,000)". Under convention D only `3A/2 + 1`
  partitions have nonzero weight: 19 at `A = 12`, not 17,977. The number of **summands** is
  small. The cost lies in evaluating each block's character, whose dimension is a ballot number,
  and that cost is real.

### 4.3 β-decay along an isobar

`Q_β = M(Z,N) − M(Z+1,N−1) − m_e` is a difference inside one isospin multiplet when `T` does not
change, and across neighbouring blocks otherwise. Every formula in §4.2 lacks the `T_z` entries
(`flavour` rank 1, `em` ranks 1 and 2) and the block dependence. So it has no isobaric parabola.
The scorecard's 0/1009 exothermic composite transitions is the measured face of these missing
entries.

### 4.4 α-decay

`Q_α = B_α − ΔB` (#9653). ΔB along the alpha line is one value (9.5366 MeV) on all 1,051 pairs,
because the binding law is linear along that line. Along the alpha line `T_z` is constant, so
the ledger's missing entries are the `em` rank-0 piece (it grows faster than linearly in `Z`)
and the block dependence. The 93 % inherited share in #9653 is the binding law's missing entries
showing through `ΔB`. The 7 % α-specific share is the `B_α` cell.

## 5. Gaps, as named summands

| # | missing entry | affects | how to close it (not done here) |
|---|---|---|---|
| G1 | `(em, T=1/2, r=1)` with its own scale | `m_n − m_p`, `m_n` | derive the EM reduced matrix element and its scale separately from `E` (#9654 says it is a different scale) |
| G2 | block-dependent braid coefficient at level `3A` (`T(T+1)`) | `B`, `Q_β`, `Q_α` | evaluate the convention-D trace block by block at level `3A`: `3A/2+1` blocks |
| G3 | `(em, T, r=0,1,2)` at level `3A` | `B`, `Q_β`, `Q_α`, mirror nuclei | two-body charge operator on the nucleus block; IMME form follows from the rank cap |
| G4 | `(flavour, T, r=1)` at `A ≥ 2` | `Q_β` | the one-body `δ` lifted to the nucleus block |
| G5 | word axis (chain → 3D plaquette) | `B` at `A ≥ 5` | outside the ledger; see `AmeBindingNotPairwise` |

No value in this audit enters a proof. The model numbers quoted come from the PRs and the
scorecard that are cited. The literature ratio in §4.1 is a comparison only.
