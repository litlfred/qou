# The EM (Coulomb) channel of binding: ranks 0, 1, 2 on the nucleus block — gap G3

Date: 2026-11-27. Bean: `qou-tcl3` (under `qou-myts`). Ledger: PR #9658,
`docs/audits/2026-11-27-term-completeness-ledger.md`, gap **G3**.
Lean: `QOU/Nuclear/CoulombIsospinChannel.lean` (generic field, sorry-free, lean-direct exit 0,
axioms `propext`, `Classical.choice`, `Quot.sound` only).
Module: `computations/coulomb_isospin_channel.py`.
Probe: `computations/probes/coulomb_isospin_channel/coulomb_isospin_channel_probe.py` (+ witness).

## 1. Result

The ledger says the binding formula had no `em` entry at level `3A`, and that the EM channel is
the two-body charge operator with ranks `r ≤ 2`, so its `T_z` dependence is `a + b·T_z + c·T_z²`.
The coefficients are derived exactly:

    Σ_{i<j} Q_i Q_j = Z(Z − 1)/2 = a + b·T_z + c·T_z²,      T_z = (Z − N)/2,
    a = A(A − 2)/8,   b = (A − 1)/2,   c = 1/2.

(`pairSum_of_idem`, `chargePairs_imme`.) With one EM pair weight `ε` the binding term is

    E_EM = ε·a + ε·b·T_z + ε·c·T_z²,     ε = 2 f · αħc / r_rms,

subtracted from a strong-only binding. `ε` is the EM channel's **own** scale, separate from the
strong map `E`, as the ledger requires.

| factor | status |
|---|---|
| `a, b, c` | **derived**, exact rationals in `A` (Lean) |
| ratios `b/c = A − 1`, `a/c = A(A − 2)/4` | **derived**; no length can move them |
| `f = 0.520011` | **derived**, pre-registered q-Hankel shape factor (PR #9665); not selected |
| `α` | derived from q₀, conditional on the Witten-κ Gram `sorry` |
| `r_rms` | **open**: no derived energy-to-length map (beans `qou-mbfv`, `qou-usft`) |

## 2. What else the Lean file gives

* **Quark level** (`quark_pairSum_split`, `proton_internal`, `neutron_internal`). On `n = 3A`
  strands the quark pair sum is the nucleon pair sum plus one internal term per nucleon. With
  the model charges `2/3, −1/3`, the unordered internal term is `0` for uud and `−1/3` for udd.
  So the total is `Z(Z − 1)/2 − N/3`. The `−N/3` is the nucleon's own EM self-energy: it is the
  `−1/3` that PR #9654 found for `m_n − m_p` (gap G1), and it does not enter inter-nucleon
  binding.
* **Rank split** (`imme_rank_split`, `rank_one_multiplet_sum`, `rank_two_multiplet_sum`). In a
  multiplet `T = d/2`, the rank-1 piece `b·T_z` and the rank-2 piece `c·(T_z² − T(T+1)/3)` both
  sum to zero over `T_z = −T..T`. The multiplet-average (rank-0) EM entry is therefore
  `ε·(A(A − 2)/8 + T(T + 1)/6)` (`em_rank_zero`). So the EM channel also contributes a
  `T(T + 1)` piece to the block term of gap G2; the G2 thread should not attribute all of the
  block dependence to the braid channel.
* **Mirror split** (`emEnergy_mirror`): `ε·(A − 1)·T_z`; at `A = 3` it is exactly `ε`
  (`emEnergy_mirror_A3`).

## 3. Numbers (conditional on the length)

The probe's exact checks all pass: the IMME identity for every `Z ≤ A ≤ 300`, the quark-level
split for `A ≤ 40`, and the multiplet averages for `2T ≤ 20`. With `f = (3/5)^{3/2}` and the
uniform-ball rms radius, the new module reproduces `coulomb_energy_mev` to 4e-71, so the
existing module is the uniform-ball special case of this one.

Mirror splits, using the only length the corpus has: the CAL-3 radius `λ̄_π·A^{1/3}`
(coefficient 1 selected, `A^{1/3}` assumed), converted to `r_rms = √(3/5)·R`. AME2020 enters
**only** in the comparison columns.

| pair | r_rms (fm, cond.) | model, q-Hankel f | model, ball | ΔB AME | err q-Hankel | err ball | r_rms AME would need |
|---|---|---|---|---|---|---|---|
| ³H/³He | 1.579 | 0.948 | 0.847 | 0.764 | +24.1 % | +11.0 % | 1.961 |
| ⁷Li/⁷Be | 2.095 | 2.145 | 1.917 | 1.644 | +30.4 % | +16.6 % | 2.732 |
| ¹¹B/¹¹C | 2.436 | 3.074 | 2.748 | 2.764 | +11.2 % | −0.6 % | 2.709 |
| ¹³C/¹³N | 2.575 | 3.489 | 3.119 | 3.003 | +16.2 % | +3.9 % | 2.992 |
| ¹⁵N/¹⁵O | 2.701 | 3.881 | 3.469 | 3.537 | +9.8 % | −1.9 % | 2.964 |
| ¹⁷O/¹⁷F | 2.816 | 4.255 | 3.803 | 3.543 | +20.1 % | +7.3 % | 3.382 |
| ³⁹K/³⁹Ca | 3.714 | 7.662 | 6.848 | 7.307 | +4.9 % | −6.3 % | 3.894 |
| ⁴¹Ca/⁴¹Sc | 3.776 | 7.932 | 7.089 | 7.278 | +9.0 % | −2.6 % | 4.115 |

How to read it:

1. **The ball looks better, and that is not evidence for the ball.** The q-Hankel f is derived
   and pre-registered; the ball is an assumed shape. Under the no-fitting rule a derived term
   with a larger miss ranks above an assumed one with a smaller miss. The ball's apparent
   advantage is two errors cancelling: an assumed shape 11.9 % low against a selected length
   that is too short.
2. **The miss is the length.** The last column is the `r_rms` that AME would need at the derived
   f. At `A = 3` it is 1.961 fm, and the measured ³He charge radius is 1.966 fm (the −0.27 %
   that PR #9665 reported). The CAL-3 length is 19.5 % short there and 4.6 % short at `A = 39`.
   So the error is in `A^{1/3}` and the selected coefficient, which the module already flags,
   not in the charge structure or the shape.
3. **Nothing was selected against the target.** f is the pre-registered primary; the length is
   the existing labelled CAL-3 one; the AME-implied radius is printed as a diagnostic and used
   nowhere.

## 4. What is not done (named summands)

* **The length `r_rms`.** Open. It needs the energy-to-length map shared with G1 (`qou-mbfv`).
* **Exchange and correlation.** The single `ε` is the Hartree reading (one spatial pair weight
  for every proton pair). Pair-isospin-dependent weights give the three ranks separate
  weights. That residual is named here, not parametrised.
* **Double counting with the strong bond.** The thread on the Q_β ladder sign measured that the
  mass-table bond term carries a `T_z`-odd slope `α·ln(f_pp/f_nn)` of −1.563 MeV per n→p swap
  (`BondChannelTzParity`; probe `composite_beta_sign_decomposition_probe.py`). A strong
  channel should be rank 0 (ledger, `braid_rank_zero`), so that slope is charge asymmetry in
  the wrong channel. Subtracting `E_EM` from a binding that still carries it would count the
  `T_z` dependence twice. Wiring this term into production binding therefore goes together with
  removing that slope.
* **Production wiring.** The scorecard's binding columns are still strong-only, and the
  dashboard reports `E_C` beside them rather than subtracting it. Changing that is an owner
  decision (asked on a card in the thread); this PR adds the term and its exact structure.

No measured value enters any proof. AME numbers appear only in §3's comparison columns.
