Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)) and let
$\{A_n\}_{n \geq 0}$ be its recursive brane tower
([Definition](#def:recursive-brane-tower)).  Since $\mathcal{C}$ is a
$R$-linear rigid monoidal category, the Frobenius--Hopf object $A$
admits a categorical trace
$\mathrm{tr} \colon \mathrm{End}_{\mathcal{C}}(A) \to R$
defined by the composition
$$
  \mathrm{tr}(f)
  \;=\;
  \bigl(\mathbf{1}
  \xrightarrow{\;\mathrm{coev}\;}
  A \otimes A^{\vee}
  \xrightarrow{\;f \otimes \mathrm{id}\;}
  A \otimes A^{\vee}
  \xrightarrow{\;\mathrm{ev}\;}
  \mathbf{1}\bigr),
$$
where $\mathrm{coev}$ and $\mathrm{ev}$ are the rigidity morphisms.
Let $\Delta \colon A \to A \otimes A$ be the comultiplication (encoding
the connection) and let $\lambda \colon A \to \mathbf{1}$ be the
Frobenius form.

The *inertial mass* of a morphism $\gamma \colon \mathbf{1} \to A$
(a "closed cycle" in the Frobenius--Hopf object) is
$$
  m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{tr}\bigl(
    (\lambda \otimes \mathrm{id})
    \circ \Delta
    \circ \gamma
  \bigr)
  \,\bigr\rVert,
$$
where $\lVert \cdot \rVert$ is the norm on $R$ induced by the
Frobenius pairing.  The mass measures the resistance of the
Frobenius--Hopf structure to transporting the cycle $\gamma$ through
the comultiplication.
