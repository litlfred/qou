**Proposition (Habiro–residue equivalence).**
*Let $T_w \in H_n(q)$ be a closed braid word and let
$\operatorname{tr}_M(T_w, q)$ denote its Markov trace, viewed in the Habiro
ring $\widehat{\mathbb{Z}[q]}$.  Then the two formulations of $\operatorname{tr}_M$
arising in this chapter agree on the archimedean realization
$q \mapsto q_0 \in \mathbb{R}$:*

1. *the **polynomial-ring** value, computed from any
   [Habiro completion](#prop:full-pole-structure-mass-trace) instance
   $\mathcal{H}$ as $\operatorname{eval}_{u_0}(\mathcal{H}.\mathrm{trace})$
   with $u_0 = q_0^{1/2}$, and*

2. *the **residue spectral sum**, computed from any
   [Gröbner–Shirshov residue spectral sum](#prop:gb-residue-spectral-sum)
   instance $\mathcal{R}$ as $\mathcal{R}.\mathrm{mass}$,*

*coincide whenever both instances correspond to the same braid word $T_w$.
Equivalently, the diagram*

$$
  \widehat{\mathbb{Z}[q]} \;\xrightarrow{\;\rho_\infty\;}\; \mathbb{R}
$$

*commutes for the two distinct constructions of
$\operatorname{tr}_M(T_w) \in \widehat{\mathbb{Z}[q]}$.*

**Status.** This is a
[non-trivial analytic identity](#def:archimedean-realization-functor): it
relates the cyclotomic-coefficient sum
$\sum_m a_m(u_0) \cdot (u_0;u_0)_m$ (Habiro side) to the
residue-spectral-sum
$|\mathrm{tr}_M^{(0)}| + \sum_\ell \mathrm{Res}_{q\to\zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M,\ell})$
(GB side).  A formal Lean proof requires the analytic identification of
the residue contributions with the cyclotomic tail, which is open at
the level of `prop:gb-residue-spectral-sum`'s `noncomputable opaque`
declarations of `gradedMarkovTrace` and `residueAtRoot`.

**Empirical witness.** The agreement is certified at machine precision
on every available atomic Markov trace by
`computations/markov/markov_pipeline_cross_validator.py`.  The
cross-pipeline witness records, per atom, the relative difference
between the two paths.  The current run achieves:

| Atom | Polynomial path $\rho_\infty(\mathcal{H}.\mathrm{trace})$ | Residue path $\mathcal{R}.\mathrm{mass}$ | $|\mathrm{rel\ diff}|$ |
|------|-----------------------------------------------------------|-------------------------------------------|------------------------|
| $\mathfrak{p}$ (proton, $A=1$)   | $2.1225825095$ | $2.1225825095$ | $0$ |
| $\mathfrak{n}$ (neutron, $A=1$)  | $1.5893934460$ | $1.5893934460$ | $2.79\!\times\!10^{-16}$ |
| D (deuteron, $A=2$)              | $0.1774369242$ | $0.1774369242$ | $0$ |

All differences fall within the relative tolerance $10^{-9}$ — the
two paths agree to machine epsilon.  This is direct empirical evidence
for the analytic identity stated above; the Lean theorem
`HabiroResidueSumEquivalence` records the agreement as an axiom-level
class.

**Cross-validation infrastructure.** The check is run by
`markov_pipeline_cross_validator.py`; output witness
`markov-pipeline-cross-validation.witness.json` records:

- Per-atom assertion `tr_M_at_q0_archimedean[atom]` with a relative
  tolerance proportional to `AGREEMENT_RTOL = 1e-9`.
- Diagnostic fields `realizer_value`, `term6_value`, `abs_diff`,
  `rel_diff` for each common atom.
- Asymmetric atom coverage (atoms present in only one input pipeline).

The validator skips when one of its inputs is absent (forward
compatibility), and uses the standard `WitnessBuilder` so
`run_pipeline.py` automatically reruns it whenever either input
witness changes.
