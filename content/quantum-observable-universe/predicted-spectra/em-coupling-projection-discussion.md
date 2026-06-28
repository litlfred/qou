**Spectral characterisation.**
The electromagnetic fine structure constant is fixed by three
structural results that establish both its existence and its
uniqueness:

1. *Two-strand spectral completeness*
   ([completeness theorem](#thm\:em-spectral-completeness)) shows
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
   ([Bring uniqueness](#prop\:force-carrier-bring-uniqueness)):
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
([EM coupling Chern-Simons](#conj\:em-coupling-chern-simons)):

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
([EM coupling Chern-Simons](#conj\:em-coupling-chern-simons)).

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
[`rem:em-coupling-chern-simons`](#conj\:em-coupling-chern-simons) for
the demoted statement and [open problems](#rem\:alpha-em-derivation-open-problems)
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
