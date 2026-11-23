# qbeta_gg_sdp_base — results (beans `qou-ales`, `qou-vd7j`; nothing wired, nothing re-scored)

Pre-registration `b3a70fdf25`, run 2026-11-20, 13/13 checks, 4 s wall, 60 dps, proton pin
`1.10997858275138…`, convention D. Probe `qbeta_gg_sdp_base_probe.py`, witness
`qbeta-gg-sdp-base.witness.json`. Lean `QOU.QBeta.GammaGammaSdpQBetaBase` (8 declarations,
no `sorryAx`).

**Correction to the pre-registration.** It called `P2 = σ₃σ₂⁻¹` and `P3 = σ₁σ₂⁻¹` the non-γγ
placements. By `vertex i = [(i,+),(i+1,−)]` the γγ vertices are `P1 = σ₂σ₃⁻¹` (vertex 2) and
`P3 = σ₁σ₂⁻¹` (vertex 1); `P2` and `P4` are not. The probe uses the right labels
(`bond_is_gg_vertex`). No verdict depends on it: all four placements give the same pattern.

## Calibration (P0)
`τ(1) = 1`, `τ(σ₀) = z_D` (dev 7.8e-62), `τ(Δ_S)` equals the scorecard closed form
`q²/2 − q z_D − 1 + z_D/q + 1/(2q²)` (dev 6.8e-62), `χ_(2,1)(V³) = 2 − 3h⁴ − h⁶` (dev 9.3e-61),
and at `H_6` `y_λ > 0` exactly on the two-row shapes.

## `qou-vd7j` (P1 + Lean)
The over-determination diagnosis of 2026-08-02 was a convention-C fact. Under D the corpus
already measured (`frobenius_admissibility_net_row_probe`, witness on main): Gram rank 5,
`1ᵀv = 0.0902…`, so the net row is satisfiable whenever `Gx = nf` is. Lean now states both
halves: `net_row_satisfiable` (the net row is never the obstruction once `Gx₀ = nf`) and
`demand_infeasible_of_radical` (the demand fails iff the radical pairs non-trivially). Here
`χ_(1³)(V^k) = 1` for `k = 0..10`, so every γγ word's pairing is `1 ≠ 0`
(`gammaGamma_demand_infeasible_of_pairing_eq_altChar`; the identification pairing = alternating
character is a hypothesis in Lean, measured in the probe). **So the `Gx = nf` test admits no
γγ word, ever, and this is a statement about that test, not about the words.** The admissibility
test the owner ruled is reading 3, and that is what is run below.

## Per nucleus, every-level reading 3

| system | level(s) | candidates | survivors |
|---|---|---|---|
| p | H_3 | V^k, k = 0..10 | V³, V⁶, V⁹ (and the empty word) |
| n | H_3 | same set | same: V³, V⁶, V⁹ |
| ²H, pp, nn (identical words) | H_6 and H_3 per nucleon | V_L^a V_R^b B, a,b ∈ {3,6,9}, B ∈ {none} ∪ {P^m, 4 placements, m = 1..6}: 225 | 81: every (a, b) with B = none, P^3 or P^6, for all four placements |

The bond pattern repeats `3 | m` at every placement. Bond placement is not decided by reading 3
(step 11 found the same, in binding).

## Q_β on the ruled base, every ordered survivor pair (no ranking)

`Q_β = |τ_{z_D}(V^{k_n}) − τ_{z_D}(V^{k_p})| · E₀`, `E₀ = qbeta_e0.canonical` (tower-summed).
CODATA column read after all values were fixed.

| p | n | Q_β (MeV) | vs CODATA |
|---|---|---|---|
| V^k | V^k (any k) | 0 | −100 % |
| V³ | V⁶ (or reverse) | 0.0181999442 | −97.67 % |
| V⁶ | V⁹ (or reverse) | 0.0302156421 | −96.14 % |
| V³ | V⁹ (or reverse) | 0.0484155863 | −93.81 % |

The cost-minimal selection (crossing count, the corpus cost) is `p = n = V³`, so `Q_β = 0`
exactly (Lean `qbeta_delta_vanishes_of_frobeniusSelected`). Any non-zero value needs `p ≠ n`,
and nothing in the γγ grammar or reading 3 assigns which survivor is which nucleon; doing that
by Q_β would be selection against the target.

## Scope
(a): the γγ grammar applied alone on three and six strands. It agrees with `qou-99qc`'s
2026-11-15 synthesis (route 3: "the Hecke side cannot carry n vs p", invariant: PR #7975's
U_q commutation) and with `trace-flavour-no-go`. It does not exclude the ruling; it shows the
ruling needs a flavour ingredient this grammar does not contain.
