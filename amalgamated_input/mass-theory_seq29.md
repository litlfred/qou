<!-- FILE_START: phi-q-markov-residue-habiro-intro.md -->
This sub-section bridges the algebraic foundations to the substrate-level Habiro evaluation. It establishes the $\hat{V}$-pair commutation trace, validates the exact pair equality at fixed jet levels, and states the uniform $\Delta_{\max}$ geometric bound.

The sequence connects the algebraic topological mass formula to the Habiro residue expansion. It interprets the residue as braid holonomy around singular fibres, explicitly splits the graded trace from the residue sum, and applies this split to the 6-term binding density. The closing blocks detail the full pole structure of the mass trace, securing the substrate-flow inputs for the binding density evaluation.
<!-- FILE_END: phi-q-markov-residue-habiro-intro.md -->

<!-- FILE_START: vhat-pair-commutation-trace.md -->
*Let $\hat V_i(q) = z(q)a_i(q) + b_i(q) \in \mathbb{Z}[q^{\pm 1/2}, z]$ be the traced volume of the $i$-th crossing of a closed braid. For any two indices $i, j$:*

$$
  \hat V_i(q) \cdot \hat V_j(q)
  \;=\;
  \hat V_j(q) \cdot \hat V_i(q)
  \qquad
  \text{in } \mathbb{Z}[q^{\pm 1/2}, z].
$$

*Equivalently:*

$$
  \mathrm{tr}_M\!\bigl(\hat V_i \hat V_j\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\hat V_j \hat V_i\bigr)
  \;=\; z^2.
$$

The pentagon identity requirement $uv = qvu$ applies strictly to non-commutative operator lifts, not to the scalar traced volumes. The traced volumes commute exactly.
<!-- FILE_END: vhat-pair-commutation-trace.md -->

<!-- FILE_START: tower-pair-equality-fixed-level.md -->
*Let $n \in \mathbb{N}$ be a brane jet level and let $\mathcal{P}_n = \{(i, j) : 0 \le i < j\}$ be the full set of unordered pair blow-up centres at level $n$. The pair contribution at level $n$ equals:*

$$
  \mathrm{pairs}_n
  \;=\;
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr).
$$

*The formula is an exact equality, not an upper bound.*

The prior upper-bound framing incorrectly assumed the pentagon inequality applied to scalar volumes. The true algebraic basis is the exact Markov-pair identity $\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$. Lifting this identity to the traced volumes preserves the strict equality at every jet level.
<!-- FILE_END: tower-pair-equality-fixed-level.md -->

<!-- FILE_START: jet-tower-uniform-delta-max.md -->
**Conjecture (uniform per-level binding bound).**
*For every confined vortex $\varrho$, there exists a finite real constant $\Delta_{\max}(\varrho) < \infty$ bounding the per-level binding contribution:*

$$
  |\Delta^{(n)}(\varrho)| \;\le\; \Delta_{\max}(\varrho)
  \qquad\text{for all } n \ge 1.
$$

The canonical formalism verifies this bound empirically at $n = 1, 2, 3$ for $^2\mathrm{H}$, $^3\mathrm{H}$, and $^3\mathrm{He}$. The observed sequence decays geometrically by exactly $\hbar_q^2$, maintaining strict uniformity.

The geometric tail bound of the mass series relies conditionally on this conjecture. Future analytical proofs must either leverage the Gröbner-Shirshov spectral sequence $E_2$-collapse or apply a Yekutieli categorical rigidity bound to the descent involution.
<!-- FILE_END: jet-tower-uniform-delta-max.md -->

<!-- FILE_START: topological-mass-formula-algebraic.md -->
*Let $\beta \in H_n(R, q)$ be the Hecke normal form of a closed braid. The categorical mass admits the closed form:*

$$
  \mathfrak{m}_{\mathrm{alg}}(\beta)
  \;=\;
  \frac{\Phi_1(\beta)}{\hbar_q^{2}},
\qquad
  \Phi_1(\beta) \;=\; \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\; \ln\!\bigl\lvert\mathrm{Vol}_{q_0}(\beta)\bigr\rvert.
$$

*The constituent operations occur strictly within $\mathbb{Q}(q)$ prior to the archimedean specialisation $\tau_{\mathrm{arch}}$.*

The algebraic quantum volume evaluates as a finite product in $\mathbb{Z}[q^{\pm 1/2}]$. The algebraic identity bypasses complex-analytic limits, asymptotic scaling, and hyperbolic volume conjectures. The archimedean topological formula emerges cleanly as the $q \mapsto q_0$ specialisation of this pre-realisation identity.
<!-- FILE_END: topological-mass-formula-algebraic.md -->

<!-- FILE_START: residue-as-braid-holonomy.md -->
**Remark.**
Each residue $\operatorname{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\,\ell}(T_w)]$ operates gauge-theoretically as the holonomy of the braid loop $T_w$ around the singular fibre at $q = \zeta_\ell$.

The complex parameter $q$ labels a flat holomorphic bundle of Hecke algebras over $\mathbb{C}^\times$. The algebra degenerates at roots of unity, creating singular fibres. The braid word defines a section that acquires monodromy when analytically continued around these fibres. The residue explicitly pairs this monodromy with the Markov trace.

At roots of unity, the Markov trace collapses to the Reshetikhin-Turaev invariant. The residues extract these invariants to populate the Habiro cyclotomic coefficients. For deep-strata braids, the regular-value tower converges too slowly; the holonomy residues supply the missing binding energy.
<!-- FILE_END: residue-as-braid-holonomy.md -->

<!-- FILE_START: graded-trace-residue-split.md -->
*The Markov trace decomposes canonically into smooth and oscillating components:*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \mathrm{tr}_{\mathrm{gr}}(T_w, q_0)
  \;+\;
  \mathrm{Res}_{\mathrm{GB}}(T_w, q_0).
$$

*The graded trace evaluates on the associated graded algebra, capturing the leading-order term. The residue sum tallies the rewriting defects from higher filtration strata via the Habiro expansion.*

The split mirrors Strutinsky's macroscopic-plus-shell decomposition. The graded trace acts as the macroscopic liquid-drop baseline. The residue sum supplies the oscillating shell corrections.
<!-- FILE_END: graded-trace-residue-split.md -->

<!-- FILE_START: graded-trace-strutinsky-interpretation.md -->
**Physical interpretation of each piece.**
The categorical split maps precisely onto the Strutinsky energy decomposition $E = \tilde E + \delta E_{\mathrm{shell}}$. The symbol map on the graded algebra implements the Strutinsky smoothing convolution. The residue sum recovers the sharp shell fluctuations that the smoothing procedure suppresses.
<!-- FILE_END: graded-trace-strutinsky-interpretation.md -->

<!-- FILE_START: term6-binding-density.md -->
**Remark.**
*The nuclear binding energy per nucleon follows the structural decomposition:*

$$
  \frac{B(Z, N)}{A}
  \;\approx\;
  \alpha \cdot \frac{T_6(Z, N)}{A^3}
  \;+\;
  \beta
  \;+\;
  \delta_M(Z, N).
$$

*Here $T_6$ evaluates the level-3 Gröbner-Shirshov spectral-sequence stratum, while $\alpha$ and $\beta$ provide AME calibration constants.*

The term $T_6$ enumerates ordered triples of nucleons, generating an intrinsic $\sim A^3$ scaling. Dividing by $A^3$ constructs the proper intensive density. The decomposition structure strictly derives from the spectral sequence and Hecke factorization, isolating the empirical inputs exclusively to the calibration scalars and operator-level magic-shell enhancements.
<!-- FILE_END: term6-binding-density.md -->

<!-- FILE_START: full-pole-structure-mass-trace.md -->
*The Markov trace of any closed braid lies natively within the Habiro cyclotomic completion:*

$$
  \mathrm{tr}_M(T_w) \;\in\; \widehat{\mathbb{Z}[q]}
  \;:=\; \varprojlim_n \mathbb{Z}[q] / (q;q)_n.
$$

*The trace expands cyclotomically as:*

$$
  \mathrm{tr}_M(T_w, q)
  \;=\;
  \sum_{m \geq 0} a_m(T_w)\,(q; q)_m.
$$

The primitive roots of unity populate $S^1$ densely, blocking any complex-analytic continuation across the boundary. The Habiro ring provides the rigorous algebraic substrate. Evaluating the trace truncates cleanly at finite cyclotomic orders, suppressing higher roots unconditionally. The expansion explicitly isolates the algebraic content from analytic convergence artifacts.
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

