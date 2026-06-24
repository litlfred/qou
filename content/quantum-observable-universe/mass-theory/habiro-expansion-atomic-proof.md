The proof is the constructive sequential cyclotomic-division
algorithm. The general existence/uniqueness of the cyclotomic
expansion (with $a_m \in \mathbb{Z}[q^{\pm 1}]$, no termination)
is the content of
([Habiro completion](#prop:full-pole-structure-mass-trace)); the
present proof specialises to atomic braids and establishes termination.

### Step 1: Integrality of $p(u)$

The Markov trace on the standard Hecke basis has rational
expression in $q$ with cyclotomic denominators: each Markov
factor $z = u/(u^2+1)$ contributes $(u^2+1)^{-k}$, and the
Schur–Weyl decomposition
([Schur–Weyl](#prop:schur-weyl-mass-decomposition)) expresses
$\mathrm{tr}_M$ via $q$-hook products
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$, also cyclotomic in $u$.
Markov–Jones integrality \cite{jones1987} Thm 3 gives
$\mathrm{tr}_M(T_w, q) \in \mathbb{Z}[u, u^{-1}] \cdot D(u)^{-1}$;
multiplying by $D(u)$ yields $p(u) \in \mathbb{Z}[u, u^{-1}]$.

### Step 2: Sequential cyclotomic division

Define $p_0 := p$ and, for $m \geq 0$,

$$
  a_m(u) \;:=\; p_m(u) \bmod (1 - u^{m+1}),
  \qquad
  p_{m+1}(u) \;:=\; \frac{p_m(u) - a_m(u)}{1 - u^{m+1}}.
$$

The polynomial $1 - u^{m+1}$ is monic (up to sign), so polynomial
division in $\mathbb{Z}[u]$ produces $a_m \in \mathbb{Z}[u]$ of
degree $\leq m$ and a quotient $p_{m+1} \in \mathbb{Z}[u]$. This
gives **integrality** and the **degree bound**.

### Step 3: Termination

At each step $\deg p_{m+1} = \deg p_m - (m+1) + \deg a_m \leq
\deg p_m - 1$, so $\deg p_m$ is strictly decreasing in any step
producing a nonzero $a_m$. The process terminates after finitely
many steps. The total degree gain $\sum_{k=0}^m (k+1) =
\binom{m+2}{2}$ then gives $m_{\max} \leq \lceil \sqrt{2d} \rceil$
where $d = \deg p$.

### Step 4: Reconstruction and uniqueness

Unrolling the recursion gives
$p(u) = \sum_{m \leq m_{\max}} a_m(u)\,(u; u)_m$. For uniqueness,
at the smallest $m$ where $a_m \neq a_m'$ the polynomial
$a_m - a_m'$ would be divisible by $1 - u^{m+1}$, but
$\deg(a_m - a_m') \leq m < m+1 = \deg(1 - u^{m+1})$ — contradiction.
$\square$
