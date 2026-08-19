We present this survey to justify our central move: we may take the substrate parameter $q \in \mathbf{No}$ in the infinitesimal neighbourhood of $1$, without disturbing any algebraic machinery of this paper. The bulk of the formal structure is **purely algebraic**. It depends only on the ground ring being a field (typically of characteristic zero), independent of any analytic or topological property of $\mathbb{R}$ or $\mathbb{C}$.

## Blocks that lift verbatim

The following constructions are formulated over
$\mathbb{Z}[q, q^{-1}]$, $\mathbb{Q}(q)$, or an arbitrary
characteristic-zero field, and therefore lift unchanged to any
real-closed extension $K \supseteq \mathbb{R}$, in particular to
$\mathbf{No}$:

1. **Hecke algebra $H_n(q)$.** The presentation
   $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ plus the braid relations
   $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ makes sense over any
   commutative ring in which $q$ is invertible. The Wedderburn
   decomposition $H_n(q) \cong \bigoplus_{\lambda \vdash n}
   M_{d_\lambda}(K)$ holds at generic $q$ over any algebraically
   closed field of characteristic zero.

2. **Hoefsmit seminormal form**
   ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).
   The matrix entries of $\rho_\lambda(\sigma_i)$ are rational
   functions in $q$ with coefficients in $\mathbb{Z}$. The
   eigenvalues $q$ (symmetric channel) and $-q^{-1}$
   (antisymmetric channel) are field-polymorphic.

3. **Markov trace and Jones polynomial.** The unique trace
   $\mathrm{tr}_M : H_\infty(q) \to K[q, q^{-1}]$ satisfying the
   Markov property yields the Jones polynomial $J_K(q)$ as an
   element of $\mathbb{Z}[q, q^{-1}]$; nothing needs $\mathbb{R}$.

4. **$q$-Schur--Weyl duality.** The decomposition of $V^{\otimes n}$
   into irreducible $H_n(q)$-modules indexed by partitions
   $\lambda \vdash n$ with at most two parts is purely
   representation-theoretic.

5. **$q$-deformed identities.**
   $c_q = 1/(q - 1)$, $\hbar_q = (q-1)/q$, $[n]_q =
   (q^n - q^{-n})/(q - q^{-1})$, $[n]_q! = \prod_{k=1}^n [k]_q$,
   and the quantum dimension $\dim_q(\lambda)$ are all rational
   in $q$ and lift unchanged to any field.

6. **Rigid :refterm[monoidal category]{#monoidal-category} axioms**
   ([rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category)).
   The axioms of a strict rigid :refterm[monoidal category]{#monoidal-category} (associator,
   unitors, left/right duals, evaluation/coevaluation) are
   categorical identities, not analytic conditions.

7. **Hopf algebra structure on $\mathcal{H}_q$**. Comultiplication,
   antipode, coassociativity, and the grouplike elements
   $\exp_q, \log_q, \mathrm{Li}_2^q$ are all formal-power-series
   manipulations over any field.

8. **Frobenius algebra structure** on $A$ as a bare algebraic
   structure (the non-degeneracy of $\int_A$ as a pairing $A
   \otimes A \to K$). This is a bilinear form condition and
   requires only a field.

9. **Braid group action**: $B_n$ acts on $V^{\otimes n}$ via the
   Hecke $R$-matrix; the action is functorial in the ground ring.

10. **Character formulas**: the Hoefsmit-Murphy formula for
    $\chi_\lambda(\sigma_w)$ in terms of contents of the Young
    diagram is a rational-function identity.

11. **Elliptic curve $\mathcal{E}_q$ as an algebraic variety.**
    The Descartes Weierstrass equation defines a smooth
    projective curve over $K[q, q^{-1}]$ (away from the
    discriminant locus). Its group law is algebraic.

12. **Tannaka--Krein reconstruction** of $\mathrm{SU}_q(2)$ from
    $(\mathbf{C}, A, \tau)$: the reconstruction procedure
    produces a Hopf algebra from a fibre functor to $K$-modules;
    the ground field plays no essential role beyond being a
    field.

13. **Rigid dualizing complex** $\omega_A^\bullet$: the Van den
    Bergh duality isomorphism
    $\omega_A^\bullet \simeq R\mathrm{Hom}_{A^e}(A, A^e)$ is a
    statement in derived algebra, unchanged over surreals.

14. **Fibre functor rigidity** (deformation-theoretic): vanishing
    of $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$ is a
    cohomological condition independent of topology.

## Note: Frobenius is a structural sieve, not a measure

Item 8 above can be mis-read. The Frobenius pairing
$\int_A : A \otimes A \to K$ on the QOU observable algebra is an
*algebraic* bilinear form: a non-degenerate $K$-linear map
witnessing the self-duality $A \cong A^\vee$ as objects of the
rigid braided monoidal category. It is **not** a Lebesgue-style
measure-theoretic integral, and it is **not** a surrogate for
one. The Costin–Ehrlich–Friedman theorem
[@costin-ehrlich-friedman2015] rules out any translation-
invariant measure on the full ring $C(\mathbf{No})$, so no
axiomatic stipulation could install one without contradicting a
proved theorem.

What the Frobenius axiom does instead is *select* a sub-algebra
of admissible observables. An object $A$ in the monoidal
category may only carry a Frobenius structure if it is rigid and
self-dual; this is a strong constraint that excludes most of
the wild functions in $C(\mathbf{No})$ (e.g.\ continuous
surreal-valued functions with non-well-ordered support, or
indicator functions of order-disconnected pieces of $\mathbf{No}$).
The QOU observable algebra is built bottom-up from
representation-theoretic data ($H_n(q)$ modules, Wedderburn
blocks, braid-word characters) — none of which can produce such
pathological elements. This dissolves the apparent paradox "QOU
has a Frobenius pairing on its observable algebra $A$, therefore
QOU has a Lebesgue integral on $C(\mathbf{No})$": the algebra $A$
is *not* $C(\mathbf{No})$, but the representation-theoretic
sub-algebra generated by Hecke matrices and Markov-trace
functionals, all of which live on the CEF-positive side of the
integration partition (analytic / transseriable functions of
$q$, evaluated at $q = q_0 \in \mathbf{No}$). The Frobenius
pairing exists on it not because we postulated one on
$C(\mathbf{No})$, but because the sub-algebra is small enough and
algebraic enough to admit one.

## Consequence for the appendix

The core mass formula — Hoefsmit seminormal form $\to$ Markov
trace $\to$ Jones polynomial at the substrate value — runs
identically over $\mathbf{No}$. The categorical mass
$\mathfrak{m}(K)$, transfer matrix $T(c,d)$, and $q$-value
predictions are all *field-polymorphic* and have well-defined
interpretations wherever we choose $q \in \mathbf{No}$.

The break from $\mathbb{R}$ to $\mathbf{No}$ only becomes
non-trivial at the last step: when a categorical quantity is
compared to a *measured* real number, a standard-part must be
taken ([classical limit as standard-part](#conj:classical-limit-stpart)).
