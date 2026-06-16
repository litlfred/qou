**Definition.**
*The **$q$-Pochhammer partial product** at depth $n \in \mathbb{N}$,
substrate parameter $q$, and state variable $x$, is the finite
rational function*

$$
  \Phi_n(x; q)
  \;:=\;
  \prod_{k=0}^{n-1} \frac{1}{1 - x q^k}
  \;=\;
  \frac{1}{(x; q)_n},
  \qquad
  (x; q)_n
  \;:=\;
  \prod_{k=0}^{n-1}\bigl(1 - x q^k\bigr).
$$

*The numerator is the constant $1$; the **denominator polynomial**
$(x; q)_n \in \mathbb{Z}[q, x]$ has $n$ simple roots $x = q^{-k}$ for
$k = 0, \dots, n-1$. As a finite rational function, $\Phi_n(x; q)$ is
well-defined for any $q \neq 0$ — including the QOU substrate
$q_0 \approx 1.11$, where the roots $\{q_0^{-k}\}_{k=0}^{n-1} =
\{1, 0.901, 0.812, \dots\}$ lie in $(0, 1]$. The partial product is
the depth-$n$ truncation of the analytic quantum dilogarithm
([quantum dilogarithm](#cor:quantum-dilogarithm))*

$$
  \Phi_q(x)
  \;=\;
  \prod_{k=0}^{\infty}\frac{1}{1 - x q^k}
  \;=\;
  \lim_{n \to \infty} \Phi_n(x; q),
  \qquad |q| < 1.
$$

*The infinite product converges only for $|q| < 1$, but the QOU
substrate has $q_0 > 1$. The partial product $\Phi_n$ is what
appears in the QOU mass formulas: a finite rational function whose
denominator zeros are the algebraic addresses of cusps regardless of
the convergence radius of the analytic limit. The Faddeev limit to
$\mathrm{Li}_2$
([Archimedean limit](#conj:dilogarithm-archimedean-limit))
takes $q \to 1$ from either side — $q \to 1^-$ in the convergence
domain, or $q \to 1^+$ via analytic continuation in the QOU
substrate regime.*

*so $\Phi_n$ is the same object as $\Phi_q^{[\leq n]}$ in
([Φ$_q$ partition-depth stratification](#prop:quantum-dilogarithm-stratified)),
with the truncation index $n$ identified with the GB-depth
$k_\star(T_w)$.*

*The stratification proposition writes the analytic product as
$\prod_{k \geq 1}(1 - q^{-k} z_i)^{-1}$ — the standard form indexed
from $k = 1$ with negative-power factors. The present block uses the
equivalent indexing-from-$k=0$ form $(1 - x q^k)$: under the
substitution $z_i = q \cdot x$ and shifting $k \mapsto k - 1$, the
two forms agree factor-for-factor. Both denote the same algebraic
object. The form here exposes the denominator polynomial
$(x; q)_n \in \mathbb{Z}[q, x]$ with non-negative powers of $q$, so
that at the QOU substrate $q_0 > 1$ the denominator zeros $q_0^{-k}$
land in $(0, 1]$ — the cusp-shape range used by the Newton-Raphson
seeding pipeline.*

## Why a partial product

The categorical Markov trace of a transient crossing word $T_w$ at
GB-depth $k_\star(T_w) = n$ pairs to zero with every centre stratum
$Z^{(k)}(A)$ of depth $k > n$
([truncation = projection onto NF-support depth](#prop:quantum-dilogarithm-stratified)).
Consequently the analytic infinite product $\Phi_q(x)$ collapses
under Frobenius pairing to its depth-$n$ truncation $\Phi_n(x; q)$
— a finite rational function with explicit denominator.

The denominator polynomial $(x; q)_n$ carries the entire pole
structure of the categorical trace at depth $n$. Each factor
$(1 - x q^k)$ is a single pole at $x = q^{-k}$; the corresponding
residue is the depth-$k$ Frobenius coefficient
$\phi_q^{(k)}(z_i)$ of the stratification proposition.

## Recursive structure

The partial product satisfies the one-step recurrence

$$
  \Phi_{n+1}(x; q)
  \;=\;
  \frac{1}{1 - x q^n} \cdot \Phi_n(x; q),
  \qquad
  \Phi_0(x; q) \;=\; 1,
$$

which is the recurrence Lean uses to define $\mathtt{qPochhammer}$
([Lean implementation](./q-pochhammer-partial-product.lean)).
The recurrence is the algebraic shadow of the inductive
**filtration step** $N_{\leq k+1} = \mathrm{NF}(N_{\leq k} \cdot
C(N_k, N_{k+1}) \cdot N_{k+1})$ that drives jet-stratified
reduction: adding one nucleon to the active filtration shell
multiplies the partial product by exactly one new pole factor.

## Interpretation of the denominator zeros

Each zero $x = q^{-k}$ of $(x; q)_n$ is a **pole of the categorical
state sum**. Under the archimedean realization $\tau_{\mathrm{arch}}$
([archimedean realization functor](#def:archimedean-realization-functor)),
these poles mark the **cuspidal boundary** of the corresponding
ideal-tetrahedron piece — the algebraic address of a geometric cusp
that bounds an active JSJ piece
([Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)). The
detailed correspondence is the content of
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)),
and the asymptotic $\Phi_n \to \mathrm{Li}_2$ as $n \to \infty$ is
the content of
([dilogarithm Archimedean limit](#conj:dilogarithm-archimedean-limit)).

## Numerical extraction (for the solver pipeline)

Given a Hecke normal-form word $T_w$ of GB-depth $n$ and a fixed
substrate $q = q_0$, the algebraic engine computes $\Phi_n(x; q_0)$
as a rational function in $x$ with explicit denominator
$(x; q_0)_n$. Its zeros $\{q_0^{-k} : k = 0, \dots, n-1\}$ are
passed across the WASM boundary to the SnapPy kernel as the
**initial seed values** for the Newton–Raphson solver of the
Thurston gluing equations
([cusp-holonomy seeding](#conj:shared-denominator-cusp-holonomy)).
The witness
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
records the seed extraction for a sample nucleon word.
