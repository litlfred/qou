<!-- FILE_START: nuclear-stability-observations-intro.md -->
Large-scale intermittency suggests a substrate parameter approaching a critical value. We examine this boundary inside the nucleus. The following blocks provide the computational tools for pushing density beyond nuclear saturation in the strangelet-stability section:
- Representative stable isotopes: Coulomb ratio and Diophantine error tabulates the Coulomb-to-strong ratio along the valley of stability and reports the Diophantine residue.
- The golden ratio as the boundary of stable chiral structure identifies $q_{\mathrm{gold}} = 1/\varphi^2$ as the threshold where chiral structure dissolves.
- Hydrogen: the simplest atom in knot form performs the explicit calculation for hydrogen.
- Discrete regime switches in SDP cross-channel couplings across isotopes records the discrete regime changes the SDP coupling exhibits as isotope number increases.
<!-- FILE_END: nuclear-stability-observations-intro.md -->

<!-- FILE_START: golden-ratio-degeneration.md -->
The Descartes elliptic curve $\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)) degenerates at a value of $q$ determined by the golden ratio.

With $s = \sqrt{q}$, the second Weierstrass coefficient factors as:

$$
  s^3 \cdot r(q)
  = 
  \frac{5(s^2 + s - 1)(4s^4 - s^3 - 4s^2 + s + 4)}{27}.
$$

The factor $(s^2 + s - 1)$ vanishes at:

$$
  s =  \frac{\sqrt{5} - 1}{2}
  =  \frac{1}{\varphi}
  =  \varphi - 1,
$$

where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio. Since $q = s^2$, this yields the golden ratio threshold:

$$
  q_{\mathrm{gold}}
  =  \frac{1}{\varphi^2}
  =  \frac{3 - \sqrt{5}}{2}
   \approx  0.382.
$$

At $q = q_{\mathrm{gold}}$, the constant term $r(q)$ vanishes and the Weierstrass equation reduces to $y^2 = x^3 + p(q_{\mathrm{gold}})x = x(x^2 + p)$. The curve acquires a node at the origin. The smooth elliptic fiber pinches to a rational curve with a double point. The chiral fibration of Bring's surface loses its elliptic structure — the three color tubes $(r, g, b)$ collapse to a degenerate configuration where two roots coincide.

**Origin of the golden ratio.**

The polynomial $s^2 + s - 1$ is the minimal polynomial of $1/\varphi$ over $\mathbb{Q}$. Its appearance in the Weierstrass coefficient is mathematically rigid. The Bring's surface is defined by $\sum x_i = \sum x_i^2 = \sum x_i^3 = 0$ in $\mathbb{CP}^4$. The $S_5$ symmetry of this quintic acts on the Lagrange resolvents through fifth roots of unity $\zeta = e^{2\pi i/5}$. The golden ratio satisfies $\varphi = -2\cos(4\pi/5) = 2\cos(\pi/5)$, directly linking it to the $\zeta$-action on the color tube coordinates. The degeneration at $q = 1/\varphi^2$ occurs exactly when the substrate deformation resonates with the $S_5$ symmetry of Bring's surface.

**Physical significance.**

The golden ratio threshold divides the $(q, \chi)$ parameter space into three regimes:

| Regime | $q$ | $\mathcal{E}_q$ | Chiral structure | Nuclear stability |
| --- | --- | --- | --- | --- |
| Sub-golden | $q < 1/\varphi^2$ | singular | degenerate | no stable hadrons |
| Classical band | $1/\varphi^2 < q < 1$ | smooth | intact but sub-classical | symmetric nuclei ($n = p$) |
| Physical | $q > 1$ | smooth, $\Delta < 0$ | one real component | full nuclear chart |

Our universe sits at $q = q_0$, well above the golden threshold. The distance from the degeneration,

$$
  q_0 - q_{\mathrm{gold}}
  =  1.110 - 0.382
  =  0.728,
$$

measures the stability margin of the Descartes universe. It quantifies how far the chiral elliptic fiber is from collapsing.

**The golden ratio in other contexts.**

The appearance of $\varphi$ in the Descartes universe connects to its role in related algebraic structures:

* **Penrose tilings**: $\varphi$ governs the quasicrystalline order of Penrose tilings. These are projections of the $A_4$ root lattice, which shares the $S_5$ symmetry underlying Bring's surface.
* **Fibonacci phyllotaxis**: The golden angle $2\pi/\varphi^2 \approx 137.5^\circ$ optimises packing on surfaces, reflecting the same algebraic constraint $(s^2 + s - 1 = 0)$ that governs the chiral degeneration.
* **$E_8$ and the icosahedron**: The golden ratio arises in the McKay correspondence for the icosahedral group (order $60$), which is $A_5 \cong S_5/\mathbb{Z}_2$ (the quotient of the symmetry group of Bring's surface by its centre).

The golden ratio is not an input to the QOU framework. It emerges strictly from the $S_5$ symmetry of the quintic and the requirement $\chi(A) = -6$. Its status as the boundary of stable chiral structure is a derived consequence of the Descartes universe.
<!-- FILE_END: golden-ratio-degeneration.md -->

<!-- FILE_START: hydrogen-knot-structure.md -->
**Example.**
Hydrogen $\mathcal{A}(1, 0)$ is the simplest atom: one proton, zero neutrons, one electron.

$$
  \mathcal{A}(1, 0)
  = 
  \underbrace{
    \mathcal{B}_3(\nu_r, \nu_g, \nu_b) \oplus \mathcal{L}_H
  }_{\mathfrak{p}\text{ (proton)}}
   \oplus 
  \underbrace{T_{2,3}}_{e^-\text{ (electron)}}
$$

**Knot inventory.**

See [Table 1](#tbl:hydrogen-knot-structure-table1-data).

Total: **3 unknots** + **1 trefoil**, linked by **1 Borromean** + **2 Hopf** links.

**Mass budget.**

See [Table 2](#tbl:hydrogen-knot-structure-table2-data).

The proton's $938$ MeV derives entirely from the Borromean linking of three massless unknots. The electron's $0.511$ MeV derives from vacuum drag (the only mass mechanism for a free trefoil with zero hyperbolic volume). The binding energy ($-13.6$ eV) is negligible on this scale.

**Ionization energy.**

The electron $T_{2,3}$ is Hopf-linked to the proton at the ground state ($n = 1$). The ionization energy is:

$$
  E_{\mathrm{ion}} =  \frac{m_e \cdot \alpha^2}{2}
  =  13.6 \text{ eV}
$$

Here $\alpha$ is the fine structure constant. The framework relates $\alpha$ to the substrate parameter via:

$$
  \alpha =  \frac{\tanh(\ln q)}{C_{\mathrm{geom}}}
$$

The fundamental formula for $\alpha$ is the EM coupling projection ([EM coupling projection](#prop:em-coupling-projection)):

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

The antisymmetric eigenvalue of the $R$-matrix $q^{-1}$ provides the bare coupling at a single crossing. The terms $[9]_q$ and $[10]_q$ are the $q$-deformed crossing numbers of the strong ($T_{2,9}$) and weak ($T_{3,5}$) force-carrier generators. At $q = q_0$, this yields the bare value $\alpha^{-1} \approx 136.82$. Including the Chern-Simons correction from the force-carrier torus knots ([EM coupling projection](#prop:em-coupling-projection)) yields $\alpha^{-1} \approx 137.036$ ($2.1\;\mathrm{ppm}$ from CODATA).

The two formulations are consistent: $\tanh(\ln q) / C_{\mathrm{geom}} = q^{-1}/([9]_q \cdot [10]_q)$. This fixes $C_{\mathrm{geom}}$:

$$
  C_{\mathrm{geom}}
  = 
  \frac{\tanh(\ln q) \cdot [9]_q \cdot [10]_q}{q^{-1}}
  = 
  \frac{(q^2 - 1) \cdot [9]_q \cdot [10]_q}{q^2 + 1}
   \approx  14.26.
$$

**Physical reading:** the electromagnetic coupling is the antisymmetric braiding eigenvalue $q^{-1}$ divided by the total topological complexity $[9]_q \cdot [10]_q$ of the strong and weak force sectors. In the crossing-asymmetry form $\alpha = \tanh(\ln q)/C_{\mathrm{geom}}$, the factor $\tanh(\ln q) = (q - q^{-1})/(q + q^{-1})$ acts as the EM-to-strong ratio, while $C_{\mathrm{geom}}$ absorbs the force-carrier $q$-integers.

The $\alpha^2$ dependence of the ionisation energy reflects **two Skein resolutions**: the mediating photon must resolve one crossing at the electron and one at the proton.

**Shell transitions.**

Exciting the electron from shell $n$ to shell $n'$ alters the Hopf linking level. The energy is:

$$
  \Delta E_{n \to n'}
  =  13.6 \left(\frac{1}{n^2} - \frac{1}{n'^2}\right)
  \text{ eV}
$$

The $1/n^2$ dependence emerges from the Skein resolution of the Hopf link at linking level $n$: the crossing energy of a level-$n$ Hopf link scales as $1/n^2$ because the Seifert surface area grows as $n^2$.

See [Table 3](#tbl:hydrogen-knot-structure-table3-data).
<!-- FILE_END: hydrogen-knot-structure.md -->

<!-- FILE_START: sdp-regime-switch.md -->
*The semidefinite-programming (SDP) extension of the LP-dual operator-selection framework ([BW coefficient shadow price](#prop:mass-coefficient-shadow-price)) introduces matrix-valued cross-block couplings $c_{\lambda\lambda'}$. These couple conjugate-partition pairs in the Wedderburn decomposition of $H_n(q)$. At fixed substrate parameter $q_0$, these couplings vary discretely with $(Z, N)$. Isolated zeros mark nuclear-structure regime switches (shell closures, pairing transitions, and jet-level crossings).*

*At each $(Z, N)$, the atom braid word $W_{\mathrm{atom}}$ has a YSN character $\chi_\lambda(W)$ in every irrep $\lambda$. These characters serve as primal observables driving the SDP:*

$$
  \Phi_{\lambda\lambda} \;=\; \frac{|\chi_\lambda(W)|^2}{\lVert W \rVert^2}
$$

*The SDP dual has a $2 \times 2$ PSD block per conjugate pair $(\lambda, \lambda')$:*

$$
  \begin{pmatrix}
    \mu_\lambda - y_0 - y_\lambda & c_{\lambda\lambda'} \\
    c_{\lambda\lambda'} & \mu_{\lambda'} - y_0 - y_{\lambda'}
  \end{pmatrix}
  \;\succeq\; 0
$$

*Here, $\mu_\lambda$ is the $q$-Laplacian eigenvalue ([$q$-heat kernel Peter-Weyl](#prop:q-heat-kernel-peter-weyl)) and $c_{\lambda\lambda'}$ is the coupling determined by the atom observables.*

*A regime switch occurs at $(Z, N)$ values where $c_{\lambda\lambda'} \to 0$. The PSD block drops from rank 2 to rank 1, the active-constraint set of the SDP jumps, and the atom's density matrix loses coherence between $\lambda$ and $\lambda'$.*

$\square$

**Witness.** The script `computations/sdp_cross_channel.py` implements `sdp_with_atom_observables(Z, N, partition_entries, pair_couplings)` using the `cvxpy` SDP solver. It falls back to a scalar LP if `cvxpy` is unavailable.
<!-- FILE_END: sdp-regime-switch.md -->

<!-- FILE_START: sdp-regime-switch-interpretation.md -->
**Observed sign-flip pattern** (computed at $q = q_0 \approx 1.11$, $k$-cap $= 5$, pairs at $H_4(q) \oplus H_5(q)$):

See [Table](#tbl:sdp-regime-switch-table-data).

*Key features observed*:

1. **Sign flips**: each coupling changes sign multiple times across the isotope chain. The zero-crossings (marked $\approx 0$) correspond to specific isotopes.
2. **Shell-closure signatures**: ${}^{3}\mathrm{He}$, ${}^{11}\mathrm{B}$, and ${}^{40}\mathrm{Ca}$ all sit at near-zero couplings — these are the SDP's markers for N=1 (trivial shell), N=6 (closed $p_{3/2}$), and Z=N=20 (double-magic $s\text{-}d$ shell closure).
3. **Isoscalar vs isovector structure**: the $(3,1)$$\leftrightarrow$$(2,1,1)$ pair changes sign most frequently (sensitive to N vs Z parity); the $(3,2)$$\leftrightarrow$$(2,2,1)$ pair varies most smoothly (less sensitive to individual-nucleon structure).

**Physical interpretation** (conjectural — awaiting Lean formalisation and experimental comparison):

- The SDP couplings $c_{\lambda\lambda'}$ act as the categorical analogues of density-matrix coherence elements between Wedderburn sectors.
- Zero couplings mark nuclear configurations where the atom's projection loses phase coherence between $\lambda$ and $\lambda'$. This is equivalent to the appearance of a conserved quantum number (shell closure, pairing gap, spin saturation).
- As $q$ is held fixed at $q_0$ (the substrate parameter from SnapPy $\mathrm{Vol}(4_1)$ and CODATA $m_\mu/m_e$), the $(Z, N)$ scan functions as a categorical probe of the Standard Model's discrete nuclear-structure hierarchy.

**Related**:
- Complementary to the LP-dual shadow prices ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)), which give only scalar per-partition variables.
- The $q$-dependence of the couplings $c_{\lambda\lambda'}(q)$ (varying $q$ at fixed $Z, N$) detects SUBSTRATE regime switches — cosmological transitions, Big-Bang to heat-death across the $q$-time coordinate ([$q$-heat equation](#def:q-heat-equation)). This extension is deferred to a future commit.
<!-- FILE_END: sdp-regime-switch-interpretation.md -->

