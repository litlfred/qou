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
