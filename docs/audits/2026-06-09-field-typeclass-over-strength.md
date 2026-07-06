# Field-typeclass over-strength audit (`[Field]` where a weaker class suffices)

**Tool:** [`computations/audits/field_typeclass_audit.py`](../../computations/audits/field_typeclass_audit.py)
**Witness:** [`computations/audits/field-typeclass-audit.witness.json`](../../computations/audits/field-typeclass-audit.witness.json)
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

## Result

Initial baseline (2026-06-09, before any relaxation or the subtype-safe regex
fix): 102 field-strength binders → 0 phantom, 64 over-strong, 38 genuine.

**The committed witness JSON is the live source of truth** (`counts` field) —
it is regenerated from the current checkout, so the per-class numbers move as
binders are relaxed and as the heuristic is refined (the subtype-safe `//`
guard from the Gemini review re-surfaced 2 findings the old regex hid). Do not
cite a frozen number from this prose; read `field-typeclass-audit.witness.json`.

### Burn-down completion (2026-06-09, PR #2072)

**0 phantom / 0 over-strong / 74 genuine.** Every remaining field-strength
binder is either (a) syntactically field-using, or (b) a **build-verified
exception** recorded in `field-typeclass-audit.exceptions.json` (the audit
reclassifies those as genuine with the recorded reason). Relaxations landed
and `lake build`-verified green:

| Module | Relaxed |
|--------|---------|
| `SurrealRateCalculus` (merged #2066) | 3 → `CommRing` |
| `ClassicalLimitObstruction` (structure) | 1 → `CommRing` |
| `GradedTraceResidueSplit` | 8 → `CommRing` |
| `GradedMarkovTraceFromGSFiltration` | 2 → `CommRing` |
| `MathlibExt/SDP` | 2 → `CommRing` |
| `MathlibExt/QPlancherel` (class; section `variable` stays `Field` for `dq²/Z`) | 1 → `CommRing` |
| `DerivedCharacterCatalogue` (class + division-free named chis; 5 dividing-witness instances stay `Field`) | 11 → `CommRing` |

Exception classes (see the exceptions JSON for per-decl reasons): ordering
without `LinearOrderedCommRing` in the pinned Mathlib (QClt, TraceLocality);
**transitive** non-unit division (`MarkovTraceAxioms` via `markovZax u =
u/(u²+1)` — a dependence the syntactic per-decl scan cannot see); and four
**pre-existing-broken modules** that never compiled (`HeckeAlgebra` 100+
errors, the `IwahoriHecke` chain with deep `Ideal.Quotient` API bitrot,
`HoefsmitV21CosSymmetrization` proof bitrot) where relaxations are
unverifiable until the modules are repaired (own PR; parse-level repairs —
import placement, renamed-module imports, a dead import, a universe
annotation — landed on this PR as strict improvements).

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

1. **Division-free** — the declaration carries no `/` or `⁻¹`. Relax to
   `[CommRing V]` directly. **The witness JSON is the source of truth for what
   is fixed**; do not trust prose. As of this branch: `SurrealRateCalculus`
   (merged #2066), `ClassicalLimitObstruction` structure, and
   `GradedTraceResidueSplit` ×8 are relaxed + `lake build`-verified.
   *(`QCltNonCommutative` / `TraceLocalityMeetsGsNonLocality` were attempted as
   `LinearOrderedCommRing` and reverted — that class is unavailable in the
   pinned Mathlib; they use ordering and stay `LinearOrderedField`.
   `HoefsmitV21CosSymmetrization` reverted — a downstream `unfold` failure.)*
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

**The checker classifies per declaration** (division/inverse/field-lemma/
field-requiring token *in that decl's own signature+body*) — it does **not**
do a module-level "field anywhere ⟹ genuine" sweep (an earlier attempt at that
mis-read `import Mathlib.Algebra.Field.Basic` as field use and produced a
misleadingly-empty burn-down; removed per Gemini/Copilot review on #2072). So
an `over-strong` finding is a **per-decl candidate**: confirm the decl (and its
module) really is division-free before relaxing — a kind-2 (Laurent) or kind-3
(non-unit) module will have *other* decls flagged `genuine`, and relaxing the
flagged signature there is a per-module *proof* refactor (rewrite formulas +
re-prove the cleared-denominator identity), not a mechanical swap.

### kind-2 reframe status (2026-06-09)

The kind-2 (q-power Laurent) reframe — provide a **division-free `…_unit (q : Rˣ)`
companion over `[CommRing R]`** bridged to a polynomial in `h = ↑q − ↑q⁻¹`, then
witness it over the non-field `LaurentPolynomial ℤ` — is **done** for the two
character modules:

- `BorromeanChiPerRep` (`chi21_borromean_qform_unit` + `…_eq_poly` + `TUnit`
  witness) — merged on `main`.
- `DerivedCharacterCatalogue` (PR #2075): `hopfOneOneDiquarkChiUnit` /
  `trefoilOneOneElectronChiUnit` / `cinquefoilOneOneMuonChiUnit` (sign-rep
  monomials), `borromeanTwoOneBaryonChiUnit` (= `chi21_borromean(↑q²−↑q⁻²)`),
  `figureEightTwoOneHiggsChiUnit` (= `h⁴+2h²−1`), with bar-invariance + Laurent
  witnesses. `linear_combination` certificates are machine-derived (sympy,
  remainder 0). The `[Field]` `IsRMatrixDerived` instances stay as the
  archimedean layer (`storedChi : R → R` cannot host `q⁻¹`), so this is purely
  additive.

Only **kind-3 non-unit division** (Hoefsmit `/[2]_q`, `markovZax = u/(u²+1)`)
genuinely needs `Field` / `Frac(R)` and remains in the exceptions ledger.

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

Run `python3 computations/audits/field_typeclass_audit.py`
(add `--strict` for a CI gate) to refresh the witness after each batch; the
`over-strong` count is the burn-down metric.
