Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def\:quantum-observable-universe)) with
Hecke algebra $H_n(R, q)$
([Hecke algebra](#rem\:hecke-algebra-from-braiding)) and Markov trace
$\mathrm{tr}_M \colon H_n(R, q) \to k$
([Jones--Markov trace](#thm\:jones-markov-trace)).

Let $\varrho \colon \mathbf{1} \to A$ be a vortex morphism with braid
representative $\beta \in B_n$.  The **mass integrand**
([mass identity](#def\:mass-identity)) is the composition

$$
  \alpha_\varrho
  =
  (\textstyle\int_A \otimes \mathrm{id})
  \circ \Delta
  \circ \varrho
  \colon \mathbf{1} \to A,
$$

which, via left multiplication in the Frobenius--Hopf algebra $A$,
determines an endomorphism
$L_{\alpha_\varrho} \in \mathrm{End}_{\mathbf{C}}(A)$.
Since all constituent maps ($\Delta$, $\int_A$, $\varrho$) are morphisms
in $\mathbf{C}$, the fibre-functor image $\tau(L_{\alpha_\varrho})$ is
an $\mathrm{SU}_q(2)$-equivariant endomorphism of $V^{\otimes n}$.
By quantum Schur--Weyl duality, every such endomorphism is an element
of the Hecke algebra.

The **Hecke mass element** of the vortex $\varrho$ is

$$
  \Phi_{\mathrm{mass}}(\beta)
  \;:=\;
  \tau\bigl(L_{\alpha_\varrho}\bigr)
  \;\in\; H_n(R, q).
$$

The :refterm[descent]{#descent} involution $\hat{\tau}_n$
([:refterm[descent]{#descent} eigenspaces](#prop\:descent-eigenspaces)) induces an
idempotent decomposition within $H_n(R, q)$:

$$
  \Phi_{\mathrm{mass}}(\beta)
  =
  \Phi^{\mathrm{desc}}(\beta)
  +
  \Phi^{\mathrm{trans}}(\beta),
$$

where $\Phi^{\mathrm{desc}} = \tau(\hat{\tau}_n(L_{\alpha}))$ encodes
the base-level (descended) cycle and
$\Phi^{\mathrm{trans}} = \tau(L_{\alpha} - \hat{\tau}_n(L_{\alpha}))$
encodes the transient contributions at the blow-up centres.
