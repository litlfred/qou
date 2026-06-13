Liouville's theorem and Roth's theorem bound the approximability
of an algebraic irrational by rationals: if $\alpha$ is algebraic of
degree $d$, then $|\alpha - p/q| > c/q^d$ for sufficiently large
$q$ (Liouville), and Roth improves the exponent to $2 + \delta$ for
any $\delta > 0$.  We use $\delta$ rather than $\varepsilon$ here
to avoid collision with the surreal infinitesimal $\varepsilon =
1/\omega$ used elsewhere in this appendix.

These are analytic statements about approximation rates. The
surreal framework suggests a **direct algebraic shadow**: algebraic
and transcendental numbers should be distinguished by the
*birthday trajectory* of their sign sequences
([birthday grading](#def:birthday-grading)).

## Setup

Every real number $\alpha \in \mathbb{R} \subset \mathbf{No}$ has a
canonical sign sequence $s_\alpha : \alpha_{\mathrm{birth}} \to
\{+, -\}$ with $\alpha_{\mathrm{birth}} = b(\alpha)$. For reals,
$b(\alpha) \leq \omega$ (since $\mathbb{R}$ embeds in the
birthday-$\leq\omega$ subfield of $\mathbf{No}$).

Define the **birthday trajectory** of $\alpha$ as the function

$$
  b_\alpha : \mathbb{N} \to \mathbb{N},
  \qquad b_\alpha(n) := \text{minimum birthday of}~p/q~\text{with}~q \leq n,~|\alpha - p/q|~\text{minimal}.
$$

This is the birthday analogue of the classical continued-fraction
convergent sequence.

## Conjecture

The birthday trajectory discriminates algebraic from transcendental:

1. **Algebraic rigidity**: if $\alpha$ is algebraic of degree
   $d$, then $b_\alpha(n) = O(\log n)$ up to a bounded error.
   The trajectory grows *logarithmically* because rational
   approximations must be explicitly constructed via integer
   linear algebra (Liouville-type).

2. **Transcendental depth**: if $\alpha$ is transcendental (of
   "generic" type, e.g. Liouville number), $b_\alpha(n)$ grows
   *super-logarithmically*, potentially approaching $\omega$ for
   Liouville-class numbers.

3. **Roth threshold**: Roth's exponent $2 + \delta$ corresponds
   to the ordinal stratum at which any single $\delta > 0$
   allows non-trivial birthday-trajectory growth for algebraic
   numbers — finite, bounded birthday depth.

4. **Continued fraction correspondence**: the $k$-th convergent of
   the continued-fraction expansion of $\alpha$ has birthday
   exactly $\sum_{j \leq k} b(a_j)$ where $a_j$ are the partial
   quotients. For algebraic $\alpha$, $\{a_j\}$ is bounded (by
   Lagrange for quadratic irrationals, conjecturally for all
   algebraic); for transcendental $\alpha$, $a_j$ may grow
   unboundedly.

## Why this is natural

Surreal construction is *exactly* the continued-fraction-like
recursive construction of reals:
- Finite sign sequences = dyadic rationals.
- Infinite sign sequences = limit reals.
- The *rate* at which birthday-depth accumulates per unit of
  approximation error is a direct measure of how "hard to
  approximate" a real number is.

Classical diophantine approximation theory measures this rate
analytically (via $|\alpha - p/q|$). The surreal framework
measures it algebraically (via birthday trajectory).

The alignment is not coincidental — both are studying the same
object: **how efficiently rationals approach a real**.

## Consequences if true

1. **New proof strategy for Roth's theorem**: Roth's theorem
   becomes a statement about the birthday-growth rate of
   algebraic sign sequences. A purely algebraic proof (avoiding
   the Thue-Siegel method) might be accessible.

2. **Liouville-number detection**: a number is Liouville if its
   birthday trajectory approaches $\omega$; this is an
   algebraic characterisation, independent of the choice of
   approximation exponent.

3. **Classification of transcendence types**: Mahler's $S, T, U$
   classification corresponds to *different ordinal strata* of
   birthday trajectories. Elements of $U$ (Liouville-type) live
   at birthday approaching $\omega$; elements of $S$ (generic
   transcendentals) at stabilising finite birthdays.

4. **QOU substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps)**: the
   conjectured value (not known to be algebraic or
   transcendental) has a specific birthday trajectory. If
   computable, this would *decide* its algebraic status.

## Specialisation to QOU

The QOU substrate parameter $q_0$ satisfies a recursive equation
from the paper's categorical structure (via fibre-functor
rigidity, Tannaka-Krein, etc.). The conjecture predicts:

- if $q_0$ is algebraic, its birthday *trajectory* $b_{q_0}(n)$
  is logarithmic (bounded continued-fraction partial quotients, per
  Lagrange/Roth);
- if transcendental, the trajectory grows super-logarithmically
  (approaching Liouville-class behaviour for certain exponentials);
- *which* trajectory class $q_0$ lives in encodes the paper's
  "algebraic complexity".

**Note.** Every real number has birthday exactly $\omega$ (the
dyadic rationals have finite birthday; every other real has
birthday $\omega$ since it is the limit of a length-$\omega$ sign
sequence).  The algebraic/transcendental distinction therefore
cannot be read off the birthday of $q_0$ itself, only off the
growth rate of its rational-approximation trajectory.

Computing $q_0$'s actual birthday trajectory would:
- decide its algebraic status (open in the main paper);
- give a birthday-based characterisation of the QOU substrate.

## Proof strategy

**Reduction to continued fractions (provable now, modulo the
algebraicity conjecture)**:

1. The birthday of a dyadic rational $p/2^k$ is $k + b(p) \leq k +
   \log_2 |p|$.

2. For an irrational real $\alpha$, the birthday trajectory is
   related to the continued-fraction expansion via:
   $b(\alpha^{(k)}) = \sum_{j \leq k} b(a_j)$ where $\alpha^{(k)}$
   is the $k$-th convergent.

3. For **quadratic irrationals** (Lagrange), $\{a_j\}$ is eventually
   periodic, so $b(\alpha^{(k)}) = O(k)$ and the birthday
   trajectory is linear in $k$, while the approximation quality is
   $O(1/q^2)$, giving $b_\alpha(n) = O(\log n)$.

4. For **higher algebraic degree**: use Roth's theorem to get
   $|\alpha - p/q| > c/q^{2+\delta}$, which bounds the
   continued-fraction partial quotients by a power of $k$, giving
   $b_\alpha(n) = O((\log n)^{1 + \delta'})$ — still poly-log.

5. For **Liouville numbers**: $|\alpha - p/q| < 1/q^n$ for every
   $n$; this corresponds to unboundedly-growing partial quotients,
   giving $b_\alpha(n)$ super-polynomial.

**Required infrastructure**:
- Continued-fraction expansion in Lean (exists in mathlib).
- Birthday function of rationals (straightforward).
- Roth's theorem in Lean (does **not** exist; would be substantial).

**Falsification path**: find an algebraic number whose birthday
trajectory grows super-logarithmically. This would either:
- refute the conjecture, or
- refute Roth's theorem (unlikely).

Conversely, find a transcendental number with logarithmic birthday
trajectory and bounded continued-fraction quotients — this would
refute conjecture (2).

**Provability assessment**: structurally clean once continued-
fraction $\leftrightarrow$ birthday bijection is formalised. The deep content
(distinguishing algebraic from transcendental) depends on Roth's
theorem, which is deep but classical.

## Discussion

**Open**, but the reduction to continued fractions is
classical. The conjecture restates Roth / Liouville in
surreal-combinatorial language.

The specific application to $q_0$ in QOU is the novel part — if
$q_0$ has a computable closed-form birthday, the conjecture
gives an algebraic-complexity characterisation of the substrate
parameter.
