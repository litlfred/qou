The six-way refutation of the level-selection rule $n_\star$ in
[`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro)
([closure audit](../../../docs/audits/2026-05-11-brane-tower-n_star-closure-audit.md))
established that no choice of $n_\star$ — scalar, operator-valued,
multiplicity-refined, pair-knot product-volume, or pair-knot
Markov-trace — recovers the AME light-isotope binding uniformly
across $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$. The
${}^3\mathrm{He}$ residual survives every operator-volume
convention probed.

The **operator-selection LP dual** ([`prop:operator-selection-lp`](#prop:operator-selection-lp))
nonetheless confirms a real structural feature: the pair-knot
composite operators $\sigma_{pp}, \sigma_{nn}$ are in the active
set EXACTLY at magic-shell atoms (Z=2 activates $\sigma_{pp}$,
N=2 activates $\sigma_{nn}$, doubly magic ⁴He activates both),
with strong duality (LP gap $\leq 10^{-15}$, SDP gap $\leq 10^{-6}$).
The
[spin-involution corollary](#prop:spin-involution-lp-dual-invariance)
gives the algebraic basis for $Z \leftrightarrow N$ symmetry at the
Markov-trace operator level.

This conjecture proposes that the surviving open path beyond
$n_\star$ is the existence of a **separate magic-shell
stabilization term** in the binding-energy formula.

## Statement

**Conjecture (magic-shell stabilization term).**
*The brane-tower binding-energy formula*

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot \bigl(
    \lvert\mathrm{tr}_M(T_w)\rvert
    + \mathrm{tower}(\mathfrak{H})
    + \sigma_{3A}
  \bigr)
$$

*from [`prop:atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation)
admits a structural correction*

$$
  B^{\star}(\mathfrak{H}) \;=\; B(\mathfrak{H})
    \;+\; \Delta_{\mathrm{shell}}(Z, N)
$$

*where $\Delta_{\mathrm{shell}}(Z, N) \in \mathbb{R}$ is the
**magic-shell stabilization term**, indexed by closed-shell
occupancy and satisfying:*

1. ***Magic-only support:*** $\Delta_{\mathrm{shell}}(Z, N) = 0$
   whenever neither $Z$ nor $N$ is a nuclear magic number
   ($\{2, 8, 20, 28, 50, 82, 126\}$).
2. ***$Z \leftrightarrow N$ symmetry:*** $\Delta_{\mathrm{shell}}(Z, N)
   = \Delta_{\mathrm{shell}}(N, Z)$ (isospin invariance, consistent
   with the Markov-trace pair-knot identity
   $\mathrm{tr}_M(\sigma_{pp}) = \mathrm{tr}_M(\sigma_{nn})$ from
   [`prop:spin-involution-lp-dual-invariance` §"Corollary (pair-knot
   $Z \leftrightarrow N$ symmetry)"](#prop:spin-involution-lp-dual-invariance)).
3. ***Substrate-derived:*** $\Delta_{\mathrm{shell}}(Z, N)$ is a
   function of the magic-shell sub-braid $\sigma_{\mathrm{shell}}$
   and its Hecke-algebra invariants only — no per-atom calibration.

The corrected formula $B^{\star}$ closes the AME light-isotope
sample $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ to within
$\sim 5\%$.

## Status — open; operator-volume convention undetermined

The closure work (PR #638) does not pin down the canonical operator-
volume convention for the underlying $B(\mathfrak{H})$. Different
conventions give different calibrations of $\Delta_{\mathrm{shell}}$:

| Convention | $\Delta_{\mathrm{shell}}(Z=2)$ from ³He | $\Delta_{\mathrm{shell}}(Z=N=2)$ from ⁴He | Z↔N consistent? |
|:---|---:|---:|:---:|
| Operator-valued per-eigenvalue, $n_\star=1$ | $+4.32$ MeV | n/a | n/a |
| Pair-knot product-volume | $-16.88$ MeV | $+5.50$ MeV | NO ($\Delta_n = +22.38$ MeV $\neq \Delta_p$) |
| Pair-knot Markov-trace (canonical) | $-11.92$ MeV | TBD | TBD |

The Z↔N inconsistency under product-volume is a known artifact
of the convention (see
[brane-tower-z-habiro §"Pair-knot Markov-trace refinement"](#conj:brane-tower-z-habiro)),
but the correct operator-volume convention for which
$\Delta_{\mathrm{shell}}$ is well-defined and Z↔N-symmetric is
**open**.

### Proof obligations

1. **Identify the canonical convention.** Find the operator-volume
   convention (full $\mathrm{tr}_M(\sigma_{\mathrm{shell}})$? Hopf-
   antipode-symmetrized? something else?) under which
   $\Delta_{\mathrm{shell}}(Z, N) = \Delta_{\mathrm{shell}}(N, Z)$
   holds empirically across $\{{}^3\mathrm{H}, {}^3\mathrm{He}\}$
   (mirror nuclei) and $\{{}^4\mathrm{He}\}$ (doubly magic).
2. **Extend to other magic shells.** Test predictions at $Z = 8$
   (¹⁶O), $N = 8$ (¹⁵N + ¹⁷O), and onwards.  At $Z = 8$ the
   intra-O sub-braid spans the 16 intra-strand generators across
   the 8 protons.
3. **Closed-form for $\Delta_{\mathrm{shell}}$.** Express
   $\Delta_{\mathrm{shell}}(Z, N)$ as a function of the magic-shell
   Markov trace $\mathrm{tr}_M(\sigma_{\mathrm{shell}})$ and the
   $q$-deformed shell-closure invariants (analogous to the Mayer-
   Jensen spin-orbit splittings in the classical nuclear shell
   model).

### Empirical motivation summary

- LP-dual active-set finding: $\sigma_{pp}, \sigma_{nn}$ are
  structurally privileged at exactly magic-shell atoms (PR #638
  family 5).
- Markov-trace Z↔N symmetry:
  $\mathrm{tr}_M(\sigma_{pp}) = \mathrm{tr}_M(\sigma_{nn}) =
  0.0622$ exactly (Hoefsmit, float64; provable algebraically via
  the spin-involution corollary).
- Brane-tower formula's universal overshoot at small $n_\star$:
  the per-generator $\sum_i \Phi_q(|\hat V_i|)$ tower at
  $n_\star \leq 3$ exceeds AME by $200$–$1000\%$ on
  $\{D, T, {}^3\mathrm{He}\}$, regardless of pair-knot collapse —
  consistent with a missing **subtracted** stabilization
  contribution rather than a missing additive contribution.
  (At doubly-magic ⁴He under pair-knot collapse, the brane-tower
  UNDER-shoots by $19.4\%$ — consistent with an **added**
  stabilization, since both Z=2 and N=2 shells contribute.)

The sign discrepancy in the empirical $\Delta_{\mathrm{shell}}$
calibration (negative for ³He, positive for ⁴He under product-
volume; sign undetermined under Markov-trace) is the central
empirical puzzle this conjecture seeks to resolve.

## Relation to nuclear physics

The classical Mayer-Jensen shell model attributes magic-number
stability to closed-shell occupancy of the harmonic-oscillator
plus spin-orbit Hamiltonian.  In the QOU framework, the
**categorical** analog of shell closure is the pair-knot
composite operator $\sigma_{\mathrm{shell}} \in H_{3A}(q)$
acting on the magic-shell-occupying strand block.  The
$\Delta_{\mathrm{shell}}$ term proposed here is the **brane-
tower categorical complement** of the classical shell-closure
energy savings — a structural term distinct from the running
$\Phi_q$ tower.

If verified, $\Delta_{\mathrm{shell}}(Z, N)$ would close
${}^3\mathrm{He}$ and provide the structural input the level-
selection rule alone cannot supply, completing the n_⋆-refutation
narrative of PR #638.
