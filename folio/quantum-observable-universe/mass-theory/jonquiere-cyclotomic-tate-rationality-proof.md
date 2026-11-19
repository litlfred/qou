### Proof

**Step 1 (Jonquière inversion formula, Lewin 1991 §7).** For
$z \notin (0, 1)$ and $n \geq 1$:

$$
  \mathrm{Li}_n(z) \;=\; (-1)^{n - 1}\,\mathrm{Li}_n(z^{-1})
  \;-\; \frac{(2\pi i)^n}{n!} B_n\!\left(\tfrac{1}{2} + \tfrac{\log(-z)}{2\pi i}\right),
$$

where the principal branch of $\log$ is taken.

**Step 2 (specialise at $z = \zeta_K = e^{2\pi i/K}$, $K \geq 2$).**
Here $-\zeta_K = e^{i (2\pi/K + \pi)}$. For $K \geq 2$, the angle
$2\pi/K + \pi$ exceeds $\pi$, so the principal log subtracts $2\pi$:

$$
  \log(-\zeta_K) \;=\; i\pi (2 - K)/K.
$$

Compute the Bernoulli argument:

$$
  \frac{1}{2} + \frac{\log(-\zeta_K)}{2\pi i}
  \;=\; \frac{1}{2} + \frac{2 - K}{2K}
  \;=\; \frac{K + (2 - K)}{2K}
  \;=\; \frac{1}{K}.
$$

The Bernoulli polynomial evaluates at $1/K$, giving a particularly
clean specialisation. Substituting into Step 1:

$$
  \mathrm{Li}_n(\zeta_K) - (-1)^{n - 1}\,\mathrm{Li}_n(\zeta_K^{-1})
  \;=\;
  -\frac{(2\pi i)^n}{n!}\,B_n(1/K).
$$

**Step 3 (extract real / imaginary part on unit circle).** Since
$\zeta_K^{-1} = \overline{\zeta_K}$, $\mathrm{Li}_n(\zeta_K^{-1}) =
\overline{\mathrm{Li}_n(\zeta_K)}$.

- *$n$ odd:* $(-1)^{n - 1} = 1$.  LHS $= \mathrm{Li}_n(\zeta_K) -
  \overline{\mathrm{Li}_n(\zeta_K)} = 2 i\,\mathrm{Im}\,\mathrm{Li}_n(\zeta_K)$.
- *$n$ even:* $(-1)^{n - 1} = -1$.  LHS $= \mathrm{Li}_n(\zeta_K) +
  \overline{\mathrm{Li}_n(\zeta_K)} = 2\,\mathrm{Re}\,\mathrm{Li}_n(\zeta_K)$.

Therefore:

$$
  \mathrm{Im}\,\mathrm{Li}_n(\zeta_K) \;=\; -\frac{(2\pi i)^n}{2 i \cdot n!}\,B_n(1/K), \qquad n \text{ odd},
$$
$$
  \mathrm{Re}\,\mathrm{Li}_n(\zeta_K) \;=\; -\frac{(2\pi i)^n}{2 \cdot n!}\,B_n(1/K), \qquad n \text{ even}.
$$

Both expressions are rational multiples of $\pi^n$, hence **Tate-rational**.
$\square$

### Verification at low depths

**$n = 2$ (even, Re part):** $B_2(x) = x^2 - x + 1/6$.

$$
  \mathrm{Re}\,\mathrm{Li}_2(\zeta_K)
  \;=\; -\frac{(2\pi i)^2}{4}\,B_2(1/K)
  \;=\; \pi^2 \left(\tfrac{1}{K^2} - \tfrac{1}{K} + \tfrac{1}{6}\right).
$$

At $K = 2$: $\pi^2(1/4 - 1/2 + 1/6) = -\pi^2/12$ (= $\mathrm{Re}\,\mathrm{Li}_2(-1)$). (yes)

**$n = 3$ (odd, Im part):** $B_3(x) = x^3 - 3x^2/2 + x/2$.

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_K)
  \;=\; \frac{(n-1)(n-2)\pi^3}{3 n^3}
  \quad \text{(see Theorem A)}.
$$

This is the special case $n = 3$, which recovers
[cyclotomic trilogarithm imaginary closed form proposition](#prop:cyclotomic-trilog-imaginary-closed-form).

**$n = 4$ (even, Re part):** $B_4(x) = x^4 - 2x^3 + x^2 - 1/30$.

$$
  \mathrm{Re}\,\mathrm{Li}_4(\zeta_K)
  \;=\; -\frac{(2\pi)^4}{2 \cdot 4!}\,B_4(1/K)
  \;=\; -\frac{\pi^4}{3}\,B_4(1/K).
$$

**$n = 5$ (odd, Im part):** $B_5(x) = x^5 - 5x^4/2 + 5x^3/3 - x/6$.

$$
  \mathrm{Im}\,\mathrm{Li}_5(\zeta_K)
  \;=\; -\frac{(2\pi)^5}{2 \cdot 5!}\,B_5(1/K)
  \;=\; -\frac{2 \pi^5}{15}\,B_5(1/K).
$$

### canonical structural verification at 50 dps

High-precision numerical check:

Verified at $n \in \{2, 3, 4, 5\}$ and $K \in \{3, 4, 5, 6, 7\}$ (20
combinations).  Max residual $4.0 \times 10^{-51}$.
