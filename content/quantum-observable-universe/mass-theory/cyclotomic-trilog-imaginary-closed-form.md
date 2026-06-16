**Proposition (general closed form for $\mathrm{Im}\,\mathrm{Li}_3$ at
every root of unity).**

The Kummer reflection formula
([`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
established the closed form at $\zeta_5$.  *This proposition
generalises to **all** $n \geq 1$:*

$$
  \boxed{\;
    \mathrm{Im}\,\mathrm{Li}_3(\zeta_n)
    \;=\;
    \frac{(n - 1)(n - 2)\,\pi^3}{3\,n^3}.
  \;}
$$

*In particular, $\mathrm{Im}\,\mathrm{Li}_3(\zeta_n)$ is **Tate-rational**
for every $n$ — lies in $\pi^3 \mathbb{Q}$ — and therefore projects
to zero under the Beilinson regulator quotient
$\mathcal{P}_3 \to \mathcal{P}_3 / \mathrm{Tate}$.*

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
[`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)'s
$4\pi^3/125$ as a special case.

### Significance

**Generalises round 10 of ** from "$\zeta_5$ only" to "every
root of unity". Concretely:

1. **Every cyclotomic depth-3 imaginary part is Tate-rational** —
   lives in $(2\pi i)^3 \mathbb{Q} = -\pi^3 \mathbb{Q}$ (up to a
   factor of $i$).
2. **Projects to zero under Beilinson regulator quotient** — the
   genuinely-new content at $\zeta_n$ over $\mathbb{Q}(\zeta_n)$ at
   depth 3 lives **entirely in the real part** $\mathrm{Cl}_3(2\pi/n)$
   and its Galois conjugates, not in $\mathrm{Im}\,\mathrm{Li}_3$.
3. **Reduces the depth-3 surface for every cyclotomic field** to the
   real-part Galois orbit, halving the dimension at the outset.

### Asymptotic behaviour

The formula reveals the asymptotic:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_n) \;=\; \frac{\pi^3}{3 n} + O(n^{-2})
$$

as $n \to \infty$.  Decays like $1/n$, with leading coefficient $\pi^3/3$.

### Cross-references

- Special case $n = 5$ (round 10 of ):
  [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- Related orbit-sum:
  [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- Numerical witness (verified at $n = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
  [`cyclotomic-trilog-imaginary.witness.json`](https://github.com/litlfred/qou/blob/main/computations/cyclotomic-trilog-imaginary.witness.json)
- Geometric realisation question:
  [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
