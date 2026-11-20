**Spectral characterisation.**
Three structural results establish the existence and uniqueness of the electromagnetic fine structure constant:

1. *Two-strand spectral completeness* ([completeness theorem](#thm:em-spectral-completeness)). The algebra $\mathrm{End}_{\mathbf{C}}(A \otimes A)$ has $R$-rank $2$. Exactly two central idempotents $e_+, e_-$ sum to $\mathrm{id}$. Their normalised traces $w_\pm = \dim_q V_\pm/[2]_q^2$ sum to $1$, since $[3]_q + 1 = [2]_q^2$. No third channel exists.
2. *Uniqueness of the gauge coupling* (corollary, *ibid.*). The singlet idempotent $e_-$ is the unique scalar exchange channel. Any $R$-linear braid-invariant scalar coupling $A \otimes A \to \mathbf{1}$ is a multiple of $\mathrm{tr}_\tau(e_-) \cdot e_-$. The constant $\alpha_{\mathrm{EM}}$ exists and is unique up to global normalisation. The antisymmetric eigenvalue captures the entirety of the electromagnetic coupling.
3. *Force-carrier uniqueness* ([Bring uniqueness](#prop:force-carrier-bring-uniqueness)). The set $\{T_{2,9}, T_{3,5}\}$ exhausts genus-$4$ torus knots. This is a Diophantine fact: the equation $(m-1)(n-1)=8$ with $\gcd(m,n)=1$ and $m \leq n$ has only the solutions $(2,9)$ and $(3,5)$. The Bring-supported quantum observable universe has a forced force-carrier sector with categorical complexity $[9]_q \cdot [10]_q \in R$.

These results turn $\alpha_{\mathrm{EM}}$ into a topological invariant of the Bring fibration. At the fundamental level, no contour integrals, no factors of $2 \pi i$, and no renormalisation-group running are required.

**:refterm[Descent]{#descent} decomposition: Chern-Simons correction.**

The bare formula $\alpha^{-1} = q \cdot [9]_q \cdot [10]_q$ gives the base holonomy of the electromagnetic endomorphism. This is the bulk coupling from the $R$-matrix eigenvalue multiplied by the $q$-deformed crossing complexities. It is the analogue of the volume term $\lambda_V \cdot A$ in the mass formula.

The full coupling receives an exceptional divisor correction from the Chern-Simons invariants of the force-carrier torus knots $T_{2,9}$ and $T_{3,5}$ ([EM coupling Chern-Simons](#rem:em-coupling-chern-simons)):

$$
  \frac{1}{\alpha_{\mathrm{EM}}}
  =
  q \cdot [9]_q \cdot [10]_q
  \cdot \bigl(1 + \delta_{\mathrm{CS}}
               + \delta_{\mathrm{CS}}^2 \cdot \kappa\bigr)
$$

where

$$
  \delta_{\mathrm{CS}}
  =
  \frac{\bigl(\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})\bigr)
        \cdot \tfrac{[2]_q}{2} \cdot \hbar_q^2}
       {q \cdot [9]_q \cdot [10]_q}
$$

and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}} / \det G_{\mathrm{CS}}^{q} \approx 1.722$ is the Gram determinant ratio of the classical and $q$-deformed Chern–Simons pairing. It captures self-dual damping at the second jet level. Both $\delta_{\mathrm{CS}}$ and $\kappa$ derive from the Chern–Simons invariants and the Bring-surface Gram matrix. No free parameters are introduced ([EM coupling Chern-Simons](#rem:em-coupling-chern-simons)).

The universal formula gives the Chern-Simons invariants of torus knots $T_{m,n}$:

$$
  \mathrm{CS}(T_{m,n})
  =
  \frac{\pi^2 (m^2 - 1)(n^2 - 1)}{12\,m\,n}.
$$

This yields $\mathrm{CS}(T_{2,9}) = \pi^2 \cdot \tfrac{10}{9}$ and $\mathrm{CS}(T_{3,5}) = \pi^2 \cdot \tfrac{16}{15}$. The quantum Planck constant is $\hbar_q = (q - 1)/q$.

**Numerical evaluation.**

See [Table 1](#tbl:em-coupling-projection-table1-data).

The Chern-Simons correction reduces the discrepancy from $0.155\%$ (bare formula) to $399\;\mathrm{ppb}$. However, the $\kappa \approx 1.722$ value was admitted as `sorry` in the Lean formalisation and never closed. Exact matching with CODATA requires $\kappa \approx 1.8878$. See [Conjectured Chern-Simons correction form $1/\alpha = q[9]_q[10]_q\cdot\bigl(1+\delta_{CS}/(1-\delta_{CS}\kappa)\bigr)$ (Gram-determinant $\kappa$ unproved)](#rem:em-coupling-chern-simons) for the demoted statement and [open problems](#rem:alpha-em-derivation-open-problems) for the path forward.

**Open problem: closing the $0.155\%$ bare residual.**
The bare formula $1/\alpha_{\text{bare}} = q\cdot[9]_q\cdot[10]_q$ has a complete categorical derivation. It accounts for $\alpha_{\text{EM}}$ to $-0.155\%$ at $q_0$. The remaining $\sim 1.55 \times 10^{-3}$ relative gap lacks a closed structural derivation:

1. The Chern-Simons form ($1+\delta_{CS}+\kappa\delta_{CS}^2$) is conjectural. The $\kappa$ identification is unproved. Both the $2{\times}2$ $J^2$-jet derivation and the Wedderburn-block Plancherel sum yield $\kappa \approx 1.722$. This falls short of the $\kappa \approx 1.888$ needed for CODATA. Block-diagonal Gram deformations cannot close this gap. See [Open problems: deriving the $1.55 \times 10^{-3}$ correction to the bare $1/\alpha_{EM} = q[9]_q[10]_q$](#rem:alpha-em-derivation-open-problems) for the multiplicative-family ruling.
2. The PSLQ-empirical form $45[3]_q(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$ matches CODATA to $7$ ppb at $q_0$. It disagrees with the bare formula at every other $q$. Only one of its four factors is structurally derived. The additive Bring zero-mode form replaces it.
3. The additive Bring zero-mode form ([Additive Bring zero-mode form $1/\alpha_{EM} = q\cdot[9]_q\cdot[10]_q + 2g/(4\pi(g-1))$ (conditional)](#prop:em-coupling-bring-zero-mode)): $1/\alpha_{EM} = q[9]_q[10]_q + 2g/(4\pi(g-1)) + \mathcal{O}(\alpha)$ at $g=4$. The correction $2g/(4\pi(g-1)) = 2/(3\pi)$ admits two geometric identifications: the Hodge / Gauss-Bonnet ratio on Bring's surface, and the sphere-volume ratio $\mathrm{Vol}(S^2)/(3\,\mathrm{Vol}(S^3))$. The single-term relative residual is $-4.2 \times 10^{-6}$. With the next-order $\alpha/(4\pi)$ term, it is $+5.7 \times 10^{-8}$. This is the numerical front-runner. It imports the archimedean transcendental $\pi$ via sphere volumes and Hodge data. This puts the correction structurally outside the pre-archimedean substrate ring $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$. Its pre-archimedean status is open. See [Uniqueness of the archimedean realization functor (Bloch-Suslin pentagon, conditional)](#prop:archimedean-functor-uniqueness) for the repair route, which factors the state sum through a Bloch-group class using substrate pentagon-coherence.

The bare $q[9]_q[10]_q$ derivation is solid and pre-archimedean. Closing the remaining $1.55 \times 10^{-3}$ gap requires a pre-archimedean origin for the $\pi$-bearing additive correction or an off-diagonal Gram deformation that escapes the multiplicative-family ruling. Neither is established.
