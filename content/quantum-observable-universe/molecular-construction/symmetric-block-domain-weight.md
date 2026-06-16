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

## Molecular consequence — one rule, $\mathrm{weight} = q^{\ell}$

Every electron domain is a braid word weighted $q^{\ell}$ on the symmetric
block: a single bond $\sigma$ ($\ell{=}1$) weighs $q$, a **double** bond
$\sigma^2$ ($\ell{=}2$) weighs $q^2$, a lone pair
$e^- = \sigma_0\sigma_1\sigma_0$ ($\ell{=}3$) weighs $q^3$ — one $q$ per bond
order, and the lone/bond ratio $q^3/q = q^2$. The angle then needs only (i) the
$AX_nE_m$ domain counts and (ii) the **hybridisation base** $\theta_0$ — set by
whether the central atom's self-dual $s$-channel is in the bonding active set,
which the atom's size (its $s$–$p$ promotion gap) controls. No angle is fitted.

| Molecule | Atom $(n)$ | $AX_nE_m$ | Bonds | Lones | Base $\theta_0$ | Predicted | Observed |
|---|---|---|---|---|---|---|---|
| $\mathrm{CH_4}$ | C $(2)$ | $AX_4E_0$ | $4\,\sigma\,(q)$ | — | sp$^3$ $109.47^\circ$ | $:val[predicted_ch4_deg]{precision=5, witness=computations/molecular-angle-master-table.witness.json}^\circ$ | $109.5^\circ$ |
| $\mathrm{NH_3}$ | N $(2)$ | $AX_3E_1$ | $3\,\sigma\,(q)$ | $e^-\,(q^3)$ | sp$^3$ $109.47^\circ$ | $:val[predicted_nh3_deg]{precision=5, witness=computations/molecular-angle-master-table.witness.json}^\circ$ | $107.0^\circ$ |
| $\mathrm{H_2O}$ | O $(2)$ | $AX_2E_2$ | $2\,\sigma\,(q)$ | $2\,e^-\,(q^3)$ | sp$^3$ $109.47^\circ$ | $:val[predicted_h2o_deg]{precision=5, witness=computations/molecular-angle-master-table.witness.json}^\circ$ | $104.5^\circ$ |
| $\mathrm{C_2H_4}$ | C $(2)$ | $AX_3$ | $\sigma^2\,(q^2){+}2\,\sigma\,(q)$ | — | sp$^2$ $120^\circ$ | $:val[predicted_c2h4_deg]{precision=5, witness=computations/molecular-angle-master-table.witness.json}^\circ$ | $116.6^\circ$ |
| $\mathrm{CO_2}$ | C $(2)$ | $AX_2$ | $2\,\sigma^2\,(q^2)$ | — | sp $180^\circ$ | $:val[predicted_co2_deg]{precision=5, witness=computations/molecular-angle-master-table.witness.json}^\circ$ | $180.0^\circ$ |
| $\mathrm{H_2S}$ | S $(3)$ | $AX_2E_2$ | $2\,\sigma\,(q)$ | $2\,e^-\,(q^3)$ | pure-$p$ $90^\circ$ | $:val[predicted_h2s_deg]{precision=5, witness=computations/molecular-angle-master-table.witness.json}^\circ$ | $92.1^\circ$ |

The second-row atoms (C, N, O — small $s$–$p$ gap) hybridise, so the
$s$-channel is active and the domains take the **sp/sp$^2$/sp$^3$ base** by steric
number ($180/120/109.47^\circ$); the $q^3$ lone (or $q^2$ double-bond) weight
then shifts it. This reproduces $\mathrm{CH_4}/\mathrm{NH_3}/\mathrm{H_2O}/
\mathrm{C_2H_4}/\mathrm{CO_2}$ within $0.6^\circ$ and specialises
[`prop:h2o-bond-angle-shift`](#prop:h2o-bond-angle-shift).

Third-row sulfur (large $s$–$p$ gap) does **not** hybridise — the $s$-channel
drops from the active set — so the two bonds use the orthogonal **pure-$p$**
orbitals, base $\theta_0 = 90^\circ$. The residual $+2.1^\circ$
($\mathrm{H_2S} \approx 92^\circ$) is a **lone-pair braid asymmetry** that
$\mathrm{H_2O}$ lacks: with the $s$-channel inert the two lone pairs are
*inequivalent* — the self-dual $3s^2$ (the $e^-$ palindrome, defect $0$,
$\ell{=}0$) and the chiral $3p_z$ (non-palindromic, defect $2\ell{=}2$) — and
the chiral pair's directional bias opens the orbital-locked $90^\circ$.
$\mathrm{H_2O}$'s two lone pairs are *equal* self-dual $e^-$ (defects $0,0$), so
it has no such tilt. The sp$^3 \leftrightarrow$ pure-$p$ flip itself is derived
from the shell braid — the self-dual-$s$ / chiral-$p$ split plus the $ns$
penetration of the $(n{-}1)$ inner shells, $\Delta(n)\propto(n{-}1)=$
central-atom size, a *discrete* flip at $n{=}2{\to}3$ (group-16
$\mathrm{O}\,104.5^\circ \to \mathrm{S/Se/Te}\sim 90^\circ$ confirms the
saturation), with no fit.
