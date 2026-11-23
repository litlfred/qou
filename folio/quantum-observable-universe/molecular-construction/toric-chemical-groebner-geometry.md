Because $\eta_2 \approx 1.77 \times 10^{-6} \ll 1$, Layer $\mathcal{L}_2$ nuclear cores remain invariant across ambient chemical transformations, reducing molecular reaction stoichiometry to integer lattice geometry and toric commutative algebra \cite{deloera-hemmecke-koeppe2013,craciun-dickenstein-shiu-sturmfels2009}.

### Smith normal form, lattice saturation, and the toric test-set hierarchy

Computing $\ker_{\mathbb{Z}}(A_{\mathrm{chem}})$ via Hermite or Smith normal form $U A_{\mathrm{chem}} V = \mathrm{diag}(d_1, \dots, d_r, 0, \dots, 0)$ yields a saturated free sublattice of $\mathbb{Z}^M$: even when invariant factors carry prime torsion in $\mathbb{Z}^E / A_{\mathrm{chem}}\mathbb{Z}^M$ (for instance $\mathrm{SNF}(A_{\mathrm{CHO}}) = \mathrm{diag}(1, 1, 2)$ owing to even hydrogen parity across $(\mathrm{C},\mathrm{H}_2,\mathrm{O}_2,\mathrm{CO},\mathrm{CO}_2,\mathrm{H}_2\mathrm{O},\mathrm{CH}_4)$), the kernel $\ker_{\mathbb{Z}}(A_{\mathrm{chem}})$ is torsion-free and generates the prime toric ideal

$$
  I_{A_{\mathrm{chem}}} := \bigl\langle x^{\nu_+} - x^{\nu_-} \;:\; \nu_+ - \nu_- \in \ker_{\mathbb{Z}}(A_{\mathrm{chem}})\bigr\rangle \subset k[x_1, \dots, x_M].
$$

Inside $\ker_{\mathbb{Z}}(A_{\mathrm{CHO}}) \cong \mathbb{Z}^4$, the support-minimal elementary circuits $\mathrm{Circ}(A_{\mathrm{CHO}})$, the universal Gröbner basis $\mathrm{UGB}(I_{A_{\mathrm{CHO}}})$, and the conformal-minimal Graver basis $\mathcal{G}(A_{\mathrm{CHO}})$ \cite{deloera-hemmecke-koeppe2013,hemmecke-koeppe-weismantel2014} form a strict chain of unoriented reaction pairs:

$$
  \bigl|\mathrm{Circ}(A_{\mathrm{CHO}})\bigr| = 20
  \;<\;
  \bigl|\mathrm{UGB}(I_{A_{\mathrm{CHO}}})\bigr| = 32
  \;<\;
  \bigl|\mathcal{G}(A_{\mathrm{CHO}})\bigr| = 33.
$$

### Zero-temperature Sturmfels–Thomas reduction and finite-temperature Birch equilibria

At $T \to 0$, minimizing molar enthalpy $h_f^\top u$ over the discrete stoichiometric fiber polytope $P_b \cap \mathbb{N}^M = \{u \in \mathbb{N}^M : A_{\mathrm{chem}} u = b\}$ reduces to monomial normal-form division modulo the $h_f$-oriented Gröbner test set \cite{sturmfels-thomas1997}. On the inventory $b = (2, 8, 4)^\top$ ($17$ feasible integer points in $P_b \cap \mathbb{N}^7$), unburned synthesis gas $u_0 = (0,4,1,2,0,0,0)$ ($2\,\mathrm{CO} + 4\,\mathrm{H}_2 + \mathrm{O}_2$) reduces confluently in three exothermic binomial rewrites to the unique integer-programming global minimum $u^* = (2,0,0,0,0,4,0)$ ($2\,\mathrm{C} + 4\,\mathrm{H}_2\mathrm{O}$).

At finite temperature $T > 0$, entropic mixing lifts the discrete boundary optimum into the positive interior $\mathbb{R}_{>0}^M$. Detailed-balance mass-action kinetics \cite{horn-jackson1972,feinberg1972,gatermann-huber2002,craciun-dickenstein-shiu-sturmfels2009} imposes the shifted toric binomial equations

$$
  x^{\nu_+} = K_{\mathrm{eq}}(\nu_+ - \nu_-)\,x^{\nu_-},
  \qquad
  K_{\mathrm{eq}}(v) = \exp\!\left(-\frac{v^\top g^\circ}{R T}\right),
$$

parameterized by elemental log-fugacity dual potentials $y \in \mathbb{R}^E$ via $x_j(y) = \exp\bigl((A_{\mathrm{chem}}^\top y)_j - g^\circ_j / (R T)\bigr)$ on the affine toric variety $V(I_{A_{\mathrm{chem}}}) = \mathrm{Spec}\,\mathbb{C}[\mathbb{N} A_{\mathrm{chem}}]$. Because the Legendre potential $\Phi(y) = \sum_{j=1}^M x_j(y) - b^\top y$ has strictly positive-definite Hessian $\nabla^2 \Phi(y) = A_{\mathrm{chem}}\,\mathrm{diag}(x(y))\,A_{\mathrm{chem}}^\top \succ 0$ on $\mathbb{R}_{>0}^M$, Birch's theorem \cite{birch1963} guarantees a unique positive equilibrium $x^* \in \mathbb{R}_{>0}^M$ in every stoichiometric compatibility class $A_{\mathrm{chem}} x = b$.
