**Theorem (existence of the graded Markov trace — categorical
existence, Sprint 4 discharge; concrete per-level values supplied
by `gb-residue-spectral-sum.lean` instances per atom).**
*Let $H_n(R, q)$ carry the Gröbner–Shirshov confinement filtration
$J^\bullet(q)$
([confinement level](#def\:confinement-level)).  Then for every
filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$ there exists
a well-defined real-valued functional*

$$
  \mathrm{tr}_{M, \ell} \colon J^\ell(q) / J^{\ell+1}(q)
    \;\longrightarrow\; \mathbb{R}
$$

*obtained as the :refterm[descent]{#descent} of the Markov trace
$\mathrm{tr}_M$ ([Jones–Markov trace](#thm\:jones-markov-trace)) along
the projection $J^\ell(q) \twoheadrightarrow J^\ell(q) / J^{\ell+1}(q)$.
The collection $\ell \mapsto \mathrm{tr}_{M, \ell}(T_w)$ is a finite
sequence indexed by $\mathrm{Fin}(\ell(K, q))$ that depends only on
the GS-normal form of $T_w$.*

**Categorical statement.**
*The Markov trace, as a cyclic 0-cocycle on the Hochschild complex
([GB spectral sequence](#prop\:gb-spectral-sequence)), is filtration
preserving and therefore induces a sequence of well-defined functionals
on each associated-graded piece.  Existence is the content of
[graded Markov trace from GS filtration](#prop\:graded-markov-trace-from-gs-filtration);
this conjecture is its formal Lean counterpart.*

**Status (current Lean encoding).**
*In `gb-residue-spectral-sum.lean`, this is encoded as the abstract
class field*

```
gradedTrace : Fin levelBound → ℝ
```

*on `GBResidueSpectralSum`, with the convenience accessor
`gradedMarkovTrace S ℓ`.  Per the P2.6 refactor, the
previous `noncomputable opaque gradedMarkovTrace ℓ q` global has been
removed; the value is now supplied by each instance.  A fully
constructive `def` would require formalising the GS-filtration of
$H_n(R, q)$ and the :refterm[descent]{#descent} of $\mathrm{tr}_M$ along its associated
graded — this depends on Mathlib infrastructure for filtered
algebras and is tracked downstream
([audit](../../computations/AUDIT-gb-residue-opaque-declarations.md)).*

**Why a conjecture and not a theorem.**
*The narrative claim is rigorous over any commutative ring $R$ for which
the Markov trace and the filtration $J^\bullet(q)$ are defined; what
remains conjectural is its formal Lean realisation.  Promoting to a
theorem requires:*

1. *A Lean formalisation of $\mathrm{ConfinementLevel}$ and the
   ideal filtration $J^\bullet(q) \subseteq H_n(R, q)$.*
2. *A Lean construction of the associated graded
   $\mathrm{gr}^\ell H_n(R, q) = J^\ell(q) / J^{\ell+1}(q)$.*
3. *A Lean proof that $\mathrm{tr}_M$ is filtration-preserving and
   therefore descends.*

*All three are out-of-scope for the current PR; instances supply the
value directly.*

**Empirical witness.**
*The numerical values of $\mathrm{tr}_{M, \ell}(T_w)$ for the proton,
neutron, and deuteron atoms are emitted by
`markov_pipeline_cross_validator.py` and stored under
`computations/markov/markov-pipeline-cross-validation.witness.json`,
agreeing with the Habiro-side values to relative tolerance $\le$ $10^{-9}$
across every available atom.*
