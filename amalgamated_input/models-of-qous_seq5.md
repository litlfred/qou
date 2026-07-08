<!-- FILE_START: categorical-differential-bridge-intro.md -->
The archimedean Hartree computations of the predicted-spectra chapter require an inner-product structure. The categorical framework does not supply this metric on its own. We must extract it from the Levi-form substrate. This section constructs that bridge.

We proceed in three steps. First, we identify the substrate parameter via the Levi form. Second, we introduce the Webster inner product. Third, we package this geometric structure into the categorical metric required by the Hartree computations.

The output is a categorical metric promoted from the Levi-form substrate. Readers focused exclusively on substrate-level statements may treat this bridge as a black box and defer the archimedean specialisation to Bring's surface.
<!-- FILE_END: categorical-differential-bridge-intro.md -->

<!-- FILE_START: c-substrate-via-levi.md -->
The abstract substrate parameter $q$ measures a connection's departure from classicality. We give its concrete archimedean realisation.

Let $A$ be an instanton connection on $P$. Let $F_A^+$ be its self-dual curvature. Let $L_\varTheta(V, W) = -id\varTheta(V, \bar{W})$ be the Levi form. Because $\Lambda^{1,1} H^* \subset \Lambda^+ H^*$ on the 4-dimensional distribution $H$, the Webster metric and Killing form define a natural contraction $\langle L_\varTheta, F_A^+\rangle_p \in \mathbb{R}$. The categorical substrate parameter over $\mathbb{C}$ or $\mathbb{R}$ evaluates to the smooth field

$$
  q(p) = 1 + \bigl\lvert\langle L_\varTheta, F_A^+ \rangle\bigr\rvert(p),
  \qquad p \in M.
$$

When the connection is classical ($F_A^+ = 0$), $q = 1$. In the deep-quantum regime, $q \to \infty$. 

All downstream quantities ($\hbar_q$, commutators, Yang–Mills action) are algebraic in $q$. Replacing $1 + x$ with $\exp(x)$ does not change the structural theory. We use the algebraic formula $1+x$ because it remains well-defined over an arbitrary base ring $R$. Non-archimedean analogues appear in subsequent chapters.
<!-- FILE_END: c-substrate-via-levi.md -->

<!-- FILE_START: webster-inner-product.md -->
We denote the inner product induced by the Webster metric $g_\varTheta$ on the horizontal distribution $H = \ker\varTheta$ and its exterior powers as $\langle \cdot, \cdot \rangle_\varTheta$. For vector fields $X, Y$ and differential forms $\alpha, \beta$:

$$
  \langle X, Y \rangle_\varTheta := g_\varTheta(X, Y),
  \qquad
  \langle \alpha, \beta \rangle_\varTheta := g_\varTheta(\alpha^{\sharp}, \beta^{\sharp}).
$$

This notation makes several dualities visually transparent:

- **Reeb duality.** The Reeb vector field $\xi$ is the metric dual to the contact form $\varTheta$: $\varTheta(X) = \langle \xi, X \rangle_\varTheta$ for all $X$.
- **Adjoint definition.** The $q$-codifferential $\delta_q$ is uniquely characterised by $\langle d_q\alpha, \beta \rangle_\varTheta = \langle \alpha, \delta_q\beta \rangle_\varTheta$.
- **Substrate contraction.** The natural contraction $\langle L_\varTheta, F_A^+ \rangle$ appearing in the substrate parameter is exactly the inner product $\langle \cdot, \cdot \rangle_\varTheta$ extended to bundle-valued $2$-forms.
<!-- FILE_END: webster-inner-product.md -->

<!-- FILE_START: observation-archimedean.md -->
Observing the universe changes it. The substrate parameter $q(p)$ is perturbed by condition (2). Every observation shifts the non-commutative geometry. In the archimedean realisation, an observation is a continuous open map from the spacetime base $M$ to the bundle of endomorphisms $\mathrm{End}(\mathcal{S}) \to M$, encoding the coordinate change in torsion energy of the bundle $\mathcal{S}$.
<!-- FILE_END: observation-archimedean.md -->

<!-- FILE_START: spatial-realization-functor.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **spatial realization** of $A$ is the space

$$
  M = \mathrm{Spec}(A) = \{ p \colon \mathbf{1} \to A \mid
  p \text{ is a categorical point} \}.
$$

This functor realises the algebra $A$ as a contact manifold. It sends the Frobenius form to the global contact $1$-form and the torus generator to the Reeb field. The target $M$ is an ordinary smooth manifold—the classical space whose function algebra $C^\infty(M)$ the fibre functor $\tau$ recovers from $A$. Concretely, $M$ is equipped with the following structures, derived purely within $\mathbf{C}$:

1. **Local germs.** For each point $p$, the *augmentation ideal* $\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$ captures the functions vanishing at $p$. The quotient $\mathfrak{m}_p / \mathfrak{m}_p^2$ is functorially dual to the tangent space $T_p M$. This gives the first-order germ decomposition

   $$
     A / \mathfrak{m}_p^2
      \cong 
     \mathbf{1} \oplus \mathfrak{m}_p / \mathfrak{m}_p^2.
   $$

2. **Kähler differentials.** The module $\Omega^1(A)$ of Kähler differentials exists in $\mathbf{C}$ by hypothesis. Under the fibre functor, $\tau(\Omega^1(A))$ maps to sections of the cotangent bundle $\Gamma(T^* M)$.

3. **The contact form.** The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces a canonical $1$-form $\varTheta_A \in \Omega^1(A)$ via pullback along the universal derivation $d \colon A \to \Omega^1(A)$.

4. **The Reeb derivation.** The generator $\xi$ of the maximal torus action satisfies the Cartan relations $\iota_\xi \varTheta_A = \mathrm{id}_{\mathbf{1}}$ and $\iota_\xi d\varTheta_A = 0$ within the non-commutative differential calculus.

```tex
\begin{equation}\label{eq:spatial-realization-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\tau"] \ar[d, "d"']
  & C^{\infty}(M) \ar[d, "d"] \\
  \Omega^1(A) \ar[r, "\tau"']
  & \Gamma(T^* M)
\end{tikzcd}
\qquad
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \varTheta_A \ar[r, mapsto, "\tau"]
  & \varTheta \\
  \xi \ar[r, mapsto, "\tau"']
  & \xi_{\mathrm{Reeb}}
\end{tikzcd}
\qquad\text{(spatial realisation)}
\end{equation}
```

Under $\tau$, these algebraic objects map to their geometric counterparts. $\varTheta_A$ becomes the global contact $1$-form $\varTheta$. $\xi$ becomes the Reeb vector field. Non-degeneracy of $\int_A$ guarantees that $d\varTheta$ is maximally non-degenerate on $\ker\varTheta$, which defines a contact manifold.
<!-- FILE_END: spatial-realization-functor.md -->

<!-- FILE_START: categorical-archimedean-bridge.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with weight decomposition $\pi_H, \pi_V$ and categorical $q$-exterior derivative $d_q$. 

Under the fibre functor $\tau$, the categorical and geometric definitions of $d_q$ coincide. The categorical vertical derivative $\pi_V \circ d$ corresponds to the geometric operation of contracting with the Reeb vector field $\xi$ and wedging with the contact form $\varTheta$. This correspondence forms a commuting square:

```tex
\begin{equation}\label{eq:categorical-archimedean-bridge-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\pi_V \circ d"] \ar[d, "\tau"']
  & \Omega^{k+1}(A) \ar[d, "\tau"] \\
  \Omega^k(M) \ar[r, "\varTheta \wedge \mathcal{L}_\xi"']
  & \Omega^{k+1}(M)
\end{tikzcd}
\qquad\text{(categorical--geometric bridge)}
\end{equation}
```

This states that $\tau(\pi_V \circ d) = \varTheta \wedge \mathcal{L}_\xi$, where $\varTheta$ is the contact form and $\mathcal{L}_\xi$ is the Lie derivative along the Reeb vector field.
<!-- FILE_END: categorical-archimedean-bridge.md -->

<!-- FILE_START: physicist-translation.md -->
In the archimedean realization where $\mathbf{C} = \mathbf{Vect}_{\mathbb{R}}$, $A = C^{\infty}(M)$ for a Riemannian manifold $M$, and $\nabla$ is an Ehresmann connection on a principal $G$-bundle $P \to M$, the three constituents of the categorical action acquire their classical meanings:

1. The *categorical trace* $\mathrm{tr} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes {-}) \circ \mathrm{coev}_A$ becomes integration against the volume form: $\mathrm{tr}(\cdot) \to \int_M (\cdot)\mathrm{dvol}$.
2. The *physics endomorphism* $\Phi_q = \mathcal{L}_q$ becomes the Lagrangian density $\mathscr{L}(x)$, a section of the density bundle.
3. The *categorical Dirac operator* $\mathcal{D}_\nabla$ reduces to the gauge-covariant Dirac operator $D\!\!\!\!/ = \gamma^\mu D_\mu$.

The three-term decomposition then reads

$$
  \mathfrak{S}_q
   \longrightarrow 
  \frac{1}{16\pi G}\!\int_M R\mathrm{dvol}
  - 
  \frac{1}{4g^2}\!\int_M \mathrm{Tr}(F \wedge \star F)
  + 
  \int_M \bar\psi D\!\!\!\!/\psi\mathrm{dvol},
$$

the Einstein–Hilbert + Yang–Mills + Dirac action, with $q \to 1$. The coupling constants $G$, $g$ emerge from the normalization of the Frobenius form $\int_A$ and the substrate parameter $q$ respectively. They are not free parameters of the categorical theory. They are determined by the choice of archimedean realization.
<!-- FILE_END: physicist-translation.md -->

<!-- FILE_START: categorical-action-vs-chern-simons.md -->
The classical Chern–Simons action \cite{witten1988}

$$
  S_{\mathrm{CS}}[A_{\mathrm{cl}}]
  =
  \frac{k}{4\pi}\!\int_M \mathrm{Tr}\!\left(
    A_{\mathrm{cl}} \wedge dA_{\mathrm{cl}}
    + \tfrac{2}{3}\, A_{\mathrm{cl}} \wedge A_{\mathrm{cl}} \wedge A_{\mathrm{cl}}
  \right)
$$

and the categorical action $\mathfrak{S} = \mathrm{tr}(\Phi)$ share a common skeleton. Both are scalar functionals built by tracing an internal morphism. (Here $A_{\mathrm{cl}}$ is a $\mathfrak{g}$-valued connection $1$-form on a $3$-manifold $M$, distinct from the QOU observable object $A \in \mathbf{C}$.) They diverge in their encoding of integration and trace:

| | Chern–Simons | Categorical |
|---|---|---|
| Domain | $3$-manifold $M$ | rigid monoidal $(\mathbf{C}, A, \tau)$ |
| Integration | $\int_M \{-\}$ | $\mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \{-\}) \circ \mathrm{coev}_A$ |
| Trace | Lie-algebra $\mathrm{Tr}_{\mathfrak{g}}$ | categorical (rigid) trace on $A$ |
| Dynamics | explicit $A_{\mathrm{cl}} \wedge dA_{\mathrm{cl}} + \tfrac{2}{3} A_{\mathrm{cl}}^{\wedge 3}$ | packaged inside $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ |

In the archimedean limit, the trace becomes $\int_M \{-\}\,\mathrm{dvol}$. The rigid loop closure $\mathrm{ev}_A \circ \{-\} \circ \mathrm{coev}_A$ yields spacetime integration without an independently postulated volume form. The rigid structure supplies it. The perturbative expansion $A_{\mathrm{cl}} = A_{\mathrm{cl}}^{(0)} + \mathcal{A}$ around a flat connection corresponds to fixing a background categorical connection and expanding $\Phi_q = \mathcal{D}_\nabla^2 + \cdots$ in fluctuations.

The bulk categorical action does not recover classical Chern–Simons. The archimedean image of $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ is the sum of the Einstein–Hilbert, Yang–Mills, and Dirac actions. Classical Chern–Simons enters the framework separately as a geometric knot invariant for non-hyperbolic torus knots.
<!-- FILE_END: categorical-action-vs-chern-simons.md -->

