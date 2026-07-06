We provide the classical meaning of the three constituents of the ([categorical action](#def:categorical-action)) in the archimedean realization ([archimedean QOU](#ex:c-quantum-observable-universe)). Here, we set $\mathbf{C} = \mathbf{Vect}_{\mathbb{R}}$ and $A = C^{\infty}(M)$ for a Riemannian manifold $M$. We let $\nabla$ be an Ehresmann connection on a principal $G$-bundle $P \to M$.

1. The *categorical trace* $\mathrm{tr} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes {-}) \circ \mathrm{coev}_A$
   becomes integration against the volume form:
   $\mathrm{tr}(\cdot) \to \int_M (\cdot)\mathrm{dvol}$.

2. The *physics endomorphism* $\Phi_q = \mathcal{L}_q$ becomes
   the Lagrangian density $\mathscr{L}(x)$, a section of the
   density bundle.

3. The *categorical Dirac operator* $\mathcal{D}_\nabla$ reduces
   to the gauge-covariant Dirac operator $D\!\!\!\!/ = \gamma^\mu D_\mu$.

The three-term decomposition ([Proposition](#prop:qou-canonical-action)) then reads

$$
  \mathfrak{S}_q
   \longrightarrow 
  \frac{1}{16\pi G}\!\int_M R\mathrm{dvol}
  - 
  \frac{1}{4g^2}\!\int_M \mathrm{Tr}(F \wedge \star F)
  + 
  \int_M \bar\psi D\!\!\!\!/\psi\mathrm{dvol},
$$

which recovers the Einstein--Hilbert + Yang--Mills + Dirac action in the limit $q \to 1$. The coupling constants $G$ and $g$ emerge from the normalization of the Frobenius form $\int_A$ and the substrate parameter $q$, respectively. They are not free parameters of the categorical theory; instead, the choice of archimedean realization determines them.
