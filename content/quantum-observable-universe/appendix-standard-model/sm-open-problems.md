The following ledger consolidates the epistemic status of every structural ingredient this appendix uses; the per-parameter status of the 26 Standard-Model parameters is tabulated in the parameter sections above and is not repeated here. Items marked *open* name the missing object precisely; none of them is discharged elsewhere in the corpus.

| Ingredient | Status | Where |
|---|---|---|
| Gauge symmetry as action groupoid; reversal, gauge equivalence, residual-symmetry monoid | proved (Lean, sorry-free) | [gauge action groupoid](#def:gauge-action-groupoid) |
| Braid group onto $H_n(q)$ by the Hecke relation | standard | [Hecke algebra from braiding](#rem:hecke-algebra-from-braiding) |
| Fibre gauge group $\mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ | proved in the framework | [$\mathrm{SU}(2)$ emergence](#thm:su2-emergence) |
| Faithful Hecke realization of gauge automorphisms | conjectural (class, no instance) | [Hecke realization](#conj:gauge-hecke-realization) |
| Coulomb charge $Q = w/2$ | derived, no fitted scale | [Coulomb charge](#def:coulomb-charge) |
| Writhe-to-isospin map $w \mapsto I_3$ | derived (sign and ratio, scale-free) | hypercharge audit, 2026-06-02 |
| Hypercharge $Y$ | open: writhe map falsified; missing second crossing invariant | hypercharge audit, 2026-06-02 |
| $\mathrm{SU}(3)$ colour factor from three-strand structure | open: no construction; octonion fragments only | colour-complex-structure Lean fragments |
| Truncation ("freeze-out") mechanism and suppression rate | open: heuristic, no derivation | [selection-rules remark](#rem:sm-lagrangian-selection-rules) |
| Electroweak identifications $W, Z, H = T(2,4), T(2,6), T(2,8)$ | conjectural; ratio-level numerics within a factor of two | [electroweak triplet](#conj:electroweak-higgs-torus-link-triplet) |
| Mass hierarchies from morphism amplitudes | open: must reduce to the canonical volume–density / Hecke-energy mass chain | canonical mass facade |
| 2-group refinement (morphisms between morphisms) | unformalised; groupoid is the 1-truncation | [self-dual 2-group remark](#rem:self-dual-2group) |
| Three-generation structure (why three copies of each fermion?) | open: prior to all mixing parameters; nowhere addressed | [neutrino-sector section](#prose:sm-params-neutrino) |

Three of these deserve emphasis, because they are the ones a derivation of the Standard Model cannot do without. The hypercharge assignment requires a second crossing invariant independent of the writhe; without it the $\mathrm{U}(1)$ factor is realised only as $I_3$, not as $Y$, and electroweak mixing is out of reach. The $\mathrm{SU}(3)$ factor has no categorical construction at all; the three-strand (colour) structure of the baryon braids is suggestive but has not produced a group action. And the truncation mechanism — why the observable-scale symmetry should be a finite-dimensional Lie group rather than the full groupoid symmetry — has no derivation; every use of the phrase "freeze-out" in this appendix is a heuristic label for that gap, not an explanation.
