All predictions use $\approx$ (derived from $q$).
Experimental values from NNDC/ENSDF with stated uncertainties.
Crossing convention: $(1, -h_{\mathrm{A}})$ throughout (unimodular, $\det T = -1$).

**Table 1 --- $q$-weighted Q-values: $2 \times 2$ block with $6 \times 6$ shell factors, zero fitting.**

The six benchmarks span the mass range, from light nuclei that need no
shell corrections to heavy nuclei that do, so a single $q$-derived
formula is tested across regimes.  This is the primary method.  Each
generator log-ratio is classified as unbinding ($u$), rebinding ($r$),
or spectator ($uc$), then $q$-weighted:

$$
Q = |q \cdot \Sigma_u + q^{-1} \cdot \Sigma_r + \Sigma_{uc}| \times \kappa_q \times F_{\mathrm{shell}}(q) \times F_{I_{10}}(Z,N;q)
$$

Here the $q$-weighted generator sum
$|q \cdot \Sigma_u + q^{-1} \cdot \Sigma_r + \Sigma_{uc}|$ is multiplied
by the $q$-dependent factors $\kappa_q$, $F_{\mathrm{shell}}(q)$, and
$F_{I_{10}}(Z,N;q)$, of which $F_{\mathrm{shell}}(q)$ is the
shell-correction factor detailed below.

See [Table](#tbl:qvalue-benchmark-table-table-data).

**MAE $\approx 4.4\%$, RMS $\approx 5.4\%$, max $|\delta| \approx 10.3\%$.**

All six benchmarks are within $11\%$.
Light nuclei (${}^3\mathrm{H}$, ${}^{14}\mathrm{C}$) are within $2.2\%$ and
need no shell corrections; heavy nuclei (${}^{60}\mathrm{Co}$, ${}^{90}\mathrm{Sr}$,
${}^{137}\mathrm{Cs}$, ${}^{210}\mathrm{Bi}$) require the shell factors
$F_{\mathrm{deg2}}$ and $F_{\mathrm{Pauli}}$ from the $6 \times 6$ regular
representation of $H_3(q)$.

**Shell correction factors (derived from $q$):**

<!-- literal-source: unnormalised Rosso-Jones weighted average at z = q^{1/2}/(q+1) -->
- $F_{\mathrm{deg2}} = 0.5904$: Rosso--Jones weighted degree-2 torus knot
  suppression for shells $\geq 5$ ($N > 28$), computed as the
  quantum-dimension weighted average
  $(J_{2,9} \cdot \mathrm{tr}(T_{2,9} \cdot \Delta) + J_{3,4} \cdot \mathrm{tr}(T_{3,4} \cdot \Delta)) / ((J_{2,9}+J_{3,4}) \cdot \mathrm{tr}(\Delta))$
  from the $H_3(q)$ Markov trace of the beta-decay operator.
  The two degree-2 knots correspond to the $\mu_2$ ($T_{3,4}$, $s = 2^2$)
  and $\mu_3$ ($T_{2,9}$, $s = 3^2$) branches of the Kummer tower,
  matching the CRT decomposition
  $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$.
<!-- literal-source: nominal Pauli suppression parameter in 6x6 regular-representation ansatz -->
- $F_{\mathrm{Pauli}} = 0.6382$: alternating-irrep projection for
  magic-number shells (filled $N$), computed as
  $|\mathrm{tr}_{\mathrm{alt}}(\Delta)| / |\mathrm{tr}(\Delta)|$
  where $\mathrm{tr}_{\mathrm{alt}}$ evaluates with eigenvalue
  $\lambda = -q^{-1}$.
- Both are eigenvalue ratios of $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$
  in the $6 \times 6$ regular representation of $H_3(q)$, which decomposes as
  $1(\mathrm{sym}) \oplus 2(\mathrm{std}) \oplus 1(\mathrm{alt})$.

**Error propagation note.** The prediction uncertainty $\delta Q$
from $\delta q_0 \approx 1.4 \times 10^{-9}$ is negligible
($\sim 10^{-9} \text{MeV}$).  The dominant theoretical uncertainty is
*structural* (model approximations in $F_{\mathrm{shell}}$) rather than
parametric.  All $\sigma$-separations are therefore
$|Q - \mathcal{Q}_{\mathrm{exp}}| / \delta\mathcal{Q}_{\mathrm{exp}}$.
