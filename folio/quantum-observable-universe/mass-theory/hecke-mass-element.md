Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
Hecke algebra $H_n(R, q)$
([Hecke algebra](#rem:hecke-algebra-from-braiding)) and Markov trace
$\mathrm{tr}_M \colon H_n(R, q) \to k$
([Jones--Markov trace](#thm:jones-markov-trace)).

Let $\varrho \colon \mathbf{1} \to A$ be a vortex morphism with braid
representative $\beta \in B_n$.  The **mass integrand**
([mass identity](#def:mass-identity)) is the composition

$$
  \alpha_\varrho
  =
  (\textstyle\int_A \otimes \mathrm{id})
  \circ \Delta
  \circ \varrho
  \colon \mathbf{1} \to A,
$$

and $L_{\alpha_\varrho} \in \mathrm{End}_{\mathbf{C}}(A)$ is left multiplication by $\alpha_\varrho$ in the Frobenius--Hopf algebra $A$.

The **Hecke mass element** of the vortex $\varrho$ is

$$
  \Phi_{\mathrm{mass}}(\beta)
  \;:=\;
  \tau\bigl(L_{\alpha_\varrho}\bigr)
  \;\in\; H_n(R, q).
$$

Its **descended** and **transient** parts are

$$
  \Phi^{\mathrm{desc}}(\beta) := \tau\bigl(\hat{\tau}_n(L_{\alpha_\varrho})\bigr),
  \qquad
  \Phi^{\mathrm{trans}}(\beta) := \tau\bigl(L_{\alpha_\varrho} - \hat{\tau}_n(L_{\alpha_\varrho})\bigr),
$$

where $\hat{\tau}_n$ is the :refterm[descent]{#descent} involution ([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).
