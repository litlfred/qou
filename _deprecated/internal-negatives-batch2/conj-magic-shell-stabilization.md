*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

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
N=2 activates $\sigma_{nn}$, doubly magic ${}^{4}$He activates both),
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
3. ***Substrate-derived (no calibration):*** $\Delta_{\mathrm{shell}}(Z, N)$
   is a function of the magic-shell sub-braid $\sigma_{\mathrm{shell}}$
   and its Hecke-algebra invariants only — **predicted** from
   substrate data, not tuned to per-atom data.  Consistent with
   the three-calibration discipline (only $m_e$, $q_0$, $Q_\beta$
   are calibration anchors).

The corrected formula $B^{\star}$ closes the AME light-isotope
sample $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ to within
$\sim 5\%$.

## Status — open; operator-volume convention undetermined

The closure work (PR #638) does not pin down the canonical operator-
volume convention for the underlying $B(\mathfrak{H})$. Different
conventions give different **measured residuals** for
$\Delta_{\mathrm{shell}}$ (residuals to be matched by the conjecture's
prediction, not free parameters):

| Convention | $\Delta_{\mathrm{shell}}(Z=2)$ from ${}^{3}$He | $\Delta_{\mathrm{shell}}(Z=N=2)$ from ${}^{4}$He | Z$\leftrightarrow$N consistent? |
|:---|---:|---:|:---:|
| Operator-valued per-eigenvalue, $n_\star=1$ | $+4.32$ MeV | n/a | n/a |
| Pair-knot product-volume | $-16.88$ MeV | $+5.50$ MeV | NO ($\Delta_n = +22.38$ MeV $\neq \Delta_p$) |
| Pair-knot Markov-trace (canonical) | $-11.92$ MeV | — | — |

The Z$\leftrightarrow$N inconsistency under product-volume is a known artifact
of the convention (see
[brane-tower-z-habiro §"Pair-knot Markov-trace refinement"](#conj:brane-tower-z-habiro)),
but the correct operator-volume convention for which
$\Delta_{\mathrm{shell}}$ is well-defined and Z$\leftrightarrow$N-symmetric is
**open**.

### Empirical status (2026-05-11, post-instantiation probe)

**Terminology note:** the table below is a **residual-extraction
measurement**, not a calibration in the
[three-calibration discipline](#prop:three-calibration-inputs)
sense.  Only $m_e$ (CAL-1), $q_0$ (CAL-2), and $Q_\beta$ (CAL-3)
are calibration anchors; $\Delta_{\mathrm{cat}}$ values are
measured structural gaps that the conjecture obligates the
framework to **predict** from substrate data, not free parameters
to tune.

[`probe_magic_shell_empirical_instantiation.py`](../../../computations/probe_magic_shell_empirical_instantiation.py)
([witness](../../../computations/magic-shell-empirical-instantiation.witness.json))
extracts per-atom $\Delta_{\mathrm{cat}}(\mathfrak{H}) :=
\mathrm{AME}(\mathfrak{H}) - m_e \cdot \rho \cdot
|\tau(\beta_{\mathfrak{H}})|$ at 50dps using
`markov_peel.tr_M_atomic`:

| Atom | $|\tau(\beta_{\mathfrak{H}})|$ (50dps) | $m_e \rho |\tau|$ MeV | AME MeV | $\Delta_{\mathrm{cat}}$ MeV |
|:-:|:---:|---:|---:|---:|
| D | $0.388286472\ldots$ | $0.198$ | $2.225$ | $+2.026$ |
| T | $0.104052119\ldots$ | $0.106$ | $8.482$ | $+8.375$ |
| ${}^{3}$He | $0.206540859\ldots$ | $0.211$ | $7.718$ | $+7.507$ |
| ${}^{4}$He | $0.055348346\ldots$ | $0.085$ | $28.296$ | $+28.211$ |

**Additivity REFUTED.** The `he4_eq_twice_he3_shell` Lean
theorem predicts $\Delta_{\mathrm{cat}}(^4\mathrm{He}) = 2 \cdot
\Delta_{\mathrm{cat}}(^3\mathrm{He})$. Empirically:

- $2 \cdot \Delta_{\mathrm{cat}}(^3\mathrm{He}) = 15.014$ MeV (predicted)
- $\Delta_{\mathrm{cat}}(^4\mathrm{He}) = 28.211$ MeV (actual)
- **Ratio = 3.758** (vs predicted $2.000$)
- Deviation $1.76\sigma$ from prediction; the actual doubly-magic
  stabilization is $\sim 88\%$ MORE than additivity predicts.

Since Z$\leftrightarrow$N symmetry was empirically supported by AME directly
(${}^{3}$He vs ${}^{3}$H Coulomb-corrected substrate-binding difference
$\sim 0.03$ MeV, see audit), the refutation must fall on
**`MagicShellAdditivity`**. The doubly-magic ${}^{4}$He has
super-additive stabilization — proton-shell and neutron-shell
closures couple beyond simple addition.

### Refined proof obligations

1. **Z$\leftrightarrow$N symmetry HOLDS** (empirically AME-confirmed).  Lean
   class `MagicShellStabilization.z_n_symmetry` is the right
   axiom; the spin-involution corollary gives the algebraic basis.

2. **Additivity FAILS** ($88\%$ super-additivity at $Z = N = 2$).
   The `MagicShellAdditivity` extension class encodes an
   empirically refuted axiom — useful as a baseline for measuring
   the size of cross-shell coupling, but not a structural property
   of the physical $\Delta_{\mathrm{shell}}$.

3. **Replace additivity with cross-shell coupling.** A refined
   conjecture:
   $$
     \Delta_{\mathrm{shell}}(Z, N) = \Delta_p \cdot \mathbb{1}_{Z \in \mathrm{magic}}
       + \Delta_n \cdot \mathbb{1}_{N \in \mathrm{magic}}
       + \Delta_{\mathrm{coupling}}(Z, N) \cdot \mathbb{1}_{Z, N \in \mathrm{magic}}
   $$
   with $\Delta_p = \Delta_n$ (Z$\leftrightarrow$N) and the cross-shell
   $\Delta_{\mathrm{coupling}}(Z, N)$ accounting for doubly-magic
   super-additivity.

4. **Extract** $\Delta_p$ as a measured residual from ${}^{3}$He, ${}^{4}$He,
   and the cross-shell
   $\Delta_{\mathrm{coupling}}(2, 2) = \Delta_{\mathrm{cat}}(^4\mathrm{He})
   - 2 \Delta_{\mathrm{cat}}(^3\mathrm{He}) = 28.211 - 15.014 = +13.20$ MeV.

5. **Extend to other magic shells.** Test predictions at $Z = 8$
   (${}^{16}$O), $N = 8$ (${}^{15}$N + ${}^{17}$O), and onwards.  At $Z = 8$ the
   intra-O sub-braid spans the 16 intra-strand generators across
   the 8 protons.

6. **Closed-form for $\Delta_{\mathrm{shell}}$.** Express
   $\Delta_{\mathrm{shell}}(Z, N)$ as a function of the magic-shell
   Markov trace $\mathrm{tr}_M(\sigma_{\mathrm{shell}})$ and the
   $q$-deformed shell-closure invariants (analogous to the Mayer-
   Jensen spin-orbit splittings in the classical nuclear shell
   model).

### Empirical motivation summary

- LP-dual active-set finding: $\sigma_{pp}, \sigma_{nn}$ are
  structurally privileged at exactly magic-shell atoms (PR #638
  family 5).
- Markov-trace Z$\leftrightarrow$N symmetry:
  $\mathrm{tr}_M(\sigma_{pp}) = \mathrm{tr}_M(\sigma_{nn}) =
  0.0622\ldots$ exactly (provable algebraically via the
  spin-involution corollary; 50-dps Hoefsmit evaluation in
  [`prop:spin-involution-lp-dual-invariance`](spin-involution-lp-dual-invariance.md)).
- Brane-tower formula's universal overshoot at small $n_\star$:
  the per-generator $\sum_i \Phi_q(|\hat V_i|)$ tower at
  $n_\star \leq 3$ exceeds AME by $200$–$1000\%$ on
  $\{D, T, {}^3\mathrm{He}\}$, regardless of pair-knot collapse —
  consistent with a missing **subtracted** stabilization
  contribution rather than a missing additive contribution.
  (At doubly-magic ${}^{4}$He under pair-knot collapse, the brane-tower
  UNDER-shoots by $19.4\%$ — consistent with an **added**
  stabilization, since both Z=2 and N=2 shells contribute.)

The sign discrepancy in the empirical $\Delta_{\mathrm{shell}}$
residual (negative for ${}^{3}$He, positive for ${}^{4}$He under product-volume;
sign undetermined under Markov-trace) is the central empirical
puzzle this conjecture seeks to resolve.

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
