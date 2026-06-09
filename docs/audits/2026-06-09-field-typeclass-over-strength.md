# Field-typeclass over-strength audit (`[Field]` where a weaker class suffices)

**Tool:** [`folio-assistant/computations/audits/field_typeclass_audit.py`](../../folio-assistant/computations/audits/field_typeclass_audit.py)
**Witness:** [`folio-assistant/computations/audits/field-typeclass-audit.witness.json`](../../folio-assistant/computations/audits/field-typeclass-audit.witness.json)
**Origin:** surfaced 2026-06-09 — `QuantumUniverse` carries a phantom `[Field k]`
that never divides (the substrate ground ring is a *commutative ring* `R`, per
the §7c base-ring convention), which blocked the `[Linear R C]` lift (PR #2065).
Owner directed: make a QA audit for over-strong field constraints, then fix them.

## What it checks

For every QOU-lib declaration constraining a type var with a field-strength
class — `[Field V]`, `[LinearOrderedField V]`, `[DivisionRing V]` — classify:

| class | meaning | action |
|-------|---------|--------|
| `phantom` | `V` unused outside the binder | relax to the weakest class |
| `over-strong` | `V` used, but no division/inverse/field-requiring construct found | `CommRing V` likely suffices — **relax + build-check** |
| `genuine` | uses `⁻¹` / `/` / `field_simp` / `finrank` / `Basis` / Wedderburn / semisimplicity | keep `Field` |

Comments, strings, URLs, and paths are stripped before operator scanning, so
prose `/` and `http://` do not produce false `genuine` hits.  The `genuine`
class also catches **field-requiring constructs** (`finrank`, `FiniteDimensional`,
`Module.Free`, `Basis`, `Wedderburn`, `*semisimple*`, `LinearIndependent`) that
need field strength without a literal division — the representation-theory core
(Hoefsmit, Markov-trace, Wedderburn) legitimately stays over a field.

## Result (2026-06-09 baseline)

102 field-strength binders → **0 phantom, 64 over-strong, 38 genuine**.

> **`over-strong` is a warn-level signal, not a proof.** The heuristic is
> syntactic; some `over-strong` findings may still need `Field` via a Mathlib
> lemma the regex does not see (instance resolution, a transitively-field-only
> rewrite). **Every relaxation must be confirmed by a module build** before it
> lands. Conversely a `genuine` finding is high-confidence (a field op is
> textually present).

Top files by `over-strong` count: `DerivedCharacterCatalogue` (18),
`GradedTraceResidueSplit` (8), `StructuralRank` (7), `MarkovAxiomsPrimitive` (6),
`Hoefsmit` (6), `IwahoriHeckeAPI` (4) — see the witness JSON for the full
per-declaration list.

## Refinement (2026-06-09): three kinds of `[Field]` use

Build-testing the burn-down showed the `over-strong`/`genuine` split is too
coarse. A `[Field V]` use falls into **three** kinds:

1. **Division-free** — `V` carries no `/` or `⁻¹` anywhere in the module.
   Relax to `[CommRing V]` directly. *(Fixed this pass: `ClassicalLimitObstruction`
   structure, `GradedTraceResidueSplit` ×8, `HoefsmitV21CosSymmetrization`,
   and `QCltNonCommutative` / `TraceLocalityMeetsGsNonLocality` → `LinearOrderedCommRing`.)*
2. **`q`-power inverse (Laurent-reframable)** — the only "division" is `1/q^k`
   i.e. `q⁻ᵏ`, the inverse of the **unit** `q`. This needs **no field**: work
   over `ℤ[q, q⁻¹]` (`abbrev R_q := LaurentPolynomial ℤ`, already in the
   Laplace/Fourier blocks) where `q⁻¹` is a Laurent unit, **or** keep
   `[CommRing R]` + a unit witness `(qinv : R) (q * qinv = 1)` and rewrite
   `1/q^k ↦ qinv^k`. Fraction *identities* clear of denominators (multiply
   through by `q^N` ⟹ a polynomial identity provable by `ring`, dropping the
   `field_simp`). *(Owner direction 2026-06-09. Example target:
   `BorromeanChiPerRep`, `DerivedCharacterCatalogue` Laurent characters.)*
3. **Non-unit division (truly field)** — division by something that is **not**
   a unit of `ℤ[q,q⁻¹]`, e.g. Hoefsmit's seminormal `α_T = (q^c − q^{−c}) /
   ([2]_q · c)` divides by `[2]_q = q + q⁻¹` (not invertible in the Laurent
   ring) and by content differences `c`. These genuinely need a field — the
   **fraction field** `Frac(R)` of the (domain) ground ring, *kept generic*:
   a bare `[Field R]` already **is** the cleanest stand-in for
   `Frac(of-the-Laurent-ring)`, so no change is needed (do **not** specialize
   to a concrete `ℚ(q)`). If the Laurent embedding should be explicit, name it
   `[Field K] [Algebra (LaurentPolynomial ℤ) K]` / `FractionRing` rather than
   hardcoding `ℚ(q)`.

The checker's module-level `genuine` (division/inverse anywhere ⟹ field-by-design)
is the **conservative** lower bound — it keeps kinds 2 and 3 as `Field`. The
kind-2 → CommRing reframe is a per-module *proof* refactor (rewrite formulas +
re-prove the cleared-denominator identity), tracked separately from the
mechanical kind-1 relaxations.

## Fixing discipline (the "fix all k-like issues" campaign)

Each relaxation is **`[Field V]` → `[CommRing V]`** (or the weakest class that
still typechecks), confirmed by `lake build QOU.<Module>` green. Two structural
notes:

- **Base-struct relaxations cascade.** `QuantumUniverse` / `QuantumObservableUniverse`
  (`CategoricalFoundations.lean`) carry `[Field k]`; relaxing them to
  `[CommRing R]` re-threads every consumer (~74 files) and is the scope of
  PR #2065 — not a leaf fix.
- **Leaf relaxations are local.** A self-contained `theorem`/`def`/`class`
  with an over-strong `[Field V]` relaxes in place; verify the owning module
  builds, then move on.

Run `python3 folio-assistant/computations/audits/field_typeclass_audit.py`
(add `--strict` for a CI gate) to refresh the witness after each batch; the
`over-strong` count is the burn-down metric.
