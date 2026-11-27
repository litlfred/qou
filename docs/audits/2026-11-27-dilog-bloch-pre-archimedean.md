# Dilogarithm equivalence conjecture and the pre-Archimedean Bloch class (2026-11-27)

Research front 2 of the 2026-11-27 swarm. Source: the owner's uploaded AI-chat
discussion (`owner-discussion-2026-11-25-to-27.md`, lines 18–206 and 649–787,
held in the project files, not in the repo). That text is **unverified external
material**; every claim below was checked against the corpus, the library, Lean,
or SnapPy 3.x (`pip install snappy`, run 2026-11-27 in this session). PR #9447.

## Summary

| # | Claim in the discussion | Verdict | Evidence |
|---|---|---|---|
| 1 | Add `conj:algebraic-geometric-dilog-equivalence` with the `TetraplecticDilogBridge` Lean structure | **Do not add as proposed.** The label already exists with different content, and the proposed Prop is vacuous | `mass-theory/algebraic-geometric-dilog-equivalence.ts` (q-Pochhammer pole/cusp version, already a conjecture); `TetraplecticDilogBridgeVacuity.exists_bridge`, `exists_bridge_with_volume` (sorry-free) |
| 2 | Foth–Leitner tetraplectic reduction, `dim_ℝ C_w = 4ℓ(w)` | **Not checked against a source.** `foth2002` (math/0103042) and `fothleitner2003` (math/0104104) are in `references.bib` but **not ingested in `library/`**. `4ℓ(w)` is what the quaternionic Bruhat decomposition gives (each cell is ℍ^{ℓ(w)}), but no corpus artifact or held source states the "reduction of the Habiro state sum" that the conjecture uses | `grep -i foth library/INDEX.md` empty; bean `qou-5843` (scrapped: the tetraplectic reduction supplies `e_k`, not `c_3`) |
| 3 | `B(F) = ker([z] ↦ z ∧ (1−z))` on `P(F) = ℤ[F∖{0,1}]/five-term`, formalisable with no analysis | **True, now formalised** over any field | `PreArchimedeanBloch.delta_fiveRel`, `BlochGroup` |
| 4 | `2[ζ₆] ∈ B(ℚ(√−3))` for `4₁` ("check the exterior-power torsion") | **True, and sharper:** `1 − ζ₆ = ζ₆⁻¹`, so `δ[ζ₆] = ζ₆ ∧ ζ₆⁻¹ = 0` **exactly** in `Λ²_ℤ F^×`; in Suslin's antisymmetric convention `δ[ζ₆]` is 2-torsion and `2[ζ₆]` is killed | `gen_mem_blochGroup_of_phi6`, `delta_two_gen_of_phi6`, `fig8Class_cyclotomic` |
| 5 | Nahm equation of `Σ_m ∏(1−q^j)(1−q^{−j})` at `q → 1` is `(1−X)(1−X⁻¹) = 1 ⇔ X² − X + 1 = 0` | **True** (as the `q = 1` specialisation of the exact shift ratio) | `habiro41_succ`, `nahm41_iff_phi6`, `nahm41_mem_blochGroup` |
| 6 | "each `(q)_m` factor contributes `[1 − X] = [ζ₆]`" | **False as written.** `1 − ζ₆ = ζ₆⁻¹ = ζ̄₆ ≠ ζ₆`. The class is `[ζ₆⁻¹]`, which is `−[ζ₆]` only modulo torsion. Sign/orientation must be tracked | `phi6_facts` |
| 7 | Braid words: `4₁ = (σ₀σ₁⁻¹)²`, `5₂ = σ₀³σ₁σ₀⁻¹σ₁`, `8₁₈ = (σ₀σ₁⁻¹)⁴` | **True** (closures isometric to census `4_1`, `5_2`, `8_18`) | SnapPy `is_isometric_to` |
| 8 | `Vol(8₁₈) ≈ 5.33349`, "Galois shadow ≈ 0.91597" | **False.** `Vol(8₁₈) = 12.350906209` (13 tetrahedra) | SnapPy |
| 9 | "trace field of `8₁₈` is `ℚ(ζ₈)` (degree 4, two complex pairs)" | **False.** The shape field (= invariant trace field for a cusped manifold) is `ℚ[x]/(x⁴ − 2x³ + x² − 2x + 1)`, discriminant **−448**; `ℚ(ζ₈)` has discriminant 256. Negative discriminant ⇒ `r₂ = 1`: **one** complex place, so no Galois-conjugate "shadow volume" exists | SnapPy shapes at 150 digits + PARI `algdep`/`polredabs`/`nfdisc` |
| 10 | `5₂` and `(−2,3,7)` have equal volume but **different Bloch class** | **Equal volume true** (`2.8281220883`, census `m015`, `m016 = 12n242`), same field (cubic of discriminant −23; `x³ − x − 1` and `x³ − x² + 1` define the same field; "Lehmer-type" is a misnomer). **"Different Bloch class" is contradicted** by GSWZ, who state the two knots give **the same class in `K₃(K)`** | `library/arxiv-2412.04241v2/sections/sec-005-…md` lines 173–177; SnapPy |
| 11 | …and different Chern–Simons | SnapPy: `CS(5₂) = −0.15320`, `CS(12n242) = +0.23654` (mirror `−0.23654`); the difference is `1/12` within SnapPy's normalisation. How this reconciles with GSWZ's "same class" is **not settled here** | SnapPy |
| 12 | Pre-Archimedean evaluation is "strictly stronger" than the volume because it keeps Galois conjugates | **Overstated.** By Borel, the regulator `B(F) ⊗ ℚ → ℝ^{r₂}` over all complex places is injective. Modulo torsion the class carries exactly the volume vector over the complex places. What it adds is the torsion (and, in the extended group, Chern–Simons) | Borel/Suslin; corpus `MathlibExt/BorelRank.lean` |
| 13 | GSWZ "Habiro ring of a number field", arXiv:2412.04241 | **Real and held**: `library/arxiv-2412.04241v2`, bib key `garoufalidis-scholze-wheeler-zagier2024`. It is the right ambient for Stage A | INDEX.md |
| 14 | Stage A ("Nahm class = Ptolemy class") is "tractable for all knots" | **Overclaim.** Proved here for `4₁` only, at the level "the Nahm solution and the geometric shape agree as field elements". The general identification is open (it is the content of the Dimofte–Garoufalidis / GSWZ framework, stated there as data `(A, z)` from a triangulation, not derived from a state sum) | GSWZ §1.7 (`sec-007`, line ~119) |

## A corpus bug found on the way (fixed in #9447)

`appendix-formalisation-notes/bloch-group-quotient-construction.lean` built its
"pentagon subgroup" from

    [x] − [y] + [y/x] − [(1 − y⁻¹)/(1 − x⁻¹)] + [(1 − y)/(1 − x)]

— Suslin's last two arguments **inverted**. This is not a relation of the
pre-Bloch group:

- Lean: `appendixRel_not_mem_pentagonSubgroup` — over `ℚ` at `(x, y) = (2, 3)` the
  antisymmetric pairing `v₂ ∧ v₃` (2- and 3-adic valuations) sends it to `4`, while
  it kills every Suslin relation (`appendixRel_two_three`).
- Numerically: with the Bloch–Wigner `D`, the inverted sum at `x = 0.3+0.7i`,
  `y = −0.4+0.2i` is `3.1306…`; Suslin's is `−2·10⁻³¹` (mpmath, 30 digits).

`lean/QOU/MassTheory/BlochGroupComplex.lean` and `BlochSuslinComplex.lean` already
use Suslin's orientation, so the fix (swap `shape₄`, `shape₅` to
`(1 − x⁻¹)/(1 − y⁻¹)`, `(1 − x)/(1 − y)`) is AGENTS.md exemption 2 (corpus-derived).
The block's QA sidecar is stale after the edit.

## What is now proved (Lean, `QOU/MassTheory/PreArchimedeanBloch.lean`)

All over an arbitrary field, sorry-free, axioms `propext, Classical.choice, Quot.sound`:

1. `delta_fiveRel` — Suslin's symbol kills the five-term relation for **any
   antisymmetric** biadditive pairing (the `β(a, a)` terms cancel exactly, so
   alternation is not needed).
2. `BlochGroup F = ker (P(F) → Λ²_ℤ F^×)`, through `ExteriorAlgebra ℤ (Additive Fˣ)`.
3. `[ζ] ∈ B(F)` whenever `ζ² − ζ + 1 = 0`; `2[ζ₆] ∈ B(ℚ(ζ₆))`.
4. The `4₁` Habiro summand recursion and its Nahm equation; every Nahm solution is
   a Bloch class.

Not proved and not assumed: that `2[ζ₆]` is the class of the geometric ideal
triangulation of `S³ ∖ 4₁` (Thurston; cited), and anything Archimedean.

## §2.24 restructuring (owner chose Stage A, 2026-11-27; applied)

`sec:q-special-functions-dilog` currently ends with
`conj:archimedean-realisation-volume-compatibility` (`τ∞ ↔ R_top`), which already
**is** the discussion's "Stage B". So the split is:

- **Stage A, new proposition** `prop:pre-archimedean-figure-eight-bloch-class`,
  placed before `archimedean-realisation-volume-compatibility`: the Nahm equation
  of the `4₁` Habiro summand is `X² − X + 1 = 0`, and its solutions give
  `[ζ₆] ∈ B(ℚ(√−3))` exactly. Lean: the theorems above. Prose states the scope (4₁
  only; the geometric identification is cited).
- **Stage B, no new block**: retitle nothing; add one sentence to
  `conj:archimedean-realisation-volume-compatibility` saying that its `4₁` case
  factors as "Stage A (proved) then the regulator `D` on `B(ℚ(√−3))`", with
  `Vol(4₁) = 2D(e^{iπ/3})` (`BlochSuslinComplex.figure8_from_rigidity` already holds
  the calibration).
- **Do not add** `TetraplecticDilogBridge`. If a tetraplectic statement is wanted,
  its fields must be *defined* from `H_n(q)` and `Li₂^q`; that requires ingesting
  Foth–Leitner first.

Default if the owner says nothing: the two Lean files and the appendix fix land;
no content block changes.
