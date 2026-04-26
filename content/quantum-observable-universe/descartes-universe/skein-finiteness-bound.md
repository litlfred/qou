The number of stable nuclear configurations at a given substrate
parameter $q$ is **finite**.  The stability boundary is the zero
locus of the Skein polynomial $P_{\mathcal{N}(p,n)}(q)$.

## The transfer matrix eigenvalue inequality

Each generator $\sigma_i$ of the nuclear braid contributes a
traced volume
$\hat{V}_i = z \cdot M_{11}^{(i)} + M_{21}^{(i)}$
([transfer matrix](#prop:skein-polynomial-transfer-matrix)),
and the Skein polynomial is the product:

$$
  P_{\mathcal{N}(p,n)}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q).
$$

The transfer matrix $T(c, d)$ at each crossing has eigenvalues

$$
  \lambda_{\pm} = 
  \frac{\mathrm{tr}T \pm \sqrt{(\mathrm{tr}T)^2 - 4\det T}}{2}
$$

which are **real and opposite in sign** (since $\det T < 0$ for
all three crossing types):

| Crossing type | $\lambda_+$ | $\lambda_-$ | $\lvert\lambda_+/\lambda_-\rvert$ |
|:---:|:---:|:---:|:---:|
| pp | $q$ | $-q^{-1}$ | $q^2$ |
| nn | $q^3$ | $-q^{-1}$ | $q^4$ |
| mix | $\approx q^{3/2}$ | $\approx -q^{-1/2}$ | $\approx q^2$ |

The chain of $k$ crossings at generator $\sigma_i$ gives

$$
  \hat{V}_i =  c_+\lambda_+^k +  c_-\lambda_-^k
$$

where $c_{\pm}$ depend on $z$ and the crossing coefficients.
Since $\lambda_- < 0$, the term $c_- \lambda_-^k$ **alternates
in sign** with $k$.

## The finiteness inequality

**Proposition.**
*A nuclear configuration $\mathcal{N}(p, n)$ is stable only if
the Skein polynomial is positive:*

$$
  P_{\mathcal{N}(p,n)}(q)  >  0.
$$

*This is equivalent to the **lattice inequality**: for each
generator $i = 0, \ldots, A-2$, the traced volume must be
positive:*

$$
  \hat{V}_i(q) = 
  c_+^{(i)}\lambda_+^{k_i}
  + 
  c_-^{(i)}\lambda_-^{k_i}
   >  0
  \qquad (i = 0, \ldots, A-2)
$$

*where $k_i$ is the number of crossings at generator $i$
(nucleon $i$ with all nucleons $j > i$).*

**The bound.** Since $|\lambda_+| > |\lambda_-|$ (the ratio
is $q^2$ or $q^4$), the $c_+ \lambda_+^k$ term dominates for
large $k$.  The sign of $\hat{V}_i$ depends on:

1. The **sign of $c_+^{(i)}$**: determined by the Markov
   parameter $z$ and the crossing coefficients.
2. The **parity of $k_i$**: when $k_i$ is odd, $\lambda_-^{k_i} < 0$;
   when even, $\lambda_-^{k_i} > 0$.
3. The **ratio $|c_-/c_+|$**: when this exceeds
   $|\lambda_+/\lambda_-|^{k_i}$, the negative term dominates.

For a nucleus with $A$ nucleons, generator $i$ has $k_i = A - 1 - i$
crossings.  Generator $0$ has the most crossings ($k_0 = A - 1$).
The stability condition at generator $0$ is the **binding**:

$$
  \hat{V}_0(q) > 0
  \quad\Longleftrightarrow\quad
  \frac{c_+^{(0)}}{|c_-^{(0)}|}
   > 
  \left|\frac{\lambda_-}{\lambda_+}\right|^{A-1}
  =  q^{-2(A-1)}
  \qquad\text{(pp-type)}
$$

This is automatically satisfied for $q > 1$ because the
right side decreases exponentially with $A$.  **Individual
generator volumes do not flip sign.**

## The product sign flip

The Skein polynomial $P = \prod \hat{V}_i$ can change sign
even though each $\hat{V}_i > 0$, if the **number of
negative-$\hat{V}_i$ generators** is odd.  From the sequential
build data:

| $A$ | $\hat{V}$ signs | $P$ sign | Stable? |
|:---:|:---:|:---:|:---:|
| $1$ | $(+)$ | $+$ | Yes |
| $2$ | $(+)$ | $+$ | Yes |
| $3$ | $(+, +)$ | $+$ | Yes |
| $4$ | $(+, +, +)$ | $+$ | Yes (shell-closure) |
| $5$ | $(+, +, +, +)$ | $+$ | Yes |
| $6$ | All $+$ but product $< 0$ | $-$ | **No** |

At $A = 6$, the product becomes negative ($P = -0.0053$) even
though individual volumes are positive.  This occurs because the
**cross-terms** between generators (from the Yang--Baxter
interaction) introduce destructive interference that flips the
total sign.

The cross-term contribution grows with $A$ because each new
nucleon interacts with all existing nucleons.  The number of
cross-terms grows as $\binom{A}{2}$, and when this exceeds the
direct-term contribution, the sign flips.

## The closed-form bound

The sign flip comes from **factorial vs exponential** competition.

The Hecke normal form $\mathcal{N}$ has at most $A!$ terms
(the dimension of $H_A(q)$).  The dominant term has coefficient
$\sim q^{\binom{A}{2}}$.  The Yang–Baxter cross-terms redistribute
coefficient among up to $(A-1)!$ reduced words.  The Markov trace
weights each word by $z^{f(w)}$ where $z = 1/[2]_q$ and $f(w)$ is
the Markov height.  The trace magnitude is:

$$
  |P(q)|  \leq  \sum_w |c_w| \cdot z^{f(w)}
   \sim  (A-1)! \cdot q^{\binom{A}{2}} \cdot z^{A-1}
$$

while the dominant contribution (without cross-term cancellation)
scales as $q^{\binom{A}{2}} \cdot z^{A-1}$.  The cancellation
ratio $1 - |P|/\Sigma|c_w|$ measures destructive interference:

| $A$ | $\lvert P\rvert$ | $\Sigma\lvert c_w\rvert$ | Cancellation |
|:---:|:-----:|:-------------:|:------------:|
| $1$ | $1.000$ | $1.00$ | $0\%$ |
| $3$ | $0.601$ | $1.52$ | $60\%$ |
| $4$ | $0.060$ | $2.42$ | $97.5\%$ |
| $5$ | $0.141$ | $4.00$ | $96.5\%$ |
| $6$ | $0.005$ | $11.4$ | $99.95\%$ ← **sign flip** |

The sign flips when $(A-1)!$ cross-terms overwhelm the dominant
term.  The critical condition is:

$$
  (A-1)!  >  [2]_q^{A-1}
$$

The $q$-deformed version uses $q$-factorials throughout (no
classical Stirling, no Euler $e$):

$$
  [n]_q! =  \prod_{k=1}^{n} [k]_q
  \qquad\text{where}\quad
  [k]_q =  \frac{q^k - q^{-k}}{q - q^{-1}}
$$

The critical condition is:

$$
  \boxed{[A-1]_q!  >  [2]_q^{A-1}}
$$

Equivalently: the **average $q$-integer** exceeds $[2]_q$:

$$
  \frac{1}{A-1}\sum_{k=1}^{A-1} \ln [k]_q
   > 
  \ln [2]_q
$$

Since $[k]_q$ is strictly increasing in $k$ (for $q > 1$) and
$[1]_q = 1 < [2]_q$, the average starts below $\ln [2]_q$ and
grows monotonically.  The crossover:

| $A$ | $[A\!-\!1]_q!$ | $[2]_q^{A-1}$ | Exceeds? |
|:---:|:---:|:---:|:---:|
| $2$ | $1.0$ | $2.01$ | No |
| $3$ | $2.01$ | $4.04$ | No |
| $4$ | $6.12$ | $8.13$ | No |
| $5$ | $25.15$ | $16.35$ | **Yes** |
| $6$ | $131.3$ | $32.88$ | **Yes** |

The crossover occurs at $A = 5$ for all $q > 1$ (the
$q$-correction is $O(\varepsilon^2)$ where $\varepsilon = \ln q$,
and at $q = q_0$: $\varepsilon^2 = 0.011$, negligible).

**At $q = q_0$:** $[A\!-\!1]_q! > [2]_q^{A-1}$ first at
$A = 5$.  The Skein polynomial sign flip occurs at $A = 6$
(one step later, because the (2,2) shell closure stabilises
$A = 4$).

**At $q = 1$:** $[k]_1 = k$ and $[2]_1 = 2$, so $(A-1)! > 2^{A-1}$
also crosses at $A = 5$.  The bound is **topological** (from
the Iwahori--Hecke algebra dimension $A!$), not dependent on $q$.

**At $q \to \infty$:** $[k]_q \sim q^{k-1}$, so $[A\!-\!1]_q! \sim q^{(A-1)(A-2)/2}$ and $[2]_q^{A-1} \sim q^{A-1}$.  The
crossover shifts to $(A-1)(A-2)/2 > A-1$, i.e., $A > 4$,
which is the same.

**Note:** This bound applies to the alternating $\mathfrak{p} \mathfrak{n}$ filling order.  Shell closures
([shell closure](#prop:shell-closure-normal-form)) create
**stability islands** beyond $A_{\max}$ where the palindromic
Poincaré distribution restores $P > 0$.  The physical nuclear
chart extends to $A \sim 300$ because successive shell closures
at magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ re-stabilize
the Skein polynomial.

## The nuclear chart lattice

The set of stable configurations forms a **finite lattice**
in the $(p, n)$ plane:

$$
  \mathcal{L}(q)
  = 
  \bigl\{
    (p, n) \in \mathbb{N}^2 :
    P_{\mathcal{N}(p,n)}(q) > 0
  \bigr\}
$$

This lattice is bounded by:
- The **beta-stability line** $p^*(A)$
  ([beta stability](#prop:beta-stability)) — the minimum-energy
  proton count at each $A$.
- The **Skein polynomial zero** $P(q) = 0$ — the drip line
  where the Skein polynomial changes sign.
- The **shell closures** ([shell closure](#prop:shell-closure-normal-form))
  — islands of enhanced stability where the palindromic Poincaré
  distribution gives maximum binding.

The lattice $\mathcal{L}(q)$ at $q = q_0$ reproduces the
experimental nuclear chart: stable isotopes cluster along the
valley of stability with magic-number shell closures at
$N, Z \in \{2, 8, 20, 28, 50, 82, 126\}$.

## Particle finiteness

The same argument applies to elementary particles.  A knot $K$
on the Bring surface ($\chi = -6$, genus $4$) must satisfy:

1. **Embeddability**: the torus knot $T_{m,n}$ embeds in
   genus $g$ only if $(m-1)(n-1)/2 \leq g$.  For $g = 4$:
   $(m-1)(n-1) \leq 8$.

2. **Positive Skein polynomial**: $P_K(q) > 0$ at the
   physical $q$.

The embeddability constraint gives a **finite list** of allowed
torus knots: $T_{2,3}$, $T_{2,5}$, $T_{2,7}$, $T_{2,9}$,
$T_{3,4}$, $T_{3,5}$.  These are the quarks, leptons, and force
carriers.  No other torus knot fits on the Bring surface — the
particle content is **determined by the genus**.
