# Pre-registration: Non-Volume Frobenius/Schur Boson Mass Ratios on $T(2,4)$ / $T(3,5)$ & Tree-Level $\sin^2\theta_W$ (`qou-vexf`)

Beans: `qou-vexf`, `qou-qzvs` (`L2 1-ppQ` Gate 2 follow-up on PR `#9198` & `#9204`).
Written and committed prior to evaluating any $T(2,4)/T(3,5)$ mass ratio or implied $\sin^2\theta_W$ at $q_0$.

## 1. Fixed Substrate Inputs (Zero Fitted Parameters)

- Proton substrate pin: `q_0 = q_at(80)` (`q0Anchor = "proton"`, `workdps = 80`, zero `float64`).
- CAL-1 electron mass `m_e` (`M_E_MEV_STR`), Planck-like substrate denominator `hbar_q^2 = (1 - q_0^-1)^2` (cancelling identically in dimensionless boson mass ratios $M_W / M_Z$).
- Convention-D Markov parameter `z_D(q) = q^3 / (q^2 + 1)` (owner ruling R1, 2026-08-15; $U_q(\mathfrak{sl}_2)$ quantum trace on $(\mathbb{C}^2)^{\otimes n}$).

## 2. Pre-Registered Torus-Link / Torus-Knot Braid Carriers (`Vol = 0`)

Because hyperbolic volume vanishes identically on all torus knots and links (`WeakScaleFactorisation.volume_channel_gives_no_fermi_scale`), we evaluate all parameter-free algebraic Hecke–Frobenius–Schur functionals on:

1. **$W^\pm$ candidate $T(2,4)$ (2-component torus link, genus 1):**
   - 2-strand braid $\beta_{2,4} = \sigma_0^4 \in H_2(q)$ ($n = 2$, writhe $w = 4$).
   - 4-strand braid $\beta_{4,2} = (\sigma_0 \sigma_1 \sigma_2)^2 \in H_4(q)$ ($n = 4$, writhe $w = 6$, closing to the same topological link $T(4,2) \cong T(2,4)$ via two positive Markov stabilizations $\mathrm{tr}_M^D(\beta_{4,2}) = z_D(q)^2 \mathrm{tr}_M^D(\beta_{2,4})$).
2. **$Z^0$ primary gate candidate $T(3,5)$ (torus knot $10_{124}$, genus 4):**
   - 3-strand braid $\beta_{3,5} = (\sigma_0 \sigma_1)^5 \in H_3(q)$ ($n = 3$, writhe $w = 10$, `QOU.Braiding.WeakVertexT35.weakVertexTrace`).
3. **EW-triplet control candidate $T(2,6)$ (from `electroweak-higgs-torus-link-triplet` / `weinberg-angle-categorical`):**
   - 2-strand braid $\beta_{2,6} = \sigma_0^6 \in H_2(q)$ ($n = 2$, writhe $w = 6$).

Note on exact Convention-D $H_2(q)$ weights: $y_{(2)}^D(q) = [3]_q / [2]_q^2 = (q^4 + q^2 + 1)/(q^2 + 1)^2$ and $y_{(1,1)}^D(q) = 1/[2]_q^2 = q^2/(q^2 + 1)^2$, satisfying $y_{(2)}^D + y_{(1,1)}^D = 1$ and $q y_{(2)}^D - q^{-1} y_{(1,1)}^D = z_D(q)$.

## 3. Pre-Registered Non-Volume Frobenius / Higman / Schur Mass Functionals $\mathcal{M}_k(\beta)$

For $\beta \in H_n(q)$ (with common carrier prefactor $m_e / \hbar_q^2$ for absolute GeV scale, cancelling in $M_W / M_Z$):

- **M1 (`markov_raw`)**: $|\mathrm{tr}_M^D(\beta)| = \left|\sum_{\lambda \vdash n,\, \ell(\lambda) \le 2} y_\lambda^D(q) \chi_\lambda(\beta)\right|$.
- **M2 (`link_stabilized`)**: $|z_D(q)^{-(n-1)} \mathrm{tr}_M^D(\beta)|$ (Markov-stabilization invariant across $\beta_{2,4} \in H_2$ and $\beta_{4,2} \in H_4$).
- **M3a (`schur_triv_poincare`)**: $|\mathrm{tr}_M^D(\beta)| \cdot c_{(n)}(q)$, with trivial-block Poincaré/Schur element $c_{(n)}(q) = q^{\binom{n}{2}} [n]_q!$.
- **M3b (`schur_mass_channel_qfact_over_qn`)**: $|\mathrm{tr}_M^D(\beta)| \cdot ([n]_q! / q^n)$ (canonical non-volume mass-channel factor of `LogTraceAdditiveEnergy.lean`, alongside $c_{(1^n)}(q) = [n]_q! / q^{\binom{n}{2}}$).
- **M4 (`schur_irrep_weighted`)**: $\left|\sum_{\lambda \vdash n,\, \ell(\lambda) \le 2} c_\lambda(q) y_\lambda^D(q) \chi_\lambda(\beta)\right|$ (irrep-by-irrep Wenzl–Higman Schur weighting).
- **M5 (`frobenius_gram_l2`)**: $\sqrt{\mathrm{tr}_M^D(\beta^\top \beta)}$ (symmetric Frobenius Gram norm under $\sigma_i^\top = \sigma_i$, and its Poincaré-scaled partner $\sqrt{\mathrm{tr}_M^D(\beta^\top \beta)} \cdot c_{(n)}(q)$).
- **M6 (`log_action`)**: $|\ln |\mathrm{tr}_M^D(\beta)||$ (`skein-binding-lagrangian.md` logarithmic action).

## 4. Tree-Level Weinberg Ratio & Decision Criterion (No Selection)

For every carrier pair $(W, Z) \in \{(\beta_{2,4}, \beta_{3,5}),\, (\beta_{4,2}, \beta_{3,5}),\, (\beta_{2,4}, \beta_{2,6})\}$ and every functional $\mathcal{M}_k$:
1. Compute the exact $q \to 1$ rational/algebraic limit and the 80-dps value at $q_0$ of $R_k = \mathcal{M}_k(W) / \mathcal{M}_k(Z)$, $\cos^2\theta_W = R_k^2$, and $\sin^2\theta_W = 1 - R_k^2$.
2. Flag honestly any pair/functional with $R_k \ge 1$ ($\sin^2\theta_W \le 0$, unphysical $M_W \ge M_Z$) vs $0 < \sin^2\theta_W < 1$.
3. Record PDG $\overline{\mathrm{MS}}$ $\sin^2\theta_W(M_Z) = 0.23122$ and CODATA-2022 on-shell $1 - m_W^2/m_Z^2 = 0.22305$ (`codata("weak mixing angle")`) strictly as post-computation comparison columns; zero parameters are fitted.
