# The σ₁³ deuteron surface-curvature term: what the corpus has, what it lacks, and why the scalar surface sector is provably zero

**Date:** 2026-08-02 · **Branch:** `claude/sigma1cubed-seifert-tessellation-nastokes-2026-08-02` ·
**Bean:** `qou-3q7t` (C_knot=5.853 deuteron Δ_λ deficit) · **Axis:** Δ_λ magnitude / NA-Stokes surface sector ·
**Tier:** honest open-research finding — scope-(b) exclusion of the *character-paired* surface-correction
class (cited invariant: trace annihilates commutators) + precise gap naming. **No fit. Nothing wired.**

## 0. BLUF

The task premise (pincer #4615 qou-prjo + #4617 qou-i4pz): the entire deuteron 5.853× categorical deficit
lives in ONE object — the transverse non-abelian (Yekutieli) Stokes surface-curvature term over the σ₁³
trefoil Seifert surface — and the stated blocker is that the corpus lacks the *surface discretization*.

This note establishes, 0-fit:

1. **What the corpus HAS.** (i) The 1D boundary holonomy is real and computed (`braidWordHolonomy`
   ordered product + Markov cocycle in `NonAbelianStokes.lean`; Hoefsmit χ^λ caches). (ii) The σ₁³
   trefoil **ideal-triangulation** discretization already exists — SnapPy 2-tetrahedron octahedral
   decomposition, `deuteron-octahedral-gluing.witness.json` (Vol=0, flat tetrahedra z∈{½,2}, z₀z₁=1). (iii)
   The **fibre** curvature 2-form `F_q = [δq₁,δq₂]` exists as an *abstract single-parallelogram identity*
   over a generic non-commutative `Ring R` (`germ-commutator-q-curvature.lean`, derived by `noncomm_ring`).

2. **What the corpus LACKS.** The **Seifert-surface** (spanning-surface) tessellation *with a per-cell
   𝔤-valued curvature 2-form* and a surface-ordered product over its cells. The `MI₂`
   (`MultiplicativeSurfaceIntegral`) in `NonAbelianStokes.lean` is a literal `fun _ _ _ => 1` **stub**; the
   fibre `F_q` is bound to no connection `A`, no manifold, no Seifert surface. This note **supplies the
   derived tessellation** (Seifert's algorithm on σ₁³) and asks whether a *derived* per-cell curvature can
   produce 5.853.

3. **Why the scalar surface sector is provably ZERO (the prune).** By the non-abelian Stokes theorem the
   genuine 2D content is the **surface-ordering correction**: the defect between the path-ordered
   `𝒫exp∮F` boundary holonomy and its abelian (unordered) product, which is a **product of commutators**.
   The binding formula `B(K) = m_e·|Σ_λ y_λ χ^λ(β_K) Δ_λ|` pairs Δ_λ with the **block character**
   `χ^λ = tr_λ(ρ(β_K))`. A character is a **cyclic trace**, and *a trace annihilates every commutator*:
   `tr(AB−BA)=0`. Hence the surface-ordering correction contributes **identically zero to χ^λ** — the
   scalar/character-paired surface term cannot supply the 5.853× deficit. This is one invariant unifying
   three prior corpus facts: `holonomy_perm` (abelian τ-shadow ordering defect = 0, #4357), the
   torus-knot **Vol=0** of σ₁³ (`deuteron-octahedral-gluing`), and `mi-sw-abelianisation`.

**Consequence (converges on the qou-3q7t surviving direction, adds the structural reason).** The deuteron
deficit cannot be a trace-level surface-curvature correction. The surface term's *operator* content
`[A,B]` is non-zero but has zero block-trace, so the *only* functional that extracts it is a **non-cyclic,
eigenphase-weighted per-block pairing** — precisely the per-vertex seminormal eigenphase / q-Reeb `Δθ_λ`
already named as Candidate #1 in the E₀-options audit and the sole survivor in qou-3q7t §STILL OPEN. The
new content here is the *proved reason* it is the only survivor: trace cyclicity excludes the entire
character-correction class (scope-(b)).

## 1. Machinery inventory (corpus-grep, all four paths)

| Object | Status in corpus | Location |
|---|---|---|
| 1D boundary holonomy (ordered product, Markov cocycle) | **REAL, computed** | `braidWordHolonomy`, `braidWordHolonomy_append_letter` (`NonAbelianStokes.lean`) |
| block character χ^λ(β_D) at H₆, q₀ | **REAL, cached** | `chi-deuteron-h6-at-q0-50dps*.witness.json` (interface-inclusive) |
| σ₁³ ideal-triangulation (octahedral / SnapPy) | **EXISTS** | `deuteron-octahedral-gluing.witness.json` (Vol=0, flat, z₀z₁=1); `trefoil-octahedral-shape-from-rep` (z=−h²) |
| fibre curvature `F_q=[δq₁,δq₂]` (single parallelogram) | **abstract identity only** | `germ-commutator-q-curvature.lean` (generic `Ring R`, no connection/manifold) |
| Seifert-surface tessellation + per-cell curvature 2-form | **ABSENT as compute** | — (`MI₂` is `fun _ _ _ => 1` stub) |
| surface-ordered product `MI₂` over cells | **STUB = 1** | `MultiplicativeSurfaceIntegral` (`NonAbelianStokes.lean`) |
| observable/geometric surface term over σ₁³ | **provably 0** (3 reasons) | `holonomy_perm`; torus-knot Vol=0; `mi-sw-abelianisation` |
| deuteron binding via **fibre tiers** | **closed to 0.036%** | `deuteron-g2-frame-artifact` (rotational + bar-odd t + bar-even h²; Ω_{k≥2}=0 for σ₁³) |

The last row matters: the deuteron **is** already closed to 360 ppm by a *fibre-level tier decomposition*,
NOT by a 2D surface integral. The 5.853× "deficit" is specific to the **categorical master-formula
normalization** `Σ_λ y_λ χ^λ sgn f^λ`; it is not an open physical prediction, it is the gap between the
*character-paired* categorical form and the geometric closure.

## 2. The derived Seifert tessellation of σ₁³ (Seifert's algorithm — canonical, 0-fit)

Seifert's algorithm on the standard σ₁³ (2-strand, 3 positive crossings) diagram:

- **Seifert circles:** the oriented smoothing of a 2-strand braid yields **2** nested Seifert circles ⇒
  **2 Seifert disks** (2-cells).
- **Bands:** one twisted band per crossing ⇒ **3 bands** (1-cells joining the two disks).
- **Euler characteristic:** `χ = (#disks) − (#bands) = 2 − 3 = −1`.
- **Genus (one boundary component, the knot):** `χ = 1 − 2g ⇒ g = 1`. The σ₁³ Seifert surface is the
  **once-punctured torus** (standard genus-1 trefoil surface).
- **First homology:** `rank H₁ = 1 − χ = 2`; two handle generators `a₁, b₁`.
- **Surface relator (genus-1, one boundary):** `∂Σ = [a₁, b₁] = a₁ b₁ a₁⁻¹ b₁⁻¹` — the boundary word is a
  **single commutator** of the two handle holonomies. *This is the exact object the non-abelian Stokes
  theorem assigns to a genus-1 surface: the surface-ordered integral of the curvature = one handle
  commutator.*
- **Symmetrized Seifert form** (canonical linking data): `V + Vᵀ = [[−2, 1], [1, −2]]`, `det = 3 =
  |Δ_trefoil(−1)|` (the trefoil determinant). The `−2` diagonal is the (A₂/E₂-type) framing, the
  off-diagonal `1` the inter-handle linking.

All of the above are **derived from Seifert's algorithm** — zero free parameters. They are machine-verified
in [`Sigma1CubedSeifertTessellation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/Sigma1CubedSeifertTessellation.lean)
(`decide`/`omega`, Mathlib-free integer core; no olean wall).

## 3. The prune: trace cyclicity annihilates the surface-ordering correction (scope-(b))

Non-abelian Stokes: `Hol(∂Σ) = 𝒫exp∮_Σ F`. Writing the boundary holonomy as the ordered product of the
generator-actions and its abelian (unordered) counterpart, the **2D surface content** is the ordering
defect `D = Hol_ordered · Hol_abelian⁻¹`, which on a genus-1 surface is the single handle commutator
`[a₁,b₁]` (and in general a product of `g` commutators).

The binding formula reads Δ_λ off against the **block character** `χ^λ(β_K) = tr_λ ρ(β_K)`. For **any**
cyclic trace `tr` and **any** `A,B`: `tr(AB) = tr(BA)` ⇒ `tr(AB − BA) = 0` ⇒ **`tr[A,B] = 0`**. Therefore

> the surface-ordering correction contributes **identically zero** to every block character χ^λ.

Equivalently: the ordered and abelian holonomies have the **same** character (`holonomy_perm`), so the
*difference* — the pure 2D surface term as seen by χ^λ — is zero. Machine-verified as
`traceLike_commutator_zero` over a generic `Ring R` with an abstract cyclic trace
([`Sigma1CubedSeifertTessellation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/Sigma1CubedSeifertTessellation.lean),
sorry-free) — the Markov trace **is** cyclic (proved elsewhere in the corpus), so the abstract hypothesis is
discharged by the real object.

**scope-(b) exclusion.** The class "Δ_λ = a surface-curvature *character* correction `tr_λ(surface term)`"
is structurally excluded, cited invariant `traceLike_commutator_zero`. This is a *proved* exclusion, not a
scope-limited numerical negative: no choice of connection `A`, tessellation refinement, or curvature `F`
can make a trace of a commutator non-zero.

## 4. Derive-then-check (target locked BEFORE compute; anti-fit)

**Locked target (before any compute):** `B_AME(²H) = 2.224566 MeV`; bare categorical
`B(D)=m_e·|Σ y_λ χ^λ sgn f^λ| = 0.380 MeV` (−82.9%); `C_knot(D) = 5.853`.

**Derived probe** ([`sigma1cubed_seifert_surface_term_probe.py`](../../computations/deltalambda/sigma1cubed_seifert_surface_term_probe.py)):
the handle-commutator surface term `[ρ(a₁),ρ(b₁)]` in the Hecke rep, its per-block trace (must be 0 by §3),
and the *eigenphase-weighted* per-block pairing as the derived Δ_λ candidate. **No parameter is tuned to
5.853.**

Result (see witness):
- **`tr_λ([A,B]) = 0` for every block** — numerically confirms §3 (the character channel is null); the
  scalar surface term does **not** move `B(D)` off 0.380. **The 5.853 deficit is NOT in the scalar surface
  sector.**
- The **eigenphase-weighted** per-block charge `Σ_i θ_i^λ ⟨λ,i|[A,B]|λ,i⟩` is the only non-vanishing
  extraction. Whether it *derives* 5.853 requires the explicit σ₁³ H₁-generator holonomies `a₁,b₁` inside
  the H₆ interface braid **and** the seminormal eigenphase weights `θ_i^λ` (q-Reeb `Δθ_λ`) — neither is a
  fit, but **the H₁-generator identification within the H₆ interface braid is not currently in the corpus**
  (see §5). This probe therefore **does not close** the deuteron; it names the datum that would.

## 5. The precise named gap (bean qou-3q7t, sharpened)

The surface sector is **not** missing "a discretization" in the naive sense — Seifert's tessellation is
canonical (§2) and the ideal triangulation already exists. What is missing, and what a derivation needs, is:

1. **The explicit H₁-generator holonomies `a₁, b₁` of the σ₁³ Seifert surface *as elements of the H₆
   interface Hecke algebra*** — i.e. which sub-words of the deuteron braid β_D realize the two handles of
   the genus-1 spanning surface. (In H₂ the two handles collapse — H₂ is abelian — so the trefoil-as-2-braid
   is degenerate; the deuteron lives at H₆ = 3A, A=2, where the handles are non-commuting.)
2. **The seminormal eigenphase weights `θ_i^λ` (q-Reeb `Δθ_λ`)** that convert the operator commutator
   `[a₁,b₁]` (zero block-trace) into a non-cyclic per-block charge — the operator-valued branching combiner.

Both are **derivable** (canonical), **neither is a fit**, and together they define
**`Δ_λ = eigenphase-weighted per-block charge of the σ₁³ handle commutator`** — a candidate structurally
**distinct from the six failed ansätze** (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov) and, being the per-block matrix element of a commutator, **naturally
mixed-sign with zero total** — matching the known mixed-sign / sum-to-zero Δ_λ requirement (the PROBE-4
chirality structure) that KL-positivity could not supply.

**Honest bottom line.** The 2D *scalar/character* surface sector is provably empty (trace kills the
commutator). The deuteron 5.853 residual is an **operator-valued** (pre-trace) quantity, extractable only by
the eigenphase-weighted per-block pairing — which is exactly the surviving q-Reeb `Δθ_λ` direction. This
note supplies the derived tessellation + the proved prune + the sharpened gap; it does **not** manufacture a
closure. The missing datum (H₁-handle holonomies in the H₆ interface braid + eigenphase weights) is filed on
`qou-3q7t`.

## 6. Anti-fit ledger

| statement | status |
|---|---|
| σ₁³ Seifert tessellation: 2 disks + 3 bands, χ=−1, g=1, rank H₁=2, relator=[a,b] | **derived (Seifert's algorithm) + Lean `decide`/`omega`** |
| symmetrized Seifert form det = 3 = trefoil determinant | **derived + Lean `decide`** |
| trace annihilates commutators ⇒ scalar surface term = 0 in χ^λ | **Lean sorry-free (`traceLike_commutator_zero`)** |
| `tr_λ([A,B]) = 0` per block (numerical) | **measured, 0-fit** |
| eigenphase-weighted per-block charge = derived Δ_λ candidate | **structure named; H₆ handle-holonomies NOT in corpus** |
| deuteron 5.853 closure | **OPEN** (`qou-3q7t`) — not manufactured |

`B_AME` used **only** as a locked diagnostic target, **never inverted**; `free_parameters = 0`; exact mpmath
(50 dps); nothing wired to production.
