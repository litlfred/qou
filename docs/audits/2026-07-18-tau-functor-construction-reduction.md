# The categorical τ-functor: current state, what a genuine construction requires, and a reduction

**Date:** 2026-07-18 · **Bean:** `qou-gym0` (attack the real τ-functor construction) ·
**Sibling:** `qou-la8r` / `qou-tq20` (the B2 Hodge-side wall, `TauRhoHodgeLift`).

**Honesty banner (STRICT, §"Axiomatization is NOT a Proof"):** τ is **NOT** constructed
and **NOT** proved in this tranche. Nothing here is wired to production; no fit; every
Lean statement is either a genuine theorem or a hypothesis threaded from an existing,
honestly-open conjecture class. The deliverable is a **reduction scaffold**: it sharpens
what "construct τ" means and reduces it to two already-named open items plus one
categorical gap Mathlib cannot yet express.

---

## 1. Current state of τ in the corpus (assumed vs axiomatized vs proved)

The fibre / observation functor τ (the Archimedean / Markov-trace functor of the
canonical-derivation chain, step 9) appears in three distinct epistemic modes.

### 1a. τ is ASSUMED as structure data (a genuine functor, but an input — never built)

| Site | Lean type | Status |
|---|---|---|
| `QOU.QuantumUniverse.fibreFunctor` (`CategoricalFoundations.lean`) | `C ⥤ Type*` (genuine `CategoryTheory.Functor`) | **field** of the structure — provided as input; the Tannaka gauge group `Aut⊗(ω)` is reconstructed from it |
| `MotivesArchimedean.FibreFunctor` | `functor : C ⥤ Arch.Obj` (genuine, post the T3 fix) | abstract data on an abstract `Arch` |
| `spatial-realization-functor.lean` | `fibreFunctor : C ⥤ D` | abstract data |

In every case τ is a **hypothesis**, not a construction: the source category `C` is an
opaque `[Category C] [MonoidalCategory C] [BraidedCategory C]`, and τ is a field. Nothing
builds τ from the concrete Hecke representations `H_n(q)`.

### 1b. τ (or a piece of it) is AXIOMATIZED as an honestly-open §3b conjecture class

| Class | File | Content | Instance? |
|---|---|---|---|
| `TauRhoHodgeLift g W Wbar` | `Archimedean/TauRhoHodgeLiftInterface.lean` | τ carries the fibre reality ρ (`q↦q̄`) to Hodge conjugation of `H¹(Bring)`; fields = hermiticity + entrywise-conjugation (its *inputs*) | **none** — THE WALL (α_EM per-loop measure `½·a₀ = 1/(8π)`) |
| `RealisationVolumeCompatibility Braid` | `Archimedean/RealisationVolumeCompatibility.lean` | `τ_∞` (Habiro `q₀`-eval) and `R_top` (motivic) both realize `V_hyp` | shape-witness only; **no instance** for the actual realizations |
| `MarkovTrace R H tr`, `HeckeAlgebra …` | `Machinery/MarkovTraceOnHecke.lean` | general-`n` Markov trace / `H_n(q)` | `HeckeAlgebra` has a `True` marker (Mathlib lacks `H_n(q)`, n≥3); `MarkovTrace` carries the real cyclicity/linearity laws but has **no general-`n` instance** |
| `conj:q-gl-fiber-functor` | `QGeometricLanglands.lean` | q-GL fibre functor | conjectural class |

### 1c. Concrete pieces of τ that ARE proved sorry-free (the constructible inputs)

| Piece | File | What is proved |
|---|---|---|
| Markov trace on `H₃(q)` | `Machinery/MarkovTraceOnHecke.lean` (`H3.trM`) | a real `R`-linear functional on the `Fin 6` NF module with **(M1) linearity, (M2) cyclicity `tr(uv)=tr(vu)`, (M3) Markov reduction** all proved over generic `[CommRing R]` — the genuine Frobenius pairing `tr_M` at `n=3` |
| Transfer-matrix ↔ Hecke correspondence | `Archimedean/TMCorrespondence.lean` | `tr_M(a·σ+b) = a·z+b`; Hecke product = transfer-matrix action — the `n=2` archimedean image, proved |
| ℂ-level ρ→Hodge model | `Archimedean/VertexLocalTauModel.lean` | the degenerate `H₂(i)` Jordan module and `ρ` (entrywise `starRingEnd ℂ`) carrying it to the `q=−i` partner — both *sides* of the lift, proved; does **not** construct the functor |

**Summary.** τ is a genuine `CategoryTheory.Functor` *only where it is assumed*. Where it
must be *built from the substrate* it is either an open §3b class (1b) or a concrete
low-`n` slice (1c). The gap between (1c) and (1a) — turning the proved `n=2,3` Markov
traces into a functor on the whole braided category, evaluated at `q₀`, respecting ρ — is
the genuine multi-week problem.

---

## 2. What a genuine construction requires

τ must be a **braided monoidal functor** `τ : 𝐂 → 𝐕𝐞𝐜_ℝ` (through the target `𝐀𝐫𝐜𝐡`),
where `𝐂` is the substrate braided category — concretely the category of finite-dimensional
`H_n(q)`-modules / the Hecke (Temperley–Lieb) category — satisfying five laws:

- **(F1) monoidal.** `τ(X⊗Y) ≅ τX ⊗ τY`, `τ(𝟙) ≅ ℝ`.
- **(F2) braided.** τ carries the R-matrix braiding of `𝐂` to the chosen symmetry/braiding
  of the target.
- **(F3) trace realization.** The categorical endomorphism-trace of `τ(ρ(β))` equals the
  Markov trace `tr_M(β) = Σ_λ y_λ(q) χ^λ(β)` (the observation-frame identity, chain step 6→9).
- **(F4) archimedean wall.** τ specializes the formal `q` to the substrate `q₀ ∈ ℝ`,
  `q₀ > 1`, `Im q₀ = 0` — the substrate→archimedean cut (§7c). Pre-wall everything is
  generic over `[Field R]` / `[CommRing R]`; ℝ appears only here.
- **(F5) reality → Hodge.** τ carries the fibre reality structure `ρ : q↦q̄` to Hodge
  conjugation on `H¹(Bring)` — exactly `TauRhoHodgeLift` (1b).

### The true remaining gaps

1. **Source category `𝐂` is not built for general `n`.** Mathlib has no `H_n(q)`, n≥3
   (`HeckeAlgebra.hecke_structure : True`). Only `n=2` (TMCorrespondence) and `n=3`
   (`H3.trM`) are concrete. The **domain** of τ is only partially constructed.
2. **F2 (braided morphism action) is unbuilt** — no R-matrix → target-braiding intertwiner
   in Lean.
3. **F3 at general `n`** is proved only at `n=2,3`; general `n` needs the
   `Ind_{H_n}^{H_{n+1}}` Markov stabilization (documented open in `MarkovTraceOnHecke.lean`).
4. **F5 (`TauRhoHodgeLift`)** — the apex, genuinely open. No instance.

Gaps 1–2 are **categorical-infrastructure** gaps (Mathlib cannot yet *express* the Hecke
category as a braided monoidal category); gaps 3–4 are the framework's own open items,
each already named as a class.

---

## 3. What this tranche builds — a reduction scaffold

New Lean file `content/quantum-observable-universe/lean/QOU/Archimedean/TauFunctorReduction.lean`.
It introduces **no vacuous marker and no fabricated instance**. It contains:

1. **`observationFrame ev tr := ev ∘ tr`** — the observation frame `τ_∞` modelled as the
   archimedean evaluation `ev : R →+* ℝ` (the wall F4, abstracted as an arbitrary ring hom
   = "specialize `q` to `q₀`") composed with a Markov trace `tr : H → R`.
2. **`observationFrame_cyclic` / `observationFrame_add`** — GENUINE theorems: given a
   `MarkovTrace R H tr` instance, `τ_∞` is **cyclic** (`τ_∞(xy) = τ_∞(yx)`, gauge-invariance
   of the observable) and additive. Derived, not assumed — the necessary condition for
   `τ_∞` to be a categorical trace (part of F3).
3. **`H3Concrete.obsH3_cyclic`** — a NON-VACUOUS concrete instance: the `n=3` observation
   frame `ev ∘ H3.trM` is proved cyclic using the already-proved `H3.trM_cyclic`. This
   **discharges the `n=3` slice of F3** with real content — one of the five laws is
   realizable *now* at `n=3`, no axiom.
4. **`tau_construction_reduces`** — the REDUCTION theorem. Threading the two *existing*
   open classes `[MarkovTrace R H tr]` and `[TauRhoHodgeLift g W Wbar]` as hypotheses, it
   derives the two properties the α_EM measure derivation consumes: (i) gauge-invariance of
   the observable (`τ_∞` cyclic) and (ii) the equal Hodge split (`Wbar.trace = W.trace`,
   the ½). Sorry-free, and non-degenerate: neither consequence is a class field — both are
   *derived* from the fields (§3b-cond rule 5).

**The reduction it records:** *constructing the observation side of τ* reduces to exhibiting
- a **general-`n` `MarkovTrace` instance** realizing `tr_M = Σ_λ y_λ χ^λ` (gap 3), and
- a **`TauRhoHodgeLift` instance** (gap 4, the wall),

on top of the categorical-infrastructure gaps 1–2 (the Hecke category itself), which Lean
cannot yet state. Everything *between* those — the composition `ev ∘ tr_M`, its cyclicity,
its `n=3` realization — is now proved. So the wall is sharpened from "construct the whole
functor" to "these two named instances + a Hecke-category infrastructure that Mathlib
lacks."

---

## 4. Honest assessment — how far from closing

**Far.** This does not close τ, and does not pretend to:

- **F5 (the wall) is untouched as a *theorem*.** `TauRhoHodgeLift` still has no instance;
  the reduction *uses* it as a hypothesis, it does not discharge it. The Hodge-side sibling
  (`qou-la8r`) is the effort that would supply it, and it too is a non-closing scaffold.
- **F1/F2 need a Hecke category Mathlib does not have.** Until `H_n(q)` and its braided
  monoidal structure exist in Lean for general `n`, the full functor `τ : 𝐂 → 𝐕𝐞𝐜_ℝ`
  cannot even be *stated*, let alone built. This is the dominant obstruction and is
  infrastructure-scale (a Mathlib contribution in its own right).
- **What genuinely moved:** the observation frame is now a *derived* cyclic functional
  (not an assumed one), its `n=3` instance is concrete and proved, and the open apex is
  pinned to two named classes rather than a diffuse "construct τ." That is real, modest
  progress and an honest tightening of the wall — nothing more.

The realistic path to closure remains: (a) build `H_n(q)` + its Wedderburn/Hoefsmit
seminormal reps as a braided monoidal category in Lean (large, infrastructure); (b) prove
the general-`n` Markov stabilization to instantiate `MarkovTrace` (framework-open, gap 3);
(c) discharge `TauRhoHodgeLift` via the geometric `W_λ` / `S³/2I` WRT route (the wall, gap 4,
Subgoal-2 general reversal 2026-07-11 makes it in-scope but the anti-fit discipline still
gates *how*). None is closed here.

## Files

- `content/quantum-observable-universe/lean/QOU/Archimedean/TauFunctorReduction.lean` (new)
- `docs/audits/2026-07-18-tau-functor-construction-reduction.md` (this doc)

Cross-refs: `docs/audits/2026-07-11-archimedean-functor-taxonomy.md` (the functor-vs-map
taxonomy), `docs/audits/2026-07-12-fibre-observable-categorical-not-analytic.md` (the
categorical, non-analytic framing of the fibre→observable passage), the canonical-derivation
cheat-sheet step 9.
