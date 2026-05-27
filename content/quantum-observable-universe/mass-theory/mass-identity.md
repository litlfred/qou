Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def\:quantum-observable-universe)) and let
$\{A_n\}_{n \geq 0}$ be its
([recursive brane tower](#def\:recursive-brane-tower)).  Since $\mathbf{C}$ is a
$R$-linear rigid :refterm[monoidal category]{#monoidal-category}, the Frobenius--Hopf object $A$
admits a categorical trace
$\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$
defined by the composition

$$
  \mathrm{tr}(f)
  = 
  \bigl(\mathbf{1}
  \xrightarrow{ \mathrm{coev}}
  A \otimes A^{\vee}
  \xrightarrow{f \otimes \mathrm{id}}
  A \otimes A^{\vee}
  \xrightarrow{ \mathrm{ev}}
  \mathbf{1}\bigr),
$$

where $\mathrm{coev}$ and $\mathrm{ev}$ are the rigidity morphisms.
Let $\Delta \colon A \to A \otimes A$ be the comultiplication (encoding
the connection) and let $\int_A \colon A \to \mathbf{1}$ be the
Frobenius form.

The *inertial mass* of a morphism $\varrho \colon \mathbf{1} \to A$
(a "closed cycle" in the Frobenius--Hopf object) is

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}\bigl(
    (\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \varrho
  \bigr)
  \bigr\rVert,
$$

where $\lVert \cdot \rVert$ is the norm on $R$ induced by the
[Frobenius pairing](#def\:frobenius-pairing).  The mass measures the resistance of the
Frobenius--Hopf structure to transporting the cycle $\varrho$ through
the comultiplication.
