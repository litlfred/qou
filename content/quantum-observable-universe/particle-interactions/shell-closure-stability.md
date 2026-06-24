**Proposition.**
*Fix a bare nuclear [confined particle](#def:confined-particle)
$P_{\mathrm{bare}}$ at level $\ell = 2$ with atomic number $Z_{\max}$,
and consider the dressing chain in the
[confinement category](#def:confinement-category):*

$$
  P_{\mathrm{bare}}
  \;\xrightarrow{\mathrm{dress}_{S_1}}\;
  P^{(1)}
  \;\xrightarrow{\mathrm{dress}_{S_2}}\;
  P^{(2)}
  \;\xrightarrow{\mathrm{dress}_{S_3}}\;
  \cdots
  \;\xrightarrow{\mathrm{dress}_{S_{Z_{\max}}}}\;
  P^{(Z_{\max})},
$$

*where $P^{(Z)}$ is the dressed particle with $Z$ attached
electrons ([dressed particle](#def:dressed-particle)).  Let
$\sigma_F(P^{(Z)}, q)$ denote the **Frobenius stability index** —
the optimal dual objective value of the
[confinement SDP](#prop:confinement-sdp) at $P^{(Z)}$:*

$$
  \sigma_F(P, q)
  \;:=\;
  n_{\mathrm{target}} \cdot u_0^*(P, q),
$$

*where $u_0^*(P, q)$ is the optimal shadow price of the
normalisation constraint.  By strong duality (Slater's condition
holds at generic $q$ since $\Phi = \mathrm{id}/\mathrm{tr}(\mathrm{id})$
is strictly feasible), $\sigma_F(P, q)$ coincides with the optimal
primal objective $\langle T, \Phi^*(P, q) \rangle$ and with the
minimum-action Markov-trace weight of the confined operator.  Then:*

1. ***Monotonic non-decrease:** $\sigma_F(P^{(Z)}, q)$ is
   non-decreasing in $Z$ along the dressing chain for every
   $q$ in the generic locus.*

2. ***Local maxima of the marginal gain at shell closures (conditional on
   the open shell-capacity derivation):** the
   **marginal stability gain**
   $\Delta\sigma_F(Z) := \sigma_F(P^{(Z)}, q) - \sigma_F(P^{(Z-1)}, q)$
   — the per-electron dressing gap — attains a strict local maximum at each
   **shell closure**, where the binding multiplicity satisfies
   $\mu(S_Z, q) \ge 2$ (the spectral-gap jump of the simultaneously-tight
   dual blocks).  It is $\Delta\sigma_F$, not $\sigma_F$ itself, that peaks:
   $\sigma_F$ is monotone non-decreasing by claim (1), so it has no interior
   local maximum.  **Whether those closures fall at the empirical noble-gas
   numbers** $Z \in \mathcal{Z}_{\mathrm{noble}} = \{2, 10, 18, 36, 54, 86\}$
   **is conditional on the open shell-capacity derivation:** the bare
   categorical operator (the $2\times2$ transfer matrix $T_{\gamma e}$; the
   pure $2n^2$ count) places closures every two electrons / at the cumulative
   $[2, 10, 28, 60, \ldots]$ — **not** at the noble gases, which require the
   Madelung sub-shell ordering not yet derived (see
   [noble-gas characterisation](#prop:noble-gas-characterization) and its
   categorical-$\sigma_F$ caveat).  A high-precision categorical $\sigma_F$
   dressing chain confirms $\sigma_F$ does not by itself reproduce the
   noble-gas peaks.*

3. ***Terminality:** For every $Z \in \mathcal{Z}_{\mathrm{noble}}$,
   $P^{(Z)}$ is a **local terminal object** of the dressing
   sub-diagram: any outgoing arrow
   $\mathrm{dress}_{S'}: P^{(Z)} \to P'$ requires simultaneously
   breaking $\mu(S_Z, q) \ge 2$ tight dual blocks of the
   confinement SDP, which is energetically forbidden at the
   electromagnetic coupling $\alpha$ in the generic locus.*

*

**Corollary (chemical inertness).**
*The categorical terminality of noble-gas $P^{(Z)}$ is the
structural origin of chemical inertness: no covalent dressing
morphism $\mathrm{dress}_{S_{\mathrm{bond}}}: P^{(Z)} \to P_{\mathrm{molecule}}$
is feasible at room-temperature $q$ without breaking a closed shell.
Compounds of noble gases (e.g. $\mathrm{XeF}_4$) require $q$ far
from the generic locus — shifted by external fields — to clear the
terminality barrier.*

**Corollary (ionisation energy peaks — conditional).**
*The first-ionisation energy $I_1(Z)$ is the Markov-trace
gap from $P^{(Z)}$ to $P^{(Z-1)} + e^-$ — i.e. exactly the marginal
stability gain $\Delta\sigma_F(Z)$ of claim (2), by
[confinement-topological](#prop:confinement-topological) and the
dual shadow-price structure (not $\sigma_F(P^{(Z)}, q)$ itself, which
is monotone).  $I_1$ therefore peaks at the shell **closures** and
dips at the shell **openings**.  Identifying those closures with the
empirical noble-gas peaks (and the alkali troughs at $Z = 3, 11, 19,
\ldots$) is **conditional on the open shell-capacity derivation**
(claim 2): the bare categorical operator does not place the closures
at the noble gases without the Madelung / $2n^2$ structure, so the
periodic-table identification is a target, not yet a theorem.*
