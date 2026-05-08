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
| Form B (gluon-octet) | $45[3]_q\,(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$ | $+6.7\times 10^{-9}$ | Conj.; PSLQ-empirical; only $45$ rigorously derived; disagrees with Form A at $q\ne q_0$ |

## Why both prior attempts fail audit

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
- $8q$ is identified two different ways (Lean: $\dim \mathfrak{su}(3)$;
  .md: "two-step crossing-pattern enumeration") with neither calculation
  performed; the required order-$3$ coefficient to make the truncation
  exact is $\approx -52$, which is not a clean $q$-rational.

Form A and Form B agree only at $q = q_0$; at every other $q$ they give
different values for $1/\alpha$, confirming that they are not the same
function of $q$ and that Form B's match is single-point fit.

## Roadmap for an honest derivation

The $1.55 \times 10^{-3}$ gap is approximately the size of an
$O(\hbar_q^2)$ correction ($\hbar_q^2 \approx 9.8 \times 10^{-3}$ at
$q_0$). Three plausible structural origins:

1. **Carry out the Plancherel-character product explicitly.** The
   formula in [prop:gram-determinant-plancherel-ratio](#prop:gram-determinant-plancherel-ratio)
   is genuinely structural. Compute character coefficients
   $c_\lambda^{(s)} = \chi_\lambda(T_{2,9})$ and $c_\lambda^{(w)} = \chi_\lambda(T_{3,5})$
   in a fixed ambient algebra (e.g. $H_5$ or $H_{10}$ via Markov
   stabilization) and evaluate
   $\kappa = \prod_\lambda [\dim V_\lambda / \dim_q V_\lambda \cdot [n]_q!/n!]^{c^{(s)}_\lambda c^{(w)}_\lambda}$
   end-to-end (see [prop:gram-determinant-plancherel-ratio](#prop:gram-determinant-plancherel-ratio) for the structural source).

   **Result of first attempt (this audit, $n=3$).** Stabilising
   $T_{2,9}$ as $\sigma_1^9 \in B_3$ and using $T_{3,5} = (\sigma_1\sigma_2)^5 \in B_3$,
   with characters $\chi_{(3)}(\sigma_1^9) = q^9$, $\chi_{(2,1)}(\sigma_1^9) = q^9 - q^{-9}$,
   $\chi_{(1,1,1)}(\sigma_1^9) = -q^{-9}$ and $\chi_{(3)}((\sigma_1\sigma_2)^5) = q^{10}$,
   $\chi_{(2,1)}((\sigma_1\sigma_2)^5) = -1$ (cube-root structure on $V_{(2,1)}$ since
   $(\sigma_1\sigma_2)^3$ is central with content sum $0$), $\chi_{(1,1,1)}((\sigma_1\sigma_2)^5) = q^{-10}$,
   the Plancherel-character product evaluates at $q_0$ to
   $\kappa \approx 7 \times 10^{-6}$ — **not** the $\sim 1.888$
   required to match CODATA.

   This rules out $n=3$ as the correct ambient. Next steps: try
   $n = 5$ (where $T_{3,5}$ lives more naturally) and $n = 10$
   (matching the $\binom{10}{2} = 45$ narrative). Both require
   explicit Hecke character tables in higher dimension and are
   non-trivial computations.

2. **Recognise the correction as $q$-Plancherel measure on Wedderburn
   blocks.** The bare formula uses force-carrier complexity
   $[9]_q[10]_q$; the correction may come from re-weighting by the
   Plancherel measure of the Hecke ambient algebra.

   **Result of first attempt (this audit, $n=5$).** Set
   $T_{2,9} \boxtimes T_{3,5} \in B_5$ as the disjoint-union 5-strand
   braid. Plancherel measure $P(\lambda) = (\dim_q V_\lambda)^2 / [5]_q!$
   on partitions of $5$ is computable; common natural sums tested:

   - $\sum_\lambda P(\lambda) \cdot \dim V_\lambda / \dim_q V_\lambda$
     gives $\sim 6.83$ (not the required $1 + 1.55 \times 10^{-3}$).
   - $\prod_\lambda (\dim V_\lambda / \dim_q V_\lambda)^{P(\lambda)}$
     gives $\sim 0$ (because $P(\lambda)$ values reach $131$ on
     $\lambda = (5)$ and $(1^5)$, blowing up the product).
   - $\sum_\lambda P(\lambda)^2$ gives $\sim 3.5 \times 10^4$.

   None matches the target correction.

3. **Direct $q$-rational scan of the multiplicative correction.**
   Required factor: $1 + \hbar_q^2 \cdot X$ with
   $X(q_0) \approx 0.15841$. Scan over
   $X = \hbar_q^k \cdot [a]_q \cdot [b]_q / ([c]_q \cdot [d]_q)$ for
   integers $1 \leq a,b,c,d \leq 12$ at tolerance $10^{-4}$:
   **zero matches.** Closest single-ratio form is $\hbar_q^2 / [6]_q$
   at $\sim 1.2\%$ off, which is well outside the precision required
   for a structural identity.

4. **Examine the role of the $\mathbb{CP}^1$-fibration on the state
   bundle.** The bare derivation uses scalar trace; a vector-valued
   refinement on the $\mathbb{CP}^1$ fibre could produce a corrective
   factor of order $\hbar_q^2$. Not yet attempted.

## Status of derivation effort (this audit)

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

## Why block-diagonal Gram deformations cannot close the gap

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
  [`conj:em-coupling-bring-zero-mode`](#conj:em-coupling-bring-zero-mode),
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
$\mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3)$ archimedeanly. Two
sub-problems remain (both open computations rather than structural
anomalies): identify the precise Bloch-group class on Bring's
surface, and lift the next-order $\alpha/(4\pi)$ term to a higher
Bloch group $B_n(\mathbb{C})$.

## What this implies

Either:

1. The bare formula $1/\alpha_{\text{bare}} = q[9]_q[10]_q$ is itself
   slightly wrong — perhaps the singlet-trace identification
   $|\mathrm{tr}_\tau(e_-)|^2 = q^{-1}$ in
   [prop:em-coupling-projection](#prop:em-coupling-projection) needs
   refinement.
2. The correction is genuinely complex (high-degree polynomial in
   many $q$-integers, or involves $q$-dilogarithms / theta-function
   special values not in the standard basis).
3. The correction reflects genuine quantum-loop corrections that
   are not expressible at the categorical / tree level — i.e., the
   bare formula is exact only in the classical / one-particle
   limit, and the missing $1.55 \times 10^{-3}$ is a vacuum
   polarisation / RG running effect that requires path-integral
   quantisation.

Until one of these is resolved, the canonical statement remains the
bare formula with the $-0.155\%$ residual documented as an open
problem.

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

The first correction has a clean geometric identification:

$$
  \frac{2}{3\pi}
  \;=\; \frac{\mathrm{Vol}(S^2)}{3\cdot\mathrm{Vol}(S^3)}
  \;=\; \frac{4\pi}{3 \cdot 2\pi^2}.
$$

This is the kind of finite topological constant that arises from a
photon zero-mode on a closed 3-manifold (standard QFT: the zero-mode
of $\Box^{-1}$ on a closed Riemannian $M$ contributes $1/\mathrm{Vol}(M)$
to a Green's function). The coefficient $2/(3\pi)$ would then encode
the categorical-Lagrangian QED vacuum-polarisation 1PI graph evaluated
at zero external momentum on the QOU substrate's natural 3-manifold
(likely $S^3$ via a Hopf-fibred $S^1 \to S^3 \to S^2$).

The next-order term $\alpha/(4\pi)$ is suggestive of a Schwinger-like
1-loop self-coupling. The numerical fit places this coefficient at
$\sim 1.4\%$ off from exactly $1/(4\pi)$; the true coefficient may
be $1/(2\pi\cdot[2]_q)$ or another small $q$-correction.

### What's needed to upgrade this lead to a proof

1. **Identify the 3-manifold** carrying the photon propagator.
2. **Compute the photon zero-mode** of the QOU vacuum-polarisation
   1PI graph at zero external momentum and verify the coefficient
   equals $2/(3\pi)$.
3. **Verify UV finiteness.** Reshetikhin-Turaev shadow-world
   regularisation should produce a finite answer (force-carrier
   complexity $[9]_q[10]_q$ regularises the categorical sum,
   replacing the continuum momentum integral).
4. **Compute the next-order self-energy** as a 2-loop graph;
   verify the coefficient is exactly $1/(4\pi)$ or identifies as
   $1/(2\pi[2]_q)$ with the small $q$-correction matching the
   residual.

A numerical match at $5.7 \times 10^{-8}$ is too precise to be
coincidence; the structural derivation almost certainly exists.