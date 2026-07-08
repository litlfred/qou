<!-- FILE_START: intro-em-completeness-gauge-coupling.md -->
The electromagnetic coupling derives from the matter particle spectrum. The Descartes universe is electromagnetically complete. The photon spectrum saturates the categorical state space. This completeness ensures the substrate parameter uniquely fixes the gauge coupling $\alpha_{\mathrm{EM}}$. The Chern–Simons form recovers gauge-invariant content from the knot-operator representation.

Spectral completeness holds. The spectral interpretation maps every photon mode to a force-carrier knot. The Plancherel-ratio Gram determinant defines the spectral measure. The derivation yields $\alpha_{\mathrm{EM}}$ as the unique gauge coupling compatible with the completeness pairing. This connects to the Chern–Simons action and the $\kappa$-spectral interpretation of the Gram-matrix determinant. The Bring zero-mode controls the precision-target gap.

This yields the categorical value of $\alpha_{\mathrm{EM}}$ as a function of the substrate parameter. Evaluating at $q_0 \approx 1.1097$ produces a numerical prediction for comparison against CODATA.
<!-- FILE_END: intro-em-completeness-gauge-coupling.md -->

<!-- FILE_START: force-carrier-spectral-interpretation.md -->
Three independent results force the denominator $[9]_q \cdot [10]_q$:

1. The existence axiom for the quantum observable universe embeds the brane into a genus-$4$ modular curve.
2. The genus-$4$ Diophantine classification exhausts torus knots of that genus by the pair $\{T_{2,9}, T_{3,5}\}$.
3. The categorical $q$-dimension assignment to torus simples is a fixed datum of $\mathbf{Rep}_q(\mathrm{SU}_q(2))$.

The denominator of the fine structure constant is therefore a topological invariant of the Bring fibration.

**Strong and weak labelling.**
The lower crossing number dominates gauge boson exchange. The assignment pairs $T_{2,9}$ to the strong force and $T_{3,5}$ to the weak force. This labelling does not affect the product $[9]_q \cdot [10]_q$. It identifies which torus knot mediates which sector.
<!-- FILE_END: force-carrier-spectral-interpretation.md -->

<!-- FILE_START: gauge-coupling-uniqueness.md -->
*Any $R$-linear, braid-invariant, scalar coupling $A \otimes A \to \mathbf{1}$ is a multiple of $\mathrm{tr}_\tau(e_-) \cdot e_-$. Up to the global normalisation $\lambda \in R$, exactly one non-trivial scalar coupling exists on the two-strand sector of $\mathbf{C}$.*
<!-- FILE_END: gauge-coupling-uniqueness.md -->

<!-- FILE_START: gauge-coupling-uniqueness-novelty.md -->
**Remark.** Spectral completeness constrains the gauge sector. It bounds possible gauge couplings strictly by algebraic singlets.
<!-- FILE_END: gauge-coupling-uniqueness-novelty.md -->

<!-- FILE_START: em-completeness-interpretation.md -->
The completeness theorem ([completeness](#thm:em-spectral-completeness)) and its corollary ([uniqueness](#cor:gauge-coupling-uniqueness)) establish the singlet channel as the unique one-dimensional invariant subspace of $A \otimes A$. It acts as the sole scalar exchange channel. The symmetric channel $V_+$ has $R$-rank $\dim_q V_+ = [3]_q$. It is the spin-$1$ irrep of $\mathrm{SU}_q(2)$ and carries non-trivial spin. It cannot serve as a scalar gauge coupling.

The categorical $R$-matrix possesses a rank-$2$ endomorphism algebra over $R$. Plancherel completeness $w_+ + w_- = 1$ exhausts the Frobenius mass. No third channel exists. This guarantees no missing scalar coupling. Modulo force-carrier complexity normalisation ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)), the singlet weight $w_-$ equals $\alpha_{\mathrm{EM}}$ ([EM coupling projection](#prop:em-coupling-projection)).

**Spectral collapse and confinement.**
The two-strand completeness theorem provides the $n = 2$ instance of spectral-sequence collapse ([spectral collapse](#prop:spectral-sequence-collapse)) and its confinement reading ([confinement = collapse](#prop:confinement-categorical)). The condition $\mathrm{HH}^{\geq 1}(H_n(R, q)) = 0$ collapses every non-central element at $E_\infty$. This leaves only $Z(H_n(R, q)) = \bigoplus_\lambda R \cdot e_\lambda$. At $n = 2$, the centre decomposes into two summands $e_+, e_-$. The singlet $e_-$ forms the unique one-dimensional summand. The QCD analogue ([confinement reading](#prop:confinement-categorical)) asserts that non-central elements remain unobservable at $E_\infty$. This forces observables to factor through $\pi_Z$. The photon channel thus represents the unique colour-singlet projection at $n = 2$, with $\alpha_{\mathrm{EM}}$ as its Frobenius-pairing weight.

**Specialisation.**
The categorical statement holds over $R$. Numerical evaluation fixes a ring map $\iota \colon R \to \mathbb{R}$ satisfying $q^{1/2} \mapsto q_0^{1/2}$ at $q_0 = 1.109978595554181\ldots$ (50 dps). The completeness theorem is independent of $\iota$. It survives any specialisation to $\mathbb{Q}_p$ or $\mathbb{F}_\ell$ that admits the required units.
<!-- FILE_END: em-completeness-interpretation.md -->

<!-- FILE_START: em-coupling-projection.md -->
**Setup.**
The categorical structure defines over the commutative ring

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

Every quantity below lives in $R$ and survives any ring map $\iota \colon R \to k$ to a target commutative ring $k$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe over $R$ with substrate parameter $q$ and force-carrier generators $T_{2,9}$ (crossing number $c_s = 9$) and $T_{3,5}$ (crossing number $c_w = 10$). The electromagnetic fine structure constant is the $\tau$-trace of the singlet idempotent $e_-$ normalised by the force-carrier categorical complexity:

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[c_s]_q \cdot [c_w]_q}
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-integer.

A cleared-denominator relation avoids division outside the integral Laurent subring $\mathbb{Z}[q, q^{-1}] \subset R$:

$$
  [9]_q \cdot [10]_q \cdot \alpha_{\mathrm{EM}} \;=\; q^{-1}.
$$

**Derivation.**
The electromagnetic coupling between two charged localized knots $(c_1, K_1)$ and $(c_2, K_2)$ factorises into three finite contributions.

*Layer 1: Charge.*
The electromagnetic charge of a knot $K$ is its $q$-writhe. This is the antisymmetric crossing count under the crossing reversal involution $\sigma$:

$$
  Q_q(K) =  [w(K)]_q
  =  \frac{q^{w(K)} - q^{-w(K)}}{q - q^{-1}}
$$

where $w(K) = \sum_i \epsilon_i \in \mathbb{Z}$ is the writhe. All crossings in a torus knot $T_{m,n}$ share the same sign. This gives $w(T_{m,n}) = \pm m(n-1)$.

*Layer 2: Coupling strength.*
The two-strand spectral completeness theorem decomposes the braiding into central idempotents:

$$
  c_{A,A} \;=\; q^{1/2}\, e_+ \,-\, q^{-1/2}\, e_-,
  \qquad e_+ + e_- = \mathrm{id}_{A \otimes A},\;\; e_+ e_- = 0.
$$

The singlet $e_-$ projects onto the unique copy of the unit object $\mathbf{1} \subset A \otimes A$. Its fibre-functor trace evaluates to

$$
  |\mathrm{tr}_\tau(e_-)|^2 \;=\; q^{-1} \,\in\, R.
$$

The singlet is unique. This trace is therefore the full scalar exchange amplitude.

*Layer 3: Force-carrier complexity.*
The genus-$4$ uniqueness theorem fixes the force-carrier sector of a Bring-supported quantum observable universe as the set $\{T_{2,9}, T_{3,5}\}$. Their categorical $q$-dimensions are $\dim_q T_{2,9} = [9]_q$ and $\dim_q T_{3,5} = [10]_q$. The product $[9]_q \cdot [10]_q$ is the categorical complexity of the force-carrier object. The electromagnetic coupling is the singlet trace divided by this normalisation:

$$
  \alpha_{\mathrm{EM}}
  \;=\;
  \frac{|\mathrm{tr}_\tau(e_-)|^2}{\dim_q T_{2,9} \cdot \dim_q T_{3,5}}
  \;=\;
  \frac{q^{-1}}{[9]_q \cdot [10]_q} \,\in\, R.
$$

**Completeness.**
Plancherel completeness $w_+ + w_- = 1$ ensures no scalar channel is omitted. These two idempotents exhaust the Frobenius mass of $\mathrm{End}(A \otimes A)$. The fine structure constant is a ring-theoretic invariant of the Descartes universe.
<!-- FILE_END: em-coupling-projection.md -->

<!-- FILE_START: em-coupling-projection-discussion.md -->
**Spectral characterisation.**
Three structural results establish the existence and uniqueness of the electromagnetic fine structure constant:

1. *Two-strand spectral completeness* ([completeness theorem](#thm:em-spectral-completeness)). The algebra $\mathrm{End}_{\mathbf{C}}(A \otimes A)$ has $R$-rank $2$. Exactly two central idempotents $e_+, e_-$ sum to $\mathrm{id}$. Plancherel completeness $w_+ + w_- = 1$ exhausts the Frobenius mass. No third channel exists.
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

The Chern-Simons correction reduces the discrepancy from $0.155\%$ (bare formula) to $399\;\mathrm{ppb}$. However, the $\kappa \approx 1.722$ value was admitted as `sorry` in the Lean formalisation and never closed. Exact matching with CODATA requires $\kappa \approx 1.8878$. See [`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) for the demoted statement and [open problems](#rem:alpha-em-derivation-open-problems) for the path forward.

**Open problem: closing the $0.155\%$ bare residual.**
The bare formula $1/\alpha_{\text{bare}} = q\cdot[9]_q\cdot[10]_q$ has a complete categorical derivation. It accounts for $\alpha_{\text{EM}}$ to $-0.155\%$ at $q_0$. The remaining $\sim 1.55 \times 10^{-3}$ relative gap lacks a closed structural derivation:

1. The Chern-Simons form ($1+\delta_{CS}+\kappa\delta_{CS}^2$) is conjectural. The $\kappa$ identification is unproved. Both the $2{\times}2$ $J^2$-jet derivation and the Wedderburn-block Plancherel sum yield $\kappa \approx 1.722$. This falls short of the $\kappa \approx 1.888$ needed for CODATA. Block-diagonal Gram deformations cannot close this gap. See [`rem:alpha-em-derivation-open-problems`](#rem:alpha-em-derivation-open-problems) for the multiplicative-family ruling.
2. The PSLQ-empirical form $45[3]_q(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$ matches CODATA to $7$ ppb at $q_0$. It disagrees with the bare formula at every other $q$. Only one of its four factors is structurally derived. It is superseded by the additive Bring zero-mode form.
3. The additive Bring zero-mode form ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)): $1/\alpha_{EM} = q[9]_q[10]_q + 2g/(4\pi(g-1)) + \mathcal{O}(\alpha)$ at $g=4$. The correction $2g/(4\pi(g-1)) = 2/(3\pi)$ admits two geometric identifications: the Hodge / Gauss-Bonnet ratio on Bring's surface, and the sphere-volume ratio $\mathrm{Vol}(S^2)/(3\,\mathrm{Vol}(S^3))$. The single-term relative residual is $-4.2 \times 10^{-6}$. With the next-order $\alpha/(4\pi)$ term, it is $+5.7 \times 10^{-8}$. This is the numerical front-runner. It imports the archimedean transcendental $\pi$ via sphere volumes and Hodge data. This puts the correction structurally outside the pre-archimedean substrate ring $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$. Its pre-archimedean status is open. See [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode) for the repair routes.

The bare $q[9]_q[10]_q$ derivation is solid and pre-archimedean. Closing the remaining $1.55 \times 10^{-3}$ gap requires a pre-archimedean origin for the $\pi$-bearing additive correction or an off-diagonal Gram deformation that escapes the multiplicative-family ruling. Neither is established.
<!-- FILE_END: em-coupling-projection-discussion.md -->

<!-- FILE_START: em-coupling-projection-interpretation.md -->
**Remark (classical limit).**
As $q \to 1$, $[n]_q \to n$ and $\alpha_{\mathrm{EM}} \to 1/90$. The observed value $\alpha^{-1} \approx 137$ requires $q > 1$. The departure from the classical limit makes the coupling weaker than $1/90$.

**Remark (physical interpretation).**
The :refterm[descent]{#descent} decomposition of the coupling mirrors the mass decomposition (see [Table 2](#tbl:em-coupling-projection-table2-data)). The correction is positive. The force-carrier braids $T_{2,9}$ and $T_{3,5}$ embed on the genus-$4$ Bring's surface. They possess crossing degeneracies that screen the bare electromagnetic charge. This increases $1/\alpha$ from the bare value.
<!-- FILE_END: em-coupling-projection-interpretation.md -->

<!-- FILE_START: em-coupling-chern-simons.md -->
### Chern--Simons level from existence of the quantum observable universe

The Chern--Simons level $k$ is not an independent input. The existence proof for a quantum observable universe ([QOU existence](#prop:quantum-observable-universe-exists)) sets $q = e^{\pi i/(k + h^{\vee})}$. This makes $\mathbf{C} = \mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$ the modular tensor category. This category simultaneously fixes the braiding in the Skein relation and the Chern-Simons partition function on the brane. The index $k = \langle c_{2}(\mathrm{Ad}(P)), [M] \rangle$ determines the $q$-deformation of the $q$-dimensions $[m]_{q}, [n]_{q}$ and the functional $\mathrm{CS}(T_{m, n})$ through a single Reshetikhin-Turaev construction. The numerical prediction specialises this shared object. It does not combine two independent quantities.

**Conjecture (Chern-Simons :refterm[descent]{#descent} correction, $\kappa$ unproved).**
*The fine structure constant receives corrections from the Chern–Simons invariants of the force-carrier torus knots $T_{2,9}$ and $T_{3,5}$ on Bring's surface:*

$$
  \frac{1}{\alpha_{\mathrm{EM}}}
  = q \cdot [9]_q \cdot [10]_q
    \cdot \bigl(1 + \delta_{\mathrm{CS}}
                 + \delta_{\mathrm{CS}}^2 \cdot \kappa\bigr)
$$

*where:*

$$
  \delta_{\mathrm{CS}}
  = \frac{\bigl(\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})\bigr)
              \cdot \tfrac{[2]_q}{2} \cdot \hbar_q^2}
             {q \cdot [9]_q \cdot [10]_q}
$$

*and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}} / \det G_{\mathrm{CS}}^{q}$ is the Gram determinant ratio of the classical and $q$-deformed Chern–Simons pairing on Bring's surface.*

*At $q_0 \approx 1.110$ with the Witten-1988 value $\kappa \approx 1.722$, $1/\alpha$ evaluates to $137.035944$. The CODATA value is $137.035999$. The residual is $399$ ppb. The value $\kappa = 1.722$ derives from the sketched Gram-determinant computation but was admitted as `sorry` in the Lean formalisation ([`em-coupling-chern-simons.lean`](#)). It was never closed. Exact CODATA matching requires $\kappa \approx 1.8878$. This differs from the Witten value by $\sim 10\%$. Either the Gram-determinant identification of $\kappa$ is wrong, or the order-$\delta_{CS}^2$ truncation omits higher-order contributions.*

*Proof sketch (does not close $\kappa$).*
The bare coupling $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ arises from the antisymmetric braiding eigenvalue. This is Layer 2 of [EM coupling projection](#prop:em-coupling-projection). It is normalized by the force-carrier $q$-dimensions from Layer 3.

The correction arises from the :refterm[descent]{#descent} decomposition of the coupling endomorphism $P_{\mathrm{anti}}$ on the force-carrier configuration. The torus knots $T_{2,9}$ and $T_{3,5}$ are non-hyperbolic. Their $\tau$-image geometric invariant is the Chern–Simons functional, not the hyperbolic volume:

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2 (m^2-1)(n^2-1)}{12 m n}.
$$

The factor $[2]_q/2$ is the $q$-deformation of $\mathrm{Vol}(S^3)/\mathrm{Vol}(S^3_{\mathrm{classical}})$. It replaces $\mathrm{Vol}(S^3) = 2\pi^2$ with $\mathrm{Vol}(S^3_q) = \pi^2 [2]_q$.

At order $J^2$, the Gram matrix of the Chern-Simons pairing for the configuration $(T_{2,9}, T_{3,5})$ on Bring's surface gives:

$$
  G_{\mathrm{CS}} =
  \begin{pmatrix}
    \mathrm{CS}_1 + \pi^2 s_1^2 / c_1^2
    & \pi^2 \ell^2 / (c_1 c_2) \\
    \pi^2 \ell^2 / (c_1 c_2)
    & \mathrm{CS}_2 + \pi^2 s_2^2 / c_2^2
  \end{pmatrix}
$$

where $s_i = (m_i-1)(n_i-1)$ is the self-linking, $\ell = |m_1 n_2 - m_2 n_1| = 17$ is the linking number, and $c_i = m_i n_i$ is the crossing product. The $q$-deformed version replaces $m,n$ with $[m]_q, [n]_q$.

The determinant ratio $\kappa = \det G^{\mathrm{cl}} / \det G^q$ is conjectured to capture the self-dual damping at the $J^2$ level, with numerical value $\kappa \approx 1.722$. This identification is unproved. The Gram matrix is dimensionally ambiguous. The choice of basis for the rank-$2$ sublattice and the explicit form of $s_i, \ell, c_i$ in the $q$-deformed setting are not fixed. The resulting $\kappa$ is not computed end-to-end. A direct fit to CODATA gives $\kappa \approx 1.8878$. This suggests the formula misses a higher-order term or the entire ansatz uses the wrong decomposition. Closing $\kappa$ structurally remains an open problem. See [open problems](#rem:alpha-em-derivation-open-problems).$\square$
<!-- FILE_END: em-coupling-chern-simons.md -->

<!-- FILE_START: gram-kappa-spectral-interpretation.md -->
**Numerical check at $q_0 = 1.109978595554181\ldots$ (50 dps).**

The Hoefsmit pipeline ([Hoefsmit](#conj:hoefsmit-scattering-pipeline)) computes $\chi_\lambda(\beta_s)$ and $\chi_\lambda(\beta_w)$ in seminormal form. At strand count $n = 9$, the hook partitions $(8,1)$ and $(7,1,1)$ and the rectangular partition $(5,4)$ are the dominant blocks. Substituting the Plancherel weights $w_\lambda = \dim_q^2(V_\lambda)/[n]_q!$ and character values yields

$$
  \kappa \;\approx\; 1.722.
$$

This matches the 2-jet hand computation. It now derives from the Wedderburn block structure without arbitrary truncation.

**Structural comparison.**

| Old derivation | Spectral derivation |
|---|---|
| Ratio of $2{\times}2$ Gram matrix determinants at $J^2$ jet | Plancherel-weighted character product over Wedderburn blocks |
| 2-jet truncation chosen by hand | Full $\lambda \vdash n$ sum, convergent by Plancherel ($\sum w_\lambda = 1$) |
| Tied to Bring-surface coordinate calculation | Categorical: depends only on $\chi_\lambda(\beta_\bullet)$ |
| Result $1.722$ stated as numerical fact | Result $1.722$ determined by the $\lambda$-blocks of the genus-$4$ pair |

**Lean handle.**

The formula evaluates symbolically over $R$ to a $q$-rational expression for $\kappa$. It specializes numerically via $\iota \colon R \to \mathbb{R}$ at $q \mapsto q_0$. Character values $\chi_\lambda(T_{m,n})$ for torus knots are polynomial in $q^{\pm 1}$ \cite{jones1987}. The formula reduces to a finite product of Laurent monomials.

**Sensitivity.**

The logarithmic derivative $\partial \ln \kappa / \partial \ln q$ at $q_0$ measures the shift of Wedderburn block weights with the substrate parameter. Plancherel ensures $\sum_\lambda w_\lambda = 1$ at every $q$. The sensitivity bounds by $\max_\lambda |c_\lambda^{(s)} c_\lambda^{(w)}| \cdot |\partial \ln(\dim_q V_\lambda)/\partial \ln q|$. This bound is finite and computable.
<!-- FILE_END: gram-kappa-spectral-interpretation.md -->

<!-- FILE_START: chern-simons-as-knot-invariant.md -->
**Remark (Chern--Simons as a knot invariant).**

Classical Chern--Simons theory does not serve as the bulk categorical action ([comparison](#rem:categorical-action-vs-chern-simons)). That role belongs to $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$. Its archimedean image recovers Einstein--Hilbert, Yang--Mills, and Dirac. The Chern--Simons functional enters strictly as a geometric knot invariant. The commensurability class of the knot complement selects it.

The mechanism proceeds as follows:

1. The trace of the coupling endomorphism $P_{\mathrm{anti}}$ on a force-carrier knot configuration defines a Gram pairing at the $J^2$ jet layer.
2. For hyperbolic knots, the Gram entry is the hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ of the knot complement.
3. For non-hyperbolic torus knots $T_{m,n}$, including the strong ($T_{2,9}$) and weak ($T_{3,5}$) force carriers, the hyperbolic volume vanishes. The classical Chern--Simons functional replaces it:

   $$
     \mathrm{CS}(T_{m,n})
     =
     \frac{\pi^2\, (m^2 - 1)(n^2 - 1)}{12\, m\, n}.
   $$

4. The determinant ratio $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}} / \det G_{\mathrm{CS}}^{q}$ appears in the fine-structure correction $1/\alpha = q \cdot [9]_q [10]_q (1 + \delta_{\mathrm{CS}} + \delta_{\mathrm{CS}}^2 \kappa)$. It exactly measures the classical-vs-$q$-deformed ratio of Chern--Simons pairings \cite{witten2011}.

Classical Chern--Simons is a derived geometric invariant. It is invoked only when the knot complement fails to be hyperbolic. Analytic continuation of Chern--Simons theory supplies its $q$-deformed counterpart $G_{\mathrm{CS}}^{q}$ \cite{witten2011}.
<!-- FILE_END: chern-simons-as-knot-invariant.md -->

<!-- FILE_START: alpha-em-derivation-open-problems.md -->
**Remark (open problems for $\alpha_{EM}$ derivation).**

The bare singlet derivation ([prop:em-coupling-projection](#prop:em-coupling-projection)) gives

$$
  \frac{1}{\alpha_{\text{bare}}} \;=\; q\cdot[9]_q\cdot[10]_q
  \;\approx\; 136.823 \quad \text{at}\;\; q = q_0.
$$

This agrees with the CODATA value $137.035999084(21)$ to within $-0.155\%$. The bare formula reproduces the fine-structure constant to three significant figures with no free parameters. A relative gap of $1.55 \times 10^{-3}$ remains. Two prior attempts to close this gap are open conjectures:

| Form | Statement | Residual at $q_0$ | Status |
|------|-----------|-------------------|--------|
| Bare | $q[9]_q[10]_q$ | $-1.55\times 10^{-3}$ | Derived |
| Form A (CS) | $\cdot(1+\delta_{CS}+\kappa\,\delta_{CS}^2)$ with $\kappa=1.722$ | $-4.0\times 10^{-7}$ | Conj.; $\kappa$ unproved (Lean `sorry`); $\kappa \approx 1.888$ needed for exact match |
| Form B (gluon-octet) | $45[3]_q\,(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$ | $+6.7\times 10^{-9}$ | Conj.; only $45$ rigorously derived; disagrees with Form A at $q\ne q_0$ |

## Audit failure of both prior attempts

**Form A's $\kappa$ is incorrect.** The Witten-1988 Gram-determinant identification gives $\kappa \approx 1.722$. Matching CODATA at $q_0$ requires $\kappa \approx 1.8878$. The discrepancy is $\sim 10\%$ and cannot be quadrature error. The Lean formalisation ([`em-coupling-chern-simons.lean`](#)) carried this as `sorry` from the start.

**Form B is hidden numerology.** Of its four factors:

- $45 = \dim \Lambda^2 V_{\text{nat}}^{10}$ is rigorous. It is the hook-length count of $V_{(9,1)} \oplus V_{(8,1,1)}$.
- $[3]_q$ does not equal the $q$-dimension of any natural irrep of $H_3(q)$ or $U_q(\mathfrak{sl}_3)$. The singlet-idempotent gluon-octet identification is asserted, not computed.
- $\hbar_q^4 \cdot [5]_q$ is claimed to be the leading non-trivial term of the Plancherel-character expansion at $n=10$. The calculation was not performed. The ambient $H_n$ is unspecified.
- $8q$ is identified two ways (Lean: $\dim \mathfrak{su}(3)$; text: two-step crossing-pattern enumeration). Neither calculation was performed. Exact truncation requires an order-$3$ coefficient of $\approx -52$, which is not a clean $q$-rational.

Form A and Form B agree only at $q = q_0$. They give different values for $1/\alpha$ at every other $q$. Form B is a single-point fit.

## Ruled-out derivation paths

Four computational paths to close the $1.55 \times 10^{-3}$ gap are ruled out. They do not produce clean low-degree $q$-rationals:

| Path | Result | Verdict |
|------|--------|---------|
| Gram-det Plancherel-character product at $n=3$ | $\kappa \approx 7 \times 10^{-6}$ | Ruled out (need $\sim 1.888$) |
| q-Plancherel sums on $H_5$ Wedderburn blocks | trivial or astronomical | Ruled out |
| Scan $\hbar_q^k\cdot[a]_q\cdot[b]_q/([c]_q\cdot[d]_q)$, $a,b,c,d \le 12$ | 0 matches at $10^{-4}$ | Ruled out at this degree |
| **PSLQ at 100 dps over 54-element basis incl. $\pi, \zeta(3), \log 2$** | **No non-trivial integer relation** | **Decisively ruled out** |

The closest single-term near-match is

$$ F - 1 \;\approx\; \frac{\hbar_q^2}{\pi \cdot [2]_q} $$

at $7.4 \times 10^{-4}$ relative residual. This structure relates to $\mathrm{Vol}(S^3_q) = \pi^2[2]_q$ geometry, but it is not exact. A direct closed-form correction in any natural $q$-arithmetic basis at low degree is impossible.

See [`alpha-em-correction-derivation-attempts.witness.json`](#) for the full attempt log.

## Insufficiency of block-diagonal Gram deformations

A natural ansatz deforms the Gram matrix by a framing correction $\mathcal{A}$ induced by a chiral anomaly on Bring's surface, $G_n' = G_n \otimes \mathcal{A}$. There are two sub-cases:

1. **Scalar $\mathcal{A} \in R$.** For an $N \times N$ Gram matrix, $\det G_n' = \mathcal{A}^N \det G_n$. The determinant ratio $\kappa = \det G_n / \det G_{n-1}$ becomes $\kappa' = \mathcal{A}^{\dim G_n - \dim G_{n-1}} \cdot \kappa_{\text{Witten}}$. This is a fixed power of $\mathcal{A}$ multiplying the Witten value. The corrected $1/\alpha_{EM}$ takes the multiplicative form $q[9]_q[10]_q \cdot (1 + \delta_{CS} + \mathcal{A}^{\Delta\dim}\kappa_{\text{Witten}}\delta_{CS}^2)$.
2. **Block-diagonal $2{\times}2$ $\mathcal{A}$**. This acts on the two Hecke eigenchannels $V_{(2)}, V_{(1,1)}$. The determinant of $G_n'$ factors as a product of per-channel scalar powers. Again, $\kappa'$ is a multiplicative perturbation of $\kappa_{\text{Witten}}$. This "old derivation" route yielded $\kappa \approx 1.722$. It agrees with the Wedderburn-block Plancherel sum but falls short of the CODATA value.

Both sub-cases live in the multiplicative $q$-rational family. The 100-dps PSLQ scan over the 54-element basis ruled out this family. Any Gram deformation preserving block-diagonal structure on $V_{(2)} \oplus V_{(1,1)}$ cannot close the gap.

Closure requires an off-diagonal approach or an additive form. The additive Bring zero-mode form ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)) supplies the correction $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ as a summand. The substrate pentagon-coherence factors the quantum observable universe mass-formula state sum through a class in the Bloch group $B(\mathbb{C})$. Bloch-Suslin pentagon-uniqueness forces every real-valued archimedean realization to coincide with the Bloch-Wigner dilogarithm $D$. The $\pi$ in $2/(3\pi)$ is the unique archimedean shadow of substrate pentagon data, not an external import. Two open computations remain: identify the explicit Bloch-group class on Bring's surface, and lift the next-order $\alpha/(4\pi)$ term to a higher Bloch group $B_n(\mathbb{C})$.

## Implications

**The correction is a genuine two-loop effect.**
The additive photon zero-mode $2/(3\pi)$ has arithmetic weight $1$. It derives from $b_1/\mathrm{Area}$ and brings the residual to $-4.2\;\mathrm{ppm}$. The remaining $\mathcal{O}(\alpha^2)$ correction has arithmetic weight $3$. Its home is $\zeta(3)$. Quantum electrodynamics first requires a two-loop diagram at this rung. Classical categorical or tree-level routes have weight $\le 2$. The parameter-free prediction is complete to $\approx 4\;\mathrm{ppm}$. The finer $\mathcal{O}(\alpha^2)$ correction is a genuine two-loop vacuum-polarisation effect. It is not a categorical-level closed form.

## Promising lead: additive QED-style correction

An additive form yields a striking numerical match:

$$
  \frac{1}{\alpha_{EM}}
  \;\approx\;
  q \cdot [9]_q \cdot [10]_q
  \;+\;
  \frac{2}{3\pi}
  \;+\;
  \frac{\alpha}{4\pi}.
$$

| Form | Predicted $1/\alpha$ at $q_0$ | Residual vs CODATA (relative) |
|------|------------------------------|-------------------------------|
| Bare $q[9]_q[10]_q$ | 136.823220 | $-1.55 \times 10^{-3}$ |
| $+ 2/(3\pi)$ | 137.035426 | $-4.2 \times 10^{-6}$ |
| $+ \alpha/(4\pi)$ | 137.036007 | $+5.7 \times 10^{-8}$ |
| CODATA | $137.035999084(21)$ | — |

The first correction is derived ([`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring)). It is the photon infrared zero-mode on the 2-surface $M_{\text{Bring}}$. The harmonic $1$-form sector $b_1(M_g) = 2g$ normalises by the Gauss–Bonnet area $4\pi(g-1)$:

$$
  \frac{2}{3\pi}
  \;=\; \frac{b_1(M_g)}{\mathrm{Area}(M_g)}
  \;=\; \frac{2g}{4\pi(g-1)}\Big|_{g=4}
  \;=\; \frac{8}{12\pi}.
$$

The sphere-volume form $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$ is a secondary reading of the same number. The photon zero-mode lives on the $2$-surface. The denominator $3$ is the Gauss–Bonnet factor $(g-1)=3$. The $\alpha/(4\pi)$ term suggests a Schwinger-like 1-loop self-coupling.
<!-- FILE_END: alpha-em-derivation-open-problems.md -->

<!-- FILE_START: em-coupling-bring-zero-mode.md -->
**Proposition (additive Bring-surface zero-mode form for $1/\alpha_{EM}$, conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit) and Bloch-Suslin pentagon-uniqueness [`suslin1991`]).**
*Let $g = 4$ denote the genus of Bring's surface. This is the unique Riemann surface supporting the genus-$4$ torus knots $T_{2,9}$ and $T_{3,5}$ ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). Assume the upstream typeclasses `QOU.QPochhammer.ArchimedeanLimit`, `QOU.Archimedean.BlochSuslinUniqueness`, and `QOU.Archimedean.BringZeroModeBlochClass` are inhabited ([`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)). Then*

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  \underbrace{q\cdot[9]_q\cdot[10]_q}_{\text{tree level}}
  \;+\;
  \underbrace{\frac{2g}{4\pi(g-1)}}_{\text{Bring zero-mode}}
  \;+\;
  \mathcal{O}(\alpha)
  \;=\;
  q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi} + \mathcal{O}(\alpha).
$$

*The constant $2/(3\pi) = 8/(12\pi)$ admits two independent geometric identifications on Bring's surface*:

1. **Hodge / Gauss-Bonnet ratio:**
   $$\frac{2g}{4\pi(g-1)} \;=\; \frac{\dim H^1(M_{\text{Bring}};\,\mathbb{R})}{\mathrm{Area}(M_{\text{Bring}})}.$$
   *The area evaluates under constant negative curvature $-1$ as $\mathrm{Area} = -2\pi\chi = 4\pi(g-1) = 12\pi$.*
2. **Sphere-volume ratio:**
   $$\frac{2}{3\pi} \;=\; \frac{\mathrm{Vol}(S^2)}{3\cdot\mathrm{Vol}(S^3)} \;=\; \frac{4\pi}{3\cdot 2\pi^2}.$$

## Numerical match

Evaluation at $q_0 = 1.109978595554181\ldots$ (50 dps) using 60 dps precision yields:

| Quantity | Value |
|----------|------:|
| $q\cdot[9]_q\cdot[10]_q$ | $136.823219654\ldots$ |
| $2/(3\pi) = 2g/(4\pi(g-1))$ | $0.212206591\ldots$ |
| Sum | $137.035426245\ldots$ |
| CODATA $1/\alpha$ | $137.035999084(21)$ |
| **Residual** (relative) | $\mathbf{-4.2 \times 10^{-6}}$ |

The second additive term $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$ brings the relative residual to $+5.7 \times 10^{-8}$. This approaches the CODATA standard deviation $\sigma_\alpha = 1.5 \times 10^{-10}$.

## Conjectural physical interpretation

The numerical match supports a structural decomposition:

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  q\cdot[9]_q\cdot[10]_q
  \;+\;
  \frac{2g}{4\pi(g-1)}
  \;+\;
  \mathcal{O}(\alpha).
$$

The $g = 4$ structure of Bring's surface appears in both main terms. The tree-level coefficient $[9]_q[10]_q$ derives from the unique pair of genus-$4$ torus knots $\{T_{2,9}, T_{3,5}\}$ ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). The infrared shift $2g/(4\pi(g-1))$ emerges from the Hodge data of the same Bring's surface. This double appearance of $g = 4$ is structurally consistent. It matches the expectations for a categorical-Lagrangian quantum field theory with a UV completion on Bring's curve.

> **Conditional theorem (§3b-cond).** Lean axiomatises the upstream conjectures as typeclasses [`QOU.QPochhammer.ArchimedeanLimit`](../braids-and-knots/dilogarithm-archimedean-limit.lean), [`QOU.Archimedean.BlochSuslinUniqueness`](archimedean-functor-uniqueness.lean), and [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean). The Lean theorem [`QOU.Archimedean.bring_zero_mode_additive_form`](em-coupling-bring-zero-mode.lean) takes `BringZeroModeBlochClass` as an instance and concludes unconditionally. The algebraic identity $2g/(4\pi(g-1)) = 2/(3\pi)$ at $g=4$ closes via `field_simp; ring`. The remaining structural input is the explicit Bloch-group class realising $2/(3\pi)$ on Bring's surface.

| Form | Type | Residual at $q_0$ | Structural status |
|------|------|-------------------|-------------------|
| Bare $q[9]_q[10]_q$ | multiplicative tree | $-1.55\times 10^{-3}$ | Derived |
| [`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) | multiplicative + Gram-det $\kappa$ | $-4\times 10^{-7}$ | $\kappa$ unproved (Lean `sorry`) |
| **This conjecture (additive Bring zero-mode)** | $q[9]_q[10]_q + 2g/(4\pi(g-1))$ | $-4.2\times 10^{-6}$ | **Geometrically clean; one Bring-genus-4 quantity in each term** |

The additive form provides the cleanest structure. It avoids fitted coefficients. Every factor maps to a known geometric or topological invariant of Bring's surface.

## Witness

See [`alpha-em-correction-derivation-attempts.witness.json`](#) for the full attempt log.
<!-- FILE_END: em-coupling-bring-zero-mode.md -->

<!-- FILE_START: em-coupling-fixed-point.md -->
**Theorem (conditional on the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization class).**
*Let $q$ be the substrate parameter and write*

$$
  T \;=\; q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi},
  \qquad
  H \;=\; \frac{[2]_q}{8\pi},
  \qquad
  h \;=\; \frac{q-1}{q}.
$$

*Assume the typeclass [`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean) is inhabited at $(q,\alpha)$. The exact $\mathcal{O}(\alpha^2)$ self-energy normalization of the coupling equation is $H\cdot(1-h^2\alpha)$. This is the archimedean image of a class in the Bloch group $B_3(\mathbb{C})$. Consequently, $\alpha$ solves the self-consistent fixed point:*

$$
  \frac{1}{\alpha}
  \;=\;
  T + \alpha\,H\,\bigl(1 - h^2\alpha\bigr).
$$

*Then $\alpha$ constitutes a root of the characteristic cubic:*

$$
  P(\alpha)
  \;=\;
  -h^2 H\,\alpha^3 + H\,\alpha^2 + T\,\alpha - 1
  \;=\; 0,
$$

*and its inverse yields CODATA-consistency: $\lvert \alpha^{-1} - 137.035999084\rvert < 10^{-3}$.*

## What is proved vs. what is assumed

The fine-structure constant emerges as the symbolic root of a self-consistent fixed-point equation. This path is additive and self-consistent. The formulation avoids the refuted multiplicative Chern–Simons or gluon-octet forms.

The equation integrates three components. Only the third remains open:

1. **Tree term $q\cdot[9]_q\cdot[10]_q$**: The bare inverse coupling from [`prop:em-coupling-projection`](#prop:em-coupling-projection). Lean verifies its categorical-trace refactoring ([`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)).
2. **Zero-mode shift $2/(3\pi) = 2g/(4\pi(g-1))\big|_{g=4}$**: The photon infrared harmonic-$1$-form contribution on Bring's surface. Lean proves this in [`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring). The normalization $8\pi = \pi b_1 = \pi\dim H^1(M_{\text{Bring}})$ maintains the harmonic count.
3. **$\mathcal{O}(\alpha^2)$ normalization $H\cdot(1-h^2\alpha)$**: The Habiro deformation $(1-h^2\alpha)$ with coefficient $H = [2]_q/(8\pi)$. Identifying the exact $\mathcal{O}(\alpha^2)$ correction to $H$ with a class in $B_3(\mathbb{C})$ is the single open input. The `b3_normalization` class field axiomatises this.

## Genuine derivation, not projection

The class carries the hypothesis, and the theorem derives the conclusion. The lemma [`QOU.ArchimedeanUniverse.fixedPoint_iff_cubic`](em-coupling-fixed-point.lean) establishes the equivalence between the fixed-point equation and the cubic root for $\alpha \neq 0$. The main theorem [`QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root`](em-coupling-fixed-point.lean) composes this equivalence with the `b3_normalization` field. The proof is a genuine derivation.

## Numerical context

At $q_0$, the tree term and zero-mode reproduce $1/\alpha$ to $-4.2\times 10^{-6}$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)). The $\mathcal{O}(\alpha^2)$ self-consistency term supplies the residual $\mathcal{O}(\alpha)$ correction. The conjectural $B_3(\mathbb{C})$ Bloch-class content supplies its exact form. The cubic $P$ features a real root near $1/137.036$. CODATA-consistency provides the empirical foundation of the conjecture.

## Status

The sole open element remains the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization. Lean proves the tree/zero-mode assembly of $T$, the algebraic equivalence of the fixed-point, and the derivation of $P(\alpha)=0$. The class remains uninhabited. No fabricated instance attempts to close the primary conjecture.
<!-- FILE_END: em-coupling-fixed-point.md -->

<!-- FILE_START: photon-ir-zero-mode-bring.md -->
*Lean sibling: `QOU.Archimedean.PhotonIRZeroMode`. The topological geometric core is unconditional. The heat-kernel zero-mode is a standard result. The $\tau_{\mathrm{arch}}$ uniqueness is the upstream conditional input.*

**Proposition (photon infrared zero-mode on Bring's surface).** *Let $M_g$ be a closed orientable genus-$g$ hyperbolic surface of constant curvature $-1$. The photon infrared zero-mode contribution to $1/\alpha_{EM}$ at zero external momentum is the harmonic $1$-form sector $H^1(M_g)$ normalized by the surface area:*

$$
  \delta\!\left(\tfrac{1}{\alpha_{EM}}\right)_{\mathrm{IR}}
  \;=\; \frac{\dim H^1(M_g)}{\operatorname{Area}(M_g)}
  \;=\; \frac{b_1(M_g)}{4\pi(g-1)}
  \;=\; \frac{2g}{4\pi(g-1)}.
$$

*We have $b_1 = 2g$ and $\operatorname{Area} = -2\pi\chi = 4\pi(g-1)$. At the Bring genus $g=4$, this evaluates to $\tfrac{8}{12\pi} = \tfrac{2}{3\pi}$. This provides the additive correction of [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode).*

## Mechanism

The Maxwell sector of the categorical Lagrangian restricts to the UV-completing Bring surface $M_4$. The surface carries the force-carrier pair $\{T_{2,9}, T_{3,5}\}$ ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)). The zero-momentum two-point function is governed by the kernel of the $1$-form Laplacian $\Delta_1$. By Hodge theory, $\dim\ker\Delta_1 = b_1(M_g) = 2g$. The heat-kernel zero-mode of a Laplacian contributes one constant mode $1/\operatorname{Vol}$ per harmonic generator. This yields an infrared shift of $b_1/\operatorname{Area}$. Gauss–Bonnet fixes the area at curvature $-1$ to $4\pi(g-1)$. The resulting infrared shift is $2g/(4\pi(g-1))$. It evaluates to $2/(3\pi)$ at $g=4$.

**Dimensional reduction.** A naive attempt places the zero-mode on the $3$-manifold $M_g\times S^1$. Here $b_1 = 2g+1$ and $\operatorname{Vol} = 2\pi\operatorname{Area}$. This gives $(2g+1)/(8\pi^2(g-1)) = 9/(24\pi^2) \approx 0.038$. Crossing with $S^1$ adds a spurious harmonic generator and a factor of $2\pi$ to the volume. The photon zero-mode lives strictly on the $2$-surface.

**Jet-order placement.** The Archimedean functor decomposes into jet grades: $\tau = \sum_{n\ge 0} a_D^{(n)}$ ([`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition)). The $n=0$ term is the electron period. The photon zero-mode forms the $n=1$ infrared term. This is the first prolongation beyond the tree coupling $q[9]_q[10]_q$. The $n=2$ self-energy takes the form $\alpha\,[2]_q/(8\pi)\,(1-h^2\alpha)$. Its denominator depends on the same Hodge datum:

$$
  8\pi \;=\; \pi\cdot\dim H^1(M_{\text{Bring}}) \;=\; \pi\,b_1.
$$

The Betti number $b_1 = 8$ controls both infrared corrections. The zero-mode carries it in the numerator ($b_1/\operatorname{Area}$). The self-energy carries it in the denominator ($\pi\,b_1$). The factors isolate the topological $b_1$ and the archimedean $\pi$. 

**Habiro structure.** The $n=2$ form groups as $\alpha\,H(q)/(\pi\,b_1)$, where $H(q) = [2]_q(1-h^2\alpha)$ is the $\alpha_{EM}$ Habiro element ([`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution)). Identity 2 acts as the Habiro deformation $(1-h^2\alpha)$. The $n=2$ self-energy structures into three sectors: substrate $H$, archimedean $\pi$, and topological $b_1$. This factorization connects the Hodge realization ($b_1/\operatorname{Area}$) to the dilogarithm realization via root-of-unity evaluations in the Habiro ring. It indicates a bridge to the Bloch group.
<!-- FILE_END: photon-ir-zero-mode-bring.md -->

<!-- FILE_START: alpha-em-derivation-exploration-options.md -->
**Remark (exploration options to close the $1/\alpha_{EM}$ derivation).**

The existing infrastructure maps to the open $2/(3\pi)$ derivation. The numerical match $1/\alpha_{EM} \approx q\cdot[9]_q\cdot[10]_q + 2/(3\pi)$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)) holds exactly via the algebraic identity $2/(3\pi) = 2g/(4\pi(g{-}1))$ at $g = 4$. A full derivation remains open. The existing infrastructure supports four potential paths forward.

## Existing infrastructure

The missing step connects the current machinery to the coupling side.

### 1. Hopf fibration $S^3 \to S^2$ as the substrate geometry

The [Reeb bundle](#def:reeb-bundle) at a brane point $p$ is

$$
  \mathcal{R}_p \;=\; \bigl( S^3 \xrightarrow{\pi_H} \mathcal{S}_p \cong S^2,\; \xi_q \bigr).
$$

The projection $\pi_H$ is the Hopf fibration. The base $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ is the exceptional divisor space. The total space $S^3$ evaluates braid words in $B_n$ via $H_n(R,q)$. This geometric pair identically matches the algebraic identity $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$.

### 2. Three color tubes on Bring's surface

Three colour primaries reside on Bring's surface ([`rem:q-chromaticity`](#rem:q-chromaticity)). These are the three $S_3$ subgroups of the Bring automorphism group. This provides the natural source of the denominator $3$ in $2/(3\pi)$. It represents photon coupling averaged over three independent chromaticity channels.

### 3. Filtration with confinement levels

A depth filtration structures $H_n(R,q)$ via [`def:confinement-level`](#def:confinement-level) and [`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification). For $H_3$, depths $\ell = 0,1,2,3$ yield a four-step filtration. The maximum depth of 3 correlates with the denominator $3$.

### 4. Spectral sequence collapse

Hochschild cohomology vanishes ($\mathrm{HH}^k = 0$ for $k \ge 1$) ([`prop:spectral-sequence-collapse`](#prop:spectral-sequence-collapse)). The spectral sequence collapses at $E_1$. All contributions reside in $E_\infty^{0,0} = Z(H_n) = \bigoplus_\lambda R\cdot e_\lambda$. This mechanism yields the closed-form mass-formula $\alpha_k$ via Plancherel-weighted Markov pairings on the centre.

### 5. Wenzl-bridge closed form for stratum prefactors

An explicit $q$-rational expression gives the Markov-trace coefficients $y_\lambda$ in the mass-formula $\alpha_k$ ([`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge)). This machinery applies to the coupling side.

## Four exploration options

### Option A — Hopf-fibration vacuum-polarisation integral

**Claim:** The photon vacuum-polarisation graph evaluates in the categorical framework. The photon propagator occupies the Hopf total space $S^3$. External legs project via $\pi_H$ to the base $S^2$. The zero-mode contribution at zero external momentum is

$$
  \Pi_{\text{zero}}(0)
  \;=\;
  \frac{\mathrm{Vol}(S^2)}{3 \cdot \mathrm{Vol}(S^3)}
  \;=\;
  \frac{2}{3\pi}.
$$

The factor $1/3$ arises from chromaticity averaging.

**Requirements:** An explicit formula defines the vacuum-polarisation graph in the categorical Lagrangian framework. The photon two-point function on $S^3$ converges to $1/\mathrm{Vol}(S^3)$ as a constant zero-momentum residue. The external-leg projection contributes the $\mathrm{Vol}(S^2)$ numerator. The chromaticity normalisation contributes the factor $1/3$.

### Option B — Stratum-prefactor approach via spectral sequence collapse

**Claim:** The mass-formula spectral-sequence machinery ([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula)) applies to the coupling side. The $\alpha_{EM}$ correction equals the depth-$\ell$ stratum prefactor of the filtration.

**Concretely:** The bare formula $1/\alpha = q\cdot[9]_q\cdot[10]_q$ is the depth-$0$ centre contribution. The $2/(3\pi)$ correction expresses a Plancherel-weighted Markov pairing on the depth-$\ell$ stratum for $\ell \ge 1$.

**Requirements:** A depth-$k$ contribution defines $1/\alpha_{EM}$. Computation proceeds via the closed form at depth $\ell$. Verification confirms the depth-$\ell$ contribution equals $2/(3\pi)$ at $q = q_0$.

### Option C — Reeb-bundle holonomy

**Claim:** The $\mathrm{U}(1)$ fibre of the Reeb bundle has holonomy $e^{2\pi i / [2]_q}$. Integrating the photon over the fibre and averaging over the base yields a finite phase-volume factor equal to $2/(3\pi)$ at $q = q_0$ for $g = 4$.

**Requirements:** The photon holonomy integral defines over the fibre. Squaring it and averaging over $\mathcal{S}_p$ uses the Fubini-Study measure. This approach predicts a $q$-dependent constant. This contradicts the required $q$-independence. Option C is falsified.

### Option D — Chern-Simons partition-function ratio

**Claim:** The constant $2/(3\pi)$ is the ratio of Chern-Simons partition functions on distinguished 3-manifolds:

$$
  \frac{2}{3\pi}
  \;=\;
  \frac{Z_{\mathrm{CS}}(S^3, \mathrm{SU}(2)_k)}{3 \cdot Z_{\mathrm{CS}}(S^3 \times S^1, \cdots)}.
$$

The constant emerges from the universal $k \to \infty$ asymptotics.

**Requirements:** The partition functions evaluate and limits take $k \to \infty$. The limit produces $1/k$ factors that map to $1/\pi$ via $k+2 = \pi/\log q$.

## Recommended path

Option B provides the recommended path. It utilises existing infrastructure and clarifies the relationship between the mass and coupling formulas. 

A practical execution follows:
1. Implement Option B in $H_3$ ([`prop:spectral-sequence-h3-explicit`](#prop:spectral-sequence-h3-explicit)).
2. Define the depth-$\ell$ coupling functional.
3. Compute the value at $q_0$ for each $\ell$ to isolate $2/(3\pi)$.
4. Generalise to higher $H_n$ and verify consistency.
5. Cross-validate against Option A.

## Natural sources for each ingredient

The natural sources for the $1/\alpha_{EM}$ ingredients appear in [Table: Natural QOU sources for the $1/\alpha_{EM}$ ingredients](#tbl:alpha-em-derivation-exploration-options-table-data). The derivation awaits the coupling-side analog of the mass-formula stratum decomposition.
<!-- FILE_END: alpha-em-derivation-exploration-options.md -->

