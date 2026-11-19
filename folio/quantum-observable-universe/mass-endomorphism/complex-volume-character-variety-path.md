The interpolation between the bound and free projections of [complex-volume unification](#conj:binding-qbeta-complex-volume) constitutes a path. The bar-odd channel provides its holonomy. No structure beyond the deformation itself is required to rotate between the bound and free states.

## Endpoints as representations

The free projection $\Pi_{\text{free}}$ drops inter-constituent confining crossings, retaining only linking data. It constructs the abelian representation of the knot group. The bound object—the full braiding—constructs the discrete-faithful side. These define the two distinguished points of the character variety of $K$.

## Path integral reading

Neumann and Zagier defined the complex volume as the integral of a holomorphic $1$-form along the path in the character variety connecting these representations \cite{neumann-zagier1985}. Transported to $\mathfrak{V}$:

$$
\mathfrak{V} \;=\; \Phi(\text{bound}) - \Phi(\text{free}),
\qquad
\mathfrak{E}_{\mathrm{bind}} = \mathrm{Re}\mathfrak{V},
\quad
\mathfrak{Q}_\beta = \mathrm{Im}\mathfrak{V},
$$

where $\Phi$ acts as a potential on the deformation path. The endpoint difference of $\Phi$ equals the projection defect $\mathrm{tr}_M\bigl((\Pi_{\text{free}} - \mathbf{1}) \circ \mathcal{M}\bigr)$. Its bar-even part represents the volume (binding) channel. Its bar-odd part captures the phase accumulated along the path. This matches how the Chern–Simons invariant acts as the phase companion to hyperbolic volume, consistent with the state-integral factorization picture \cite{garoufalidis-zagier-2024}. For the figure-eight knot this phase is extracted along a one-parameter path of irreducible $\mathrm{SL}(2,\mathbb{C})$ representations, with meridian eigenvalue $e^{u/2}$ for real $0 < u < 0.9624$, from the coloured Jones asymptotics jointly with the twisted Reidemeister torsion \cite[Thm.~1.4]{murakami-h2011}; that result says nothing about the abelian endpoint of the path.

In the literature, the classical limit of a quantum-dilogarithm integral knot invariant has saddle-point equations that coincide with the hyperbolicity (gluing) consistency conditions, and evaluates to a sum of Rogers dilogarithms when the geometrically preferred solutions dominate \cite[\S5, eq.~(5.20)]{hikami2001}. Completeness of that saddle-point picture and the choice of branch are not proved there.

## Categorical carrier

Prior to archimedean evaluation (over a generic ring $R$ with a bar involution), the deformation parameter $t$ of a single Askey–Wilson tridiagonal family carries the path. At $t = 0$, the family sits at the $q$-Hermite bottom of the scheme. Here, all Askey–Wilson parameters vanish, and the orthogonality measure uses the $q$-Plancherel weight $W_\lambda$, representing the free side. At $t = 1$, it supplies the bound channel data.

This is captured by the Askey–Wilson deformation-path hypothesis, which specifies the family, the $q$-Hermite free endpoint, the potential yielding $\mathfrak{V}$, and a single three-term ladder recurrence with a bar-even multiplier. The two-channel descent—where both the binding and $\mathfrak{Q}_\beta$ ladders satisfy the exact same recurrence—is a derived consequence of the recurrence involution-descent law, rather than an independent assumption.

## Falsifiable consequences

The hypothesis predicts one decidable numerical signature: the binding and $\mathfrak{Q}_\beta$ channel ladders share a single bar-even three-term multiplier. Equivalently, the multiplier solved from the complex ladder $\mathfrak{V}_A$ has a vanishing bar-odd part. This probes the holomorphic connection.

The mechanism remains computationally confirmed. The Hopf-power tower $\mathfrak{V}_n = \mathrm{tr}_M\bigl((\sigma_1^2)^n\bigr)$ strictly follows a three-term recurrence with the bar-even multiplier $q^2 + q^{-2}$ (the continuous $q$-ultraspherical class), exercising the recurrence involution-descent mechanism end-to-end. 

The physical identification—that the measured $c_k$-ladder exemplifies this mechanism—remains open; it depends on the even-channel $c_3$. Along the isotope triples $({}^2\mathrm{H}, {}^3\mathrm{H}, {}^4\mathrm{He})$ and $({}^2\mathrm{H}, {}^3\mathrm{He}, {}^4\mathrm{He})$, the parity split of the log-trace binding proxy does not share one bar-even multiplier. This refutes that specific ladder construction, but leaves the underlying mechanism—confirmed at the fibre level by the Hopf tower—intact.
