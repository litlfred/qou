# Is the "archimedean functor" really a functor? — functor-claim taxonomy audit

**Date:** 2026-07-11
**Branch:** `claude/archimedian-functor-analysis-o2ca00`
**Question (owner):** *"Look at the archimedean functor. Is it really a
functor? To/from what category? There are a few other functors that are
claimed. Analyze and resolve issues."*

## TL;DR

- **No — the object(s) called "the archimedean functor" are not functors.**
  Every candidate for that name reduces to a **real-valued map or a ring
  homomorphism**, carrying *no action on morphisms* and *no functor laws*:
  - `R_top` ("archimedean realization functor"): a map **out of the
    Grothendieck ring** `K₀(Var)` — i.e. a *motivic measure / ring
    homomorphism* (`χ_top` is literally a ring hom; `π_∞` is a place).
    Decategorified; there are no morphisms to act on.
  - `τ_arch = π_∞ ∘ τ`: Lean-typed as `τ_arch : ℝ → ℝ`. The **archimedean
    evaluation/component** of the fibre functor — a functor *followed by an
    evaluation into a set*, not itself a functor.
  - `𝓕_Arch` / "standard-part functor": Lean-typed as
    `standardPartRingHom : finiteSubring →+* ℝ`, whose own docstring says
    "**surjective ring homomorphism**."
- **The genuine functor in this story is the fibre functor τ**
  (Tannakian). It *is* a real `CategoryTheory.Functor` in
  `CategoricalFoundations` (`fibreFunctor : C ⥤ Type*`), in
  `spatial-realization-functor.lean` (`fibreFunctor : C ⥤ D`), and the
  classical-limit functor is a genuine `MonoidalFunctor`. But **τ's
  codomain is stated five incompatible ways** across the corpus
  (`Type*` / `Vec_ℝ` / `Arch` / `D` / `ℝ`), and it is even once called the
  "forgetful functor."
- **The target category `Arch` is asserted but never constructed as a
  category** — its only formal encoding (`ArchimedeanCategory`) is
  `{ Obj : Type*, archProj : Obj → ℝ }`: objects and a real evaluation, but
  **no Hom, no composition, no identities**.
- **The paper's own notation register already states the correct
  taxonomy** (`notation/notation-collisions.md` §"Archimedean / fibre /
  forgetful functors"): τ : **C → Arch** is the fibre functor; U : **Arch →
  Vec_ℝ** the forgetful functor; the "archimedean realization" `R ↦ ℝ` is
  "**not** a functor between QOU categories"; and "**Arch** is the target of
  τ, not the name of a functor … we never write 'the archimedean functor'
  without context." **The issues below are violations of this existing
  register, plus Lean encodings that do not match it.**

## What a "functor" requires (the yardstick)

A `CategoryTheory.Functor F : 𝐀 ⥤ 𝐁` needs: (i) source and target
**categories** (objects *and* morphisms, with composition + identities);
(ii) an object map `F.obj`; (iii) a **morphism map**
`F.map : (X ⟶ Y) → (F.obj X ⟶ F.obj Y)`; (iv) the **functor laws**
`F.map (𝟙 X) = 𝟙 (F.obj X)` and `F.map (g ∘ f) = F.map g ∘ F.map f`.

A map whose *codomain is a set/ring* (`… → ℝ`, `… → K_0(Var)`) is at best a
functor into a one-object/discrete category — i.e. not what "functor" is
meant to convey here. Such maps are **ring homomorphisms**, **motivic
measures**, **traces**, or **linear functionals** — all standard, correct
notions, just not *functors*.

## Catalog of every "functor" claim

Legend — **Yes** = genuine `CategoryTheory.Functor` (or `MonoidalFunctor`);
**No** = object/ring/set map with no morphism action; **Partial** = bundles a
genuine functor field but the named thing is not itself the functor.

| # | Name (label) | Claimed src → tgt | Actual Lean type | Functor? |
|---|---|---|---|---|
| 1 | **Fibre functor τ** (`rem:fibre-functor-rigidity`, `def:fibre-functor-atlas`) | inconsistent: **C** → `Type*`/`Vec_ℝ`/`Arch`/`D`/`ℝ`; once "forgetful" | genuine `C ⥤ Type*` in `CategoricalFoundations`; genuine `C ⥤ D` field in `spatial-realization`; **but** `MotivesArchimedean.FibreFunctor` = `obj : C → Arch.Obj` (object map only) | **Yes** (in 2 files) / **No** (in `MotivesArchimedean`) |
| 2 | **Archimedean realization functor R_top** (`def:archimedean-realization-functor`) | `M̂` (Grothendieck-ring completion) → **ℝ** | `structure ArchimedeanRealizationFunctor` = `{ Motive, eulerChar : Motive→Int, archPostProc : ℝ→ℝ, realize : Motive→ℝ }` | **No** — motivic measure / ring hom into ℝ |
| 3 | **Standard-part functor St / 𝓕_Arch** (`def:standard-part-functor`; `archimedean-functor-trace-commutativity.md`) | prose: `C_fin → C_ℝ`; realized as **ℝ-valued** | `standardPartRingHom : finiteSubring →+* ℝ` ("surjective ring homomorphism"); sibling theorem is `subst; rfl` | **No** — ring homomorphism |
| 4 | **Spatial realization functor** (`def:spatial-realization-functor`) | `A ↦ Spec(A) = M` (contact manifold) | `structure SpatialRealizationFunctor` bundling data **plus** genuine `fibreFunctor : C ⥤ D` | **Partial** — carries a real `C ⥤ D`; "spatial realization" itself is `Spec` + data |
| 5 | **Observation Frame / Markov trace τ** (`frobenius-self-duality-…`) | `Obs_τ(a) = τ(a·−)` on `H_n` | `def Obs (a:A) : A → R := fun b => F.τ (a*b)` | **No** — trace / linear functional |
| 6 | **Classical-limit functor L** (`def:classical-limit-functor`) | `C_q → C_1` | `structure` carrying `functor : MonoidalFunctor Cq C1` | **Yes** (genuine monoidal functor) |
| 7 | **CMB functor** (`cmb-functor`) | Aeon 𝒜 → Mod_R | `CMB : Aeon → M` | **No** — plain map to a module |
| 8 | **Horizon functor ∂** (`horizon-functor`) | π₀(Bun°) → 𝒫(…) | `boundary : Aeon → Set Config` | **No** — set-valued map |
| 9 | **Flavor-dressing functor** (`def:flavor-dressing-functor`) | flavors → ℝ | `class` with `μ : Flavor → ℝ` | **No** — plain real map |
| 10 | **q-GL fibre functor** (`conj:q-gl-fiber-functor`) | into Rep(Ǧ_q) | conjectural `class` (sorry instance); reuses τ | **No** (conjectural class, not a functor def) |
| 11 | **Casimir mode-count functor** (`conj:casimir-epsilon-vacuum` Stage C) | iso-classes → surreal counts | `class` with `modeCountDiff : ℝ → ℝ → ℝ` | **No** — 2-arg real map; functorial lift explicitly open |

### The two categories

| Object | Encoding | A genuine category? |
|---|---|---|
| **C** (substrate rigid monoidal cat) | Mathlib `[Category C] [MonoidalCategory C] [BraidedCategory C]` throughout | **Yes** (via Mathlib typeclasses) |
| **Arch** (target of τ) | `structure ArchimedeanCategory where Obj : Type*; archProj : Obj → ℝ` | **No** — no Hom/composition/identities |

## Diagnosis

1. **Level confusion (functor vs. ring hom / motivic measure).** `R_top`
   is defined *out of the Grothendieck ring* `K₀(Var)`. Passing to `K_0`
   **decategorifies** — morphisms are gone, so "functor" no longer applies;
   the Euler-characteristic realization out of `K₀(Var)` is the textbook
   **motivic measure** (a ring homomorphism; Denef–Loeser). A realization
   *functor* proper lives one level up, on the category of motives `DM(k)`
   (which has morphisms). As written, `R_top` is a ring hom, not a functor.

2. **"Functor into ℝ."** `τ_arch : ℝ → ℝ` and `st : … → ℝ` land in a
   *set/ring*. These are the **archimedean evaluation** (`π_∞`, a place)
   and the **standard-part ring homomorphism** (Robinson). The Lean is
   already honest for the standard part (`…→+* ℝ`); only the *prose* calls
   them functors.

3. **τ's codomain is not pinned.** `Type*` (CategoricalFoundations),
   `Vec_ℝ` (tau-notation, markov-trace), `Arch` (register,
   archimedean-realization, vol-through-tau), `D` (spatial-realization),
   `ℝ` (uniqueness), and "forgetful functor" (quantum-observable-universe).
   The register's intended reading — τ : C → **Arch**, then U : Arch →
   Vec_ℝ, then the evaluation π_∞ : Arch → ℝ (**not** a functor) — is
   correct and should be made the single convention.

4. **`Arch` is never built as a category**, so "τ : C → Arch" cannot
   literally typecheck as a functor even where τ is otherwise genuine.

## Recommended resolution (tiered)

**T1 — enforce the existing register (mechanical). ✅ APPLIED.**
`mass-theory/archimedean-image-table.md` opened with "The **archimedean
functor** τ : C → Arch"; corrected to "The **fibre functor** τ … followed
by the archimedean evaluation π_∞" (the register forbids "the archimedean
functor"; τ *is* the fibre functor).

**T2 — naming honesty for the non-functors. ✅ APPLIED.**
- `archimedean-realization-functor.md` — added a "Level of the construction"
  note: `R_top` is a **motivic measure / ring homomorphism** out of
  `K₀(Var)` + a place, a functor only if lifted to `DM(k)`.
- `archimedean-functor-trace-commutativity.md` — `𝓕_Arch` relabeled the
  **object-level standard-part map `st`** (a ring hom, the underlying
  evaluation of the categorical functor `St`), not a functor itself;
  diagram edge relabeled.
- `standard-part-functor.lean` docstring — same clarification.
- `standard-part-functor.md` left as-is: it already calls `st` "a
  surjective ring homomorphism" and defines `St` with both an object-map
  and a morphism-map (a genuine functor claim).

**T3 — Lean structural. ✅ APPLIED (verified sorry-free).**
`MotivesArchimedean.lean`: `ArchimedeanCategory` now bundles
`[cat : Category Obj]`, and `FibreFunctor` carries a genuine
`functor : C ⥤ Arch.Obj` (morphism action + functor laws), requiring
`[Category C]`. `archRestriction` (`π_∞ ∘ τ : C → ℝ`) is documented as the
object-level evaluation, not a functor. `ArchimedeanRealizationFunctor`
docstring relabeled a motivic measure. Verified via lean-direct on restored
`v4-24-0` oleans (exit 0).

**T4 — pin τ's codomain (register). ✅ APPLIED.**
`notation-collisions.md` now states τ : C ⥤ Arch is canonical and the other
targets (`Vec_ℝ`, `Type*`, `D`) are **composites** with τ (`U ∘ τ`, the
underlying set-valued functor, τ into a geometric model) — genuine functors
at de-enriched levels, not rival functors. The maps into ℝ (`π_∞`, `R_top`,
`st`) are evaluations/ring homs, not functors. No corpus-wide rename needed;
the composite-tower framing reconciles the five stated codomains.

## Note on prior QA sidecars

The `.qa.json` sidecars for #2 and #4 recorded referee `open-objection` /
reproducibility `fail` from Lean compile errors, later overridden by
interactive `pass` notes with generic praise ("Sound conceptual
formulation…") rather than a re-verification of functoriality. The
functor-vs-map defect was never the object of those passes.

## Files

- `content/quantum-observable-universe/lean/QOU/MotivesArchimedean.lean`
- `content/quantum-observable-universe/mass-theory/archimedean-realization-functor.{md,lean,ts}`
- `content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness.{md,lean}`
- `content/quantum-observable-universe/mass-theory/archimedean-image-table.md`
- `content/quantum-observable-universe/appendix-surreals-archimedean/{standard-part-functor.lean, archimedean-functor-trace-commutativity.md}`
- `content/quantum-observable-universe/lean/QOU/AppendixSurreals/StandardPart.lean`
- `content/quantum-observable-universe/models-of-qous/spatial-realization-functor.{md,lean}`
- `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`
- `content/quantum-observable-universe/notation/notation-collisions.md` (the authoritative register, §"Archimedean / fibre / forgetful functors")
