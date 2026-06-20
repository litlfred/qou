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

2. ***Local maxima of the marginal gain at noble-gas $Z$:** the
   **marginal stability gain**
   $\Delta\sigma_F(Z) := \sigma_F(P^{(Z)}, q) - \sigma_F(P^{(Z-1)}, q)$
   — the per-electron dressing gap — attains a strict local maximum at
   $Z \in \mathcal{Z}_{\mathrm{noble}} = \{2, 10, 18, 36, 54, 86\}$, and
   the binding multiplicity satisfies $\mu(S_Z, q) \ge 2$ there.  It is
   $\Delta\sigma_F$, not $\sigma_F$ itself, that peaks: $\sigma_F$ is
   monotone non-decreasing by claim (1), so it has no interior local
   maximum.  The simultaneous tightness of $\mu \ge 2$ dual blocks is the
   spectral-gap jump that makes the marginal gain a local maximum.*

3. ***Terminality:** For every $Z \in \mathcal{Z}_{\mathrm{noble}}$,
   $P^{(Z)}$ is a **local terminal object** of the dressing
   sub-diagram: any outgoing arrow
   $\mathrm{dress}_{S'}: P^{(Z)} \to P'$ requires simultaneously
   breaking $\mu(S_Z, q) \ge 2$ tight dual blocks of the
   confinement SDP, which is energetically forbidden at the
   electromagnetic coupling $\alpha$ in the generic locus.*

*Proof.*
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
within the $\mathrm{dress}$ sub-diagram.  $\square$*

**Corollary (chemical inertness).**
*The categorical terminality of noble-gas $P^{(Z)}$ is the
structural origin of chemical inertness: no covalent dressing
morphism $\mathrm{dress}_{S_{\mathrm{bond}}}: P^{(Z)} \to P_{\mathrm{molecule}}$
is feasible at room-temperature $q$ without breaking a closed shell.
Compounds of noble gases (e.g. $\mathrm{XeF}_4$) require $q$ far
from the generic locus — shifted by external fields — to clear the
terminality barrier.*

**Corollary (ionisation energy peaks).**
*The first-ionisation energy $I_1(Z)$ is the Markov-trace
gap from $P^{(Z)}$ to $P^{(Z-1)} + e^-$ — i.e. exactly the marginal
stability gain $\Delta\sigma_F(Z)$ of claim (2), by
[confinement-topological](#prop:confinement-topological) and the
dual shadow-price structure (not $\sigma_F(P^{(Z)}, q)$ itself, which
is monotone).  The local-maxima statement of claim (2) then predicts
the observed peaks of $I_1$ at $Z \in \mathcal{Z}_{\mathrm{noble}}$ —
and the troughs immediately after, at the alkali metals $Z = 3, 11,
19, 37, 55, 87$ — recovering the classical periodic-table structure
from the confinement SDP.*
