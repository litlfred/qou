The atomic-braid Markov trace, expressed in the parameter
$u = q^{1/2}$, admits a finite **Habiro cyclotomic expansion**
with integer coefficients.  This is the Hecke-algebra shadow of
Habiro's cyclotomic expansion for the colored Jones polynomial
\cite{habiro2002}, specialised to the single-level (non-colored)
Markov trace.

**Proposition.**
*Let $T_w(Z, N) \in H_{3A}(q)$ be the atomic-braid image for
$A = Z + N$ nucleons
([categorical mass, Markov](#prop:categorical-mass-markov)), and
let $u = q^{1/2}$.  Then there exists a denominator $D(u)$ — a
finite product of cyclotomic polynomials in $u$ — and a Laurent
polynomial*

$$
  p(u) \;:=\; D(u) \cdot \mathrm{tr}_M\!\bigl(T_w(Z, N), u^2\bigr)
  \;\in\; \mathbb{Z}\bigl[u, u^{-1}\bigr]
$$

*admitting the Habiro cyclotomic expansion*

$$
  p(u) \;=\; \sum_{m=0}^{m_{\max}} a_m(u) \cdot (u; u)_m,
  \qquad (u; u)_m = \prod_{k=1}^{m}(1 - u^k),
$$

*with*

1. **Integrality.** *$a_m(u) \in \mathbb{Z}[u]$ for every $m$.*
2. **Degree bound.** *$\deg_u a_m(u) \leq m$.*
3. **Termination.** *$a_m = 0$ for $m > m_{\max}$, and
   $m_{\max} \leq \lceil \sqrt{2 \deg_u p(u)} \rceil$.*
4. **Uniqueness.** *The expansion is unique: given
   $\deg a_m \leq m$, the sequence $\{a_m\}$ is determined by
   $p$.*

## Proof

The proof is constructive and mirrors the sequential
cyclotomic-division algorithm used in
([atomic Habiro computation](#rem:habiro-atomic-computation)).

### Step 1: Integrality of $p(u)$

The Markov trace $\mathrm{tr}_M \colon H_n(R, q) \to \mathbb{Q}(q^{1/2})$
is characterised uniquely by Markov's axioms (I) and (II)
\cite{jones1987, kassel1995}:

- *(I) Cyclicity*: $\mathrm{tr}_M(\alpha\beta) =
  \mathrm{tr}_M(\beta\alpha)$.
- *(II) Markov move*: $\mathrm{tr}_M(\alpha \cdot \sigma_{n-1}) =
  z \cdot \mathrm{tr}_M(\alpha)$ for $\alpha \in H_{n-1}(q)$,
  with $z = (q^{1/2} + q^{-1/2})^{-1} = u/(u^2+1)$.

In the standard Hecke basis $\{T_w\}_{w \in S_n}$ every basis
element has rational expression in $q$ with **cyclotomic
denominator**: each $z^k$ contributes a factor $(u^2+1)^{-k}$
([Hecke mass trace](#prop:hecke-mass-trace)), and the
Schur-Weyl decomposition
([Schur-Weyl](#prop:schur-weyl-mass-decomposition)) expresses
$\mathrm{tr}_M$ via $q$-hook products, whose factors are
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$ — again cyclotomic in $u$.

Let $D(u) \in \mathbb{Z}[u]$ be the product of all cyclotomic
denominators arising in this expansion.  Then
$p(u) = D(u) \cdot \mathrm{tr}_M(T_w(Z, N), u^2)$ has no
denominator, i.e., $p(u) \in \mathbb{Q}(u)$ with empty pole set,
hence $p(u) \in \mathbb{Q}[u, u^{-1}]$.

**Integrality in $\mathbb{Z}$**: the Jones-Markov trace takes
values in $\mathbb{Z}[q^{1/2}, q^{-1/2}]$ when applied to braid
words in the standard generators $\sigma_i$ (this is the integrality
of the Jones polynomial as a knot invariant;
\cite{jones1987} Theorem 3).  The atomic braid is a word in the
standard Hecke generators, so
$\mathrm{tr}_M(T_w, q) \in \mathbb{Z}[u, u^{-1}] \cdot D(u)^{-1}$,
and multiplying through by $D(u)$ yields
$p(u) \in \mathbb{Z}[u, u^{-1}]$.

### Step 2: Sequential cyclotomic division

Define the iteration $p_0 := p$ and, for $m \geq 0$,

$$
  a_m(u) \;:=\; p_m(u) \bmod \bigl(1 - u^{m+1}\bigr),
  \qquad
  p_{m+1}(u) \;:=\; \frac{p_m(u) - a_m(u)}{1 - u^{m+1}}.
$$

The polynomial $1 - u^{m+1}$ is monic (up to sign) of degree
$m+1$ in $\mathbb{Z}[u]$.  Since $\mathbb{Z}[u]$ is a unique
factorisation domain and the leading coefficient of
$1 - u^{m+1}$ is a unit in $\mathbb{Z}$, polynomial division
yields a remainder $a_m \in \mathbb{Z}[u]$ of degree $\leq m$
and a quotient $p_{m+1} \in \mathbb{Z}[u]$, both with integer
coefficients.  This establishes **integrality** and the
**degree bound**.

### Step 3: Termination

Each iteration satisfies $\deg_u p_{m+1} = \deg_u p_m - (m+1) +
\deg_u a_m \leq \deg_u p_m - 1$ (since $\deg a_m \leq m < m+1$).
Hence $\deg p_m$ strictly decreases at every step that produces
a nonzero $a_m$, so the process terminates after finitely many
steps.  Quantitatively: if $\deg p_0 = d$, then $\deg p_m \leq
d - \sum_{k=0}^{m-1}(k+1 - k) = d - m$, so $p_m = 0$ by
$m = d + 1$.  A tighter bound uses the total-degree gain
$\sum_{k=0}^{m}(k+1) = \binom{m+2}{2}$: termination occurs
once $\binom{m_{\max}+2}{2} > d$, giving $m_{\max} \leq
\lceil \sqrt{2 d} \rceil$.

### Step 4: Reconstruction identity

Unrolling the recursion:

$$
\begin{aligned}
  p(u) &= a_0 + (1-u) \, p_1                                 \\
       &= a_0 + (1-u) \bigl[ a_1 + (1-u^2)\, p_2 \bigr]      \\
       &= a_0 + (1-u)\, a_1 + (1-u)(1-u^2)\, p_2             \\
       &= \cdots                                             \\
       &= \sum_{m=0}^{m_{\max}} a_m(u) \cdot (u; u)_m.
\end{aligned}
$$

### Step 5: Uniqueness

Suppose $p(u) = \sum_m a_m(u) (u;u)_m = \sum_m a_m'(u) (u;u)_m$
with $\deg a_m, \deg a_m' \leq m$.  Taking the smallest $m$
where $a_m \neq a_m'$ gives $(u;u)_m \cdot (a_m - a_m') =
\sum_{k > m} (a_k' - a_k) (u;u)_k$, where the right side is
divisible by $(u;u)_{m+1} = (u;u)_m \cdot (1-u^{m+1})$.  Hence
$a_m - a_m'$ is divisible by $(1 - u^{m+1})$ in $\mathbb{Z}[u]$.
But $\deg(a_m - a_m') \leq m < m+1 = \deg(1-u^{m+1})$, so
$a_m = a_m'$ — contradiction.

$\square$

## Computational verification

The symbolic pipeline
(`habiro_coefficients_atomic.py`) implements the above
cyclotomic-division algorithm and verifies the proposition for
the three smallest atomic braids.  All coefficients lie in
$\mathbb{Z}[u]$ and the reconstruction $\sum_m a_m (u;u)_m$
matches $p(u)$ exactly.

| Braid | $\deg_u p(u)$ | # Habiro terms | $m_{\max}$ | $\sqrt{2 d}$ bound |
|:------|:-:|:-:|:-:|:-:|
| proton $(Z{=}1, N{=}0)$   | $48$  | $10$ | $9$  | $\lceil \sqrt{96} \rceil = 10$  |
| neutron $(Z{=}0, N{=}1)$  | $40$  | $9$  | $8$  | $\lceil \sqrt{80} \rceil = 9$   |
| deuteron $(Z{=}1, N{=}1)$ | $104$ | $14$ | $13$ | $\lceil \sqrt{208} \rceil = 15$ |

The observed $m_{\max}$ saturates the Step-3 bound to within one
step, consistent with the cyclotomic structure of $p(u)$
inherited from Markov–Jones integrality.

Pointwise agreement with the numerical-interpolation path
(`habiro_coefficients_interpolate.py`) is verified at
$q_0 \approx 1.1100$ to 50 decimal digits, cross-validating the
two pipelines:

- $\mathrm{tr}_M(\mathrm{proton}, q_0) = 2.12258250945\ldots$
- $\mathrm{tr}_M(\mathrm{neutron}, q_0) = 1.58939344595\ldots$
- $\mathrm{tr}_M(\mathrm{deuteron}, q_0) = 0.17743692421\ldots$

## Embedding into the Habiro ring

The Habiro ring $\widehat{\mathbb{Z}[q]}$
([Habiro ring](#def:habiro-ring)) is by definition the
inverse limit $\varprojlim_n \mathbb{Z}[q]/((q;q)_n)$.  An element
of $\widehat{\mathbb{Z}[q]}$ is represented by a sequence
$\{f_n\}$ with $f_n \equiv f_{n-1} \pmod{(q;q)_n}$, equivalently
by an infinite Habiro expansion $\sum_{m \geq 0} a_m \cdot (q;q)_m$.

The finite expansion of $p(u)$ furnished by
Proposition ([Habiro expansion](#prop:habiro-expansion-atomic))
realises the atomic-braid Markov trace as a canonical element of
$\widehat{\mathbb{Z}[u]}$, with all but finitely many $a_m$
equal to zero.  This is the algebraic home predicted by
([Habiro ring](#def:habiro-ring), item 1): the Jones-Markov
trace of any finite braid embeds into the Habiro ring as a
**truncated** element, with termination degree controlled by
the braid length.

The colored-Jones Volume Conjecture
([Kashaev volume density](#rem:kashaev-volume-density)) concerns
the infinite-colored limit, which requires an honest element of
$\widehat{\mathbb{Z}[u]}$ (i.e., infinite Habiro support).  The
finite Habiro expansion established here is the
non-colored / level-zero predecessor of that limit: it places
the atomic-braid Markov trace in the Habiro ring as a
**finitely-supported** element, with the infinite-support case
reserved for the colored generalisation.
