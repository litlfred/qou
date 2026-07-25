# Planck-step atomicity — formalizing the deepest link of the clock-uniqueness reduction chain

**Date:** 2026-07-25 · **Bean:** qou-3v3d · **PR:** #4250 (tranche home) ·
**Tier:** formalization of an OPEN premise — scope-(a), audit-only, NO FIT,
nothing wired, no instance created.

**Lean:** [`QOU/AlgebraicSubstrate/PlanckStepAtomicity.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/PlanckStepAtomicity.lean)
— verified `lean`-direct, **exit 0, sorry-free** (olean-cache path,
`-D autoImplicit=false`; the dependency
`SubstrateClockUniqueness.olean` compiled `lean`-direct first, also exit 0).

## 1. Mission

The merged reduction chain
([`2026-07-25-substrate-clock-uniqueness-reduction.md`](2026-07-25-substrate-clock-uniqueness-reduction.md) §5)
bottoms out at a single prose-only premise:

$$
\text{conj:schwinger-measure-computational-time}
\Longleftarrow (\mathrm{REP}) + \text{determinacy}
\Longleftarrow \mathrm{SCU} + \text{representability} + \text{keystone}
\Longleftarrow \textbf{atomicity}
$$

The discharge map `unique_up_to_scale_of_atomic`
([`SubstrateClockUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean))
proves atomicity $\Rightarrow$ SCU, but atomicity itself lived only in the
prose of
[`rem:discrete-planck-step`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md).
This tranche gives it a Lean carrier.

## 2. Prose → formal extraction

The remark's atomicity claims, verbatim:

| Prose (rem:discrete-planck-step) | Formal counterpart |
|---|---|
| "This limit defines a **Planck step** — the minimal dynamical time unit of the QOU. Time is discrete at the origin." | the single generator `g` of the class field `atomic` |
| "we define one full Reeb circuit as **one unit of time**" ($t_P = 1/\hbar_q = q/(q-1)$) | `g` is one unit: every segment is `n • g` (`generates` clause) |
| "The continuous Reeb flow is merely the $\mathbb{R}$-shadow of this discrete iteration. **There is no sub-step resolution.**" | `generates` (nothing between iterates) + derived indivisibility `atomic_generator_indivisible` (`a + b = g → a = 0 ∨ b = 0` — literally "no half-step") |
| "The count of Planck steps measures dynamical distance in Reeb time." | `free` clause (distinct counts ↦ distinct segments — counting well defined, no wrap-around); with `generates` this makes `n ↦ n • g` a bijection `ℕ → M` (`stepIterate_bijective`) — the "$\mathcal{M} \cong \mathbb{N}$" reading |

Carrier question (§3a): the remark **cannot** carry the formal claim (a
remark makes no logical claims). Its backing block `def:planck-time` defines
the step *unit*, and
[`def:information-theoretic-time`](../../content/quantum-observable-universe/information-theory/information-theoretic-time.md)
defines the *counter* — neither *asserts* atomicity of the computation
monoid as a proposition. So the formal statement goes to the library tree
next to its consumer (`AlgebraicSubstrate/`, beside
`SubstrateClockUniqueness.lean`); block promotion is a recorded follow-up
(§6).

## 3. The (a)/(b) verdict: **(b) — atomicity is a PREMISE, not a theorem**

Checked honestly whether the existing corpus Lean *forces* atomicity
(option (a), which would have discharged SCU outright):

1. **`QOU.InformationTheoreticTime` declares `stepCount : ℕ`**
   ([`information-theoretic-time.lean`](../../content/quantum-observable-universe/information-theory/information-theoretic-time.lean)).
   The ℕ-indexing is a **modeling chart**: the structure *chooses* to model
   the counter as ℕ-valued; nothing in the corpus derives the ℕ-shape of
   the substrate's computation order from categorical structure. Proving
   "atomicity" from `stepCount : ℕ` would prove a fact about the chart, and
   passing it off as a fact about the substrate would launder the modeling
   choice into physics (§Axiomatization is NOT a Proof). The structure also
   contains no composition law at all — there is no monoid in that file to
   be atomic.
2. **`prop:ordering-jet-compatibility` does not force it either.** Its
   proved leg is well-foundedness of $\prec_\infty$ — and well-foundedness
   does **not** imply atomicity: $\mathbb{N} \times \mathbb{N}$ under lex
   order is well-founded yet not atomic (now Lean-proved,
   `atomicity_fails_for_two_generators`). Its extension/compatibility legs
   are themselves Lean `axiom`s.
3. **Corpus-grep:** no existing atomicity formalization anywhere in
   `content/**/lean` (only `.lake` package hits); the reduction audit §3
   already recorded the premise as OPEN with its own checklist.

**Verdict: (b).** `PlanckStepAtomicity` is a §3b-tax **primary conjecture
class** — content-bearing, parameter-quantified, **NO instance**. What
would upgrade (b) → (a): a genuine derivation of the computation order's
rank-one/ℕ-shape — e.g. from the jet tower's single level-by-level-extended
ordering once `prop:ordering-jet-compatibility`'s axiom legs are
discharged, or a Tannakian `FibreFunctorRigidity`-style reconstruction
pinning the composition monoid of the Reeb iteration. Until then, the
ℕ-indexing of `stepCount` is a chart reading *of* the conjecture, not
evidence *for* it.

## 4. Lean deliverable (verified per file)

New file
[`PlanckStepAtomicity.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/PlanckStepAtomicity.lean)
— namespace `QOU.AlgebraicSubstrate.SubstrateClock` (shares the SCU
namespace); §7c generic (`{M : Type*} [AddCommMonoid M]`,
`{K : Type*} [Field K] [CharZero K]`; no `Real.*`, no ordering; witness on
concrete `ℕ × ℕ`); imports only `QOU.AlgebraicSubstrate.SubstrateClockUniqueness`
(cone stays Mathlib-only). `scripts/check-sidecars.sh` §7c pass:
"library Lean — no ℝ, generic OK".

| Declaration | Kind | Status |
|---|---|---|
| `PlanckStepAtomicity` | **primary conjecture class (§3b-tax)** — one existential content field: a generator with `generates` + `free`; **NO instance** | **open** (honest state) |
| `atomic_generator_ne_zero` | the generator is not the empty computation | **proved** |
| `atomic_generator_indivisible` | **no half-step, derived**: `a + b = g → a = 0 ∨ b = 0` from `generates` + `free` | **proved** |
| `stepIterate_bijective` | `n ↦ n • g` bijective `ℕ → M` — the "$\cong \mathbb{N}$" content | **proved** |
| `PlanckStepAtomicity.exists_indivisible_generator` | class-level packaging: nonzero + indivisible + generating — the class encodes the full prose claim, not a weaker shadow (guards `proof-claims-unencoded`) | **proved** (conditional on the class) |
| `atomicity_fails_for_two_generators` | non-tautology witness: atomicity FALSE for `ℕ × ℕ`; also shows well-foundedness ⇏ atomicity | **proved** (unconditional) |
| `substrateClockUniqueness_of_planckStepAtomicity` | **conditional discharge**: `[PlanckStepAtomicity M] → SubstrateClockUniqueness M K`, an *instance* (§3b dependent pattern — honest because the premise class has no instance; nothing fires unconditionally) | **proved** |
| `borel_identification_core_of_atomicity` | end-to-end: atomicity + clock premises + `hrep` + keystone `hkey` ⇒ `N(m+1) = m!` | **proved** (conditional) |

Per-file `lean`-direct status (olean-cache recipe, dependency olean
compiled first, `-D autoImplicit=false`):

| File | lean-direct | sorry |
|---|---|---|
| `QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean` (unchanged; recompiled as dep) | exit 0 | 0 |
| `QOU/AlgebraicSubstrate/PlanckStepAtomicity.lean` (new) | exit 0 | 0 |

## 5. End-to-end chain status (what is now Lean-recorded)

$$
\text{conj} \Longleftarrow \underbrace{(\mathrm{REP}) + \text{determinacy}}_{\text{Attack A: moments proved; analysis open}}
\Longleftarrow \underbrace{\mathrm{SCU} + \text{hrep} + \text{keystone}}_{\text{Attack D: implication proved}}
\Longleftarrow \underbrace{\textbf{PlanckStepAtomicity}}_{\text{this tranche: Lean-carried, open}}
$$

- **Every arrow of the chain is now a sorry-free Lean implication**;
  `borel_identification_core_of_atomicity` composes the last two arrows
  into one statement whose deepest structural hypothesis is the atomicity
  class itself. The conjecture's clock-level content is Lean-recorded
  end-to-end: *atomicity ⇒ SCU ⇒ (with `hrep` + proved keystone)
  `N(m+1) = m!`*.
- **Open premises, unchanged in count but now all named in Lean:**
  1. `PlanckStepAtomicity` (this file, class, no instance) — the single
     structural root;
  2. shared-variable representability `hrep` (named hypothesis);
  3. the analytic (REP) fields `positive` / `integrable` + classical
     Carleman–Stieltjes determinacy (sibling attack, untouched).
- **Nothing was proved about the substrate itself.** The tranche relocates
  the conjecture's structural content into one named class; it does not
  shrink the physical open surface — it makes it precisely addressable.

## 6. Follow-ups (recorded; not done this tranche)

1. **Block promotion (per §3a "promote"):** the atomicity claim deserves a
   dedicated `conjecture` block (e.g. `conj:planck-step-atomicity`,
   information-theory chapter) with this Lean as sibling, `uses[]` on
   `def:information-theoretic-time` + `rem:discrete-planck-step`'s backing
   `def:planck-time`, and the remark's `uses[]` updated to reference it.
   Block surgery deferred (chapter manifest + uses[] + pipeline churn is
   out of scope for a library-Lean tranche); the remark's `.ts` carries an
   `authorNotes` cross-link (kind `note`, 2026-07-25) in the meantime.
2. **Aggregator wiring:** neither `SubstrateClockUniqueness` nor
   `PlanckStepAtomicity` is imported by `QOU/AlgebraicSubstrate.lean`;
   aggregate both once a lake-verifiable environment is available (the
   instance is conditional on an instance-free class, so typeclass-search
   pollution is nil — cf. the `MotivicSubstrateTrivial` note there).
3. **Upgrade routes to (a):** the two §3 routes — jet-tower ordering
   rank-one-ness (needs `prop:ordering-jet-compatibility`'s axiom legs) and
   the Tannakian `FibreFunctorRigidity` reconstruction (audit §6 of the
   reduction doc).
4. **Repo-wide `authors-note Lean-coverage stats` drift** flagged by
   `check-sidecars.sh` is pre-existing (fires for any file) — refresh once
   at tranche end (`bun run scripts/refresh-authors-note.ts`), not
   per-agent.

## 7. Scope discipline + render-QA

- **NO FIT; nothing wired; no instance created.** The class is open; the
  discharge is conditional; `hrep`/`hkey` stay named hypotheses
  (§Conditional-proved ≠ premise-established). No numerics, no dashboards,
  no kernel-convergence/Fréchet–Shohat files touched (parallel-agent
  scope respected).
- **Content edits:** only `discrete-planck-step.ts` (an `authorNotes`
  metadata entry — no `.md` prose touched, per §4d). Validation pipeline
  run: `bun run scripts/run-validate.ts content/quantum-observable-universe`
  → ✓ Valid (1 pre-existing unrelated warning, `prop:tm-gs-normal-form`).
- **Render-QA:** no math-bearing `.md` content block was created or
  edited. The preflight grep battery was run by hand on THIS document
  (balanced `$`/`$$`/braces; no `\operatorname`; no list-hijack lines
  inside display math; no inline align-family environments). The pipeline
  render was not run in this sandbox — stated explicitly per the render-QA
  gate: this document was **not machine-validated**.

## 8. Cross-references

- Reduction chain + discharge map: [`2026-07-25-substrate-clock-uniqueness-reduction.md`](2026-07-25-substrate-clock-uniqueness-reduction.md), [`SubstrateClockUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/SubstrateClockUniqueness.lean)
- Atomicity prose: [`discrete-planck-step.md`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md); canonical counter: [`information-theoretic-time.md`](../../content/quantum-observable-universe/information-theory/information-theoretic-time.md) (+ `.lean`)
- Computation order: [`ordering-jet-compatibility.md`](../../content/quantum-observable-universe/lifting-and-descent/ordering-jet-compatibility.md)
- Sibling attacks: [`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md); keystone: [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md)
