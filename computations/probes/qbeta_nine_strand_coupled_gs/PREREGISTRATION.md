# Pre-registration: 9-Strand Left-Coupled γγ Pair + Nucleon Hecke GS Probe (`qou-gtv6` / `NF-P1`)

Beans: `qou-qzvs`, `qou-gtv6`.
Written prior to evaluating any 9-strand trace, `q -> 1` limit, or MeV observable.

## 1. Question Tested

Isolated 3-strand nucleon `V^3 = (sigma_0 sigma_1^-1)^3` gives scored `Q_beta / m_e = R(q)` with
`R(1) = 3/4` and `R(q) <= 3/4` for all `q > 1` (`QOU.QBeta.QBetaErrorBudget`), giving
`Q_beta(q_0) = 0.325433929... MeV` (`2.404x` below empirical `0.78233 MeV`; `2.04x` at `q -> 1`).
Meanwhile:
- `QOU.QBeta.GammaGammaPairReduction` proved the 6-strand `gamma-gamma` pair word
  `W_pair = V_0 V_1 V_2 V_0 V_3` reduces by braid relations alone to the 4-letter normal form
  `sigma_0^2 sigma_1^-1 sigma_4^-1` (`ell_min = 4`, cancellation count `3`), with no nucleon strand.
- `QOU.QBeta.WeightedTraceSide` proved that closing a crossing's **left** strand with weight
  `K = diag(q, q^-1)` leaves the non-scalar Cartan operator `diag(q^2 + 1 - q^-2, 1)` on the right
  strand (breaking `NucleonWeightSpaceTraces.trace_word_eq`), whereas closing a right strand leaves
  only the scalar `q^2`.

This probe places the 6-strand `gamma-gamma` pair on strands `0..5` **to the left** of the 3-strand
nucleon `V_nuc^3 = (sigma_6 sigma_7^-1)^3` on strands `6..8` (`n = 9` strands total), reduces the
left-coupled words exactly over `Q(q)` in `H_9(q)` / `(C^2)^{otimes 9}`, and evaluates all
pre-registered readouts at `q -> 1` and at the proton pin `q_0 = q_at(80)`.

## 2. Pre-Registered 9-Strand Word Family (Zero Tuned Parameters)

### Left 6-strand `gamma-gamma` pair block (`strands 0..5`)
1. `pair_std`: `W_pair = V_0 V_1 V_2 V_0 V_3` (`equiv sigma_0^2 sigma_1^-1 sigma_4^-1` in `B_6`,
   touching strand `5` via `sigma_4^-1`).
2. `pair_rev`: `W_pair_rev = V_3 V_2 V_1 V_3 V_0` (strand-index reflection `i -> 4 - i` on `B_6`,
   `equiv sigma_4^2 sigma_3^-1 sigma_0^-1`, placing the `sigma_4^2` clasp adjacent to strand `5`).
3. `bare_spectator` (control): identity `1` on strands `0..5` (isolating the single boundary
   crossing on strand `5` from the internal `gamma-gamma` letters on `0..4`).

### Boundary coupling `C_{5,6}` between left block (`strand 5`) and nucleon (`strands 6..8`)
1. `C0_uncoupled`: `1` (control: must factorize identically).
2. `C1_pos`: `sigma_5` (single positive crossing).
3. `C2_neg`: `sigma_5^-1` (single negative crossing).
4. `C3_clasp`: `sigma_5^2 = 1 + (q - q^-1) sigma_5` (2-crossing pure-braid clasp, `C_{5,6}|_{q=1} = 1`).
5. `C4_vertex`: `V_5 = sigma_5 sigma_6^-1` (chiral 4th-term `gamma-gamma` vertex across boundary).

Right-placement control (`right_C1_pos`): nucleon on `0..2`, `sigma_2`, `W_pair` on `3..8`, verifying
`WeightedTraceSide.rightTrace_R` scalarization (`q^2` times uncoupled).

## 3. Pre-Registered Readouts (Evaluated Symbolically Over `Q(q)` and at 80 dps at `q_0`)

Let `eps_p^(9)(W)` and `eps_n^(9)(W)` be the Convention-D quantum traces `[2]_q^-9 Tr(K^{otimes 9} W)`
restricted on strands `6..8` to the 3D proton weight space `W_p` (`uud`, `K^{otimes 3} = q`) and 3D
neutron weight space `W_n` (`udd`, `K^{otimes 3} = q^-1`), with `tau_left = tau_D^(6)(W_left)` and
`E_0^full / m_e = 1 / (q (q - 1) (1 - (1 - q^-1)^2))`:

- **F1 (`R_raw`)**: `E_0^full / m_e * |eps_n^(9)(W) - eps_p^(9)(W)|` (unconditioned 9-strand split).
- **F2 (`R_cond`)**: `E_0^full / m_e * |eps_n^(9)(W) - eps_p^(9)(W)| / |tau_left|` (conditioned on
  the 6-strand pair trace `tau_left`).
- **F3C (`Placement C`, `BetaVertexBudget.lepton_cancels_cell`)**:
  `E_0^full / m_e * |ln(tr_plain_n(W) / tr_plain_p(W))|`, where `tr_plain_{p,n}` divides out the
  nucleon `K^{otimes 3}` factor `q^{+-1}` cancelled by the `(nu, e^-)` weight step.
- **F3B (`Placement B`, `BetaVertexBudget.qbeta_B_lt`)**:
  `-E_0^full / m_e * ln(eps_n^(9)(W) / eps_p^(9)(W)) - 1` (signed, when `eps_n, eps_p > 0`).

## 4. Decision Criterion (No Selection, All Rows Reported)

- Every `(left_block, coupling)` combination and all four readouts are reported in full.
- Verify exact `B_9` / `H_9(q)` equality between unreduced `10`-letter `W_pair` and reduced
  `4`-letter `pairReduced` inside all coupled 9-strand words (`tolerance = 0` in `Q(q)`).
- Record honestly whether any parameter-free readout yields `R(1) > 3/4` or whether all pure Hecke
  couplings remain bounded away from empirical `Q_beta / m_e = 1.5310`. CODATA `Q_beta` appears
  strictly as a post-computation comparison column; nothing is tuned or selected.
