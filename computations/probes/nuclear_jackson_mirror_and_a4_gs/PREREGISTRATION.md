# Pre-registration: Thomae–Jackson Mirror-Nuclei Coulomb Ladder (`A = 3..17`) & `A = 4` GS Ordering (`qou-otet` / `NF-P3`)

Beans: `qou-qzvs`, `qou-otet`.
Written prior to evaluating any Thomae–Jackson mirror split or `A = 4` ordering energy.

## 1. Part 1 — Parameter-Free Thomae–Jackson Mirror-Nuclei Split (`A = 3, 7, 11, 13, 15, 17`)

### Fixed Derived / CAL-1/2/3 Inputs (Zero Tuned Parameters, Zero CODATA `alpha`)
- Proton substrate pin: `q_0 = q_at(80)`.
- Form-B Bring-surface derived coupling: `alpha_q(q_0) = (q_0 [9]_{q_0} [10]_{q_0} + 2 / (3 pi))^-1`.
- CAL-1 electron mass `m_e` (`M_E_MEV_STR`), QOU derived proton mass `m_p(q_0)` from the proton
  substrate identity, and CAL-3 pion mass proxy `m_pi = M_PI_PM_MEV_VALIDATION`.
- Proper-time UV floor `tau_0 = ln(q_0)`, Reeb mass gap `mu^2 = q_0 (q_0^2 - 1)`, geometric
  Thomae–Jackson lattice `tau_j = tau_0 * q_0^(2j)` (`j >= 0`).
- Out-of-sample `T = 1/2` mirror pairs `(Z_<, Z_>) = ((A - 1)/2, (A + 1)/2)` for
  `A in {3, 7, 11, 13, 15, 17}`, with normal-ordered proton-pair difference
  `Delta(Z(Z - 1)/2) = (A - 1)/2 in {1, 3, 5, 6, 7, 8}`.

### Pre-Registered Quadrature × Kernel × Recoil Branches (All Reported Side-by-Side)
1. **Quadrature steps on `tau_j = tau_0 q_0^(2j)`:**
   - `backward`: `Delta tau_j = (1 - q_0^-2) tau_j`
   - `symmetric`: `Delta tau_j = (2 (q_0^2 - 1) / (q_0^2 + 1)) tau_j` (and arithmetic mean
     `((q_0^2 - q_0^-2) / 2) tau_j`)
   - `forward`: `Delta tau_j = (q_0^2 - 1) tau_j`
   - `continuum_ref`: analytic `erfc(mu * sqrt(tau_0))` for comparison.
2. **3D Schwinger proper-time kernels:**
   - `normalized` (`int_0^infty = 1`): `K_norm(tau) = (mu / sqrt(pi * tau)) exp(-mu^2 * tau)`
   - `unnormalized` (`int_0^infty = 1/mu`): `K_unnorm(tau) = (1 / sqrt(pi * tau)) exp(-mu^2 * tau)`
3. **Constituent `SU(6)` / `SU_q(6)` magnetic recoil correction:**
   - `coulomb_only`: `1`
   - `with_su6_recoil`: `1 - (3/2) * (m_pi / (2 m_p(q_0)))^2` (`|mu_p / mu_n| = 3/2`, repulsive vs
     attractive magnetic contact sign both recorded: `(1 +- (m_pi / (2 m_p(q_0)))^2)`).
4. **Geometric `A`-scaling across `A = 3, 7, 11, 13, 15, 17` (zero fitted radius):**
   - `volume_R_A13`: `((A - 1)/2) * (3 / A)^(1/3)` (constant-density nuclear radius `R ~ A^(1/3)`
     anchored parameter-free to the single `A = 3` pair).
   - `unscaled_pairs`: `((A - 1)/2)` (no radius dilution).

AME2020 `Delta B = B(Z_<, A) - B(Z_>, A)` is read from `codata_constants.ame_binding_mev` strictly
for post-computation comparison; no branch is selected by residual.

## 2. Part 2 — `A = 4` (`^4He`) Pre-Registered Nucleon Ordering via Hecke GS Support / Length

Enumerate all `C(4, 2) = 6` linear chain orderings of `(p, p, n, n)`:
`ppnn`, `pnpn`, `pnnp`, `nppn`, `npnp`, `nnpp`.
Before reading AME2020 `B(^4He)`:
1. Compute exact interface bond counts `(n_pp, n_pn, n_nn)` (`n_pp`: pure `sigma`, 1 Hecke term;
   `n_nn`: `sigma^-1 = sigma - h`, 2 Hecke GS terms; `n_pn`: averaged `sigma - c_pn h`, 2 Hecke GS
   terms), total Hecke GS word-expansion term count across the 3 interfaces, and leading-`h` bond
   trace.
2. Evaluate exact 80-dps Convention-D `tr_M` and `B_log` across all 6 orderings to test whether
   minimal Hecke GS complexity selects block (`ppnn`/`nnpp`) vs alternating (`pnpn`/`npnp`).
