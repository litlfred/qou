### Proof

**Step 1 (Kummer reflection).** For $z \notin (0, 1)$ (Lewin 1991,
Eq. 6.10):

$$
  \mathrm{Li}_3(z) - \mathrm{Li}_3(1/z)
  \;=\;
  -\frac{\log^3(-z)}{6} - \frac{\pi^2 \log(-z)}{6}.
$$

**Step 2 (principal log of $-\zeta_n$).** For $n \geq 2$, $\zeta_n =
e^{2\pi i/n}$ and

$$
  -\zeta_n \;=\; e^{i (2\pi/n + \pi)}
  \;=\; e^{i\,\theta_n}, \quad \theta_n := 2\pi/n + \pi.
$$

Since $\theta_n > \pi$ for $n \geq 2$, the principal branch gives

$$
  \log(-\zeta_n) \;=\; i\,(\theta_n - 2\pi)
  \;=\; i\pi \cdot \frac{2 - n}{n}.
$$

(For $n = 1$, $\zeta_1 = 1$ and $\mathrm{Li}_3(1) = \zeta(3)$ is real,
so $\mathrm{Im}\,\mathrm{Li}_3(\zeta_1) = 0$ — consistent with the
formula at $n = 1$: $(0)(-1) = 0$.)

**Step 3 (substitute and simplify).** Write $\alpha := (2 - n)/n$, so
$\log(-\zeta_n) = i\pi\alpha$ and $\log^3(-\zeta_n) = -i\pi^3\alpha^3$.

$$
  \begin{aligned}
    -\frac{\log^3(-\zeta_n)}{6} - \frac{\pi^2 \log(-\zeta_n)}{6}
    &\;=\;
    \frac{i\pi^3\alpha^3}{6} - \frac{i\pi^3\alpha}{6} \\
    &\;=\;
    \frac{i\pi^3 \alpha (\alpha^2 - 1)}{6}.
  \end{aligned}
$$

Since $\mathrm{Li}_3(\zeta_n^{-1}) = \overline{\mathrm{Li}_3(\zeta_n)}$:

$$
  \mathrm{Li}_3(\zeta_n) - \mathrm{Li}_3(\zeta_n^{-1})
  \;=\; 2 i\,\mathrm{Im}\,\mathrm{Li}_3(\zeta_n).
$$

Therefore

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_n)
  \;=\; \frac{\pi^3 \alpha (\alpha^2 - 1)}{12}.
$$

**Step 4 (factor in $n$).** With $\alpha = (2-n)/n$:

$$
  \alpha^2 - 1 \;=\; \frac{(2-n)^2 - n^2}{n^2} \;=\; \frac{4 - 4n}{n^2}
  \;=\; \frac{-4(n-1)}{n^2}.
$$

So

$$
  \alpha(\alpha^2 - 1)
  \;=\; \frac{2-n}{n} \cdot \frac{-4(n-1)}{n^2}
  \;=\; \frac{4(n-1)(n-2)}{n^3}.
$$

Substituting:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_n)
  \;=\; \frac{\pi^3}{12} \cdot \frac{4(n-1)(n-2)}{n^3}
  \;=\; \frac{(n-1)(n-2)\,\pi^3}{3\,n^3}.
$$

$\square$

### Verifications

Substituting into the closed form:

See [Table](#tbl:cyclotomic-trilog-imaginary-closed-form-table-data).

The $n = 5$ row recovers
[Trilogarithm imaginary part at $\zeta_5$](#prop:bring-trilog-imaginary-tate-rational)'s
$4\pi^3/125$ as a special case.
