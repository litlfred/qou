Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)) and let $\{A_n\}_{n \geq 0}$ be its recursive brane tower ([recursive brane tower](#def:recursive-brane-tower)). Let $\mu$, $\eta$ be the multiplication and unit of the Frobenius--Hopf object $A$, let $\Delta \colon A \to A \otimes A$ be the comultiplication and let $\int_A \colon A \to \mathbf{1}$ be the Frobenius form. The **mass integrand** is the endomorphism

$$
  \Psi = (\textstyle\int_A \otimes \mathrm{id}) \circ \Delta \colon A \to A .
$$

The **inertial mass** of a morphism $\varrho \colon \mathbf{1} \to A$ is the norm of the composite $\mathbf{1} \xrightarrow{\varrho} A \xrightarrow{\Psi} A \xrightarrow{\int_A} \mathbf{1}$:

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
    \textstyle\int_A \circ\, \Psi \circ \varrho
  \bigr\rVert,
$$

where $\lVert \cdot \rVert$ is the norm on $R$ induced by the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)).

When $\varrho = \rho(\beta)$ is the image of a braid $\beta$ on $n$ strands with writhe $w(\beta)$ and $\int_A$ is the Jones–Markov trace, the **mass of the braid class** of $\beta$ is defined by the framing-corrected form

$$
  (1 + q^2)^{n} \, q^{-n - 2 w(\beta)} \textstyle\int_A \rho(\beta).
$$
