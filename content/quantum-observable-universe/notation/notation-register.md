Every mathematical symbol used in this paper belongs to exactly one
register. The tables below group symbols by the chapter where each is
first introduced; within a chapter, entries are sorted alphabetically
by concept name. This block is authoritative — `CLAUDE.md` §7aa
refers to it.

### Quantum universes (Chapter 1)

| Concept | Font | Symbols |
|---------|------|---------|
| Categories | bold | $\mathbf{C}$, $\mathbf{Rep}$ |
| Lie algebras | fraktur lc | $\mathfrak{su}(2)$, $\mathfrak{g}$ |

### Quantum observable universes (Chapter 2)

| Concept | Font | Symbols |
|---------|------|---------|
| Bundles / sheaves | calligraphic | $\mathcal{S}$, $\mathcal{O}$, $\mathcal{L}$, $\mathcal{A}$ |
| State bundle fibre | calligraphic | $\mathcal{S}_p$ — fibre of $\mathcal{S}$ at brane point $p$. Never write $E_p$. |

### Braids and knots (Chapter 4)

| Concept | Font | Symbols |
|---------|------|---------|
| Crossing energy | plain italic | $E_{\mathfrak{H}}$ — total crossing energy of hadron $\mathfrak{H}$. $E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$. |
| Hook-length product | Latin cap + arg | $H_q(\lambda) = \prod_{x \in \lambda} [h_x(\lambda)]_q$ — always with partition argument. |
| Iwahori–Hecke algebra | Latin cap | $H_n(q)$ — always with subscript $n$. |
| Atomic braid word | calligraphic | $\mathcal{B}_K \in H_{3A}(q)$ — canonical atomic braid for atom $K = (Z, N)$ with $A = Z + N$. Factorises as $\mathcal{B}_K = \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K$ (vacuum · interface). Relocated from $\beta_K$ to cal in Phase 5n — cal register expanded to admit Hecke-algebra structural elements alongside bundles/sheaves. |
| Vacuum (constit) factor | calligraphic + superscript | $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_p^{(Z)} \mathcal{B}_n^{(1)} \cdots \mathcal{B}_n^{(N)}$ — disjoint Hecke product of per-nucleon 3-strand blocks (no interface generators), i.e. "constituent vacuum". Phase 5n synonym for the historical $\beta_K^{\mathrm{constit}}$ of PR #819. |
| Proton / neutron H_3 braid | calligraphic | $\mathcal{B}_p, \mathcal{B}_n \in H_3(q)$ — canonical 3-strand intra-nucleon braids (quark content u-u-d / u-d-d). Relocated from $\beta_p, \beta_n$ in Phase 5n. |
| Intra-atom interface operator | bowtie + K subscript | $\bowtie_K$ — K-deformed Hopf-link-style operator at strand-block boundaries of atom $K$; $\mathcal{B}_K = \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K$. Always adorned with $K$ subscript (no bare $\bowtie$ for this concept). Phase 5n replacement for $\Delta_I^K$. |
| Inter-block Hopf-link operation | $\oplus$ | $X \oplus Y$ — Hopf-link / fusion of two composite structures (e.g., $Z\mathfrak{p} \oplus N\mathfrak{n}$ = Z proton blocks Hopf-linked with N neutron blocks). Relocated from bare $\bowtie$ in Phase 5n to disambiguate from intra-atom $\bowtie_K$. |
| Hopf link object | calligraphic | $\mathcal{L}_K$, $\mathcal{L}_H$ — the Hopf link as a knot/link object. $\mathcal{L}_H$ is the standard Hopf link in the appendix mass-formula notation; $\mathcal{L}_K$ is the K-parameterized variant. |
| Frobenius Gram matrix | upright cap + arg | $\mathrm{G}(q) \in \mathrm{Mat}_N(R)$ — Gram matrix of the chosen N-element Frobenius basis at Hecke parameter $q$, with R the Hecke base ring (not $\mathbb{R}$). Currently a **matrix-valued function** $\mathrm{G}: \mathbb{R} \to \mathrm{Mat}_N(R)$, $q \mapsto \mathrm{G}(q)$; promotion to a functor (with Reeb source category) is aspirational pending formalization of Reeb as a category. Upright distinguishes from gravitational scalar $G_q$ (italic, q-subscript). |
| Markov trace | upright lc + M | $\mathrm{tr}_M$ — Jones–Markov trace on $H_n(q)$; $\mathrm{tr}_M(\mathcal{B}_K) = \sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K)$. Lowercase upright matches QOU's universal `\mathrm{tr}` convention (1489+ uses, parallel to $\det$, $\dim$, $\mathrm{Hom}$). Distinct from fibre functor $\tau$ (italic Greek). |
| Jones–Markov central coefficient | plain italic | $y_\lambda$ — coefficient in $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$, given by Wenzl's hook–content closed form [wenzl1988]. Sign-indefinite at $n \geq 4$. Distinct from the Plancherel measure $w_\lambda$ and the q-deformed Wedderburn-block weight $\tilde w_\lambda$ at $q \neq 1$ — coincides with $w_\lambda$ only on the self-conjugate stratum (see [`prop:wedderburn-weight-canonical`](../braids-and-knots/wedderburn-weight-canonical.md)). Never confuse with $u_\lambda$ (LP shadow-price). |
| LP shadow-price | plain italic | $u_\lambda, u_0$ — Schrijver linear-programming convention for operator-selection LP dual variables. Non-negative by LP duality. Never write $y_\lambda$ here. |
| Markov parameter | plain italic | $z = 1/(r + r^{-1})$ — equivalently $1/(q^{1/2} + q^{-1/2})$. |
| Mass (knot) | fraktur | $\mathfrak{m}_{\mathcal{K}}$ — knot mass. |
| Plancherel measure (classical) | plain italic | $w_\lambda := (\dim V_\lambda)^2 / n!$ — the classical Plancherel probability measure on partitions $\lambda \vdash n$, with $\dim V_\lambda$ the $q$-independent (classical) Hecke-irrep dimension (= number of standard Young tableaux of shape $\lambda$). Sums to $1$ exactly in $\mathbb{Q}$. See [`prop:plancherel-weight-boundedness`](../braids-and-knots/plancherel-weight-boundedness.md). **Distinct** from the q-deformed Wedderburn-block weight $\tilde w_\lambda$; the two coincide at $q = 1$ only. |
| Quantum dimension | plain italic | $\dim_q(\lambda) = [n]_q! / \prod_{x \in \lambda} [h_x]_q$ — the $q$-deformed Frame–Robinson–Thrall hook-length dimension. Reduces to $\dim V_\lambda$ at $q = 1$. Used in the q-deformed Wedderburn-block weight $\tilde w_\lambda = \dim_q^2(\lambda)/[n]_q!$. |
| Spinor information rate | plain italic | $r$ — eigenvalue of the elementary half-twist on the spin-½ fundamental rep of $\mathrm{SU}_q(2)$, $r^2 = q$. The "rate per half-twist" along a single linear braid (no surface area). Analogous to $i: -1$ as $r: q$ — the algebraic ingredient that lifts the 1-D adjoint braid algebra to the 2-D spinor (spin-½) representation. **Never** use $t$ (clashes with $V_K(t)$ knot variable) or $\iota$ (clashes with involution / inclusion). |
| Wedderburn-block weight (q-deformed) | plain italic with tilde | $\tilde w_\lambda := \dim_q^2(\lambda) / [n]_q!$ — the q-deformed analogue of the classical Plancherel measure $w_\lambda$. **Not** a probability measure at $q \neq 1$: empirically $\sum_\lambda \tilde w_\lambda \approx 1.51$ at $q_0 = 1.109978595554181\ldots$ (50 dps) for $n = 12$. Specialises to $w_\lambda$ at $q = 1$. Used in [`prop:plancherel-term-7-formulation`](../braids-and-knots/plancherel-term-7-formulation.md) and the q-deformed Wedderburn-block normalisation of [`prop:wedderburn-weight-canonical`](../braids-and-knots/wedderburn-weight-canonical.md). **Never** call this "Plancherel weight" without the tilde — the classical Plancherel $w_\lambda$ is a different, smaller object. |
| Wenzl principal-spec length | Greek | $\ell$ — number of points in the Schur principal specialisation $s_\lambda(1, q^2, q^4, \ldots, q^{2(\ell-1)})$ defining $y_\lambda$ via Wenzl's formula. **Renamed from $r_W$** to free $r$ for the spinor rate above. |

### Algebraic substrate (Chapter 6)

| Concept | Font | Symbols |
|---------|------|---------|
| $q$-shuffle Hopf algebra | calligraphic | $\mathcal{H}_q$ — convolution algebra of $\mathrm{End}_{\mathbf{C}}(A)$ under $\ast_q$; carries the grouplikes $\exp_q$, $\log_q$, $\mathrm{Li}_2^q$. Never plain $H_q$. |
| Goncharov period filtration | calligraphic | $\mathcal{P}_n$ — weight-$n$ periods in the Goncharov motivic filtration ([Kontsevich–Zagier, Goncharov]). Used in [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence). Distinct from $P_\ell$ (elementary symmetric polynomials in JM elements, [`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)). |
| Primitive root of unity | Greek + sub | $\zeta_n := e^{2\pi i / n}$ — primitive $n$-th root of unity. **Always with subscript:** $\zeta_5$ for Bring $S_5$-symmetry shape, $\zeta_6 = e^{i\pi/3}$ for figure-8 ideal-tetrahedron shape. **Never bare $\zeta$** (collides with Riemann zeta $\zeta(s)$ — always parenthesised — and with character $\chi_\zeta$ — always with $\chi$ prefix). |
| Vortex morphism | Greek | $\varrho \colon \mathbf{1} \to A$ — generic closed vortex. Never $\gamma$ for a vortex; $\gamma$ is reserved (photon, Euler–Mascheroni constant, Dirac matrices). |

### Information theory (Chapter 8)

| Concept | Font | Symbols |
|---------|------|---------|
| Entropy (operational) | Greek | $\eta_q = (2q - 1)/q^3$ |
| Information bandwidth | fraktur | $\mathfrak{B}(q)$ — information bandwidth per Planck time, a scalar function of $q$; not a sheaf, hence relocated from $\mathcal{B}(q)$ to fraktur (Phase 5n). |
| Lyapunov exponent | Greek | $\chi_q = 1/(2q - 1)$. Distinct from $\chi_\zeta(c)$ (character). |

### Descartes universe (Chapter 9)

| Concept | Font | Symbols |
|---------|------|---------|
| Elliptic curve | calligraphic | $\mathcal{E}_q$ — Descartes elliptic curve. Never $E_q$ for a curve. |
| Gravitational constant | Latin cap | $G_q$ — gravitational constant; $G_{\mathrm{Planck}} = 1$ (exact). |
| Julia-set measure | Greek | $\mu_J$ — measure on Julia set |
| Weierstrass | fraktur cap | $\wp(z)$ — Weierstrass elliptic function on $\mathcal{E}_q$. Reserved. |

### Particle interactions (Chapter 10)

| Concept | Font | Symbols |
|---------|------|---------|
| $C_5$ invariants | functional | $p_1(c)$ (power sum), $h_2(c)$, $h_3(c)$ (Hermitian), $\chi_\zeta(c)$ (character) |
| Color | plain italic | $c$ (color vector), $c_r$, $c_g$, $c_b$ (tube coords), $\hat{c}$, $\hat{c}_r$ (chromaticity) |
| Energy | fraktur | $\mathfrak{E}_q$ ($q$-energy), $\mathfrak{E}_\times$ (crossing), $\mathfrak{E}_{\mathrm{bind}}$ (binding), $\mathfrak{E}_0$ (hadronic energy scale, single-Planck-tick form $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV; tower-summed form $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2)$; truncations $\mathfrak{E}_0^{(N)}$ for depth $N$). Relocated from bold $\mathbf{E}$ to fraktur in Phase 5n — matches the fraktur "physical observable" convention. **Never confuse $\mathfrak{E}_0$ with $Q_\beta(n)$** — see [collisions](./notation-collisions.md). |
| Mass (categorical) | fraktur | $\mathfrak{m}$, $\mathfrak{m}_{\mathfrak{H}}$ (hadron). Never plain $m$ for categorical mass. |
| Photon | Greek | $\gamma$ — photon (standard physics convention). Used in pair-production / Breit–Wheeler vertices ($\gamma\gamma \to e^+ e^-$) and photonic channels. Distinct from the Euler–Mascheroni constant $\gamma$ (only ever appears inside zeta-value identities) and from Dirac matrices $\gamma^\mu$ (always with a Lorentz index). **Never** use $\gamma$ for a vortex morphism — the vortex is $\varrho$ (see [the Frobenius--Hopf substrate definition](#def:frobenius-hopf-substrate)). |
| $q$-Hamiltonian | hat | $\hat{H}_q$ — operator hat, Dirac convention. Distinct from $\mathcal{H}_q$ and $H_n(q)$. |

### Observations (Chapter 11)

| Concept | Font | Symbols |
|---------|------|---------|
| Derived constants | plain italic | $c_q = 1/(q - 1)$ (speed of light), $\hbar_q = (q - 1)/q$ (Planck), $d_H(q) = (2q - 1)^2/q^3$ (Hausdorff dimension) |
| Mass number | Latin cap | $A = Z + N$ |
| Neutron number | Latin cap | $N$ |
| Particles | fraktur | $\mathfrak{u}$, $\mathfrak{d}$, $\mathfrak{s}$, $\mathfrak{c}$, $\mathfrak{b}$, $\mathfrak{t}$ (quarks); $\mathfrak{p}$, $\mathfrak{n}$ (proton, neutron); $\mathfrak{H}$, $\mathfrak{H}_p$ (hadron, localised) |
| Proton number | Latin cap | $Z$ — atomic number. Never use $p$ for proton count; $p$ is reserved for brane points. |

### Lean source convention (cross-chapter)

Applies to every `.lean` file in the paper. Mirrors
[`CLAUDE.md` §7c](https://github.com/litlfred/qou/blob/main/CLAUDE.md#7c-base-ring-convention-generic-r-vs-archimedean-r-strict).

| Concept | Font | Symbols |
|---------|------|---------|
| Generic base ring | Latin cap | $R$ — type variable in Lean (`{R : Type*}` with the weakest typeclass that admits the construction: `[CommRing R]`, `[Field R]`, `[GroupWithZero R]`, etc.). Default for **all** categorical / algebraic / q-deformation / Wenzl–Hecke–Hoefsmit structural data. |
| Archimedean base ring | blackboard bold | $\mathbb{R}$ (`ℝ` in Lean) — used **only past the archimedean wall**: any declaration that genuinely needs `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`, `Real.log`, an ordering predicate (`0 < q`), `linarith`, or a CODATA / experimental numerical value. Narrative side: $q \in R$ when only the algebraic structure matters; $q \in \mathbb{R}$ only for archimedean evaluation (e.g. $q_0 = 1.109978595554181\ldots$ (50 dps)). |
