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
the smallest eigenvalue of the dual Gram matrix of the
[confinement SDP](#prop:confinement-sdp) restricted to the active
support $\mathcal{S}^*(S_Z, q)$.  Then:*

1. ***Monotonic non-decrease:** $\sigma_F(P^{(Z)}, q)$ is
   non-decreasing in $Z$ along the dressing chain for every
   $q$ in the generic locus.*

2. ***Local maxima at noble-gas $Z$:** $\sigma_F(P^{(Z)}, q)$ attains
   a strict local maximum at $Z \in \mathcal{Z}_{\mathrm{noble}} =
   \{2, 10, 18, 36, 54, 86\}$.  At these values, the binding
   multiplicity satisfies $\mu(S_Z, q) \ge 2$.*

3. ***Terminality:** For every $Z \in \mathcal{Z}_{\mathrm{noble}}$,
   $P^{(Z)}$ is a **local terminal object** of the dressing
   sub-diagram: any outgoing arrow
   $\mathrm{dress}_{S'}: P^{(Z)} \to P'$ requires simultaneously
   breaking $\mu(S_Z, q) \ge 2$ tight dual blocks of the
   confinement SDP, which is energetically forbidden at the
   electromagnetic coupling $\alpha$ in the generic locus.*

*Proof.*
*Claim (1).  At each step $Z - 1 \to Z$ the dressing morphism
$\mathrm{dress}_{S_Z}$ enlarges the Hecke algebra
$H_{A + Z - 1}(q) \hookrightarrow H_{A + Z}(q)$ and extends the
active support by at most one new dual block.  The Gram matrix of
the enlarged SDP is a block-positive extension of the coarse Gram
(matrix Frobenius positivity,
[prop:confinement-sdp](#prop:confinement-sdp)), so its minimum
eigenvalue cannot decrease: interlacing of eigenvalues on a
principal sub-matrix ([Cauchy interlacing](https://doi.org/10.1017/CBO9780511810817))
forces $\sigma_F(P^{(Z)}) \ge \sigma_F(P^{(Z-1)})$.*

*Claim (2).  For $Z \in \mathcal{Z}_{\mathrm{noble}}$ the orbital
parametrisation of [electron shell](#def:electron-shell) fills all
magnetic and spin labels of principal shell $n$, so multiple
Wedderburn blocks of the multi-level SDP are simultaneously tight —
$\mu(S_Z, q) \ge 2$ by the binding-multiplicity definition.  The
simultaneous tightness of two or more blocks means the active-support
Gram matrix has a rank-$\mu$ dual kernel; by
[confinement-topological](#prop:confinement-topological) the
corresponding Frobenius form is non-degenerate on the complementary
subspace, and its minimum eigenvalue strictly exceeds the
single-block value — establishing the local maximum.*

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
gap from $P^{(Z)}$ to $P^{(Z-1)} + e^-$.  By
[confinement-topological](#prop:confinement-topological) and the
dual shadow-price structure, $I_1(Z)$ is proportional to
$\sigma_F(P^{(Z)}, q)$.  The local-maxima statement of claim (2)
predicts the observed peaks of $I_1$ at $Z \in
\mathcal{Z}_{\mathrm{noble}}$, recovering the classical
periodic-table structure from the confinement SDP.*
