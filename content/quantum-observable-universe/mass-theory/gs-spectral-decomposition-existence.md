**Conjecture (spectral decomposition of the mass).**
*For every closed braid $K$ with normal form $T_w \in H_n(R, q)$ at
$q = q_0$ in the generic locus, the categorical mass admits the
decomposition*

$$
  \mathfrak{m}(K, q_0)
  \;=\;
  \bigl|\,\mathrm{tr}_M^{(0)}(T_w, q_0)\,\bigr|
  \;+\;
  \sum_{\ell = 0}^{\ell(K, q_0) - 1}
    \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q
      \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr],
$$

*where $\mathrm{tr}_M^{(0)}$ is the descended (level-$0$) Markov trace,
and the sum runs over the finitely many filtration strata up to the
confinement level $\ell(K, q_0)$
([confinement level exists](#prop:confinement-level-exists)).*

**Categorical statement.**
*This is the formal Lean counterpart of
[GB residue spectral sum](#prop:gb-residue-spectral-sum) and
[graded-trace residue split](#prop:graded-trace-residue-split):
the $E_\infty$-pairing of $\mathrm{tr}_M$ with $T_w$ in the filtered
Hochschild spectral sequence ([GB spectral sequence](#prop:gb-spectral-sequence))
splits into the level-$0$ descended piece (smooth/Strutinsky
liquid-drop part) and the higher-stratum cyclotomic residues
(shell-correction part).*

**Status (current Lean encoding).**
*In `gb-residue-spectral-sum.lean`, this is the class-field axiom*

```
spectral_decomposition :
  mass = |descended| + ∑ ℓ : Fin levelBound, residue ℓ
```

*on `GBResidueSpectralSum`. It is the analytic content of the
`noncomputable opaque` block: instances must supply this identity as
input, currently as `sorry` per CLAUDE.md §3b.*

**Why a conjecture and not a theorem.**
*A Lean proof requires:*

1. *[graded Markov trace existence](#conj:gs-graded-markov-trace-existence)
 and [residue at root existence](#conj:gs-residue-at-root-existence)
 as formal Lean defs (not class fields).*
2. *The classical Habiro–Mittag-Leffler bridge identifying the
 cyclotomic tail of $\mathrm{tr}_M(T_w, q_0)$ with the residue
 sum — i.e. an analytic identification of the spectral-sequence
 $E_\infty$-pairing with the contour integral over the Descartes
 elliptic curve.*

*Effort is "very large" per the
[audit](../../computations/AUDIT-gb-residue-opaque-declarations.md);
the empirical witness (machine-precision agreement on every available
atom) is the working substitute.*

**Empirical witness.**
*Cross-pipeline validation at `proton`, `neutron`, `deuteron` records
relative difference $\le$ $10^{-9}$ to machine precision on every
checkpoint. See
`computations/markov/markov-pipeline-cross-validation.witness.json`.*
