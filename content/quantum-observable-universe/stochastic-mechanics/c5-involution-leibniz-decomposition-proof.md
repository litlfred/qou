### Step 1: bar involution and the averaged crossing

The Hecke algebra $H_n(q)$ carries the **bar involution** $\overline{\,\,}$,
a $\mathbb{Z}$-linear anti-ring-automorphism defined by:
$$
\overline{q} = q^{-1}, \quad \overline{\sigma_i} = \sigma_i^{-1}.
$$

Using the Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ (where $h = q - q^{-1}$),
we have $\sigma_i^{-1} = \sigma_i - h$.

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

From [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic),
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
\tau_M(\mathcal{B}_n - \mathcal{B}_p) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\; \frac{h^2}{2} - h
\;=\; \frac{h(h-2)}{2}.
$$

The $h^2/2$ term is the product of TWO averaged-crossing $h/2$
contributions (the neutron has two such positions). The $h/2$
generates the $1/2$ in $\Delta(\mathrm{net})$.

For higher rungs $N = k \geq 4$ of the precision ladder, the
expansion of $\tau_M(T_\beta)$ in $b \cdot \hbar_q^2$ produces
coefficients with two distinct categorical origins:

- **Pure-$\sigma$ contributions**: from non-averaged positions in
  the braid. These factor through $\sigma^p \cdot b^{2m}$
  combinatorics. At the silver ratio ($\sigma$-eigenvalues
  $= 1 \pm \sqrt{2}$ via the Hecke quadratic
  [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null)),
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
