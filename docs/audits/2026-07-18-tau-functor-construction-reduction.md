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
   - **`n=4` rung (2026-07-19, PR #4046, `Machinery/MarkovTraceH4.lean`):** the concrete
     `Fin 24` NF module now carries (M1) linearity, (M3) Markov-σ₂ reduction, and a
     **sorry-free cyclicity *reduction*** `trM_cyclic_of_gram_symm` — `mulNF` bilinearity
     (with the `mulσ` actions kept opaque, so the depth-6 `whnf` wall is untouched) lifts
     to the Gram form `tr_M(u·v)=∑ u_i v_j G_{ij}`, whence `trM_cyclic` is *derived* modulo
     the single residual `gram_symm` (the finite `24²` base `G_{ij}=G_{ji}`, still
     `whnf`-blocked; audit `2026-07-19-h4-cyclicity-whnf-explosion.md`, beans `qou-svnb`).
     The clean closure is the abstract cyclic-trace lemma on `MarkovStabilization`
     (`HeckeBraidedCategoryScaffold`), which supplies this reduction generically for all
     `n` and discharges `gram_symm` — bean `qou-0vsu`. NB: `MarkovTraceH4` (concrete
     `mulNF` + reduction) is complementary to `HeckeH4StabilizationRung` (concrete
     `mulσ`/`TRM4` + Hecke/braid/stabilization, no `mulNF`); the two should be reconciled
     when the abstract lemma lands.
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

## 3b. Infra built in (owner directive — two pieces, both NON-CLOSING)

Following the owner's request to build the needed infra into this PR (still
honest, no laundering):

### Piece 1 — Hodge-side instantiation of `TauRhoHodgeLift` (bean qou-la8r)

New file `.../lean/QOU/Archimedean/HodgeGramLift.lean`. It proves the B2 class
`TauRhoHodgeLift` **IS instantiable by the Hodge Gram matrix**:

- `complexify M` — the `H^{1,0} ⊕ H^{0,1}` embedding (`M.map ofReal`);
- `complexify_isHermitian` — a real *symmetric* matrix, complexified, is
  Hermitian (the `hermitian` field);
- `complexify_map_conj` — **Hodge reality**: a real matrix is fixed by entrywise
  conjugation `ρ` (the `conjugated` field, with `Wbar = W`);
- `hodgeGramLift B` — the real **Gram** `Bᵀ·B` (symmetric, PSD), complexified,
  **instantiates** `TauRhoHodgeLift g (complexify (Bᵀ·B)) (complexify (Bᵀ·B))`;
- `LoopWeightIsHodgeGram W` — the **single remaining open identification** as a
  named `Prop`: `∃ B, W = complexify (Bᵀ·B)`;
- `tauRhoHodgeLift_of_loopWeightIsHodgeGram` — the wall-tightening theorem: **IF**
  the loop weight is a Hodge Gram, **THEN** `TauRhoHodgeLift` holds. Sorry-free.

**This does NOT close the wall.** No instance/witness is given for the *actual*
α_EM loop weight. The wall is *tightened* from "construct τ + prove the ρ→Hodge
lift" to the single identification **"loop weight = Hodge Gram."** That
identification is `LoopWeightIsHodgeGram`, and it stays OPEN.

### Piece 2 — Hecke braided-monoidal source-category scaffold (beans qou-pbjv, qou-ep0a)

New file `.../lean/QOU/Machinery/HeckeBraidedCategoryScaffold.lean`, tiered:

- **Tier 1 (proved slice + open apex).** `HeckeBraidedPresentation` — a §3b
  PRIMARY conjecture class carrying the three real relations of the braided
  presentation (Hecke quadratic = R-matrix eigenvalue; braid relation =
  Yang–Baxter/hexagon shadow = F2; far commutation = F1). Content-bearing (no
  `True`, no empty `: Prop`), **no general-n instance** (the F1/F2 source-category
  gap Mathlib lacks). A concrete n=2 slice `heckeQuadratic_h2` is **proved**
  (the diagonal generator with eigenvalues `q, −q⁻¹`), complementing the proved
  n=3 identities in `MarkovTraceOnHecke` (`H3.mulσ₀_hecke`).
- **Tier 2 (dependent open apex).** `MarkovStabilization` — a §3b DEPENDENT
  conjecture class (bean qou-ep0a): `tr_{n+1}(ι x) = tr_n x`. The dependency on
  the primary is **threaded through the type** — two `[HeckeBraidedPresentation …]`
  instance binders are the dependency edge. Content-bearing, **no instance**;
  base cases n=2,3 are the proved Markov reductions (`H3.trM_markov_σ₁`).
- **Bridge (derived).** `TauFunctorReduction.observationFrame_stabilizes` —
  GIVEN `MarkovStabilization`, the derived observation frame is tower-stable
  (`τ_∞(ι x) = τ_∞(x)`). Sorry-free; feeds the stabilization into the
  observation frame. `MarkovStabilization` still has no instance (general-n OPEN).

**lean-direct status (all sorry-free, exit 0 on `v4.24.0` restored oleans):**
`HodgeGramLift.lean` ✓, `HeckeBraidedCategoryScaffold.lean` ✓,
`TauFunctorReduction.lean` ✓ (imports both).

---

## 4. Honest assessment — how far from closing

**Far.** This does not close τ, and does not pretend to:

- **F5 (the wall) is now TIGHTENED, not closed.** `TauRhoHodgeLift` is proved
  **instantiable by a Hodge Gram** (§3b Piece 1), so the wall reduces to the single
  open identification `LoopWeightIsHodgeGram` ("the categorical loop weight equals a
  Hodge Gram `Bᵀ·B`"). No instance/witness for the *actual* α_EM loop weight is given —
  that identification stays OPEN. The class is instantiable; the identification is not
  discharged.
- **F1/F2 are now SCAFFOLDED (content-bearing conjecture classes), not built.**
  `HeckeBraidedPresentation` (primary) + `MarkovStabilization` (dependent) state the
  braided-presentation and Markov-stabilization content honestly, with proved n=2/n=3
  slices — but **neither has a general-n instance**. Until `H_n(q)` and its braided
  monoidal structure exist in Lean for general `n`, the full functor `τ : 𝐂 → 𝐕𝐞𝐜_ℝ`
  cannot be *built*. This remains the dominant obstruction (a Mathlib contribution in
  its own right); the scaffold names it precisely rather than closing it.
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

- `content/quantum-observable-universe/lean/QOU/Archimedean/TauFunctorReduction.lean` (new; + `observationFrame_stabilizes`)
- `content/quantum-observable-universe/lean/QOU/Archimedean/HodgeGramLift.lean` (new — Piece 1)
- `content/quantum-observable-universe/lean/QOU/Machinery/HeckeBraidedCategoryScaffold.lean` (new — Piece 2)
- `docs/audits/2026-07-18-tau-functor-construction-reduction.md` (this doc)

Cross-refs: `docs/audits/2026-07-11-archimedean-functor-taxonomy.md` (the functor-vs-map
taxonomy), `docs/audits/2026-07-12-fibre-observable-categorical-not-analytic.md` (the
categorical, non-analytic framing of the fibre→observable passage), the canonical-derivation
cheat-sheet step 9.
