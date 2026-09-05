---
# qou-ekga
title: 'GAP: 8 vacuous existentials, hidden by an ASCII-only detector — one claims to discharge an axiomatic class'
status: todo
type: task
priority: normal
created_at: 2026-09-05T08:33:27Z
updated_at: 2026-09-05T08:49:29Z
---

## What was found

`scripts/lean-vacuous-existential-audit.py` reported **0 candidates in 0 files**
on a tree holding **eight** live instances of the shape it exists to find.

Cause: `EXISTS_EQ` bound the variable with `[A-Za-z_][A-Za-z0-9_']*` — ASCII-only
— in a corpus that names its mathematical variables κ, δ, λ, τ, ρ by convention.
Every Greek-bound existential was structurally invisible. Fixed on
`claude/gram-kappa-laundered-axiom-2026-09-05` (Unicode pattern + a
`--self-test`, 10 fixtures, so a future narrowing cannot report zero silently).

Same class as `qou-r0ih` ("three Lean audits reported 0 candidates when handed
a single file") — an absent check indistinguishable from a passing one — by a
different mechanism.

## The 8 (detector fixed; DRAIN NOT DONE)

| file:line | decl | conclusion | proof |
|---|---|---|---|
| `lean/QOU/BraidKnot/MarkovAxiomsPrimitive.lean:171` | `markov_iterated_stab_gen` | `∃ τ_k, τ_k = τ * z^k` | `⟨τ * z^k, rfl⟩` |
| `…:178` | `markov_iterated_stab` | `∃ τ_k, τ_k = τ * (markovZax u)^k` | delegates to the above |
| `…:188` | `markov_iterated_stab_real` | `∃ τ_x_k_stab, … = τ_x * (markovZax_real q hq)^k` | delegates |
| `…:211` | `disjoint_product_factorisation_gen` | `∃ τ_joint, τ_joint = τ_K1 * τ_K2 * z^k` | `obtain … refine … ring` |
| `…:218` | `disjoint_product_factorisation` | same, `(markovZax u)^k` | delegates |
| `…:225` | `disjoint_product_factorisation_real` | same, `markovZax_real` | delegates |
| `mass-theory/gram-determinant-plancherel-ratio.lean:71` | `gram_determinant_plancherel_ratio` | `∃ κ, κ = gramKappa …` | `exact ⟨…, rfl⟩` |
| `observations/cp-violation-spectral-form.lean:48` | `cp_violation_spectral_form` | `∃ δ, δ = (W.chiAlt / W.chiSym).im` | `⟨…, rfl⟩` |

## The one that matters — a class "discharge" that discharges nothing

`MarkovAxiomsPrimitive.lean:238`, under a section header reading *"We can now
PROVE the previously-axiomatic `MarkovDisjointStabilisation` class from the more
fundamental `MarkovTraceAxioms` class"*:

```lean
theorem MarkovTraceAxioms_implies_disjoint_stabilisation
    {R : Type*} [Field R] (u : R) [h : MarkovTraceAxioms u] :
    ∀ τ_x : R, ∃ τ_x_stab : R, τ_x_stab = τ_x * markovZax u := by
  intro τ_x
  refine ⟨τ_x * h.tau_stab_factor, ?_⟩
  rw [h.tau_stab_factor_eq_z]
```

Citing `h.tau_stab_factor` and `h.tau_stab_factor_eq_z` makes it look as though
the axioms do the work. **They do not — MEASURED, not asserted.**
`docs/audits/…` probe, `lean`-direct **exit 0**, two theorems:

- the same statement proved `fun τ_x => ⟨τ_x * markovZax u, rfl⟩`, never
  touching `h` — Lean itself then reports `unused variable h`;
- the same statement with an **arbitrary function** `f : R → R` in place of
  `markovZax`, also proved by handing back the RHS.

So the declaration constrains the Markov parameter not at all. Per AGENTS.md
§Axiomatization is NOT a Proof, this is the anti-laundering shape: an axiomatic
class reported as discharged by something that asserts nothing.

Note the detector cannot see this one either — its conclusion opens with `∀`,
not `∃`, so it is outside `EXISTS_EQ` even after the Unicode fix. **A ninth
instance, found by reading rather than by scanning.**

## Blast radius: SMALLER than the docstring implies — check before alarm

`MarkovDisjointStabilisation` is a real content-bearing class
(`mass-endomorphism/categorical-chain-convergence-mechanisms.lean:105`, field
`stab_spec`) with live consumers (`stabIter`, `stabIter_spec`,
`inter_knot_decoupling`). But `MarkovTraceAxioms_implies_disjoint_stabilisation`
is a **theorem, not an `instance`**, and has **zero consumers** — so the
"discharge" was never wired. The class stays axiomatic and every
`[MarkovDisjointStabilisation q]`-conditional result stays honestly
conditional. Nothing downstream is contaminated; the defect is the false claim
in the prose, not a laundered number.

## Scope

Scope-(a), and deliberately: this is a claim about the Lean ENCODINGS. That
`markov_iterated_stab_gen` does not encode "k applications of M3 give τ·z^k"
says nothing about whether that is true of the Markov trace.

## Honest dispositions available (§1a)

Per case: prove the real statement (an equation against an independently
defined quantity, e.g. `deltaCP W = (W.chiAlt / W.chiSym).im` — `deltaCP` is
already defined four lines above its vacuous existential and the theorem does
not mention it); or state it with `sorry` + `-- Ref:`; or demote. Not done
here — it is content work across three files and wants its own branch.

Two further specifics worth carrying into that work: `cp_violation_spectral_form`
is declared a `theorem` while its own docstring calls it a **Conjecture**, and
its `[ComplexSubstrate]` binder is unused.


## 2026-09-05 — the ∀-prefixed shape is BOUNDED at one (measured)

The write-up above records a ninth instance the fixed detector still could not
see, its conclusion opening with `∀`. Measured over the same 3606 files with a
standalone probe before changing anything: **exactly one** such instance
corpus-wide, and it is that same already-known declaration. There is no hidden
reservoir behind this shape.

Wired into the detector anyway (`strip_forall`, one `∀` group, findings carry
`forall_prefixed`), on the grounds that a documented blind spot nobody closes
becomes a permanent one — and the measurement is what makes it safe to wire,
since nothing unexpected lands with it. Live scan **8 → 9 in 3 files**;
self-test 10 → 13 fixtures, 13/13.

So the drain queue is **9**, not 8, and the count is now complete for both
shapes rather than open-ended.


## 2026-09-05 (2) — the root under the Markov six: the class has no trace, and is trivially inhabited

The six `MarkovAxiomsPrimitive.lean` entries above are a symptom. Reading the
file end to end: **it contains no trace function at all.** Every declaration in
it is `markovZax` (three variants), the class, and the seven theorems. The `τ`
in every one of those theorems is a free scalar the caller supplies, with no
connection to any Markov trace — which is why the claims could only be phrased
as `∃ x, x = <expr>`: there is no object for them to be about.

`QOU.BraidKnot.MarkovTraceAxioms` has four fields and none is a trace:

```lean
tau_identity : R                              -- a scalar
tau_identity_eq_one : tau_identity = 1        -- pinned to 1
tau_stab_factor : R                           -- a scalar
tau_stab_factor_eq_z : tau_stab_factor = markovZax u   -- pinned to z
```

Both scalars are pinned by their own equations, so the class has exactly one
inhabitant per `u`. **Verified, not argued** — `docs/audits/2026-09-05-markov-trace-axioms-triviality-probe.lean`,
`lean`-direct **exit 0**: `instance … : MarkovTraceAxioms u := ⟨1, rfl, markovZax u, rfl⟩`
type-checks for ANY `u` in ANY field, and a `[MarkovTraceAxioms u]`-conditional
theorem is then obtained with only that trivial instance in scope. So the
conditionality is decorative — the `qou-7yj0` shape ("conditional-on-conjecture
is decorative"), here on a class calling itself *axioms* in its own name.

### 🛑 SCOPE — three classes share this name; only ONE is trivial

I nearly attributed the triviality across the shared name, which is the
`markovZ` hazard AGENTS.md documents ("attributes do not transfer across
overloaded symbols"). Measured:

| namespace | fields | verdict |
|---|---|---|
| `QOU.Braiding` (`mass-theory/markov-trace-product.lean:83`) | `trace : List GeneratorChain → R_q`, `trace_nil`, `trace_cons` | **content-bearing** |
| `QOU.Hecke` (`lean/QOU/Hecke/MarkovTraceProduct.lean:63`) | the same three | **content-bearing** (near-duplicate of the above) |
| `QOU.BraidKnot` (`lean/QOU/BraidKnot/MarkovAxiomsPrimitive.lean:146`) | two scalars + two pinning equations | **TRIVIALLY INHABITED** |

The theorems in `markov-trace-product.lean` (`markov_trace_pair`,
`markov_trace_append`, `markov_trace_product_recursion`, …) are conditional on
the **content-bearing** class, do real cons-induction against a real `trace`,
and are **NOT** affected by any of this.

### Blast radius: total containment

Every consumer of the trivial `QOU.BraidKnot` class is **inside its own file** —
the six existentials at 178/188/218/225 and the unwired discharge at 239.
Nothing outside `MarkovAxiomsPrimitive.lean` depends on it. So this is a
self-contained defect, not a corpus-wide contamination.

### What the repair actually needs

Not a restatement. The honest claims ("k applications of M3 give `τ·z^k`";
"disjoint braids factorise") are claims **about a trace**, and this file has
none. Either the file adopts the content-bearing class (which already exists,
twice) and states equations against its `trace`, or the six theorems are
withdrawn as premature. That is a design decision about which of the three
classes is canonical, and it is upstream of any Lean edit.

Worth noting separately: `QOU.Braiding` and `QOU.Hecke` hold near-identical
copies of the content-bearing class. Whether that duplication is deliberate
(content block + library sibling) is unexamined here.
