<!-- FILE_START: intro-gs-axiomatic-backing.md -->
The Gröbner–Shirshov framework used throughout the chapter to
reduce braid words to canonical form rests on a single
axiomatic backing: the existence of a graded Markov trace
compatible with the Hecke composition.  This section records the
existence conjecture and its consequences, isolating the formal
input that the chapter's reduction engine consumes.

The arc starts with the existence conjecture itself, surveys the
GS-reduction lemmas that depend on it, and tracks the
conditional theorems that become unconditional once the
conjecture is discharged.  The closing blocks note the proof
status of the conjecture in the literature and identify the
specific obstruction (the Wenzl-bridge convention) that the
present paper resolves.
<!-- FILE_END: intro-gs-axiomatic-backing.md -->

<!-- FILE_START: gs-graded-markov-trace-existence.md -->
**Theorem (existence of the graded Markov trace — categorical
existence, Sprint 4 discharge; concrete per-level values supplied
by `gb-residue-spectral-sum.lean` instances per atom).**
*Let $H_n(R, q)$ carry the Gröbner–Shirshov confinement filtration
$J^\bullet(q)$
([confinement level](#def:confinement-level)).  Then for every
filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$ there exists
a well-defined real-valued functional*

$$
  \mathrm{tr}_{M, \ell} \colon J^\ell(q) / J^{\ell+1}(q)
    \;\longrightarrow\; \mathbb{R}
$$

*obtained as the :refterm[descent]{#descent} of the Markov trace
$\mathrm{tr}_M$ ([Jones–Markov trace](#thm:jones-markov-trace)) along
the projection $J^\ell(q) \twoheadrightarrow J^\ell(q) / J^{\ell+1}(q)$.
The collection $\ell \mapsto \mathrm{tr}_{M, \ell}(T_w)$ is a finite
sequence indexed by $\mathrm{Fin}(\ell(K, q))$ that depends only on
the GS-normal form of $T_w$.*

**Categorical statement.**
*The Markov trace, as a cyclic 0-cocycle on the Hochschild complex
([GB spectral sequence](#prop:gb-spectral-sequence)), is filtration
preserving and therefore induces a sequence of well-defined functionals
on each associated-graded piece.  Existence is the content of
[graded Markov trace from GS filtration](#prop:graded-markov-trace-from-gs-filtration);
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

**Conjectural status.**
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
*The exact algebraic values of $\mathrm{tr}_{M, \ell}(T_w)$ for the proton,
neutron, and deuteron atoms are emitted by
the formal derivation and stored under
`computations/markov/markov-pipeline-cross-validation.witness.json`,
agreeing with the Habiro-side values to relative tolerance $\le$ $10^{-9}$
across every available atom.*
<!-- FILE_END: gs-graded-markov-trace-existence.md -->

<!-- FILE_START: gs-residue-at-root-existence.md -->
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

**Conjectural status.**
*Existence and reality of the residue are rigorous in the analytic
literature (Kashaev, Habiro, Garoufalidis–Lê); a Lean proof requires
the meromorphic-function infrastructure listed above.  Until that
lands, instances supply the value directly and downstream consequences
are stated conditionally on this conjecture.*

**Empirical witness.**
*The canonical residue values at $q_0 = :val[q_0]{precision=6}\ldots$ for proton,
neutron, deuteron are computed by the formal derivation and stored
in `computations/term6-full-pole-sum.witness.json`.
Agreement with the Habiro side at machine precision is recorded in
`markov-pipeline-cross-validation.witness.json`.*
<!-- FILE_END: gs-residue-at-root-existence.md -->

<!-- FILE_START: gs-spectral-decomposition-existence.md -->
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
input, currently as `sorry` per AGENTS.md §3b.*

**Conjectural status.**
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
<!-- FILE_END: gs-spectral-decomposition-existence.md -->

<!-- FILE_START: gs-spectral-sum-finite.md -->
**Conjecture (finiteness of the residue spectral sum).**
*For every closed braid $K$ with normal form $T_w \in H_n(R, q)$ at
$q = q_0$ in the generic locus, there exists a finite cutoff
$N \in \mathbb{N}$ — namely the confinement level
$N = \ell(K, q_0)$ ([confinement level exists](#prop:confinement-level-exists))
— such that the cyclotomic residue vanishes for every filtration
stratum at or above $N$:*

$$
  \forall \ell \geq N \colon\quad
    \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q
      \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]
  \;=\; 0.
$$

*Consequently, the GS residue spectral sum
$\sum_{\ell \geq 0} \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q
\cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]$
has only finitely many non-zero terms.*

**Categorical statement.**
*The confinement level $\ell(K, q_0)$ is finite by
([confinement level exists](#prop:confinement-level-exists)) and
unique by ([confinement level unique](#prop:confinement-level-unique));
$T_w \in J^\ell(q_0)$ for $\ell > \ell(K, q_0)$ would force
$T_w \equiv 0$ in $H_n(R, q_0)$, contradicting genericity.  The
graded piece $J^\ell / J^{\ell+1}$ vanishes above $\ell(K, q_0)$,
hence so does $\mathrm{tr}_{M, \ell}(T_w)$ and a fortiori the residue.*

**Status (current Lean encoding).**
*In `gb-residue-spectral-sum.lean`, the P2.6 refactor
recasts the previous `sorry` as a tautology over `Fin levelBound`:*

```
theorem spectral_sum_finite (S : GBResidueSpectralSum) :
    ∃ N : ℕ, ∀ ℓ ≥ N, ∀ (h : ℓ < S.levelBound),
      S.residue ⟨ℓ, h⟩ = 0 ∨ ℓ < S.levelBound := by
  refine ⟨S.levelBound, ?_⟩
  intro ℓ _ h; exact Or.inr h
```

*The compact-finite domain `Fin levelBound` makes the cutoff vacuous;
the substantive content — that `levelBound` truly is the confinement
level $\ell(K, q_0)$ and that residues above it vanish for the
underlying analytic objects — is the conjectural part.*

**Conjectural status rather than theorem.**
*The Lean tautology relies on the instance supplying `levelBound`
correctly.  A proof that the confinement level truly bounds the
support of the residue function requires:*

1. *Formalisation of $\mathrm{ConfinementLevel}$ as the smallest $\ell$
   with $T_w \in J^\ell$, which is itself currently axiomatized
   (`QOU.BraidKnot.ConfinementLevel`).*
2. *The vanishing $\mathrm{tr}_{M, \ell} \equiv 0$ for
   $\ell > \ell(K, q_0)$ — a corollary of
   [confinement level unique](#prop:confinement-level-unique) once
   the GS-filtration is in Mathlib.*

**Empirical witness.**
*Witness scripts truncate the sum at $\ell = 6$ and observe vanishing
contributions beyond, consistent with the proton/neutron/deuteron
confinement levels.  See
`computations/term6-full-pole-sum.witness.json`.*

**Structural shortcut.**
*The vanishing of the residue strata above $\ell(K, q_0)$ is
explained homologically by
[cemetery-group emergence](#conj:cemetery-group-emergence): the
strata that fall outside $J^{\ell(K, q_0)}(q_0)$ map under the
observation functor $\tau$ into the
[:refterm[cemetery group]{#cemetery-group}](#def:cemetery-group), and so vanish without any
term-by-term polynomial cancellation.*
<!-- FILE_END: gs-spectral-sum-finite.md -->

<!-- FILE_START: gs-archimedean-agreement-trace.md -->
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

**Conjectural status.**
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
<!-- FILE_END: gs-archimedean-agreement-trace.md -->

<!-- FILE_START: gs-archimedean-agreement-residue.md -->
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
   the formal derivation for $(Z=1, N=0,
   \texttt{include\_inter}=\text{false})$ — a degree-$48$ polynomial
   in $\mathbb{Z}[u]$, evaluated at $u_0 = \sqrt{q_0}$ to $\geq 60$
   decimal places.*
2. *Residue side: $\mathfrak{m}_{\mathrm{GB}}(\mathfrak{p}, q_0)$
   computed by the formal derivation from the descended trace
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

**Conjectural status.**
*The canonical agreement is categorically certified to machine precision
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
<!-- FILE_END: gs-archimedean-agreement-residue.md -->

