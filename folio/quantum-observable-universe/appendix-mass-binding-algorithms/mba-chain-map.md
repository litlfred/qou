**Canonical evaluation chain.**
The twelve steps below trace the complete mathematical path from a braid word $w \in B_n$ in a quantum observable universe $(\mathbf{C}, A, \tau)$ to archimedean mass, binding, confinement, and weak-decay observables, continuing [the pre-archimedean derivation chain](#prose:pre-archimedean-derivation-chain).

| Step | Algorithm | Mathematical Input $\to$ Output | Arithmetic & Complexity | Status |
|:---:|:---|:---|:---|:---:|
| 1 | [Categorical braid action](#alg:categorical-action) | $(w \in B_n,\, V \in \mathbf{C}) \;\to\; \rho_n(w) \in H_n(q)^\times \subset \mathrm{End}_{\mathbf{C}}(V^{\otimes n})$ | Symbolic word morphism, $O(|w|)$ | proved |
| 2 | [Gröbner–Shirshov reduction](#alg:gs-reduce-to-hecke-nf) | $w \in B_n \;\to\; \mathrm{NF}(w) = \sum_{u \in S_n} c_u(q)\,T_u \in H_n(q)$ | Exact $\mathbb{Z}[q, q^{-1}]$; $O(m)$ per $2\times 2$ transfer run, $O(n!\,|w|)$ worst case | proved |
| 3 | [Convention-D Markov trace](#alg:markov-trace) | $\mathrm{NF}(w) \in H_n(q) \;\to\; \mathrm{tr}_M(w)\big|_{z = z_D} \in \mathbb{Q}(q)$ | Exact $\mathbb{Q}(q)$ descent or Bratteli edge sweep | derived |
| 4 | [Genus-4 Bring curve invariants](#alg:bring-brane) | $\Sigma_4 \subset \mathbb{P}^4 \;\to\; (\chi = -6,\, g = 4,\, \tfrac{2}{3\pi},\, S_5,\, \{T_{2,9}, T_{3,5}\})$ | Exact algebraic/Hodge invariants, $O(1)$ | proved |
| 5 | [Semisimple Wedderburn & GPMT trace](#alg:wedderburn-decomposition) | $(n, q) \;\to\; \{(d_\lambda,\, q^{2c(\lambda)},\, w_\lambda(z_D),\, d_{\mathrm{mod}}(\lambda))\}_{\lambda \vdash n}$ | Exact $\mathbb{Z}$ hook lengths and $\mathbb{Q}(q)$ polynomial division, $O(p(n)\,n^2)$ | proved |
| 6 | [Symmetric Frobenius pairing](#alg:frobenius-pairing) | $a, b \in H_n(q) \;\to\; \langle a, b \rangle_F = \mathrm{tr}_M(ab),\; \Psi = S^2 = \mathrm{id}$ | Exact $\mathbb{Q}(q)$ bilinear form on $A$ and $H_n(q)$ | proved |
| 7 | [Length filtration & $E_2$ collapse](#alg:gb-filtration) | $H_n(q) \;\to\; \bigoplus_{\ell=0}^{\binom{n}{2}} \mathrm{gr}_\ell H_n(q)$ with $d_r = 0$ ($r \ge 2$) | Exact $\mathbb{Z}$-graded filtration, $O(n!)$ | derived |
| 8 | [Jet-prefix $q \to 1$ transport](#alg:jet-prefix-transport) | $(P_K(q), N) \;\to\; P_K^{(N)}(\hbar_q) + O(\hbar_q^{N+1})$ | Exact $\mathbb{Q}[\hbar_q]$ jet + $\geq 80$-digit interval tail | conditional |
| 9a | [Two-Term Lagrangian nucleon mass](#alg:mass-identity) | $(q_0, m_e, \mathrm{Vol}(4_1)) \;\to\; M = M_{\mathrm{QCD}} + M_{\mathrm{QED}},\, \alpha_{\mathrm{EM}}^{\mathrm{corr}},\, m_p/m_e,\, m_\mu/m_e$ | Closed-form $\mathbb{Q}(q)$ traces + $\geq 80$-digit Clausen & cubic root | conditional |
| 9b | [Multi-scale nuclear binding](#alg:per-isotope-binding) | $(Z, N, q_0, m_e) \;\to\; B(Z, N)$ ($H_4$ $\alpha$-cell + 3D simplicial ball + $(2j+1)$ spin–orbit + TL pairing + FCC Coulomb) | Exact $\mathbb{Z}$ Dehn–Sommerville & shell filling + $\geq 80$-digit $\mathbb{Q}(q_0)$ evaluation | derived / open heavy deformation |
| 10 | [Confinement primal–dual SDP](#alg:confinement-sdp) | $(t, G \succeq 0, n_{\mathrm{target}}) \;\to\; (x^*, y_0^*, y^* \ge 0,\; p^* = d^*)$ | Polynomial-time interior-point conic SDP | derived |
| 11 | [Convention-D $\mathfrak{Q}_\beta$, $g_A$, and $\tau_n$](#alg:q-beta-truncation) | $(q_{2t}, m_e, \varepsilon) \;\to\; \mathfrak{Q}_\beta^{(N)},\, g_A(q),\, f_0(\epsilon_0),\, \tau_n$ | Exact $\mathbb{Q}(q)$ / $\mathbb{Q}(\sqrt{3})$ series + $\geq 80$-digit phase-space quadrature, $O(N(\varepsilon))$ | derived |

**Auxiliary structural blocks and atomic closure.**
Five companion blocks follow the canonical chain:

1. **[Per-partition Springer/Donaldson–Thomas weight](#alg:delta-lambda-closure).** Unconditional closed form $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$, the intensive-versus-extensive trace theorem, the $A = 4$ pairwise determinant cap, and the two remaining open multi-body problems ($H_{12}(q) \supset H_3(q)^{\otimes 4}$ cabled coarse-graining and deformed actinide Nilsson stiffness).
2. **[External three-body/four-body correlation analysis](#rem:tjon-universality-external).** Exact algebraic proof over ordered commutative rings that the zero-range Yakubovsky ratio $M(4) = 5\,M(3)$ lies strictly outside the $\mu_4 = 0$ simplex baseline.
3. **[Mirror-pair baseline cancellation](#prop:mirror-baseline-cancellation).** Exact cancellation of bar-even crossing invariants across mirror nuclei $(Z, N) \leftrightarrow (N, Z)$, isolating bar-odd writhe and discrete proton-pair Coulomb potentials.
4. **[Isovector chiral residue](#prop:isovector-chiral-residue).** Conditional reduction of the mirror isovector slope $b = 4\kappa$ to the $A_5$ Galois chiral residue of the Birman–Wenzl Plancherel measure.
5. **[All-order Convention-D $c_k^{(D)}$ generating function](#alg:ck-truncation-ladder).** Bar-even $H = (q - q^{-1})^2$ rational building blocks, Lagrange–Bürmann critical branch point $H_* = (-15 + \sqrt{33})/4$ and convergence radius $R_u \approx 0.369009$, closed-form rungs $c_2^{(D)}, c_3^{(D)}(q), c_4^{(D)}(q)$, and division-free distinct-partition triangular extraction.

Neutral atomic masses combine the nuclear mass $M_{\mathrm{nuc}}(Z, N) = Z m_p + N m_n - B(Z, N)$ with the bare-$Z$ hydrogenic shell sum $M_{\mathrm{atom}}(Z, N) = M_{\mathrm{nuc}}(Z, N) + Z m_e - B_{\mathrm{el}}(Z)$ evaluated at the Hartree scale $E_h = (\alpha_{\mathrm{EM}}^{\mathrm{corr}})^2 m_e$; inter-electron Hartree–Fock screening ($Z_{\mathrm{eff}}$) beyond the hydrogenic sum is an open multi-electron refinement.
