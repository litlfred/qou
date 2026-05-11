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
| Jones–Markov central coefficient | plain italic | $y_\lambda$ — coefficient in $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$, given by Wenzl's hook–content closed form [wenzl1988]. Sign-indefinite at $n \geq 4$. Distinct from the Plancherel measure $w_\lambda$ and the q-deformed Wedderburn-block weight $\tilde w_\lambda$ at $q \neq 1$ — coincides with $w_\lambda$ only on the self-conjugate stratum (see [`prop:wedderburn-weight-canonical`](../braids-and-knots/wedderburn-weight-canonical.md)). Never confuse with $u_\lambda$ (LP shadow-price). |
| LP shadow-price | plain italic | $u_\lambda, u_0$ — Schrijver linear-programming convention for operator-selection LP dual variables. Non-negative by LP duality. Never write $y_\lambda$ here. |
| Markov parameter | plain italic | $z = 1/(r + r^{-1})$ — equivalently $1/(q^{1/2} + q^{-1/2})$. |
| Mass (knot) | fraktur | $\mathfrak{m}_{\mathcal{K}}$ — knot mass. |
| Plancherel measure (classical) | plain italic | $w_\lambda := (\dim V_\lambda)^2 / n!$ — the classical Plancherel probability measure on partitions $\lambda \vdash n$, with $\dim V_\lambda$ the $q$-independent (classical) Hecke-irrep dimension (= number of standard Young tableaux of shape $\lambda$). Sums to $1$ exactly in $\mathbb{Q}$. See [`prop:plancherel-weight-boundedness`](../braids-and-knots/plancherel-weight-boundedness.md). **Distinct** from the q-deformed Wedderburn-block weight $\tilde w_\lambda$; the two coincide at $q = 1$ only. |
| Quantum dimension | plain italic | $\dim_q(\lambda) = [n]_q! / \prod_{x \in \lambda} [h_x]_q$ — the $q$-deformed Frame–Robinson–Thrall hook-length dimension. Reduces to $\dim V_\lambda$ at $q = 1$. Used in the q-deformed Wedderburn-block weight $\tilde w_\lambda = \dim_q^2(\lambda)/[n]_q!$. |
| Spinor information rate | plain italic | $r$ — eigenvalue of the elementary half-twist on the spin-½ fundamental rep of $\mathrm{SU}_q(2)$, $r^2 = q$. The "rate per half-twist" along a single linear braid (no surface area). Analogous to $i: -1$ as $r: q$ — the algebraic ingredient that lifts the 1-D adjoint braid algebra to the 2-D spinor (spin-½) representation. **Never** use $t$ (clashes with $V_K(t)$ knot variable) or $\iota$ (clashes with involution / inclusion). |
| Wedderburn-block weight (q-deformed) | plain italic with tilde | $\tilde w_\lambda := \dim_q^2(\lambda) / [n]_q!$ — the q-deformed analogue of the classical Plancherel measure $w_\lambda$. **Not** a probability measure at $q \neq 1$: empirically $\sum_\lambda \tilde w_\lambda \approx 1.51$ at $q_0 \approx 1.1097$ for $n = 12$. Specialises to $w_\lambda$ at $q = 1$. Used in [`prop:plancherel-term-7-formulation`](../braids-and-knots/plancherel-term-7-formulation.md) and the q-deformed Wedderburn-block normalisation of [`prop:wedderburn-weight-canonical`](../braids-and-knots/wedderburn-weight-canonical.md). **Never** call this "Plancherel weight" without the tilde — the classical Plancherel $w_\lambda$ is a different, smaller object. |
| Wenzl principal-spec length | Greek | $\ell$ — number of points in the Schur principal specialisation $s_\lambda(1, q^2, q^4, \ldots, q^{2(\ell-1)})$ defining $y_\lambda$ via Wenzl's formula. **Renamed from $r_W$** to free $r$ for the spinor rate above. |

### Algebraic substrate (Chapter 6)

| Concept | Font | Symbols |
|---------|------|---------|
| $q$-shuffle Hopf algebra | calligraphic | $\mathcal{H}_q$ — convolution algebra of $\mathrm{End}_{\mathbf{C}}(A)$ under $\ast_q$; carries the grouplikes $\exp_q$, $\log_q$, $\mathrm{Li}_2^q$. Never plain $H_q$. |
| Goncharov period filtration | calligraphic | $\mathcal{P}_n$ — weight-$n$ periods in the Goncharov motivic filtration ([Kontsevich–Zagier, Goncharov]). Used in [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence). Distinct from $P_\ell$ (elementary symmetric polynomials in JM elements, [`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)). |
| Primitive root of unity | Greek + sub | $\zeta_n := e^{2\pi i / n}$ — primitive $n$-th root of unity. **Always with subscript:** $\zeta_5$ for Bring $S_5$-symmetry shape, $\zeta_6 = e^{i\pi/3}$ for figure-8 ideal-tetrahedron shape. **Never bare $\zeta$** (collides with Riemann zeta $\zeta(s)$ — always parenthesised — and with character $\chi_\zeta$ — always with $\chi$ prefix). |
| Vortex morphism | Greek | $\varrho \colon \mathbf{1} \to A$ — generic closed vortex. Never $\gamma$ for a vortex; $\gamma$ is reserved. |

### Information theory (Chapter 8)

| Concept | Font | Symbols |
|---------|------|---------|
| Entropy (operational) | Greek | $\eta_q = (2q - 1)/q^3$ |
| Information bandwidth | calligraphic | $\mathcal{B}(q)$ — information bandwidth per Planck time |
| Lyapunov exponent | Greek | $\chi_q = 1/(2q - 1)$. Distinct from $\chi_\zeta(c)$ (character). |

### Descartes universe (Chapter 9)

| Concept | Font | Symbols |
|---------|------|---------|
| Elliptic curve | calligraphic | $\mathcal{E}_q$ — Descartes elliptic curve. Never $E_q$ for a curve. |
| Gravitational constant | Latin cap | $G(q)$ — gravitational constant; $G_{\mathrm{Planck}} = 1$ (exact). |
| Julia-set measure | Greek | $\mu_J$ — measure on Julia set |
| Weierstrass | fraktur cap | $\wp(z)$ — Weierstrass elliptic function on $\mathcal{E}_q$. Reserved. |

### Particle interactions (Chapter 10)

| Concept | Font | Symbols |
|---------|------|---------|
| $C_5$ invariants | functional | $p_1(c)$ (power sum), $h_2(c)$, $h_3(c)$ (Hermitian), $\chi_\zeta(c)$ (character) |
| Color | plain italic | $c$ (color vector), $c_r$, $c_g$, $c_b$ (tube coords), $\hat{c}$, $\hat{c}_r$ (chromaticity) |
| Energy | bold | $\mathbf{E}_q$ ($q$-energy), $\mathbf{E}_\times$ (crossing), $\mathbf{E}_{\mathrm{bind}}$ (binding). Never $\mathfrak{E}$. |
| Mass (categorical) | fraktur | $\mathfrak{m}$, $\mathfrak{m}_{\mathfrak{H}}$ (hadron). Never plain $m$ for categorical mass. |
| $q$-Hamiltonian | hat | $\hat{H}_q$ — operator hat, Dirac convention. Distinct from $\mathcal{H}_q$ and $H_n(q)$. |

### Observations (Chapter 11)

| Concept | Font | Symbols |
|---------|------|---------|
| Derived constants | plain italic | $c_q = 1/(q - 1)$ (speed of light), $\hbar_q = (q - 1)/q$ (Planck), $d_H(q) = (2q - 1)^2/q^3$ (Hausdorff dimension) |
| Mass number | Latin cap | $A = Z + N$ |
| Neutron number | Latin cap | $N$ |
| Particles | fraktur | $\mathfrak{u}$, $\mathfrak{d}$, $\mathfrak{s}$, $\mathfrak{c}$, $\mathfrak{b}$, $\mathfrak{t}$ (quarks); $\mathfrak{p}$, $\mathfrak{n}$ (proton, neutron); $\mathfrak{H}$, $\mathfrak{H}_p$ (hadron, localised) |
| Proton number | Latin cap | $Z$ — atomic number. Never use $p$ for proton count; $p$ is reserved for brane points. |
