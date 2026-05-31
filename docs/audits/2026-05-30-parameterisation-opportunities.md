# Parameterisation opportunities — codebase audit (2026-05-30)

Triggered by the user's observation on PR #1537: "the SDP-to-Lean pattern works for nucleotides — can we generalize this?" Yes — and the same generalisation principle applies to **several** other duplicated proof patterns across the codebase.

This audit identifies 5 parameterisation opportunities ranked by LOC-saved + downstream-value.

## Opportunity 1 — `AtomicMass.lean` per-element deviation theorems (HIGH)

**File**: [`content/quantum-observable-universe/lean/QOU/AtomicMass.lean`](../../content/quantum-observable-universe/lean/QOU/AtomicMass.lean) (3354 LOC, 119 declarations).

**Pattern**: 60+ `deviation_X` theorems for individual elements (H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, ..., Zr and beyond), each at ~27 LOC apart, each with the identical proof structure:

```lean
theorem deviation_X :
    |X.codataMass - X.ameMass| < <bound> := by
  unfold ElementDatum.codataMass ElementDatum.ameMass X
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_<X-tag>
  norm_num
```

What's element-specific: the element's `ElementDatum` (Z, N, BperA) and the numerical bound. The proof STRUCTURE is identical.

**Generalisation**:

```lean
-- In a generic ElementDeviation module
theorem element_deviation
    (e : ElementDatum) (bound : ℝ) (h_bound : <numerical condition>) :
    |e.codataMass - e.ameMass| < bound := by
  unfold ElementDatum.codataMass ElementDatum.ameMass
  norm_num [h_bound]   -- or similar generic close

-- Per-element files become ~3-line abbrevs:
abbrev deviation_h := @element_deviation h 0.0001 (by norm_num)
```

**LOC savings**: ~70 elements × ~7 LOC each (proof body) = ~490 LOC removed, replaced with ~60 × 1-line `abbrev`s + ~50 LOC generic = net ~380 LOC saved.

**Caveat**: each element's bound is element-specific (some use 0.0001, others 0.0002, depending on which CODATA derivation chain is invoked). The generic version needs to accept the bound as a parameter.

**Difficulty**: medium. Each element's specific `ame_delta_<X-tag>` reference might need a per-element side hypothesis. But the dominant body is mechanical.

## Opportunity 2 — `Conjectures.lean` per-conjecture class scaffolds (MEDIUM)

**File**: [`content/quantum-observable-universe/lean/QOU/AppendixSurreals/Conjectures.lean`](../../content/quantum-observable-universe/lean/QOU/AppendixSurreals/Conjectures.lean) (1244 LOC).

**Pattern**: many conjecture entries follow the §3b-cond pattern:

```lean
opaque <ConjectureName>Holds : Prop
class <ConjectureName> : Prop where
  holds : <ConjectureName>Holds
instance : <ConjectureName> where
  holds := sorry   -- the conjecture IS the sorry
```

**Generalisation**: a single `ConjectureClass` macro/typeclass that generates the opaque Prop + class + sorry instance from a name. Possibly Lean 4 macros or commands.

**LOC savings**: marginal per conjecture (~5-10 LOC each); aggregate ~100+ LOC across the file.

**Difficulty**: high — requires Lean 4 macros, which is a deeper investment than `abbrev`-based parameterisation.

## Opportunity 3 — `SDPRankEquality.lean` axiom + specialisation pattern (LOW, already good)

**File**: [`content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean) (781 LOC).

**Pattern**: already follows good practice — abstract axioms + structural specialisations (`_of_dualSlack_posDef`, `_of_active_empty_and_cost_posDef`). No further parameterisation needed.

**LOC savings**: ~0. This file is the model for what other files should look like.

## Opportunity 4 — Per-knot Hecke-character closed forms (MEDIUM)

**Pattern across `lean/QOU/BraidKnot/`**: many files have per-knot character closed forms (T(2,3), T(2,5), T(2,7), T(3,5), Whitehead, etc.) where the proof shapes are similar.

**Generalisation**: per-knot-family generic versions parameterised on the knot's (p, q) torus parameters or Conway notation. Examples:

```lean
-- Per-torus-knot generic
theorem torus_knot_character_closed_form
    (p q : ℕ) (hpq : Nat.Coprime p q) :
    χ_(p,q)(σ) = <closed form depending on p, q> := ...

-- Specialise:
abbrev T29_character := @torus_knot_character_closed_form 2 9 (by norm_num)
abbrev T35_character := @torus_knot_character_closed_form 3 5 (by norm_num)
```

**LOC savings**: ~50-100 LOC across the BraidKnot directory.

**Difficulty**: medium-high — the closed forms genuinely depend on (p, q) in non-trivial ways; the generic version may need case splits.

## Opportunity 5 — Per-nucleus mass-formula assembly (HIGH if real-SDP wiring lands)

**Pattern (future)**: when the "real" per-nucleus SDP wiring lands (multi-term cost + non-empty constraints from the mass formula), each nucleus will have its own `<nucleus>_realSDP` with mass-formula-derived cost function. If the mass formula has a uniform structure per nucleus (which it does — see `mass-formula-6term-mpfr-50dps.witness.json`), the parameterisation pattern from #1537 extends naturally.

**Generalisation**:

```lean
-- Parameterised real SDP
def nucleusRealSDP (datum : NucleusDatum) : SDPPrimal ... where
  cost := mass_formula_cost datum
  constraint := ...
  rhs := ...

-- Per-nucleus:
abbrev deuteron_realSDP := nucleusRealSDP deuteronDatum
abbrev tritium_realSDP := nucleusRealSDP tritiumDatum
```

**LOC savings**: not yet realised (the real SDP wiring isn't on main); but pre-design for the parameterised version would save ~7 nuclei × ~100 LOC = ~700 LOC when the wiring lands.

**Difficulty**: pre-design (low), then implementation tracks the mass-formula sprint.

## Recommended ordering

1. **Land #1537 first** (current PR, parameterised empty-SDP for 10 nuclei) — proves the pattern works at production scale.
2. **AtomicMass.lean refactor** (Opportunity 1) — highest LOC savings, mechanical, immediate value. Could be 1-2 PRs.
3. **Pre-design Opportunity 5** during the Phase 2 IwahoriHecke sprint — coordinate with the real-SDP wiring so the parameterisation lands together with the per-nucleus theorems, not as a refactor afterwards.
4. **Opportunity 4** — when the per-torus-knot character closed forms are next touched.
5. **Opportunity 2** — Lean-macro-based; do later when there's macro expertise on the team.

## Anti-pattern observed: per-instance docstrings on every `abbrev`

PR #1537's per-nucleus files have docstrings on each `abbrev`, which inflates LOC. The trade-off: more LOC vs. better reader-friendliness (each `abbrev` shows up in `#print` with its context). Default to including docstrings; if LOC pressure becomes severe, a follow-up PR can strip them to just module-level docstrings.

## Coordination

- This audit captures the principle from PR #1537. The 4 prioritised opportunities are independent work tracks; no inter-PR dependencies.
- Phase 2 IwahoriHecke sprint (active, sibling commits `sprint2-iwahori` / `sprint3-4-iwahori` / `sprint5-iwahori`) should be aware of Opportunity 5 — coordinate via a heads-up comment on the most recent active Iwahori PR.
