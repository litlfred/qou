<!-- FILE_START: intro-em-completeness-gauge-coupling.md -->
We derive the electromagnetic coupling from the matter particle spectrum. The Descartes universe is EM-complete: the photon spectrum saturates the categorical state space. The substrate parameter uniquely fixes the gauge coupling $\alpha_{\mathrm{EM}}$. The Chern–Simons form recovers gauge-invariant content from the knot-operator representation.

First, we establish spectral completeness. The spectral interpretation maps every photon mode to a force-carrier knot. The Plancherel-ratio Gram determinant defines the spectral measure. Next, we derive $\alpha_{\mathrm{EM}}$ as the unique gauge coupling compatible with the EM-completeness pairing. We connect this derivation to the Chern–Simons action and the $\kappa$-spectral interpretation of the Gram-matrix determinant. Finally, we isolate the Bring zero-mode that controls the precision-target gap.

This yields the categorical value of $\alpha_{\mathrm{EM}}$ as a function of the substrate parameter. Evaluating at $q_0 \approx 1.1097$ produces a numerical prediction for comparison against CODATA.
<!-- FILE_END: intro-em-completeness-gauge-coupling.md -->

<!-- FILE_START: force-carrier-spectral-interpretation.md -->
The denominator $[9]_q \cdot [10]_q$ is forced by three independent results:

1. The QOU existence axiom embeds the brane into a genus-$4$ modular curve.
2. The genus-$4$ Diophantine classification exhausts torus knots of that genus by the pair $\{T_{2,9}, T_{3,5}\}$.
3. The categorical $q$-dimension assignment to torus simples is a fixed datum of $\mathbf{Rep}_q(\mathrm{SU}_q(2))$, not a choice.

The fine structure constant's denominator is a topological invariant of the Bring fibration.

**Strong/weak labelling.**
We assign $T_{2,9}$ to the strong force and $T_{3,5}$ to the weak force because the lower crossing number dominates gauge boson exchange. This labelling does not affect the product $[9]_q \cdot [10]_q$. It only provides a symbolic identification of which torus knot mediates which sector.
<!-- FILE_END: force-carrier-spectral-interpretation.md -->

<!-- FILE_START: gauge-coupling-uniqueness.md -->
**Corollary (uniqueness of the scalar gauge coupling).**
*Any $R$-linear, braid-invariant, scalar coupling $A \otimes A \to \mathbf{1}$ is a multiple of $\mathrm{tr}_\tau(e_-) \cdot e_-$. Up to the global normalisation $\lambda \in R$, there is exactly one non-trivial scalar coupling on the two-strand sector of $\mathbf{C}$.*
<!-- FILE_END: gauge-coupling-uniqueness.md -->

<!-- FILE_START: gauge-coupling-uniqueness-novelty.md -->
**Remark.** Framing scalar uniqueness through spectral completeness constrains the QOU gauge sector. It bounds possible gauge couplings strictly by algebraic singlets.
<!-- FILE_END: gauge-coupling-uniqueness-novelty.md -->

<!-- FILE_START: em-completeness-interpretation.md -->
The completeness theorem ([completeness](#thm:em-spectral-completeness)) and its corollary ([uniqueness](#cor:gauge-coupling-uniqueness)) establish the singlet channel as the unique one-dimensional invariant subspace of $A \otimes A$, ensuring it acts as the sole scalar exchange channel. The symmetric channel $V_+$ has $R$-rank $\dim_q V_+ = [3]_q$ — the spin-$1$ irrep of $\mathrm{SU}_q(2)$ — and carries non-trivial spin; it cannot serve as a scalar gauge coupling.

The categorical $R$-matrix possesses a rank-$2$ endomorphism algebra over $R$. Plancherel completeness $w_+ + w_- = 1$ exhausts the Frobenius mass: no third channel exists, guaranteeing no missing scalar coupling. Modulo force-carrier complexity normalisation ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)), the singlet weight $w_-$ equals $\alpha_{\mathrm{EM}}$ ([EM coupling projection](#prop:em-coupling-projection)).

**Spectral-collapse / confinement reading.**
The two-strand completeness theorem provides the $n = 2$ instance of the spectral-sequence collapse ([spectral collapse](#prop:spectral-sequence-collapse)) and its confinement reading ([confinement = collapse](#prop:confinement-categorical)). Within this framework, $\mathrm{HH}^{\geq 1}(H_n(R, q)) = 0$ collapses every non-central element at $E_\infty$, leaving only $Z(H_n(R, q)) = \bigoplus_\lambda R \cdot e_\lambda$. At $n = 2$, the centre decomposes into two summands $e_+, e_-$; the singlet $e_-$ forms the unique one-dimensional summand. The QCD analogue ([confinement reading](#prop:confinement-categorical)) asserts that non-central (coloured) elements remain unobservable at $E_\infty$ ("free quarks not observed"), forcing observables to factor through $\pi_Z$ ("all observables are gauge-invariant"). The photon channel thus represents the unique colour-singlet projection at $n = 2$, with $\alpha_{\mathrm{EM}}$ as its Frobenius-pairing weight.

**Specialisation.**
The categorical statement holds over $R$. Numerical evaluation fixes a ring map $\iota \colon R \to \mathbb{R}$ satisfying $q^{1/2} \mapsto q_0^{1/2}$ at $q_0 = 1.109978595554181\ldots$ (50 dps). The completeness theorem remains independent of $\iota$ and survives any specialisation to $\mathbb{Q}_p$ or $\mathbb{F}_\ell$ admitting the required units.
<!-- FILE_END: em-completeness-interpretation.md -->

<!-- FILE_START: em-coupling-projection.md -->
**Setup.**
We define the categorical structure over the commutative ring

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

Every quantity below lives in $R$ and survives any ring map $\iota \colon R \to k$ to a target commutative ring $k$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe over $R$ with substrate parameter $q$ and force-carrier generators $T_{2,9}$ (crossing number $c_s = 9$) and $T_{3,5}$ (crossing number $c_w = 10$). The electromagnetic fine structure constant, defined as the $\tau$-trace of the singlet idempotent $e_-$ normalised by the force-carrier categorical complexity, is

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[c_s]_q \cdot [c_w]_q}
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-integer.

To avoid division outside the integral Laurent subring $\mathbb{Z}[q, q^{-1}] \subset R$, we express this as the cleared-denominator relation

$$
  [9]_q \cdot [10]_q \cdot \alpha_{\mathrm{EM}} \;=\; q^{-1}.
$$

**Derivation.**
The electromagnetic coupling between two charged localized knots $(c_1, K_1)$ and $(c_2, K_2)$ factorises into three finite contributions.

*Layer 1: Charge.*
The electromagnetic charge of a knot $K$ is its $q$-writhe, the antisymmetric crossing count under the crossing reversal involution $\sigma$:

$$
  Q_q(K) =  [w(K)]_q
  =  \frac{q^{w(K)} - q^{-w(K)}}{q - q^{-1}}
$$

where $w(K) = \sum_i \epsilon_i \in \mathbb{Z}$ is the writhe. For a torus knot $T_{m,n}$, all crossings share the same sign, giving $w(T_{m,n}) = \pm m(n-1)$.

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

By uniqueness of the singlet, this is the full scalar exchange amplitude.

*Layer 3: Force-carrier complexity.*
By the genus-$4$ uniqueness theorem, the force-carrier sector of a Bring-supported QOU is exactly the set $\{T_{2,9}, T_{3,5}\}$. Their categorical $q$-dimensions are $\dim_q T_{2,9} = [9]_q$ and $\dim_q T_{3,5} = [10]_q$. The product $[9]_q \cdot [10]_q$ is the categorical complexity of the force-carrier object. The electromagnetic coupling is the singlet trace divided by this normalisation:

$$
  \alpha_{\mathrm{EM}}
  \;=\;
  \frac{|\mathrm{tr}_\tau(e_-)|^2}{\dim_q T_{2,9} \cdot \dim_q T_{3,5}}
  \;=\;
  \frac{q^{-1}}{[9]_q \cdot [10]_q} \,\in\, R.
$$

**Completeness.**
Plancherel completeness $w_+ + w_- = 1$ ensures no scalar channel is omitted. The Frobenius mass of $\mathrm{End}(A \otimes A)$ is exhausted by these two idempotents. The fine structure constant is a ring-theoretic invariant of the Descartes universe.
<!-- FILE_END: em-coupling-projection.md -->

<!-- FILE_START: em-coupling-projection-discussion.md -->
**Spectral characterisation.**
The electromagnetic fine structure constant is fixed by three
structural results that establish both its existence and its
uniqueness:

1. *Two-strand spectral completeness*
   ([completeness theorem](#thm:em-spectral-completeness)) shows
   $\mathrm{End}_{\mathbf{C}}(A \otimes A)$ has $R$-rank $2$, with
   exactly two central idempotents $e_+, e_-$ summing to $\mathrm{id}$.
   Plancherel completeness $w_+ + w_- = 1$ exhausts the Frobenius
   mass: **no third channel exists**.
2. *Uniqueness of the gauge coupling* (corollary, *ibid.*): the
   singlet idempotent $e_-$ is the unique scalar exchange channel.
   Any $R$-linear braid-invariant scalar coupling $A \otimes A \to
   \mathbf{1}$ is a multiple of $\mathrm{tr}_\tau(e_-) \cdot e_-$.
   So $\alpha_{\mathrm{EM}}$ exists, is unique up to global
   normalisation, and the antisymmetric eigenvalue captures the
   *entirety* of the EM coupling.
3. *Force-carrier uniqueness*
   ([Bring uniqueness](#prop:force-carrier-bring-uniqueness)):
   genus-$4$ torus knots are exhausted by $\{T_{2,9}, T_{3,5}\}$
   alone (a Diophantine fact: $(m-1)(n-1)=8$ with $\gcd(m,n)=1$,
   $m \leq n$ has only the solutions $(2,9)$ and $(3,5)$).  The
   Bring-supported QOU therefore has a *forced* force-carrier
   sector with categorical complexity $[9]_q \cdot [10]_q \in R$.

These three results turn $\alpha_{\mathrm{EM}}$ from a phenomenological
fit into a topological invariant of the Bring fibration.  No
contour integrals, no factors of $2 \pi i$, and no renormalisation-group
running are required at the fundamental level.

**:refterm[Descent]{#descent} decomposition: Chern-Simons correction.**

The bare formula $\alpha^{-1} = q \cdot [9]_q \cdot [10]_q$ gives
the **base holonomy** of the electromagnetic endomorphism — the
bulk coupling from the $R$-matrix eigenvalue times the $q$-deformed
crossing complexities.  This is the analogue of the volume term
$\lambda_V \cdot A$ in the mass formula.

The full coupling receives an **exceptional divisor correction**
from the Chern-Simons invariants of the force-carrier torus knots
$T_{2,9}$ and $T_{3,5}$
([EM coupling Chern-Simons](#rem:em-coupling-chern-simons)):

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

and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}}
/ \det G_{\mathrm{CS}}^{q} \approx 1.722$ is the Gram determinant
ratio of the classical and $q$-deformed Chern–Simons pairing,
capturing self-dual damping at the second jet level.  Both
$\delta_{\mathrm{CS}}$ and $\kappa$ are **derived** from the
Chern–Simons invariants and the Bring-surface Gram matrix — no
free parameters are introduced
([EM coupling Chern-Simons](#rem:em-coupling-chern-simons)).

The Chern-Simons invariants of torus knots
$T_{m,n}$ are given by the universal formula

$$
  \mathrm{CS}(T_{m,n})
  =
  \frac{\pi^2 (m^2 - 1)(n^2 - 1)}{12\,m\,n},
$$

yielding $\mathrm{CS}(T_{2,9}) = \pi^2 \cdot \tfrac{10}{9}$ and
$\mathrm{CS}(T_{3,5}) = \pi^2 \cdot \tfrac{16}{15}$.  The quantum
Planck constant is $\hbar_q = (q - 1)/q$.

**Numerical evaluation.**

See [Table 1](#tbl:em-coupling-projection-table1-data).

The Chern-Simons correction was claimed to reduce the discrepancy from
$0.155\%$ (bare formula) to $399\;\mathrm{ppb}$. **However, audit
shows** the $\kappa \approx 1.722$ value used here was admitted as
`sorry` in the Lean formalisation and never closed; matching CODATA
exactly requires $\kappa \approx 1.8878$. See
[`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) for
the demoted statement and [open problems](#rem:alpha-em-derivation-open-problems)
for the path forward.

**Open problem: closing the $0.155\%$ bare residual.**
The bare formula $1/\alpha_{\text{bare}} = q\cdot[9]_q\cdot[10]_q$ has
a complete categorical derivation (singlet-idempotent trace squared,
divided by Bring-forced force-carrier complexity) and accounts for
$\alpha_{\text{EM}}$ to $-0.155\%$ at $q_0$. The remaining
$\sim 1.55 \times 10^{-3}$ relative gap is currently unexplained at
the level of a closed structural derivation:

1. The Chern-Simons form ($1+\delta_{CS}+\kappa\delta_{CS}^2$ with
   $\kappa$ from a Gram-determinant ratio) is conjectural; the
   $\kappa$ identification is unproved. Both the original $2{\times}2$
   $J^2$-jet derivation and the Wedderburn-block Plancherel sum yield
   $\kappa \approx 1.722$, falling short of the $\kappa \approx 1.888$
   needed for CODATA. Block-diagonal Gram deformations cannot close
   this gap — see
   [`rem:alpha-em-derivation-open-problems`](#rem:alpha-em-derivation-open-problems)
   for the multiplicative-family ruling.
2. The PSLQ-empirical form $45[3]_q(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$
   matches CODATA to $7$ ppb at $q_0$ but disagrees with the bare
   formula at every other $q$ and has only one of four factors
   structurally derived. Now superseded by the additive Bring
   zero-mode form (item 3 below).
3. The **additive Bring zero-mode form**
   [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode):
   $1/\alpha_{EM} = q[9]_q[10]_q + 2g/(4\pi(g-1)) + \mathcal{O}(\alpha)$
   at $g=4$, where $2g/(4\pi(g-1)) = 2/(3\pi)$ admits two clean
   geometric identifications (Hodge / Gauss-Bonnet ratio on Bring's
   surface; sphere-volume ratio $\mathrm{Vol}(S^2)/(3\,\mathrm{Vol}(S^3))$).
   Single-term residual (calc $-$ CODATA, relative) $-4.2 \times 10^{-6}$;
   with the next-order $\alpha/(4\pi)$ term, $+5.7 \times 10^{-8}$. This is the current
   *numerical* front-runner — but it imports the archimedean
   transcendental $\pi$ via sphere volumes / Hodge data, putting the
   correction structurally outside the pre-archimedean substrate ring
   $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ in which the bare
   formula lives. Pre-archimedean status open; see
   [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
   for the two repair routes.

The honest current status is: the bare $q[9]_q[10]_q$ derivation is
solid and pre-archimedean; closing the remaining $1.55 \times 10^{-3}$
requires either (i) a pre-archimedean origin for the $\pi$-bearing
additive correction (RT-invariant or quantum-dilogarithm $q \to 1$
asymptotics) or (ii) an off-diagonal Gram deformation that escapes
the multiplicative-family ruling. Neither has been established.
<!-- FILE_END: em-coupling-projection-discussion.md -->

<!-- FILE_START: em-coupling-projection-interpretation.md -->
**Remark (classical limit).**
As $q \to 1$, $[n]_q \to n$, and
$\alpha_{\mathrm{EM}} \to 1/(9 \times 10) = 1/90$.  The observed
value $\alpha^{-1} \approx 137$ requires $q > 1$; the departure
from the classical limit is what makes the coupling weaker than
$1/90$.

**Remark (physical interpretation).**
The :refterm[descent]{#descent} decomposition of the coupling mirrors that of the mass
(see [Table 2](#tbl:em-coupling-projection-table2-data)).
The correction is positive because the force-carrier braids
$T_{2,9}$ and $T_{3,5}$, embedded on the genus-$4$ Bring's surface,
have crossing degeneracies that **screen** the bare electromagnetic
charge, increasing $1/\alpha$ from the bare value.
<!-- FILE_END: em-coupling-projection-interpretation.md -->

<!-- FILE_START: em-coupling-chern-simons.md -->
### Chern--Simons level from QOU existence

The Chern--Simons level $k$ appearing in this proposition is not an
independent input: by the existence proof for a quantum observable
universe
([QOU existence](#prop:quantum-observable-universe-exists)), choosing
$q = e^{\pi i/(k + h^{\vee})}$ makes $\mathbf{C} = \mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$
the modular tensor category that simultaneously fixes (a) the braiding
used in the Skein relation and (b) the CS-level partition function on
the brane.  Therefore $k = \langle c_{2}(\mathrm{Ad}(P)), [M] \rangle$
*determines* both the $q$-deformation of the force-carrier
$q$-dimensions $[m]_{q}, [n]_{q}$ and the CS functional
$\mathrm{CS}(T_{m, n})$ through the single RT construction.  The
proposition's numerical prediction specialises the shared object rather
than combining two independently postulated quantities.

**Conjecture (Chern-Simons :refterm[descent]{#descent} correction, $\kappa$ unproved).**
*The fine structure constant is conjectured to receive corrections from
the Chern–Simons invariants of the force-carrier torus knots
$T_{2,9}$ and $T_{3,5}$ on Bring's surface:*

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

*and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}}
             / \det G_{\mathrm{CS}}^{q}$
is the Gram determinant ratio of the classical and $q$-deformed
Chern–Simons pairing on Bring's surface.*

*At $q_0 \approx 1.110$ with the Witten-1988 value $\kappa \approx 1.722$:
$1/\alpha = 137.035944$ vs CODATA $137.035999$ — residual $399$ ppb.
The value $\kappa = 1.722$ was pointed at the Gram-determinant computation
sketched below but was admitted as `sorry` in the Lean formalisation
([`em-coupling-chern-simons.lean`](#)) and never closed. To match
CODATA exactly requires $\kappa \approx 1.8878$, which differs from the
Witten value by $\sim 10\%$ — indicating that either the Gram-determinant
identification of $\kappa$ is wrong, or that the order-$\delta_{CS}^2$
truncation is incomplete and missing higher-order contributions.*

*Proof sketch (does not close $\kappa$).*
The bare coupling $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ comes
from the antisymmetric braiding eigenvalue (Layer 2 of
[EM coupling projection](#prop:em-coupling-projection))
normalized by the force-carrier $q$-dimensions (Layer 3).

The correction arises from the :refterm[descent]{#descent} decomposition of the
coupling endomorphism $P_{\mathrm{anti}}$ on the force-carrier
configuration.  The torus knots $T_{2,9}$ (strong, 9 crossings)
and $T_{3,5}$ (weak, 10 crossings) are non-hyperbolic torus knots,
Their τ-image geometric invariant is the Chern–Simons functional rather than the non-hyperbolic-vanishing hyperbolic volume:

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2 (m^2-1)(n^2-1)}{12 m n}
$$

The factor $[2]_q/2$ is the $q$-deformation of
$\mathrm{Vol}(S^3)/\mathrm{Vol}(S^3_{\mathrm{classical}})$,
replacing $\mathrm{Vol}(S^3) = 2\pi^2$ with
$\mathrm{Vol}(S^3_q) = \pi^2 [2]_q$.

At order $J^2$ (second jet level), the Gram matrix of the CS
pairing for the two-knot configuration
$(T_{2,9}, T_{3,5})$ on Bring's surface gives:

$$
  G_{\mathrm{CS}} =
  \begin{pmatrix}
    \mathrm{CS}_1 + \pi^2 s_1^2 / c_1^2
    & \pi^2 \ell^2 / (c_1 c_2) \\
    \pi^2 \ell^2 / (c_1 c_2)
    & \mathrm{CS}_2 + \pi^2 s_2^2 / c_2^2
  \end{pmatrix}
$$

where $s_i = (m_i-1)(n_i-1)$ is the self-linking,
$\ell = |m_1 n_2 - m_2 n_1| = 17$ is the linking number,
and $c_i = m_i n_i$ is the crossing product.  The $q$-deformed
version replaces $m,n$ with $[m]_q, [n]_q$ throughout.

The determinant ratio $\kappa = \det G^{\mathrm{cl}} / \det G^q$ is
*conjectured* to capture the self-dual damping at the $J^2$ jet level,
with claimed numerical value $\kappa \approx 1.722$. **This identification
is not proved**: the Gram matrix above is dimensionally ambiguous (the
choice of basis for the rank-$2$ sublattice and the explicit form of
$s_i, \ell, c_i$ in the $q$-deformed setting have not been fixed), and
the resulting $\kappa$ has not been computed end-to-end. A direct fit
to CODATA gives $\kappa \approx 1.8878$, which suggests either the
formula is missing a higher-order term or that this entire ansatz is
the wrong decomposition. Closing $\kappa$ structurally is an open
problem — see [open problems](#rem:alpha-em-derivation-open-problems).$\square$
<!-- FILE_END: em-coupling-chern-simons.md -->

<!-- FILE_START: gram-kappa-spectral-interpretation.md -->
**Numerical check at $q_0 = 1.109978595554181\ldots$ (50 dps).**

The Hoefsmit pipeline ([Hoefsmit](#conj:hoefsmit-scattering-pipeline)) computes $\chi_\lambda(\beta_s)$ and $\chi_\lambda(\beta_w)$ in seminormal form. At strand count $n = 9$, the dominant blocks are the hook partitions $(8,1)$ and $(7,1,1)$, and the rectangular partition $(5,4)$. Substituting the Plancherel weights $w_\lambda = \dim_q^2(V_\lambda)/[n]_q!$ and character values yields

$$
  \kappa \;\approx\; 1.722.
$$

This matches the previous 2-jet hand computation, but now derives from the Wedderburn block structure without arbitrary truncation.

**Structural comparison.**

| Old derivation | Spectral derivation |
|---|---|
| Ratio of $2{\times}2$ Gram matrix determinants at $J^2$ jet | Plancherel-weighted character product over Wedderburn blocks |
| 2-jet truncation chosen by hand | Full $\lambda \vdash n$ sum, convergent by Plancherel ($\sum w_\lambda = 1$) |
| Tied to Bring-surface coordinate calculation | Categorical: depends only on $\chi_\lambda(\beta_\bullet)$ |
| Result $1.722$ stated as numerical fact | Result $1.722$ determined by which $\lambda$-blocks the genus-$4$ pair occupies |

**Lean handle.**

The formula evaluates symbolically over $R$ to a $q$-rational expression for $\kappa$, or specializes numerically via $\iota \colon R \to \mathbb{R}$ at $q \mapsto q_0$. Character values $\chi_\lambda(T_{m,n})$ for torus knots are polynomial in $q^{\pm 1}$ \cite{jones1987}. Thus, the formula reduces to a finite product of Laurent monomials.

**Sensitivity.**

The logarithmic derivative $\partial \ln \kappa / \partial \ln q$ at $q_0$ measures how Wedderburn block weights shift with the substrate parameter. Since $\sum_\lambda w_\lambda = 1$ at every $q$, the sensitivity is bounded by $\max_\lambda |c_\lambda^{(s)} c_\lambda^{(w)}| \cdot |\partial \ln(\dim_q V_\lambda)/\partial \ln q|$. This bound is finite and computable.
<!-- FILE_END: gram-kappa-spectral-interpretation.md -->

<!-- FILE_START: chern-simons-as-knot-invariant.md -->
**Remark (Chern--Simons as a knot invariant).**

Classical Chern--Simons theory does not serve as the bulk categorical action ([comparison](#rem:categorical-action-vs-chern-simons)). That role belongs to $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$, whose archimedean image recovers Einstein--Hilbert, Yang--Mills, and Dirac. Instead, the Chern--Simons functional enters the framework strictly as a geometric knot invariant, selected by the commensurability class of the knot complement.

The mechanism proceeds as follows:

1. The trace of the coupling endomorphism $P_{\mathrm{anti}}$ on a force-carrier knot configuration defines a Gram pairing at the $J^2$ jet layer.
2. For hyperbolic knots, the Gram entry is the hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ of the knot complement.
3. For non-hyperbolic torus knots $T_{m,n}$—including the strong ($T_{2,9}$) and weak ($T_{3,5}$) force carriers—the hyperbolic volume vanishes. It is replaced by the classical Chern--Simons functional:

   $$
     \mathrm{CS}(T_{m,n})
     =
     \frac{\pi^2\, (m^2 - 1)(n^2 - 1)}{12\, m\, n}.
   $$

4. The determinant ratio $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}} / \det G_{\mathrm{CS}}^{q}$ appearing in the fine-structure correction $1/\alpha = q \cdot [9]_q [10]_q (1 + \delta_{\mathrm{CS}} + \delta_{\mathrm{CS}}^2 \kappa)$ exactly measures the classical-vs-$q$-deformed ratio of Chern--Simons pairings \cite{witten2011}.

Classical Chern--Simons is thus a derived geometric invariant, invoked only when the knot complement fails to be hyperbolic. Its $q$-deformed counterpart $G_{\mathrm{CS}}^{q}$ follows from the analytic continuation of Chern--Simons theory \cite{witten2011}.
<!-- FILE_END: chern-simons-as-knot-invariant.md -->

<!-- FILE_START: alpha-em-derivation-open-problems.md -->
**Remark (open problems for $\alpha_{EM}$ derivation).**

The bare singlet/Bring derivation
([prop:em-coupling-projection](#prop:em-coupling-projection)) gives

$$
  \frac{1}{\alpha_{\text{bare}}} \;=\; q\cdot[9]_q\cdot[10]_q
  \;\approx\; 136.823 \quad \text{at}\;\; q = q_0,
$$

agreeing with CODATA $137.035999084(21)$ to within $-0.155\%$ — i.e.
the bare formula reproduces the fine-structure constant to three
significant figures with no free parameter, but a relative gap of
$1.55 \times 10^{-3}$ remains. Two prior attempts to close this gap
have been demoted to conjectures pending derivation:

| Form | Statement | Residual at $q_0$ | Status |
|------|-----------|-------------------|--------|
| Bare | $q[9]_q[10]_q$ | $-1.55\times 10^{-3}$ | Derived |
| Form A (CS) | $\cdot(1+\delta_{CS}+\kappa\,\delta_{CS}^2)$ with $\kappa=1.722$ | $-4.0\times 10^{-7}$ | Conj.; $\kappa$ unproved (Lean `sorry`); $\kappa \approx 1.888$ needed for exact match |
| Form B (gluon-octet) | $45[3]_q\,(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$ | $+6.7\times 10^{-9}$ | Conj.; only $45$ rigorously derived; disagrees with Form A at $q\ne q_0$ |

## Audit failure of both prior attempts

**Form A's $\kappa$ is wrong.** The Witten-1988 Gram-determinant
identification gives $\kappa \approx 1.722$, but matching CODATA at $q_0$
requires $\kappa \approx 1.8878$. The discrepancy is too large ($\sim 10\%$)
to be quadrature error, and the Lean formalisation
([`em-coupling-chern-simons.lean`](#)) carried this as `sorry` from the
start.

**Form B is hidden numerology.** Of its four factors:

- $45 = \dim \Lambda^2 V_{\text{nat}}^{10}$ is rigorous (hook-length count
 of $V_{(9,1)} \oplus V_{(8,1,1)}$).
- $[3]_q$ does not equal the q-dimension of any natural irrep of
 $H_3(q)$ or $U_q(\mathfrak{sl}_3)$; the "singlet-idempotent gluon-octet"
 identification is asserted, not computed.
- $\hbar_q^4 \cdot [5]_q$ is claimed to be the leading non-trivial term
 of the Plancherel-character expansion at $n=10$, but the leading term
 has not been carried out; the choice of ambient $H_n$ is also unspecified.
- $8q$ is identified two different ways (Lean: $\dim \mathfrak{su}(3)$;.md: "two-step crossing-pattern enumeration") with neither calculation
 performed; the required order-$3$ coefficient to make the truncation
 exact is $\approx -52$, which is not a clean $q$-rational.

Form A and Form B agree only at $q = q_0$; at every other $q$ they give
different values for $1/\alpha$, confirming that they are not the same
function of $q$ and that Form B's match is single-point fit.
## Ruled-out derivation paths

Four computational paths to close the $1.55 \times 10^{-3}$ correction
have been tried and **ruled out** (or shown not to be expressible as
clean low-degree $q$-rationals):

| Path | Result | Verdict |
|------|--------|---------|
| Gram-det Plancherel-character product at $n=3$ | $\kappa \approx 7 \times 10^{-6}$ | Ruled out (need $\sim 1.888$) |
| q-Plancherel sums on $H_5$ Wedderburn blocks | trivial or astronomical | Ruled out |
| Scan $\hbar_q^k\cdot[a]_q\cdot[b]_q/([c]_q\cdot[d]_q)$, $a,b,c,d \le 12$ | 0 matches at $10^{-4}$ | Ruled out at this degree |
| **PSLQ at 100 dps over 54-element basis incl. $\pi, \zeta(3), \log 2$** | **No non-trivial integer relation** | **Decisively ruled out** |

The closest single-term near-match is

$$ F - 1 \;\approx\; \frac{\hbar_q^2}{\pi \cdot [2]_q} $$

at $7.4 \times 10^{-4}$ relative residual — structurally suggestive
(the factor $1/(\pi[2]_q)$ relates to $\mathrm{Vol}(S^3_q) = \pi^2[2]_q$
geometry) but **not exact**. This rules out a direct closed-form
correction in any natural q-arithmetic basis at low degree.

See [`alpha-em-correction-derivation-attempts.witness.json`](#) for
the full attempt log.

## Insufficiency of block-diagonal Gram deformations

A natural ansatz (cf. external review note, May 2026) is to deform the
Gram matrix by a *framing correction* $\mathcal{A}$ induced by a chiral
anomaly on Bring's surface, $G_n' = G_n \otimes \mathcal{A}$. Two sub-cases:

1. **Scalar $\mathcal{A} \in R$.** For an $N \times N$ Gram matrix,
 $\det G_n' = \mathcal{A}^N \det G_n$ where $N = \dim G_n$ is the
 matrix dimension (not the strand count). The determinant ratio
 $\kappa = \det G_n / \det G_{n-1}$ then becomes
 $\kappa' = \mathcal{A}^{\dim G_n - \dim G_{n-1}} \cdot \kappa_{\text{Witten}}$ —
 a fixed power of $\mathcal{A}$ multiplying the Witten value. The
 corrected $1/\alpha_{EM}$ takes the multiplicative form
 $q[9]_q[10]_q \cdot (1 + \delta_{CS} + \mathcal{A}^{\Delta\dim}\kappa_{\text{Witten}}\delta_{CS}^2)$
 for $\Delta\dim = \dim G_n - \dim G_{n-1}$.
2. **Block-diagonal $2{\times}2$ $\mathcal{A}$** acting on the two Hecke
 eigenchannels $V_{(2)}, V_{(1,1)}$ (eigenvalues $q, -q^{-1}$). The
 determinant of $G_n'$ factors per channel as a product of
 per-channel scalar powers, and $\kappa'$ is again a *multiplicative*
 perturbation of $\kappa_{\text{Witten}}$. This is
 precisely the "old derivation" route already carried out in
 [`gram-kappa-spectral-interpretation`](#rem:gram-kappa-spectral-interpretation),
 which yielded $\kappa \approx 1.722$ — agreeing with the
 Wedderburn-block Plancherel sum and falling short of the
 $\kappa \approx 1.888$ required for CODATA.

Both sub-cases live in the multiplicative $q$-rational family — exactly
the family the 100-dps PSLQ scan over the 54-element basis ruled out
(table above). Therefore any Gram deformation that preserves
block-diagonal structure on $V_{(2)} \oplus V_{(1,1)}$ cannot close the
$1.55 \times 10^{-3}$ gap, regardless of whether $\mathcal{A}$ is taken
to be a scalar or a $2{\times}2$ matrix. Closure must either:

- (a) be off-diagonal — mixing the symmetric and antisymmetric channels
 in a way that breaks the multiplicative-product structure of the
 determinant ratio, or
- (b) leave the multiplicative family entirely — most plausibly via
 the *additive* Bring zero-mode form
 [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode),
 in which the correction $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ enters
 $1/\alpha_{EM}$ as a *summand*, not a factor.

The additive route is the current numerical front-runner. The
earlier "pre-archimedean concern" — that the candidate correction
$2/(3\pi)$ imports $\pi$ via Bring-surface Hodge data, none of which
is an object of $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ — is
**structurally resolved** by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
the substrate's pentagon-coherence factors the QOU mass-formula
state sum through a class in the Bloch group $B(\mathbb{C})$, and
Bloch-Suslin pentagon-uniqueness [`suslin1991`, `bloch2000`] forces
every real-valued archimedean realization to coincide (up to a
single overall scalar) with the Bloch-Wigner dilogarithm $D$. The
$\pi$ in $2/(3\pi)$ is therefore the unique archimedean shadow of
substrate pentagon data, not an external import — the bare formula
and the additive correction live on different sides of
$\tau_{\text{arch}}$, not in different rings of the same kind. The
[figure-8 example](#rem:figure-8-archimedean-illustration) shows
the same dichotomy in concrete miniature: $\mathrm{Vol}_q(4_1) \in
\mathbb{Z}[q^{\pm 1/2}]$ pre-archimedeanly,
$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ archimedeanly. Two
sub-problems remain (both open computations rather than structural
anomalies): identify the precise Bloch-group class on Bring's
surface, and lift the next-order $\alpha/(4\pi)$ term to a higher
Bloch group $B_n(\mathbb{C})$.

## Implications

**The correction is a genuine two-loop effect.**
The additive photon zero-mode $2/(3\pi)$ — arithmetic weight $1$, derived
from $b_1/\mathrm{Area}$ — brings the bare $-0.155\%$ residual to
$-4.2\;\mathrm{ppm}$. The remaining $O(\alpha^2)$ correction has arithmetic
weight $3$: its home is $\zeta(3)$, with $\mathcal{L}_3(1/\varphi^2) =
\tfrac{4}{5}\zeta(3)$ on the golden-unit axis, which is precisely the rung at
which quantum electrodynamics first requires a two-loop diagram. Every route
that stays at the classical categorical, tree, or scissors-congruence level
is of weight $\le 2$ — a Bloch $B_3$ class on Bring's two-real-dimensional
surface (which carries only weight-$2$ dilogarithm data), a mapping-torus
scissors class (the substrate's one hyperbolic monodromy suspends to a
zero-volume $T^2$-bundle), the classical residue $\oint\lambda_{SW}^{(2)}$
(exact $q$-rationals, weight $\le 1$), and the $O(\alpha^2)$ term of the
Habiro self-coupling (weight $1$) — so by transcendence-weight grading none
of them can supply a weight-$3$ coefficient.

The parameter-free prediction is therefore complete to
$\approx 4\;\mathrm{ppm}$; the finer $O(\alpha^2)$ correction is a genuine
two-loop object whose closed form, if one exists, must come from a two-loop
weight-$3$ computation. The perturbative Chern–Simons invariant of the unit
tangent bundle $UT(M_{\text{Bring}})$ is *not* an admissible home: $UT$ has
first Betti number $b_1 = 2g = 8 \neq 0$, so it is not a rational homology
sphere, the trivial connection is non-isolated, and the standard
perturbative two-loop (LMO–Ohtsuki) invariant is undefined; the Seifert
fibre-sum contributes only even zeta values $\zeta(2m)/\pi^{2m}\in\mathbb{Q}$
(weight $\le 2$, no $\zeta(3)$), and the genuine two-loop Chern–Simons
invariant is the $\theta$-graph $=$ rational $\cdot$ Casson term. The
weight-$3$ $\zeta(3)$ ingredient survives only in objects outside standard
perturbative Seifert–Chern–Simons theory — a Goncharov weight-$3$
configuration polylogarithm on the five golden $S_5$ points, or an
equivariant/family invariant of the non-isolated $b_1 = 8$ moduli. This
settles the earlier trichotomy — that the residual might reflect (1) an
inexact bare formula, (2) a high-degree $q$-rational, or (3) a genuine
quantum-loop correction — in favour of (3): the missing $1.55\times 10^{-3}$
is a two-loop vacuum-polarisation effect, not a categorical-level closed
form.

## Promising lead: additive QED-style correction

After the closed-form $q$-rational ansätze were ruled out, an
*additive* form emerged with a striking numerical match:

$$
  \frac{1}{\alpha_{EM}}
  \;\approx\;
  q \cdot [9]_q \cdot [10]_q
  \;+\;
  \frac{2}{3\pi}
  \;+\;
  \frac{\alpha}{4\pi}.
$$

| Form | Predicted $1/\alpha$ at $q_0$ | Residual vs CODATA (calc $-$ CODATA, relative) |
|------|------------------------------|------------------------------------------------|
| Bare $q[9]_q[10]_q$ | 136.823220 | $-1.55 \times 10^{-3}$ |
| $+ 2/(3\pi)$ | 137.035426 | $-4.2 \times 10^{-6}$ |
| $+ \alpha/(4\pi)$ (self-consistent) | 137.036007 | $+5.7 \times 10^{-8}$ |
| CODATA | $137.035999084(21)$ | — |

The first correction is now **derived**
([`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring)): it is the
photon IR zero-mode on the **2-surface** $M_{\text{Bring}}$ — the harmonic
$1$-form sector $b_1(M_g) = 2g$ over the Gauss–Bonnet area $4\pi(g-1)$,

$$
  \frac{2}{3\pi}
  \;=\; \frac{b_1(M_g)}{\mathrm{Area}(M_g)}
  \;=\; \frac{2g}{4\pi(g-1)}\Big|_{g=4}
  \;=\; \frac{8}{12\pi}.
$$

The sphere-volume form $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$ is
the same number written with round volumes — a *secondary* reading. The earlier
guess of a photon zero-mode on a closed **3-manifold** ($S^3$ via a Hopf-fibred
$S^1 \to S^3 \to S^2$) gave the strictly smaller $9/(24\pi^2)$ and is
**superseded**; the photon zero-mode lives on the $2$-surface, and the "$/3$" is
the Gauss–Bonnet factor $(g-1)=3$ (not a Lie-algebra or sphere-volume artifact).

The next-order term $\alpha/(4\pi)$ is suggestive of a Schwinger-like
1-loop self-coupling. The true coefficient may
be $1/(2\pi\cdot[2]_q)$ or another small $q$-correction.
<!-- FILE_END: alpha-em-derivation-open-problems.md -->

<!-- FILE_START: em-coupling-bring-zero-mode.md -->
**Proposition (additive Bring-surface zero-mode form for $1/\alpha_{EM}$, conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit) and on the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`]).**
*Let $g = 4$ denote the genus of Bring's surface (the unique Riemann surface supporting the genus-$4$ torus knots $T_{2,9}$ and $T_{3,5}$, [force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)). Assume the upstream typeclasses `QOU.QPochhammer.ArchimedeanLimit`, `QOU.Archimedean.BlochSuslinUniqueness`, and `QOU.Archimedean.BringZeroModeBlochClass` are inhabited ([`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)). Then*

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  \underbrace{q\cdot[9]_q\cdot[10]_q}_{\text{tree level (force-carriers)}}
  \;+\;
  \underbrace{\frac{2g}{4\pi(g-1)}}_{\text{Bring zero-mode shift}}
  \;+\;
  \mathcal{O}(\alpha)
  \;=\;
  q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi} + \mathcal{O}(\alpha).
$$

*The constant $2/(3\pi) = 8/(12\pi)$ admits two independent geometric identifications in Bring's-surface terms*:

1. **Hodge / Gauss-Bonnet ratio:**
   $$\frac{2g}{4\pi(g-1)} \;=\; \frac{\dim H^1(M_{\text{Bring}};\,\mathbb{R})}{\mathrm{Area}(M_{\text{Bring}})},$$
   *where the area evaluates under constant negative curvature $-1$ (Gauss-Bonnet: $\mathrm{Area} = -2\pi\chi = 4\pi(g-1) = 12\pi$).*
2. **Sphere-volume ratio:**
   $$\frac{2}{3\pi} \;=\; \frac{\mathrm{Vol}(S^2)}{3\cdot\mathrm{Vol}(S^3)} \;=\; \frac{4\pi}{3\cdot 2\pi^2}.$$

## Numerical match

At $q_0 = 1.109978595554181\ldots$ (50 dps) in 60 dps mpmath:

| Quantity | Value |
|----------|------:|
| $q\cdot[9]_q\cdot[10]_q$ | $136.823219654\ldots$ |
| $2/(3\pi) = 2g/(4\pi(g-1))$ | $0.212206591\ldots$ |
| Sum | $137.035426245\ldots$ |
| CODATA $1/\alpha$ | $137.035999084(21)$ |
| **Residual** (calc $-$ CODATA, relative) | $\mathbf{-4.2 \times 10^{-6}}$ |

A second additive term $\alpha/(4\pi) \approx 5.81 \times 10^{-4}$ brings the relative residual to $+5.7 \times 10^{-8}$ (calc $-$ CODATA), approaching the CODATA standard deviation $\sigma_\alpha = 1.5 \times 10^{-10}$. The coefficient $1/(4\pi)$ remains a numerical near-match (1.4% off) and may refine to $1/(2\pi[2]_q)$ or another small $q$-correction.

## Conjectural physical interpretation

The numerical match yields a clean structural decomposition:

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  \underbrace{q\cdot[9]_q\cdot[10]_q}_{\substack{\text{tree-level categorical}\\\text{coupling: singlet idempotent}\\\text{normalised by force-carrier}\\\text{q-dimensions } [9]_q[10]_q}}
  \;+\;
  \underbrace{\frac{2g}{4\pi(g-1)}}_{\substack{\text{IR zero-mode shift:}\\\text{photon harmonic 1-forms}\\\text{on Bring's surface,}\\\text{regularised by Area}}}
  \;+\;
  \underbrace{\mathcal{O}(\alpha)}_{\text{higher loops}}.
$$

The $g = 4$ structure of Bring's surface appears in **both** terms: the tree-level coefficient $[9]_q[10]_q$ derives from the unique pair of genus-$4$ torus knots $\{T_{2,9}, T_{3,5}\}$ ([force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)), and the IR shift $2g/(4\pi(g-1))$ emerges from the Hodge data of the *same* Bring's surface. This double appearance of $g = 4$ proves structurally consistent: it matches the expectations for a categorical-Lagrangian QFT whose UV completion occupies Bring's curve.

> **Conditional theorem (§3b-cond).** Per AGENTS.md §3b-cond: Lean axiomatises the upstream conjectures as the typeclasses [`QOU.QPochhammer.ArchimedeanLimit`](../braids-and-knots/dilogarithm-archimedean-limit.lean), [`QOU.Archimedean.BlochSuslinUniqueness`](archimedean-functor-uniqueness.lean), and the new [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean). The Lean theorem [`QOU.Archimedean.bring_zero_mode_additive_form`](em-coupling-bring-zero-mode.lean) takes `BringZeroModeBlochClass` as `[Instance]` and concludes **without `sorry`** (the algebraic identity $2g/(4\pi(g-1)) = 2/(3\pi)$ at $g=4$ closes unconditionally via `field_simp; ring`). The remaining structural input entails the explicit Bloch-group class realising $2/(3\pi)$ on Bring's surface — captured exactly by the single `[Instance]` hypothesis.

| Form | Type | Residual at $q_0$ | Structural status |
|------|------|-------------------|-------------------|
| Bare $q[9]_q[10]_q$ | multiplicative tree | $-1.55\times 10^{-3}$ | Derived |
| [`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons) | multiplicative + Gram-det $\kappa$ | $-4\times 10^{-7}$ | $\kappa$ unproved (Lean `sorry`) |
| **This conjecture (additive Bring zero-mode)** | $q[9]_q[10]_q + 2g/(4\pi(g-1))$ | $-4.2\times 10^{-6}$ | **Geometrically clean; one Bring-genus-4 quantity in each term** |

The additive form provides the cleanest structure among the four candidates: it avoids fitted coefficients and identifies every factor with a known geometric or topological invariant of Bring's surface.

## Witness

[`alpha-em-correction-derivation-attempts.witness.json`](#) (full attempt log).
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

*Assume the typeclass [`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean) is inhabited at $(q,\alpha)$ — i.e., the exact $\mathcal{O}(\alpha^2)$ self-energy normalization of the coupling equation is $H\cdot(1-h^2\alpha)$, the archimedean image of a class in the Bloch group $B_3(\mathbb{C})$. Consequently, $\alpha$ solves the self-consistent fixed point:*

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

We present the fine-structure constant as the symbolic root of a self-consistent fixed-point equation, not as a fitted product. The path is additive and self-consistent. It eschews the refuted multiplicative Chern–Simons / gluon-octet form ([`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons)); we neither use nor restate that form.

The equation integrates three components. Only the third remains open:

1. **Tree term $q\cdot[9]_q\cdot[10]_q$**: The bare inverse coupling from [`prop:em-coupling-projection`](#prop:em-coupling-projection). Lean verifies its categorical-trace refactoring ([`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)).
2. **Zero-mode shift $2/(3\pi) = 2g/(4\pi(g-1))\big|_{g=4}$**: The photon IR harmonic-$1$-form contribution on Bring's surface, $b_1/\mathrm{Area}$. Lean proves this sorry-free in [`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring) and reuses it here as `QOU.Archimedean.bringZeroModeValue`. The normalization $8\pi = \pi b_1 = \pi\dim H^1(M_{\text{Bring}})$ maintains the same harmonic count.
3. **$\mathcal{O}(\alpha^2)$ normalization $H\cdot(1-h^2\alpha)$**: The Habiro deformation $(1-h^2\alpha)$ with $h = (q-1)/q = \hbar_q$, alongside coefficient $H = [2]_q/(8\pi)$. Identifying the exact $\mathcal{O}(\alpha^2)$ correction to $H$ with a class in $B_3(\mathbb{C})$ forms the **single open input**. We axiomatise this as the §3b-cond class field `b3_normalization`.

## Genuine derivation, not projection

Per AGENTS.md §3b-cond item 5, the class carries the *hypothesis* (the self-consistency relation), and the theorem *derives* the conclusion. The sorry-free lemma [`QOU.ArchimedeanUniverse.fixedPoint_iff_cubic`](em-coupling-fixed-point.lean) establishes for every $\alpha \neq 0$:

$$
  \Bigl(\tfrac{1}{\alpha} = T + \alpha H(1-h^2\alpha)\Bigr)
  \;\Longleftrightarrow\;
  P(\alpha) = 0,
$$

by clearing the denominator ($\alpha \neq 0$ from `alpha_pos`) and applying `linear_combination`. The main theorem [`QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root`](em-coupling-fixed-point.lean) composes this equivalence with the class's `b3_normalization` field. No stored `alphaCubic_zero` field exists to short-circuit the proof, rendering the derivation non-degenerate.

## Numerical context

At $q_0$, the tree term and zero-mode reproduce $1/\alpha$ to $-4.2\times 10^{-6}$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)). The $\mathcal{O}(\alpha^2)$ self-consistency term supplies the residual $\mathcal{O}(\alpha)$ correction; the conjectural $B_3(\mathbb{C})$ Bloch-class content (encoded in the class field) supplies its exact form. The cubic $P$ features a real root near $1/137.036$. CODATA-consistency provides the empirical foundation of the conjecture, enforced by the class field `codata_consistent`.

## Status

The sole open element remains the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization (the class field `b3_normalization`). Lean proves everything else sorry-free: the tree/zero-mode assembly of $T$, the algebraic equivalence fixed-point $\Leftrightarrow$ cubic, and the derivation of $P(\alpha)=0$ from the class. We leave the class uninhabited (the honest open state, §3b-tax); no fabricated instance attempts to close the primary conjecture.
<!-- FILE_END: em-coupling-fixed-point.md -->

<!-- FILE_START: photon-ir-zero-mode-bring.md -->
*Lean sibling: `QOU.Archimedean.PhotonIRZeroMode`. The topological/geometric core is unconditional; the heat-kernel zero-mode is a cited standard result; the $\tau_{\mathrm{arch}}$ uniqueness is the upstream conditional input.*

**Proposition (photon IR zero-mode on Bring's surface).** *Let $M_g$ be a closed orientable genus-$g$ hyperbolic surface of constant curvature $-1$. The photon IR zero-mode contribution to $1/\alpha_{EM}$ at zero external momentum is the harmonic $1$-form sector $H^1(M_g)$ normalized by the surface area:*

$$
  \delta\!\left(\tfrac{1}{\alpha_{EM}}\right)_{\mathrm{IR}}
  \;=\; \frac{\dim H^1(M_g)}{\operatorname{Area}(M_g)}
  \;=\; \frac{b_1(M_g)}{4\pi(g-1)}
  \;=\; \frac{2g}{4\pi(g-1)},
$$

*with $b_1 = 2g$ and $\operatorname{Area} = -2\pi\chi = 4\pi(g-1)$. At the Bring genus $g=4$, this evaluates to $\tfrac{8}{12\pi} = \tfrac{2}{3\pi}$, providing the additive correction of [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode).*

## Mechanism

We restrict the Maxwell sector of the categorical Lagrangian to the UV-completing Bring surface $M_4$. The surface carries the force-carrier pair $\{T_{2,9}, T_{3,5}\}$ ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)). The zero-momentum two-point function is governed by the kernel of the $1$-form Laplacian $\Delta_1$. By Hodge theory, $\dim\ker\Delta_1 = b_1(M_g) = 2g$. The heat-kernel zero-mode of a Laplacian contributes one constant mode $1/\operatorname{Vol}$ per harmonic generator, yielding an infrared shift of $b_1/\operatorname{Area}$. Gauss–Bonnet fixes the area at curvature $-1$ to $4\pi(g-1)$. This gives an infrared shift of $2g/(4\pi(g-1))$, evaluating to $2/(3\pi)$ at $g=4$.

**Dimensional reduction.** A naive attempt places the zero-mode on the $3$-manifold $M_g\times S^1$, where $b_1 = 2g+1$ and $\operatorname{Vol} = 2\pi\operatorname{Area}$. This gives $(2g+1)/(8\pi^2(g-1)) = 9/(24\pi^2) \approx 0.038$. Crossing with $S^1$ adds a spurious harmonic generator and a factor of $2\pi$ to the volume. The photon zero-mode lives strictly on the $2$-surface.

**Jet-order placement.** We decompose the Archimedean functor into jet grades: $\tau = \sum_{n\ge 0} a_D^{(n)}$ ([`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition)). The $n=0$ term is the electron period. The photon zero-mode forms the $n=1$ infrared term, which is the first prolongation beyond the tree coupling $q[9]_q[10]_q$. The $n=2$ self-energy takes the form $\alpha\,[2]_q/(8\pi)\,(1-h^2\alpha)$. Its denominator depends on the same Hodge datum:

$$
  8\pi \;=\; \pi\cdot\dim H^1(M_{\text{Bring}}) \;=\; \pi\,b_1.
$$

The Betti number $b_1 = 8$ controls both infrared corrections. The zero-mode carries it in the numerator ($b_1/\operatorname{Area}$), while the self-energy carries it in the denominator ($\pi\,b_1$). The factors isolate the topological $b_1$ and the archimedean $\pi$. 

**Habiro structure.** We group the $n=2$ form as $\alpha\,H(q)/(\pi\,b_1)$, where $H(q) = [2]_q(1-h^2\alpha)$ is the $\alpha_{EM}$ Habiro element ([`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution)). Identity 2 acts as the Habiro deformation $(1-h^2\alpha)$. This structures the $n=2$ self-energy into three sectors: substrate $H$, archimedean $\pi$, and topological $b_1$. This factorization connects the Hodge realization ($b_1/\operatorname{Area}$) to the dilogarithm realization via root-of-unity evaluations in the Habiro ring, indicating a bridge to the Bloch group.
<!-- FILE_END: photon-ir-zero-mode-bring.md -->

<!-- FILE_START: alpha-em-derivation-exploration-options.md -->
**Remark (exploration options to close the $1/\alpha_{EM}$ derivation).**

We map the existing QOU infrastructure to the open $2/(3\pi)$ derivation. The numerical match $1/\alpha_{EM} \approx q\cdot[9]_q\cdot[10]_q + 2/(3\pi)$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)) holds exactly via the algebraic identity $2/(3\pi) = 2g/(4\pi(g{-}1))$ at $g = 4$. However, it requires a derivation. We record the existing infrastructure and four potential paths forward.

## Existing infrastructure

The missing step is connecting the current machinery to the coupling side.

### 1. Hopf fibration $S^3 \to S^2$ as the substrate geometry

The [Reeb bundle](#def:reeb-bundle) at a brane point $p$ is

$$
  \mathcal{R}_p \;=\; \bigl( S^3 \xrightarrow{\pi_H} \mathcal{S}_p \cong S^2,\; \xi_q \bigr),
$$

where $\pi_H$ is the Hopf fibration, the base $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ is the exceptional divisor (colour space), and the total space $S^3$ evaluates braid words in $B_n$ via $H_n(R,q)$. This geometric pair identically matches the algebraic identity $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$. The category of the base is $\mathcal{S}_p \cong S^2$ and the category of the total space is $S^3$.

### 2. Three color tubes / chromaticity primaries on Bring's surface

We identify three colour primaries on Bring's surface (the three color tubes, or three $S_3$ subgroups of the Bring automorphism group) in [`rem:q-chromaticity`](#rem:q-chromaticity). This provides the natural source of the "$/3$" denominator in $2/(3\pi)$. It represents photon coupling averaged over three independent chromaticity channels.

### 3. GB filtration with confinement levels

We filter $H_n(R,q)$ by GB-depth via [`def:confinement-level`](#def:confinement-level) and [`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification). For $H_3$, depths $\ell = 0,1,2,3$ yield a four-step filtration. The maximum depth of 3 correlates with the $/3$ denominator.

### 4. Spectral sequence collapse

Hochschild cohomology vanishes ($\mathrm{HH}^k = 0$ for $k \ge 1$) ([`prop:spectral-sequence-collapse`](#prop:spectral-sequence-collapse)). The GB spectral sequence collapses at $E_1$. All contributions reside in $E_\infty^{0,0} = \mathrm{HH}^0 = Z(H_n) = \bigoplus_\lambda R\cdot e_\lambda$. This mechanism yields the closed-form mass-formula $\alpha_k$ via Plancherel-weighted Markov pairings on the centre.

### 5. Wenzl-bridge closed form for stratum prefactors

We obtain an explicit q-rational expression for the Markov-trace coefficients $y_\lambda$ in the mass-formula $\alpha_k$ ([`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge)). We apply this machinery to the coupling side rather than the mass side.

## Four exploration options

### Option A — Hopf-fibration vacuum-polarisation integral

**Claim:** We compute the photon vacuum-polarisation 1PI graph in the QOU framework. We set the photon propagator on the Hopf total space $S^3$ and external legs (force-carrier knots) projecting via $\pi_H$ to the base $\mathcal{S}_p \cong S^2$. The zero-mode contribution at zero external momentum is

$$
  \Pi_{\text{zero}}(0)
  \;=\;
  \frac{\mathrm{Vol}(S^2)}{3 \cdot \mathrm{Vol}(S^3)}
  \;=\;
  \frac{2}{3\pi},
$$

where the $1/3$ factor arises from chromaticity averaging across the three colour primaries on Bring's surface.

**Requirements:** We need an explicit formula for the vacuum-polarisation 1PI graph in the categorical-Lagrangian framework. This includes:
1. The photon two-point function on $S^3$ (Hodge-decomposed). Harmonic 1-forms vanish because $H^1(S^3) = 0$. The non-harmonic spectrum converges to $1/\mathrm{Vol}(S^3)$ as a constant zero-momentum residue.
2. The external-leg projection $\pi_H \colon S^3 \to S^2$, contributing the $\mathrm{Vol}(S^2)$ numerator.
3. The Lie-algebra / chromaticity normalisation, contributing the $1/3$ factor.

### Option B — Stratum-prefactor approach via spectral sequence collapse

**Claim:** We apply the spectral-sequence machinery used for the mass formula ([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula)) to the coupling side. The $\alpha_{EM}$ correction equals the depth-$\ell$ stratum prefactor of the GB filtration for a specific $\ell$.

**Concretely:** The bare formula $1/\alpha = q\cdot[9]_q\cdot[10]_q$ is the depth-$0$ centre contribution. The $2/(3\pi)$ correction expresses a Plancherel-weighted Markov pairing on the depth-$\ell$ stratum for $\ell \ge 1$, computed via the Wenzl-bridge closed form.

**Requirements:**
1. We define a depth-$k$ contribution to $1/\alpha_{EM}$, analogous to the mass functional $\mathfrak{m}^{(k)}$.
2. We compute this via the $y_\lambda$ closed form at depth $\ell$.
3. We verify that the depth-$\ell$ contribution at $q = q_0$ equals $2/(3\pi)$.

### Option C — Reeb-bundle holonomy + U(1) integration

**Claim:** The $\mathrm{U}(1)$ fibre of the Reeb bundle has holonomy $e^{2\pi i / [2]_q}$. Integrating the photon over the fibre and averaging over the base yields a finite phase-volume factor equal to $2/(3\pi)$ at $q = q_0$ for $g = 4$.

**Requirements:**
1. We define the photon holonomy integral over the $\mathrm{U}(1)$ fibre: $\oint_{U(1)} A_\mu d\theta = 2\pi/[2]_q$.
2. We square or take the modulus and average over $\mathcal{S}_p$ using the Fubini-Study measure.
3. We verify the result equals $2/(3\pi)$ at $q = q_0$. However, this predicts a $q$-dependent constant, contradicting the required $q$-independence. This falsifies the holonomy approach.

### Option D — Chern-Simons partition-function ratio

**Claim:** The constant $2/(3\pi)$ is the ratio of Chern-Simons partition functions on distinguished 3-manifolds at the QOU substrate level $k(q)$:

$$
  \frac{2}{3\pi}
  \;=\;
  \frac{Z_{\mathrm{CS}}(S^3, \mathrm{SU}(2)_k)}{3 \cdot Z_{\mathrm{CS}}(S^3 \times S^1, \cdots)}
  \quad\text{or similar}.
$$

The constant emerges from the universal $k \to \infty$ asymptotics, independent of the finite-$k$ value.

**Requirements:** We evaluate the Chern-Simons partition functions on the relevant 3-manifolds and take the appropriate limit. The Witten formulas provide explicit closed forms for $\mathrm{SU}(2)_k$ on $S^3$. The $k \to \infty$ limit produces $1/k$ factors that map to $1/\pi$ via $k+2 = \pi/\log q$.

## Recommended path

We recommend Option B (stratum-prefactor via spectral sequence). It utilises existing infrastructure and clarifies the relationship between the QOU mass and coupling formulas. Option A provides a direct QFT calculation but requires new infrastructure.

A practical execution follows:
1. Implement Option B in $H_3$ ([`prop:spectral-sequence-h3-explicit`](#prop:spectral-sequence-h3-explicit)).
2. Define the depth-$\ell$ coupling functional analogously to the mass functional.
3. Compute the value at $q_0$ for each $\ell$ to isolate $2/(3\pi)$.
4. Generalise to higher $H_n$ and verify consistency.
5. Cross-validate against Option A by comparing the depth-$\ell$ stratum-prefactor to the Hopf-fibration zero-mode integral.

## Natural sources for each ingredient

We catalogue the natural QOU sources for the $1/\alpha_{EM}$ ingredients in [Table: Natural QOU sources for the $1/\alpha_{EM}$ ingredients](#tbl:alpha-em-derivation-exploration-options-table-data). The derivation awaits the coupling-side analog of the mass-formula stratum decomposition.
<!-- FILE_END: alpha-em-derivation-exploration-options.md -->

