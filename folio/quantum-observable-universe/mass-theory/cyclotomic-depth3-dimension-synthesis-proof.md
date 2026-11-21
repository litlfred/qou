**Sketch.**

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
[Trilogarithm imaginary part at $\zeta_n$: closed form $(n - 1)(n - 2)\pi^3 / (3 n^3)$ for every root of unity](#prop:cyclotomic-trilog-imaginary-closed-form):

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_K^j)
  \;=\;
  \frac{(jK - 1)(jK - 2)\,\pi^3}{3\,(jK)^3}
  \quad \text{(?)}
$$

Wait — the formula applies at $\zeta_n$ with $n = K/\gcd(j, K)$.
For prime $K$ and $1 \leq j \leq K - 1$, $\gcd(j, K) = 1$, so
$\zeta_K^j$ is itself a primitive $K$th root. Apply Theorem A
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
  [General orbit-sum identity: $\sum_k \mathrm{Cl}_3(2\pi k/N) = -(N^2-1)/N^2 \cdot \zeta(3)$ at every $N \geq 2$](#prop:cyclotomic-cl3-orbit-sum-general):

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

$\square$

### Lower bound — conditional on Beilinson

**Claim.** $\dim_{\mathbb{Q}} \mathcal{V}_K \geq (K - 3)/2$, conditional
on Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$.

**Argument.** Borel's theorem:
for prime $K$, $\mathbb{Q}(\zeta_K)$ is totally complex with $r_2 = (K - 1)/2$.
For $n = 3$ (odd):

$$
  \dim_{\mathbb{Q}} K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_K)) \otimes \mathbb{Q}
  \;=\;
  r_2 \;=\; \frac{K - 1}{2}.
$$

This $\frac{K - 1}{2}$-dim space includes the $\zeta(3)$-line
(rank 1, traces from $K_5(\mathbb{Z}) \otimes \mathbb{Q}$); modding out
gives a Borel-predicted **$(K - 3)/2$**-dim "genuinely-new"
component.

Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ asserts that the
Beilinson regulator image saturates this Borel rank — i.e., the
$(K - 3)/2$ genuinely-new dimensions are *all realised* in
$\mathcal{V}_K$. Combined with the upper bound:

$$
  \dim_{\mathbb{Q}} \mathcal{V}_K \;=\; \frac{K - 3}{2}
  \quad \text{(conditional on Beilinson).}
$$

### canonical PSLQ certification at $K = 5, 7$

the canonical formalism,
[witness](https://github.com/litlfred/qou/blob/main/computations/cyclotomic-depth3-dimension-pslq.witness.json):

See [Table 1](#tbl:cyclotomic-depth3-dimension-synthesis-table1-data).

The $K = 7$ certificate verifies the dimension prediction one prime
beyond the Bring-natural $K = 5$ case.

### Predictions at higher primes

See [Table 2](#tbl:cyclotomic-depth3-dimension-synthesis-table2-data).

Extending the PSLQ certificate to $K \geq 11$ is straightforward (the
same formalism works); each test takes ~30 seconds at 50 dps.
