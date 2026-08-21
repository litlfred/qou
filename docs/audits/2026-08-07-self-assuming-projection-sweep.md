# Self-assuming projections — corpus sweep (2026-08-07)

Eight provable declarations in the corpus have the shape

```lean
theorem name ... (h : P) : P := h
```

The hypothesis *is* the conclusion. The proof term is the identity
function. Such a declaration asserts nothing about the objects it
mentions: it is `P → P`, true for every `P`, and it remains true if
every definition it names is replaced by a different one.

## How they were found

Not by the existing detectors, and not by design. The sweep came out of
running the triviality probe
([`lean-triviality-probe.ts`](https://github.com/litlfred/folio-assistant/blob/main/content/pipeline/lean-triviality-probe.ts))
against the QOU corpus. That probe rewrites each declaration's proof
body to `by <tactic>` down a cheapest-first ladder; `trivial` calls
`assumption`, so it closes exactly this shape.

Six of forty probed declarations closed. Reading them split four/two:

| Declaration | Closed by | Verdict |
|---|---|---|
| `standard_restricts_to_both_leptons` | `trivial` | **legit** — `branchingH3H2` is match-defined; `rfl` on a concrete value |
| `bring_trefoil_cinquefoil_channel` | `trivial` | **legit** — `decide` on concrete `torusKnotGenus` arithmetic |
| `genus_from_hecke_completeness` | `trivial` | **legit** — `interval_cases` + `decide` over a finite range |
| `genus_ideal_characterisation` | `simp` | **legit** — real content, discharged by Mathlib's `Ideal.mk_ker` |
| `defect_legendrian_knot` | `trivial` | **self-assuming** |
| `topological_charge_quantization` | `trivial` | **self-assuming** |

The four legit hits are the documented false-positive mode: content
living in a definition or in the `simp` set is not absence of content.
The two genuine ones motivated a static sweep for the shape, since it is
syntactic and the Lean probe is expensive (~11 min per 40 declarations,
so ~4.5 h for the corpus). The static pass covers 2590 files in 4.5 s.

## Why the existing gates do not catch these

[`lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
keys its trivial-true detectors on a conclusion of `True` (and, since the
`def`-disguise fix, on non-`theorem` kinds concluding `True`). A
self-assuming projection concludes something that *looks* substantive —
`Res_xi ≫ Φ = Φ`, a Fomin identity, an ILP minimality claim. There is:

- no `sorry` — the proof is complete
- no `axiom` — nothing is postulated
- no `True` — the conclusion is a real proposition
- no failed build — it type-checks, and always will

So every existing gate passes it. AGENTS.md §3b-cond item 5 already
names the pattern in the conditional-class setting ("a class that carries
the block's own conclusion as a field, with a *theorem* that merely
projects it"), and the honesty rules under §"Axiomatization is NOT a
Proof" and §"Strict Lean Discipline" item 5 forbid it. What was missing
was a detector.

## Findings

All eight confirmed by reading the declaration. Line numbers are on
`main` at `b48ce882fa`.

| # | Declaration | File:line |
|---|---|---|
| 1 | `defect_legendrian_knot` | [`brings-surface/defect-legendrian-knot.lean:47`](../../content/quantum-observable-universe/brings-surface/defect-legendrian-knot.lean) |
| 2 | `topological_charge_quantization` | [`brings-surface/topological-charge-quantization.lean:43`](../../content/quantum-observable-universe/brings-surface/topological-charge-quantization.lean) |
| 3 | `fomin_identity` | [`lean/QOU/Archimedean/BranchingConvergence.lean:138`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BranchingConvergence.lean) |
| 4 | `fomin_identity_n3` | [`lean/QOU/Archimedean/BranchingConvergence.lean:152`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BranchingConvergence.lean) |
| 5 | `length_bound_necessary` | [`lean/QOU/BraidKnot/PSDFeasibilityProxy.lean:94`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PSDFeasibilityProxy.lean) |
| 6 | `universal_ilp_selects_minimum` | [`nuclear-interactions/universal-ilp-algorithm.lean:43`](../../content/quantum-observable-universe/nuclear-interactions/universal-ilp-algorithm.lean) |
| 7 | `variational_transport` | [`quantum-observable-universes/categorical-action.lean:109`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.lean) |
| 8 | `ordering_extends` | [`unital-groebner-bases/lean/UGB/GrobnerShirshov/JetOrder.lean:213`](../../content/unital-groebner-bases/lean/UGB/GrobnerShirshov/JetOrder.lean) |

Three are worth quoting, because the gap between the name and the content
is where the cost lands.

**`fomin_identity`** — the comment states the move outright:

```lean
theorem fomin_identity (k n : ℕ) (hn : n ≤ k)
    (partitions_k : Finset (List ℕ))
    (dim_fn : List ℕ → ℕ)    -- dim(λ) = #SYT(λ)
    (mult_fn : List ℕ → ℕ)   -- m_μ^λ = #SYT(λ/μ) for fixed μ
    (dim_mu : ℕ)              -- dim(μ)
    -- Hypothesis: the sum satisfies the Fomin identity
    (h_fomin : partitions_k.sum (fun lam => dim_fn lam * mult_fn lam) =
      k.factorial / n.factorial * dim_mu) :
    partitions_k.sum (fun lam => dim_fn lam * mult_fn lam) =
    k.factorial / n.factorial * dim_mu :=
  h_fomin
```

Fomin's identity is assumed and then reported as proved. `dim_fn` and
`mult_fn` are uninterpreted function parameters, so the statement does
not even mention standard Young tableaux — the intended meaning lives
only in the `--` comments.

**`universal_ilp_selects_minimum`** — the name claims the ILP selects the
minimum; the proof assumes the minimality:

```lean
theorem universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    (K : KnotOperator q) (hK : universal_ilp q state K)
    (K' : KnotOperator q) (hK' : universal_ilp q state K')
    (hmin : K.crossing_number ≤ K'.crossing_number) :
    K.crossing_number ≤ K'.crossing_number :=
  hmin
```

`hK` and `hK'` — the entire ILP content — are unused. The theorem holds
verbatim with `universal_ilp` replaced by any predicate whatsoever.

**`topological_charge_quantization`** carries a `-- Ref: [yekutieli2015]`
citation and a docstring describing a residue computation, then proves
`h_reeb_residue → h_reeb_residue`.

## What this does and does not mean

Scope-(a), per AGENTS.md §"Before declaring refuted": this says the
*Lean* for these eight carries no content. It does **not** say the
underlying mathematics is wrong, nor that the narrative `.md` claims are
unsupported. Fomin's identity is a true theorem of the literature; the
question is only that our file does not prove it. The correct dispositions
are the three honest ones from §1a — prove it, state it with `sorry` + a
`-- Ref:`, or demote it to a `conjecture` — and choosing among them per
declaration is substantive work, not a mechanical edit.

**Nothing in this PR edits the eight declarations.** Rewriting a theorem
statement changes what the corpus claims, and for `fomin_identity` in
particular the honest restatement needs the actual SYT definitions rather
than uninterpreted parameters. Each is filed as its own bean.

## Tool

[`scripts/lean-self-assuming-audit.py`](../../scripts/lean-self-assuming-audit.py) —
static, no Lean required, 2590 files in 4.5 s.

```
python3 scripts/lean-self-assuming-audit.py content
```

Conservative by construction. It flags only a bare-identifier proof term
naming an explicit hypothesis whose type is syntactically identical to
the conclusion. It does **not** flag `:= by exact h`, `h.1`, `h.symm`,
`f h`, or any conclusion differing from the hypothesis even by
reassociation — all of those can do real work, and separating them needs
elaboration. So the eight are a floor, not a ceiling: the `by`-tactic
variants of the same laundering remain uncounted, and reaching them means
running the triviality probe corpus-wide.

Vendored trees under `.lake/` are skipped — Mathlib ships this shape in
`MathlibTest/` deliberately (`MathlibTest/CategoryTheory/Reassoc.lean`,
`MathlibTest/fun_prop_dev.lean`), and those three hits are correct
behaviour of *their* test suite, not findings.

## Follow-ups

1. Wire the check into
   [`lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
   as a `proof-self-assuming` criterion (critical), so it joins the
   review-ledger workflow that already governs the vacuity classes and
   gets an agent verdict per candidate rather than living in a standalone
   script.
2. Run the triviality probe corpus-wide to reach the `by`-tactic
   variants this static pass cannot see. Note that the probe currently
   needs the LEAN_PATH ordering fix — see below.

## Probe prerequisite: the LEAN_PATH shadowing bug

The probe skipped **928 of 938** blocks as "file does not elaborate
standalone" before this sweep was possible. That was not the corpus.
`leanPathFor` searched the *paper* Lake root before the workspace root,
and the paper's `.lake/packages` holds a vestigial near-empty copy of
each dependency (observed: 3 `batteries` oleans vs 85 at the workspace
root). LEAN_PATH resolution is first-match on the *directory*, so the
near-empty copy shadows the complete one and the import fails:

```
error: object file '.../lean/.lake/packages/batteries/.lake/build/lib/lean/
Batteries/Tactic/Lint.olean' of module Batteries.Tactic.Lint does not exist
```

which surfaces as "does not elaborate standalone" — a path bug wearing
the costume of a broken corpus. Ordering workspace roots first (matching
[`scripts/lib/lean-env.sh::lean_leanpath`](../../scripts/lib/lean-env.sh),
which already searches `$REPO_ROOT/.lake/packages` first) took the run
from *probed 10, closed 0, skipped 928* to *probed 40, closed 6,
skipped 27*. The fix belongs to `folio-assistant` and is not in this
repo's PR.

A sibling of the same bug in this repo is
[#4694](https://github.com/litlfred/qou/pull/4694): `lean-verify.sh`
counted oleans under `$LEAN_DIR` rather than `$REPO_ROOT`, re-running the
cache restore on every call (1m58s → 3s once fixed) and hard-failing on a
working tree whenever the cache branch was unreachable.

---

## 2026-08-21 revision — the count was 8 because the detector could not read its own hardest cases

Bean `qou/q407`. Two changes: the sweep tool was under-reporting, and one
of the findings has been discharged by proof.

### The detector silently skipped nested hypotheses

`scripts/lean-self-assuming-audit.py` parsed explicit binders with

```python
BINDER = re.compile(r"\((?P<names>[^():]+?)\s*:\s*(?P<type>(?:[^()]|\([^()]*\))*)\)")
```

The `type` alternation admits characters that are not parentheses, or **one**
parenthesised group. A hypothesis nesting two deep —

```lean
(h_invalid : ¬(w ≠ [] ∧ (∀ g ∈ w, g ≠ 0) ∧ (∀ g ∈ w, 3 ≤ Int.natAbs g ∧ …)))
```

— does not match, so the binder was dropped and the declaration could never be
reported. It **skipped, it did not fail**: a scan that cannot parse a
declaration and one that parses it and finds it clean produced identical
output. And the bias ran the wrong way, against exactly the elaborate
statements most likely to be hiding a tautology.

Replaced with balanced-delimiter scanning (`parse_binders`), which has no
depth limit and also reads `{..}`, `⦃..⦄` and `[..]` binders.

### The corrected sweep: 12, not 8

3008 `.lean` files (the original run saw 2590). All 7 still-open originals
reproduce, plus **five that were never visible**:

| declaration | file:line |
|---|---|
| `structurallyValidBinding_necessary` | `QOU/BraidKnot/PSDFeasibilityProxy.lean:103` |
| `jet_preserves_channel_separation` | `QOU/ChannelSeparation.lean:162` |
| `adjoint_has_no_degree_zero` | `QOU/GradedFrobeniusHopf.lean:116` |
| `plancherel_total_bound` | `mass-theory/plancherel-term-7-formulation.lean:61` |
| `plancherel_sum_eq_one` | `mass-theory/plancherel-term-7-formulation.lean:71` |

`structurallyValidBinding_necessary` is the sharpest illustration: it sits
**nine lines below** `length_bound_necessary` in a file the original sweep did
report, and differs from it only by having a more complicated hypothesis.

Two of the five are already honest in prose — `plancherel_sum_eq_one`'s own
docstring says "This is a parametric restatement, not a proof of the
q-deformed identity". That lowers the stakes of their disposition but does not
change the defect: a `**Theorem**` docstring over `theorem X (h : P) : P := h`
is what §3b-cond item 5 forbids, whatever the prose concedes.

### One finding discharged: `universal_ilp_selects_minimum`

`nuclear-interactions/universal-ilp-algorithm.lean`. The old statement took
`hmin : K.crossing_number ≤ K'.crossing_number` and returned it, so it said
nothing about `universal_ilp`.

Its docstring — "The LP selects the minimum-crossing feasible knot operator" —
names a genuine and provable claim: **the ILP attains its minimum**. Since
`crossing_number : ℕ`, the feasible crossing numbers form a nonempty set of
naturals and well-ordering supplies a least element:

```lean
theorem universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    (K₀ : KnotOperator q) (hK₀ : universal_ilp q state K₀) :
    ∃ K, universal_ilp q state K ∧
      ∀ K', universal_ilp q state K' →
        K.crossing_number ≤ K'.crossing_number
```

Proved, sorry-free; the file compiles clean. This is the §1a "prove it"
disposition, and it was available because the docstring already said what the
theorem should have been saying.

Worth flagging separately, not fixed here: that file defines
`gram_matrix _q = 0`, so `frobenius_positive` is vacuously true and
`universal_ilp` reduces to `is_knot ∧ crossing_number > 0`. The docstring
concedes this ("Trivial zero-witness"), so it is disclosed rather than hidden,
but the new theorem is correspondingly weak — it attains a minimum over a
feasible set whose Frobenius constraint currently constrains nothing.

### Note on verification

`JetOrder.lean` appeared to have three arity errors under a hand-rolled
`LEAN_PATH`. It does not: the container's `UGB/*.olean` were a month stale
(2026-07-19 objects against a 2026-08-15 source), so `OverlapComposition` was
being read without its `ord` parameter. Rebuilding the five-module chain with
`lean -o` cleared it, and the file compiles clean on `main`. Recorded because
the symptom — an arity error deep in an unrelated file — reads like a corpus
breakage rather than a cache-age problem. Use `scripts/lib/lean-env.sh`'s
`lean_leanpath`, and check olean mtimes before believing an arity error.

## 2026-08-21, second pass — a second vacuity shape: 27 candidates

The detector now covers the shapes the original pass listed as out of scope.

### `by exact h` and `by assumption`: widened, and found nothing

The original docstring excluded tactic proofs because "a `by exact h` may
still be vacuous but needs elaboration to judge". That is true of
`by exact <expression>` and false of `by exact <bare identifier>`: when the
argument names a binder whose type is the conclusion, it is exactly as
certain as the bare form. Both are now recognised, along with
`by assumption` (vacuous precisely when some binder already carries the
conclusion's type — the detector names which).

**Result: still 12 self-assuming.** No tactic-wrapped instance exists in the
corpus. Worth recording as a measured negative rather than an untested
assumption.

### New category `trivial-existential`: 15 findings

`∃ x, e = x` proved by `⟨e, rfl⟩`. No hypothesis is echoed, so it is not
self-assumption — but it is the same defect: the statement holds for **every**
`e` in a total type theory, so "`e` is well-defined" is not a theorem about
`e`. Five are named `*_well_defined` and are at least self-describing. Two are
not:

- **`wenzl_annihilator`** (`zeta8-witness-level2-su2.lean:168`). Docstring:
  "For any partition `λ` with first-column length `≥ 4`, the Hecke character
  `χ^λ` at `q = ζ` has zero quantum trace." Statement:
  `∃ chi_lambda_at_zeta : R, chi_lambda_at_zeta = 0`. That says a ring has a
  zero. `firstCol` and `_h : 4 ≤ firstCol` are **unused**, so it holds for
  first-column length 1 as readily as 4, and carries three literature Refs
  ([wenzl1987] §3 Thm 3.1, [jones1987] §5, [witten1989] §4) while proving
  nothing any of them says. Its docstring does concede "stated as a structural
  target".
- **`nuclear_knot_classification`** (`nuclear-knot-classification.lean:33`).
  Docstring: "For A ≥ 4, the nuclear braid is Borromean-like." Statement:
  `∃ K : NuclearKnotType, K = .borromean`, i.e. the constructor exists.
  `Z`, `N` and `hA : Z + N ≥ 4` are all unused; it holds for A = 0.

The remaining eight are `∃ y, f x = y` restatements of definitions
(`archimedean_eval_well_defined`, `n6/n7/n8_dimq_at_well_defined`,
`habiro_integral`, `regime_switched_binding_defined`, `phi_k_finite`,
`plancherel_term_7_finite`, `knot_factor_*`, `q_0_well_defined`,
`qou_standardPart_image_exists`, `spectral_decomposition_qvalue`).

A useful tell, cheap to check and not yet automated: **every one of these has
unused hypotheses.** A theorem whose binders do not appear in its conclusion is
not necessarily vacuous, but a vacuous one almost always has them.

### A second silent parser bug, fixed in passing

The conclusion was extracted at the **last** top-level `:` in the signature.
For a quantified conclusion that colon belongs to the quantifier:

```lean
theorem phi_k_finite (k : ℕ) … : ∃ x : ℝ, phi_k k blocks = x
```

gave conclusion `ℝ, phi_k k blocks = x`. Every `∃ x : T,` conclusion in the
corpus was therefore unanalysable — and, as with the binder regex, unparsed
and clean produced identical output. Now taken as the first `:` outside all
binder groups.

That is twice in one tool that a parsing limit silently shrank the reported
set. Both were invisible for the same reason: nothing distinguished "could not
read this" from "read it and it was fine".

## 2026-08-21, dispositions applied — 27 → 22

Five discharged, each by the §1a option its own evidence pointed to. No
declaration was rewritten to say something the corpus did not already claim.

### Proved: 3

- **`universal_ilp_selects_minimum`** — see above.
- **`ordering_extends`** (`JetOrder.lean`). Group (E) needed no ruling in the
  end: **the corpus had already answered it.**
  `QOU.AlgebraicSubstrate.AtomicityJetIndependence` records that "the block's
  `axiom ordering_extends` is tautological there", because the ordering is one
  global relation whose levels are restrictions, and recovers the genuine
  extension leg as `ltAt_extends`, derived from `level_mono`. Restated in this
  module's vocabulary: `degLexAt n a b := degLexNat a b ∧ (∀ g ∈ a, g < n) ∧
  (∀ g ∈ b, g < n)`, and `ordering_extends : m ≤ n → degLexAt m a b →
  degLexAt n a b`, proved from monotonicity of `<`. The levels are alphabet
  bounds; the docstring's "embedding" never existed.
- **`nuclear_knot_classification`**. The classification table existed **only in
  end-of-line comments** on the `NuclearKnotType` constructors, so nothing in
  Lean connected `(Z,N)` to a knot type and the theorem could not be about the
  classification. Transcribed the comments into `nuclearKnotType (Z N : ℕ)`
  and proved `4 ≤ Z + N → nuclearKnotType Z N = .borromean` — `hA` now does
  work. Added `bindingScale_of_borromean`, which is the proposition's own
  title ("closure type determines binding scale") and was not previously
  derivable. Could **not** be deleted: it is the `lean.ref` target of
  `prop:nuclear-knot-classification`.

### Deleted: 2

- **`length_bound_necessary`**, **`structurallyValidBinding_necessary`**
  (group (B)). Conventions of `binding-k-enumerator` written in the grammar of
  results — the first's docstring conceded "excluded from the search *by
  hypothesis*". Both conventions are now recorded as prose in
  `PSDFeasibilityProxy.lean` where they belong. Neither had a caller: the only
  corpus reference to either name was its own definition site.

  The alternative — define `inEnumeratorSearchSpace` and re-prove
  `¬bound → ¬inSpace` by `id` — was rejected: the definition would exist only
  to be echoed, which is the same defect one level up.

### Weakened to what is actually supported: 1

- **`wenzl_annihilator`**. Was `∃ x : R, x = 0`, i.e. a field has a zero, with
  `firstCol` and `4 ≤ firstCol` unused and three literature Refs attached. Now
  `∃ j ≤ firstCol, qInt ζ j = 0`, proved from the file's own
  `qInt_four_eq_zero` — the Wenzl truncation boundary being reached, which is
  the part of the claim this file can support. The full character statement
  (`χ^λ` has zero quantum trace at `q = ζ`) is documented as still open: there
  is no `χ^λ` in scope to state it about.

### Which of the rest can be deleted, and which cannot

Checked every remaining `trivial-existential` for `lean.ref` targeting. Three
are bound to content blocks and must be **restated, not deleted** —
`knot_factor_spectral_form`, `habiro_integral`,
`spectral_decomposition_qvalue`. The other ten have no reference beyond their
own definition site.

### The unused-binder tell does not generalise — measured

All 27 findings shared a property: hypotheses that never appear in the
conclusion. As a corpus-wide filter that fires **854** times (~28% of provable
declarations); requiring at least one relation-bearing binder brings it to
**447**, still ~15%. Ordinary theorems about global constants mention globals
rather than binders, and that is not a defect. So it ships behind
`--heuristic`, off by default, as a triage aid — **not** as a gate. Recorded
because the negative is worth knowing: the obvious generalisation of the tell
does not work.

## 2026-08-21, groups (A)/(C)/(D) applied — self-assuming count reaches zero

All twelve self-assuming projections are now discharged. The corpus-wide sweep
reports **0 self-assuming**, 13 trivial-existential.

### Ref-bound: the claim is named, not asserted (2)

`defect_legendrian_knot` and `topological_charge_quantization` are the
`lean.ref` targets of their content blocks, so deletion was not available.
Both are now **`def`s naming the condition** rather than theorems asserting it,
and both blocks move from `validation: "not_checked"` to
`validation: "stub"` — which is the accurate state and more informative than
"nobody ran the checker".

`def`-valued `lean.ref` targets are established practice here
(`QOU.Braiding.r_matrix_braiding_structure`), so the refs still resolve.

Worth recording about `defect_legendrian_knot`: its `zero : A ⟶ A` was a **free
variable merely named `zero`**, not the zero morphism. The suggestive reading
was fictional before you even asked what it proved.

### Deleted, with the claim recorded (7)

`variational_transport`, `jet_preserves_channel_separation`,
`adjoint_has_no_degree_zero`, `plancherel_total_bound`,
`plancherel_sum_eq_one`, `fomin_identity`, `fomin_identity_n3`. None had any
reference beyond its own definition site.

Two of these were **already diagnosed in place**:
`jet_preserves_channel_separation` and `adjoint_has_no_degree_zero` carried
inline `⚠` comments spelling out the `P → P` shape and citing bean
`qou-fav8` — including, for the latter, the observation that the real statement
"is expressible, but only once the adjoint object carries the grading too".
The diagnosis was right and had been sitting there; what it did not change is
that both still type-checked clean, so every gate still read them as proved.
**A comment is not a disposition.** That is the gap this pass closes.

### A near-miss worth noting

There are **two** declarations named `variational_transport`, in
`quantum-observable-universes/categorical-action.lean` and in
`lean/QOU/QuantumObservableUniverse/GaugeTheory.lean`. Only the first is
vacuous; the sweep never flagged the second. A name-based edit would have hit
the wrong one.
