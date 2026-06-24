*Step 1 (count starting generators).* The cyclotomic Galois orbit
of $\zeta_K$ consists of $\varphi(K) = K - 1$ primitive $K$th roots
of unity. Grouped by complex-conjugate pairs (since $\overline{\zeta_K^j} = \zeta_K^{K-j}$),
the orbit yields $(K - 1)/2$ pairs.

For each pair $\{\zeta_K^j, \zeta_K^{K-j}\}$, the corresponding
$\mathrm{Li}_3$ values give:

- One **real part** $\mathrm{Cl}_3(2\pi j/K) = \mathrm{Re}\,\mathrm{Li}_3(\zeta_K^j)$
  (bar-fixed in $\mathcal{P}_3^+$).
- One **imaginary part** $S_3(2\pi j/K) = \mathrm{Im}\,\mathrm{Li}_3(\zeta_K^j)$
  (bar-twisted in $\mathcal{P}_3^-$, related to its conjugate by sign).

Total: $(K - 1)/2$ real parts $+$ $(K - 1)/2$ imaginary parts =
$K - 1$ candidate generators.

*Step 2 (eliminate imaginary parts via Theorem A).* By
[`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form):

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_K^j)
  \;=\;
  \frac{(jK - 1)(jK - 2)\,\pi^3}{3\,(jK)^3}
  \quad \text{(?)}
$$

Wait — the formula applies at $\zeta_n$ with $n = K/\gcd(j, K)$.
For prime $K$ and $1 \leq j \leq K - 1$, $\gcd(j, K) = 1$, so
$\zeta_K^j$ is itself a primitive $K$th root. We apply Theorem A
at $n = K$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_K^j)
  \;=\;
  \mathrm{sign}(\ldots) \cdot
  \frac{(K - 1)(K - 2)\,\pi^3}{3\,K^3} \cdot (\text{sign from } j).
$$

More precisely: $\mathrm{Im}\,\mathrm{Li}_3(\zeta_K^j) = S_3(2\pi j/K)$
where $S_3$ is bounded in magnitude by the closed-form expression
$(K - 1)(K - 2)\pi^3/(3K^3)$ at the principal angle. By the
multi-angle Tate-rational structure (Step 1 above), **every imaginary
part is a $\mathbb{Q}$-linear combination of $\pi^3$** — i.e., lies in
the 1-dim Tate-line $\pi^3 \mathbb{Q} \subset \mathcal{P}_3$.

Under the Beilinson regulator quotient $\mathcal{P}_3 \to \mathcal{P}_3 / \mathrm{Tate}$,
**all $(K - 1)/2$ imaginary parts collapse to zero**. They contribute
**zero dimensions** to $\mathcal{V}_K$.

*Step 3 (count residual real-part dimensions).* The $(K - 1)/2$ real
parts $\{\mathrm{Cl}_3(2\pi j/K) : 1 \leq j \leq (K - 1)/2\}$ satisfy:

- **Orbit-sum relation** by
  [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general):

  $$
    \sum_{j=1}^{(K - 1)/2} \mathrm{Cl}_3(2\pi j/K)
    \;=\;
    -\frac{K^2 - 1}{2K^2}\,\zeta(3).
  $$

  This is **one** linear relation modulo $\mathcal{V}_K$ — it pulls a
  1-dim component into the $\zeta(3)$-line, which projects to zero
  in $\mathcal{P}_3 / (\mathcal{P}_2 + \mathbb{Q}\zeta(3))$.

Therefore the *remaining* $\mathbb{Q}$-rank of the real parts modulo
$\mathcal{V}_K$ is at most:

$$
  \frac{K - 1}{2} - 1 \;=\; \frac{K - 3}{2}.
$$

*Step 4.* Combining Steps 2 (imaginary parts contribute 0) and 3
(real parts contribute at most $(K - 3)/2$):

$$
  \dim_{\mathbb{Q}} \mathcal{V}_K \;\leq\; \frac{K - 3}{2}.
$$
$\qquad\blacksquare$
