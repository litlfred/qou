# The Hecke pairing engine `(σ⁻¹)^Z = c_Z σ + d_Z` is a theorem

**Date:** 2026-06-07
**Consumers:** [`conj:palindromicity-orbital-type`](../../content/quantum-observable-universe/molecular-construction/palindromicity-orbital-type.md),
[`conj:shell-closure-nf-term-count`](../../content/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.md),
and the pairing term of
[`conj:q-integer-mass-formula`](../../content/quantum-observable-universe/mass-theory/q-integer-mass-formula.md).

## Statement

Let $H_2(q)$ be the Iwahori–Hecke algebra on one generator $\sigma$ with
the QOU convention
$$
\sigma^2 = h\,\sigma + 1,\qquad h := q - q^{-1},
$$
equivalently $(\sigma - q)(\sigma + q^{-1}) = 0$, so $\sigma$ has
eigenvalues $q$ and $-q^{-1}$. The $Z$-fold nuclear–electron crossing
$(\sigma^{-1})^Z$ reduces, in the $2$-dimensional algebra $H_2(q)$ with
basis $\{1,\sigma\}$, to the linear form
$$
\boxed{\;(\sigma^{-1})^Z \;=\; c_Z\,\sigma + d_Z\;},\qquad
c_Z = \frac{q^{-Z} - (-1)^Z q^{Z}}{[2]_q},\quad
d_Z = \frac{q^{-(Z+1)} + (-1)^Z q^{Z+1}}{[2]_q},
$$
where $[2]_q = q + q^{-1}$.

**Corollary (sign alternation — the "pairing" mechanism).** At any real
substrate $q>1$:
$$
c_Z < 0 \ \text{for even } Z,\qquad c_Z > 0 \ \text{for odd } Z,
$$
and $|c_Z|$ is strictly increasing in $Z$ with $|c_Z| = \dfrac{q^{Z} -
(-1)^Z q^{-Z}}{[2]_q} \sim q^{Z}/[2]_q$. The even-$Z$ negative
$\sigma$-coefficient is the algebraic origin of pairing suppression; the
odd-$Z$ positive coefficient is the algebraic origin of term expansion.

## Proof

$H_2(q)$ is $2$-dimensional over the base field with basis $\{1,\sigma\}$
(any higher power of $\sigma$ reduces via $\sigma^2 = h\sigma+1$). Since
$(\sigma-q)(\sigma+q^{-1})=0$ with $q \neq -q^{-1}$, $\sigma$ is
diagonalisable with the two distinct eigenvalues $q$ and $-q^{-1}$; hence
$\sigma^{-1}$ has eigenvalues $q^{-1}$ and $-q$, and $(\sigma^{-1})^Z$ has
eigenvalues $q^{-Z}$ and $(-q)^{Z} = (-1)^Z q^{Z}$.

Write $(\sigma^{-1})^Z = c_Z\sigma + d_Z$ (possible because the algebra is
spanned by $\{1,\sigma\}$). Evaluating both sides on the two eigenvectors
of $\sigma$ — on which $\sigma$ acts as $q$ and as $-q^{-1}$ respectively
— gives the linear system
$$
\begin{cases}
c_Z\, q + d_Z = q^{-Z},\\[2pt]
c_Z(-q^{-1}) + d_Z = (-1)^Z q^{Z}.
\end{cases}
$$
Subtracting the second equation from the first eliminates $d_Z$:
$$
c_Z\,(q + q^{-1}) = q^{-Z} - (-1)^Z q^{Z}
\;\Longrightarrow\;
c_Z = \frac{q^{-Z} - (-1)^Z q^{Z}}{[2]_q}.
$$
Back-substituting $d_Z = q^{-Z} - c_Z q$ and simplifying over $[2]_q$,
$$
d_Z = \frac{q^{-Z}(q + q^{-1}) - q\,(q^{-Z} - (-1)^Z q^{Z})}{[2]_q}
    = \frac{q^{-(Z+1)} + (-1)^Z q^{Z+1}}{[2]_q}.
$$
$\blacksquare$

**Sign alternation.** For $q>1$ and even $Z$, $q^{-Z} - q^{Z} < 0$ and
$[2]_q>0$, so $c_Z<0$; for odd $Z$, $q^{-Z} + q^{Z} > 0$, so $c_Z>0$.
Monotonicity of $|c_Z|$ follows from $|c_Z| = (q^{Z} - (-1)^Z q^{-Z})/[2]_q$
and $q>1$.

**Boundary checks.** $Z=0$: $c_0 = 0$, $d_0 = [2]_q/[2]_q = 1$, so
$(\sigma^{-1})^0 = 1$. $Z=1$: $c_1 = (q^{-1}+q)/[2]_q = 1$,
$d_1 = (q^{-2}-q^{2})/[2]_q = -(q-q^{-1}) = -h$, so $\sigma^{-1} = \sigma - h$,
which is exactly the inverse relation read off from $\sigma^2 = h\sigma+1$.

## Numerical witness

[`computations/chebyshev_pairing_engine_witness.py`](../../computations/chebyshev_pairing_engine_witness.py)
builds the regular representation $M_\sigma = \begin{psmallmatrix}0&1\\1&h\end{psmallmatrix}$
of $\sigma$ on $\{1,\sigma\}$, forms $M_\sigma^{-1}$, raises it to each
$Z=0,\dots,12$ at the substrate $q_0$, and verifies $M_\sigma^{-Z} =
c_Z M_\sigma + d_Z I$ against the closed forms above to $10^{-40}$,
together with the sign-alternation corollary. Witness JSON:
[`chebyshev-pairing-engine.witness.json`](../../computations/chebyshev-pairing-engine.witness.json).

## What this does and does not close

**Proved (this note):** the algebraic *engine* — the exact reduction
$(\sigma^{-1})^Z = c_Z\sigma + d_Z$ with the closed forms and the
sign-alternation $c_Z\lessgtr 0$. This was previously stated as a
computed mechanism in the consumer blocks but not proved as a standalone
result.

**Still conjectural (unchanged):** the *interpretations* that rest on the
engine —
- `conj:palindromicity-orbital-type`: that the resulting GS normal-form
  word-length histogram is palindromic $\iff$ all occupied sub-shells are
  $s$-orbitals, with defect $=2\ell$;
- `conj:shell-closure-nf-term-count`: that the term-count growth ratio
  $\gamma(Z)$ separates into the three regimes $\{1\}$ / $[1.2,1.4]$ /
  $[3.0,4.0]$ with the structural gap $(1.4,3.0)$.

These remain open because they concern how the proved sign-alternation
propagates through the *full* GS reduction of the quotient-atom braid in
$H_{Z+1}(q)$ (a combinatorial normal-form statement), not the
two-strand reduction proved here. The blocks stay `kind: "conjecture"`;
this note supplies their now-rigorous algebraic foundation and isolates
the open content to the normal-form combinatorics.
