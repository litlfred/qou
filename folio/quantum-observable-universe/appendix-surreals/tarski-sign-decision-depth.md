Let $K$ be any ordered field and let $\alpha \in K$ be a root of a rational polynomial $p$. Follow $\alpha$ through Conway's sign-expansion recipe: start at $0$; at each step compare $\alpha$ with the current dyadic value $v$, take the sign $+$ if $v < \alpha$ and $-$ otherwise, and move to the next dyadic of Gonshor's construction. After $n$ signs, $\alpha$ lies in a dyadic window $\ell_n < \alpha \le h_n$ whose endpoints are born by day $n$.

**Proposition.** Let $f \in \mathbb{Q}[x]$.

1. *(Each sign is a finite rational check.)* If $p$ has no zero on the half-window that does not contain $\alpha$, the next sign is determined. A certificate is a Bernstein form $\sum_{i \le d} c_i (x - a)^i (b - x)^{d-i}$ of $\pm p$ on $[a, b]$ with $c_i \ge 0$ and $c_0, c_d > 0$ (or a Taylor shift $\sum c_i (x - m)^i$ on a half-line). Checking it is a polynomial identity and finitely many inequalities between rationals.
2. *(Decision.)* If $f$ has such a certificate on $[\ell_n, h_n]$, then $0 < f(\alpha)$. The least such $n$ is the **decision depth** of the claim: the birthday of the coarsest dyadic window that decides it.
3. *(Locatedness without an axiom.)* Once both $\ell_n$ and $h_n$ exist, each further sign halves the window. So the cut of $\alpha$ by its windows is located in any Archimedean $K$: the Lawvere condition $\mathrm{coev} = 0$ holds as a theorem for finite-$N$ algebraic quantities.

Nothing here uses the intermediate value theorem, a real closed field, or the hypothesis that every observable is located: $\alpha$ is given, and only its location is refined.

**Birthdays grade windows, not numbers.** An irrational algebraic number, like every non-dyadic real, is born on day $\omega$, so the birthday cannot measure the complexity of $\alpha$ itself. It does measure the finite part of the sign expansion that a given claim reads, and that is a natural number.

**The embedding is a sign prefix.** For $c = \zeta_N + \zeta_N^{-1}$, the choice $\zeta_N = e^{2\pi i/N}$ is the choice of the largest root of the minimal polynomial $\Psi_N$ of $c$. That choice is the shortest sign prefix whose window holds no other root of $\Psi_N$ (the *embedding depth*). It is finite rational data; no cosine and no $\pi$ enter.

**Example: the figure-eight knot.** With $C_j(c) = q^j + q^{-j}$ written as a polynomial in $c = q + q^{-1}$, the Kashaev invariant is

$$
\langle 4_1 \rangle_N \;=\; \sum_{k=0}^{N-1} \prod_{j=1}^{k} \bigl(2 - C_j(c)\bigr) \;=\; \sum_{k=0}^{N-1} (q;q)_k\,(q^{-1};q^{-1})_k ,
$$

an element of $\mathbb{Z}[c]/(\Psi_N)$. For example $\langle 4_1 \rangle_5 = 48 + 4c$ and $\langle 4_1 \rangle_7 = 103 + 25c + 11c^2$. Deciding $\lfloor \langle 4_1 \rangle_N \rfloor$ gives:

| $N$ | $\deg \Psi_N$ | embedding depth | decision depth | $\lfloor \langle 4_1 \rangle_N \rfloor$ |
|---|---|---|---|---|
| 3 | 1 | 0 | 0 | 13 |
| 4 | 1 | 0 | 0 | 27 |
| 5 | 2 | 2 | 6 | 50 |
| 6 | 1 | 0 | 0 | 89 |
| 7 | 3 | 3 | 10 | 151 |
| 8 | 2 | 3 | 9 | 250 |
| 9 | 3 | 3 | 12 | 407 |
| 10 | 2 | 3 | 13 | 651 |
| 11 | 5 | 3 | 15 | 1030 |
| 12 | 2 | 3 | 12 | 1610 |
| 13 | 6 | 4 | 17 | 2495 |
| 14 | 3 | 3 | 17 | 3835 |
| 15 | 4 | 4 | 18 | 5855 |
| 16 | 4 | 3 | 18 | 8883 |

For $\deg \Psi_N = 1$ the value is rational and nothing needs deciding. The floors give the chain $\langle 4_1 \rangle_3 < \langle 4_1 \rangle_4 < \dots < \langle 4_1 \rangle_{16}$, a comparison between elements of different fields $\mathbb{Q}(\zeta_N)^+$ made through integer separators. Every entry is a sorry-free Lean theorem over an arbitrary ordered field.

**Scope.** These are finite-$N$ statements. The limit $N \to \infty$, where $\frac{2\pi}{N}\log\langle 4_1\rangle_N$ is conjectured to tend to the hyperbolic volume, is not decided this way; it stays a locatedness claim on the single non-constructive hypothesis of the Lawvere cut framework.
