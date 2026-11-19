## Proof sketch

### Step 1: bar involution and the averaged crossing

The Hecke algebra $H_n(q)$ carries the **bar involution** $\overline{\,\,}$,
a $\mathbb{Z}$-linear anti-ring-automorphism defined by:
$$
\overline{q} = q^{-1}, \quad \overline{\sigma_i} = \sigma_i^{-1}.
$$

Using the Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ (where $h = q - q^{-1}$)
gives $\sigma_i^{-1} = \sigma_i - h$.

The **bar-invariant projector** is $P_{\text{avg}} = (1 + \overline{\,\,})/2$.
Its action on $\sigma_i$ gives:
$$
P_{\text{avg}}(\sigma_i) \;=\; \frac{\sigma_i + \overline{\sigma_i}}{2}
\;=\; \frac{\sigma_i + \sigma_i^{-1}}{2}
\;=\; \frac{\sigma_i + \sigma_i - h}{2}
\;=\; \sigma_i - \frac{h}{2}.
$$

This is the **averaged crossing operator** $\sigma_{\text{avg}}$ used
in the typed-$\mathbf{B}_3$ braid recipe.

### Step 2: averaged crossings in the typed braid

From the [symbolic neutron $Q$-value proposition](#prop:neutron-qvalue-symbolic),
the typed-$\mathbf{B}_3$ proton braid uses ONE averaged $\sigma_1$:
$$
\mathcal{B}_p \;=\; \sigma_0 \cdot (\sigma_1 - \tfrac{h}{2}\mathbf{1})
\;=\; \sigma_0 \cdot \sigma_{1,\text{avg}}.
$$

The typed neutron braid uses TWO averaged crossings (one at $\sigma_0$,
one at $\sigma_1$):
$$
\mathcal{B}_n \;=\; (\sigma_0 - \tfrac{h}{2}\mathbf{1}) \cdot (\sigma_1 - h\mathbf{1})
\;=\; \sigma_{0,\text{avg}} \cdot \sigma_1^{-1}.
$$

Each averaged crossing contributes a factor of $h/2 = 1/2$ at the
specific position where it appears.

### Step 3: Leibniz propagation to higher rungs

The categorical Markov-trace expansion of the typed braid in powers
of $h$ generates the single-wrap baseline (Form A) plus the
precision-ladder corrections. The $h/2$ contributions from averaged
positions propagate via the **Leibniz product expansion**:

$$
\mathrm{tr}_M(\mathcal{B}_n - \mathcal{B}_p) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\; \frac{h^2}{2} - h
\;=\; \frac{h(h-2)}{2}.
$$

The $h^2/2$ term is the product of TWO averaged-crossing $h/2$
contributions (the neutron has two such positions). The $h/2$
generates the $1/2$ in $\Delta(\mathrm{net})$.

For higher rungs $N = k \geq 4$ of the precision ladder, the
expansion of $\mathrm{tr}_M(T_\beta)$ in $b \cdot \hbar_q^2$ produces
coefficients with two distinct categorical origins:

- **Pure-$\sigma$ contributions**: from non-averaged positions in
  the braid. These factor through $\sigma^p \cdot b^{2m}$
  combinatorics. At the silver ratio ($\sigma$-eigenvalues
  $= 1 \pm \sqrt{2}$ via the Hecke quadratic in the
  [silver-ratio $\beta$-decay null proposition](#prop:silver-ratio-beta-decay-null)),
  these reduce to **Pell-Lucas-clean** rationals.

- **Averaged-crossing contributions**: from positions where $\sigma_{\text{avg}}$
  acts. These pick up the $1/2$ fingerprint of $P_{\text{avg}}$. At
  the silver ratio they give rationals with a $1/2$ component that
  is **Pell-Lucas-incompatible**.

### Step 4: rung-by-rung classification

Sequential extraction of $c_k$ via $R(q_0) = \prod_k (1 + c_k b^k \hbar_q^{2k})$
gives:

| $c_k$ | Closed form | Origin | At silver ratio |
|:----:|:-----------:|:-------|:-------|
| $c_3$ | $-2$ | $J_{\text{Hopf}}(q=1)$, pure inter-block | $-2$ (clean) |
| $c_4$ | $c_3 \cdot b^4$ | $\sigma^p \cdot b^{2m}$ pure | $-49/32 = -a_3^2/2^5$ (clean) |
| $c_5$ | $\boxed{-b^2 - 1/2}$ | $\sigma$ + averaging | $-11/8$ (1/2 OUTLIER) |
| $c_6$ | $c_3^2 \cdot b^2$ | $\sigma^p \cdot b^{2m}$ pure | $7/2 = a_3/2$ (clean) |
| $c_7$ | $c_3^3$ | pure $\sigma$ powers | $-8$ (clean integer) |

The $c_5$ outlier is **structurally distinct** because $\sigma_{\text{avg}}$
contributions at rung $5$ are dominant — at all other rungs in
$[3, 7]$, the pure-$\sigma$ contributions dominate and the
averaging contributions are subdominant. □

## Algebraic identities and real-analytic bounds for $c_5$

### Hoefsmit–Quantum-2 identity

**Theorem.** For all $q \neq 0$ in $\mathbb{R}$,

$$b^2(q) \;=\; \frac{q^4 + q^2 + 1}{(q^2 + 1)^2} \;=\; 1 - \frac{1}{[2]_q^2}.$$

*Proof.* Multiply both sides by $[2]_q^2 = (q + q^{-1})^2$:
$(q^2 + 1)^2 = q^2 \cdot (q + q^{-1})^2$ since $(q+q^{-1})^2 = (q^2+1)^2/q^2$. So $b^2 = (q^4+q^2+1)/(q^2[2]_q^2)$. Multiplying numerator and denominator of $b^2$ by $1/q^2$ gives $b^2 = (q^2 + 1 + q^{-2})/[2]_q^2 = ([2]_q^2 - 1)/[2]_q^2 = 1 - 1/[2]_q^2$ since $q^2 + 1 + q^{-2} = (q+q^{-1})^2 - 1 = [2]_q^2 - 1$. $\square$

**Corollary.** $c_5(q) = -3/2 + 1/[2]_q^2$.
*Proof.* Substitute $b^2 = 1 - 1/[2]_q^2$ into $c_5 = -b^2 - 1/2$:
$c_5 = -(1 - 1/[2]_q^2) - 1/2 = -3/2 + 1/[2]_q^2$. $\square$

### Classical-QOU limit and Wedderburn identification

**Theorem.** $c_5(q = 1) = -5/4$.
*Proof.* At $q = 1$: $[2]_q = 2$, so $[2]_q^2 = 4$, $1/[2]_q^2 = 1/4$, and $c_5(1) = -3/2 + 1/4 = -5/4$. $\square$

**Theorem.** $c_5(1) = -(\dim V_{(3)} + \dim V_{(2,1)})/2 + 1/4 = -5/4$.
*Proof.* The Wedderburn decomposition of $\mathbb{C}[S_3]$ has three irreps with dimensions $1$ ($V_{(3)}$), $2$ ($V_{(2,1)}$), and $1$ ($V_{(1,1,1)}$). The non-sign sum is $1 + 2 = 3$; half is $3/2$. So $-3/2 = -(\dim V_{(3)} + \dim V_{(2,1)})/2$, which combines with $1/4 = 1/[2]_q^2$ at $q=1$ to give $-5/4$. $\square$

### Silver-ratio identity

**Lemma.** $[2]_q^2 = 8$ at $q = 1 + \sqrt 2$.
*Proof.* $[2]_{1+\sqrt 2} = (1+\sqrt 2) + 1/(1+\sqrt 2) = (1+\sqrt 2) + (\sqrt 2 - 1) = 2\sqrt 2$, hence $[2]_q^2 = 8$. $\square$

**Theorem.** $b^2(1 + \sqrt 2) = 7/8$.
*Proof.* Combining the Hoefsmit–Quantum-2 identity with the lemma above gives $b^2 = 1 - 1/[2]_q^2 = 1 - 1/8 = 7/8$. $\square$

**Corollary.** $c_5(1 + \sqrt 2) = -11/8$.
*Proof.* Substituting $[2]_q^2 = 8$ into $c_5 = -3/2 + 1/[2]_q^2$ gives $c_5 = -3/2 + 1/8 = -12/8 + 1/8 = -11/8$. The numerator $11$ is **inert** in $\mathbb{Z}[1+\sqrt 2]$ (outside the Pell-Lucas closure) — the $c_5$ outlier fingerprint. $\square$

### Expression in terms of the Hecke skein $h$

**Lemma.** For all $q \neq 0$,
$[2]_q^2 = h^2 + 4$ where $h = q - q^{-1}$.
*Proof.* $(q + q^{-1})^2 = q^2 + 2 + q^{-2}$ and $(q - q^{-1})^2 + 4 = (q^2 - 2 + q^{-2}) + 4 = q^2 + 2 + q^{-2}$. $\square$

**Theorem.** $c_5(q) = -3/2 + 1/(h^2 + 4)$ where $h = q - q^{-1}$.
*Proof.* Substitute $[2]_q^2 = h^2 + 4$ into $c_5 = -3/2 + 1/[2]_q^2$. $\square$

### Rational map properties over $\mathbb{R}$

Define the rational map $\widetilde{c}_5(h) := -3/2 + 1/(h^2 + 4)$ for $h \in \mathbb{R}$.

**Proposition.** $\widetilde{c}_5(h(q)) = c_5(q)$ for all $q \neq 0$.
*Proof.* Direct from the skein formula $c_5(q) = -3/2 + 1/(h^2 + 4)$. $\square$

**Proposition.** $h^2 + 4 > 0$ (and hence $h^2 + 4 \neq 0$) for all $h \in \mathbb{R}$.
*Proof.* Since $h^2 \geq 0$, $h^2 + 4 \geq 4 > 0$. $\square$

**Proposition.** Concrete evaluations: $\widetilde{c}_5(0) = -5/4$, $\widetilde{c}_5(2) = -11/8$, and $\widetilde{c}_5(1) = -13/10$.
*Proof.* Direct rational arithmetic at $h = 0, 2, 1$. $\square$

**Theorem.** $\widetilde{c}_5(-h) = \widetilde{c}_5(h)$ (even function).
*Proof.* Since $(-h)^2 = h^2$, $\widetilde{c}_5$ is invariant under the bar action $h \mapsto -h$. $\square$

**Theorem.** $\widetilde{c}_5(h) \leq -5/4$ for all $h \in \mathbb{R}$, with equality at $h = 0$.
*Proof.* From $h^2 + 4 \geq 4$ it follows that $1/(h^2 + 4) \leq 1/4$, hence $\widetilde{c}_5(h) = -3/2 + 1/(h^2+4) \leq -3/2 + 1/4 = -5/4$. $\square$

**Theorem.** $\widetilde{c}_5(h) > -3/2$ for all $h \in \mathbb{R}$.
*Proof.* Since $1/(h^2 + 4) > 0$, $\widetilde{c}_5(h) > -3/2$, approached asymptotically as $|h| \to \infty$. $\square$

**Theorem.** $\widetilde{c}_5(h) < 0$ for all $h \in \mathbb{R}$.
*Proof.* Immediate from $\widetilde{c}_5(h) \leq -5/4 < 0$. $\square$

**Theorem.** $h = 0$ achieves the global maximum of $\widetilde{c}_5$ on $\mathbb{R}$.
*Proof.* Combine $\widetilde{c}_5(h) \leq -5/4$ with $\widetilde{c}_5(0) = -5/4$. $\square$

**Theorem.** As a function of $u = h^2 \geq 0$, $\widehat{c}_5(u) := -3/2 + 1/(u + 4)$ is monotonically decreasing on $[0, \infty)$.
*Proof.* For $0 \leq x \leq y$, both $x+4$ and $y+4$ are positive with $y + 4 \geq x + 4$, so $1/(y+4) \leq 1/(x+4)$ and $\widehat{c}_5(y) \leq \widehat{c}_5(x)$. $\square$

### Factorisation through $h^2$

**Theorem.** $\widetilde{c}_5(h) = \widehat{c}_5(h^2)$.
*Proof.* Both expressions evaluate to $-3/2 + 1/(h^2 + 4)$. $\square$

Categorically, $c_5$ factors as
$$h \xrightarrow{\text{squaring}} h^2 \xrightarrow{\text{rational map}} c_5$$
where the first arrow sends a bar-anti-symmetric element to its bar-symmetric square and the second arrow preserves bar-symmetry, making the bar-invariance of $c_5$ manifest at the level of function composition.
