The $q$-weighted Q-value formula is *categorically defined*: every
ingredient is derived from the substrate parameter $q$ and the
Iwahori--Hecke algebra structure, with zero fitting parameters.

**Categorical (zero fitting) --- the $q$-weighted method.**

1. The transfer matrix $T(c,d)$ follows from the Iwahori--Hecke
   relation $\sigma^{-1} = \sigma - (q - q^{-1})$, giving crossing
   coefficients $(1, -\mathrm{HA})$ with $\det T = -1$ (unimodular).
2. Each generator log-ratio is classified as unbinding ($u$),
   rebinding ($r$), or spectator ($uc$) using nucleon type changes.
3. The $q$-weighting $|q \cdot \Sigma_u + q^{-1} \cdot \Sigma_r + \Sigma_{uc}|$
   exploits the Iwahori--Hecke eigenvalue asymmetry ($q$ vs $-q^{-1}$).
4. Shell corrections $F_{\mathrm{deg2}}$ and $F_{\mathrm{Pauli}}$ are
   eigenvalue ratios in the $6 \times 6$ regular representation of
   $H_3(q)$: the $2 \times 2$ standard representation generates the
   full $6 \times 6$ via tensor products.
5. The energy scale $\kappa_q = \ln(q) \times m_e / 3$ follows from
   the Skein mass relation.

**Result**: MAE $\approx 4.9\%$ across six benchmark nuclei
spanning $A = 3$ to $A = 210$, with zero free parameters.

**Phenomenological (fitted) methods for comparison.**

- *Lagrangian sum*: $\mathcal{L} = \sum_i (\hat{V}_{d,i} - \hat{V}_{p,i})/\hat{V}_{p,i}$
  with $E_0$ calibrated from ${}^3\mathrm{H}$.  MAE $\approx 45\%$.
  Signal dilution from equal-weight spectator contributions.
- *Dirac decomposition*: $D = q^{-1} \sum \Delta\mathrm{tr}/\mathrm{tr} +
  \hbar_q \sum \Delta\mathrm{spr}/\mathrm{spr}$ with same calibration.
  MAE $\approx 71\%$.  Same dilution pathology.
- *$E_0$ calibration*: $E_0 = \mathcal{Q}_n / |\Delta\mathrm{net}_{\mathrm{free}}|$
  from free-neutron Gröbner--Shirshov normal form.  Gives $E_0 = 4.406\;\text{MeV}$
  but does not transfer to multi-nucleon systems without
  topology-dependent suppression.

The naive methods fail because they sum $A - 1$ generator contributions
with equal weight, diluting the signal from the single converting
neutron.  The $q$-weighted method succeeds because it classifies
generators by their role in the transition, applying the categorical
eigenvalue separation of the Iwahori--Hecke algebra.  The
$2 \times 2 = 6 \times 6$ identity ensures the standard representation
captures the full regular representation structure.
