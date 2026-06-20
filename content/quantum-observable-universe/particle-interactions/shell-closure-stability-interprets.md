**Remark.**
*[Shell-closure stability](#prop:shell-closure-stability) gives a
categorical origin for three independent empirical regularities of
the periodic table:*

1. ***Periodicity (conditional).***  *Dressing
   $\mathrm{dress}_{S_Z}: P^{(Z-1)} \to P^{(Z)}$ traces a chain in
   the confinement category.  The Frobenius stability index
   $\sigma_F(P^{(Z)}, q)$ is monotone non-decreasing; its
   **marginal increment** $\Delta\sigma_F(Z) = I_1(Z)$ has local maxima
   at the shell **closures**.  Whether those closures coincide with the
   noble-gas atomic numbers $\{2, 10, 18, 36, 54, 86\}$ (row spacing
   2, 8, 8, 18, 18, 32) is the open shell-capacity question: the bare
   categorical operator gives closures every two electrons / at the
   pure-$2n^2$ cumulative $[2, 10, 28, 60, \ldots]$, so the Madelung
   row length is **not** yet derived — a target, not an established
   consequence of the SDP.*

2. ***Chemical inertness.***  *A noble-gas $P^{(Z)}$ is a **local
   terminal object** of the dressing sub-diagram: the
   single-electron dressing
   $\mathrm{dress}_{S_1}: P^{(Z)} \to P^{(Z+1)}$ is feasible only if
   every currently tight dual block of the confinement SDP is
   simultaneously broken.  With $\mu(S_Z, q) \ge 2$, this requires
   $\ge 2\,\Delta E_{\mathrm{shell}}$, which exceeds the
   electromagnetic binding scale $\alpha \cdot m_e c_q^2$ at
   generic $q$.  Hence no covalent arrow leaves $P^{(Z)}$ under
   ordinary conditions: helium, neon, argon, krypton, xenon, radon
   form no stable compounds at room temperature.  The known
   exceptions (e.g. $\mathrm{XeF}_4$) require external fields or
   pressures that shift $q$ out of the generic locus.*

3. ***Ionisation-energy peaks (conditional).***  *The first ionisation energy
   $I_1(Z) = \mathrm{tr}_M(P^{(Z)}) - \mathrm{tr}_M(P^{(Z-1)}) -
   \mathrm{tr}_M(e^-)$ is the **marginal increment** $\Delta\sigma_F(Z)$
   via the dual shadow-price structure (not $\sigma_F(P^{(Z)}, q)$
   itself, which is monotone).  By
   [prop:shell-closure-stability](#prop:shell-closure-stability)
   claim (2) it peaks at the shell **closures** and dips at the
   **openings**.  Identifying those with the observed peaks at
   noble-gas $Z$ and the alkali troughs ($Z = 3, 11, 19, \ldots$) is
   **conditional on the open shell-capacity derivation**: the bare
   matrix Frobenius positivity of the
   [confinement SDP](#prop:confinement-sdp) does not place the closures
   at the noble gases without the still-underived Madelung / $2n^2$
   structure.*

**Valence as dressing-arrow availability.**
*An atom's **valence** $v(Z)$ is the number of forward dressing
arrows
$\mathrm{dress}_{S_1}: P^{(Z)} \to P^{(Z+1)}$ that remain feasible
at the electromagnetic scale.  For $Z$ far from noble-gas values,
$v(Z) > 0$ (one or more feasible arrows $\to$ reactive atom).  For $Z
\in \mathcal{Z}_{\mathrm{noble}}$, $v(Z) = 0$ (terminal object $\to$
inert).  Classical valence rules (octet, 18-electron rule) are
shadow-statements of the feasibility count, and hybridised
bonding is a composite of dressing + folding morphisms in
$\mathbf{Conf}$.*

**Nucleon–electron parallel.**
*The nucleon magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ and the
electron magic numbers $\{2, 10, 18, 36, 54, 86\}$ are the **same
structural phenomenon at different confinement levels**.  Both
sequences are level-specific closures of the multi-level SDP — the
nucleon closure at $\ell = 1$ (within $H_{3A}$), the electron
closure at $\ell = 6$ (the atom-electron block of
$H_{A+Z}$).  [Prop:shell-closure-stability](#prop:shell-closure-stability)
applies uniformly at every level; the particular numeric sequences
reflect the shell-boundary polytope of each level, not independent
physical laws.*
