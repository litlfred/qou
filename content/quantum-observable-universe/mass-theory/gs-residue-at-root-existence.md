**Conjecture (cyclotomic residue exists at each level).**
*For each filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$ and
each primitive $\ell$-th root of unity
$\zeta_\ell \in \mu_{\ell}(\mathbb{C})$, the cyclotomic projection*

$$
  \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q(u)
    \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]
  \;\in\; \mathbb{R}
$$

*is a well-defined real number, where $\Phi_q$ is the quantum
dilogarithm
([quantum dilogarithm stratified](#prop:quantum-dilogarithm-stratified))
and $\mathrm{tr}_{M, \ell}$ is the graded Markov trace at level $\ell$
([graded Markov trace existence](#conj:gs-graded-markov-trace-existence)).
The value depends only on $\ell$ and the equivalence class of $T_w$
modulo $J^{\ell+1}(q)$.*

**Categorical statement.**
*This is the formal Lean counterpart of
[residue at root](#prop:residue-at-root): the cyclotomic projection
of $\Phi_q \cdot \mathrm{tr}_{M,\ell}$ in the Habiro completion
([Habiro ring](#def:habiro-ring)) is the residue contribution that the
filtered Hochschild spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) attaches to
filtration stratum $\ell$.*

**Status (current Lean encoding).**
*In `gb-residue-spectral-sum.lean`, this is encoded as the abstract
class field*

```
residue : Fin levelBound → ℝ
```

*on `GBResidueSpectralSum`, with the convenience accessor
`residueAt S ℓ`.  Per the P2.6 refactor, the previous
`noncomputable opaque residueAtRoot ℓ ζ q` global has been removed;
the value is supplied by each instance.  A fully constructive `def`
would require:*

1. *A Mathlib formalisation of $\Phi_q$ as a meromorphic function on
   $\{|q| < 1\} \cup S^1 \setminus \mu_\infty$ — currently absent.*
2. *A `meromorphic_quantum_dilogarithm_at_roots_of_unity` lemma
   identifying the pole structure at each $\zeta_\ell$.*
3. *The Habiro completion as a Lean topological ring with a
   well-defined evaluation map at $u_0 = q_0^{1/2}$.*

*See the
[opaque-declarations audit](../../computations/AUDIT-gb-residue-opaque-declarations.md)
for the full Mathlib gap analysis.*

**Why a conjecture and not a theorem.**
*Existence and reality of the residue are rigorous in the analytic
literature (Kashaev, Habiro, Garoufalidis–Lê); a Lean proof requires
the meromorphic-function infrastructure listed above.  Until that
lands, instances supply the value directly and downstream consequences
are stated conditionally on this conjecture.*

**Empirical witness.**
*The numerical residue values at $q_0 = :val[q_0]{precision=6}\ldots$ for proton,
neutron, deuteron are computed by `term6_full_pole_sum.py` and stored
in `computations/term6-full-pole-sum.witness.json`.
Agreement with the Habiro side at machine precision is recorded in
`markov-pipeline-cross-validation.witness.json`.*
