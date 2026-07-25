# Substrate clock uniqueness — the one-clock reduction of the Borel/proper-time identification (Attack D)

**Date:** 2026-07-25 · **Bean:** qou-0arr (Attack D) under epic qou-q04o ·
**Target:** [`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md) ·
**Tier:** **REDUCTION** — scope-(a), audit-only, NO FIT, nothing wired.
The deliverable is the precise smaller statement the conjecture reduces to,
its Lean carrier, and the discharge map — **not** a proof of the conjecture.

**Lean:** [`QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean)
— verified `lean`-direct, **exit 0, sorry-free** (olean-cache restore recipe,
`-D autoImplicit=false`).

## 1. The reduction idea

Under owner premise **P2** (proper time is computational time — recorded in
[`2026-07-25-r2core-schwinger-measure-exploration.md` §0](2026-07-25-r2core-schwinger-measure-exploration.md)),
BOTH sides of the target identification count the substrate's computation
steps: the binding sector's (q-)Borel variable (whose keystone-forced
normalizer $N(n) = (n-1)!$ is Lean-proved,
[`KeystoneBridgeC1Binding`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean))
and the loop's Schwinger proper time $s$ (whose measure shape $\varsigma\,ds/s$
is Lean-rigid,
[`SchwingerMeasureShape`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean)).
The conjecture "these are the same substrate object" therefore follows from a
smaller, more fundamental, purely structural statement:

> **The substrate has ONE clock.** Any two step-counters of the substrate's
> computation order that respect composition of computation steps differ by
> the single scale that owner premise **P1** (substrate scale-freedom)
> already quotients out.

The exploration audit already showed the intrinsic per-step **units** are
chart artifacts (every intrinsic weight pin-killed; only the tautological
$u = \ln q_0$ survives — Haar restated in the chart). This tranche's question
is about the **counters** themselves: which corpus "clock-like" gradings are
counters of the *same* substrate steps in different charts, and which are
genuinely independent gradings.

## 2. Corpus survey — the clock-like objects

| # | Counter | Corpus carrier | Same-clock chart or independent grading? | Evidence |
|---|---|---|---|---|
| 1 | **Reeb operation count $\mathcal{T} = N$** | [`def:information-theoretic-time`](../../content/quantum-observable-universe/information-theory/information-theoretic-time.md) (Lean `QOU.InformationTheoreticTime`: `stepCount : ℕ`, continuous rescale $t = \hbar_q \cdot \mathcal{T}$, monotone proved) | **(a) — the canonical clock itself.** The corpus's definitional substrate step counter; each iteration advances the braiding-induced ordering $\prec_c$ by one step | `reeb_time_monotone` (sorry-free); [`rem:discrete-planck-step`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md): "There is no sub-step resolution" — the atomicity prose |
| 2 | **Reeb circuit / Planck step $t_P = q/(q-1)$** | `rem:discrete-planck-step` ("one full Reeb circuit = one unit of time") | **(a) — same clock, linear-unit chart.** A linear time unit is invisible to the multiplicative measure: $\int_{a/T}^{b/T} dt/t = \int_a^b dt/t$ exactly (exploration B1) | exploration §2(c): "cannot carry $c$"; demoted to chart choice; the two step charts $\ln q$ vs $\hbar_q$ agree only classically (B6) |
| 3 | **q-ladder rung index $n$** ($t \in \{t_0 q_0^n\}$) | exploration §2(b) rung lattice | **(a) — same clock, log-lattice chart.** One rung spans $\ln q_0$ of log-time; every intrinsic per-rung weight is pin-killed; the unique pin-stable weight is the rung's own e-fold width — Haar restated | exploration B4 (exact rung measure $\ln q$; all four intrinsic units killed; the pair ratio $\tfrac12$ scale-free) |
| 4 | **Markov-tower / jet level $n$** (the binding step counter) | [`KeystoneBridgeC1Binding`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean); jet tower $A_n$ of [`prop:ordering-jet-compatibility`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.md) | **(a) — same clock, Borel-dual chart** (conjecturally). The *naive* "level = time" fails (exploration §2(d): object-level mismatch), but the level's forced factorial normalizer IS the proper-time moment sequence (§2(d′), exact $n = 1..6$): the level is the Borel/Laplace-conjugate chart of the same clock. This identification is the target conjecture — the reduction makes it a consequence of one-clock | `period_carrier_strip` proves $n \cdot N(n) = n!$; `moment_eq_factorial` ([`BorelProperTimeMoment`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)) proves $\int_0^\infty s^{n+1} e^{-s}\,ds/s = n!$ |
| 5 | **Loop expansion order $k$ (the $h$-grading)** | the $\alpha_{EM}$ Habiro element $[2]_q(1 - h^2\alpha)$ (#1511); $h^k$ counts loop insertions | **(a) — same clock, coarse-grained.** A loop order counts *complete loop cycles* — composite computation segments — while the Schwinger $s$ is the *intra-loop* time. A coarse-graining of the same composition order, not a second clock; its weights are exact binomials, not $\Gamma$-moments, which is exactly why the *naive* level-as-time reading fails while the Borel-dual (row 4) works | exploration §2(d) falsifier: ladder weights carry no $\Gamma(k)$ factors |
| 6 | **Surreal blow-up grading $\mathrm{ord}_\omega(\delta)$** | [`def:surreal-blowup-calculus`](../../content/quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.md), surreal-rate-calculus; the §7ab surreal-equality bookkeeping | **(b) — genuinely independent.** Grades the asymptotic *size* of remainders (infinitesimal / finite / growing $\omega$-grade), not a count of computation steps: it is not additive under composition of computation segments and not cofinal in $\prec_\infty$. Language-tier bookkeeping (per the 2026-06-08 narrowing ledger) — it does not compete for the clock | AGENTS.md §7ab: "bookkeeping, not new mathematics" |

**Survey verdict.** Rows 1–5 are all counters (or coarse-grainings /
conjugate charts) of ONE substrate step count; only row 6 is an independent
grading, and it is not a clock at all (fails additivity + cofinality). The
one-clock statement is therefore corpus-consistent: no second genuine clock
exists in the corpus to refute it.

## 3. The precise clock-uniqueness statement

**Setting (structure the corpus HAS).** The substrate's computation order is
corpus-carried: the braiding-induced admissible ordering $\prec_\infty$ on
the jet tower, well-founded and multiplication-compatible
([`prop:ordering-jet-compatibility`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.md);
Lean `QOU.Torsion`: `degLex_wellFounded` proved, extension/compatibility
axioms), with canonical counter $\mathcal{T} = N$
([`def:information-theoretic-time`](../../content/quantum-observable-universe/information-theory/information-theoretic-time.md)).
Abstract the composition of finite computation segments as an additive
monoid $(\mathcal{M}, +)$. A **substrate clock** is a map
$T \colon \mathcal{M} \to K$ ($K$ a characteristic-zero field, §7c generic)
such that:

1. **(additivity / functoriality)** $T(a + b) = T(a) + T(b)$ — the counter
   respects the categorical composition of computation steps (the
   $\tau$-functor sends composition to composition, so an observable-side
   counter is an additive character of the composition monoid);
2. **(non-degeneracy)** $T \not\equiv 0$ — the algebraic shadow of
   cofinality (archimedean-side refinements: strict
   $\prec_\infty$-monotonicity and cofinality in the well-founded
   computation order; recorded here, used nowhere in the algebra).

> **Conjecture (SCU — substrate clock uniqueness).** Any two substrate
> clocks differ by a nonzero scale: $T' = \lambda\, T$ with
> $\lambda \neq 0$. Equivalently, the $K$-space of additive characters of
> the substrate's computation monoid is **one-dimensional** — the
> computation monoid has rank one. The residual scale $\lambda$ is exactly
> the freedom P1 quotients out.

**This is not a tautology.** For a rank-two step monoid
$\mathcal{M} = \mathbb{N} \times \mathbb{N}$ the statement is FALSE (the
two coordinate counters are non-proportional clocks) — proved sorry-free
(`uniqueness_fails_for_two_generators`). SCU genuinely asserts that the
substrate's computation does not decompose into independent parallel
step-counting directions.

**What the corpus HAS vs what is OPEN:**

| Needed structure | Status |
|---|---|
| The computation order + composition (jet tower, $\prec_\infty$, well-foundedness) | HAVE — `prop:ordering-jet-compatibility` (well-foundedness Lean-proved; extension + multiplication-compatibility as Lean `axiom`s) |
| The canonical counter $\mathcal{T}$ | HAVE — `def:information-theoretic-time` (Lean structure + monotonicity) |
| The scale action + measure-shape rigidity | HAVE — `SchwingerMeasureShape.scale_invariant_density_unique` (sorry-free) |
| Clock-uniqueness on an **atomic** step monoid | HAVE (this tranche) — `unique_up_to_scale_of_atomic`, sorry-free |
| **Atomicity** of the substrate's computation monoid (every segment an iterate of the single Planck step; "no sub-step resolution") | **OPEN** — prose-only in `rem:discrete-planck-step`; never formalized. This is the single premise that discharges SCU |
| That the binding Borel counter and the loop proper-time counter are clocks **of the same monoid** (the P2 content per sector) | **OPEN** — this is what P2 asserts ontologically; SCU is stated so that this is the only bridge premise left at the clock level |

## 4. Lean deliverable (verified per file)

File: [`QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean)
— namespace `QOU.AlgebraicSubstrate.SubstrateClock`; §7c generic
(`{M : Type*} [AddCommMonoid M]`, `{K : Type*} [Field K] [CharZero K]`; no
`Real.*`, no ordering); imports Mathlib-only (factorials, `CharZero`,
`Prod`, tactics). Verified `lean`-direct against the restored olean cache:
**exit 0, zero `sorry`**.

| Declaration | Kind | Status |
|---|---|---|
| `IsClock` | def (additive + non-degenerate counter) | — |
| `map_zero_of_additive`, `map_nsmul_of_additive` | helper lemmas | **proved** |
| `SubstrateClockUniqueness` | **primary conjecture class (§3b-tax)** — one parameter-quantified field `unique_up_to_scale`; **NO instance** (creating one without proving the substrate monoid's rank-one structure would be laundering) | **open** (honest state) |
| `uniqueness_fails_for_two_generators` | non-tautology witness: the statement is FALSE for $\mathbb{N} \times \mathbb{N}$ | **proved** |
| `unique_up_to_scale_of_atomic` | **discharge map**: atomicity $\Rightarrow$ the uniqueness statement (a plain theorem, deliberately NOT an instance) | **proved** |
| `clocks_agree_up_to_scale` | conditional clock-level core: $[\mathrm{SCU}] \Rightarrow T_b = \lambda\, T_s$, $\lambda \neq 0$ | **proved** (conditional on the class) |
| `scale_and_unit_pinned_of_keystone` | keystone kills both parameters: $N(m{+}1) = \lambda^{m+1} \varsigma\, m!$ together with the proved $n \cdot N(n) = n!$ forces $\lambda = 1 \wedge \varsigma = 1$ (two moments decide: $m=0$ gives $\lambda\varsigma = 1$; $m=1$ gives $\lambda^2\varsigma = 1$) | **proved** (unconditional algebra) |
| `borel_identification_core` | the composed reduction: $[\mathrm{SCU}]$ + clock premises + shared-variable representability `hrep` + keystone `hkey` $\Rightarrow N(m{+}1) = m!$ — verbatim the `moment_eq_normalizer` field of `BorelProperTimeIdentification` at $\varsigma = 1$ | **proved** (conditional; `hkey` named per the `_of_` discipline, not imported — file cone stays Mathlib-only) |

## 5. The reduction chain (the payoff structure)

$$
\text{conj:schwinger-measure-computational-time}
\;\Longleftarrow\;
(\mathrm{REP}) + \text{classical Carleman–Stieltjes determinacy}
$$

$$
(\mathrm{REP})\text{'s arithmetic core}
\;\Longleftarrow\;
\mathrm{SCU} + \text{shared-variable representability} + \text{keystone (proved)}
$$

$$
\mathrm{SCU}
\;\Longleftarrow\;
\text{atomicity of the substrate computation monoid}
$$

- The first implication is the sibling Attack A machinery
  ([`BorelProperTimeMoment`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)):
  `kernel_moments_eq_schwinger` proved; `carleman_divergence` proves the
  determinacy theorem's hypothesis (the theorem itself classical,
  unformalized).
- The second is this tranche's `borel_identification_core`: given one-clock,
  the two sectors' variables agree up to a scale $\lambda$, and the
  Lean-proved keystone identity kills $\lambda$ AND the unit $\varsigma$
  simultaneously — a strictly sharper conclusion than the sibling's
  unit-only forcing (the scale mismatch between the charts is ALSO excluded).
- The third is `unique_up_to_scale_of_atomic`: pure monoid theory, no
  analysis. The conjecture's hard structural content is thereby relocated
  into a statement about the substrate's computation order alone —
  attackable with category/monoid tools, independent of ζ-regularization,
  heat kernels, or resummation.

**What the reduction does NOT capture (honest residual).** The analytic
fields of $(\mathrm{REP})$ — `positive` and `integrable` of
`BindingKernelSchwingerRepresentation` — are untouched by any clock-level
argument: that the binding resummation weight is a genuine positive
integrable kernel is an independent analytic premise. Likewise the
`hrep` hypothesis of `borel_identification_core` (the normalizer is the
loop-moment sequence read scale-covariantly in the binding chart) is the
arithmetic face of representability, stated as an explicit named
hypothesis — not smuggled. The full closure needs: atomicity (SCU) +
kernel representability + classical determinacy.

## 6. Discharge map — what bears on SCU

| Corpus result | Bearing |
|---|---|
| `rem:discrete-planck-step` — "no sub-step resolution"; one Reeb circuit = one time unit | The atomicity premise in prose. **Formalizing this block's atomicity claim** (the substrate step monoid is generated by the single Planck step) **discharges SCU outright** via `unique_up_to_scale_of_atomic`. This is the recommended next formalize-first step |
| `prop:ordering-jet-compatibility` — well-founded $\prec_\infty$, one ordering extended through the whole tower | Structural support: the tower carries ONE ordering propagated level-by-level (not a family of independent orderings) — the order-theoretic face of rank-one-ness. Well-foundedness Lean-proved; extension/compatibility currently Lean `axiom`s |
| `def:information-theoretic-time` — $\mathcal{T} = N$, monotone (proved) | The canonical clock; SCU says every other counter is $\lambda \mathcal{T}$ |
| `FibreFunctorRigidity` ([`QGeometricLanglands.lean`](../../content/quantum-observable-universe/lean/QOU/QGeometricLanglands.lean)) — a q-local system is determined by substrate + holonomy residues; eigenvalue determination "by the fibre functor $\tau$ via Tannaka–Krein" | The nearest existing $\tau$-functor uniqueness/rigidity result. Itself a conditional class (axiomatized, no instance) — so it *parallels* SCU's epistemic shape rather than proving it; a Tannakian reconstruction argument, if ever discharged, would supply exactly the "counters functorial under $\tau$ are determined by their substrate data" mechanism |
| `FaddeevUniquenessCapstone` (QBeta cluster) | Precedent for the *style* of discharge (uniqueness from bar-symmetry + boundedness + localization), analytic side; no direct clock content |
| `scale_invariant_density_unique` (`SchwingerMeasureShape`) | The archimedean shadow of SCU's quotient: once the clock is unique up to scale, the only scale-invariant measure on its half-line is $\varsigma\, ds/s$ — shape already proved rigid |
| Exploration B1/B4/B6 kills | Consistency: every candidate *rival* per-step unit is a chart artifact; no surviving candidate constitutes a second clock |

## 7. Honest gap list

1. **SCU is open.** No instance exists; the class is a genuine restriction
   (false for rank two, proved). Nothing here proves the conjecture or SCU.
2. **Atomicity is prose-only.** `rem:discrete-planck-step`'s "no sub-step
   resolution" has no Lean carrier; until it does, the discharge map's
   final arrow is unformalized.
3. **The clock premises for the two sectors are P2-ontological.** That the
   binding Borel counter and the loop proper-time counter are additive
   counters *of the same monoid* is exactly what P2 asserts; SCU cleanly
   isolates it but does not remove it.
4. **The analytic residue stands.** `positive` / `integrable` of the (REP)
   class and the classical Carleman–Stieltjes determinacy theorem remain
   open/unformalized, exactly as in the sibling attack.
5. **Order-theoretic clauses not formalized.** The generic class carries
   additivity + non-degeneracy only; monotonicity/cofinality w.r.t.
   $\prec_\infty$ are stated here (§3) but not Lean-carried (they would
   need the wall-side ordered structure; nothing downstream uses them yet).
6. **`prop:ordering-jet-compatibility`'s extension/compatibility legs are
   Lean `axiom`s** — the computation-order structure SCU quantifies over is
   itself only partially proved.

## 8. Scope discipline + render-QA

- **NO FIT; audit-only.** No numerics run; every Lean statement is exact
  algebra; no data read; nothing wired; no dashboard touched; the target
  conjecture block **not edited** (parallel-authored this tranche — the
  suggested follow-up below is recorded here instead).
- **Scope-(a) throughout.** The non-tautology witness refutes only the
  stated uniqueness property for $\mathbb{N} \times \mathbb{N}$; the
  exploration's KILLED rows are cited with their original scope.
- **Anti-laundering.** The primary class has no instance; the discharge is
  a plain theorem, not an instance; `hkey`/`hrep` are named hypotheses; the
  conditional theorems prove implications, never premises
  (§Conditional-proved ≠ premise-established).
- **Render-QA:** the preflight grep battery was run by hand on this
  document (balanced `$`/`$$`/braces; no `\operatorname`; no
  markdown-list-hijack lines inside display math; no inline align-family
  environments). The pipeline render was not run in this sandbox — stated
  explicitly per the render-QA gate: this change was **not
  machine-validated**.

## 9. Suggested follow-ups (recorded here; conjecture block NOT edited)

1. **Formalize atomicity** of the Planck step (`rem:discrete-planck-step`):
   a content-bearing class or theorem stating the substrate computation
   monoid is generated by one atomic step; on discharge, instantiate SCU
   through `unique_up_to_scale_of_atomic`.
2. **Conjecture-block cross-link** (for the block's owner, follow-up
   branch): note in `conj:schwinger-measure-computational-time` that the
   identification's clock-level core is now a CONSEQUENCE of
   `SubstrateClockUniqueness` (+ representability + the proved keystone),
   with the reduction chain of §5.
3. **Tannakian route on SCU:** attempt the `FibreFunctorRigidity`-style
   argument — counters functorial under $\tau$ determined by substrate
   data — as an alternative (non-atomicity) discharge of SCU.

## 10. Cross-references

- Exploration (P1/P2, candidate table, §5 lead): [`2026-07-25-r2core-schwinger-measure-exploration.md`](2026-07-25-r2core-schwinger-measure-exploration.md)
- Sibling Attacks A+E (moment core, Carleman, bar falsifier): [`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md), [`BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)
- Target conjecture block + sibling Lean: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md), [`schwinger-measure-computational-time.lean`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.lean)
- Keystone normalizer (proved): [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean), [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md)
- Computation order: [`ordering-jet-compatibility.md`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.md); canonical counter: [`information-theoretic-time.md`](../../content/quantum-observable-universe/information-theory/information-theoretic-time.md); atomicity prose: [`discrete-planck-step.md`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md)
- Measure shape rigidity: [`SchwingerMeasureShape.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean)
- τ-rigidity parallel: [`QGeometricLanglands.lean`](../../content/quantum-observable-universe/lean/QOU/QGeometricLanglands.lean) (`FibreFunctorRigidity`)
