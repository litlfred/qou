The constituent baseline
$Z\,m_{\mathfrak{p}} + N\,m_{\mathfrak{n}} + Z\,m_e$ is the
free-particle sum from CODATA.  The binding energy is the
algebraic difference of the bound atom's mass formula and its
free baseline.  Each of the six terms contributes additively to
the categorical mass per
[unified six-term decomposition](#thm:six-term-mass-formula-complete);
isolating the **physical scale** of each contribution is exactly
the per-derivation reading above:

- *$T_1$ binding (descended Markov):* the categorical mass
  formula
  $\mathcal{M}(Z, N) = E_{0,\beta} \cdot \mathfrak{m}(\beta_{Z,N})$
  with $E_{0,\beta} = 0.7823$ MeV the free-neutron β-decay $Q$
  per [categorical mass, Markov](#prop:categorical-mass-markov)
  reads $T_1$ in cat units.  The binding contribution is the
  bound–free differential.
- *$T_2 + T_3$ binding (brane tower):* per
  the *atomic-braid mass formula* in the Particles chapter, the binding
  correction is $\alpha \cdot \sum_i \ln\lvert \hat V_i \rvert$
  where $\alpha = m_e \cdot 8G$ is the
  [Borromean–Catalan binding scale](#prop:binding-scale-catalan)
  and $G \approx 0.9160$ is Catalan's constant.  Per
  [the divergence-audit branch's reconciliation](#prop:mass-endomorphism-tower),
  $\alpha\,\ln\lvert V \rvert$ is the leading-order expansion of
  $-\alpha\,\mathrm{Li}_2^q(-\lvert V \rvert)$, so the same $\alpha$
  scale governs both the leading-order and the corrected
  q-dilogarithm form.
- *$T_4$ binding (Frobenius co-Casimir):* the universal
  [Frobenius co-Casimir](#thm:frobenius-codim-universal)
  $T_4 = m_e \cdot \tau(C_{\dim_q})$ has $m_e$ baked into the
  formula.  Empirically the bound–free differential vanishes for
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
and is positive for bound systems.
$\qquad\blacksquare$
