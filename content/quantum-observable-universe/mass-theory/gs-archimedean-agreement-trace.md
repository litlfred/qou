**Conjecture (archimedean agreement, generic instance).**
*For every closed braid $K$ admitting a Habiro polynomial trace
$T_K(u) \in \mathbb{Z}[u]$ ([Habiro ring](#def:habiro-ring)) and a
Gröbner–Shirshov mass value $\mathfrak{m}_{\mathrm{GB}}(K, q_0) \in \mathbb{R}$
([GB residue spectral sum](#prop:gb-residue-spectral-sum)), the
archimedean evaluation*

$$
  \tau\bigl(T_K\bigr)\bigl(u_0\bigr)
  \;:=\;
  T_K\bigl(\sqrt{q_0}\bigr)
  \;\in\;\mathbb{R},
$$

*obtained by mapping the integer-coefficient polynomial along
$\mathbb{Z} \hookrightarrow \mathbb{R}$ and evaluating at
$u_0 = \sqrt{q_0}$, agrees with the GB mass:*

$$
  T_K\bigl(\sqrt{q_0}\bigr)
  \;\approx\;
  \mathfrak{m}_{\mathrm{GB}}(K, q_0).
$$

**Categorical statement.**
*This is the substrate axiom of
[Habiro residue sum equivalence](#prop:habiro-residue-sum-equivalence):
the archimedean fibre functor
$\tau \colon R \hookrightarrow \mathbb{C}$
([archimedean realization functor](#def:archimedean-realization-functor))
intertwines the Habiro side (polynomial evaluation in
$\mathbb{Z}[u]$) and the spectral-sequence side
(descended trace plus cyclotomic residues).  Existence of this common
value across both pipelines is the analytic content of the
$E_\infty$-pairing identification on opposite sides of $\tau$
([GB spectral sequence](#prop:gb-spectral-sequence)).*

**Status (current Lean encoding).**
*In `habiro-residue-sum-equivalence.lean`, this is the class field
axiom*

```
archimedean_agreement :
  (habiro_trace.map (Int.castRingHom ℝ)).eval (Real.sqrt q_0) = gb_mass
```

*on `HabiroResidueSumEquivalence`.  Each instance supplies it as a
substrate axiom (`sorry` per AGENTS.md §3b), backed by the empirical
cross-pipeline witness.*

**Why a conjecture and not a theorem.**
*A Lean proof reduces to (and requires):*

1. *[Spectral decomposition existence](#conj:gs-spectral-decomposition-existence)
   — the closed-form expression of $\mathfrak{m}_{\mathrm{GB}}$ as
   $|\mathrm{descended}| + \sum_\ell \mathrm{residue}(\ell)$.*
2. *The polynomial-side `tail_in_ideal` axiom of the Habiro completion
   — that the truncated polynomial trace converges in the Habiro
   topology to the same archimedean value.*
3. *Closing the analytic identification of $\Phi_q \cdot \mathrm{tr}_{M,\ell}$
   residues with the corresponding Habiro coefficients.*

*Effort is "large" per the
[opaque-declarations audit](../../computations/AUDIT-gb-residue-opaque-declarations.md).*

**Empirical witness.**
*Cross-pipeline validation
(`computations/markov/markov-pipeline-cross-validation.witness.json`)
records $\mathrm{rel\_diff} \leq 10^{-9}$ to machine precision on
every available atom (proton, neutron, deuteron), and rel\_diff = 0
to 60 decimal places on the atomic-vs-interpolate checkpoint.*
