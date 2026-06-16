**Proposition (cyclotomic depth-$n$ generators decompose into
Dirichlet $L$-values).**

The cyclotomic $\mathrm{Cl}_n$ values established as a basis for the
genuinely-new depth-$n$ content over $\mathbb{Q}(\zeta_K)$ (Theorem G,
[`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths))
are $\mathbb{Q}$-linearly equivalent to **Dirichlet $L$-values** $L(\chi, n)$
for primitive Dirichlet characters $\chi$ mod $K$ with $\chi(-1) = (-1)^n$.

This bridges the graded-Mikusiński framework directly to classical
analytic number theory.

### Statement

For prime $K \geq 3$ and integer $n \geq 1$ with $n \equiv$ parity
matching the odd / even character class:

$$
  L(\chi, n) \;=\; \frac{G(\chi)}{K^n}\, \sum_{a = 1}^{K - 1} \overline{\chi(a)} \cdot \mathrm{Cl}_n(2\pi a/K),
$$

where $G(\chi) = \sum_{a = 1}^{K - 1} \chi(a) \zeta_K^a$ is the
Gauss sum.  Inverting via character orthogonality:

$$
  \mathrm{Cl}_n(2\pi a/K)
  \;=\;
  \frac{1}{\varphi(K)}\, \sum_\chi G(\overline{\chi}) \chi(a) \cdot \frac{K^n}{G(\chi)}\, L(\chi, n),
$$

i.e., **each $\mathrm{Cl}_n(2\pi a/K)$ is a $\mathbb{Q}(\zeta_K)$-linear
combination of $L(\chi, n)$ values** (and vice versa).

### Specific consequence: Catalan-like depth-3 L-value

**Theorem (instance verified at $N = 4$, $n = 3$):**

$$
  \boxed{\;
    \beta(3) \;=\; L(\chi_4, 3) \;=\; \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \frac{\pi^3}{32},
  \;}
$$

where $\chi_4$ is the non-trivial Dirichlet character mod 4
($\chi_4(1) = 1, \chi_4(3) = -1$) and $\beta$ is the Dirichlet beta
function.

**Constructive proof from Theorem A.**  By
[`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
at $(n, K) = (3, 4)$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_4) \;=\; \frac{(K - 1)(K - 2)\pi^3}{3 K^3}
  \;=\; \frac{3 \cdot 2 \cdot \pi^3}{3 \cdot 64} \;=\; \frac{\pi^3}{32}.
$$

Since $\zeta_4 = i$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \sum_{m=0}^{\infty} \frac{\sin((2m+1)\pi/2)}{(2m+1)^3}
  \;=\; \sum_{m=0}^{\infty} \frac{(-1)^m}{(2m+1)^3}
  \;=\; \beta(3).
$$

So $\beta(3) = \pi^3/32$ is a **corollary of Theorem A**.  Classical
result, derived constructively. $\square$

### Numerical verification at 50 dps

[`cl_n_l_value_decomposition.py`](https://github.com/litlfred/qou/blob/main/computations/cl_n_l_value_decomposition.py),
[witness](https://github.com/litlfred/qou/blob/main/computations/cl-n-l-value-decomposition.witness.json):

| Quantity | Value (50 dps) |
|---|---|
| $\mathrm{Im}\,\mathrm{Li}_3(i)$ (closed form $\pi^3/32$) | $0.96894614625937036181867968128\ldots$ |
| $\mathrm{Im}\,\mathrm{Li}_3(i)$ (direct polylog) | $0.96894614625937036181867968128\ldots$ |
| $\beta(3)$ (classical closed form) | same |
| Residual | $0$ (exact match) |

### N = 5 instance (Theorem G dim $(K - 3)/2 = 1$)

Cyclotomic depth-3 content over $\mathbb{Q}(\zeta_5)$:

- $\mathrm{Cl}_3(2\pi/5) \approx 0.18937$
- $\mathrm{Cl}_3(4\pi/5) \approx -0.76636$
- Genuinely-new generator $= \mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5) \approx 0.95572$

Corresponds, via the Hurwitz–Lerch decomposition, to the 2 odd
Dirichlet characters $\chi_5$, $\chi_5^3$ mod 5 (complex-conjugate
pair).  Modulo bar-conjugation: 1 real dimension. Matches Theorem G.

### Why this matters — Bridge to analytic number theory

The graded-Mikusiński framework's depth-$n$ cyclotomic content
**IS** the Dirichlet $L$-value content at integer $n$, up to
$\mathbb{Q}(\zeta_K)$-linear combinations.  This means:

1. **Classical L-value identities are theorems of our framework**:
   $\beta(3) = \pi^3/32$, $\beta(5) = 5\pi^5/1536$, $L(\chi_3, 3) = ?$,
   etc., all follow from Theorem A as instances.
2. **Conversely**: any new theorem we prove about cyclotomic depth-$n$
   structure (e.g., Theorem D dimension) gives a corresponding
   statement about Dirichlet L-values.
3. **Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ depth $n$** is
   the Beilinson conjecture on $L$-values of Dirichlet characters —
   a classical open problem now reframed as part of B1's discharge
   surface.

### Catalan's constant ($n = 2$ instance)

For $(n, K) = (2, 4)$ even case: Theorem A gives
$\mathrm{Re}\,\mathrm{Li}_2(i) = -\pi^2/48$ (Bernoulli $B_2(1/4) = -1/48$,
times $\pi^2 \cdot 2! / 2 = \pi^2$). And $\mathrm{Im}\,\mathrm{Li}_2(i) =
\mathrm{Cl}_2(\pi/2) = G$ — Catalan's constant.

$G$ is **not** Tate-rational (conjecturally transcendental); it's the
genuinely-new depth-2 generator over $\mathbb{Q}(i)$.  Matches Theorem G:
$(K - 1)/2 = (4 - 1)/2$ — but $K = 4$ is not prime; for prime $K = 3$:
dim 1 = $\mathrm{Cl}_2(2\pi/3)$ (Gieseking).

### Cross-references

- Theorem A: [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Theorem G: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Bloch–Suslin (depth-2 theorem):
  [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- K-theory $\leftrightarrow$ depth filtration: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
