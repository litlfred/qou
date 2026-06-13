The Lean formalisation of the GB-residue spectral sum
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence))
relies on a second `noncomputable opaque` declaration,
`residueAtRoot`, axiomatised in
[`content/.../gb-residue-spectral-sum.lean`](gb-residue-spectral-sum.lean)
alongside `gradedMarkovTrace`. This block gives the **narrative
replacement** for `residueAtRoot` — defining the cyclotomic
residue $\mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot
\mathrm{tr}_{M, \ell})$ purely algebraically as a quotient in the
**Habiro completion** of $\mathbb{Z}[q^{\pm 1}]$, with no
analytic continuation in $\mathbb{C}$.

The companion graded-trace block is
[`prop:graded-markov-trace-from-gs-filtration`](#prop:graded-markov-trace-from-gs-filtration).

## Setup

Let $\Phi_q(z) = \prod_{k = 1}^{\infty} (1 - q^{-k} z)^{-1}$ be the
quantum dilogarithm and let
$\mathrm{tr}_{M, \ell} : J^\ell / J^{\ell+1} \to \mathbb{Q}(q)$ be
the graded Markov trace
([`prop:graded-markov-trace-from-gs-filtration`](#prop:graded-markov-trace-from-gs-filtration)).
Fix a closed braid $K$ with Hecke normal form
$T_w \in H_n(q)$ and confinement level $\ell(K, q)$
([`prop:confinement-level-exists`](#prop:confinement-level-exists)).

For each $\ell \in \{1, \dots, \ell(K, q)\}$ the
GB-filtration index $\ell$ determines a **distinguished
cyclotomic order** $n_\ell \in \mathbb{N}_{\geq 2}$ — the order of
the primitive root of unity $\zeta_\ell$ at which the $\ell$-th
graded contribution is supported. Concretely $n_\ell$ is the
smallest integer such that the $q$-Pochhammer factor
$(q;q)_{n_\ell}$ divides the leading coefficient of every
representative of $J^\ell / J^{\ell+1}$ — a property that is
combinatorial in the GS leading-monomial order, not analytic
\cite{habiro2002}.

The **Habiro ring** is the cyclotomic completion

$$
  \widehat{\mathbb{Z}[q]}
  \;=\;
  \varprojlim_n \mathbb{Z}[q] / ((q; q)_n),
$$

with cyclotomic-projection maps
$\pi_n : \widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q] / \Phi_n(q)$,
where $\Phi_n(q)$ is the $n$-th cyclotomic polynomial.

## Statement

**Proposition (algebraic cyclotomic residue).**
*Let $T_w \in J^\ell / J^{\ell+1}$ have $\mathrm{tr}_{M, \ell}(T_w)
\in \mathbb{Q}(q)$.  The cyclotomic residue*

$$
  \mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M, \ell})(T_w)
$$

*is well-defined as the image of $\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)$
under the cyclotomic projection*

$$
  \pi_{n_\ell}
  \;:\;
  \widehat{\mathbb{Z}[q]}
  \longrightarrow
  \mathbb{Z}[q] / \Phi_{n_\ell}(q),
$$

*viewed as an element of the residue field $\mathbb{Q}(\zeta_\ell)$
via the natural isomorphism*

$$
  \mathbb{Z}[q] / \Phi_{n_\ell}(q)
  \;\cong\;
  \mathbb{Z}[\zeta_\ell].
$$

*Equivalently, in the standard $q$-series language:*

$$
  \mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M, \ell})(T_w)
  \;=\;
  \frac{(\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w))}{\Phi_{n_\ell}(q)}
  \pmod{\Phi_{n_\ell}(q)}.
$$

## Why this replaces the Lean `opaque`

The Lean declaration

```lean
noncomputable opaque residueAtRoot (ℓ : ℕ) (ζ : RootOfUnity) (q : ℝ) : ℝ
```

in [`gb-residue-spectral-sum.lean`](gb-residue-spectral-sum.lean)
treats the residue as an unspecified function of three variables
($\ell$, $\zeta$, $q$) returning a real number — which forces the
formalisation to live over $\mathbb{R}$ and to invoke complex
analysis informally to compute residues at unit-circle roots.

The proposition above replaces this by a constructive algebraic
definition entirely inside $\widehat{\mathbb{Z}[q]}$: cyclotomic
projection plus the Habiro-ring isomorphism. Three things become
immediate:

1. **No analytic continuation.** The residue is a quotient by a
   cyclotomic polynomial, not a complex-analytic limit.
2. **Algebraic-side stays in $\mathbb{Q}(\zeta_\ell)$.** The
   Lean type changes from `ℝ` to `LaurentPolynomial ℚ` (or, more
   precisely, an element of the cyclotomic ring
   $\mathbb{Z}[\zeta_\ell]$), aligning with the three-calibration
   discipline
   ([`prop:three-calibration-discipline`](../observations/three-calibration-discipline.md))
   that the algebraic side lives in $\mathbb{Q}$-coefficients.
3. **Compatibility with the spectral sequence** of
   [`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence) is
   automatic — the $E_\infty$ page reads off the cyclotomic
   projections of the graded trace.

## Proof sketch

The graded Markov trace
$\mathrm{tr}_{M, \ell}(T_w) \in \mathbb{Q}(q)$ has, by
construction
([`prop:graded-markov-trace-from-gs-filtration`](#prop:graded-markov-trace-from-gs-filtration)),
$q$-degree $= \ell$ in the GS-filtration grading. Multiplied by
$\Phi_q$, the product is an element of the Habiro ring:

$$
  \Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)
  \;\in\;
  \widehat{\mathbb{Z}[q]}.
$$

The Habiro ring's cyclotomic projection
$\pi_n : \widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q] / \Phi_n(q)$
is a $\mathbb{Z}$-algebra map for each $n$ \cite{habiro2002}.
Applying $\pi_{n_\ell}$ (the cyclotomic projection at the
distinguished order for stratum $\ell$) and identifying
$\mathbb{Z}[q] / \Phi_{n_\ell}(q)$ with $\mathbb{Z}[\zeta_\ell]$
gives an element of the cyclotomic ring — the residue.

Equivalence with the analytic definition (when both apply) is the
content of the Habiro-completion theorem
\cite{habiro2002}: the cyclotomic projections agree with the
analytic residue at $\zeta_\ell$ for any element of
$\widehat{\mathbb{Z}[q]}$ that converges as a complex function on
$|q| > 1$. The algebraic projection, however, is well-defined
*regardless* of analytic convergence — which is the point: the
algebraic-side derivation does not need analytic continuation.
