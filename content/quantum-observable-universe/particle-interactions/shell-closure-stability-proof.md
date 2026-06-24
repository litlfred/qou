*Claim (1) — **SDP-relaxation monotonicity**.
At each step $Z - 1 \to Z$ the dressing morphism
$\mathrm{dress}_{S_Z}$ induces a cabling embedding
$\iota: H_{A + Z - 1}(q) \hookrightarrow H_{A + Z}(q)$.  Three
structural changes follow in the
[confinement SDP](#prop:confinement-sdp):*

*(a) **Primal relaxation.**  The primal variable space extends from
$\mathrm{End}_R(H_{A+Z-1}(R, q))$ to
$\mathrm{End}_R(H_{A+Z}(R, q))$; the cabling-induced lift
$\Phi \mapsto \iota_* \Phi \oplus 0$ embeds every primal-feasible
point of $\mathrm{SDP}_{Z-1}$ into the primal-feasible set of
$\mathrm{SDP}_Z$ while preserving $\langle T, \Phi \rangle$.*

*(b) **Dual relaxation.**  Dual variables extend by new shadow
prices $u_\lambda \ge 0$ for every Wedderburn block
$\lambda \vdash k$ with $k \in \{A+Z-1+1,\ldots, A+Z\}$ that first
becomes available.  Setting these new variables to zero recovers the
old dual feasibility condition unchanged, so every dual-feasible
point of $\mathrm{SDP}_{Z-1}$ admits a lift to a dual-feasible point
of $\mathrm{SDP}_Z$ achieving the same objective
$n_{\mathrm{target}} \cdot u_0$.*

*(c) **Cost compatibility.**  The cost operator extends as a direct
sum $T^{(Z)} = \iota_* T^{(Z-1)} \oplus T_{\mathrm{new}}$ where
$T_{\mathrm{new}}$ is the Markov-trace weight on the new block.
Feasibility of the dual lift in (b) requires only that the
additional $u_\lambda^{(Z)}$ on the new blocks dominate
$T_{\mathrm{new}}$ in the matrix inequality
$u_0 I + \sum u_\lambda \pi_\lambda - T \preceq 0$; since
$T_{\mathrm{new}}$ is bounded and the new $u_\lambda$ are free to
take any non-negative value, such a dominating choice always
exists.*

*Since $\mathrm{SDP}_Z$ maximises the dual objective over a
superset of feasible points containing the lift of
$(u_0^{(Z-1)}, u_\lambda^{(Z-1)})$, the standard SDP-relaxation
monotonicity argument ([Boyd–Vandenberghe §5.4.1](https://doi.org/10.1017/CBO9780511804441))
gives*

$$
  \sigma_F(P^{(Z)}, q)
  \;=\;
  n_{\mathrm{target}} \cdot u_0^{*(Z)}
  \;\ge\;
  n_{\mathrm{target}} \cdot u_0^{*(Z-1)}
  \;=\;
  \sigma_F(P^{(Z-1)}, q).
$$

*(Note: the monotonicity here is SDP-relaxation, not Cauchy
eigenvalue interlacing — the two would give opposite conclusions on
the raw Gram matrix, because dressing both enlarges the algebra and
adds constraints consistent with the lift.  The cost-compatibility
step (c) is what makes the lift feasible and the relaxation
argument work.)*

*Claim (2).  For $Z \in \mathcal{Z}_{\mathrm{noble}}$ the orbital
parametrisation of electron shell fills all
magnetic and spin labels of principal shell $n$, so multiple
Wedderburn blocks of the multi-level SDP are simultaneously tight —
$\mu(S_Z, q) \ge 2$ by the binding-multiplicity definition.  The
simultaneous tightness of two or more blocks means the active-support
Gram matrix has a rank-$\mu$ dual kernel; by
[confinement-topological](#prop:confinement-topological) the
corresponding Frobenius form is non-degenerate on the complementary
subspace, and its minimum eigenvalue strictly exceeds the
single-block value.  This shell-boundary spectral-gap jump is exactly
the strict local maximum of the marginal gain $\Delta\sigma_F$ (and the
$\mu \ge 2$ multiplicity); $\sigma_F$ itself stays monotone by
claim (1).*

*Claim (3).  An outgoing dressing
$\mathrm{dress}_{S'}: P^{(Z)} \to P'$ with
$Z \in \mathcal{Z}_{\mathrm{noble}}$ extends the active support by
opening a block of principal shell $n + 1$.  Because the $n$-th
shell is fully closed, no dual variable in shell $n$ can slack, so
the extension is feasible only if every dual variable in shell $n$
is simultaneously increased — equivalently, every currently tight
block must be broken to admit the new one.  The energetic cost of
breaking $\mu(S_Z, q) \ge 2$ tight blocks is at least
$\mu \cdot \Delta E_{\mathrm{shell}}(q)$, where
$\Delta E_{\mathrm{shell}}$ is the single-block shell-boundary gap
(derived categorically from the multi-level SDP's dual shadow
prices).  For $q$ in the generic locus, $\mu \cdot \Delta E_{\mathrm{shell}}(q) >
\alpha \cdot m_e \cdot c_q^2$ (electromagnetic binding scale), so no
EM-mediated dressing can clear the barrier: $P^{(Z)}$ is terminal
within the $\mathrm{dress}$ sub-diagram.
$\qquad\blacksquare$
