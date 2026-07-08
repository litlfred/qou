<!-- FILE_START: orbital-symmetry-embedding-intro.md -->
We now determine which cohomological room the topological mass spectrum occupies. The orbital space at shell $n$ identifies as a space of sections of the normal bundle, allowing quantum numbers to be read directly from Fourier decompositions. We demonstrate that torus knot representations exhaust the first cohomology of the genus-$g$ surface, ensuring the knot generators fill the available cohomological space without redundancy.
<!-- FILE_END: orbital-symmetry-embedding-intro.md -->

<!-- FILE_START: orbital-space-normal-bundle.md -->
Let $T_{2,3} \hookrightarrow \Sigma_4$ be the trefoil embedded in Bring's surface, and let $N = N_{T_{2,3}/\Sigma_4}$ be its normal bundle. At shell $n$ (framing twist $k = 2(n-1)$ relative to the Seifert framing), the space of orbital states is:
$$
  \mathcal{O}_n
  = 
  \bigl\{
    \sigma \in \Gamma(N)  : 
    \mathrm{tw}(\sigma) = k, \quad
    \Delta_{T}\sigma = \lambda\sigma, \quad
    \lambda \leq \lambda_{n-1}
  \bigr\}
$$
where $\mathrm{tw}(\sigma)$ is the total twist, $\Delta_T$ is the ambient-induced Laplacian on $T_{2,3}$, and $\lambda_\ell$ is the $\ell$-th eigenvalue. This orbital space has dimension $\dim \mathcal{O}_n = n^2$.

The normal bundle $N$ is a rank-$2$ real vector bundle over $T_{2,3} \cong S^1$. A section $\sigma \in \Gamma(N)$ describes a transverse displacement of the trefoil. The total twist $\mathrm{tw}(\sigma) = k$ measures the self-linking number of the displaced curve relative to the Seifert surface, representing the global R-I count.

The $q$-Laplacian $\Delta_q$ on $T_{2,3} \cong S^1$ has eigenvalues $\lambda_\ell =  [\ell]_q  [\ell + 1]_q$ for $\ell = 0, 1, 2, \ldots$. Each eigenvalue $\lambda_\ell$ for $\ell \geq 1$ has multiplicity $2$.

At each point of the trefoil, the transverse displacement has two independent normal directions in the $3$-dimensional ambient space. A section $\sigma$ with Fourier mode $\ell$ and direction $\hat{n}$ parametrizes the same space as a spherical harmonic $Y_\ell^m$ on the unit sphere surrounding the proton. This identification holds because the trefoil orbits the proton, sweeping out a sphere. The magnetic quantum number $m = -\ell, \ldots, +\ell$ labels the $2\ell + 1$ orientations of the mode relative to the Reeb axis.

At shell $n$, the energy constraint admits modes $\ell = 0, 1, \ldots, n-1$. For each mode $\ell$, the section space transforms as the irreducible $\mathrm{SO}(3)$ representation $V_\ell$ of dimension $2\ell + 1$. The total orbital dimension is:
$$
  \dim \mathcal{O}_n
  = \sum_{\ell=0}^{n-1} \dim V_\ell
  = \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  n^2.
$$
The energy of mode $\ell$ at shell $n$ is $E_\ell = \frac{[\ell]_q  [\ell + 1]_q}{[n]_q^2} \cdot E_{\mathrm{ion}}$. The mode fits within shell $n$ exactly when $\ell \leq n - 1$.
<!-- FILE_END: orbital-space-normal-bundle.md -->

<!-- FILE_START: orbital-fourier-decomposition.md -->
Let $\varrho: S^1 \hookrightarrow \Sigma_4$ be the trefoil $T_{2,3}$ embedded in Bring's surface, and let $N = N_{\varrho/\Sigma_4}$ be the normal bundle. The four quantum numbers $(n, \ell, m, s)$ arise directly from the Fourier decomposition of sections $\sigma \in \Gamma(N)$.

At each point of the trefoil, $N_p \cong \mathbb{R}^2$. Let $\varTheta \in [0, 2\pi)$ parametrise the trefoil. A section decomposes into orthogonal modes:
$$
  \sigma(\varTheta)
  = \sum_{\ell=0}^{\infty} \bigl(a_\ell \cos(\ell\varTheta) + b_\ell \sin(\ell\varTheta)\bigr) \hat{n}_1(\varTheta)
  + \sum_{\ell=0}^{\infty} \bigl(c_\ell \cos(\ell\varTheta) + d_\ell \sin(\ell\varTheta)\bigr) \hat{n}_2(\varTheta)
$$
where $\hat{n}_1, \hat{n}_2$ form an orthonormal frame for $N$.

**(1) Principal quantum number $n$.**
The total twist $k = 2(n-1)$ constraints the total energy $E_n = -E_{\mathrm{ion}}/n^2$. The twist equates to the $L^2$ norm-squared of $\sigma$. At fixed $k$, only finitely many Fourier modes can be nonzero.

**(2) Angular momentum quantum number $\ell$.**
The $\ell$-th Fourier mode acts as a resonance frequency of the trefoil's transverse vibration, carrying eigenvalue $\lambda_\ell = [\ell]_q [\ell + 1]_q$ under the $q$-Laplacian. The $q$-deformation shifts the eigenvalues by order $\alpha^2$, producing fine-structure splitting between sub-shells at the same $n$.

**(3) Magnetic quantum number $m$.**
The $\mathrm{SO}(3)$ rotation group acts on $\mathbb{R}^3$ and the normal-bundle sections. Mode-$\ell$ sections transform as the irreducible representation $V_\ell$ of $\mathrm{SO}(3)$. The magnetic quantum number $m = -\ell, \ldots, +\ell$ labels the weight spaces relative to the Reeb axis.

**(4) Spin quantum number $s$.**
The fiber adjoint involution acts on the normal bundle by exchanging the two orientations of the Hopf link between electron and proton. This involution $\sigma \mapsto -\sigma$ splits each orbital $(n, \ell, m)$ into two eigenspaces ($s = \pm 1/2$), doubling the orbital count to $2n^2$ states per shell.

| Quantum number | Fourier origin | Representation |
|:-:|---|---|
| $n$ | Total framing twist $k = 2(n-1)$ | Energy shell |
| $\ell$ | Fourier mode on $S^1$ | $\mathrm{SO}(3)$ irreducible $V_\ell$ |
| $m$ | Weight in $V_\ell$ (Reeb projection) | Spherical harmonic $Y_\ell^m$ |
| $s$ | Fiber adjoint involution eigenvalue | Spin $\pm 1/2$ |
<!-- FILE_END: orbital-fourier-decomposition.md -->

<!-- FILE_START: fivefold-symmetry.md -->
Bring's surface $\Sigma_4$ possesses an $S_5$ automorphism group. This $5$-fold symmetry drives the crystallographic obstruction, defines the five sheets of $\Sigma_4$ (and the associated golden ratio phase transition), and determines the five-fold symmetry of the affine charts governing the generation partition.

See [Table 2](#tbl:fivefold-symmetry-table2-data).

The $3$-fold symmetry (Borromean, color, periodic) and $5$-fold symmetry (aperiodic, weak, parity-violating) serve as the two irreducible components of Bring's surface. Mediated by $T_{3,5}$, the strong force binds periodically, the weak force transforms aperiodically, and the electromagnetic force measures the interface.
<!-- FILE_END: fivefold-symmetry.md -->

<!-- FILE_START: fivefold-crystallographic-obstruction.md -->
A lattice $\Lambda \subset \mathbb{R}^n$ allows rotational symmetry of order $k$ only if $k \in \{1, 2, 3, 4, 6\}$ (for $n = 2, 3$). Periodic lattices cannot possess $5$-fold rotational symmetry. 

See [Table 1](#tbl:fivefold-symmetry-table1-data).

The $5$-fold symmetry of Bring's surface uniquely breaks periodicity. It is carried by $T_{3,5}$, the weak force mediator, which is the only force violating parity and utilizing massive carriers ($W^{\pm}$, $Z^0$). The weak force remains weak precisely because its $5$-fold symmetry confines it to local, aperiodic interactions.
<!-- FILE_END: fivefold-crystallographic-obstruction.md -->

<!-- FILE_START: fivefold-sheets-golden-ratio.md -->
Bring's curve $\Sigma_4$ is defined by $x_1^5 + \dots + x_5^5 = 0$ and $x_1 + \dots + x_5 = 0$ in $\mathbb{P}^3$. The $S_5$ action permutes the five coordinates. Each coordinate defines a sheet of the surface, glued together along the ramification locus. 

The five sheets meet at ramification points where two or more coordinates coincide. The regular pentagon inscribed in the unit circle links non-adjacent sheets via a "diagonal" connection ($T_{3,5}$ interaction) proportional to the golden ratio $\varphi \approx 1.618$. 

The $q$-AND polynomial $P_{7,6}(q)$ has a zero at $q = 1/\varphi^2 \approx 0.382$. This golden ratio phase transition eliminates the diagonal $T_{3,5}$ connection, degenerating the $5$-fold symmetry down to $3$-fold.
<!-- FILE_END: fivefold-sheets-golden-ratio.md -->

<!-- FILE_START: fivefold-affine-charts-generations.md -->
Each fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}$ serves as an affine chart. The $S_5$ symmetry acts directly on the space of these affine charts. The five sheets of Bring's surface correspond to five classes of affine charts. 

1. **Five observer types.** There are five topologically distinct embeddings of a fibre functor. Three sheets carry the matter families ($T_{2,3}, T_{2,5}, T_{2,7}$), while the remaining two carry the force mediators ($T_{2,9}, T_{3,5}$). 
2. **Aperiodic global structure.** Transition functions between distinct sheets invoke $5$-fold monodromy, establishing a globally aperiodic structure similar to a quasicrystal.
3. **Penrose tiling analogy.** The five affine chart types tile the base $\mathbb{P}(V)$ with local $5$-fold symmetry but no global period, governed by Gröbner--Shirshov relations.
<!-- FILE_END: fivefold-affine-charts-generations.md -->

<!-- FILE_START: klein-bring-icosahedral-bridge.md -->
A faithful icosahedral $A_5$-action exists on the categorical base $\mathbb{P}(V)$, realising Klein's icosahedral solution of the Bring–Jerrard quintic. The orbifold quotient is $\mathbb{P}(V)/A_5 \cong S^2(2,3,5)$, the base of the Seifert fibration $S^3/2I \to S^2(2,3,5)$ of the Poincaré homology sphere. Its order-$2$ and order-$3$ generators are geometrically distinct from the trefoil $S_3$ generators.

Bring's curve corresponds to the Bring–Jerrard normal form of the quintic. The orientation-preserving symmetry group of the $(2,3,5)$ spherical triangle is the icosahedral group $A_5$.

Klein's icosahedral generators on $\mathbb{P}(V)$ incorporate the $\zeta_5$ pentad $S \colon w \mapsto \varepsilon w$ as the order-5 element, paired with an icosahedral 2-fold operation $T$. These distinct generators assemble into $A_5$. The three exceptional $A_5$-orbits on $\mathbb{P}(V)$ have cyclic stabilisers determining the cone-point orders of the quotient, giving $\mathbb{P}(V)/A_5 = S^2(2,3,5)$. 

The $\zeta_5$ pentad and the colour trefoil are both parity-even, generating $A_5$. The EM involution $z\mapsto 1/z$ is parity-odd, falling in the coset $S_5\setminus A_5$. This establishes that the weak/colour sector corresponds to the even $A_5$ group, while EM relates to the odd coset. The single remaining component is the spectral identification associating the $\zeta_5$ pentad coordinate ratio $w$ to the spectral ratio $\eta$.
<!-- FILE_END: klein-bring-icosahedral-bridge.md -->

<!-- FILE_START: cohomological-embedding.md -->
The torus knots embeddable on the moduli surface $\Sigma_g$ form a complete set of representations, exhausting the available cohomology and spanning the space of knot observables.

**(i) Embeddability = representation.** A torus knot $T_{r,s}$ with $\gcd(r, s) = 1$ admits a representation in $\mathbf{C}$ if and only if its Seifert rank embeds in the first cohomology of $\Sigma_g$:
$$
  \mathrm{rank} H_1(\mathrm{Seifert}(T_{r,s}))
  =  \frac{(r-1)(s-1)}{2}  \leq  g
$$

**(ii) Fiber degree.** The maximum fiber degree for $T_{r, p^k}$ on $\Sigma_g$ is:
$$
  k_{\max}(r, p, g)
  = \max\!\left\{k : \frac{(r-1)(p^k - 1)}{2} \leq g\right\}
$$

**(iii) Completeness.** The Jones polynomials of embeddable torus knots span the space of knot invariants on $\Sigma_g$. 

**(iv) Genus 4 is forced.** The QOU axioms require $T_{2,3}$ and $T_{2,9}$ to embed, but $T_{2,11}$ must not. This uniquely forces $g = 4$ and $\chi = -6$.

See [Table 1](#tbl:cohomological-embedding-table1-data).

The cohomology of $\Sigma_4$ admits a knot basis:
$$
  H^*(\Sigma_4)
  = \underbrace{H^0 \oplus H^2}_{\dim 2} \oplus \underbrace{H^{1,0}}_{\dim 4} \oplus \underbrace{H^{0,1}}_{\dim 4}
$$

See [Table 2](#tbl:cohomological-embedding-table2-data).

The $6$ embeddable knots form a complete basis spanning the $5$-dimensional space of irrep characters. Every observable hadron is a composite of these 6 blocks, and every interaction is mediated by the 7 associated transfer matrices (including free propagation). Genus $4$ is the unique minimal environment that supports $\mathrm{SU}_2$ reconstruction and strong binding without introducing unobserved spurious matter.
<!-- FILE_END: cohomological-embedding.md -->

<!-- FILE_START: knot-basis-color-content.md -->
An element of $H_3(q)$ of the form
$$
  \gamma
  = \mathbf{1} + \varphi_0 \sigma_0 + \varphi_1 \sigma_1 + \varphi_{01} \sigma_0\sigma_1
$$
is called a photon with color content. Setting $\varphi_{01} = 0$ yields a 3-term linear specialization. Given two such elements $\gamma_1$ and $\gamma_2$, the Gröbner--Shirshov normal form of their product factors into:
$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = (1 + \varphi_0\psi_0 + \varphi_1\psi_1) \mathbf{1}
  + (\varphi_0 + \psi_0 + \varphi_0\psi_0h) \sigma_0
  + (\varphi_1 + \psi_1 + \varphi_1\psi_1h) \sigma_1
  + \varphi_0\psi_1 \sigma_0\sigma_1
  + \varphi_1\psi_0 \sigma_1\sigma_0.
$$
The normal form decomposes into the first five entries of the knot basis. Hopf-link terms (word length 2) arise exclusively from cross-color products, while length-1 terms reflect both additive contributions and Hecke self-energy corrections. Setting all weights to zero recovers $\gamma_1 \cdot \gamma_2 = \mathbf{1}$.
<!-- FILE_END: knot-basis-color-content.md -->

<!-- FILE_START: trivial-knot-photon-interpretation.md -->
The trivial knot operator $T_{1,0}$ implies a photon pair collision without inserted crossings. Every resulting structure derives strictly from the photons' inherent color content. The 16 cross-terms from the full expansion reduce to normal form via the Hecke and Yang--Baxter relations.

See [Table 1](#tbl:trivial-knot-photon-interpretation-table1-data).
See [Table 2](#tbl:trivial-knot-photon-interpretation-table2-data).
See [Table 3](#tbl:trivial-knot-photon-interpretation-table3-data).
See [Table 4](#tbl:trivial-knot-photon-interpretation-table4-data).
See [Table 5](#tbl:trivial-knot-photon-interpretation-table5-data).

**Vacuum channel ($\gamma$):** Co-polarized photons amplify the vacuum channel. The Hopf dressing $\varphi_{01}$ does not feed the vacuum.
**Linear polarization channels ($\sigma_0, \sigma_1$):** Receive symmetric additive and Hecke contributions, plus asymmetric twist-rotation terms where Hopf dressing converts into orthogonal polarization.
**Positive Hopf link ($L_+$):** Fed preferentially because the photon's internal twist is inherently positive ($L_+$).
**Negative Hopf link ($L_-$):** Restricted to cross-polarization and Hopf self-products, demonstrating a clear chirality signature.
**Electron channel ($e^-$):** Opens only when at least one photon carries Hopf dressing, supplying the necessary crossings to form a trefoil.

If all polarizations vanish, $\gamma_1 \cdot \gamma_2 = \mathbf{1}$. $L_+$ and $L_-$ vanish when photons are co-polarized on a single axis. Electrons cannot emerge from photons lacking twist content. The Hopf link functions as a $90^\circ$ polarization rotator: combining Hopf dressing with linear polarization absorbs the crossing and emits orthogonal polarization.
<!-- FILE_END: trivial-knot-photon-interpretation.md -->

<!-- FILE_START: outro-archimedean-universe.md -->
This concludes the Descartes-universe chapter, fixing Bring's surface ($\chi = -6$) as the spacetime base. The substrate parameter $q_0$, the gauge coupling $\alpha_{\mathrm{EM}}$, and the five-fold symmetric basis are now established. The subsequent particle-interactions chapter applies this basis and machinery to compute mass spectra and interaction dynamics under the Gröbner–Shirshov formalisms.
<!-- FILE_END: outro-archimedean-universe.md -->

