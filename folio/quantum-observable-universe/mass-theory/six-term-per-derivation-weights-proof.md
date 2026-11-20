*Argument (not a proof).*
The constituent baseline
$Z\,m_{\mathfrak{p}} + N\,m_{\mathfrak{n}} + Z\,m_e$ is the
free-particle sum.  The binding energy is the
algebraic difference of the bound atom's mass formula and its
free baseline.  Each of the six terms contributes additively to
the categorical mass per
[unified six-term decomposition](#conj:six-term-mass-formula-complete);
isolating the **physical scale** of each contribution is exactly
the per-derivation reading above:

- *$T_1$ binding (descended Markov):* the categorical mass
  formula
  $\mathfrak{m}(Z, N) = E_{0,\beta} \cdot \mathfrak{m}(\beta_{Z,N})$
  with $E_{0,\beta}$ the β-decay scale
  per [categorical mass, Markov](#prop:categorical-mass-markov)
  reads $T_1$ in cat units.  The binding contribution is the
  bound–free differential.
- *$T_2 + T_3$ binding (brane tower):* per
  the *atomic-braid mass formula* in the Particles chapter, the binding
  correction is $\alpha \cdot \sum_i \ln\lvert \hat V_i \rvert$
  where $\alpha = m_e \cdot 8G$ is the
  [Borromean–Catalan binding scale](#conj:binding-scale-catalan) (itself a conjecture)
  and $G \approx 0.9160$ is Catalan's constant.  Per
  [the mass-endomorphism tower](#prop:mass-endomorphism-tower),
  $\alpha\,\ln\lvert V \rvert$ is the leading-order expansion of
  $-\alpha\,\mathrm{Li}_2^q(-\lvert V \rvert)$, so the same $\alpha$
  scale governs both the leading-order and the corrected
  q-dilogarithm form.
- *$T_4$ binding (Frobenius co-Casimir):* the universal
  [Frobenius co-Casimir](#thm:frobenius-codim-universal)
  $T_4 = m_e \cdot \sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$, a
  formal sum over all partitions, has $m_e$ baked into the formula.
  Under convention D this is not $m_e \cdot \tau(C_{\dim_q})$, since
  $\tau(p_\lambda) = 0$ on every block with three or more rows.  Empirically the bound–free differential vanishes for
  the atomic-braid $\tau$, so $T_4$ contributes no binding at
  this stage (open question — see remarks).
- *$T_5$ binding (chirality):* per
  [chirality dual-space derivation](#prop:chirality-dual-space-derivation),
  $T_5 = (a_K - 1) \cdot T_1$ as a multiplicative correction on
  $T_1$.  With $T_1$ in cat units and $E_{0,\beta}$ as $T_1$'s MeV
  scale, the binding contribution is
  $E_{0,\beta} \cdot (a_K - 1) \cdot T_1^{\rm atom}$.
- *$T_6$ binding (cyclotomic tail):* per
  [full pole structure](#prop:full-pole-structure-mass-trace),
  $T_6$ comes pre-converted to MeV via the canonical Habiro
  residue evaluation.  No additional scaling needed.

The total $B(Z, N)$ is the sum of these per-term contributions
and is positive for bound systems.  The argument assumes the
scale assignment of each term; it does not derive it, and the
Catalan scale it uses is itself conjectural.

**Comparison boundary.** The measured inputs enter here and only here.

The assembly is implemented in
the formal derivation
as `assemble_per_derivation_weights(Z, N)` with hardcoded
constants $E_{0,\beta} = 0.78233341$ MeV (CODATA β-decay $Q$),
$\alpha = m_e \cdot 8G = 3.74446989$ MeV, $m_e = {{ qou.library.codata-2022.electron-mass-energy-equivalent-in-mev | precision: 6 }}\;\text{MeV}$ MeV.
Across the proton..${}^{9}$Be spectrum (12 atoms):

See [Table 3](#tbl:six-term-per-derivation-weights-table3-data).

**Mean $\lvert\delta\mathfrak{m}/\mathfrak{m}\rvert = 0.184\%$,
max $= 0.525\%$ (${}^{4}$He).**

These percentages are relative to the **total atomic mass**, whose
constituent baseline $Z\,m_{\mathfrak{p}} + N\,m_{\mathfrak{n}} + Z\,m_e$
is taken from CODATA, so they measure the binding only weakly. Read
from the same Table 3 as a **binding** energy
$B = Z\,m(^1\mathrm{H}) + N\,m_{\mathfrak{n}} - \mathfrak{m}$,
the assembly gives $B_{\mathrm{pred}}(\mathrm{D}) = 2.308$ MeV
($+3.7\%$ against AME $2.225$ MeV), but misses every heavier atom
by $-22\%$ to $-69\%$: ${}^{3}$H $4.160$ vs $8.482$ ($-50.9\%$),
${}^{3}$He $5.996$ vs $7.718$ ($-22.3\%$), ${}^{4}$He $8.716$ vs
$28.296$ ($-69.2\%$), ${}^{6}$Li $18.790$ vs $31.994$ ($-41.3\%$),
${}^{9}$Be $38.835$ vs $60.210$ ($-35.5\%$) MeV. The comparison
with the standalone atomic-braid formula (0.13–0.16% mean) and with
the single-$E_0$ assembly (14.7% mean) is likewise a comparison on
total mass, not on binding.

**Open questions.**

1. *$T_4$ binding contribution vanishes empirically.* The
   `term4_frobenius_codim` evaluation gives the same value for
   bound and free configurations, so the differential
   $T_4^{\rm atom} - T_4^{\rm free} = 0$ identically.  Either
   $T_4$ is independent of inter-nucleon crossings by
   construction (in which case it cancels out of the binding
   formula and contributes only to the total mass via the
   $Z\,m_{\mathfrak{p}}$ baseline), or the implementation is
   missing a coupling.  Investigation pending.
2. *$T_6$ Habiro residue witness coverage.* The
   `_load_canonical_t6_MeV` helper currently returns 0 for
   $A \geq 5$ atoms because the Habiro residue witness lacks
   data for them.  Once populated, $T_6$ will start
   contributing to the heavier-atom predictions; expect
   ${\sim}\,$few-keV-level corrections per atom based on the
   $A \leq 4$ pattern.
3. *${}^{4}$He outlier (0.525 %).* Largest residual in the spectrum.
   Worth a focused look — possibly a missing $T_4$ contribution
   that would manifest only at the doubly-magic ${}^{4}$He
   configuration.
