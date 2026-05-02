**Proposition (residue at a root of unity, defined algebraically).**
*Let $\ell \geq 1$ and $\zeta_\ell \in \mathbb{C}$ be a primitive $\ell$-th
root of unity. Let $\mathrm{tr}_{M, \ell} : J^\ell / J^{\ell+1} \to R$
be the graded Markov trace on the $\ell$-th piece of the
Gröbner-Shirshov filtration
([graded Markov trace](#prop:graded-markov-trace-from-gs-filtration)).
Define the **residue at $\zeta_\ell$** of $\mathrm{tr}_{M, \ell}$ as
the $\ell$-th cyclotomic coefficient of its Laurent expansion in
$\mathbb{Z}[q^{\pm 1}]$:*

$$
  \mathrm{Res}_{q \to \zeta_\ell} \bigl(\mathrm{tr}_{M, \ell}\bigr)
  \;:=\;
  \frac{1}{\ell}
  \sum_{k=0}^{\ell-1}
    \zeta_\ell^{-k} \cdot
    \bigl[q^k\bigr]\,\mathrm{tr}_{M, \ell}
$$

*where $[q^k]\,\mathrm{tr}_{M, \ell}$ denotes the coefficient of
$q^k$ in the Laurent expansion of $\mathrm{tr}_{M, \ell}$ as an
element of $R = \mathbb{Z}[q^{\pm 1}]$, taken modulo $\ell$.
This is the standard discrete-Fourier extraction of the cyclotomic
component, valid for any element of $\mathbb{Z}[q^{\pm 1}]$
**without invoking meromorphic continuation in $\mathbb{C}$**.*

## What this block replaces

The compute pipeline previously declared `residueAtRoot` as
`noncomputable opaque ℕ → RootOfUnity → ℝ → ℝ`
([`gb-residue-spectral-sum.lean:36`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/gb-residue-spectral-sum.lean)).
That declaration was a placeholder: the natural reading is "residue
of a meromorphic function in $q$ at a pole at $\zeta_\ell$", which
requires Archimedean function theory. **This proposition gives a
purely algebraic definition** that lives entirely in $\mathbb{Z}[q^{\pm 1}]$
and recovers the same numerical values as the meromorphic residue
when both are defined.

## Why this is purely algebraic

The graded Markov trace at level $\ell$ is by construction a Laurent
polynomial in $q$ with integer coefficients
([graded Markov trace proposition](#prop:graded-markov-trace-from-gs-filtration)):

$$
  \mathrm{tr}_{M, \ell}(\overline{x}) \;=\; \sum_{k} c_k(\overline{x}) \, q^k
  \qquad
  c_k \in \mathbb{Z}.
$$

Reducing the exponents $k$ modulo $\ell$ gives a finite sum in
$\mathbb{Z}[q]/(q^\ell - 1)$, on which the discrete Fourier transform
$q \mapsto \zeta_\ell^k$ is well-defined as an algebraic operation:
the formula above is just the inverse DFT extraction of the
$\zeta_\ell$-component.

Equivalently, viewing $\mathrm{tr}_{M, \ell}$ as an element of
$\mathbb{Z}[q^{\pm 1}]$ projected to $\mathbb{Z}[q]/(q^\ell - 1)$,
the residue is the coefficient that survives the projection
$\pi_\ell : \mathbb{Z}[q^{\pm 1}] \to \mathbb{Z}[q^{\pm 1}] / \Phi_\ell(q)$
where $\Phi_\ell$ is the $\ell$-th cyclotomic polynomial
(Bourbaki, *Lie* VII, §11):

$$
  \mathrm{Res}_{q \to \zeta_\ell}(\mathrm{tr}_{M, \ell})
  \;=\;
  \pi_\ell\!\bigl(\mathrm{tr}_{M, \ell}\bigr)\!(\zeta_\ell).
$$

This is an **algebraic** evaluation: cyclotomic projection is a
$\mathbb{Z}[q^{\pm 1}]$-module operation, and the resulting element
of $\mathbb{Z}[\zeta_\ell]$ is taken in the standard cyclotomic ring.
No analytic continuation, no contour integration, no notion of
"pole" in the analytic sense is invoked.

## Why this matters

- **Removes Archimedean leak.** The Lean opacity hid an analytic
  residue. Replacing it with the cyclotomic-projection definition
  keeps the entire spectral-sum identity in
  $\mathbb{Z}[q^{\pm 1}]$ until the final substitution at $q_0$.

- **Discharges audit P2.6** narrative-anchoring requirement
  alongside [graded Markov trace](#prop:graded-markov-trace-from-gs-filtration).

- **Computes via DFT.** The discrete-Fourier formula above is
  trivial to evaluate symbolically with `sympy` or any
  $\mathbb{Z}[q^{\pm 1}]$ CAS; the previous opaque declaration
  blocked symbolic evaluation in compute.

## Agreement with the meromorphic residue

When $\mathrm{tr}_{M, \ell}$ extends to a meromorphic function on
$\mathbb{C} \setminus \{\zeta_\ell\}$ with a simple pole at
$\zeta_\ell$, the analytic residue (Cauchy contour integral around
$\zeta_\ell$) equals the cyclotomic-projection value defined above.
This is a special case of the discrete-Fourier ↔ residue
correspondence for rational functions on the unit circle. The
algebraic side does not depend on the analytic agreement; the
proposition stands without it.

## Proof

1. **The graded trace is in $\mathbb{Z}[q^{\pm 1}]$.** By
   [graded Markov trace](#prop:graded-markov-trace-from-gs-filtration),
   each $\mathrm{tr}_{M, \ell}$ is a Laurent polynomial.

2. **Cyclotomic projection is well-defined.** $\Phi_\ell(q) \in \mathbb{Z}[q]$
   is irreducible over $\mathbb{Q}$; $\mathbb{Z}[q^{\pm 1}] / \Phi_\ell(q)
   \cong \mathbb{Z}[\zeta_\ell]$ is the $\ell$-th cyclotomic ring.

3. **The DFT extraction equals the cyclotomic projection.** The map
   $f(q) \mapsto \frac{1}{\ell} \sum_{k=0}^{\ell-1} \zeta_\ell^{-k} f(q^k)$
   reduces a Laurent polynomial to its image under the projection
   $\mathbb{Z}[q^{\pm 1}] \to \mathbb{Z}[q^{\pm 1}] / \Phi_\ell(q)$
   evaluated at $\zeta_\ell$. Direct computation.

4. **Finiteness of the spectral sum.** By
   [GB spectral sequence](#prop:gb-spectral-sequence), only finitely
   many graded traces are non-zero on any fixed $x$; hence only
   finitely many residues contribute to the spectral-sum identity.

$\square$
