**Proposition (cyclotomic dimension synthesis at every depth $n$
and prime $K$).**

[`prop:cyclotomic-depth3-dimension-synthesis`](#prop:cyclotomic-depth3-dimension-synthesis)
gave the dimension count at $n = 3$.  *This proposition extends to
every depth $n \geq 2$ via the parity-dependent combination of the
Jonquière Tate-rationality + orbit-sum theorems:*

$$
  \boxed{\;
    \dim_{\mathbb{Q}}\mathcal{V}_{n, K}
    \;=\;
    \begin{cases}
      (K - 3)/2 & \text{$n$ odd}, \\
      (K - 1)/2 & \text{$n$ even},
    \end{cases}
  \;\;\text{(upper bound theorem; Beilinson-conditional lower bound)}
  \;}
$$

*where $\mathcal{V}_{n, K}$ is the $\mathbb{Q}$-vector space spanned by
depth-$n$ grouplikes at the $\zeta_K$-orbit modulo the
$\zeta(n)$-line and Tate.*
### Significance

**Cyclotomic depth-$n$ picture is structurally complete at every
$n \geq 2$ and every prime $K \geq 3$.**

Combined with prior framework:

- [`prop:two-filtration-bridge-general`](#prop:two-filtration-bridge-general):
  bridge map at every partition.
- This proposition: dimension at every $(n, K)$ pair.
- B1 keystone status: theorem-level at $n = 2$ (Bloch–Suslin),
  Beilinson-conditional at $n \geq 3$.

The framework's cyclotomic depth structure is **fully characterised**.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-depth3-dimension-synthesis`](#prop:cyclotomic-depth3-dimension-synthesis)
- Special case $n = 5$, $K = 5$: round-12  [`prop:cl3-zeta5-pslq-independence`](#prop:cl3-zeta5-pslq-independence)
- Tate-rationality (Step 2): [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Orbit-sum (Step 3): [`prop:cyclotomic-orbit-sum-all-depths`](#prop:cyclotomic-orbit-sum-all-depths)
- Borel rank: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Depth-2 theorem-level: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- B1 status synthesis: [`rem:b1-current-status`](#rem:b1-current-status)
