# P3.1 policy decision — three options for §3b strict propagation

## Background

AGENTS.md §3b STRICT conjectural-propagation rule: a provable
block (`theorem`/`proposition`/`lemma`/`corollary`) whose
`uses[]` cone transitively touches a `conj:` must be `conjecture`
(or `remark` with `interprets:`).

Current audit
([2026-05-01-p3-1-conjectural-propagation.witness.json](2026-05-01-p3-1-conjectural-propagation.witness.json)):
**233 provable blocks** transitively touch conjectures. After
the body-asymptotics-catalog fix
([2026-05-02-cone-sweep-status.md](2026-05-02-cone-sweep-status.md)),
no further catalog-style leaks remain. The 233 are structurally
correct dependencies on the 9 bridge conjectures.

This memo presents three policy options for closing P3.1.

---

## Option A — STRICT demotion (mechanical)

**Action.** Relabel all 233 provable blocks as `conjecture`. Add
narrative `**Conjecture (... conditional on conj:X).**` banners.
Run a codemod across `.ts` manifests + `.md` headings.

**Effort.** 1–2 days (mostly mechanical).

**Pros.**
- Strictly correct per §3b — no rule violations.
- Validation rule `conjectural-propagation` passes 100%.
- Conservative; honest about what's proved vs assumed.

**Cons.**
- Massive narrative downgrade — all "Theorem" → "Conjecture
  (conditional on …)" headings cascade across the paper.
- The framework's *core results* (mass formula, BW coefficients,
  shell-closure derivation) all become conjectural in name.
- **Doesn't reduce the cone size** — just relabels.
- Reviewers may interpret 233 `conjecture` blocks as the
  framework being "all conjectures", missing that ~220 are
  rigorous *conditional* derivations.

**Recommendation.** Reject — the sea-of-conjectures presentation
under-represents the actual structure (rigorous conditional
results conditional on a small set of substrate conjectures).

---

## Option B — Substrate-axiom classification (recommended)

**Action.** Identify a small set of **substrate-foundation
conjectures** (≤ 20 from the audit). Axiomatise each as a Lean
`class` with explicit content. Downstream provable blocks become
*conditional theorems* over that class instance:

```lean
class CategoricalNeutralitySaturatedShells where
  twist_acts_trivially_at_magic : ∀ n ∈ MAGIC, …
  -- the conjecture's content as a class field

theorem mass_formula_at_magic [CategoricalNeutralitySaturatedShells]
    (n : ℕ) (hn : n ∈ MAGIC) : … :=
  -- proof using the class instance, fully verified by Lean
```

The narrative side mirrors this:

- Conjecture blocks remain `conjecture`, with explicit
  "axiomatised as a Lean class" status.
- Downstream blocks remain `theorem`/`proposition`, with
  narrative banner: **Theorem (conditional on
  CategoricalNeutralitySaturatedShells).** Body cites the class
  hypothesis explicitly.

The §3b validation rule is **relaxed** to permit this pattern:
provable blocks may transitively touch conjectures *if* every
such conjecture is axiomatised as a Lean class and every
downstream theorem statement carries the class as an explicit
hypothesis.

**Effort.** 2–3 weeks (per-conjecture axiomatisation; downstream
banner updates; validation-rule relaxation).

**Pros.**
- Honest representation: rigorous conditional theorems remain
  theorems; the conjectural inputs are isolated.
- The Lean `class` mechanism makes the conditional structure
  *machine-checkable* — every downstream proof is verified
  modulo the explicit class hypothesis.
- Existing `conj:per-braid-mass-tower` etc. can keep their
  proofs; they just become "proof under the substrate
  axioms" rather than unconditional.
- Aligns with how the algebraic-substrate appendix already
  handles its conjectures (via `conj:hahn-substrate` etc.).

**Cons.**
- Requires per-conjecture Lean axiomatisation (the classes
  must encode enough content to feed downstream proofs).
- ~9 bridge conjectures × 1–3 days each ≈ 2–3 weeks of work.
- Validation-rule relaxation must be carefully scoped to avoid
  letting future ad-hoc conjectures slip through.

**Recommendation.** Adopt — this matches the actual structure
of the framework (rigorous conditional results) and the existing
class-axiomatisation pattern in the algebraic-substrate appendix.

---

## Option C — Per-block conditional reading

**Action.** For each of the 233 provable blocks, audit the proof
body and tag with an explicit `conditional_on:` field listing
the conjectures actually used. Render in the narrative as
"**Proposition (conditional on X, Y).**". Maintain a global
table mapping each provable to its conditional cone.

The `conditional_on:` tag is then validated to match the
transitive `uses[]` cone — preventing silent drift.

**Effort.** 4–6 weeks (per-block review of 233 blocks).

**Pros.**
- Most informative — each block carries explicit conditional
  semantics.
- No global axiomatisation (lighter than Option B).
- Discoverable: a reader of any one theorem sees its
  conditional dependencies.

**Cons.**
- Lots of bookkeeping; vulnerable to drift unless validated.
- Heavier than Option B without proportional gain (the bridge
  conjectures are mostly the same across all 233 blocks).
- Per-block tagging duplicates information already in the
  `uses[]` cone.

**Recommendation.** Reject — too granular. Option B's
class-axiomatisation captures the same content with less
manual bookkeeping.

---

## Summary table

| Criterion | A (strict demote) | **B (substrate-axiom)** | C (per-block) |
|-----------|:-----------------:|:-----------------------:|:-------------:|
| §3b compliance | strict | conditional pattern | per-block tag |
| Narrative impact | massive downgrade | minor (banner notes) | per-block annotation |
| Lean structure | none | class axiomatisation | none |
| Effort | 1–2 days | 2–3 weeks | 4–6 weeks |
| Information preserved | ❌ collapses | ✅ explicit | ✅ explicit (more verbose) |
| Recommended | no | **yes** | no |

---

## Decision required

Pick A, B, or C (or a hybrid) for P3.1 closure. **Recommend B
(substrate-axiom classification)** — preserves the rigorous-
conditional structure, isolates the ~9 bridge conjectures, and
matches the existing class-axiomatisation pattern in the
algebraic-substrate appendix.

If B is selected, next steps:

1. Enumerate the bridge conjectures (audit lists 9 direct,
   may have a few more in their cones).
2. For each, decide on Lean class content (existing
   `prop:vhat-pair-commutation-trace`-style class structure).
3. Update AGENTS.md §3b to permit the conditional-class
   pattern explicitly (currently §3b is unconditional).
4. Codemod downstream theorems to add explicit class
   hypotheses + narrative banners.
