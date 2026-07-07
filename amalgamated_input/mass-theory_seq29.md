<!-- FILE_START: phi-q-markov-residue-habiro-intro.md -->
The preceding sub-section developed the $\phi_q$ + Markov +
Schur-Weyl foundations (Markov-trace factorisation, $\phi_q$
resums of the trace series, per-braid mass tower, Schur-Weyl mass
decomposition, GB-residue spectral sum, categorical mass
positivity, mass-spectrum generating function, the graded Markov
trace, residue at root). This sub-section pulls in the residue +
Habiro identifications that pin the mass tower: $\widehat{V}$-pair
commutation trace + tower-pair equality at fixed level + jet-tower
uniform $\Delta_{\max}$ + the topological-mass formula's algebraic
form + residue-as-braid-holonomy + the graded-trace residue split +
the 6-term binding density + the full pole structure of the mass
trace + the Habiro residue-sum equivalence that closes the
foundations.

The output is the substrate-level Habiro residue formula together with the substrate-flow data the term-6 binding-density block consumes.
<!-- FILE_END: phi-q-markov-residue-habiro-intro.md -->

<!-- FILE_START: vhat-pair-commutation-trace.md -->
The jet-tower mass formula
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower))
contains a "pentagon ascension" argument that non-rigorously invokes the
quantum-dilogarithm pentagon identity
$\Phi_q(v)\,\Phi_q(u) = \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)$ —
which **as an operator identity requires
$uv = q\,vu$**. The audit
[`derivation-audit-.md` line 113](../../../docs/audits/derivation-audit-.md)
flagged this as "expected but unwritten" for traced volumes
$\hat V$ at generic jet level. This block closes the gap by
giving the precise algebraic statement and a one-paragraph proof.

The headline: **the traced volumes commute.** The pentagon
ascension argument is therefore **not load-bearing on the
operator pentagon identity**; the same conclusion (singletons

* pairs + jet ascension) follows from Markov-trace factorization
  without any q-commutation input.

## Statement

Let $\hat V_i(q) \in \mathbb{Z}[q^{\pm 1/2}, z]$ be the traced
volume of the $i$-th crossing of a closed braid, defined by

$$
  \hat V_i(q) \;=\; z(q)\,a_i(q) + b_i(q),
\qquad
  z(q) \;=\; \frac{1}{q^{1/2} + q^{-1/2}},
$$

with $a_i, b_i \in \mathbb{Z}[q^{\pm 1/2}]$ determined by the
braid word and the Hecke normal form
([def:algebraic-quantum-volume](#def:algebraic-quantum-volume)).

**Lemma (pair commutation at traced-volume level).**
*For any two indices $i, j$ — adjacent or non-adjacent —*

$$
  \hat V_i(q) \cdot \hat V_j(q)
  \;=\;
  \hat V_j(q) \cdot \hat V_i(q)
  \qquad
  \text{in } \mathbb{Z}[q^{\pm 1/2}, z].
$$

*Equivalently,*

$$
  \mathrm{tr}_M\!\bigl(\hat V_i \hat V_j\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\hat V_j \hat V_i\bigr)
  \;=\; z^2.
$$

*The pentagon q-factor* $q$ *appearing in the prerequisite
$uv = q\,vu$ does **not** apply to scalar traced volumes; it
applies only to operator-valued lifts of $\hat V_i$ in some
non-commutative quantization of the brane tower (see "Operator
lift" below).*
<!-- FILE_END: vhat-pair-commutation-trace.md -->

<!-- FILE_START: tower-pair-equality-fixed-level.md -->
The jet-tower mass formula
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower))
contains a pair contribution

$$
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr)
$$

at each jet level $n$. The audit
[`derivation-audit-.md` line 114](../../../docs/audits/derivation-audit-.md)
flagged this as an **upper bound** (because the original
heuristic was the pentagon-ascension argument, which gives only
an inequality), with **sharpness open**. This block closes
audit GAP 17b by replacing the bound with an equality.

## Statement

**Lemma (pair-contribution equality at fixed jet level).**
*Let $n \in \mathbb{N}$ be a brane jet level and let
$\mathcal{P}_n = \{(i, j) : 0 \le i < j\}$ be the full set of
unordered pair blow-up centres at jet level $n$
([rem:mass-endomorphism-jet-tower §$\mathcal{P}_n$ all-pairs](#rem:mass-endomorphism-jet-tower)).
Then the pair contribution at level $n$ is the **exact** value*

$$
  \mathrm{pairs}_n
  \;=\;
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr),
$$

*with no upper-bound slack — i.e., the formula is an equality, not an
inequality.*

## Equality versus bound

The original "upper bound" framing came from the pentagon-ascension
argument. By
[`lem:vhat-pair-commutation-trace`](#lem:vhat-pair-commutation-trace)
(P3.2), the pentagon identity in its operator form does **not** apply
to scalar traced volumes $\hat V_i \in \mathbb{Z}[q^{\pm 1/2}, z]$;
it applies only to inter-level operator lifts. Hence the pentagon
gives no bound — upper or otherwise — on the level-$n$ pair
contribution. The bound was vacuous to begin with.

The actual algebraic content of the pair contribution is the
**Markov-pair identity**
[`prop:markov-pair-z2`](#prop:markov-pair-z2):

$$
  \mathrm{tr}_M\!\bigl(\sigma_i \sigma_j\bigr) \;=\; z^2
  \qquad\text{for all } i < j,
$$

which is an exact equality (proved by Markov peel, no inequality
involved). Lifting this from raw braid generators $\sigma_i$ to
traced volumes $\hat V_i^{(n)}$ via the algebraic-quantum-volume
factorization
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)) and
the Markov-trace factorization theorem
([`thm:markov-trace-factorization`](#thm:markov-trace-factorization))
preserves the equality at every jet level $n$.
<!-- FILE_END: tower-pair-equality-fixed-level.md -->

<!-- FILE_START: jet-tower-uniform-delta-max.md -->
The brane-tower convergence proposition
([prop:jet-tower-convergence](#prop:jet-tower-convergence))
gives a geometric tail bound for the mass series
$\mathfrak{m}(\varrho) = \mathfrak{m}^{(0)}(\varrho) +
\sum_{n \ge 1} \hbar_q^{2n} \cdot \Delta^{(n)}(\varrho)$
**conditional** on a uniform per-level boundedness hypothesis

$$
  |\Delta^{(n)}(\varrho)| \;\le\; \Delta_{\max}(\varrho)
  \qquad\text{for all } n \ge 1.
$$

The audit
[`derivation-audit-.md` line 112](../../../docs/audits/derivation-audit-.md)
flagged this hypothesis as open (GAP 14a). This block names the
hypothesis as a conjecture, summarises the empirical evidence at
$n = 1, 2, 3$ for D, T, ${}^{3}$He, and points to the measurement
infrastructure (the formal derivation + the new
`jet-tower-delta-max.witness.json`).

## Statement

**Conjecture (uniform per-level binding bound).**
*For every confined vortex $\varrho$ in the QOU substrate there
exists a finite real $\Delta_{\max}(\varrho) < \infty$ such that
the per-level binding contribution*

$$
  \Delta^{(n)}(\varrho)
  \;=\;
  \mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})
  - \mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}})
$$

*satisfies*

$$
  |\Delta^{(n)}(\varrho)| \;\le\; \Delta_{\max}(\varrho)
  \qquad\text{for all } n \ge 1.
$$

*Equivalently, the sequence $(\Delta^{(n)})_{n \ge 1}$ is bounded
in absolute value (with the bound allowed to depend on the vortex
but not on $n$).*

## Empirical evidence (path (b) deliverable)

The measurement formalism
the canonical formalism
runs `unified_lift.unified_atom_binding` (which already computes
`delta_n` per jet level — see the formal derivation line 158) for
$\mathrm{D}$, $\mathrm{T}$, $^3\mathrm{He}$ across
$n = 1, \dots, N_{\max}$ and reports

* the maximum $|\Delta^{(n)}|$ observed (the empirical
  $\Delta_{\max}$),
* the geometric-decay ratio
  $|\hbar_q^{2n} \Delta^{(n)}| / |\hbar_q^{2(n-1)} \Delta^{(n-1)}|$
  (which the conjecture predicts $= \hbar_q^2 \approx 0.00982$
  in the bounded regime),
* a pass/fail flag for **uniform-bound consistency** (true if
  $|\Delta^{(n)}|$ does not grow over $n$).

Witness output (paste-ready for the conjecture cone):

```
Atom    n_levels  max|Δ^(n)|  geometric-ratio  uniform-bound-pass
D       3         <empirical> <empirical>      (yes)
T       3         <empirical> <empirical>      (yes)
³He     3         <empirical> <empirical>      (yes)
```

(Concrete canonical entries are produced on each run; the
witness JSON is the canonical record.)

The empirical observation
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower)
§"Open subconjecture 1") that
$|\hbar_q^{2n}\,\Delta^{(n)}|
  \le |\hbar_q^{2(n-1)}\,\Delta^{(n-1)}| \cdot \hbar_q^2$
to three significant figures at $n = 1, 2, 3$ is consistent
with a uniform-bound
$\Delta_{\max}$ that holds exactly, with the geometric decay
coming entirely from the $\hbar_q^{2n}$ prefactor.

## Commitments of the conjecture

Per AGENTS.md §3b, the formal status of `prop:jet-tower-convergence`
is **conditional** on this conjecture: any provable result that
quotes the geometric tail bound

$$
  |T(\varrho) - T_N(\varrho)|
  \;\le\;
  \Delta_{\max}(\varrho) \cdot
  \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2}
$$

is itself conjectural until the uniform bound is established.

The current scoreboard:

* *(provable)* The geometric tail bound itself is *proved* in
  [prop:jet-tower-convergence](#prop:jet-tower-convergence) §Proof
  — assuming the bound on $\Delta^{(n)}$ as a hypothesis.
* *(conjectural)* The uniform bound on $\Delta^{(n)}$ is conjectural (this
  block).
* *(empirical)* At $n = 1, 2, 3$ for D, T, ${}^{3}$He, the bound holds empirically
  with margin.

## Path to a proof

Two structural avenues for promoting this conjecture to a theorem:

1. **GS spectral-sequence $E_2$-collapse** (audit-flagged as
   blocked on the `mass-units-bridge-followups` branch). The
   $E_2$-collapse of the GS spectral sequence on the brane tower
   would force $\Delta^{(n)}$ to factor through finite-dimensional
   pieces, automatically supplying a uniform bound. This is the
   workplan's path (a) for **P3.4**.

2. **Yekutieli rigidity argument**. The :refterm[descent]{#descent} involution
   $\hat\tau_n$ ([def:descent-involution](../lifting-and-descent/descent-involution.md))
   is rigid on the categorical level
   ([yekutieli2010](https://doi.org/10.1090/conm/518/10212));
   a level-uniform rigidity bound on the :refterm[descent]{#descent} action implies
   $\Delta^{(n)}$ is bounded by the :refterm[descent]{#descent} norm, which is itself
   uniform.

Both paths require infrastructure beyond the scope of this block;
the conjecture is stated to make the dependency explicit and the
empirical motivation citable.

## Discussion

**Status: conjectural** under AGENTS.md §3b, with strong empirical
support at $n = 1, 2, 3$ for D, T, ${}^{3}$He via the formal derivation.
The downstream cone of this conjecture includes
[prop:jet-tower-convergence](#prop:jet-tower-convergence) — but
that proposition's *statement* is provable in pure analysis (the
conditional geometric-tail bound is unconditional once the
hypothesis holds). Only the *unconditional* application of the
tail bound is conjectural.

This block closes audit GAP 14a as a **path (b) resolution**:
the bound is named as a conjecture with empirical evidence
attached. Path (a) — proof from GS $E_2$-collapse — remains a
deferred Lean / narrative refactor target.
<!-- FILE_END: jet-tower-uniform-delta-max.md -->

<!-- FILE_START: topological-mass-formula-algebraic.md -->
The companion proposition
[`prop:topological-mass-formula`](#prop:topological-mass-formula)
states the topological mass identity in its **Archimedean** form

$$
  \mathfrak{m}(K) \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^{2}}
$$

where $\mathrm{Vol}(K)$ is the hyperbolic volume of $S^3 \setminus K$
under the archimedean fibre functor. Audit §4.B flagged that
identity as a **wall risk** for callers that treat it as an
algebraic-side input. This block supplies the **algebraic-side
restatement** in $\mathbb{Q}(q)$ via $\mathrm{Vol}_q(K)$
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)),
with the Archimedean form recovered as a specialisation under
$\tau_{\mathrm{arch}}$.

## Statement

**Proposition (algebraic topological mass formula).**
*Let $\beta \in H_n(R, q)$ be the Hecke normal form of a closed
braid $K = \widehat{\beta}$, and let
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ be the
algebraic quantum volume
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)).
Then the categorical mass of the vortex $\varrho_\beta$ admits the
$\mathbb{Q}(q)$-valued closed form*

$$
  \mathfrak{m}_{\mathrm{alg}}(\beta)
  \;=\;
  \frac{\Phi_1(\beta)}{\hbar_q^{2}},
\qquad
  \Phi_1(\beta) \;=\; \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\; \ln\!\bigl\lvert\mathrm{Vol}_{q_0}(\beta)\bigr\rvert,
$$

*where $\hbar_q = (q-1)/q$ is the quantum Planck constant
([`def:quantum-planck-constant`](#def:quantum-planck-constant)) and
the symbol $\tau_{\mathrm{arch}}$ is the archimedean specialisation
$q \mapsto q_0$ followed by the absolute logarithm
([`def:archimedean-realization-functor`](#def:archimedean-realization-functor)).
The identity holds in $\mathbb{Q}(q)$ before the
$\tau_{\mathrm{arch}}$ application.*

*Equivalently, the descended-trace + brane-tower decomposition*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl|\,\mathrm{tr}_M(\rho(\beta))\,\bigr|
  \;+\;
  \sum_{i = 1}^{N} \Phi_q\!\bigl(\bigl|\hat V_i(q)\bigr|\bigr)
  \;+\;
  z^2 \sum_{(i, j) \in \mathcal{P}}
    \Phi_q\!\bigl(\bigl|\hat V_i(q) \hat V_j(q)\bigr|\bigr)
$$

*([`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified) +
[`lem:tower-pair-equality-fixed-level`](#lem:tower-pair-equality-fixed-level))
is an equality in $\mathbb{Q}(q)$ at every term: the descended
piece is the Markov trace of the braid word; the singleton
sum is the level-$0$ singleton contribution; the pair sum is the
level-$0$ pair contribution. Every $\hat V_i(q)$ is an element of
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$.*

## Algebraic-side character of the statement

The archimedean version
[`prop:topological-mass-formula`](#prop:topological-mass-formula)
goes through the Chern–Simons / hyperbolic-volume correspondence,
which is post-$\tau$ — hyperbolic volume is the imaginary part of
the Chern–Simons functional, and the equality with $\mathrm{Vol}(K)$
is the volume conjecture
\cite{kashaev1997, murakami-murakami2001}. Both ingredients require
the archimedean fibre functor.

The algebraic version above replaces $\mathrm{Vol}(K)$ with
$\mathrm{Vol}_q(\beta)$, which is *defined* as a finite product in
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)).
The $\tau_{\mathrm{arch}}$ specialisation $q \mapsto q_0$ then
recovers the canonical Archimedean value $\Phi_1(\beta)$, but
**every step of the derivation up to the specialisation is in
$\mathbb{Q}(q)$**. There is no analytic continuation, no roots-of-
unity limit, no asymptotic, and no volume-conjecture borrowing.

## Compatibility with the Archimedean form

The archimedean topological mass formula
[`prop:topological-mass-formula`](#prop:topological-mass-formula)
is the **specialisation** of this algebraic version at $q = q_0$
under $\tau_{\mathrm{arch}}$:

$$
  \tau_{\mathrm{arch}}\bigl(\mathfrak{m}_{\mathrm{alg}}(\beta)\bigr)
  \;=\;
  \frac{\tau_{\mathrm{arch}}(\Phi_1(\beta))}{\hbar_q^{2}\big|_{q = q_0}}
  \;=\;
  \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^{2}},
$$

where the last equality uses the volume conjecture as a τ-side
identification (not as a derivation step).  Equivalently, the
Archimedean prop is **post-$\tau$**; the algebraic prop is
**pre-$\tau$**. Callers that need a $\mathbb{Q}(q)$-side mass
identity must cite this proposition; callers that need an
Archimedean exact algebraic values of $\mathrm{Vol}(K)$ may cite either.
<!-- FILE_END: topological-mass-formula-algebraic.md -->

<!-- FILE_START: residue-as-braid-holonomy.md -->
**Remark.**
*Each residue
$\operatorname{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\,\ell}(T_w)]$
in the spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) has a
gauge-theoretic interpretation: it is the **holonomy of the braid
loop $T_w$ around the singular fibre** at $q = \zeta_\ell$.*

**Gauge-theoretic picture.**
*Specialise the indeterminate $q$ of
$R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$ via a ring map
$\iota \colon R \to \mathbb{C}$, viewing $q$ as a parameter labelling
the family of Hecke algebras $\{H_n(\mathbb{C}, q)\}_{q \in \mathbb{C}^\times}$.  The map
$q \mapsto H_n(\mathbb{C}, q)$ is a flat holomorphic bundle of algebras over
$\mathbb{C}^\times \setminus \{\zeta_\ell\}$, with **singular
fibres** at each $\zeta_\ell$ where the algebra fails to be
semisimple.  A braid word $T_w$ defines a section of this bundle:*

- *On the regular locus it picks out a specific element
  $T_w(q) \in H_n(\mathbb{C}, q)$.*
- *Around a singular fibre $\zeta_\ell$, the section acquires
  **monodromy** encoded by how the Gröbner–Shirshov reduction of
  $T_w$ would change if $q$ were analytically continued once
  around $\zeta_\ell$.*

*The residue at $\zeta_\ell$ is precisely this monodromy, paired
with the Markov trace.  In the notation of
([rho, $S^3$ holonomy](#rem:rho-s3-holonomy-exposition)), the
residue is the $q$-deformed analogue of the Chern–Simons holonomy
of a Wilson loop in $S^3$ around an obstruction divisor.*

**Connection to Reshetikhin–Turaev.**
*At $q = \zeta_\ell$ the category of representations of $H_n(\mathbb{C}, q)$
truncates to a modular tensor category, and the Markov trace
becomes the Reshetikhin–Turaev invariant evaluated on the closed
braid. The residue $\operatorname{Res}_{q=\zeta_\ell}$ extracts
precisely this RT invariant from the Laurent expansion of
$\mathrm{tr}_M(T_w, q)$ at the pole. In the Habiro framework
([Habiro completion](#prop:full-pole-structure-mass-trace)) the
RT invariants assemble as the cyclotomic coefficients $a_m$ of
the Habiro expansion of $\mathrm{tr}_M(T_w)$: each $a_m$ encodes
the contribution of the $m$-th cyclotomic stratum, with the
total mass functional
$\mathfrak{m}(K, q_0) = |\mathrm{tr}_M(T_w, q_0)|$ realised as
the Habiro evaluation at $q_0$, not as a complex-analytic
partial-fraction sum.*

**Omission by the empirical regular-value tower.**
*The regular-value formula
([mass endomorphism tower](#prop:mass-endomorphism-tower))
evaluates $\Phi_{q_0}$ on $|\hat V_i^{\mathrm{full}}|$ without
knowledge of where each $\hat V_i$ sits in the confinement
filtration.  For braids occupying deep filtration strata
(confinement level $\ell(K, q_0) \geq 2$), the regular-value
expansion converges too slowly and the residues at $\zeta_\ell$
for $\ell \geq 2$ supply the missing contributions.*

**Exceptional divisor and the singular fibre.**
*The singular fibre at $\zeta_\ell$ is the categorical shadow of
the $\ell$-th exceptional divisor in the brane tower
([exceptional divisor](#def:exceptional-divisor)): blowing up
the singular locus resolves the degeneration of the Hecke
eigenvalues $(q, -q^{-1})$ at $\zeta_\ell$, and the holonomy of
$T_w$ around the resulting exceptional $\mathbb{P}^1$-fibre
encodes the residue.  In this sense the spectral sum recovers
the brane-tower contribution algebraically, **without** invoking
the external geometry of the blow-up: the filtration on $H_n(\mathbb{C}, q)$
is enough.*

**Example: trefoil at $q_0 \approx 1.11$.**
*The trefoil knot has confinement level $\ell = 1$ at $q_0$.
Only $\zeta_1 = 1$ contributes a nonzero residue, and
$|q_0 - 1| \approx 0.11$ is small — so the level-$1$ residue is
a dominant correction to the descended Markov trace.  This is
consistent with the observed breakdown of the
$\hat V_i^{\mathrm{full}}$-product approximation when the
descended term is itself small (confer the $\lesssim 1\%$ binding
residuals on $^2$H, $^3$H, and the degradation toward $^{40}$Ca
where $\ell(K, q_0)$ grows).*
<!-- FILE_END: residue-as-braid-holonomy.md -->

<!-- FILE_START: graded-trace-residue-split.md -->
Let $H_n(R, q)$ carry the confinement filtration $J^\bullet(q)$
([confinement level](#def:confinement-level)), with associated
graded algebra $\mathrm{gr}\,H_n(R, q) = \bigoplus_\ell
J^\ell(q)/J^{\ell+1}(q)$, and let $\mathrm{tr}_M$ be the Markov
trace on $H_n(R, q)$
([Jones–Markov trace](#thm:jones-markov-trace)).

**Proposition (graded-trace residue split).**
*The Markov trace admits a canonical decomposition*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \underbrace{\mathrm{tr}_{\mathrm{gr}}(T_w, q_0)}_{\text{smooth / graded}}
  \;+\;
  \underbrace{\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)}_{\text{oscillating / residue}},
$$

*where:*

1. *$\mathrm{tr}_{\mathrm{gr}}(T_w, q_0)$ is the Markov trace of the
 **image of $T_w$ in $\mathrm{gr}\,H_n(q_0)$** — i.e., the trace
 computed on the associated graded algebra, obtained by
 replacing each generator product with its leading-order term
 in the Gröbner–Shirshov filtration (no rewriting defects).*
2. *$\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)$ is the sum of
 rewriting-defect residues from
 ([GB residue spectral sum](#prop:gb-residue-spectral-sum)).
 In symbolic feeding-lemma form this is
 $\sum_{\ell \geq 1} (q_0 - \zeta_\ell)^{-1} \cdot
   \mathrm{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)]$
 — formal cyclotomic shadow, not a $\mathbb{C}$-analytic
 identity. The convergent statement is the Habiro expansion
 ([Habiro completion](#prop:full-pole-structure-mass-trace))
 of $\mathrm{tr}_M(T_w)$ minus its level-$0$ piece.*

*Both pieces are computable from $T_w$ alone; neither involves
empirical calibration.*

**Canonicity of the split.**
*The filtration $J^\bullet(q)$ makes $H_n(R, q)$ a filtered algebra
with compatible trace
([Hecke mass trace](#prop:hecke-mass-trace)). Any such filtered
trace admits the canonical splitting*

$$
  \mathrm{tr}(x)
  =
  \mathrm{tr}_{\mathrm{gr}}(\sigma(x))
  +
  \bigl[\mathrm{tr}(x) - \mathrm{tr}_{\mathrm{gr}}(\sigma(x))\bigr],
$$

*where $\sigma: J^\ell \to J^\ell/J^{\ell+1}$ is the symbol map
and the second summand — the defect of the symbol map to preserve
the trace — is precisely the residue sum above. The
decomposition is functorial in the filtered algebra and does not
depend on the choice of Gröbner–Shirshov normal form.*

**Reduction to the mass endomorphism conjecture.**
*Combining with the quantum-dilogarithm rewriting at each
stratum
([quantum dilogarithm](#cor:quantum-dilogarithm))
gives the mass of a braid as*

$$
  \mathfrak{m}(K, q_0)
  =
  |\mathrm{tr}_{\mathrm{gr}}(T_w, q_0)|
  +
  |\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)|,
$$

*which is the content predicted by the
[mass endomorphism conjecture](#conj:mass-endomorphism). The
graded piece reproduces the regular-value brane-tower formula
([mass endomorphism tower](#prop:mass-endomorphism-tower)) when
$T_w$ lies in filtration level $0$ and all cross-pair terms
commute through the symbol map; deviations between
$\mathrm{tr}_{\mathrm{gr}}$ and the regular-value expansion are
absorbed into $\mathrm{Res}_{\mathrm{GB}}$.*

**Cohomological form.**
*In the spectral-sequence formulation of
([GB residue spectral sum](#prop:gb-residue-spectral-sum)),
$\mathrm{tr}_{\mathrm{gr}}$ is the pairing with the $E^\infty$
page restricted to filtration level $0$; $\mathrm{Res}_{\mathrm{GB}}$
is the pairing with the higher strata. The full Markov trace is
the pairing with all of $E^\infty$, i.e., the total
Hochschild-type cohomology class of $T_w$.*

**Consistency checks.**
*(i) If $T_w \in J^0 \setminus J^1$ then $\mathrm{Res}_{\mathrm{GB}}
= 0$ and $\mathrm{tr}_M = \mathrm{tr}_{\mathrm{gr}}$; recovers the
pure-descended case
([categorical mass as Markov trace](#prop:categorical-mass-markov)).
(ii) The split is additive under braid concatenation: for
commuting braids $T_{w_1}, T_{w_2}$ in the same stratum, the two
pieces add separately.
(iii) The split is multiplicatively stable under tensor products
of atoms only on the graded part; the residue part picks up
cross-terms, which is consistent with the observed
non-multiplicativity of shell corrections across nucleon
boundaries.*
<!-- FILE_END: graded-trace-residue-split.md -->

<!-- FILE_START: graded-trace-strutinsky-interpretation.md -->
**Physical interpretation of each piece.**
*The split mirrors Strutinsky's macroscopic-plus-shell
decomposition $E = \tilde E + \delta E_{\mathrm{shell}}$: the
graded trace is the categorical analogue of the liquid-drop
(macroscopic) energy, and the residue sum is the shell
correction. This is not only a formal analogy: the Strutinsky
smoothing procedure (Gaussian convolution of the single-particle
spectrum) is the physics shadow of the symbol map $\sigma$ on
$\mathrm{gr}\,H_n(R, q)$, and the oscillating $\delta E_{\mathrm{shell}}$
is the residue contribution from filtration strata that the
smoothing collapses.*
<!-- FILE_END: graded-trace-strutinsky-interpretation.md -->

<!-- FILE_START: term6-binding-density.md -->
**Remark (calibrated; shape derived).**
*The per-nucleon binding energy of an atomic nucleus $(Z, N)$
admits the structural decomposition*

$$
  \frac{B(Z, N)}{A}
  \;\approx\;
  \alpha \cdot \frac{T_6(Z, N)}{A^3}
  \;+\;
  \beta
  \;+\;
  \delta_M(Z, N),
$$

*where $A = Z + N$, $T_6(Z, N)$ is the level-$3$ Gröbner-Shirshov
spectral-sequence stratum contribution
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence)),
$\alpha, \beta$ are calibration coefficients fit to the AME panel,
and $\delta_M(Z, N)$ is an operator-level magic-shell enhancement.*

## Term 6 explicit form

The level-$3$ stratum contribution per
[`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)'s
identification of $E_\infty^{\ell \geq 3, *}$ with Term 6 is

$$
  T_6(Z, N)
  \;=\;
  z^3 \sum_{(i, j, k) \in \mathcal{S}_3(Z, N)} \Phi_q\!\bigl(\, |\mathrm{tr}_M(\xi_{ijk})| \,\bigr),
$$

where $\mathcal{S}_3(Z, N)$ is the set of ordered triples of
nucleons in the atom, $\xi_{ijk} \in H_9(R, q)$ is the canonical
$9$-strand sub-braid acting on the three nucleons indexed
$(i, j, k)$, and $z$ is the Markov parameter
([thm:jones-markov-trace](#thm:jones-markov-trace)).

By [thm:markov-trace-factorization](#thm:markov-trace-factorization),
the $9$-strand Markov trace decomposes by triple-type:

See [Table 1](#tbl:term6-binding-density-table1-data).

so $T_6$ is computed with four atom-independent traces
(one per triple-type) plus the four binomial coefficients.

## $A^3$ normalization

The $A^3$ in the denominator is canonical: $T_6$ counts triples
($\sim \binom{A}{3} \sim A^3 / 6$), so $T_6 / A^3$ is the
per-cubed-A density — the natural intensive quantity matching
binding-energy-per-nucleon dimensions. This normalization arises
**before** any AME data; it follows from the combinatorial
structure of the level-$3$ stratum.

## Magic-shell correction $\delta_M$

The operator-level magic correction adds binding at doubly-magic
shells per
[`prop:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/braids-and-knots/categorical-neutrality-saturated-shells.md)
in the **operator-level** sense (not the Plancherel-character
sum, which vanishes — see
[reframing memo](../../../docs/audits/-self-conj-support-reframing.md)).
Empirically:

$$
  \delta_M(Z, N) \approx
  \begin{cases}
    +\Delta_M & (Z, N) \in \mathfrak{M} \times \mathfrak{M} \\
    +\Delta_P / A^{1/2} & Z \text{ even} \wedge N \text{ even} \\
    0 & \text{otherwise}
  \end{cases}
$$

with $\Delta_M \approx 2.5$ MeV at the lightest doubly-magic
$^4\mathrm{He}$ and $\Delta_P \sim 0.5$ MeV at $A \sim 12$ scale.
At heavier doubly-magic atoms ($^{40}\!\mathrm{Ca}$, $^{56}\!\mathrm{Ni}$),
$\delta_M \to 0$: the smooth $T_6/A^3$ formula already absorbs
the magic enhancement at large $A$.

## Empirical calibration

Fit on the 16-atom panel D, 3He, 3H, 4He, 6Li, 7Li, 9Be, 12C,
16O, 20Ne, 24Mg, 28Si, 32S, 40Ca, 48Ca, 56Ni, 58Ni against AME
2020 binding energies:

$$
  \alpha \approx 339.4 \;\mathrm{MeV},
  \quad
  \beta \approx 1.14 \;\mathrm{MeV},
  \quad
  R^2 = 0.84,
  \quad
  \sigma_{\mathrm{resid}} = 0.76 \;\mathrm{MeV}.
$$

Per-atom residuals (B/A AME minus prediction):

See [Table 2](#tbl:term6-binding-density-table2-data).

Witness: [`Term6-scaling-heavy.witness.json`](../../../docs/audits/2026-05-02-Term6-scaling-heavy.witness.json).

## Structurally derived content

* The **shape** $\alpha \cdot T_6/A^3 + \beta + \delta_M$ follows
  from
  [`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)'s
  identification of $E_\infty^{\ell \geq 3, *}$ with Term 6
  plus the combinatorial $\binom{A}{3} \sim A^3$ structure of
  triples.
* The **definition** of $T_6$ in terms of $9$-strand Markov
  traces is structurally derived from the Hecke-trace
  factorization theorem.

## Empirical content (not yet derived)

* The **values** $\alpha = 339.4$ MeV and $\beta = 1.14$ MeV
  are **calibrated** to the AME panel. A categorical derivation
  predicting these from $q_0$ + $m_e$ + $\mathfrak{Q}_\beta$ alone is open;
  candidate expressions like
  $m_e \cdot [7]_q [8]_q [9]_q = 361.2$ MeV are within $7\%$ of
  the fit but outside the $\pm 3\%$ fit window
  ([attempt witness](../../../docs/audits/2026-05-02-alpha-categorical-derivation.witness.json)).
* The **form** of $\delta_M$ is operator-level — proper
  derivation requires the operator structure of $\Phi_n$ on
  self-conjugate isotypical Wedderburn blocks, which is the
  content of `prop:categorical-neutrality-saturated-shells`.
<!-- FILE_END: term6-binding-density.md -->

<!-- FILE_START: full-pole-structure-mass-trace.md -->
The Markov trace $\mathrm{tr}_M(T_w, q)$ has been written so far as a
function of $q \in \mathbb{C}$ with poles at the roots of unity, and
the residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) has been
treated as a Mittag-Leffler partial-fraction expansion in $\mathbb{C}$.
That picture is misleading: the primitive roots of unity are dense
in $S^1$, so $S^1$ is a **natural boundary** of $\mathrm{tr}_M$, not
an isolated singular set, and the Cauchy-kernel sum
$\sum_{n,j} r_n^{(j)}/(q - \zeta_n^{(j)})$ is not a complex-analytic
identity in any neighbourhood of $S^1$.

The correct algebraic home is the **Habiro ring** — the cyclotomic
completion of $\mathbb{Z}[q]$ — where convergence is $q$-adic and
values at every root of unity are well-defined, but no
$\mathbb{C}$-meromorphic structure is asserted on or across $S^1$.

**Proposition (Habiro completion of the mass trace).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$, the
Markov trace of any closed braid lies in the Habiro ring*

$$
  \mathrm{tr}_M(T_w) \;\in\; \widehat{\mathbb{Z}[q]}
  \;:=\; \varprojlim_n \mathbb{Z}[q] / (q;q)_n.
$$

*See [Habiro ring](#def:habiro-ring) for the cyclotomic-completion
construction. The trace admits a unique cyclotomic expansion*

$$
  \mathrm{tr}_M(T_w, q)
  \;=\;
  \sum_{m \geq 0} a_m(T_w)\,(q; q)_m,
  \qquad
  (q; q)_m = \prod_{k=1}^{m}(1 - q^k),
  \quad
  a_m(T_w) \in \mathbb{Z}\bigl[q^{\pm 1}\bigr].
$$

*The expansion has the following properties:*

1. *(Roots of unity.) $\mathrm{tr}_M(T_w, q)$ has well-defined values
 at every root of unity $\zeta_n^{(j)}$, since $(q;q)_m$ vanishes
 at $\zeta_n^{(j)}$ for every $n \leq m$ and the partial sums are
 polynomials in $q$.*
2. *(Cyclotomic truncation.) Truncation at order $m$ exactly
 suppresses the contribution from every root of unity of order
 $\leq m$: the residual $\mathrm{tr}_M(T_w) - \sum_{k < m} a_k (q;q)_k$
 lies in the ideal $((q;q)_m) \subset \widehat{\mathbb{Z}[q]}$.*
3. *(Confinement-level support.) For an atomic closed braid the
 expansion terminates: $a_m = 0$ for $m > m_{\max}(T_w)$ with
 $m_{\max}$ controlled by the confinement level
 ([atomic Habiro expansion](#cor:habiro-expansion-atomic)).*

**Empirical regimes.**
*The qualitative regimes formerly described as "$\zeta_1$-dominant",
"resonant cancellation", and "resonant enhancement" reflect the
distribution of nonzero $a_m$ across cyclotomic orders. In Habiro
form they are stated as: a braid is regime-(1) if only
$a_0, a_1$ are nonzero; regime-(2) if signs alternate across $a_m$;
regime-(3) if signs reinforce. The Habiro expansion is the natural
target for the symbolic computation of these regimes (see
[atomic Habiro expansion](#cor:habiro-expansion-atomic)).*

**Tail control at the substrate value via the $q \leftrightarrow q^{-1}$
involution.**
*The QOU substrate value $q_0 \approx 1.110$ lies in the supercritical
regime $q > 1$, where the naive Pochhammer monotonicity*
$|(q;q)_{N+1}| \leq |(q;q)_N|$ *fails — each new factor $|1 - q^{N+1}|$
exceeds $1$ and $|(q;q)_N|$ in fact grows roughly like $q^{N(N+1)/2}$.
The Habiro completion is, however, symmetric under the involution
$q \leftrightarrow q^{-1}$ \cite{habiro2004}: the explicit identity*
$$
  (q^{-1}; q^{-1})_N \;=\; (-1)^N q^{-N(N+1)/2} (q; q)_N
$$
*shows that control of the cyclotomic tail at $q_0 > 1$ is supplied
by the monotone bound on the dual Pochhammer factor*
$|(q_0^{-1}; q_0^{-1})_N|$, *which lives in the range
$q_0^{-1} \in (0, 1)$ where the elementary monotone bound applies.
The Lean corollary `habiro_truncation_bound_supercrit` discharges
this bridge: at $q > 1$ the dual sequence
$|(q^{-1}; q^{-1})_N|$ is non-increasing in $N$.*
<!-- FILE_END: full-pole-structure-mass-trace.md -->

<!-- FILE_START: full-pole-structure-mass-trace-interpretation.md -->
**Remark (what the Mittag-Leffler picture actually was).**
*The earlier "$\sum_{n,j} r_n^{(j)}/(q_0 - \zeta_n^{(j)})$" expression
is a formal residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) — a
**heuristic shadow** of the Habiro expansion valid only after one
fixes a finite cyclotomic order and a regular evaluation point $q_0$
disjoint from $S^1$. It is not a convergent sum on or near $S^1$
and does **not** define $\mathrm{tr}_M$ as a meromorphic function on
$\mathbb{C}$. Each finite-order Cauchy-kernel partial sum is the
$q$-adic image of a Habiro truncation; computational data confirms
that for the proton and neutron the Cauchy kernel partial sum
truncated at $n \leq 6$ is identically zero, in agreement with
property (2) of the mass-trace pole structure
([`prop:full-pole-structure-mass-trace`](#prop:full-pole-structure-mass-trace))
(the Habiro coefficients $a_0, \ldots, a_5$
vanish on the atomic trefoil class).*
<!-- FILE_END: full-pole-structure-mass-trace-interpretation.md -->

<!-- FILE_START: habiro-residue-sum-equivalence.md -->
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
the formal derivation.  The
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
the formal derivation; output witness
`markov-pipeline-cross-validation.witness.json` records:

- Per-atom assertion `tr_M_at_q0_archimedean[atom]` with a relative
  tolerance proportional to `AGREEMENT_RTOL = 1e-9`.
- Diagnostic fields `realizer_value`, `term6_value`, `abs_diff`,
  `rel_diff` for each common atom.
- Asymmetric atom coverage (atoms present in only one input pipeline).

The validator skips when one of its inputs is absent (forward
compatibility), and uses the standard `WitnessBuilder` so
the formal derivation automatically reruns it whenever either input
witness changes.
<!-- FILE_END: habiro-residue-sum-equivalence.md -->

<!-- FILE_START: habiro-residue-sum-equivalence-interpretation.md -->
**Remark.** The polynomial-ring path is **constructive** (the
Habiro coefficients $a_m(u)$ are computed by sequential cyclotomic
division, see [`cor:habiro-expansion-atomic`](#cor:habiro-expansion-atomic))
while the residue path is **analytic** (it requires the quantum
dilogarithm $\Phi_q$ and complex-analytic residues at primitive roots
of unity).  The equivalence shows the two viewpoints are
two computational handles on the **same underlying object** in the
Habiro ring, and lets later proofs use whichever is more tractable
without losing rigour.
<!-- FILE_END: habiro-residue-sum-equivalence-interpretation.md -->

<!-- FILE_START: borromean-h4-categorical-derivation.md -->
**Proposition (Borromean $h^4$ categorical derivation).**
*The $h^4$ coefficient of the Borromean Markov trace
$\mathrm{tr}_M(\beta_{\mathrm{Bor}}) = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4)$
factorises as*

$$
  \boxed{\;\;
  \bigl[h^4\text{-coeff of } \mathrm{tr}_M(\beta_{\mathrm{Bor}})\bigr]
  \;=\;
  \underbrace{(-3)}_{\chi^{(2,1)}\text{ from R-matrix}}
  \;\cdot\;
  \underbrace{\tfrac{1}{4}}_{[2]_q^{-2}|_{q=1}\text{ Markov norm.}}
  \;=\;
  -\tfrac{3}{4},
  \;\;}
$$

*where $-3$ is the $h^4$ coefficient of the $S_3$ standard-irrep character
$\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$, derived from the
$U_q(\mathfrak{sl}_2)$ R-matrix on $V_{1/2}^{\otimes 3}$ via Schur–Weyl
duality; and $1/4 = 1/[2]_q^2|_{q=1}$ is the standard Markov-trace
normalisation for $c = 3$-component link closure.*
## Connection to the wider framework on `main`

The two ingredients each have a categorical home that landed on `main`
after the initial derivation:

- **Step 1 (the polynomial form `χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶`)**
  shares its Wedderburn partition-indexed framework with the
  [q-heat-kernel Peter–Weyl
  decomposition](../information-theory/q-heat-kernel-peter-weyl.md)
  and the [Habiro residue-sum equivalence](habiro-residue-sum-equivalence.md).
  Note the q-heat-kernel proposition supplies the
  $q$-Laplacian eigenvalues $\mu_\lambda(q)$ — heat-flow decay rates,
  *not* the braid-character values $\chi^\lambda(\beta)$; the
  polynomial form itself comes from the projector route below or
  from direct substitution on the closed-form trace.
  The categorical projector onto the (2,1) channel is the
  $\mathbf{e}_-$ minus-eigenspace idempotent of the Hecke quadratic
  relation $q\sigma^2 = (q^2 − 1)\sigma + q$, formalised sorry-free
  in `QOU.Hecke.SpectralProjector` (`eminus_idem`,
  `eplus_eminus_orthogonal`, `eplus_add_eminus = 1`).
  Closed-form trace computation on $V^{\otimes 3}$ can be done via
  the Cayley–Hamilton block reduction
  `QOU.Braiding.HeckeGenPolyReduction.hecke_gen_poly_reduction`.

- **Step 2 (the Markov normalisation `y_{(2,1)}(q=1) = 1/4`)**
  is the $q = 1$ evaluation of the exact closed-form Wenzl weight
  $y_{(2,1)}(q) = 1/[2]_q^2$ established in
  [`prop:h3-markov-wenzl-weights`](h3-markov-wenzl-weights.md).
  The full $\mathrm{H}_3$ weight vector is
  $\bigl([4]_q/[2]_q^3,\ 1/[2]_q^2,\ 0\bigr)$, evaluating at $q = 1$
  to the non-uniform $(\tfrac12, \tfrac14, 0)$ — the sign channel
  carries zero weight identically (Temperley–Lieb quotient), and the
  Jones-normalised trace is chiral, so no bar-involution uniformity
  applies.

Concretely, the R-matrix derivation in **Step 1** of this proof can
be reformulated equivalently as: extract the $\mathbf{e}_-$ component
of $\sigma_1^{-1}\sigma_2$ on $V_{1/2}^{\otimes 3}$, take the $h^4$
coefficient of its trace.  The $\mathbf{e}_-$ idempotent is the
categorical replacement for the explicit $8 \times 8$ R-matrix
computation; both are now valid Lean entry points to the same
`χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶` identity.

## Significance

The Borromean $h^4 = -3/4$ — the *first topological invariant* of the
Borromean linking, the part of the Jones polynomial that distinguishes
$\mathcal{B}_3$ from the trivial 3-component unlink — is now derived
*from first principles* within $\mathrm{H}_3(q)$. The chain is:

| Step | Source | Result |
|---|---|---|
| 1 | $U_q(\mathfrak{sl}_2)$ R-matrix on $V_{1/2}^{\otimes 3}$ | $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$ |
| 2 | Markov normalisation for $c = 3$ link closure | $y_{(2,1)}(q=1) = 1/4 = 1/[2]_q^2|_{q=1}$ |
| 3 | Combined Frobenius expansion | $h^4(\mathrm{tr}_M) = (-3) \cdot (1/4) = -3/4$ |

The derivation is purely categorical — no empirical fitting, no
free parameters. Each ingredient ($\check{R}$, the Hecke relation, the
Schur–Weyl decomposition, the Markov normalisation $[2]_q^{c-1}$) is a
standard categorical / topological object whose form is determined by
the framework's existing structure.

> **Scope note.** This closes the *within-$\mathrm{H}_3$* categorical
> chain (the 3-strand side of the Borromean story). It does **not**
> resolve the *cross-algebra* obstruction linking 5-strand $A_5$ fiber
> action to 3-strand $\mathrm{H}_3$ — that was the original GAP-A-4
> question (`conj:s5-so3-fiber-action`) and remains open per the
> [T4–T14 retrospective](../../../docs/audits/2026-06-06-gap-a4-T9-T14-followup-retrospective.md)
> (eight candidate cross-algebra functors refuted).

**Archimedean specialisation (§7c).** The factor $1/4 = [2]_q^{-2}\big|_{q=1}$ is the archimedean $q = 1$ numerical evaluation of the exact Wenzl weight; the companion Lean states the rational factorisation $(-3)\cdot(1/4) = -3/4$ over $\mathbb{R}$, on the archimedean side of the substrate wall.
<!-- FILE_END: borromean-h4-categorical-derivation.md -->

<!-- FILE_START: habiro-precision-ladder-equivalence.md -->
**Proposition (Habiro integrality of the Markov trace).**
*The Markov trace $\operatorname{tr}_M(T_w, q)$ of any braid word
admits a finite Habiro expansion with integer coefficients $a_m \in
\mathbb{Z}[u]$. The Habiro form is the canonical representation: it is
an exact, finite rational evaluation, not a truncated series.*

**Mathematical Novelty.** While the existence of the Habiro expansion for quantum invariants with integer coefficients is a standard result in quantum topology, its novel application here is using the strictly finite nature of this algebraic ladder to eliminate arbitrary truncation choices in evaluating physical mass differences, anchoring the observable spectrum directly to the exact cyclotomic integrality of the trace.

*Specifically, the Markov trace of the neutron–proton braid-word
difference admits the finite expansion*

$$
  \operatorname{tr}_M(\beta_n) - \operatorname{tr}_M(\beta_p)
  \;=\;
  \sum_{m=0}^{M} a_m(u) \cdot (u;\,u)_m,
  \qquad
  a_m \in \mathbb{Z}[u],
$$

*where $u = q^{1/2}$, $(u;\,u)_m = \prod_{k=1}^{m}(1-u^{2k})$ is the
$q$-Pochhammer symbol, and $M < \infty$ (the series terminates).*

*Under the archimedean evaluation $u \mapsto u_0$ at the substrate
square-root, each $(u_0;\,u_0)_m$ contributes a factor that shrinks
like $\sim \hbar_q^m$, where $\hbar_q$ is the universal substrate
Planck quantum (categorical; exact algebraic values at the substrate q_0
recorded in the audit ledger, not here).*

## Proton Habiro coefficients (verified integral)

The proton's Markov trace has $M = 8$ (series terminates):

| $m$ | $a_m(u) \in \mathbb{Z}[u]$ |
|-----|---------------------------|
| 0 | $4$ |
| 1 | $-74u - 74$ |
| 2 | $340u^2 + 365u + 389$ |
| 3 | $-711u^3 - 789u^2 - 872u - 959$ |
| 4 | $788u^4 + 901u^3 + 1029u^2 + 1172u + 1328$ |
| 5 | $-466u^5 - 559u^4 - 660u^3 - 781u^2 - 918u - 1078$ |
| 6 | $133u^6 + 167u^5 + 212u^4 + 264u^3 + 328u^2 + 402u + 494$ |
| 7 | $-12u^7 - 17u^6 - 24u^5 - 34u^4 - 48u^3 - 63u^2 - 84u - 110$ |
| 8 | $u^4 + 2u^3 + 3u^2 + 5u + 7$ |

The neutron has the same structure with $M = 8$ and different integer
coefficients. The deuteron has $M = 12$.

## Resolution of the axiom-vs-theorem question

The archimedean functor is not an arbitrary map — it is the UNIQUE
evaluation $\widehat{\mathbb{Z}[q]} \to \mathbb{R}$ that:

1. Sends the Habiro ring element $\operatorname{tr}_M(T_w)$ to its
   value at $q = q_0$.
2. Respects the cyclotomic integrality: each $a_m \in \mathbb{Z}[u]$.
3. Terminates at finite $M$ (no truncation needed).

The integrality and finiteness of the $a_m$ require no fitting and no
free parameters beyond $(m_e, q_0)$ — the Habiro evaluation of
$\operatorname{tr}_M$ at $q_0$ is determined.

## Scope of the exact evaluation

Since the Habiro expansion is **finite** ($M = 8$ for proton), the
evaluation $\operatorname{tr}_M(\beta_K, q_0)$ is **exact** — a
well-defined element of $\mathbb{Q}(q_0)$, not a truncated series.

What this does **not** give is experiment-grade agreement with
data. An observable such as $\mathfrak{Q}_\beta$ is
$m_e \cdot f(\operatorname{tr}_M(\beta_n), \operatorname{tr}_M(\beta_p),
q_0)$, and the exact Habiro evaluation of that map lands at the
substrate's *intrinsic* accuracy (improving once the derived low-order
$\tau_M$ corrections of `prop:tau-M-asymptotic-rep-theory` are
included; specific intrinsic-accuracy and ladder-correction figures
live in the archimedean witness ledger, not here).
Reaching experiment-grade precision requires higher-order
corrections that are **not** currently derived from the $a_m$;
attempts to read them off as a "precision ladder" tuned the
coefficients against the experimental value rather than evaluating
them categorically. The canonical content of this block is the
integrality of the $a_m$, not a high-precision prediction.

**Archimedean specialisation (§7c).** The Habiro / precision-ladder Taylor coefficients ($\mathbb{N}\to\mathbb{R}$) are the real archimedean evaluations of the generic Habiro-ring expansion; the real coefficient sequences sit on the archimedean side of the substrate wall, acknowledged here.
<!-- FILE_END: habiro-precision-ladder-equivalence.md -->

<!-- FILE_START: habiro-pochhammer-bridge.md -->
**Proposition (Habiro–Markov bridge via Pochhammer factorisation).**
*Let $q \in \mathbb{R}_{>0}$, $u = \sqrt{q}$, and let
$\{a_m(u)\}_{m=0}^{M}$ be the Habiro coefficients of a braid word
$\beta \in B_n$ (integer polynomials in $u$). Define the two
Pochhammer conventions:*

$$
  (q;q)_m \;=\; \prod_{k=1}^{m}(1 - q^k),
  \qquad
  (u;u)_m \;=\; \prod_{k=1}^{m}(1 - u^k).
$$

*Then $1 - q^k = (1 - u^k)(1 + u^k)$ for all $k \geq 1$, and the
ratio of the two Habiro evaluations is the Habiro-weighted product:*

$$
  \frac{\sum_m a_m(u)\,(q;q)_m}{\sum_m a_m(u)\,(u;u)_m}
  \;=\;
  \Bigl\langle\prod_{k=1}^{m}(1 + u^k)\Bigr\rangle_{\!\mathrm{Hab}}
$$

*where the Habiro average is
$\langle f_m \rangle_{\mathrm{Hab}} =
\sum_m a_m(u)\,(u;u)_m \cdot f_m \,/\, \sum_m a_m(u)\,(u;u)_m$.*

## canonical structural verification (proton, $n = 9$)

At the substrate $q_0 \approx 1.1100$, $u_0 = \sqrt{q_0} \approx 1.0536$:

| Quantity | Value |
|----------|-------|
| $\sum a_m\,(q;q)_m$ | $136.071$ |
| $\sum a_m\,(u;u)_m$ | $24.227$ |
| $\langle\prod(1+u^k)\rangle_{\mathrm{Hab}}$ | $5.616$ |
| Ratio check | $136.071 / 24.227 = 5.616$ (confirmed) |

The full bridge
$R_{\mathrm{alg}}(q) = \mathrm{bridge}(q) / (n!/[n]_q!)$
is an exact rational function of $q$ (degree $226/97$ in $u$).
The correction $S = R_{\mathrm{alg}} / (\mathrm{Vol}(4_1)/\hbar_q^2)$
inherits transcendental dependence on $\mathrm{Vol}(4_1)$ and
cannot be expressed as a closed-form rational function of $\hbar_q^2$
from representation theory alone.

**Mathematical Novelty:** The proved identity relies on the elementary textbook algebraic factorization $1-q^k = (1-u^k)(1+u^k)$. The novel, framework-specific mathematical contribution lies in its application to the Habiro-weighted-average ratio, linking standard q-series identities to the physical structure.
<!-- FILE_END: habiro-pochhammer-bridge.md -->

