**Proposition.** *On the symmetric (trivial) representation of the braid
monoid — the one-dimensional Wedderburn block that a molecule's $C_{nv}$
assembly projector selects (the $S_n$-symmetric channel of
[`rem:h2o-c2v-from-projector`](#rem:h2o-c2v-from-projector)) — every generator
$\sigma_i$ acts as the scalar $q$. Hence an electron domain represented by a
braid word $w$ of length $\ell$ has weight*

$$
  w_{\mathrm{domain}} = q^{\ell}.
$$

*In particular the lone pair $e^- = \sigma_0\sigma_1\sigma_0$ (length $3$) and
the $\sigma$-bond (length $1$) have weights $q^3$ and $q$, so the lone-pair to
bond weight ratio is*

$$
  \frac{w_{\mathrm{lone}}}{w_{\mathrm{bond}}} = \frac{q^3}{q} = q^2 .
$$

This ratio is **derived** — a ratio of Hecke eigenvalues on the symmetric
channel — with no central-atom input and no fit, and (being a ratio of
eigenvalues, not an angle) it is independent of the repulsion kernel. The
provable core — the weight law $q^{\ell}$ and the corollary $q^3 = q^2\cdot q$ —
is formalized sorry-free in the Lean sibling
(`symmetric_block_domain_weight`, `lone_bond_ratio_q_squared`).

## Molecular consequence

Feeding the single ratio $q^2$ into the weighted points-on-a-sphere VSEPR
minimiser, with only the per-molecule domain counts (the $AX_nE_m$ type: $n$
bonding $+$ $m$ lone-pair domains), reproduces the second-row hydride angles:

| Molecule | Type | Predicted | Observed |
|----------|------|-----------|----------|
| $\mathrm{CH_4}$ | $AX_4E_0$ | $\approx 109.47^\circ$ | $109.5^\circ$ |
| $\mathrm{NH_3}$ | $AX_3E_1$ | $\approx 106.88^\circ$ | $107.0^\circ$ |
| $\mathrm{H_2O}$ | $AX_2E_2$ | $\approx 104.72^\circ$ | $104.5^\circ$ |

Each is within $0.22^\circ$ of experiment, with $\mathrm{CH_4}$ exact by
symmetry. The variation across the series is carried entirely by the domain
counts; the electron-structure ratio $q^2$ is the **same** for every molecule.
The same-block analysis specialises [`prop:h2o-bond-angle-shift`](#prop:h2o-bond-angle-shift):
it supplies the lone/bond weight ratio that the bent-angle quadratic well
consumes.

$\mathrm{H_2S}$ (third row, $AX_2E_2$) is **not** captured by the second-row
$q^2$ ratio: reaching its $\approx 92^\circ$ angle would require
$w_{\mathrm{lone}}/w_{\mathrm{bond}} \approx 2.26$, which is **not** a clean
power of $q$ ($\approx q^{7.8}$). The deviation is therefore a genuine
*feature* — it correctly flags that $\mathrm{H_2S}$ leaves the second-row
electron structure (its near-$90^\circ$ angle reflects reduced $s$–$p$
hybridisation, nearly pure $p$-orbital bonding) — but the precise third-row
ratio is an **open extension** of the heavier-atom braid structure, not yet
derived. The clean derivation here is the second-row series.
