*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (silver-ratio $\beta$-decay null).**
*Let $q$ be the substrate parameter and $h = q - q^{-1}$ the Hecke
skein parameter on $H_3(q)$. Then:*

$$
\boxed{\;
\Delta(\mathrm{net}) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\;
\frac{h(h-2)}{2}
\;=\;
\frac{q^2 - 2q - 1}{2q}
\;}
$$

*vanishes if and only if $h = 2$ if and only if $q = 1 \pm \sqrt{2}$
(the **silver-mean conjugates**).*

*At $q = 1 + \sqrt{2}$ (silver ratio):*

1. *The Hecke quadratic $\sigma^2 = h\sigma + 1$ becomes
   $\sigma^2 = 2\sigma + 1$, whose roots are*
   $$\sigma = 1 \pm \sqrt{2} = q^{\pm 1}|_{q=1+\sqrt{2}}.$$
   *The generator $\sigma$ has eigenvalues equal to the
   silver-ratio conjugates themselves — a **self-referential
   fixed point**.*
2. *Proton and neutron single-wrap Markov traces become equal:
   $\mathrm{net}(p) = \mathrm{net}(n) = 1 - h/2 = 0$.*
3. *Form A vanishes: $\mathfrak{Q}_\beta^A = m_e \cdot |q^2-2q-1|(q+1)/(2q^3) = 0$.*

*The value $q = 1 + \sqrt{2}$ is the **β-decay null point**: the
substrate value at which proton and neutron have equal single-wrap
Markov traces and free-neutron $\beta^-$ decay vanishes at the
leading-order (Form A) level.*

## Derivation

From [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic),
the symbolic single-wrap Markov-trace net coefficients are:

| | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | net |
|---|:---:|:---:|:---:|:---:|:---:|
| proton | $0$ | $-h/2$ | $0$ | $1$ | $1 - h/2$ |
| neutron | $h^2/2$ | $-h$ | $-h/2$ | $1$ | $1 - 3h/2 + h^2/2$ |

Subtracting: $\Delta(\mathrm{net}) = h^2/2 - h = h(h-2)/2$.

Setting $h = 2$ gives $q - q^{-1} = 2$, i.e. $q^2 - 2q - 1 = 0$,
with roots $q = 1 \pm \sqrt{2}$.
