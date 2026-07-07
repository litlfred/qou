<!-- FILE_START: h2o-molecular-braid.md -->
*Lean sibling: combinatorial strand-partition datum, self-contained per the content-block convention (AGENTS.md §7c / §8).*

**Definition.** **Water** *$H_2O$ is the molecular braid assembled from three sub-units — one oxygen $O(8,8)$ ($A+Z = 16+8 = 24$ strands, valence $2$ with two lone pairs) and two hydrogens $H_1, H_2$ ($2$ strands each) — in $H_{28}(q)$, by the [assembly projector](#def:molecular-assembly-projector) $e_{\lambda,\mu}$ over the parabolic subalgebra $H_\lambda(q)$ with [strand-partition](#def:molecular-strand-partition) $\lambda = (24, 2, 2)$.*

Of the $H_\lambda(q)$ generators, the $N - k = 25$ intra-block generators are internal to the three atoms, and the $k - 1 = 2$ cross-block (bonding) generators are the two O–H $\sigma$-bonds; the assembly projector selects the Wedderburn block $\mu$ that pairs each hydrogen's electron with oxygen. The Lean sibling fixes the combinatorics — total $N = 28$, two bonding generators, and the hydrogen-exchange symmetry of the partition.

Two interpretations follow: the molecular point symmetry as the stabiliser of $e_{\lambda,\mu}$, and the bent geometry forced by oxygen's lone pairs.
<!-- FILE_END: h2o-molecular-braid.md -->

<!-- FILE_START: h2o-c2v-from-projector.md -->
*Interpretation of the [H$_2$O molecular braid](#def:h2o-molecular-braid).*

The two hydrogen sub-units of water carry equal strand count, so the exchange $H_1 \leftrightarrow H_2$ fixes the strand-partition $\lambda = (24,2,2)$ and hence the assembly projector $e_{\lambda,\mu}$. That $S_2$ stabiliser **is** the $C_{2v}$ point symmetry of the molecule — a $C_2$ rotation about the bisector of the H–O–H angle, with oxygen fixed.

This is the H$_2$O instance of the general principle that **a structure's point symmetry is the stabiliser of its assembly projector**: the same mechanism that gives benzene's three equal acetylene units the ring symmetry $S_3$ (via $e_{(2,2,2),(6)}$). The assembly projector is the structure-forming operator, and its invariance group is the structure's symmetry; water and benzene are the $S_2$ and $S_3$ instances of one categorical statement. The same reading, applied to the inter-molecular operator that forms a condensed phase rather than the intra-molecular one that forms a bond, extends the principle from molecular point groups to the symmetries of phases of matter.
<!-- FILE_END: h2o-c2v-from-projector.md -->

<!-- FILE_START: h2o-bent-geometry.md -->
*Interpretation of the [H$_2$O molecular braid](#def:h2o-molecular-braid).*

Oxygen contributes two bonding sites and **two lone pairs**. In the assembly, the lone pairs occupy two of the four tetrahedral directions around oxygen as non-bonding *phantom sites* — the $NH_3 \to H_2O$ extension of the methane $T_d$ optimisation: lone-pair repulsion relaxes the $H$–$O$–$H$ angle from the ideal $109.5^\circ$ toward the observed $\approx 104.5^\circ$.

The four directions — two donor $H$ and two acceptor lone pairs — are the per-molecule input to the **ice lattice**. Each water hydrogen-bonds to four neighbours, two as donor and two as acceptor, and the resulting tetrahedral coordination tiles into hexagonal ice $I_h$ (space group $P6_3/mmc$); the open tetrahedral network is why ice is less dense than liquid water. The choice of which two of the four bonds carry "this molecule's" hydrogens, subject to the rule that every bond holds exactly one hydrogen, is the categorical origin of the Pauling residual entropy of ice, $\approx R\ln(3/2)$. The detailed tiling and its symmetry are developed in the phase-symmetry model.
<!-- FILE_END: h2o-bent-geometry.md -->

<!-- FILE_START: tetrahedral-hbond-directions.md -->
*Lean sibling: explicit Euclidean computation over $\mathbb{R}$.*

**Proposition.** The four hydrogen-bond directions of [a water in ice](#def:h2o-molecular-braid) — two donor, two acceptor — point to the vertices of a regular tetrahedron. Taking the vertex vectors $(\pm 1, \pm 1, \pm 1)$ with an even number of minus signs, they sum to zero, each has squared length $3$, and any two have dot product $-1$, so the bond-angle cosine is
$$ \cos\theta_0 \;=\; \frac{u_i \cdot u_j}{|u_i|\,|u_j|} \;=\; \frac{-1}{3}, \qquad \theta_0 = \arccos\!\left(-\tfrac13\right) \approx 109.47^\circ. $$
This is the symmetric reference angle $\theta_0$ from which oxygen's lone pairs displace the H–O–H angle to $\approx 104.5^\circ$ (the quadratic-well shift). The Lean sibling proves the four facts — balanced sum, squared length $3$, pairwise dot $-1$, and $\cos\theta_0 = -1/3$ — exactly over $\mathbb{R}$.
<!-- FILE_END: tetrahedral-hbond-directions.md -->

<!-- FILE_START: h2o-bond-angle-shift.md -->
*Lean sibling: structural, over $\mathbb{R}$ (the bending energy is archimedean).*

**Proposition.** Near the symmetric tetrahedral value $\theta_0$, the bond-bending energy of [water](#def:h2o-molecular-braid) is harmonic — a **quadratic** restoring term $a(\theta-\theta_0)^2$ with stiffness $a > 0$ — and oxygen's two lone pairs add a **linear** perturbation $b\,\theta$ (the net angular penalty from lone-pair repulsion exceeding bond-pair repulsion). The energy $a(\theta-\theta_0)^2 + b\,\theta$ is minimised at
$$ \theta_{\min} \;=\; \theta_0 - \frac{b}{2a}, $$
a linear response of the quadratic minimum. For water $b > 0$ (the lone-pair term penalises the wider symmetric angle), so $\theta_{\min} < \theta_0$: the reduction $109.5^\circ \to 104.5^\circ$ **is** the quadratic well's minimum displaced by the lone-pair term. The sign of the shift is structural; its magnitude $b/(2a)$ is the lone-pair repulsion strength relative to the angular stiffness.
<!-- FILE_END: h2o-bond-angle-shift.md -->

<!-- FILE_START: symmetric-block-domain-weight.md -->
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
<!-- FILE_END: symmetric-block-domain-weight.md -->

<!-- FILE_START: domain-weight-vsepr-angles.md -->
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
<!-- FILE_END: domain-weight-vsepr-angles.md -->

<!-- FILE_START: h2s-angle-s3-braid-holonomy.md -->
**Conjecture (H$_2$S bond-angle chiral residue $=$ S$^3$ braid holonomy).**

*The bond-angle residual of $\mathrm{H_2S}$ — the opening
$\Delta\theta \approx +2.1^\circ$ of the H–S–H angle above the pure-$p$ base
$\theta_0 = 90^\circ$ — equals the $q$-deformed Chern–Simons holonomy (the
monodromy phase around the singular fibre $\zeta_\ell$) of the chiral $3p_z$
lone-pair braid $\beta_{3p_z}$ on the chirality cell — the signed-content-zero
standard Wedderburn block $V_{(2,1)}$ (the $q$-Dirac kernel $D_q^2(\lambda)=0$):*

$$
  \Delta\theta_{\mathrm{H_2S}}
  \;=\;
  \arg \operatorname{Res}_{q=\zeta_\ell}\!\Bigl[\,\Phi_q \cdot
        \mathrm{tr}_{M,(2,1)}\bigl(\beta_{3p_z}\bigr)\Bigr].
$$

*Equivalently, $\Delta\theta$ is the **bar-anti-symmetric**
($P_{\mathrm{skew}}$, odd-in-$h$) part of the chiral lone's S$^3$ braid holonomy —
the chiral channel the framework otherwise projects away — and it **vanishes**
for the bar-symmetric (self-dual, palindromic) lone pairs of $\mathrm{H_2O}$,
which is why $\mathrm{H_2O}$'s angle is the clean $q^2$ prediction with no
residual.*
## Concrete realisation — the Bring $1/\sqrt5$ residual-mixing form

A predictive realisation (no fit): a third-row (pure-$p$) atom retains a small
**residual $s$-character** $f_s = (1/\sqrt5)/(n-1)^2$ that opens the $90^\circ$
base toward sp$^3$, so

$$
  \theta(n) \;=\; 90^\circ \;+\; \frac{1}{\sqrt5}\cdot
    \frac{\arccos(-\tfrac13) - 90^\circ}{(n-1)^2}.
$$

| | $n$ | predicted | observed |
|---|---|---|---|
| $\mathrm{H_2S}$ | $3$ | $92.18^\circ$ | $92.1^\circ$ |
| $\mathrm{H_2Se}$ | $4$ | $90.97^\circ$ | $91.0^\circ$ |
| $\mathrm{H_2Te}$ | $5$ | $90.54^\circ$ | $90.0^\circ$ |

$\mathrm{H_2S}$ and $\mathrm{H_2Se}$ land within $0.1^\circ$. The coefficient is
the **Bring / quintic constant** $1/\sqrt5$ ($\varphi = (1+\sqrt5)/2$; $\sqrt5$
the quintic discriminant) — the conjectured $S^3$-embedding chiral curvature
surfacing as the quintic $\sqrt5$ of Bring's surface — and the size dependence
is inverse-square in the $s$–$p$ gap. This is the concrete content of the
conjecture: the chiral residue is the $1/\sqrt5$ Bring curvature, inverse-square
in central-atom size. *Tier:* a strong, Bring-grounded near-match constrained by
two data points — reported as a tiered observation; the exact $\zeta_\ell$
monodromy is still the formal target.

The explicit geometry of this $\sqrt5$ is the provable scaffold
[`prop:bring-trefoil-cinquefoil-channel`](../brings-surface/bring-trefoil-cinquefoil-channel.md):
the chiral channel is the **trefoil** $T_{2,3}$ (Seifert genus $1$) and the
$\zeta_5$ is the **cinquefoil** $T_{2,5}$ (genus $2$) — two distinct torus knots
sharing Bring's $\Sigma_4$ (genus $4$) and linked by $\mathrm{Aut}(B) = S_5$.

> [!NOTE]
> **The Quintic Within Brings:** It is critical to distinguish the global *Bring curve* (a genus-4 curve in $\mathbb{CP}^4$ whose $S_5$ characters fix the $2 \times 2$ Picard-Fuchs matrix and depth-2 recurrence for the mass tower) from the *hyperelliptic quintic* $\mathcal{X}_5 \colon y^2 = x^5 - 1$. The latter is a genus-2 curve **embedded within Bring's surface**. The chiral normalisation specifically relies on the $\mathbb{Z}_5$ automorphism of this embedded quintic.

The $\sqrt5$ is supplied by the $\mathbb{Z}_5$-orbit quadratic Gauss sum
$\bigl(\sum_k \zeta_5^{k^2}\bigr)^2 = 5$ carried by the first Lagrange resolvent
$w_1$ that embeds the hyperelliptic quintic $\mathcal{X}_5$. That structural scaffold is established; evaluating the exact analytic Picard-Lefschetz monodromy of the $\zeta_5$-residue on the homology of $y^2 = x^5 - 1$ to formally return precisely $1/\sqrt5$ and the $+2.1^\circ$ phase remains the open content of this conjecture.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: h2s-angle-s3-braid-holonomy.md -->

<!-- FILE_START: ice-pauling-residual.md -->
*Lean sibling: combinatorial, exact over $\mathbb{Q}$ (the entropy $S = R\ln W_1$ step is archimedean).*

**Proposition (Pauling residual entropy of ice).** In ice $I_h$ each water is hydrogen-bonded to four neighbours — two as **donor** (its two H's) and two as **acceptor** (its two lone pairs), the four directions of [the H$_2$O braid](#def:h2o-molecular-braid). Subject to the ice rule that every bond carries exactly one hydrogen, the per-molecule multiplicity is
$$ W_1 \;=\; \binom{4}{2}\left(\tfrac12\right)^{2} \;=\; \frac{6}{4} \;=\; \frac{3}{2}, $$
thus the molar residual entropy is $S = R\ln\tfrac32 \approx 3.37\ \mathrm{J\,mol^{-1}\,K^{-1}}$ (Pauling, 1935), in close agreement with the measured ice calorimetry.
<!-- FILE_END: ice-pauling-residual.md -->

