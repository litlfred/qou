<!-- FILE_START: lepton-mass-tower-canonical.md -->
> **⚠ Resolution update (2026-06-30).** The muon knot-ID is the torus knot $T(2,5)$, and $4_1$ is the Higgs. Torus-knot leptons carry zero intrinsic hyperbolic volume. The charged lepton mass originates from its coupling to the Higgs. The per-braid tower evaluation presented below tests the lepton's intrinsic isolated tower, not its mass. The material is retained as a scope-limited negative on the isolated-tower hypothesis.

**Conjecture (canonical lepton-mass tower).**
*Let $\ell \in \{\mathfrak{e}, \mu, \tau\}$ be a charged lepton with canonical braid representative $K_\ell$. The lepton mass evaluates as:*

$$
  \mathfrak{m}(K_\ell)
  \;=\;
  m_e \cdot \mathcal{F}_\ell(q)
  \;=\;
  m_e \cdot \xi_\ell(q) \cdot \mathrm{Vol}_q^{\mathrm{tower}}(K_\ell).
$$

*The evaluation occurs entirely within the canonical per-braid mass tower, without invoking the superseded scalar density $\rho_q$.*

The atomic graded expansion evaluates nuclear mass by adding constituent nucleon masses to binding-energy corrections. Leptons lack nucleon constituents. The isolated lepton mass requires a separate canonical formula.

The operative Skein formula evaluates the $m_\mu / m_e$ ratio using the Kashaev limit $\mathrm{Vol}(4_1)/\hbar_q^2$. The direct operator-level Markov-trace ratio yields $\sim 0.27$, falsifying the Skein formula as a direct pre-limit identity. The canonical $\mathcal{F}_\ell(q)$ must supply the missing magnitude at the finite substrate $q_0$.

**Two-constraint obstruction.**
Any working $\mathcal{F}_\ell(q)$ must satisfy two constraints simultaneously. 
1. **Nonzero on torus knots.** The electron $T(2,3)$ and tau $T(2,7)$ are torus knots. Their hyperbolic volume vanishes identically. The Skein formula fails to predict $m_\tau / m_e$ entirely. 
2. **$O(10^2)$ mass ratios.** If $\xi_\ell(q)$ is a universal scalar, it cancels in inter-lepton ratios. The symmetric $\mathrm{Li}_2^q$ tower yields $O(1)$ ratios, missing CODATA values by factors of $30$ to $130$. 

The symmetric $\mathrm{Li}_2^q$ tower lacks the $1/\hbar$ Kashaev blow-up required to supply the $O(10^2)$ magnitude.

**Faddeev $\Phi_q$ probe.**
Substituting the Faddeev quantum dilogarithm $\Phi_q$ injects the required $1/\hbar$ enhancement but fails to reproduce CODATA. The muon $4_1$ evaluation diverges severely near the $\Phi_q$ convergence radius. The $T(2,5)$ evaluation undershoots. The muon knot-ID split ($4_1$ vs $T(2,5)$) governs the divergence behavior entirely.

The isolated $\Phi_q$ per-braid tower cannot close the lepton mass ratios. The mass generation requires the $4_1$ Higgs coupling mechanism.
<!-- FILE_END: lepton-mass-tower-canonical.md -->

<!-- FILE_START: lepton-bring-surface-h3-3channel.md -->
**Proposition (lepton Bring-surface convention).**
*For any torus-knot lepton candidate $K_\ell = \sigma_1^{2m+1}$, the additive Wedderburn volume $\hat V_\ell^{\mathrm{full}}$ evaluates via the $H_3$ 3-channel Plancherel-weighted character sum:*

$$
  \hat V_\ell^{\mathrm{full}}
  \;=\;
  W_{\mathrm{sym}} \cdot q^{2m+1}
  \;+\;
  W_{\mathrm{std}} \cdot (z \cdot a_{2m+1} + b_{2m+1})
  \;+\;
  W_{\mathrm{alt}} \cdot (-q^{-1})^{2m+1},
$$

*where $W_\lambda$ are the $H_3$ Plancherel weights and $(a_{2m+1}, b_{2m+1})$ are the Hecke recursion coefficients.*

The framework embeds nucleons on the Bring surface via 3 quark color tubes. The lepton embedding utilizes the 3 $H_3$ Wedderburn channels. Both configurations project 3-fold substrate representations into single observables. The $H_3$ evaluation satisfies the cohomological discipline linking 3 calibration inputs to 3 Wedderburn channels.

Evaluating the electron $\sigma_1^3$ recovers the calibration $\hat V_e^{\mathrm{full}} \approx 0.586$. The tau candidate $T(2,7)$ forces $\hat V > q_0$, breaching the $\mathrm{Li}_2^q$ convergence radius and diverging. The lepton mass evaluation requires the Higgs coupling resolution.
<!-- FILE_END: lepton-bring-surface-h3-3channel.md -->

<!-- FILE_START: conj-lepton-tower-h-n-plus-1-branching.md -->
**Conjecture (lepton-tower closure factor).**
*Let $K_\ell$ be the canonical knot for the lepton at tower-index $m$ (electron $m=1$, muon $m=2$, tau $m=3$). The canonical mass-tower correction factor is*

$$
  \xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q}.
$$

The factor $(2m-1, m, 2m)$ exhibits strict symmetry in $h = q - q^{-1}$. The odd upper index contributes a bar-anti-symmetric upper-jet bracket. The even lower index contributes a bar-symmetric closing trace. This precise amphichiral reflection reflects the knot-operator equivalence structural directive.

The predicted muon factor $[3]_q \cdot [2]_q / [4]_q$ matches the empirical requirement to within $0.001\%$. The tau factor $[5]_q \cdot [3]_q / [6]_q$ matches to within $0.79\%$. The algebraic identities reducing these brackets are Lean-verified. The full categorical derivation of this branching factor from the $H_{2m+1}$ substrate remains open.
<!-- FILE_END: conj-lepton-tower-h-n-plus-1-branching.md -->

<!-- FILE_START: conj-atom-braid-exterior-algebra.md -->
**Conjecture (atom-braid exterior-algebra structure).**
*Let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word. Its image in $H_{3A}(q)$ generates a sub-algebra whose Gröbner-Shirshov normal-form filtration shape is given by:*

$$
  \dim_R \bigl(F_k(T_w(Z, N))\bigr) \;=\; \binom{3A - Z}{k - (Z - 1)}.
$$

*The sub-algebra is isomorphic to the exterior algebra $\Lambda^*(R^{3A - Z})$ with grade shift $\delta = Z - 1$.*

The canonical atom-braid populates a fermion Fock-space subalgebra of $H_{3A}(q)$. Each interface between adjacent strands contributes one binary degree of freedom. The proton count $Z$ enforces dimension reduction (removing one degree of freedom per proton) and a grade shift (offsetting the filtration bound).

This exterior structure restricts the active dimension profoundly. For $^4\mathrm{He}$, the dimension collapses from the $12!$ standard Wedderburn basis to exactly $2^{10} = 1024$. The restriction governs the computational complexity of the canonical solver.
<!-- FILE_END: conj-atom-braid-exterior-algebra.md -->

<!-- FILE_START: conj-psd-trace-orthogonality.md -->
**Conjecture (PSD-vs-trace orthogonality).**
*Decompose $H_{3A}(q)$ into Wedderburn blocks. The partitions maximising the Hecke Markov-trace weight $|y_\lambda(q_0)|$ are 1- or 2-row long-string partitions. The partitions minimising the PSD-cone scaling eigenvalue are 3+row multi-step tall-narrow partitions. No partition belongs to both classes.*

The two objectives of the operator-selection problem—maximising the Markov trace and minimising the PSD scaling penalty—pull the solution toward disjoint sectors of the Young lattice. The tension forces the optimal knot operator into compromise Wedderburn channels.
<!-- FILE_END: conj-psd-trace-orthogonality.md -->
