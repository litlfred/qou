The torus knots $T_{2,p}$ for primes $p \geq 11$ are not merely
absent from the Bring surface for dimensional reasons --- they
are **algebraically killed** by an ideal in the Hecke algebra
$H_2(q)$, whose generator is the Chebyshev overflow at genus $4$.

## Statement

**Proposition.**
*Let $s = q - q^{-1}$, $u = s^2$, and let $a_p(u)$ be
the Hecke coefficient of $T^p$ in $H_2(q)$, i.e.,
$T^p = a_p \cdot T + a_{p-1} \cdot \mathbf{1}$.  Then:*

**(i) Chebyshev degree = Seifert genus.**
*For odd $p$, $a_p$ is a polynomial of degree $(p-1)/2$ in
$u = s^2$:*

$$
  a_p(u)
  \;=\;
  U_{p-1}\!\left(\tfrac{s}{2}\right)
  \;=\;
  \sum_{j=0}^{(p-1)/2} c_j\, u^j
$$

*where $U_{n}$ is the Chebyshev polynomial of the second kind
and $c_{(p-1)/2} = 1$.  The degree
$\deg_u a_p = (p-1)/2 = g(T_{2,p})$
is the Seifert genus of $T_{2,p}$.*

**(ii) Genus-filtration ideal.**
*Define the genus-$g$ filtration ideal
$\mathfrak{I}_g \subset \mathbb{Z}[u]$ by*

$$
  \mathfrak{I}_g
  \;=\;
  \bigl\{\, f(u) \in \mathbb{Z}[u] : \deg f > g \,\bigr\}
  \;=\;
  (u^{g+1}).
$$

*A torus knot $T_{2,p}$ admits a localized knot structure on
$\Sigma_g$ if and only if $a_p \notin \mathfrak{I}_g$, i.e.,
$\deg_u a_p \leq g$.*

**(iii) Yekutieli obstruction = leading coefficient.**
*The Yekutieli obstruction class
$\kappa(T_{2,p}) \in H^2(\Sigma_g, \mathbb{Z})$ is
the image of the leading monomial of $a_p$ under the
projection $\pi_g \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^{g+1})$:*

$$
  \kappa(T_{2,p})
  \;=\;
  \begin{cases}
    0 & \text{if } (p-1)/2 \leq g \quad
      (\text{lifts: } a_p \text{ fits in } H^1(\Sigma_g)), \\[6pt]
    c_{(p-1)/2} \cdot [u^{(p-1)/2}] \neq 0 &
      \text{if } (p-1)/2 > g \quad
      (\text{obstructed: overflow}).
  \end{cases}
$$

*Since $c_{(p-1)/2} = 1$ for all odd $p$, the obstruction is
nonzero for every prime $p \geq 2g + 3$.*

## The Chebyshev table

The Hecke recurrence $a_{n+1} = s \cdot a_n + a_{n-1}$ with
$a_0 = 0$, $a_1 = 1$ gives, for odd primes, the following
polynomials in $u = s^2 = (q - q^{-1})^2$:

| $p$ | $a_p(u)$ | $\deg_u$ | genus | embeds in $\Sigma_4$? |
|:---:|:---------|:---:|:---:|:---:|
| $3$ | $u + 1$ | $1$ | $1$ | Yes |
| $5$ | $u^2 + 3u + 1$ | $2$ | $2$ | Yes |
| $7$ | $u^3 + 5u^2 + 6u + 1$ | $3$ | $3$ | Yes |
| $9^*$ | $u^4 + 7u^3 + 15u^2 + 10u + 1$ | $4$ | $4$ | Yes (saturates) |
| $11$ | $u^5 + 9u^4 + 28u^3 + 35u^2 + 15u + 1$ | $5$ | $5$ | **No** |
| $13$ | $u^6 + 11u^5 + 45u^4 + 84u^3 + 70u^2 + 21u + 1$ | $6$ | $6$ | **No** |

($*$: $9 = 3^2$ is not prime but $T_{2,9}$ is the degree-$2$
tower of the trefoil.)

## Two characterisations of "no $T_{2,11}$"

**Chebyshev (algebraic).**
The polynomial $a_{11}(u) = u^5 + 9u^4 + 28u^3 + 35u^2 + 15u + 1$
has a degree-$5$ leading term.  Under the truncation
$\pi_4 \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^5)$:

$$
  a_{11} \;\equiv\; 9u^4 + 28u^3 + 35u^2 + 15u + 1
  \pmod{u^5}
$$

The **remainder** $a_{11} - \pi_4(a_{11}) = u^5$ is the
generator of $\mathfrak{I}_4$.  Every $T_{2,p}$ with $p \geq 11$
has $a_p \equiv a_p \pmod{u^5}$ with nonzero remainder --- the
leading $u^{(p-1)/2}$ term cannot be absorbed.

**Yekutieli (cohomological).**
The Seifert surface $F_p$ of $T_{2,p}$ has $g_p = (p-1)/2$
independent $1$-cycles $\{\gamma_1, \ldots, \gamma_{g_p}\}$.
Embedding $T_{2,p}$ in $\Sigma_g$ requires an injection

$$
  \iota_* \colon H_1(F_p;\, \mathbb{Z})
  \;\hookrightarrow\;
  H_1(\Sigma_g;\, \mathbb{Z})
  \;=\; \mathbb{Z}^{2g}.
$$

For $g_p \leq g$: the injection exists, and $\kappa = 0$.

For $g_p = g + 1$ (the critical case $p = 2g + 3$): the
$(g+1)$-th Seifert cycle $\gamma_{g+1}$ has no target.  The
connecting homomorphism in the exact sequence of the pair
$(\Sigma_g, F_p)$ sends $\gamma_{g+1}$ to a nonzero class:

$$
  \partial \colon
  H_1(F_p, \partial F_p)
  \;\longrightarrow\;
  H_0(\partial F_p)
  \;\longrightarrow\;
  H^2(\Sigma_g)
  \;\cong\; \mathbb{Z}
$$

producing $\kappa(T_{2,p}) = 1 \cdot [\Sigma_g] \neq 0$,
where $[\Sigma_g]$ is the fundamental class.  This matches
$c_{(p-1)/2} = 1$ in the Chebyshev characterisation.

## Formal coordinates: unwinding $d_q^2 \neq 0$

The non-nilpotence $d_q^2 \alpha = q^{-1}(1-q^{-1})\,
\omega_V \wedge_q [\xi, \alpha]$
([categorical $d_q^2$](#prop:categorical-dq-squared)) provides
the differential-geometric mechanism.

Associate to $T_{2,p}$ the form
$\alpha_p = a_p(u) \cdot \omega_T \in \Omega^1(A)$, where
$\omega_T$ is the Hecke $1$-form (the $T$-component of the
Maurer--Cartan form on $H_2(q)$) and $u = s^2$ acts as a
grading parameter.

The weight decomposition assigns degree $k$ in $u$ to the
$k$-th Seifert cycle: $\alpha_p = \sum_{k=0}^{g_p} c_k \,
u^k \omega_T$, with $[\xi, u^k \omega_T] = k \cdot u^k \omega_T$
(the Lie derivative counts Seifert cycles).

Applying $d_q^2$ iteratively:

1. **At genus level $k \leq g$:** The component $c_k u^k \omega_T$
   maps under $\iota_*$ to a class in $H^1(\Sigma_g)$.
   The obstruction $d_q^2(c_k u^k \omega_T) \propto
   k \cdot \omega_V \wedge c_k u^k \omega_T$ is absorbed by
   the available $H^2(\Sigma_g)$ pairing --- it vanishes on the
   horizontal subcomplex ($\xi$-invariant forms project the
   surplus away).

2. **At genus level $k = g + 1$:** The component
   $c_{g+1} u^{g+1} \omega_T$ has no target in $H^1(\Sigma_g)$.
   The obstruction

   $$
     d_q^2(c_{g+1}\, u^{g+1}\, \omega_T)
     \;=\;
     q^{-1}(1-q^{-1})\,(g+1)\, c_{g+1}\, u^{g+1}\,
     \omega_V \wedge_q \omega_T
   $$

   is a **nonzero class in $\Omega^2(A)$** that does not pair
   to zero against $H_2(\Sigma_g)$.  The coefficient
   $(g+1) \cdot c_{g+1} \cdot q^{-1}(1-q^{-1})$ is nonzero
   for all $q > 1$, and $c_{g+1} = 1$ (the leading Chebyshev
   coefficient is always $1$).

3. **The obstruction class.** The $d_q^2$-obstruction at level
   $g + 1$ descends to the Yekutieli class:

   $$
     \kappa(T_{2,p})
     \;=\;
     (g+1) \cdot q^{-1}(1-q^{-1}) \cdot [\omega_V \wedge_q \omega_T]
     \;\in\; H^2(\Sigma_g,\, \mathbb{Z})
   $$

   which is nonzero for $q \neq 1$.  At $q = 1$ (the classical
   limit), $d_q^2 = 0$ and all obstructions vanish ---
   consistent with classical de Rham cohomology having no
   genus constraint on embeddings.

## For all primes $p \geq 11$ on $\Sigma_4$

Setting $g = 4$:

- **$p = 11$:** $\deg_u a_{11} = 5 > 4$.  The surplus is
  $u^5$.  One Seifert cycle is obstructed.
  $\kappa(T_{2,11}) = 5 \cdot q^{-1}(1-q^{-1}) \neq 0$.

- **$p = 13$:** $\deg_u a_{13} = 6 > 4$.  Surplus $u^6 + 11u^5$.
  Two Seifert cycles obstructed.

- **$p = 17$:** $\deg_u a_{17} = 8 > 4$.  Four surplus terms.

In general, for prime $p \geq 11$: the Chebyshev polynomial
$a_p(u)$ has $(p-1)/2 - 4$ terms above the genus-$4$ cutoff,
each generating an independent obstruction.  The ideal
$\mathfrak{I}_4 = (u^5)$ annihilates all of them simultaneously.

## The $q$-primorial and additive structure

The embeddable primes $\{2, 3, 5, 7\}$ satisfy a remarkable
additive property in the Chebyshev table: their $a_p(u)$ polynomials
are **exactly** the ones whose constant term is $1$ and whose
coefficients are bounded by the Catalan triangle.  Specifically,
the coefficient of $u^j$ in $a_{2k+1}$ is the ballot number
$\binom{k+j}{2j}$, and for $k \leq 3$ (primes $3, 5, 7$),
all these coefficients lie within the range of the $4$-dimensional
Seifert pairing on $H^1(\Sigma_4)$.

The **$q$-primorial** $[7]_q\# = [2]_q \cdot [3]_q \cdot [5]_q
\cdot [7]_q$ (the product of $q$-integers for all embeddable primes)
is the natural volume unit of the Hecke algebra restricted to
$\Sigma_4$.  Its degree in $u$ is $0 + 1 + 2 + 3 = 6 < 2g = 8$,
confirming that the prime content $\{2, 3, 5, 7\}$ fits within
$H^1(\Sigma_4)$ with room to spare (for the composites
$T_{2,9}$ and $T_{3,4}$).

The prime $11$ is the **first prime whose $q$-integer
$[11]_q$ has Chebyshev degree exceeding $g = 4$** in the
two-strand Hecke algebra.  This is the algebraic root of
particle finiteness: the genus bound is a corollary of the
Chebyshev overflow, not the other way around.
