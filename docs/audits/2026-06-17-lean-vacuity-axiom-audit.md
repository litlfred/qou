# Lean vacuity + provable-axiom audit

**Date:** 2026-06-17
**Branch:** `claude/sleepy-darwin-bokth1`
**Skill:** [`lean-proof-vacuity-audit`](../../.claude/skills/local/lean-proof-vacuity-audit.md)
**Scanner:** [`content/pipeline/lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
**Witness:** [`2026-06-17-lean-vacuity-axiom-audit.json`](2026-06-17-lean-vacuity-axiom-audit.json)

> **Recall-fix supersession (2026-06-18, [PR #2462](https://github.com/litlfred/qou/pull/2462)).**
> A `splitDecls` parser fix closed a body-extraction recall gap: the live
> `self-assuming-projection` count is now **201** (was 22 below), and the
> witness JSON has been refreshed to 368 total candidates. The triage in this
> doc covers the original 22; the root cause + expanded drain queue are in
> [`2026-06-18-lean-vacuity-recall-fix-and-drain-queue.md`](2026-06-18-lean-vacuity-recall-fix-and-drain-queue.md).

## Scope

Extends the `lean-proof-vacuity-audit` from an agent-only / grep-heuristic
checklist to a **runnable, repeatable scanner** over every `.lean` (library
trees + content-block siblings), and adds a **new category** requested by the
owner: an `axiom` that is a **candidate to prove**.

Categories (criterion ids — the first two mirror the skill; `proof-no-provable-axiom`
is new):

| criterion | what it flags | severity |
|---|---|---|
| `proof-no-trivial-true` | conclusion is `True` / a reflexive tautology (`x = x`) | major |
| `proof-no-self-assuming-projection` | body returns a conclusion-typed structure field verbatim (`:= d.claim`, `:= ⟨d.f1, d.f2⟩`) | critical |
| `proof-no-false-premise` | a hypothesis is impossible — vacuously true | major |
| `proof-no-decide-masking` | closed by `native_decide` (adds `Lean.ofReduceBool` to the axiom set) | critical |
| `proof-no-provable-axiom` **(new)** | an `axiom` with no `-- Ref:` / citation — should be proved or cited | major |

The scanner strips comments/docstrings before detection, and **exempts**:
- **sibling-resolution / docstub shadows** — a `: True := trivial` sibling whose
  real formalisation resolves elsewhere (the block's `lean.ref` or a docstring
  Lake-tree pointer maps to a real library decl). A `: True` stub with **no**
  resolvable real decl is a *genuine placeholder* and **is** flagged
  (`placeholder-true`).
- **field compositions that derive** (`Iff.intro`, `.trans`, `linarith`,
  `obtain …`) — not bare projections (the legit §3b-cond shape).

A `fail` is a **candidate**, not a verdict: detection is heuristic and
agent-confirmed per the skill's legit-vs-anti discriminator.

## Repository-state finding (why this audit is self-contained)

On `origin/main` (= this branch) the QA TypeScript pipeline — `qa-sweep.ts`,
`qa-criteria-registry.ts`, `qa-utils.ts`, `qa-checkers-*.ts`, and the schema
files `folio-assistant/schemas/{block-qa,lean-packages}.ts` — has been
**removed** (an in-progress migration). Only `content/pipeline/qa-agent-drain-queue.ts`
survives, and its `./qa-utils` / `./qa-criteria-registry` imports dangle. The
2323 `*.qa.json` sidecars remain as committed data, but their producing scripts
and the commit SHAs they cite are not on this line of history.

Consequently the documented `bun run content/pipeline/qa-sweep.ts … --only …`
workflow **cannot run here**. Rather than resurrect the whole removed pipeline
(which would fight the migration), this audit is delivered as a **self-contained
scanner** depending only on node builtins. The `block-qa/v1` sidecar types are
**inlined** in the scanner (the canonical schema home
`folio-assistant/schemas/block-qa.ts` is gitignored on this branch, so an import
from there would dangle on a fresh checkout). It emits the witness above and,
with `--write-sidecars`, upserts `reviewer.kind="script"` candidate entries into
the owning blocks' `.qa.json`.

## Run results (2026-06-17)

Initial scan: 197 candidates / 178 files. After resolving the 5
`proof-no-provable-axiom` (cited — see below) and applying the Gemini PR-review
fixes (multi-line `absurd` recall): **196** candidates across **181** files; **39**
exempt shadows (1755 `.lean` scanned).

| criterion | candidates |
|---|---|
| `proof-no-trivial-true` | 130 (73 `conclusion-True`, 48 `placeholder-true`, 9 `reflexive-tautology`) |
| `proof-no-self-assuming-projection` | 22 (13 field-projection, 9 tuple-projection) |
| `proof-no-false-premise` | 13 |
| `proof-no-decide-masking` (`native_decide`) | 31 |
| `proof-no-provable-axiom` | **5 → 0 (resolved this PR)** |

### `proof-no-provable-axiom` — all 5 (the actionable new category)

All in [`lean/QOU/BraidsKnots/LinearJSJVolume.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsKnots/LinearJSJVolume.lean):

- `AtomicKnot (Z N : ℕ) : Type` (l.10)
- `Vol (K : Type) : ℝ` (l.16)
- `Vol_p : ℝ`, `Vol_n : ℝ` (l.21–22)
- `JSJ_volume_additivity (Z N : ℕ) : …` (l.31)

`Vol(K)` is the hyperbolic volume in the canonical mass formula
`m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`. These uncited axioms are prime
prove-or-cite candidates — addressed in this PR.

### `proof-no-self-assuming-projection` — agent triage (all 22 adjudicated)

A sub-agent applied the legit-vs-anti discriminator per-decl (reading each
structure/class field's TYPE). Verdict: **3 VACUOUS-CIRCULAR, 14
conditional-class-degenerate, 5 LEGIT (scanner false positives)**.

| file:line | decl | verdict | recipe |
|---|---|---|---|
| `braids-and-knots/r-matrix-braiding-structure.lean:75` | `r_matrix_braiding_structure` | VACUOUS-CIRCULAR | 1 — instantiate R, prove YBE (or cite Drinfeld) |
| `braids-and-knots/r-matrix-braiding-structure.lean:90` | `braid_rep_from_R_check` | VACUOUS-CIRCULAR | 1 — derive braid reln from YBE |
| `lean/QOU/MassDerivation.lean:73` | `topological_mass_formula` | **FALSE-POSITIVE** | none — `mass_eq` is *derived* upstream (`ArchimedeanMassFormula.mass_eq_vol_div_h_q_sq` is a `theorem` from the proved decomposition); this is a terminal interface accessor |
| `fluid-dynamics/acoustic-horizon-conditions.lean:98` | `acoustic_horizon_regularity` | COND-CLASS-DEGEN | 2 — derive from inputs |
| `fluid-dynamics/discrete-vortex-spectrum.lean:91` | `discrete_vortex_spectrum` | COND-CLASS-DEGEN | 2 |
| `lean/QOU/Archimedean/AxialCoupling.lean:166` | `sym_trace_ordering_independent` | COND-CLASS-DEGEN | 2 |
| `lean/QOU/BraidKnot/LevelSufficiency.lean:104` | `LevelSufficiency` | COND-CLASS-DEGEN | 2 |
| `lean/QOU/BraidKnot/SubstrateEWHypotheses.lean:119` | `g_eq_pi_h_substrate_hypothesis` | COND-CLASS-DEGEN | **4 — owner sign-off (empirical, OPEN)** |
| `lean/QOU/BraidKnot/SubstrateEWHypotheses.lean:139` | `v_ratio_eq_log_S3_hypothesis` | COND-CLASS-DEGEN | **4 — owner sign-off (empirical, OPEN)** |
| `lean/QOU/BraidKnot/SubstrateEWHypotheses.lean:160` | `scalar_gauge_ratio_eq_six_fifths_hypothesis` | COND-CLASS-DEGEN | **4 — owner sign-off (empirical, OPEN)** |
| `lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:61` | `plancherelWeight_sum_eq_one` | COND-CLASS-DEGEN | 2 — derive Wedderburn sum |
| `lean/QOU/ParticleInteractions/atomic_lp_stability.lean:51` | `atomic_lp_stability` | COND-CLASS-DEGEN | 2 (LP dichotomy from solves) |
| `lean/QOU/ParticleInteractions/corrected_markov_trace.lean:40` | `corrected_markov_trace` | COND-CLASS-DEGEN | 2 — compute tr_M(trefoil) |
| `lean/QOU/ParticleInteractions/deuterium_derived_binding.lean:128` | `deuterium_derived_binding` | COND-CLASS-DEGEN | **4 — owner sign-off (binding-energy claim)** |
| `mass-theory/he4-channel-active-set.lean:308` | `he4_class_is_feasible_solution` | COND-CLASS-DEGEN (mild bridge) | 2 / accept |
| `mass-theory/q-beta-q-eq-one-shadow-gate.lean:79` | `qbeta_q_eq_one_shadow_anchors` | COND-CLASS-DEGEN (mild gate) | 2 / accept as named gate |
| `mass-theory/q-beta-bar-even-kernel-typeclass.lean:115` | `bar_even_kernel_implies_q_one_shadow` | COND-CLASS-DEGEN (mild lift) | 2 / accept as lifting lemma |
| `lean/QOU/Encounter/MostowRigidity.lean:153` | `mass_rigidity_of_mostow` | **LEGIT-EXISTENTIAL** | none (∃-repackaging, §7d U4) |
| `lean/QOU/Torsion/MassGap.lean:241` | `yangMillsMassGap_construction` | **LEGIT-EXISTENTIAL** | none (witness-packaging) |
| `lean/QOU/MathlibExt.lean:134` | `List.prod_eq_of_perm` | **LEGIT-COMPOSITION** | none (applies Mathlib `Perm.prod_eq`; scanner over-match on `h.field`) |
| `mass-theory/confinement-nf-partial-proof.lean:109` | `strong_duality` | **LEGIT-COMPOSITION** | none (cited external LP fact, consumed downstream) |
| `mass-theory/he4-two-row-dominance.lean:102` | `dominant_in_two_row_stratum` | **LEGIT-COMPOSITION** | none (constructor-composition of 2 sub-properties) |

### Drain assessment (Lean cache restored 2026-06-17)

With the `lake-cache/qou-v4-24-0` oleans restored (`lean`-direct verification
available; 2951 mathlib oleans), per-decl tracing shows the flagged set is **not
a set of quick recipe-1 wins** — it splits into:

- **False positives (trace upstream before "fixing"):** `topological_mass_formula`
  — `mass_eq` is a `theorem` *derived* from the proved decomposition in
  `ArchimedeanMassFormula`; the flagged decl is a terminal interface accessor, not
  a self-assuming projection. (Lesson: the discriminator must follow class/struct
  fields to their upstream definition; a field set from a *derived theorem* is
  legit.)
- **Atomic cited results encoded as conditional-class projections:** `r_matrix`
  ×2 (YBE / braid relation over an *opaque* `V3`/`comp`, no instance). YBE for
  U_q(su2) is a true cited theorem (Drinfeld 1985, Kassel Ch. VIII) but **atomic**
  — there are no sub-hypotheses to derive from, so a non-degenerate §3b-cond
  restructure means *formalizing YBE* (research-grade), and the decl is the
  block's `lean.ref` target (cannot be deleted). Honest options: formalize, or
  accept as a cited conditional restatement.
- **Atomic empirical conjectures, already honest scaffolds:** the 3
  `SubstrateEWHypotheses` (and `deuterium_derived_binding`) are **library-only
  `.lean` with no owning content block**, already documented OPEN / §3b-cond with
  no instance + `-- Ref:`. **Recipe-4 (demote block kind) is not applicable** (no
  block to demote); the only change is research-grade derivation or unilaterally
  deleting the author's scaffold theorems.
- **5 LEGIT** rows are scanner false positives (no change).

**Conclusion:** the genuine defects are research-grade formalizations or
already-honest atomic scaffolds — not sloppy circular proofs. The honest path is
to **merge the audit infrastructure (#2428) and pursue the drain as a scoped,
build-backed follow-up**, decl-by-decl, rather than rushing unverifiable rewrites
or deleting deliberate §3b-cond scaffolds. The one committed Lean change
(`LinearJSJVolume.lean` axiom citations) verified `lean`-direct **exit 0**.

Scanner recall note (**CLOSED 2026-06-18, [PR #2462](https://github.com/litlfred/qou/pull/2462)**):
the sub-agent found `knot_factor_spectral_derivation:70` (sibling of the flagged
`plancherelWeight_sum_eq_one:61`) is the same pattern but was NOT flagged. Root
cause was a `splitDecls` body-extraction bug that swept the trailing
`end <Namespace>` closer into the last decl's body, breaking the projection
regex's `\s*$` anchor for every last-decl-before-a-closer. The fix lifted recall
from **22 → 201** self-assuming candidates; see
[`2026-06-18-lean-vacuity-recall-fix-and-drain-queue.md`](2026-06-18-lean-vacuity-recall-fix-and-drain-queue.md).

## Drain plan (priority order)

1. **`proof-no-provable-axiom` (this PR).** Prove or cite the 5 `LinearJSJVolume`
   axioms.
2. **`self-assuming-projection` agent triage.** Per-decl legit-vs-anti; recipe-1
   genuine proof where vacuous; respect prior false-positive verdicts.
3. **`placeholder-true` (48).** Genuine `: True` gaps: honest fix is state the
   real proposition with `sorry` + `-- Ref:`, or **demote `theorem → conjecture`**
   — a **claim change requiring owner sign-off** (do NOT auto-commit).
4. **`native_decide` (31).** Advisory: replace with `decide` where it terminates
   to drop `Lean.ofReduceBool`; otherwise accept with a note.

Claim-changes (theorem→conjecture demotions, axiom removals that cannot be
proved) are surfaced for owner sign-off rather than auto-committed, per the
skill's recipe-4.
