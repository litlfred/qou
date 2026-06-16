**Conjecture (archimedean agreement, proton instance).**
*Instantiating the generic
[archimedean agreement conjecture](#conj:gs-archimedean-agreement-trace)
on the proton braid $T_w(Z = 1, N = 0)$, the degree-$48$ Markov-normalised
Habiro polynomial trace
$T_{\mathfrak{p}}(u) \in \mathbb{Z}[u]$
evaluates at the substrate value $u_0 = \sqrt{q_0}$,
$q_0 = :val[q_0]{precision=6}\ldots$, to the proton GB mass*

$$
  T_{\mathfrak{p}}\bigl(\sqrt{q_0}\bigr)
  \;\approx\;
  \mathfrak{m}_{\mathrm{GB}}(\mathfrak{p}, q_0)
  \;\approx\; 2.1225825095.
$$

*The same identity holds for the neutron, deuteron, and triton
instances using the corresponding Markov-normalised polynomials.*

**Categorical statement.**
*This is the per-instance specialisation of the substrate axiom of
[Habiro residue sum equivalence](#prop:habiro-residue-sum-equivalence)
for the proton.  It unifies two independent computational pipelines:*

1. *Habiro side: $T_{\mathfrak{p}}$ produced by
   `habiro_coefficients_atomic.py` for $(Z=1, N=0,
   \texttt{include\_inter}=\text{false})$ — a degree-$48$ polynomial
   in $\mathbb{Z}[u]$, evaluated at $u_0 = \sqrt{q_0}$ to $\geq 60$
   decimal places.*
2. *Residue side: $\mathfrak{m}_{\mathrm{GB}}(\mathfrak{p}, q_0)$
   computed by `term6_full_pole_sum.py` from the descended trace
   plus cyclotomic residues at $\zeta_\ell$ for
   $\ell = 1, \ldots, 6$.*

**Status (current Lean encoding).**
*In `habiro-residue-sum-equivalence.lean`, this is the per-instance
witness*

```
noncomputable instance protonExample : HabiroResidueSumEquivalence where
  ...
  archimedean_agreement := by sorry
```

*The `sorry` is the proton-specific instance witness — closing it
requires either:*

1. *Full transcription of $T_{\mathfrak{p}}$ into Lean as 49 integer
   literals plus a `native_decide`/`decide` evaluation at $q_0$, or*
2. *Auto-generation of `examples/proton-trace-coeffs.lean` from
   `habiro-coefficients-atomic.witness.json` via a small Bun/TS
   importer.*

*Effort is "medium" per the
[opaque-declarations audit](../../computations/AUDIT-gb-residue-opaque-declarations.md);
this is a feasible standalone follow-up.*

**Why a conjecture and not a theorem.**
*The numerical agreement is empirically certified to machine precision
in `markov-pipeline-cross-validation.witness.json` (proton
$\mathrm{rel\_diff} = 0$ at machine precision); a rigorous Lean proof
requires either (i) brute-force `native_decide` on the explicit
polynomial — feasible but currently unimplemented, or (ii) the
generic
[archimedean agreement conjecture](#conj:gs-archimedean-agreement-trace)
applied to this instance.*

**Empirical witness.**
*Bit-pattern equality of the two pipelines for the proton at $q_0$ is
recorded in
`computations/markov/markov-pipeline-cross-validation.witness.json`
(rel\_diff = 0.00e+00 to machine precision) and
`computations/term6-full-pole-sum.witness.json`.*
