# Pre-registration: $1p$-Shell Compton Harmonic-Oscillator Slater Coulomb Ladder on Mirror Nuclei $A = 3..17$ (`qou-otet`)

Beans: `qou-otet`, `qou-qzvs` (`L2 1-ppQ` Gate 3 follow-up on PR `#9204`).
Written and committed prior to evaluating any Compton harmonic-oscillator Slater Coulomb split against AME2020.

## 1. Fixed Derived & CAL-1/2/3 Inputs (Zero Fitted Parameters, Zero Empirical Radius)

- Proton substrate pin: `q_0 = q_at(80)` (`q0Anchor = "proton"`, `workdps = 80`, zero `float64`).
- Form-B Bring-surface derived electromagnetic coupling: `alpha_q(q_0) = (q_0 [9]_{q_0} [10]_{q_0} + 2 / (3 pi))^-1`.
- CAL-1 electron mass `m_e` (`M_E_MEV_STR`), QOU derived proton mass `m_p(q_0)` from the proton substrate identity, CAL-3 charged pion mass `m_pi = M_PI_PM_MEV_VALIDATION`.
- QOU derived Compton nuclear harmonic-oscillator constant (`knot-periodic-table.md` / `knot-centric-table.md` nuclear HO shell hierarchy):
  $$E_{\mathrm{osc}}(q_0) := \frac{m_e}{(q_0 - 1)^2}, \qquad \hbar\omega_0(A) := E_{\mathrm{osc}}(q_0)\,A^{-1/3},$$
  determining the parameter-free inverse oscillator length in natural units ($\hbar = c = 1$):
  $$b(A)^{-1} = \sqrt{m_p(q_0)\,\hbar\omega_0(A)} = \sqrt{m_p(q_0)\,E_{\mathrm{osc}}(q_0)}\,A^{-1/6}\;\text{(MeV)}, \qquad E_C^{(1s)}(A) := \alpha_q(q_0)\sqrt{\frac{2}{\pi}}\,b(A)^{-1}.$$
- Backward Thomae–Jackson proper-time UV damping factor from `#9204`:
  $$D_{\mathrm{back}}(q_0) = \mu \sum_{j=0}^\infty \frac{e^{-\mu^2 \tau_j}}{\sqrt{\pi \tau_j}}(1 - q_0^{-2})\tau_j \quad (\tau_0 = \ln q_0,\; \mu^2 = q_0(q_0^2 - 1),\; \tau_j = \tau_0 q_0^{2j}),$$
  with continuum reference $D_{\mathrm{erfc}}(q_0) = \mathrm{erfc}(\mu\sqrt{\tau_0})$ and constituent $SU(6)$ / $SU_q(6)$ magnetic recoil factor $R_{\mathrm{su6}-} = 1 - \frac{3}{2}\left(\frac{m_\pi}{2 m_p(q_0)}\right)^2$ vs `coulomb_only` ($1$).

## 2. Out-of-Sample $T = 1/2$ Mirror Pairs & Mayer–Jensen Spherical HO Configurations

By Elliott–Skyrme (1955), lowest-configuration spherical harmonic-oscillator two-body matrix elements $\langle nl, n'l' | V(|\vec{r}_1 - \vec{r}_2|) | nl, n'l' \rangle$ depend solely on relative coordinates and carry zero center-of-mass spuriousness:

| $A$ | Mirror pair | $(Z_<, Z_>)$ | Valence transition $Z_< \to Z_>$ | Direct $F^0$ sum added by $Z_>$ proton |
|---:|---|---|---|---|
| $3$ | $^3\mathrm{H}$–$^3\mathrm{He}$ | $(1, 2)$ | $1s_{1/2}^1 \to 1s_{1/2}^2$ ($J=0^+$) | $1\,F^0(1s, 1s)$ |
| $7$ | $^7\mathrm{Li}$–$^7\mathrm{Be}$ | $(3, 4)$ | $1s_{1/2}^2 1p_{3/2}^1 \to 1s_{1/2}^2 1p_{3/2}^2$ ($v: 1 \to 0$) | $2\,F^0(1s, 1p) + 1\,F^0(1p, 1p)$ |
| $11$ | $^{11}\mathrm{B}$–$^{11}\mathrm{C}$ | $(5, 6)$ | $1s_{1/2}^2 1p_{3/2}^3 \to 1s_{1/2}^2 1p_{3/2}^4$ ($v: 1 \to 0$) | $2\,F^0(1s, 1p) + 3\,F^0(1p, 1p)$ |
| $13$ | $^{13}\mathrm{C}$–$^{13}\mathrm{N}$ | $(6, 7)$ | $1s_{1/2}^2 1p_{3/2}^4 \to 1s_{1/2}^2 1p_{3/2}^4 1p_{1/2}^1$ ($v: 0 \to 1$) | $2\,F^0(1s, 1p) + 4\,F^0(1p, 1p)$ |
| $15$ | $^{15}\mathrm{N}$–$^{15}\mathrm{O}$ | $(7, 8)$ | $1s_{1/2}^2 1p_{3/2}^4 1p_{1/2}^1 \to 1s_{1/2}^2 1p^6$ ($Z=8$ closure) | $2\,F^0(1s, 1p) + 5\,F^0(1p, 1p)$ |
| $17$ | $^{17}\mathrm{O}$–$^{17}\mathrm{F}$ | $(8, 9)$ | $1s_{1/2}^2 1p^6 \to 1s_{1/2}^2 1p^6 1d_{5/2}^1$ ($N=2$ entry) | $2\,F^0(1s, 1d) + 6\,F^0(1p, 1d)$ |

## 3. Pre-Registered Branches Reported Side-by-Side (Zero Selection)

1. **`baseline_pr9204_vol_A13`**: `#9204`'s uniform $((A - 1)/2)(3/A)^{1/3} \alpha_q(q_0) m_\pi D_{\mathrm{back}}(q_0)$ (`coulomb_only` and `su6_minus`).
2. **`S1_ho_direct_F0_jackson_back`**: Exact spherical HO direct Slater integrals $F^0(nl, n'l'; b(A))$ $\times$ backward Thomae–Jackson $D_{\mathrm{back}}(q_0)$ (`coulomb_only` and `su6_minus`).
3. **`S2_ho_antisym_jj_seniority_jackson_back`**: Full antisymmetrized $jj$-coupled seniority Slater matrix elements (incorporating exact core-valence Pauli exchange $G^1(1s,1p), G^2(1s,1d), G^1(1p,1d), G^3(1p,1d)$ and $1p_{3/2}^n$ seniority pairing $F^2(1p,1p)$) $\times$ backward Thomae–Jackson $D_{\mathrm{back}}(q_0)$ (`coulomb_only` and `su6_minus`).
4. **`S3_ho_undamped_controls`**: Undamped ($D = 1$) direct $F^0$ and antisymmetrized $jj$-seniority Slater splits, isolating the exact numerical effect of backward Thomae–Jackson UV damping.

AME2020 $\Delta B = B(Z_<, A) - B(Z_>, A)$ from `codata_constants.ame_binding_mev` is read strictly for post-computation residual reporting (`before` vs `after` across $A = 3, 7, 11, 13, 15, 17$); nothing is fitted or selected.
