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

The lone/bond ratio $q^2$ is the **same braid weight for every atom** (the
identical local $e^-/\sigma$ words on the symmetric block, $q^3/q$); the bond
angle varies only by (i) the $AX_nE_m$ domain counts and (ii) the
**hybridisation base** $\theta_0$ — the geometry the bonding orbitals take,
fixed by the central atom's $s$–$p$ promotion gap.

| Molecule | Atom $(n)$ | Bond | Lone | $w_{\mathrm{lone}}/w_{\mathrm{bond}}$ | Base $\theta_0$ | Predicted | Observed |
|---|---|---|---|---|---|---|---|
| $\mathrm{CH_4}$ | C $(2)$ | $\sigma\ (\ell 1,\,q)$ | — | — | $109.47^\circ$ (sp³) | $109.47^\circ$ | $109.5^\circ$ |
| $\mathrm{NH_3}$ | N $(2)$ | $\sigma\ (\ell 1,\,q)$ | $e^-\ (\ell 3,\,q^3)$ | $q^2$ | $109.47^\circ$ (sp³) | $106.88^\circ$ | $107.0^\circ$ |
| $\mathrm{H_2O}$ | O $(2)$ | $\sigma\ (\ell 1,\,q)$ | $e^-\ (\ell 3,\,q^3)$ | $q^2$ | $109.47^\circ$ (sp³) | $104.72^\circ$ | $104.5^\circ$ |
| $\mathrm{H_2S}$ | S $(3)$ | $\sigma\ (\ell 1,\,q)$ | $e^-\ (\ell 3,\,q^3)$ | $q^2$ | $90^\circ$ (pure-$p$) | $90.0^\circ$ | $92.1^\circ$ |

The second-row atoms (C, N, O — small $s$–$p$ gap) hybridise, so the four
domains take the **sp³ tetrahedral base** $\theta_0 = \arccos(-\tfrac13) =
109.47^\circ$; the $q^2$ lone weight then narrows it (VSEPR), giving
$\mathrm{CH_4}/\mathrm{NH_3}/\mathrm{H_2O}$ within $0.22^\circ$ ($\mathrm{CH_4}$
exact by symmetry). This specialises
[`prop:h2o-bond-angle-shift`](#prop:h2o-bond-angle-shift): $q^2$ is the
lone/bond weight its bent-angle quadratic well consumes.

Third-row sulfur (large $s$–$p$ gap) does **not** hybridise: the two bonds use
the mutually **orthogonal pure-$p$ orbitals**, so the base is $\theta_0 =
90^\circ$, orbital-locked, and the $q^2$ lone pairs (on the $s$ $+$ axial-$p$
directions) do not reopen it — giving $\mathrm{H_2S}\approx 90^\circ$, within
$2.1^\circ$ of experiment. The $\mathrm{H_2S}$ deviation is therefore **not** a
weight anomaly — the $q^2$ braid weight is universal — but the **base
geometry**, fixed by the structural $s$–$p$ promotion gap, with no fit.
(Forcing the sp³ base instead would demand the spurious non-integer
$w_{\mathrm{lone}}/w_{\mathrm{bond}}\approx q^{7.8}$, which is the diagnostic
that the base, not the weight, is what changes.)
