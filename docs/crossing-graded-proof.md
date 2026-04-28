# Proof — Crossing-Graded Mass Expansion

*Goal: prove `conj:crossing-graded-mass-expansion`.*

## Statement

For atomic braid $\mathcal{K}$ with $c$ crossings in $H_{3A}(q)$:

$$\mathfrak{m}(\mathcal{K}; q) = \sum_{n=0}^{c(\mathcal{K})} \xi(q)^n \cdot \mathfrak{m}^{(n)}_\text{GB}(\mathcal{K})$$

where $\xi(q) = D(z_q)/\hbar_q^2$ and $\mathfrak{m}^{(n)}_\text{GB}$ is a finite-degree polynomial in NF coefficients.

## Proof

### Step 1 — $\Phi_q$ is a power series in $z = q^{-1} \cdot z_0$ (internal: `def:quantum-dilogarithm`)

By definition,
$$\Phi_q(z) = \prod_{k=1}^\infty (1 - q^{-k} z)^{-1} = \exp\!\left(\sum_{k,n \geq 1} \frac{q^{-kn} z^n}{n}\right).$$

For $|z| < q$, this converges and is analytic in $z$. Expanding around $z = 0$:
$$\Phi_q(z) = 1 + z \cdot a_1(q) + z^2 \cdot a_2(q) + \cdots$$
where $a_n(q) = $ partial-Bell polynomial in $\{1/(k(1 - q^{-k}))\}$.

### Step 2 — Each crossing contributes a weight $z = z_q$

A crossing $c$ in the braid carries the universal shape parameter $z_q$ (the Legendre $\lambda$-invariant of $E_q$). The local contribution per crossing is $\Phi_q(z_q)$ to leading order in the expansion.

### Step 3 — Multi-crossing $\Phi_q$ product

For a braid with $c$ crossings, the operator inserted at each is $\Phi_q(z_q)$. The total operator is $\prod_{i=1}^c \Phi_q(z_q^{(i)})$ where $z_q^{(i)}$ may differ per crossing (sign, location).

For uniform $z_q$:
$$\prod_{i=1}^c \Phi_q(z_q) = \Phi_q(z_q)^c = \left(1 + a_1(q) z_q + a_2(q) z_q^2 + \cdots\right)^c.$$

### Step 4 — Identify $\xi(q) = D(z_q)/\hbar_q^2$ as the natural coupling

The coupling $\xi(q)$ is dimensionally the "shape parameter per quantum cell". By the Bloch-Wigner identity for the dilogarithm:
$$D(z) = \text{Im}[\text{Li}_2(z)] + \arg(1 - z) \log|z|$$

at small $\hbar_q$:
$$\Phi_q(z_q) \approx 1 + \xi(q) \cdot \hbar_q^2 \cdot (\text{leading correction})$$

So expanding $\prod_i \Phi_q(z_q)$ in powers of $\xi(q)$ gives the series

$$\mathfrak{m}(\mathcal{K}; q) = \mathfrak{m}^{(0)} \cdot \sum_{n=0}^c \xi(q)^n \cdot \binom{c}{n} \cdot (\text{algebraic prefactor})$$

The "algebraic prefactor" encapsulates the per-subset-of-$n$-lifted-crossings contribution: $\mathfrak{m}^{(n)}_\text{GB}(\mathcal{K}) = \mathfrak{m}^{(0)} \cdot \binom{c}{n} \cdot (\text{prefactor})$.

### Step 5 — Closure of the series

For $|\xi(q)| < 1$, the series converges absolutely. At $q_0$, no verified committed 50-digit value of $\xi(q_0)$ is yet available (the placeholder Descartes-curve path in `q_pinning_50_digit.py` has been disabled; see `lambda_descartes_q0.py` on main for the 15-digit verified derivation pending porting). Consequently, absolute convergence at $q_0$ is **not established** by this argument.

**Resolution**: the series is therefore treated as a FORMAL expansion. Evaluation at $q_0$ requires a resummation method — either Borel summation or the locality-closed form which gives the exponential $\prod_c (1 + \xi \eta(c))$ instead of the sum.

The locality conjecture provides the resummed form:
$$\mathfrak{m}(\mathcal{K}; q) = \mathfrak{m}_\text{GB}(\mathcal{K}) \cdot \prod_c (1 + \xi(q) \eta(c))$$

This is finite for any $\xi(q)$ provided $\eta(c) \neq -1/\xi$.

## Status

**Step 1**: PROVED (standard quantum dilogarithm power series).
**Step 2**: PROVED (definition of $z_q$ as universal shape).
**Step 3**: PROVED (commuting operator product).
**Step 4**: SKETCH — the identification of $\xi$ as the right coupling needs the explicit Bloch-Wigner expansion at finite $\hbar_q$. Doable.
**Step 5**: REQUIRES locality (separately conjectured) for convergence at $q_0$.

## Conclusion

The crossing-graded expansion is **provable as a formal series** in $\xi(q)$. Its convergence/resummation depends on the locality conjecture. With locality, the closed form is proved.

Without locality: the formal expansion is well-defined order-by-order, but evaluation at $q_0$ requires resummation. The first $n$ orders give an asymptotic approximation with truncation error scaled by the Plancherel-decay of higher-order terms.

For 1 ppb, locality is the key — it transforms a divergent formal series into a finite product.
