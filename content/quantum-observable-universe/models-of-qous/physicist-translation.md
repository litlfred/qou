In the archimedean realization
([archimedean QOU](#ex:c-quantum-observable-universe))
where $\mathbf{C} = \mathbf{Vect}_{\mathbb{R}}$,
$A = C^{\infty}(M)$ for a Riemannian manifold $M$, and
$\nabla$ is an Ehresmann connection on a principal $G$-bundle
$P \to M$, the three constituents of the
([categorical action](#def:categorical-action)) acquire their
classical meanings:

1. The *categorical trace* $\mathrm{tr} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes {-}) \circ \mathrm{coev}_A$
   becomes integration against the volume form:
   $\mathrm{tr}(\cdot) \to \int_M (\cdot)\mathrm{dvol}$.

2. The *physics endomorphism* $\Phi_q = \mathcal{L}_q$ becomes
   the Lagrangian density $\mathscr{L}(x)$, a section of the
   density bundle.

3. The *categorical Dirac operator* $\mathcal{D}_\nabla$ reduces
   to the gauge-covariant Dirac operator $D\!\!\!\!/ = \gamma^\mu D_\mu$.

The three-term decomposition
([Proposition](#prop:qou-canonical-action)) then reads

$$
  \mathfrak{S}_q
   \longrightarrow 
  \frac{1}{16\pi G}\!\int_M R\mathrm{dvol}
  - 
  \frac{1}{4g^2}\!\int_M \mathrm{Tr}(F \wedge \star F)
  + 
  \int_M \bar\psi D\!\!\!\!/\psi\mathrm{dvol},
$$

the Einstein--Hilbert + Yang--Mills + Dirac action, with $q \to 1$.
The coupling constants $G$, $g$ emerge from the normalization of the
Frobenius form $\int_A$ and the substrate parameter $q$ respectively;
they are not free parameters of the categorical theory but are
determined by the choice of archimedean realization.
