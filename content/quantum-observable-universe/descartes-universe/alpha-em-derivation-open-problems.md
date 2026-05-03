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

Three computational paths to close the $1.55 \times 10^{-3}$ correction
have been tried and **ruled out** (or shown not to be expressible as
clean low-degree $q$-rationals):

| Path | Result | Verdict |
|------|--------|---------|
| Gram-det Plancherel-character product at $n=3$ | $\kappa \approx 7 \times 10^{-6}$ | Ruled out (need $\sim 1.888$) |
| q-Plancherel sums on $H_5$ Wedderburn blocks | trivial or astronomical | Ruled out |
| Scan $\hbar_q^k\cdot[a]_q\cdot[b]_q/([c]_q\cdot[d]_q)$, $a,b,c,d \le 12$ | 0 matches at $10^{-4}$ | Ruled out at this degree |

See [`alpha-em-correction-derivation-attempts.witness.json`](#) for
the full attempt log.

Until one of these (or another structural source) closes the gap,
the canonical statement should remain the bare formula
$1/\alpha_{\text{bare}} = q[9]_q[10]_q$ with the $-0.155\%$ residual
documented as an open problem.