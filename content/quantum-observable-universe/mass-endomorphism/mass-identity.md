Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)) and let $\{A_n\}_{n \geq 0}$ be its recursive brane tower ([recursive brane tower](#def:recursive-brane-tower)). Since $\mathbf{C}$ is a $R$-linear rigid :refterm[monoidal category]{#monoidal-category}, the Frobenius--Hopf object $A$ admits a categorical trace $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$ (cf. \cite{stolz-teichner-2012}) defined by the composition:

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

where $\mathrm{coev}$ and $\mathrm{ev}$ are the rigidity morphisms. Let $\Delta \colon A \to A \otimes A$ be the comultiplication and let $\int_A \colon A \to \mathbf{1}$ be the Frobenius form.

The **inertial mass** of a morphism $\varrho \colon \mathbf{1} \to A$ (a "closed cycle" in the Frobenius--Hopf object) is:

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

where $\lVert \cdot \rVert$ is the norm on $R$ induced by the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)). The mass measures the resistance of the Frobenius--Hopf structure to transporting the cycle $\varrho$ through the comultiplication.

**Archimedean specialisation.** This block spans the substrate wall. The pre-archimedean `frobeniusMass` is valued in the generic ground ring $R$ (the Frobenius norm $\lVert x\rVert_F = \langle x, x\rangle_F$ stays in $R$). The post-$\tau$ `scalarMass` is the archimedean realisation $R \to \mathbb{R}$, $x \mapsto \lVert x\rVert$, obtained by evaluating the Frobenius norm at the substrate parameter $q = q_0$. The $R \to \mathbb{R}$ realisation map inherently crosses the wall and cannot be made $\mathbb{R}$-free or generic-only. We acknowledge it here rather than splitting it off.
