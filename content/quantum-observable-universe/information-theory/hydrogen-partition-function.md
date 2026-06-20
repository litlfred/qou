*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Setup.**
Consider a monatomic hydrogen gas: $N$ atoms of
$\mathcal{A}(1,0)$
([hydrogen knot structure](#ex:hydrogen-knot-structure))
at quantum temperature $T_q = \hbar_q$ in a region $U$
with quantum volume $V_q$
([quantum volume](#def:quantum-volume)).
Each hydrogen atom consists of a proton (Borromean link
$\mathcal{B}_3$ with Hopf binding $\mathcal{L}_H$) and
an electron (trefoil $T_{2,3}$).  We treat the atom as
a single composite knot $K_H = \mathcal{A}(1,0)$.

This is the simplest non-trivial gas: hydrogen has the
lightest knot structure and the fewest internal degrees
of freedom.  We work with monatomic $H$ (plasma regime),
not molecular $H_2$, to avoid the additional complication
of inter-atomic bonding braids.

**Single-atom partition function.**
The atom $K_H$ lives in an $S^3$ fibre.  Its internal
degrees of freedom are:

1. **Translational**: the brane point $p \in U$ where
   the atom sits.  This contributes a factor of $|U|$
   (the number of available brane points).

2. **Rotational**: the $\mathrm{SU}_q(2)$ orientation
   of the Borromean link within the fibre.  The
   $q$-angular momentum eigenvalues are
   $J_q^2 = [j]_q [j+1]_q$
   ([q-energy](#def:q-energy)), and the rotational
   partition function is

$$
  z_q^{(\mathrm{rot})}
  \;=\;
  \sum_{j=0}^{j_{\max}}
  [2j+1]_q \;
  e^{-\beta_q \, [j]_q [j+1]_q \, \hbar_q}.
$$

3. **Vibrational**: the writhe of the braid closure,
   governing $q$-momentum $p_q(\beta)$.  For the
   Borromean link, the writhe is $w(\mathcal{B}_3) = 0$
   (the link is amphichiral), so the translational
   kinetic contribution vanishes at lowest order.

4. **Internal (action)**: the categorical action
   $\mathfrak{S}_q(K_H) = \mathrm{tr}_\tau(\rho(\beta_H))$, where
   $\beta_H$ is the braid representative of $K_H$.
   This is the rest-mass contribution.

The single-atom partition function is therefore

$$
  z_q
  \;=\;
  e^{-\beta_q \, \mathfrak{S}_q(K_H)}
  \cdot z_q^{(\mathrm{rot})}
  \cdot z_q^{(\mathrm{vib})},
$$

where $z_q^{(\mathrm{vib})} = 1 + O(\hbar_q^2)$ for
the amphichiral Borromean proton (the leading vibrational
mode is suppressed by the vanishing writhe).

**$N$-atom gas.**
Applying the quantum ideal gas law
([quantum ideal gas law](#prop:quantum-ideal-gas-law)):

$$
  P_q \, V_q
  \;=\; N \, \hbar_q
  \left(
    1 \;+\;
    \frac{\hbar_q^2}{[2]_q}
    \,\mathfrak{S}_q(K_H)
  \right).
$$

The correction term
$\hbar_q^2 \, \mathfrak{S}_q(K_H) / [2]_q$ is the ratio of the
$q$-anomaly energy (from the non-trivial knot topology
of hydrogen interacting with the boundary) to the fibre
volume.  For a gas of unknots (hypothetical structureless
particles with $\mathfrak{S}_q = 0$), the correction vanishes and
we recover the exact leading-order law $P_q V_q = N \hbar_q$.

**Why hydrogen is "easiest".**
Among all atoms $\mathcal{A}(Z, N)$:

- Hydrogen has the **simplest knot**: one Borromean link
  plus one trefoil, with composite crossing number $n_K = 13$
  ([crossing parity](#prop:composite-crossing-parity)).
- The Borromean link is **amphichiral** ($w = 0$), so the
  momentum contribution vanishes at leading order.
- The proton mass dominates:
  $\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2$ accounts for
  $\sim 99.95\%$ of the atomic mass.  The electron trefoil
  $T_{2,3}$ is a torus knot with
  $\mathrm{Vol}(T_{2,3}) = 0$, contributing zero
  hyperbolic volume — its mass arises entirely from
  vacuum drag (Skein corrections).

**Heat capacity.**
The constant-volume heat capacity follows from
$C_V = -\beta_q^2 (\partial^2 \ln Z_q / \partial \beta_q^2)$.
At high temperature ($\beta_q \to 0$, deep quantum
regime), only the $j = 0$ rotational mode is populated
and $C_V \to 0$.  At low temperature ($\beta_q \to \infty$,
classical limit), all rotational modes contribute and
$C_V \to \frac{3}{2} N \hbar_q$ — recovering the
classical monatomic result $C_V = \frac{3}{2} N k_B$.
The crossover is governed by the rotational temperature
$T_q^{(\mathrm{rot})} = [1]_q [2]_q \, \hbar_q^2$, the
energy gap between $j = 0$ and $j = 1$.
