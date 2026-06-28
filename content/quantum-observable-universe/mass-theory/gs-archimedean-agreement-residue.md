**Conjecture (archimedean agreement, proton instance).**
*Instantiating the generic
[archimedean agreement conjecture](#conj:gs-archimedean-agreement-trace)
on the proton braid $T_w(Z = 1, N = 0)$, the Markov-normalised
Habiro polynomial trace
$T_{\mathfrak{p}}(u) \in \mathbb{Z}[u]$
evaluates at the substrate value $u_0 = \sqrt{q_0}$ to its corresponding cyclotomic residue sum.*

*The same identity holds for the neutron, deuteron, and triton
instances using the corresponding Markov-normalised polynomials.*

**Categorical statement.**
*This is the per-instance specialisation of the substrate axiom of
[Habiro residue sum equivalence](#prop:habiro-residue-sum-equivalence)
for the proton.*

**Status (current Lean encoding).**
*In `habiro-residue-sum-equivalence.lean`, this is the per-instance
witness*

```lean
noncomputable instance protonExample : HabiroResidueSumEquivalence where
  ...
  archimedean_agreement := by sorry
```

*The `sorry` is the proton-specific instance witness — closing it
requires a formal derivation or direct evaluation in Lean.*

**Conjectural status.**
*A rigorous Lean proof
requires either (i) direct `native_decide` on the explicit
polynomial, or (ii) the generic
[archimedean agreement conjecture](#conj:gs-archimedean-agreement-trace)
applied to this instance.*
