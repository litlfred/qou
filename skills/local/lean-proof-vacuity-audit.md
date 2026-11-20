---
name: lean-proof-vacuity-audit
description: >-
  Detect and fix Lean "vacuous proof" anti-patterns — declarations that
  type-check, are sorry-free and axiom-clean, and whose statement matches the
  .md, yet carry NO mathematical content (they assume what they claim, conclude
  something trivially true, or rest on a false premise). These slip past
  `proof-statement-integrity` (which only checks signature-stability + an axiom
  sweep), so detection is semantic and agent-checked. Use when auditing Lean for
  circular / vacuous / trivially-true proofs, after a batch
  proof-statement-integrity normalization (the batch "wrap the conclusion in a
  structure field and project it" fix produces these), or when a "theorem" looks
  too easy. Also covers the mirror-image defect — a cited `sorry` standing in
  front of a FALSE statement (§9) — so use it when planting or auditing a cited
  `sorry`. Emits per-block QA sidecar params under the `proof-no-*` criteria.
roles: [collaborator]
---

# lean-proof-vacuity-audit

A proof can be **sorry-free, axiom-clean, and statement-faithful** and still
prove **nothing**. `proof-statement-integrity` guards the *statement* (signature
unchanged vs prior commit, no `sorryAx`) but not the *content*. This skill
catches the family of **vacuous proofs** — proofs whose validity is purely
syntactic — and drains them to honest representations.

The canonical trigger: a batch "fix proof-statement-integrity" pass that
discharges a `sorry`/false-`axiom` by wrapping the conclusion in a `structure`
field and projecting it. That removes the `sorry` and the axiom, the statement
is unchanged, the checker goes green — but the theorem now **assumes its own
conclusion**. See the exemplar `predicted-spectra/gauge-coupling-uniqueness.lean`
(superseded with a genuine proof, PR on `claude/funny-hawking-qeyqa2`).

## The anti-pattern family

### 1. Self-assuming projection (circular) — `proof-no-self-assuming-projection`

The conclusion is carried as a `structure`/`class` field and the proof returns
that field verbatim. The other fields (the would-be hypotheses) are unused.

```lean
structure D (S) where
  hyp1 : ...                                   -- decoration, NEVER used
  exists_lambda : ∃ λ, ∀ r, phi r = λ * psi r  -- ← the CONCLUSION, as a field
theorem foo (S) (d : D S) :
    ∃ λ, ∀ r, d.phi r = λ * d.psi r := d.exists_lambda   -- ← P ⊢ P, vacuous
```

The goal is *literally the type of* `d.exists_lambda`. Equivalent shapes:
`:= ⟨d.claim_a, d.claim_b⟩` (conjunction of conclusion-fields), `:= by exact
d.claim`, `:= ctx.claim_foo`, class form `[C M] … := C.field`.

### 2. Trivial-true conclusion — `proof-no-trivial-true`

The stated goal is a tautology, so any proof is content-free.

```lean
theorem foo (heavy hypotheses) : True := trivial          -- conclusion is True
theorem bar : (0 : R) = 0 := rfl                          -- tautology
theorem baz : x = x := rfl                                 -- reflexivity dressed as a result
structure D where holds : Prop := True                     -- a "Prop" field pinned to True
```

Watch for a `holds : Prop` / `claim : Prop` field that is later **instantiated
as `True`**, or a conclusion that `simp`/`tauto`/`trivial` closes with no use of
the hypotheses.

**The `theorem`→`def` dodge (STRICT — forbidden, 2026-06-23).** Re-declaring a
vacuous `theorem X : True := trivial` as `def X : True := trivial` (or
`abbrev`/`instance`) once hid it from every detector here (they keyed on the
provable kinds). The scanner now flags a trivial-bodied `: True` `def` as
pattern **`def-disguised-true`**. Carve-outs: a shadow-stub (real decl resolves
elsewhere) or a `conjecture`-block Lean placeholder (sibling `.ts` is
`conjecture(...)`) → exempt. Per **AGENTS.md §1a**, dodging an audit this way is
a review failure; the honest dispositions are *prove it* / *state the real
proposition with `sorry` + `-- Ref:`* / *demote to `conjecture`* — never a
vacuous `def : True`.

### 3. False / unsatisfiable premise (vacuously true) — `proof-no-false-premise`

A hypothesis can never hold, so the theorem is vacuously true and asserts
nothing about the intended domain.

```lean
theorem foo (h : (0 : R) = 1) : Anything := absurd h (by norm_num)   -- premise impossible
theorem bar (h : n < 0) (hn : n : ℕ) : P n := (Nat.not_lt_zero n h).elim
```

### 4. Unused hypotheses (statement weaker than intended) — `proof-no-unused-hypotheses`

*All* declared hypotheses are unused. Sometimes legitimate (uniformity across a
family), but frequently a signal that the statement was weakened until it became
trivial, or that the "hypotheses" are scaffolding for a circular field-projection.
Agent judges intent.

### 5. `decide` / `native_decide` masking — `proof-no-decide-masking`

A non-trivial statement is closed by `decide`/`native_decide`, trusting the
kernel/compiler evaluator instead of proving structure. `native_decide` adds
`Lean.ofReduceBool` to the axiom set — an integrity concern in its own right.
The runnable scanner (below) flags **only `native_decide`**; a plain `decide`
on a small decidable goal (`(-1:ℤ)^6 = 1`, `seifertGenus_T2 11 = 5`) is
idiomatic and not a defect.

### 6. Axiom that is a candidate to prove — `proof-no-provable-axiom`

An `axiom` carrying **no bibliographic `-- Ref:` justification** (and no
`[cite]` / DOI / URL in its docstring) asserts content with nothing backing
it — it should either be **proved** (converted to a `theorem`) or **cited**
(marked a genuine external input). This is the dual of `proof-no-axiom-growth`
(which guards against *adding* axioms): this guards against *leaving provable
or unjustified content as a global axiom*.

```lean
axiom my_identity (x : R) : f x = g x          -- no -- Ref:, looks provable → flag
```

Tiers (agent-confirmed):

- **provable** — Mathlib or a short argument discharges it ⇒ prove it (recipe-1).
- **legitimate-but-uncited** — a genuine external/substrate input (deep theorem,
  opaque postulated construction) ⇒ add a `-- Ref:` (recipe-3), do NOT pretend
  to prove it.
- **conditional input** — belongs as a `[Class]` hypothesis on downstream
  consumers (recipe-2 / §3b-cond) rather than a global axiom.

Do **not** flag an axiom that already carries a `-- Ref:` / citation — resting
on a cited upstream result is sound.

### 7. Import-free `Int`/`Bool` wrapper & `X - X = 0` definitional-subtraction laundering (CRITICAL — `no-import-wrapper` / `sub-zero-tautology`)

A particularly destructive anti-pattern occurs when an agent cannot resolve
`.olean` imports (or cannot prove a theorem over the actual library/Mathlib
types) and instead writes a stand-alone `.lean` file that:

1. **Drops `import` of `QOU.*` and `Mathlib.*`** so raw `lean` compiles it
   without `.lake`,
2. **Replaces mathematical objects** (categories, endomorphisms, matrices, Hecke
   algebras, connections, differential forms, trace functionals) with ad-hoc
   `Int`, `Nat`, or `Bool` record structures (`structure FooDatum where trA : Int ...`),
3. **Defines a local arithmetic combination** `def total (d : FooDatum) : Int := d.a + d.b`
   and states a "theorem" that merely subtracts the definition's body from
   itself:
   ```lean
   theorem total_expansion (d : FooDatum) :
       total d - (d.a + d.b) = 0 := by
     dsimp [total]; omega
   ```
   or checks a boolean record flag (`s.isValid = true := rfl`).

This is **fake Lean**: it is `X - X = 0` wrapped in borrowed mathematical names.
Both `scripts/lean-borrowed-name-audit.py` (`no-import-wrapper`) and
`scripts/lean-definition-collapsed-audit.py` (`sub-zero-tautology`) flag this
shape as **CRITICAL**.

**Mandatory rule — fail honestly and document for handoff:**
- **Never** write an `Int`/`Bool` proxy structure for a mathematical object that
  exists in `QOU` or `Mathlib`.
- **Never** strip `import` lines to bypass a missing `.olean` cache; run
  `scripts/lean-cache-restore.sh` and `scripts/lean-verify.sh <file.lean>`.
- **If a proof over the real types fails or is blocked, it is 100% OK for the
  process step to fail / remain `open` or `blocked`.** Keep the genuine theorem
  statement over the real imported types (`QOU.*`, `Mathlib.*`), leave an
  annotated `sorry` (`-- Ref:`) at the stuck sub-goal, and write a structured
  **blocker & handoff note** on the bean (exact file/declaration, remaining
  `lean_goal` state, lemmas proved so far, tactics/approaches tried and why they
  failed, and what specific lemma or bridge is needed next) so another agent or
  human can pick up where you left off.

## Why `proof-statement-integrity` misses all of these

Per the QA registry, `proof-statement-integrity` is `automated: false`
(agent-checked) and verifies exactly two things: (i) the provable-kind signature
is **unchanged** vs the prior commit (or an author-approved restatement appears
in the same `.md` + `.ts` diff); (ii) `lean_verify` shows no `sorryAx` /
unexpected axioms. A self-assuming projection satisfies **both** — the signature
is the intended one, and there is no `sorry`/axiom. Vacuity is a *semantic*
property of the proof term, invisible to a signature-diff + axiom sweep. Hence a
separate, agent-checked criterion family.

## Legit vs. anti — the discriminators

Do **not** flag these legitimate patterns:

- **§3b-cond conditional-class** where the proof **composes** multiple class
  fields or **applies lemmas** to *derive* the conclusion — `Iff.intro h.fwd
  h.bwd`, `h.step1.trans h.step2`, `by rw [h.a]; exact h.b`, `by linarith
  [h.x, h.y]`. The class fields encode *hypotheses*; the theorem *derives*. This
  is exactly AGENTS.md §3b-cond item 5's required shape. Verified exemplar:
  `QOU/FluidDynamics/q_bkm_criterion.lean`.
- **Honest named axiom with `-- Ref:`** for a genuine external input (e.g.
  `em_spectral_completeness_axiom`, Jones 1987), where downstream theorems
  **`obtain`/consume** it rather than re-assuming the conclusion. Resting on a
  cited upstream axiom is sound; smuggling the conclusion into a local field is
  not.
- **A field that is a genuine hypothesis** the theorem then *uses*.
- **Unused hypothesis kept for family uniformity** (the agent should confirm the
  statement is non-trivial despite the unused binder).

The single discriminator for #1: does the proof **return a conclusion-typed
field verbatim** (anti) or **derive the conclusion from hypothesis-typed fields**
(legit)? `obtain ⟨…⟩ := upstream; <derivation>` is legit; `:= d.<conclusion>` is
not.

## Sibling-resolution stubs — delete shadows, flag placeholders (do NOT bless)

A **sibling-resolution stub** is a content-block `.lean` sibling whose body is
`theorem foo : True := trivial` with a docstring `**Sibling-resolution stub** …`.
The criterion evaluates the decl the block's `lean.ref` **resolves to**
(`export-json.ts`: sibling **first**, then `<lakeRoot>/<Decl/Path>.lean`), so a
trivial sibling *shadows* the real library decl. Handle each by class — never
silently bless a bare `: True`:

- **Shadow** — the ref's decl-path resolves to a real library decl. The stub is
  pure shadowing: **delete it** (the block then resolves to the real proof). Do
  NOT exempt. See the **no-shadowing-stubs** directive in AGENTS.md §0a.
- **Genuine placeholder** — no library formalisation exists. The block is an
  *unformalised* proposition asserting `: True` — **flag it** (honest fix: state
  the real proposition with `sorry` + `-- Ref:`, or demote to `conjecture`).
- **`definition`** blocks require a sibling — it must carry the **real**
  formalisation, never `: True`.

Detect a stub by: docstring `Sibling-resolution stub`, OR body `: True := by
trivial` / `:= trivial`. A stub *corrupted* into a `: True ∧ True := ⟨d.f1,…⟩`
projection (batch `e138518a`) is the self-assuming-projection anti-pattern —
restore the honest stub, then apply the shadow/placeholder rule above.

> **Manifest (2026-06-14).** 219 stubs → 147 shadow (delete), 25 mismatch (align
> ref), 19 genuine placeholder (flag), 3 definition, 25 no-ref. See
> `docs/audits/2026-06-14-lean-vacuous-proof-audit.md`.

## Fix recipe (priority order)

When a vacuous proof is confirmed, make it **honest** — do not hand-wave a fake
proof:

1. **Genuine proof (best).** Restructure so the carrier's fields are genuine
   *hypotheses* (or come from a cited upstream result via `obtain`), and the
   theorem **derives** the conclusion. Exemplar: `gauge-coupling-uniqueness.lean`
   now `obtain`s the `e₊+e₋=1`, `e₊·e₋=0` decomposition from
   `em_spectral_completeness`, *derives* idempotency, and proves uniqueness with
   witness `λ = c·u⁻¹` — the import is load-bearing.
2. **§3b-cond conditional-class.** If the result depends on a genuine conjecture,
   axiomatise the conjecture's **inputs** as a `class`, carry it as an explicit
   `[Instance]` hypothesis, and **derive** the conclusion (non-degenerate per
   §3b-cond item 5). Add the conditional banner to the `.md`.
3. **Honest named axiom with `-- Ref:`.** If the content is a legitimate external
   input, make it a clearly-named `axiom` with a bibliographic `-- Ref:` and have
   downstream theorems **consume** it.
4. **Demote the block kind `theorem` → `conjecture`.** If the statement is
   genuinely unproved and not yet a rigorous conditional, change the `.ts` kind
   to `conjecture` (and update `.md`). This is a claim change — surface it to the
   owner before committing.

**Never** the batch anti-fix: wrapping the conclusion in a structure field and
projecting it. That converts a *visible* gap (`sorry`) into an *invisible* one.

## Detection heuristic (candidate grep → agent confirmation)

0. **Runnable scanner (preferred).** `bun run
   folio/pipeline/lean-vacuity-axiom-audit.ts` walks every `.lean` (library
   trees + content-block siblings), strips comments/docstrings, and emits a
   witness JSON (`docs/audits/<date>-lean-vacuity-axiom-audit.json`) keyed by
   path, with one entry per category (#1–#6 above). It exempts sibling-stub
   *shadows* (real formalisation resolvable via `lean.ref` / docstring) and
   field *compositions* that derive. `--write-sidecars` upserts
   `reviewer.kind="script"` candidate entries on the owning blocks' `.qa.json`.
   This replaces the manual grep below in environments where the migrated
   `qa-sweep.ts` / `qa-criteria-registry.ts` are unavailable.

1. **Cheap candidate filter** (regex):
   - proof body `:=\s*\w+\.\w+\s*$`, `:=\s*⟨[^⟩]*\.\w+[^⟩]*⟩`, `:= by\s+exact\s+\w+\.\w+`, `:= ctx\.`, `:= d\.`, `:= h\.`
   - conclusion `: True`, `: .* = .*` where both sides identical, `holds : Prop`
   - `decide`, `native_decide`
   - structures whose field names are `claim_*`, `exists_*`, `*_holds`, `result`, `property`, `spec`, `main`
2. **Agent confirmation** (this skill / `lean-proof-review`): open the file, read
   the carrier's definition, check whether the projected field's type unifies
   with the goal (up to bound variables), and whether sibling fields are used.
   Apply the legit-vs-anti discriminator above. Record verdict + evidence.

### 7. `: True` carrier field — `proof-claims-unencoded` / pattern `true-class-field`

A `class`/`structure` field typed literally `: True` (or `True ∧ … ∧ True`, or a
`Prop := True` default) carries **zero** content — every instance satisfies it,
so a downstream consumer that takes the field as a hypothesis assumes nothing.
This is the *field-level* analogue of a `: True` conclusion, and it is the gap
that the empty-prop-carrier (zero-field) and claims-unencoded (≥2 enumerated
bullets) detectors both structurally miss: a **single** `: True` field on an
otherwise-populated carrier. Exemplar: `mass-theory/confinement-categorical.lean`
`hh_vanish : True`; worst case: a `Conjectures/*` carrier with `holds : True` that
a trivial `instance … := ⟨⟩` then "closes" (fabricating a content-free instance of
an open conjecture — the §3b-tax violation). **Honest fix:** encode the real
property as the field type, or — for genuinely-open infrastructure Mathlib lacks
— annotate the field `opaque marker` / `@marker` (then it is **exempt-but-tracked**,
consistent with the empty-carrier opt-out), never leave a bare un-annotated `: True`.

> **Escalation signal on trivial-true (2026-06-28).** A `placeholder-true` /
> `def-disguised-true` whose docstring carries theorem-assertion language
> (`**Theorem**` / `**Lemma**` / `**Proposition**`) and is **not** a conjecture
> carrier is annotated *"docstring asserts a provable claim while the Lean
> concludes `True`"* — the `q_gl_obstruction_calc` failure mode (a real claim
> hidden behind a tautology), distinct from an honest open conjecture. This is
> the heuristic that the 2026-06-26 triage missed on `q_gl_obstruction_calc`,
> `confinement-categorical`, the fluid-dynamics conditionals, and others.

### 8. Docstring claims a `sorry` the body does not have — `proof-docstring-sorry-mismatch`

The prose says *"the body is therefore `sorry`"* / *"discharged by `sorry`"* /
*"stated with `sorry` + citation"*, and the body contains **no `sorry`**.

**Why this is a separate criterion and not a case of #1.** `detectSelfAssuming`
gates on the projected **field name** (`CONCLUSION_FIELD`: `claim_`, `_holds`,
`_eq`, …). A class field named outside that convention is invisible to it no
matter how plainly it posits the conclusion. Two live cases found by hand on
2026-08-08 were missed for exactly that reason, and both happened to be named
`*_ident`:

| declaration | body | why #1 missed it |
|---|---|---|
| `confinement_categorical` | `exact ctx.confinement_ident` | `confinement_ident` ∉ `CONCLUSION_FIELD` |
| `nucleon_ordering_factorization` | `exact ctx.factorization_ident` | `factorization_ident` ∉ `CONCLUSION_FIELD` |

This detector reads **only** the doc block and the body, so no naming choice can
dodge it. It is also the cheapest possible signal: an author who writes "the body
is therefore `sorry`" and then discharges by projection has left the
contradiction in plain text.

**Why `critical`.** The docstring is not merely stale, it is load-bearing
misinformation *in two directions at once*: an audit reading the prose records an
honest queued gap, an audit reading `#print axioms` records a proof. Both are
wrong and they disagree, so neither review path catches it unaided.

**First corpus run (2026-08-08): 13 candidates.** Three were spot-checked and
**all three were true positives** — including two whose docstrings assert the
precise opposite of their code:

- `volume_perturbation` — *"Stated with `sorry` … **no conclusion field on the
  class hands this back**"*, above `exact ctx.volume_perturbation_claim`, where
  the class field is even commented `(conclusion)`.
- `shell_filling_rule` — *"the unproved ones carry honest `sorry`s in their named
  sub-theorems … **not projected conclusion fields**"*, while both named
  sub-theorems are `exact ctx.inner_shells_fill` / `exact ctx.hund_rule`, with no
  `sorry` in either.
- `kappa_vanishes_iff_chi` — *"inherits that lemma's single honest `sorry`"*, but
  `qou_obstruction_reduction.lean` contains **no `sorry` in code at all**; the
  cited `obstruction_trace_gap` is `exact ⟨ctx.kappa0_eq_chi_A,
  ctx.phi_1_image_eq_chi_A⟩`. Anything downstream calling that file's result
  "derived, never assumed" inherits an assumption instead.

**Do not soften the regex to exclude delegated sorries.** The obvious refinement
— skip when the doc attributes the `sorry` to a sub-theorem or an inherited lemma
("in their named sub-theorems", "inherits … `sorry`") — would have suppressed
**two of those three**. Delegation is exactly where the claim goes unchecked. The
detector stays high-recall and the call stays with the agent, per the ledger below.

What it does **not** fire on: historical or negated mentions (`sorry-free`,
"previously carried a `sorry`", "the `sorry` is removed", "no longer"), matched
per-sentence so one declaration's "sorry-free" does not mask another's claim in
the next paragraph.

### 9. Cited `sorry` on a FALSE statement — `proof-no-false-cited-sorry`

The mirror image of everything above. Patterns #1–#7 are proofs that prove
nothing; this is a **`sorry` in front of a proposition that is not true**. It is
strictly worse than an open gap: discharging it would discharge `False`, every
downstream consumer is unsound the moment anyone "closes" it, and the `-- Ref:`
to a real theorem makes it look audited. The citation is usually correct *about
the informal theorem* — the defect is in the formalisation's quantifier range,
where the Lean statement silently admits degenerate inputs the textbook excludes.

**How they arise.** A cited `sorry` is never elaborated against a witness, so
nothing ever forces the author to look at a small instance. Three found in one
sweep (2026-08-08), all the same shape — a hypothesis the informal theorem takes
for granted:

| declaration | admitted degenerate input | consequence |
|---|---|---|
| `QGevreyOrder.cauchyMul_order` | `b = 0` (order `0`, since `Real.log 0 = 0`) | `a ⋆ b = 0` has order `0`, but `E(s,0) = max s 0 = s` |
| `YoungTableauStandard.branching_two_one` | `λ` not containing `μ` | unguarded `fDimSkew` counts `1` where `f^{λ/μ} = 0`; fails at `k = 3` |
| `HadamardFactorization.hadamard_factorization` | `ρ < 0` (satisfiable: the constant `1`) | conclusion needs `(p : ℝ) ≤ ρ` for `p : ℕ` |

Note how ordinary each admitted input is. Two of the three are junk-value
artefacts of Mathlib totality conventions (`Real.log 0 = 0`, `Real.rpow 0 ρ = 0`)
and the third is a definition missing a side condition.

**Detection — the small-instance check.** No regex finds these; the check is
semantic and cheap:

1. Instantiate the statement at the **smallest nontrivial parameter** (`n = 0,1,2,3`;
   the empty diagram; the zero sequence; the constant function) and evaluate both
   sides by hand. Most of the work is arithmetic.
2. Ask what the **junk values** do. Every Mathlib total function has them —
   `log 0`, `0⁻¹`, `Nat` subtraction, `Nat.card` of an infinite type, `x ^ (0:ℝ)`,
   `Finset.sup'` of `∅`. If any appears in the statement, feed it deliberately.
3. Ask which hypothesis the **informal** theorem assumes without saying so —
   nonconstancy, non-cancellation, containment, nonnegativity of an order,
   nonvanishing of a leading coefficient. Then check it is in the Lean binder.
4. Read the docstring against the signature. All three above were *pre-flagged in
   prose* ("additionally needs a non-cancellation hypothesis", "positive /
   no-cancel coefficients") — the hypothesis just never reached the binder. A
   docstring that names a condition the signature does not carry is a direct hit.

**Fix recipe (in addition to the four above).**

5. **Refute, then restate.** Do not silently patch the binder.
   a. Add a machine-proved `¬ ∀ …` refutation of the over-general form, named
      `<thm>_unhypothesised_false` / `<thm>_needs_<hypothesis>`, with the witness
      spelled out in its docstring. This is the in-repo `freeProjClaim_false`
      idiom (`SnWedderburnPartitionBridge`), and it is what stops the hypothesis
      being "simplified away" by a later pass.
   b. Restate the theorem with the hypothesis the refutation forces, keeping the
      cited `sorry`.
   c. Re-run the small-instance check on the restated statement, and record the
      arithmetic in the docstring so the next reader need not redo it.
   d. If the defect is in a **definition** rather than the theorem (case #2
      above), fix the definition — weakening the theorem to dodge a broken
      definition just moves the bug.
   e. Prove whatever half is now provable. Splitting `cauchyMul_order` sent its
      entire `≤` direction sorry-free and left a strictly smaller gap; a false
      statement often has real content hiding behind it.

**Where this belongs in the workflow.** Run the small-instance check *when
planting* a cited `sorry`, not only when auditing one — minutes then, a full
audit later. Record it in the docstring: "checked at `k = 3, 4`".

## Agent-inspection ledger — making agent confirmation mandatory (2026-06-28)

The detector is **high-recall by design**; the legit-vs-genuine call requires
agent inspection (a `decide` on a true concrete fact is legit; a `: True` hiding
a real theorem is not). For **content blocks** that verdict lands on the
`<block>.qa.json` sidecar (above). But a **standalone library `.lean`**
(`content/**/lean/QOU/**/*.lean` with no `.ts`/`.md` sibling) has **no sidecar**,
so an agent verdict had nowhere durable to live — detection stayed purely
machine, and a one-off triage doc could silently mis-call a candidate "legit"
(as happened). The **review ledger** closes that gap:

```bash
# Seed/refresh: new + file-changed candidates become `needs-agent`.
bun run folio/pipeline/lean-vacuity-axiom-audit.ts folio/quantum-observable-universe \
  --review-ledger docs/audits/lean-vacuity-review-ledger.json
# Enforce: exit 1 if ANY non-exempt candidate lacks a FRESH agent verdict.
bun run folio/pipeline/lean-vacuity-axiom-audit.ts folio/quantum-observable-universe \
  --check-ledger docs/audits/lean-vacuity-review-ledger.json
```

- **Ledger** (`lean-vacuity-review/v1`, committed): keyed by
  `<relpath>::<decl>::<category>`; each entry records the agent `verdict`
  (`genuine` | `legit` | `advisory` | `needs-agent`), optional `disposition` /
  `evidence` / `reviewer`, and the **`.lean` sha at review time**.
- **Staleness = re-review.** If the `.lean` changes after a verdict, `file_sha`
  drifts and `--review-ledger` resets the entry to `needs-agent`
  (preserving `stale_prev_verdict`). A verdict only counts while it matches the
  file it was made against — the machine cannot bless a candidate, only an agent
  verdict can, and only while fresh.
- **Resolved candidates are pruned** automatically (a fixed file no longer
  flags, so its key drops out).
- **The agent workflow:** run `--review-ledger` to materialise the queue, inspect
  each `needs-agent` entry per the legit-vs-anti discriminators above, write the
  verdict (+ disposition/evidence) into the ledger, fix every `genuine` /
  `advisory` candidate, then `--check-ledger` must pass. This is the
  "agent inspection, not just machine" gate.

## QA criteria (sidecar params) — wiring

Mirrors the existing `proof-statement-integrity` model (Agent-checked,
`automated: false`). Per-block sidecar `<block>.qa.json` gains a
`criteria["proof-no-<x>"]` array of `QaCriterionEntry` with `reviewer.kind =
"agent"`.

### 10. Conjectural class carries too little — `proof-unclosable-context-sorry`

A `sorry` whose statement is **refutable over the very class it is stated on**.
Not an open gap: it can never be discharged, because discharging it would prove
something false.

The shape is a §3b-cond conjectural class whose fields the conclusion talks
about, but which the class never relates to one another:

```lean
class MassCategoricalDescentContext where
  B : ℝ            -- total binding energy
  B_desc : ℝ       -- descended component
  B_trans : ℝ      -- transient component
  …               -- no equation mentioning any of the three

theorem mass_categorical_descent [ctx : MassCategoricalDescentContext] :
    ctx.B = ctx.B_desc + ctx.B_trans := by
  -- Ref: [manuscript] …
  sorry
```

Pick `B := 0, B_desc := 1, B_trans := 0` and the statement is false. Machine
proof, no junk values and no cleverness required:

```lean
theorem mass_categorical_descent_unconstrained_false :
    ¬ ∀ ctx : MassCategoricalDescentContext, ctx.B = ctx.B_desc + ctx.B_trans := by
  intro h
  have := h { CategoricalObj := Unit, m_endo := id,
              B := 0, B_desc := 1, B_trans := 0, B_BW := 0 }
  norm_num at this
```

**How it differs from #1 and #9.** All three are "the Lean does not prove the
claim", but the classes differ in *where* the content went:

| | class carries | consequence |
|---|---|---|
| #1 self-assuming | the **conclusion**, as a field | theorem projects it; proves nothing |
| #10 unclosable | **neither** conclusion nor relating hypotheses | nothing to derive from; `sorry` unclosable |
| #9 false cited | (no class) statement admits a degenerate input | discharging it discharges `False` |

**AGENTS.md §3b-cond item 5 already forbids this** — *"the class axiomatises
hypotheses, not the conclusion … the theorem must **derive** its conclusion
from them."* That sentence has been read as forbidding only the #1 direction
(carrying too much). These fail it the other way: carrying too little. The
rubric's own verified exemplar shows the shape that works —
`QOU/FluidDynamics/q_bkm_criterion.lean`'s `QBKMContext` carries the two
directions as **implications** (`vorticityIntegralFinite → extendsSmoothly` and
its converse) and the theorem composes them with `Iff.intro`, sorry-free.

**Detection — build an adversarial instance, do not grep.** This was tried two
ways syntactically and both failed:

- flagging junk-value smells by regex: matched doc-comment slashes, 26 of 33
  "hits", useless;
- flagging classes whose fields are all bare data: caught 1 of 11, because
  `MassCategoricalDescentContext` *does* have a hypothesis field — it just does
  not mention `B`, `B_desc` or `B_trans`.

The property that matters is *"do the class's hypotheses constrain the fields
the conclusion mentions"*, and that is not a grep. The reliable test is the
small-instance check of §9 lifted from parameters to classes: **instantiate the
class with numbers chosen to disagree** and see whether it compiles. Two
minutes per statement, and the answer is a proof either way.

**#1 and #10 are adjacent, and the naive fix for #1 produces #10.** Deleting a
conclusion-bearing field removes the self-assuming projection and leaves the
theorem with nothing to derive from — vacuous becomes unclosable. Observed
in-repo: `QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean`'s
`obstruction_trace_gap` says so in its own docstring —

> The two conjuncts were previously carried as class fields
> (`kappa0_eq_chi_A`, `phi_1_image_eq_chi_A`) and projected here, which made
> this theorem assume exactly what it claims … Fields deleted; the gap is now
> real.

The gap became real *and* impossible to close. Deleting the field is half a
repair; the other half is putting back the hypotheses the derivation needs. When
fixing a #1, check the result against #10 before calling it done.

**A class that constrains nothing refutes both a statement and its opposite.**
`bare_is_lp_unstable` (`∃ X, …`) and `dressed_is_lp_stable` (`¬ ∃ X, …`) share
`AtomicLPStabilityContext` and are both refutable — `Candidate := Empty` kills
the first, one satisfying candidate kills the second. If you find one of a
±pair, check its sibling.

**Where they concentrate.** Measured over the whole qou corpus (bean qou-o7qo):
18 context-class `sorry`s among the 822 modules that no build ever reached,
against 3 among the 870 that always compiled — six times the density. A module
that compiles gets read and its `sorry`s reported every build. Sweep
never-built modules first.

**Fix.** Add to the class the hypothesis the derivation actually needs — for
the example above, whatever relates `B` to its two components — so the theorem
composes it, per the exemplar. Restating the theorem to dodge the gap moves the
bug. Since this changes what the block claims, it is the author's call, not the
auditor's: report with the refutation attached.

**Where these hide.** All three found so far were in modules outside the
`lake build` import closure (bean qou-rc7b), so no build had ever reported
their `sorry`s, and each carried `-- Ref:` citations that made them look
audited. Expect the population to correlate with build coverage, not with
apparent maturity.

### 11. Axiom-in-class-field laundering — `proof-no-axiom-class-laundering`

A class field encodes a mathematical claim (e.g., `almost_everywhere_nontrivial`).
The theorem that extracts this field is 'sorry-free' because the sorry was pushed
into the `instance` declaration, which fills the field via a bare `axiom` or
`sorry`. The theorem appears sorry-free in audits while the claim remains
unproved.

```lean
-- The class declares the claim as a field:
class MotivicGaloisCharacter (M : Type*) where
  galois_action : M → M
  almost_everywhere_nontrivial : ∃ S, ∀ x ∉ S, galois_action x ≠ x  -- ← unproved claim

-- The instance fills it with an axiom:
axiom ae_nontrivial_placeholder : ∃ S, ∀ x ∉ S, myAction x ≠ x
instance : MotivicGaloisCharacter MyType where
  galois_action := myAction
  almost_everywhere_nontrivial := ae_nontrivial_placeholder  -- ← bare axiom

-- The downstream theorem looks sorry-free:
theorem galois_char_nontrivial [MotivicGaloisCharacter M] :
    ∃ S, ∀ x ∉ S, MotivicGaloisCharacter.galois_action x ≠ x :=
  MotivicGaloisCharacter.almost_everywhere_nontrivial  -- ← "proved" ✗
```

**Why this is WORSE than a visible `sorry`:**

- Audits that grep for `sorry`/`axiom` in theorem files miss it — the axiom
  lives in the instance file, not the theorem file
- The class instance file may not even compile (as happened with
  `qou-motivic-galois-instance.lean` which had 3 type mismatches)
- Downstream blocks cite the 'sorry-free' theorem as proved
- `#print axioms` on the theorem shows `sorryAx` or the named axiom, but
  only if someone thinks to run it — the file-level grep misses it entirely

**How it differs from #1 and #10:**

| | mechanism | why audits miss it |
|---|---|---|
| #1 self-assuming | conclusion IS a field; theorem projects it | file-local, caught by field-name grep |
| #10 unclosable | class has too few hypotheses; sorry unclosable | file-local sorry visible |
| #11 axiom-in-class | claim is a field; INSTANCE fills it with axiom/sorry | axiom is in a **different file**; theorem file is clean |

**Honest dispositions:**

1. **PROVE it** — supply a constructive witness for the class field in the
   instance
2. **SEPARATE it** — move the claim OUT of the class into a standalone
   theorem with an explicit `sorry` and `-- Ref:` citation
3. **DEMOTE it** — label the block as `conjecture(...)` in the `.ts` metadata

**Never:** pack an unproved claim as a class field and fill it with `axiom`.

**Detection.** For every `class` with a `Prop`-valued field, check that every
`instance` fills that field with a proof term, not `sorry` / `axiom` /
`by exact someAxiom`. Concretely:

1. Enumerate all `class` declarations; for each, identify fields whose type
   is `Prop` (or returns `Prop` after applying parameters).
2. For each `instance` of that class (grep `instance.*:.*ClassName`), check
   whether the corresponding field assignment is a proof term or one of:
   - a bare `axiom` name
   - `sorry`
   - `by exact <axiom_name>` where the name resolves to an `axiom`
3. If the instance is in a file that does not compile, flag unconditionally —
   a non-compiling instance filling a `Prop` field is evidence of laundering.
4. Run `#print axioms <theorem_name>` on any downstream theorem that extracts
   the field — if it shows `sorryAx` or an unjustified `axiom`, the laundering
   is confirmed.

**Motivating incident.** `MotivicGaloisCharacter.almost_everywhere_nontrivial`
was carried as a class field. The instance in `qou-motivic-galois-instance.lean`
attempted to fill it with a bare axiom but had 3 type mismatches and never
compiled. Downstream theorems extracted the field and appeared sorry-free,
passing all file-level audits. The claim was unproved.

| criterion id | status | anti-pattern |
|---|---|---|
| `proof-no-self-assuming-projection` | active | #1 circular projection |
| `proof-no-trivial-true` | active | #2 tautological conclusion |
| `proof-no-false-premise` | active | #3 vacuously true |
| `proof-no-unused-hypotheses` | active | #4 weakened statement |
| `proof-no-decide-masking` | active | #5 evaluator masking (`native_decide`) |
| `proof-no-provable-axiom` | active | #6 uncited / provable axiom |
| `proof-no-false-cited-sorry` | active | #9 cited `sorry` on a false statement |
| `proof-docstring-sorry-mismatch` | active | #8 docstring claims a `sorry` the body lacks |
| `proof-unclosable-context-sorry` | active | #10 class carries too little; `sorry` unclosable |
| `proof-no-axiom-class-laundering` | active | #11 axiom-in-class-field laundering |

**Minimal wiring (per Agent-A recon):**

1. `content/pipeline/qa-criteria-registry.ts` — add a `QaCriterionDefinition`
   to the `PROOF` array (it auto-flows into `QA_CRITERIA_REGISTRY`,
   `PROOF_WATCHER_CRITERIA`, and the `proof` watcher axis). Use:
   `domain: "proof"`, `default_severity: "critical"`, `depends_on: ["lean"]`,
   `automated: false`, `applies_to: ["theorem","lemma","proposition","corollary"]`.
2. `.claude/skills/local/proof-integration-watcher.md` — add a dispatch row per
   criterion → `lean-proof-review` (logic-validity review type).
3. No new checker file: `qa-sweep` marks `automated: false` criteria
   `needs-agent`; `proof-integration-watcher` dispatches an agent that runs this
   skill and writes the `reviewer.kind="agent"` sidecar entry.

`bun run content/pipeline/qa-sweep.ts <block-path> --only proof-no-self-assuming-projection`
marks the entry `needs-agent`; the agent then fills the verdict.

## Audit + drain workflow

1. **Audit:** grep candidates across all `.lean` (library trees + content-block
   siblings), agent-confirm, record findings in
   `docs/audits/<date>-lean-vacuous-proof-audit.md`.
2. **Classify:** assign each confirmed instance a fix from the recipe (1–5).
   Recipe-4 (demote to conjecture) items are claim changes — list them for owner
   sign-off, don't auto-demote. Recipe-5 (refute + restate) items change a
   *statement*, so they are claim changes too — but the refutation is machine-
   proved, so the evidence travels with the fix.

2b. **Sweep the cited sorries too, not just the closed proofs.** `grep -rnE
   '^\s*sorry\s*$'` the tree and run the §9 small-instance check on every hit.
   The 2026-08-08 sweep found 3 of 12 standing in front of false propositions —
   a higher genuine-defect rate than any of the regex-detectable patterns.
3. **Drain:** fix file-by-file (or small directory batches), microcommit per
   AGENTS.md branch+PR policy, verify each with `lean`-direct against the
   restored `lake-cache/qou-<toolchain-slug>` oleans (per
   `lean-environment-setup.md`).
4. **Backfill sidecars:** run `qa-sweep --only <criterion>` on the drained blocks
   so the green verdict is recorded.

## Current audit findings

See `docs/audits/2026-06-14-lean-vacuous-proof-audit.md` for the original list. As
of 2026-06-14: **12 HIGH-confidence self-assuming-projection instances** (6 from
the batch commit `e138518a`, 6 independent); `gauge-coupling-uniqueness` already
superseded with a genuine proof; 6 legitimate conditional-class proofs correctly
excluded.

2026-06-17 (`docs/audits/2026-06-17-lean-vacuity-axiom-audit.md`, full corpus
scan via the runnable scanner): 197 candidates / 178 files — 130 trivial-true (48
genuine `placeholder-true` gaps, 73 `conclusion-True`, 9 reflexive), 22
self-assuming-projection, 31 `native_decide`, 9 false-premise, **5
`proof-no-provable-axiom`** (all `LinearJSJVolume`, resolved to cited inputs:
`[thurston1978]` / `[manuscript]`). 39 sibling-stub shadows exempted.
