*Proof.*

We establish three claims.

**1. SDP-relaxation monotonicity.**
At each step $Z - 1 \to Z$, the dressing morphism $\mathrm{dress}_{S_Z}$ induces a cabling embedding $\iota: H_{A + Z - 1}(q) \hookrightarrow H_{A + Z}(q)$. Three structural changes follow in the [confinement SDP](#prop:confinement-sdp):

**(a) Primal relaxation.** The primal variable space extends from $\mathrm{End}_R(H_{A+Z-1}(R, q))$ to $\mathrm{End}_R(H_{A+Z}(R, q))$. The cabling-induced lift $\Phi \mapsto \iota_* \Phi \oplus 0$ embeds every primal-feasible point of $\mathrm{SDP}_{Z-1}$ into the primal-feasible set of $\mathrm{SDP}_Z$, preserving the objective $\langle T, \Phi \rangle$.

**(b) Dual relaxation.** Dual variables extend by new shadow prices $u_\lambda \ge 0$ for every Wedderburn block $\lambda \vdash k$ with $k \in \{A+Z-1+1,\ldots, A+Z\}$ that first becomes available. Setting these new variables to zero recovers the old dual feasibility condition. Every dual-feasible point of $\mathrm{SDP}_{Z-1}$ admits a lift to a dual-feasible point of $\mathrm{SDP}_Z$ achieving the same objective $n_{\mathrm{target}} \cdot u_0$.

**(c) Cost compatibility.** The cost operator extends as a direct sum $T^{(Z)} = \iota_* T^{(Z-1)} \oplus T_{\mathrm{new}}$, where $T_{\mathrm{new}}$ is the Markov-trace weight on the new block. Feasibility of the dual lift requires only that the additional $u_\lambda^{(Z)}$ on the new blocks dominate $T_{\mathrm{new}}$ in the matrix inequality $u_0 I + \sum u_\lambda \pi_\lambda - T \preceq 0$. Because $T_{\mathrm{new}}$ is bounded and the new $u_\lambda$ can take any non-negative value, a dominating choice always exists.

Because $\mathrm{SDP}_Z$ maximises the dual objective over a superset of feasible points containing the lift of $(u_0^{(Z-1)}, u_\lambda^{(Z-1)})$, standard SDP-relaxation monotonicity gives
$$
  \sigma_F(P^{(Z)}, q)
  \;=\;
  n_{\mathrm{target}} \cdot u_0^{*(Z)}
  \;\ge\;
  n_{\mathrm{target}} \cdot u_0^{*(Z-1)}
  \;=\;
  \sigma_F(P^{(Z-1)}, q).
$$
(Cost compatibility makes the lift feasible, ensuring the relaxation argument holds despite constraints added by dressing).

**2. Local maxima.**
For $Z \in \mathcal{Z}_{\mathrm{noble}}$, the orbital parametrisation of the electron shell fills all magnetic and spin labels of principal shell $n$. Multiple Wedderburn blocks of the multi-level SDP are simultaneously tight: $\mu(S_Z, q) \ge 2$. Simultaneous tightness means the active-support Gram matrix has a rank-$\mu$ dual kernel. By [confinement-topological](#prop:confinement-topological), the corresponding Frobenius form is non-degenerate on the complementary subspace (**convention D**: the complement is taken inside $H_n/\mathrm{rad} \cong \mathrm{TL}_n$, since the radical blocks are degenerate for the trace and would otherwise sit in every complement), and its minimum eigenvalue strictly exceeds the single-block value. This shell-boundary spectral-gap jump equals the strict local maximum of the marginal gain $\Delta\sigma_F$; $\sigma_F$ itself stays monotone.

**3. Terminality.**
An outgoing dressing $\mathrm{dress}_{S'}: P^{(Z)} \to P'$ with $Z \in \mathcal{Z}_{\mathrm{noble}}$ extends the active support by opening a block of principal shell $n + 1$. Because the $n$-th shell is fully closed, no dual variable in shell $n$ can slack. The extension is feasible only if every dual variable in shell $n$ increases; every currently tight block must break to admit the new one. The energetic cost of breaking $\mu(S_Z, q) \ge 2$ tight blocks is at least $\mu \cdot \Delta E_{\mathrm{shell}}(q)$. For $q$ in the generic locus, $\mu \cdot \Delta E_{\mathrm{shell}}(q) > \alpha \cdot m_e \cdot c_q^2$. No electromagnetic-mediated dressing clears the barrier, making $P^{(Z)}$ terminal within the $\mathrm{dress}$ sub-diagram. $\square$

**Corollary (chemical inertness).**
Categorical terminality of noble-gas $P^{(Z)}$ structurally forces chemical inertness. No covalent dressing morphism $\mathrm{dress}_{S_{\mathrm{bond}}}: P^{(Z)} \to P_{\mathrm{molecule}}$ is feasible at room-temperature $q$ without breaking a closed shell. Noble gas compounds require $q$ far from the generic locus to clear the terminality barrier.

**Corollary (ionisation energy peaks).**
The first-ionisation energy $I_1(Z)$ is the Markov-trace gap from $P^{(Z)}$ to $P^{(Z-1)} + e^-$. This matches the marginal stability gain $\Delta\sigma_F(Z)$. By [confinement-topological](#prop:confinement-topological) and the dual shadow-price structure, $I_1$ peaks at shell closures and dips at shell openings. Identifying these closures with empirical noble-gas peaks is conditional on the open shell-capacity derivation; the bare categorical operator does not place the closures at the noble gases without the Madelung structure.
