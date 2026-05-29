The [decomposition](#prop:crossing-energy-decomposition) separates
crossing energy into two physically distinct channels.

**Channel identification.**

| Channel | Weight per crossing | Mirror behaviour | Physical force |
|---------|-------------------|-----------------|----------------|
| Symmetric | $\cosh(\ln q)$ | Invariant under $\sigma$ | **Strong binding** |
| Antisymmetric | $\sinh(\ln q)$ | Reverses under $\sigma$ | **Coulomb (electromagnetic)** |

The symmetric part contributes equally to particle and antiparticle —
it binds regardless of charge.  The antisymmetric part has opposite
effect on particle and antiparticle — it distinguishes charges.

**Pair creation: why the pair flies apart.**

When an $e^- e^+$ pair is created, the proposition's pair
cancellation result gives:

$$
  \mathfrak{E}_{\mathrm{cross}}(e^-) + \mathfrak{E}_{\mathrm{cross}}(e^+)
  =  6\sinh(\ln q)
   \approx  0.630 \quad (\text{Skein units}).
$$

The symmetric (strong) contributions cancel.  The residual
$6\sinh\lambda > 0$ is pure Coulomb repulsion driving the pair
apart.

**EM/strong ratio.**

At $q = q_0$:

$$
  \tanh(\ln q_0)  \approx  0.104.
$$

Electromagnetism is approximately **10\%** of the strong force at the
constituent (Skein) scale.

**Crossing energy table** for a particle with $n_c$ positive
crossings:

| Quantity | Formula | $T_{2,3}$ ($n_c = 3$) | Value |
|----------|---------|----------------------|-------|
| Total crossing energy | $n_cq$ | $3q$ | $3.330$ |
| Strong component | $n_c\cosh(\ln q)$ | $3\cosh(\ln q)$ | $3.015$ |
| Coulomb component | $n_c\sinh(\ln q)$ | $3\sinh(\ln q)$ | $0.315$ |
| Pair net energy | $n_c(q - q^{-1})$ | $3(q - q^{-1})$ | $0.630$ |
| EM/strong ratio | $\tanh(\ln q)$ | $\tanh(\ln q)$ | $0.104$ |

The [Hopf stability](#prop:torus-hopf-stability) result —
$\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$ — says the strong symmetric
channel dominates the Coulomb antisymmetric channel for the proton,
ensuring stability.
