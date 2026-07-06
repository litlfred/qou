# Boiling / freezing temperatures from the q-ideal gas law (`q-PV = nRT`)

**Date:** 2026-06-10. **Status:** derivation plan (corpus-grounded; first
compute pending). **Owner directive:** "work on temperature questions… we
should use q-PV=nRT."

## The corpus already contains `q-PV = nRT`

The owner's `q-PV = nRT` is **`prop:quantum-ideal-gas-law`**
([`quantum-ideal-gas-law.md`](../../content/quantum-observable-universe/information-theory/quantum-ideal-gas-law.md),
`qou:QOU.Information.IdealKnotGas`):

$$
  P_q V_q \;=\; N\,T_q\Bigl(1 + \tfrac{\hbar_q^2}{[2]_q}\langle S_q\rangle\Bigr),
  \qquad T_q := \hbar_q = \tfrac{q-1}{q}\ \ (\text{def:quantum-temperature}).
$$

So the "where does q enter" fork (the A/B/C menu) is **already decided by the
framework**: it is **option C** — q acts on the thermal scale `T_q = ℏ_q` —
**plus** the entropy-anomaly correction `(ℏ_q²/[2]_q)·⟨S_q⟩` from `d_q² ≠ 0` at
`∂U`. The Boltzmann factor is the *ordinary* `e^{−β_q S_q}` of the categorical
action `S_q` (not a `exp_q`, ruling out A; `N` is the plain count, not `[n]_q`,
ruling out B). The single-particle partition function is
`z_q = Σ_{K∈Conf_p} e^{−β_q S_q(K)}`, `β_q = 1/ℏ_q`.

## The Kelvin bridge (no separate scale factor)

[`boltzmann-constant.md`](../../content/quantum-observable-universe/information-theory/boltzmann-constant.md):
in QOU natural units `k_B = 1`, and

$$
  k_B\,T_{\mathrm{phys}} \;=\; \hbar_q \;=\; \tfrac{q-1}{q}.
$$

Thermal energy per degree of freedom *equals* `ℏ_q`. Temperature is the Reeb
**tick rate** (`quantum-temperature-interpretation.md`), a holographic boundary
datum — entropy `S_q(U)` is a surface integral over `∂U`.

## Why a *variable* boiling/freezing point (no fit)

`T_q = ℏ_q` is **fixed** at `q_0`. So the molecule-to-molecule variation —
H₂O boils at 373 K, H₂S at 213 K — cannot come from `T_q`. It can come only
from the **molecule-specific categorical action of the hydrogen-bond network**,
`S_q(\text{H-bonds})`, which is read off the braid exactly as binding energies
are (bar-symmetric `Li_2^q` sector; cf. `covalent-bond-shared-trefoil`,
`ch4-lp-dual-binding`):

| molecule | H-bond network | expected `S_q(H-bonds)` | observed T_boil |
|---|---|---|---|
| H₂O | 4 tetrahedral H-bonds (`tetrahedral-hbond-directions`) | large | 373 K |
| H₂S | weak / few H-bonds | small | 213 K |
| HF | 2 strong H-bonds (chain) | large | 293 K |

A phase transition is the **liquid ↔ vapour free-energy crossing**
`F_q = −T_q ln Z_q` with `μ_liquid = μ_vapour`: thermal `k_B T` against the
H-bond cohesion `S_q`. Clausius–Clapeyron form, with the q-ideal-gas vapour and
the H-bond-network liquid:

$$
  k_B\,T_{\text{boil}} \;\approx\; \frac{E_{\text{HB}}}{\ln(P_0/P_{\text{amb}})},
  \qquad E_{\text{HB}} = \mathfrak{m}_e\cdot S_q(\text{H-bond network}),
$$

with `E_HB` the latent heat per molecule = the H-bond cohesion (for H₂O,
`L_vap ≈ 0.42 eV/molecule ≈ 2 × 0.21 eV` H-bonds). **Freezing** mirrors this:
the ordered ice lattice's q-residual entropy (`ice-pauling-residual`, Pauling
`ln(3/2)`) sets `T_melt` via the same free-energy crossing of the ordered phase.

## The single open quantity

Everything above is fixed by the existing corpus **except** the map

$$
  \text{H-bond braid} \;\longmapsto\; S_q(\text{H-bond network}),
$$

i.e. the categorical action of a *weak* `σ`-crossing (an H-bond) relative to a
covalent crossing. This is the one thing to compute from braid weights; it must
be **derived, not fitted** to reproduce 373 K / 273 K (anti-pattern guard from
`.beans/research-queue.json::research-boiling-freezing-temps-from-braid-hbond`).

## Concrete compute steps

1. **`S_q` of one H-bond.** Define the H-bond as a weak `σ`-crossing in the
   intermolecular braid; compute its categorical action `S_q` (Markov-trace /
   `Li_2^q` binding-sector value) relative to a covalent `σ`. Witness it.
2. **Per-molecule H-bond network.** H₂O = 4 tetrahedral (coordination from
   `tetrahedral-hbond-directions`); H₂S, HF, NH₃ from their VSEPR braids
   (`prop:symmetric-block-domain-weight`). `E_HB = Σ S_q` over the network.
3. **T_boil via the q-gas-law crossing.** Solve `μ_liquid = μ_vapour` with the
   q-ideal-gas vapour; convert to Kelvin via `k_B T_phys = ℏ_q`. Compare the
   *ratios* T_boil(H₂O)/T_boil(H₂S) first (ratios cancel the global scale and
   are the no-fit-cleanest test), then absolute K.
4. **T_melt via ice q-residual entropy.** `ice-pauling-residual` + the ordered-
   phase free energy.

## Deliverables (this tranche)

- `computations/hbond_categorical_action.py` (+ witness): step 1–2.
- `computations/phase_transition_q_ideal_gas.py` (+ witness): step 3–4.
- A content block extending `prop:quantum-ideal-gas-law` to molecular phase
  transitions (proposition or remark, with Lean where provable), once the
  `S_q(H-bond)` map is in hand and the ratios validate.

Report **tiered** (proved / near-match / fitted); if `S_q(H-bond)` cannot be
derived cleanly, report the transition temperatures as `tier=open`, never fitted.
