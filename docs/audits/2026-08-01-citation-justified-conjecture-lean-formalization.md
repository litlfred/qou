# Citation-justified conjecture-class Lean formalization — enumeration + status

Bean `qou-pddf` ("citation-justified conjecture classes for eventual Lean
formalization"; owner: *"at some point we need to lean formalize those too —
not all physics papers are fully accurate"*). Branch
`claude/citation-conjecture-lean-formalization-2026-08-01`.

This audits the QOU Lean corpus for propositions/lemmas whose only backing is a
**bibliographic citation to an external result** — a `sorry` + `-- Ref:[key]`
(or an instance-less conjecture class) — and asks, per item, **is the cited
result formalizable in Mathlib today?** Where yes, it is proved sorry-free;
where no, the missing Mathlib infra is recorded.

## Method

`grep`-scan of `content/quantum-observable-universe/lean/QOU/**/*.lean` for
`sorry` bodies with a nearby `-- Ref:[…]`, plus the Prop-valued conjecture
classes. Counts (2026-08-01, off `origin/main`):

- 86 `sorry` bodies carry a `-- Ref:` citation.
- **47** cite `[manuscript]` — QOU-internal open claims, **out of scope** here
  (not "external results in Mathlib"; they are the framework's own open math).
- **39** cite an external work. These split into the classical-math citations
  (symmetric-group / RSK / hyperbolic-volume / computability / LP) triaged
  below.

## Enumeration — external-citation cited sorries

| Decl | File | Cited ref | Mathlib-tractable? | Status |
|---|---|---|---|---|
| `ReebTuringClassical` | `Information/ReebTuringClassical.lean` | `[cardona2021]` | **YES** | **CLOSED** — old encoding was *false*; re-stated + proved sorry-free via `ComputablePred.halting_problem`. |
| `branching_two_one` | `BraidKnot/YoungTableauStandard.lean` | `[sagan2001]` | no | RSK branching rule — no RSK/hook-length in Mathlib. |
| `skew_le_straight` | `BraidKnot/YoungTableauStandard.lean` | `[sagan2001]` | no | Skew SYT / Jacobi–Trudi — not in Mathlib. |
| `sum_dimSYT_eq_involution` | `BraidKnot/YoungTableauStandard.lean` | `[sagan2001]` | no | RSK-for-involutions (`Σ f^λ = I(n)`) — no RSK in Mathlib. |
| `specht_finrank_eq_numSYT` | `BraidKnot/Specht.lean`, `…/SpechtStandardBasisCore.lean` | `[sagan2001]` | no | Specht standard-basis theorem — no Specht modules in Mathlib. |
| `specht_isSimple` | `BraidKnot/Specht.lean` | `[james1984representation]` | no | Specht irreducibility (char 0) — not in Mathlib. |
| `standardPolytabloid_linearIndependent`, `straightening_step_colMax` | `BraidKnot/SpechtStandardBasisCore.lean` | `[sagan2001]` | no | Garnir straightening / triangularity — not in Mathlib. |
| `spechtIso_imp_dom_both` | `BraidKnot/SpechtClassification.lean` | `[james1984representation]` | no | James cross-shape dominance/multiplicity — not in Mathlib. |
| `specht_exhausts_irreducibles` | `BraidKnot/SpechtClassification.lean` | `[sagan2001]` | no | Specht modules exhaust the irreducibles — not in Mathlib. |
| `burnside` | `BraidKnot/DeltaLambdaSignRule.lean` | `[sagan2001]` | no | `Σ (f^λ)² = n!` (RSK / Artin–Wedderburn for `S_n`) — not in Mathlib (finite `n≤5` `decide`-checks present). |
| `numSYT_mul_hookProduct` | `BraidKnot/StandardYoungTableau.lean` | `[sagan2001]` | no | Hook-length formula — not in Mathlib. |
| `seminormalVector_base_exists`, `syt_content_tuple_injective`, `syt_adjacentSwap_connected` | `BraidKnot/JucysMurphy.lean` | `[vershik-kerov1977]`,`[sagan2001]` | partial | Vershik–Kerov seminormal form / GZ-spectrum simplicity — "pure combinatorics" but substantial; not in Mathlib. Candidate for a future hand-formalization. |
| `partitionDom_antisymm` | `BraidKnot/SpechtClassification.lean` | (was `[james1984]`) | — | **already sorry-free** (prior agent; elementary order theory, not James's theorem). Precedent for "elementary-as-formalized despite a deep citation". |
| `hyperbolic-volume independence` (instance) | `Archimedean/HyperbolicVolumeIndependence.lean` | `[zagier1986]` | no | Algebraic independence of Vol(4₁),Vol(5₂),Vol(𝓑₃) over ℚ — **open transcendence** (Borel–Zagier); honestly an instance-less §3b conjecture. |
| `pair_skein_mass_formula` | `HadronicMass/pair_skein_mass_formula.lean` | `[jones1987]` | no | `S_ab` is an `opaque` real; identity is unprovable until the categorical Skein construction gives it a definition. |
| `cauchyMul_order` | `Mathlib/QGevreyOrder.lean` | `[ramis-sauloy-zhang2013]` | no | q-Gevrey Newton-polygon order of a Cauchy product — genuine ε-δ + non-cancellation analysis; not packaged in Mathlib. |
| `knot_operator_selection` | `Archimedean/knot_operator_selection.lean` | `[wenzl1990]` | no | Wenzl Hecke-rep eigenvalue data — not in Mathlib / QOU. |
| `operator_selection_lp`, `lp_dual_stability`, `bare_is_lp_unstable`, `dressed_is_lp_stable`, `confinement_frobenius_reciprocity` | `ParticleInteractions/*` | `[bertsimas1997]`,`[wenzl1990]` | no | LP strong duality + explicit Gram data. The context classes carry the *data* but not the *certificate relations*, so the assertions are not derivable from them (honest cited sorries, not false). LP strong duality is not in Mathlib in usable form. |
| `hecke_baer_star_generic` | `BraidKnot/HeckeBaerStarGeneric/…` | `[kassel1995]` | no (untried) | Hecke Baer-*-involution genericity — algebraic; a future candidate but not attempted this pass. |
| `ConfinementSDP` | `Interactions/ConfinementSDP.lean` | `[boyd-vandenberghe-2004]` | no | SDP strong duality — not in Mathlib. |

## The closed item — `ReebTuringClassical` (a false cited sorry)

The standout finding. The prior encoding

```lean
theorem ReebTuringClassical :
    ∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true := by sorry
```

is **provably false**: `dec : ℕ → Bool` ranges over *all* functions, and
classically `dec n := decide (halts n)` decides every predicate, so
`∃ dec, ∀ n, halts n ↔ dec n = true` holds for every `halts`. The `sorry`
therefore sat on an unsatisfiable proposition — it could never be closed. The
refutation is machine-checked in **pure Lean core** (no Mathlib):

```lean
open Classical in
example : ¬ (∃ halts : ℕ → Prop, ¬ ∃ dec : ℕ → Bool, ∀ n, halts n ↔ dec n = true) := by
  rintro ⟨halts, hne⟩
  exact hne ⟨fun n => decide (halts n), fun n => ⟨decide_eq_true, of_decide_eq_true⟩⟩
```

This is a **scope-(b)** structural refutation of the *encoding*, not of the
cited Cardona–Miranda–Peralta-Salas–Presas theorem, which is genuine. The bug
is the classic one: an undecidability claim must quantify non-decidability over
**computable** deciders, not arbitrary `ℕ → Bool`. Corrected to the honest
computational shadow — a predicate with no computable decision procedure —
discharged **sorry-free** by Mathlib's `ComputablePred.halting_problem` on the
countable (`Denumerable`) `Nat.Partrec.Code`:

```lean
theorem ReebTuringClassical :
    ∃ halts : Nat.Partrec.Code → Prop, ¬ ComputablePred halts :=
  ⟨fun c => (Nat.Partrec.Code.eval c 0).Dom, ComputablePred.halting_problem 0⟩
```

Verified via lean-direct (exit 0, no sorry, no error). This is exactly the
"not all physics papers are fully accurate" case the owner flagged — the *paper*
is fine; the *Lean shadow* was mis-formalised.

## Why the rest are blocked — Mathlib infra gaps

Two dominant missing-infra clusters account for nearly every remaining external
cited sorry:

1. **`S_n` representation theory / RSK (the `BraidKnot/Specht*`, `YoungTableau*`,
   `JucysMurphy`, `DeltaLambdaSignRule` cluster).** Mathlib (as of `v4.24.0`)
   has `YoungDiagram` and semistandard-tableau combinatorics but **no** Specht
   modules, **no** RSK correspondence, **no** hook-length formula, and **no**
   `S_n` irreducible classification. Every `[sagan2001]` / `[james1984]` /
   `[vershik-kerov1977]` sorry bottoms out here. These are correct, well-scoped
   cited sorries (each carries a precise "Missing infra" note); they are the
   Identity-I / P1–P5 program, not low-hanging fruit.

2. **Optimization duality (`ParticleInteractions/*`, `Interactions/ConfinementSDP`).**
   LP/SDP strong duality is not available in Mathlib in a form that discharges
   these. The context classes deliberately carry *only the data* (Gram matrix,
   primal/dual vectors), not the certificate relations, so the assertions are
   genuinely underivable from them — honest cited sorries, **not** false.

Isolated blockers: transcendence (`[zagier1986]`, genuinely open),
q-difference Newton polygons (`[ramis-sauloy-zhang2013]`, real analysis),
opaque-object identities (`[jones1987]`, needs the categorical construction).

## Candidates for a future pass (not attempted here)

- `JucysMurphy.syt_content_tuple_injective` / `syt_adjacentSwap_connected` —
  the docstring calls them "pure combinatorics"; each is a real but
  self-contained proof (SYT reconstruction from content sequence; connectivity
  by admissible adjacent swaps). No Mathlib dependency, so hand-formalizable —
  but each is dozens of lines, deferred.
- `hecke_baer_star_generic` (`[kassel1995]`) — algebraic Baer-* genericity;
  worth a targeted attempt.

## Verification environment note

Machine verification used lean-direct (`lean <file>`, never `lake build`) per
AGENTS.md. The shared Mathlib olean cache was mid-eviction/rebuild by sibling
agents (6990 → ~1200 oleans); the `Mathlib.Computability.Halting` cone (13
modules: Primrec → Partrec → PartrecCode → Halting + Encodable/Denumerable
deps) was **not** in the restored cache and was built from source into the
shared tree (~1 min) to verify the corrected `ReebTuringClassical`. Both the
pure-core refutation and the corrected proof compiled exit-0, sorry-free.
