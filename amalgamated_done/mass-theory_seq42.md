<!-- FILE_START: intro-parity-classification-discrepancy.md -->
The classical evaluation is parity-blind. It cannot distinguish a knot from its mirror image. This causes a systematic discrepancy between the predicted and empirical mass spectra.

We trace the discrepancy to the chirality pairing. We resolve it using the augmented parity classification. Finally, we map the atomic atlas to track which elements resolve unambiguously.
<!-- FILE_END: intro-parity-classification-discrepancy.md -->

<!-- FILE_START: mn-classical-parity-blind.md -->
**Remark (Murnaghan–Nakayama parity blindness).**
*The classical Murnaghan–Nakayama recursion computes $S_n$ characters. When applied to the $S_{3A}$ atomic braid projection, it cannot distinguish a proton from a neutron. Both possess identical permutation cycle types.*

Positive and negative crossings project to the identical $S_n$ transposition. The q-deformed Hecke algebra distinguishes them through eigenvalue signs. The classical limit $q \to 1$ crushes this distinction.

The classical computation fails to predict mass splitting but succeeds as a structural diagnostic. It identifies the exact sparse partition support of the atomic braid. The full calculation uses the $q$-character evaluated strictly on this pre-computed support.
<!-- FILE_END: mn-classical-parity-blind.md -->

<!-- FILE_START: q-character-closes-parity-gap.md -->
**Remark (closing the parity gap).**
*The $q$-deformed Hecke character $\chi^\lambda_q(\sigma_w)$ explicitly breaks the parity blindness. Computed via the Hoefsmit seminormal form, it distinguishes $\sigma$ from $\sigma^{-1}$ using the Hecke eigenvalue gap $(q, -q^{-1})$. This strictly separates proton from neutron.*

The symbolic matrix evaluation preserves $q$ exactness. A positive crossing contributes differently to the partition sum than a negative crossing. The mixed $\sigma^{\pm 1}$ braid words accumulate a net $q$-dependence. The proton (majority $\sigma$) trace diverges from the neutron (majority $\sigma^{-1}$) trace.

This separation restores the beta-decay calibration constraint. The structural information lost in the classical limit returns.
<!-- FILE_END: q-character-closes-parity-gap.md -->

<!-- FILE_START: frobenius-codim-universal.md -->
**Theorem (Frobenius quantum-co-dimension trace).**
*Let $A = H_n(R, q)$ be a self-dual Frobenius algebra with Markov trace $\tau$. The quantum-co-dimension element*

$$
  C_{\dim_q}
  \;:=\;
  \sum_{\lambda \in \widehat{A}}
    \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)}
    \cdot p_\lambda
  \;\in\; Z(A)
$$

*lies in the centre of $A$ and satisfies*

$$
  \boxed{
    \tau\bigl(C_{\dim_q}\bigr)
    \;=\;
    \sum_{\lambda \in \widehat{A}} \frac{1}{\dim_q(\lambda)}.
  }
$$
<!-- FILE_END: frobenius-codim-universal.md -->

<!-- FILE_START: frobenius-codim-universal-interpretation.md -->
**Physical content.**
*Any vortex on the self-dual Frobenius algebra inherits a tower residual. The residual equals the trace of the quantum-co-dimension element scaled by the electron mass $m_e$:*

$$
  \Delta m_{\text{vortex}}
  \;=\;
  m_e \cdot \tau\bigl(C_{\dim_q}^{(A)}\bigr).
$$

*This trace provides the universal derivation of the $(5/2) m_e$ proton residual.*
<!-- FILE_END: frobenius-codim-universal-interpretation.md -->

<!-- FILE_START: frobenius-limits-substrate-cost.md -->
**Remark (limits of the substrate cost).**
*The Frobenius co-Casimir trace $\tau(C_{\dim_q}) = \sum_\lambda 1/\dim_q(\lambda)$ exhibits a regular limit structure.*

As $q \to 1$, it reaches the classical sum $\sum 1/d_\lambda$. At $q \to 0$ or $q \to \infty$, it freezes to exactly $2$ (the sum of the two 1-dimensional endpoints). At the observed substrate $q_0 \approx 1.11$, the trace is slightly reduced from the classical peak.

This sum measures the substrate's fundamental processing overhead. The brane tower evaluates the cost of the specific knot computation. The substrate imposes the Frobenius bound independently of the braid.
<!-- FILE_END: frobenius-limits-substrate-cost.md -->

<!-- FILE_START: knot-mass-formula-unified.md -->
**Theorem (unified knot mass formula).**
*The categorical mass of the vortex $\varrho$ is exactly:*

$$
  \boxed{
    \mathfrak{m}(\varrho)
    \;=\;
    \underbrace{\bigl|\mathrm{tr}_M(T_w)\bigr|}_{\text{descended}}
    \;-\;
    \underbrace{\sum_{i=0}^{n-2} \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}}|\bigr)
               - z^2 \sum_{0 \leq i < j \leq n-2}
                  \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|\bigr)}_{\text{brane tower}}
    \;+\;
    \underbrace{m_e \cdot \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)}_{\text{Frobenius co-Casimir}}
  }
$$

*where $\mathrm{Li}_2^q(z)$ is the symmetric q-dilogarithm. This integrates the Briggs–Klein expansion over each resolved defect.*

The descended piece evaluates the basic topological trace. The brane tower resolves the computational cost of the braid diagram. The Frobenius co-Casimir accounts for the substrate's universal algebra representation overhead.

The archimedean specialisation $\Phi_q(|\hat V_i|)$ breaks the exact Markov invariance of the algebraic trace. Replacing it with the rigorous Habiro-coefficient cyclotomic sum eliminates the isospin pathology at $q_0$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: knot-mass-formula-unified.md -->
