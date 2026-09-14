# The conjunctive self-assuming projection, and why one detector could not express it

**Date** 2026-09-14 · **Beans** `qou-wbtz` (the finding), `qou-a2d7`, `qou-9gpo`,
`qou-9b3p`, `qou-z9ws` · **Taxonomy** row 46 in
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md)

## What was blind, and how blind

[`scripts/lean-self-assuming-audit.py`](../../scripts/lean-self-assuming-audit.py)
had exactly two rules:

1. the proof IS a bare binder whose declared type equals the conclusion;
2. the proof is a single qualified projection `X.f …` whose field type equals
   the conclusion.

It had **no handling of Lean's anonymous constructor at all** — `⟨` occurred
nowhere in the file. A theorem concluding `A ∧ B ∧ C` proved by `⟨X.a, X.b,
X.c⟩`, where `a`/`b`/`c` are exactly the carrier fields declaring `A`/`B`/`C`,
exited the candidate gate *before its conclusion was ever parsed*: `⟨` matches
no rule-1 or rule-2 pattern, so `analyze()` `continue`d. The class was invisible
**by construction**, not missed case by case — the same shape of failure the
taxonomy has now recorded forty-five times.

## Before / after

Measured on `content/` at `a251f70059`, and note the root matters:

| root | `.lean` scanned | before | after |
|---|---|---|---|
| `content` (the script's default) | 3852 | **41** | **48** |
| `content/quantum-observable-universe/lean` | 2882 | 30 | 37 |

The 41 pre-existing `class-field-is-conclusion` hits are **byte-identical**
before and after, checked by set comparison on `(file, line, decl, variant)`
rather than by count. `hypothesis-is-conclusion` was 0 before and is 0 after.
The new variant `conjunction-is-conclusion` is **7**, over 6 files, with 2–6
components.

The finding bean `qou-wbtz` quotes "30 candidates over 2880 `.lean`". That is
the **`…/lean` root**, not the script's default `content`; on the default it was
41 over 3852. Both are right about different roots — state which you ran.

## What it must NOT catch, and why the discrimination is structural

AGENTS.md §3b-cond item 5 names
[`QOU/FluidDynamics/q_bkm_criterion.lean`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean)
as the **verified exemplar** of a *legitimate* conditional-class theorem:
"carry the two directions of an iff as hypotheses, derive it by `Iff.intro`."
Its proof term is shape-identical to the defect:

```lean
theorem q_bkm_criterion {R : Type*} [CommRing R] [ctx : QBKMContext R] :
    ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite :=
  ⟨ctx.bkm_necessity, ctx.bkm_continuation⟩
```

A rule that widened until it caught this would be worse than no rule. The
separation is **structural, not a name list**: `A ↔ B` is not the conjunction of
the two hypothesis types, and `↔` binds looser than `∧` in Lean, so
`conjuncts()` refuses any conclusion carrying a top-level `↔`, `→` or `,` (the
last being a quantifier body, `∀ x, P x ∧ Q x`). The component counts can then
never agree, and the exemplar is excluded without ever being named.

Five corpus theorems the hand regex found are excluded exactly this way, and all
five are correctly excluded:

| theorem | file:line | conclusion | why excluded | verdict |
|---|---|---|---|---|
| `q_bkm_criterion` | `QOU/FluidDynamics/q_bkm_criterion.lean:69` | `ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite` | top-level `↔` | **legit** — the §3b-cond exemplar |
| `ns_obstruction_tower` | `QOU/FluidDynamics/ns_obstruction_tower.lean:46` | `ctx.is_NS_singular ↔ ∃ n, ctx.res_sigma n ≠ 0` | top-level `↔` | **legit** — same `Iff.intro` shape, same file family |
| `p_bandwidth_bound` | `QOU/Information/p_bandwidth_bound.lean:112` | `ctx.inP ↔ ctx.bandwidthBounded` | top-level `↔` | **legit** — same shape |
| `equivalence_of_faithfulness` | `QOU/Information/PNeqNpEquivalence.lean:72` | `r ≠ 0 ↔ P` | top-level `↔`; also projects a NAMESPACE (`ResidueFaithfulness.faithful`), not a binder | **legit** |
| `Positive.sigma` / `Positive.tau` | `QOU/Knot/M004AngleStructure.lean:125,130` | `Positive γ₁ β₁ α₁ α₂ γ₂ β₂` | a structure application has no top-level `∧` | **legit** — `⟨h.hγ₁, h.hβ₁, h.hα₁, h.hα₂, h.hγ₂, h.hβ₂⟩` **permutes** its components; that is content |

`Positive.sigma` is worth separating from the `Iff` three. The hand regex
counted it as a 6-component conjunctive projection, and it is not a conjunction
at all — it is a structure-instance constructor for a *permuted* argument list.
So of the 13 hand-regex candidates, **7 are the defect, 5 are legitimate, and 1
(`q_bkm_criterion`) was already flagged as the fairness case in the bean**; the
hand count over-stated the defect population by 6.

## The comparison tolerance, measured four ways

A field type is written **inside** the carrier, where the binder's type is
spelled out; the conclusion is written at the **use site**, where Lean infers it
and the author omits it. `JetHorizon.degree_zero_vanishes` declares
`∀ (s : algebra.sections 0), s = algebra.zero 0`; `qou_is_ccc`'s conjunct is
`∀ s, s = H.algebra.zero 0`. Same proposition. Raw text can never see it.

So the comparison normalises in three narrow ways — sibling qualification
(`algebra` → `H.algebra`, the rewrite rule 2 already did), outer parentheses,
and an inferable binder ascription. Each tier was measured on the same tree
rather than asserted, by monkey-patching the step off and re-running the whole
scan:

| tolerance tier | conjunctive candidates |
|---|---|
| literal text comparison | 1 |
| + outer-paren strip | 4 |
| + quantifier ascription strip (`∀ (x : T),` → `∀ x,`) | 6 |
| + lambda ascription strip (`fun j : U =>` → `fun j =>`) | **7** |

No tier is doing most of the work and none is merely defensive. The 41 rule-2
hits are unaffected at every tier.

**Is it too tolerant?** Checked component by component, not in aggregate. Across
the 7 hits there are **23 components**; **16 match EXACTLY after sibling
qualification** and **7** need an ascription strip. Nothing matched by anything
looser. Two propositions the strips equate differ *only* in an annotation the
elaborator supplies, so if the file compiles they are the same proposition — the
tolerance cannot manufacture an agreement Lean does not already have.

**The judgement call, stated as one.** The lambda tier is the one I would defend
least confidently and it is the one that buys exactly one hit
(`lp_dual_stability`). `fun j : Fin n => f j` and `fun j : Fin m => f j` differ
only in the ascription and *are* different terms; stripping equates them. I
accept that because a genuine disagreement there would be a type error and the
file compiles — but it is a judgement, not a proof, so it sits behind the module
flag `STRIP_LAMBDA_ASCRIPTIONS` and is the documented way to re-measure. It is
also pinned by a selftest fixture: without that fixture the flag could be
flipped off and the selftest still passed (measured — it did).

## Cross-check against the TypeScript detector, which DOES handle tuples

This is the half of the result that matters most, and it runs both ways.

`content/pipeline/lean-vacuity-axiom-audit.ts` has had `TUPLE_PROJECTION` and
`APPLIED_TUPLE_PROJECTION` for some time (taxonomy row 42), and its adjudications
live in [`lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json)
(332 entries, 96 of them `proof-no-self-assuming-projection`, ledger
`updated_at` 2026-09-14T07:56Z). Of my 7:

* **4 are already in that ledger**, every one adjudicated `verdict: genuine`,
  `disposition: restate-to-derive-or-demote` —
  `confinement_frobenius_reciprocity`, `four_term_pair_nucleon`,
  `lp_dual_stability`, `parity_regime_selection`. An independent detector
  written without consulting the ledger reproduces four standing `genuine`
  adjudications exactly: **zero false positives on the overlap**.
* **3 are in no ledger entry at all** — `qou_is_ccc`,
  `ccc_boundary_data_exists`, `deuteron_binding_energy`. Their files
  (`JetHorizon.lean`, `deuteron_binding_energy.lean`) have **zero** ledger
  entries of any category.

Zero entries is row 43's trap — indistinguishable from a file the scan never
visited — so the cause was measured rather than inferred, by running the TS
regex on the actual bodies in `node`:

```js
const TUPLE_PROJECTION =
  /^⟨\s*([a-z][\w']*)\.[A-Za-z_][\w']*\s*(?:,\s*\1\.[A-Za-z_][\w']*\s*)*⟩\s*$/;
```

| body | matches | control |
|---|---|---|
| `⟨H.degree_zero_vanishes, H.degree_one_leaks, H.degree_two_leaks⟩` | **no** | lowercase the binder to `h` → **MATCH** |
| `⟨H.degree_one_leaks, H.degree_two_leaks⟩` | **no** | same |
| `⟨ctx.h_ΔE_exp, ctx.h_ΔE_bind_precision⟩` | **no** | ASCII-ise to `h_dE_exp` → **MATCH** |
| the other four | MATCH | — |

So the TS detector misses these three for two precise, controlled reasons, and
neither is about the shape it already handles:

1. **The binder's CASE.** `([a-z][\w']*)` requires the binder to start with a
   lowercase ASCII letter. `qou_is_ccc` binds `(H : JetHorizon)`. Lowercasing
   the same body makes it match, so case is the whole cause.
2. **The identifier's ALPHABET.** JavaScript `\w` is ASCII-only (`/\w/.test("Δ")`
   is `false`), so a field named `h_ΔE_exp` cannot be matched. This is taxonomy
   row 35 — *the identifier's alphabet* — recurring in a second tool, in a
   second language, where it is a property of the regex engine rather than of
   the author's pattern.

The same alphabet problem was present on the Python side and is fixed here:
`CLASS_FIELD` was `[A-Za-z_][A-Za-z0-9_']*`, so Unicode-named fields never
entered the field map at all. Python's `\w` *is* Unicode-aware for `str`
patterns, and subscript digits `₀-₉` are `isdigit()`, so `[^\W\d][\w'!?]*` is
the right class. Behaviour-neutral for rules 1–2 (41 → 41, no adds, no losses)
and necessary for rule 3.

**Three of the seven were invisible to every detector in the corpus.** The
overlap is 4/7, and the two tools are blind in different directions.

## The blind spot was KNOWN, in a bean, for two weeks

Corpus-grep path 6 found it. Bean `qou-9gpo`, re-triaged 2026-08-31:

> `confinement_frobenius_reciprocity`'s proof is `⟨ctx.reciprocity,
> ctx.primal_nontrivial, ctx.y_0_star_pos, ctx.A_star_nonempty, …⟩` — six
> conjuncts, six class fields, the first of which is literally named
> `reciprocity`. […] **Note it is MISSED by
> `scripts/lean-self-assuming-audit.py`: that tool needs the whole proof term to
> be a single identifier, so a conjunctive `⟨…⟩` of projections never matches.**

That is this blind spot, named correctly, fourteen days before it was closed.
(The bean's description of the tool is a little behind — rule 2 does accept an
*applied* single projection — but its conclusion is exactly right.) So this work
**closes a recorded gap**; it does not discover one.

## Triage — the seven

Verdict vocabulary and dispositions follow the review ledger's own
(`genuine` / `legit` / `advisory`; `restate-to-derive-or-demote`).

**All seven are `genuine`. None is `legit`. None is `advisory`.** Every one is
pure re-bundling: the carrier asserts each conjunct and the anonymous
constructor is the identity on the hypotheses. Where a docstring *claims*
otherwise, that is recorded below as a second defect rather than as mitigation.

---

### 1. `qou_is_ccc` — `QOU/JetHorizon.lean:306`, carrier `structure JetHorizon:57`

```lean
theorem qou_is_ccc (H : JetHorizon) :
    (∀ s, s = H.algebra.zero 0) ∧
    (∃ s, s ≠ H.algebra.zero 1) ∧
    (∃ s, s ≠ H.algebra.zero 2) :=
  ⟨H.degree_zero_vanishes, H.degree_one_leaks, H.degree_two_leaks⟩
```

The three carrier fields are, verbatim:

```lean
  degree_zero_vanishes : ∀ (s : algebra.sections 0), s = algebra.zero 0
  degree_one_leaks     : ∃ (s : algebra.sections 1), s ≠ algebra.zero 1
  degree_two_leaks     : ∃ (s : algebra.sections 2), s ≠ algebra.zero 2
```

**Verdict `genuine`.** Zero derivation. Note this is not a §3b-cond
conditional-class at all — `JetHorizon` is a data `structure` taken as an
explicit binder, so there is no instance gate; the theorem says "any `H` whose
three fields hold, has its three fields hold."

Bean `qou-a2d7` reached the same reading independently on 2026-09-14 by hand:
*"definitional restatement, correctly caveated in prose, oversold by the
proposition TITLE."* The `.md` and the Lean docstring are both candid (the
docstring says CCC-2, the only non-definitional leg, "is not yet formalised
here"); the defect is that `prop:qou-is-ccc` is stated as a proposition.
**Disposition: restate-to-derive-or-demote.**

### 2. `ccc_boundary_data_exists` — `QOU/JetHorizon.lean:281`, same carrier

```lean
theorem ccc_boundary_data_exists (H : JetHorizon) :
    (∃ s, s ≠ H.algebra.zero 1) ∧ (∃ s, s ≠ H.algebra.zero 2) :=
  ⟨H.degree_one_leaks, H.degree_two_leaks⟩
```

**Verdict `genuine`**, and additionally **redundant**: its conclusion is
conjuncts 2–3 of `qou_is_ccc` and its proof is the corresponding sub-tuple. Two
declarations, one non-statement. Same disposition.

### 3. `deuteron_binding_energy` — `QOU/HadronicMass/deuteron_binding_energy.lean:54`, carrier `:29`

```lean
theorem deuteron_binding_energy [ctx : DeuteronBindingEnergyContext] :
    ctx.ΔE_exp = 2.2246 ∧ |ctx.ΔE_bind - ctx.ΔE_exp| < 0.001 :=
  ⟨ctx.h_ΔE_exp, ctx.h_ΔE_bind_precision⟩
```

```lean
  h_ΔE_exp             : ΔE_exp = 2.2246
  h_ΔE_bind_precision  : |ΔE_bind - ΔE_exp| < 0.001
```

**Verdict `genuine`, and the most consequential of the seven.** The carrier
axiomatises the AME/CODATA number *and the accuracy claim itself*. A Lean
theorem whose content is "the prediction is within 1 keV" and whose proof is
"because the class says so" is the anti-fit discipline's worst case wearing a
proof: it is a *tolerance asserted as an axiom*.

Mitigation, such as it is: the docstring is honest — *"the substantive
mathematical content is carried by the context-class axioms, and a full
derivation from substrate primitives remains pending."* That keeps it out of
`advisory` all the same, because the DECLARATION is the artifact a reader cites.
**Disposition: restate-to-derive-or-demote** — the honest form is a
`conjecture`, or a carrier holding the *substrate* inputs with the
0.001 bound DERIVED.

### 4. `confinement_frobenius_reciprocity` — `QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean:105`, carrier `:53`

Six conjuncts, six carrier fields, matched one-for-one:

```lean
  ⟨ctx.reciprocity, ctx.primal_nontrivial, ctx.y_0_star_pos,
   ctx.A_star_nonempty, ctx.active_iff_pos_shadow, ctx.strong_duality⟩
```

**Verdict `genuine`** — already the standing ledger verdict, and already
re-triaged in bean `qou-9gpo` (which corrected an earlier "infra-blocked"
stamp). **What is new here is a second, independent defect: the file's prose
asserts the opposite of its own code.**

The module docstring, §"Disposition (integrity)", lines 21–43:

> "It does **not** carry the reciprocity formula or the LP sub-claims as fields
> (the previous versions did — first a `theorem := ⟨ctx.claim_*⟩` self-assuming
> projection, then a `def … : Prop` …) […] `confinement_frobenius_reciprocity`
> now states the genuine `.md` claim […] and ends in `sorry` (disposition B)."

and the carrier's own docstring, lines 49–52 (the quoted clause is line 51):

> "All fields are *inputs* […]; **none asserts the reciprocity conclusion**."

Measured against the file: the carrier's field 13 is
`reciprocity : ∀ O : Observable, physExp O = ∑ …` — the master formula — and
five more fields carry the five LP sub-claims. **The file contains no `sorry`.**
The single occurrence of the string `sorry` in the whole file is at line 37,
inside the prose sentence quoted above. So both claims are false, and the
paragraph describing the repair is the only surviving trace of it.

This is the *same wording* as row 42's exposing case
(`mobius_frobenius_kernel.lean`, "All fields are inputs; none is the
conclusion"), over a field that was the conclusion. **Disposition:
restate-to-derive-or-demote; and correct the prose, which is currently a false
integrity attestation.**

### 5. `lp_dual_stability` — `QOU/ParticleInteractions/lp_dual_stability.lean:86`, carrier `:41`

```lean
  ⟨ctx.primal_stable, ctx.dual_price_bound, ctx.partial_unstable,
   ctx.strong_duality⟩
```

**Verdict `genuine`** — standing ledger verdict. Same prose/code contradiction,
and here the corpus records that **the repair was made and is not in the tree**.
Module docstring §"Disposition (integrity)", lines 20–35; and the carrier's
own docstring, lines 39–40, reads "All fields are *inputs*; none asserts a
conclusion":

> "It does **not** carry the four conclusions as fields (the previous version
> did, then projected them — the self-assuming projection forbidden by
> AGENTS.md §3b-cond item 5). `lp_dual_stability` states the genuine four-part
> conjunction over that data **and ends in `sorry` (disposition B)**"

Bean `qou-9b3p` (reopened 2026-08-21):

> "The `sorry` was replaced by a new context-class field carrying the theorem's
> own conclusion, and the proof became a projection […] The commit also deleted
> the sorry-free `*_unconstrained_false` refutation that proved the class was
> too weak. **PR #5411 restored the prior state**: honest `sorry` + `-- Ref:`
> citation, and the refutation theorem back in place."

Live file today: the four conclusion fields are present, the proof is the
4-tuple, there is **no `sorry`** (the only occurrence is the prose at line 30),
and **no `*_unconstrained_false` theorem** anywhere in the file. Whether that is
a revert, a bad merge, or a repair that never reached this branch is **not
settled here** — the clone is shallow (54 commits) and `git log -- <file>`
returns one commit, so the history that would decide it is not present. What is
measured is only that prose and code disagree, and which one the bean says was
correct. **Disposition: restate-to-derive-or-demote, and re-check against #5411
with a full history.**

### 6. `parity_regime_selection` — `QOU/ParticleInteractions/parity_regime_selection.lean:70`, carrier `:31`

```lean
  ⟨ctx.sign_identity, ctx.odd_regime, ctx.even_regime, ctx.neutron_regime⟩
```

**Verdict `genuine`** — standing ledger verdict — and the one case where the
prose is *candid about having introduced the defect deliberately*, module
docstring lines 12–18:

> "The original encoding carried only data fields with no relation to the
> conclusion — making the `sorry` provably refutable
> (`parity_regime_selection_unconstrained_false`, **now deleted**). Fixed by
> adding the four regime identities as upstream class fields. The conclusion
> follows by assembly."

That is the exact move bean `qou-9b3p` says was reverted for `lp_dual_stability`
in the same August window, applied here and left standing — and the refutation
witness that proved the carrier too weak was deleted with it. (Sibling files
kept theirs: `QOU/FluidDynamics/q_turbulence_spectrum.lean:197` and
`QOU/Molecular/shell_filling_rule.lean:182` still carry
`*_unconstrained_false`.) Replacing a refutable `sorry` with an unrefutable
re-bundle is not one of the three honest dispositions.
**Disposition: restate-to-derive-or-demote; restore the refutation witness.**

### 7. `four_term_pair_nucleon` — `QOU/ParticleInteractions/four_term_pair_nucleon.lean:118`, carrier `:57`

```lean
  ⟨ctx.proton_net_match, ctx.neutron_net_match⟩
```

**Verdict `genuine`** — standing ledger verdict — **with the best disclosure of
the seven**, and it is worth quoting because it shows the drift being caught by
hand once already:

> "**Not a `sorry` — the body is `⟨ctx.proton_net_match, ctx.neutron_net_match⟩`
> (corrected 2026-09-03).** This paragraph began "Honest `sorry`:";
> `#print axioms` reports no `sorryAx`. The two net values are context-class
> fields and this theorem pairs them, so they are assumed by whoever
> instantiates the class."

So this file is the third instance of the same prose/code drift as #4 and #5, it
was found by hand on 2026-09-03, and the fix applied was to the **prose**. The
declaration still assumes its own conclusion. Note the genuinely proved
neighbour in the same file, `confinement_universality` (line 95), which derives
polarization-independence from `MarkovTrace.trace_conj_of_mul_eq_one` — that is
what a derivation in this file looks like, and it is not what
`four_term_pair_nucleon` does. **Disposition: restate-to-derive-or-demote.**

---

## Summary

| | count |
|---|---|
| hand-regex candidates in bean `qou-wbtz` | 13 |
| → flagged `conjunction-is-conclusion` | **7** |
| → correctly excluded (`Iff` assembly ×4, permuting structure instance ×2) | 6 |
| verdicts: `genuine` / `legit` / `advisory` | **7 / 0 / 0** |
| already `genuine` in the TS review ledger | 4 |
| flagged by no detector in the corpus before today | **3** |
| files whose own docstring contradicts their code on this point | **3** (#4, #5, #7 — #7's prose already corrected) |

## What is NOT covered, and must be said

* **Carriers are resolved within the declaring file only.** `parse_classes`
  reads `class`/`structure … where` blocks in the same file; a carrier imported
  from another module, or reached through `extends`, is not resolved and the
  candidate is dropped silently. Every count here is a **lower bound**, not a
  clean bill. The script now prints this on every run, because an unstated
  limitation reads exactly like an all-clear.
* **Rules 1 and 2 are still ASCII-only in their proof-term patterns.** Only
  `CLASS_FIELD` was widened. A rule-1 or rule-2 body whose binder or field is
  Unicode is still invisible. Measured: widening `CLASS_FIELD` alone changed
  nothing for those rules (41 → 41), so the remaining exposure is unquantified
  rather than known-zero — row 35 again, and I am leaving it open rather than
  changing two rules in a commit about a third.
* **Applied components are rejected** (`ctx.field s t` inside a tuple). Their
  type is `P s t`, which cannot equal a conjunct written without the
  application, so admitting them would widen the surface without ever matching.
  The TS detector's `APPLIED_TUPLE_PROJECTION` handles that case on its side.
* **Left-nested tuples are not flattened.** `⟨⟨a, b⟩, c⟩ : (A ∧ B) ∧ C` is a
  different association from `⟨a, b, c⟩ : A ∧ B ∧ C`; only the right spine is
  spliced. A left-nested defect would be a false negative.
* **No `.lean` file was edited.** This task is detector plus triage. The seven
  dispositions are recorded, not applied.

## Reproducing

```sh
python3 scripts/lean-self-assuming-audit.py --selftest    # 7 fixtures + 8 units
python3 scripts/lean-self-assuming-audit.py content       # 48 = 41 + 7
```

The selftest pins **both** ends — three positives (`qou_is_ccc`,
`ccc_boundary_data_exists`, `lp_dual_stability`), three negatives
(`q_bkm_criterion`, `equivalence_of_faithfulness`, `Positive.sigma`), two rule-1/2
regression fixtures — so the rule can neither regress to zero nor widen onto the
sanctioned exemplar. Mutation-tested: disabling rule 3 fails with three
`MISSED`; weakening the `↔`/`→` guard fails on a unit; flipping
`STRIP_LAMBDA_ASCRIPTIONS` off fails on `lp_dual_stability`.
