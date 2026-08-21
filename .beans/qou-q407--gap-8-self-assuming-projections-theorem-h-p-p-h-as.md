---
# qou-q407
title: 'GAP: 8 self-assuming projections — ''theorem (h : P) : P := h'' asserts nothing'
status: in-progress
type: task
priority: high
tags:
    - lean
created_at: 2026-08-07T18:24:34Z
updated_at: 2026-08-21T15:23:31Z
---

Eight provable declarations have the shape 'theorem name ... (h : P) : P := h' — hypothesis identical to conclusion, proof term the identity. They assert nothing about the objects named, and stay true if every definition is swapped.

Found via the folio-assistant triviality probe (6/40 closed; 2 genuine, 4 legit decide/simp), then swept statically by scripts/lean-self-assuming-audit.py (2590 files, 4.5 s). Full analysis + quoted bodies: docs/audits/2026-08-07-self-assuming-projection-sweep.md

Findings (lines on main @ b48ce882fa):
1. defect_legendrian_knot — brings-surface/defect-legendrian-knot.lean:47
2. topological_charge_quantization — brings-surface/topological-charge-quantization.lean:43
3. fomin_identity — lean/QOU/Archimedean/BranchingConvergence.lean:138
4. fomin_identity_n3 — lean/QOU/Archimedean/BranchingConvergence.lean:152
5. length_bound_necessary — lean/QOU/BraidKnot/PSDFeasibilityProxy.lean:94
6. universal_ilp_selects_minimum — nuclear-interactions/universal-ilp-algorithm.lean:43
7. variational_transport — quantum-observable-universes/categorical-action.lean:109
8. ordering_extends — unital-groebner-bases/lean/UGB/GrobnerShirshov/JetOrder.lean:213

Why no existing gate caught them: no sorry, no axiom, no True conclusion, type-checks clean. AGENTS.md 3b-cond item 5 names the pattern; there was no detector.

NOT fixed in the detector PR — rewriting a theorem statement changes what the corpus claims. Per 1a the honest dispositions are prove / state-with-sorry+Ref / demote-to-conjecture, chosen per declaration. fomin_identity needs real SYT definitions rather than its uninterpreted dim_fn/mult_fn parameters.

Scope-(a): the Lean carries no content. NOT a claim the underlying math is wrong — Fomin's identity is a true theorem of the literature.

Follow-ups: wire as a proof-self-assuming criterion in content/pipeline/lean-vacuity-axiom-audit.ts; run the triviality probe corpus-wide to reach the ':= by exact h' variants the static pass cannot see.



## Re-verified 2026-08-19 (current main @ 5b158ef0)
Re-ran scripts/lean-self-assuming-audit.py: **all 8 still live** — none fixed in the 5-week gap. Same 8 decls, same lines (defect_legendrian_knot, topological_charge_quantization, fomin_identity, fomin_identity_n3, length_bound_necessary, universal_ilp_selects_minimum, variational_transport, ordering_extends). Ready to work; still the most concrete item in the vacuity arc.

---

## 2026-08-21 — the count was wrong, and one is now proved

### The detector under-reported by a third: 12, not 8

`scripts/lean-self-assuming-audit.py` parsed explicit binders with a regex
whose type alternation admitted only **one** level of parentheses. Any
hypothesis nesting two deep was unparseable, so the binder was dropped and the
declaration could never be reported — **silently**: a declaration it could not
parse and one it parsed and found clean produced identical output. The bias ran
against exactly the elaborate statements most likely to hide a tautology.

Fixed with balanced-delimiter scanning (`parse_binders`, no depth limit, also
reads `{..}` / `⦃..⦄` / `[..]`). Corrected sweep over 3008 files (the original
saw 2590) finds **five more**:

- `structurallyValidBinding_necessary` — `QOU/BraidKnot/PSDFeasibilityProxy.lean:103`
- `jet_preserves_channel_separation` — `QOU/ChannelSeparation.lean:162`
- `adjoint_has_no_degree_zero` — `QOU/GradedFrobeniusHopf.lean:116`
- `plancherel_total_bound` — `mass-theory/plancherel-term-7-formulation.lean:61`
- `plancherel_sum_eq_one` — `mass-theory/plancherel-term-7-formulation.lean:71`

`structurallyValidBinding_necessary` sits **nine lines below**
`length_bound_necessary`, which the original sweep *did* report. It differs
only by having a more complicated hypothesis.

### `universal_ilp_selects_minimum` — proved (§1a "prove it")

The docstring already named a genuine claim: "The LP selects the
minimum-crossing feasible knot operator." That is an **attainment** statement,
and `crossing_number : ℕ` makes it provable by well-ordering. Restated and
proved sorry-free; the file compiles clean.

```lean
theorem universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    (K₀ : KnotOperator q) (hK₀ : universal_ilp q state K₀) :
    ∃ K, universal_ilp q state K ∧
      ∀ K', universal_ilp q state K' → K.crossing_number ≤ K'.crossing_number
```

The pattern generalises: **read the docstring first.** Where the prose names a
real claim, the disposition is usually "prove it" and the statement to prove is
already written down in English.

### Dispositions for the remaining 11 — analysis, not yet applied

Grouped by what the honest disposition turns on. Several need an owner ruling
because rewriting a statement changes what the corpus claims.

**(A) No definitions exist to state the claim — needs `sorry`+Ref or demotion.**
`defect_legendrian_knot`, `topological_charge_quantization`,
`variational_transport`, `jet_preserves_channel_separation`,
`adjoint_has_no_degree_zero`. All quantify over an *arbitrary* category with
uninterpreted morphisms. In `defect_legendrian_knot`, `zero : A ⟶ A` is a free
variable merely *named* "zero" — not the zero morphism. Nothing about contact
forms, Reeb residues or Legendrian knots is expressible until the substrate
structures exist. Note `PSDFeasibilityProxy.lean` already uses `axiom` + `Ref`
for exactly this situation, so the file-local idiom is established.

**(B) True by definition — the "theorem" records a convention.**
`length_bound_necessary`, `structurallyValidBinding_necessary`. The docstring
of the first concedes it: "Any candidate violating this bound is excluded from
the search **by hypothesis**." These are not results; naming the enumerator's
search space as a `def` and stating necessity against *that* would at least
make them about something, but adding a definition solely to dignify a
tautology may be worse than deleting. **Owner call.**

**(C) Honest in prose, vacuous in Lean.**
`plancherel_total_bound`, `plancherel_sum_eq_one`. Docstrings already say
"a parametric restatement, not a proof". Lower stakes, but a `**Theorem**`
docstring over `theorem X (h : P) : P := h` is what §3b-cond item 5 forbids
regardless of what the prose concedes.

**(D) Needs real combinatorics.** `fomin_identity`, `fomin_identity_n3`.
As the original audit says: `dim_fn` / `mult_fn` are uninterpreted parameters.
Genuine proof needs real SYT definitions; `sorry`+Ref is the honest interim.

**(E) Vacuous by choice of representation.** `ordering_extends`. Its docstring
claims "the substantive content is that the embedding is order-preserving" —
but **there is no embedding**: the module models monomials as bare `List ℕ` at
every level, and `degLexNat` never mentions an alphabet bound. Nothing can be
proved because nothing is being mapped. A substantive statement *is* available
in this representation — a fully-descended word is deg-lex below a fully
transient one of the same length, which is what would justify processing
descended parts first — but that is a different theorem from the one claimed.
**Owner call.**

### Adjacent, out of scope, worth separate beans

- `phi_k_finite` (`plancherel-term-7-formulation.lean:78`):
  `∃ x : ℝ, phi_k k blocks = x := ⟨phi_k k blocks, rfl⟩`. Vacuous — every term
  equals itself; "well-defined" is not a theorem in a total type theory. A
  *different* vacuity shape the detector cannot see, since the proof is not a
  bare identifier. Matches the original audit's own follow-up about
  `:= by exact h` variants.
- `KnotOperator.is_knot : Prop` is an opaque `Prop` field — the §3b-cond
  "projected opaque Prop" pattern, in the same file as the ILP fix.
- `gram_matrix _q = 0` in `universal-ilp-algorithm.lean` makes
  `frobenius_positive` vacuously true. Disclosed in its docstring, so not
  hidden, but it means the newly proved attainment theorem ranges over a
  feasible set whose Frobenius constraint constrains nothing.

## Next

- [x] Fix the detector's binder parsing; re-sweep corpus-wide
- [x] `universal_ilp_selects_minimum` — proved
- [ ] Owner ruling on groups (B) and (E), where the honest fix changes what the
      corpus claims
- [ ] Apply (A), (C), (D) dispositions once (B)/(E) are settled, so the whole
      set lands as one reviewable change
- [ ] Extend the detector to the `:= by exact h` and `⟨x, rfl⟩` shapes
