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
   derived tessellation** (Seifert's algorithm on σ₁³) and tests, empirically, whether a
   *tessellation-invariant* (per-cell-DOF-free, so non-fit) surface term can produce 5.853 — §4.

3. **Tessellation-independence (owner's make-or-break test) + why the scalar surface sector is ZERO.**
   *Empirically* (probe + witness, §4), the one tessellation-independent, per-cell-DOF-free scalar surface
   quantity — the writhe-normalised Kauffman/Jones **state sum** — is **identical across two tessellations**
   (σ₁³ 8-state vs an R2-refined 32-state diagram, agreeing to `5e-51`): a topological invariant with **no
   tunable per-cell DOF ⇒ not a fit**. But its **archimedean-q₀ value does NOT reproduce 5.853** (it is the
   ordinary trefoil Jones — torus-knot degenerate). *Structurally*, the genuine 2D content is the
   **surface-ordering correction** (a **product of commutators**), and the binding formula
   `B(K)=m_e·|Σ_λ y_λ χ^λ(β_K) Δ_λ|` pairs Δ_λ with the **block character** `χ^λ = tr_λ ρ(β_K)`. Since a
   character is a **cyclic trace** and *a trace annihilates every commutator* (`tr(AB−BA)=0`), the correction
   contributes **identically zero to χ^λ** (confirmed numerically to 40 dps, §4). This one invariant unifies
   three prior corpus facts: `holonomy_perm` (abelian τ-shadow ordering defect = 0, #4357), the torus-knot
   **Vol=0** of σ₁³ (`deuteron-octahedral-gluing`, `PinchedOctahedronDegenerate.lean`), and
   `mi-sw-abelianisation`.

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

The **structural / combinatorial** facts (cell count, Euler relation, genus, rank H₁, relator abelianisation,
symmetrized-Seifert det = 3) are machine-verified in
[`Sigma1CubedSeifertTessellation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/Sigma1CubedSeifertTessellation.lean)
(`decide`, Mathlib-free `Int` core, `lean`-direct exit 0, sorry-free; no olean wall):
`seifertEuler_eq_neg_one`, `seifert_euler_relation` (χ = 2−2g−b closes ⇒ g=1), `rankH1_eq_two`,
`relator_abelianises_to_zero`, `symmetrizedSeifertDet_eq_three`. **These are pure structural facts only** —
per the owner ruling (2026-08-02) the numerical surface-term → binding (C_knot) connection is *empirical*
(§4), never a Lean proof.

## 3. The prune: trace cyclicity annihilates the surface-ordering correction (scope-(b))

Non-abelian Stokes: `Hol(∂Σ) = 𝒫exp∮_Σ F`. Writing the boundary holonomy as the ordered product of the
generator-actions and its abelian (unordered) counterpart, the **2D surface content** is the ordering
defect `D = Hol_ordered · Hol_abelian⁻¹`, which on a genus-1 surface is the single handle commutator
`[a₁,b₁]` (and in general a product of `g` commutators).

The binding formula reads Δ_λ off against the **block character** `χ^λ(β_K) = tr_λ ρ(β_K)`. For **any**
cyclic trace `tr` and **any** `A,B`: `tr(AB) = tr(BA)` ⇒ `tr(AB − BA) = 0` ⇒ **`tr[A,B] = 0`**. Therefore

> the surface-ordering correction contributes **identically zero** to every block character χ^λ.

Equivalently: the ordered and abelian holonomies have the **same** character (`holonomy_perm`, corpus-proved
in `QOU.MathlibExt.YekutieliIntegration`, `CommMonoid` permutation-invariance), so the *difference* — the
pure 2D surface term as seen by χ^λ — is zero. Its **combinatorial abelianised shadow** is machine-verified
here as `relator_abelianises_to_zero` (the genus-1 relator `[a,b]` has exponent-sum `(0,0)`;
[`Sigma1CubedSeifertTessellation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/Sigma1CubedSeifertTessellation.lean),
Mathlib-free, sorry-free). The trace-level statement `tr[A,B]=0` is the standard cyclicity of a trace (the
Markov trace is cyclic — corpus-proved), invoked here as textbook algebra, **not** re-formalised as a new
theorem.

**scope-(b) exclusion.** The class "Δ_λ = a surface-curvature *character* correction `tr_λ(surface term)`"
is structurally excluded by trace cyclicity (`tr[A,B]=0`): no choice of connection `A`, tessellation
refinement, or curvature `F` can make a trace of a commutator non-zero. This is a *proved algebraic*
exclusion, not a scope-limited numerical negative — and it is confirmed numerically in §4 (the surface
correction to the closure character is `0` to 40 dps).

## 4. Empirical tessellation-independence probe (owner protocol; target locked BEFORE compute; anti-fit)

Per the owner ruling this sector is tested **empirically** (Python probe + witness, never a Lean proof).
**Locked targets (before any compute):** `B_AME(²H) = 2.224566 MeV`; bare categorical
`B(D)=m_e·|Σ y_λ χ^λ sgn f^λ| = 0.380 MeV` (−82.9%); `C_knot(D) = 5.853`. `B_AME` diagnostic-only, never
inverted.

**The make-or-break test (owner): is the surface term tessellation-independent?** The one
tessellation-independent, per-cell-DOF-**free** scalar the σ₁³ surface admits is the Kauffman-bracket / Jones
**state sum** — a literal sum over the `2^c` smoothing states (= a tessellation of the diagram),
writhe-normalised to a Reidemeister/Pachner invariant. Probe
[`sigma1cubed_seifert_surface_term_probe.py`](../../computations/deltalambda/sigma1cubed_seifert_surface_term_probe.py)
(witness `sigma1cubed-seifert-surface-term.witness.json`) evaluates it over two tessellations:

| tessellation | word | states | `f` at q₀ |
|---|---|---|---|
| TESS-A (minimal) | σ₁³ | 2³ = 8 | `0.79806841228179419819` |
| TESS-B (R2-refined = sub-plaquette regulator) | σ₁³·(σ₁σ₁⁻¹) | 2⁵ = 32 | `0.79806841228179419819` |

- **Tessellation-independent: YES.** The two agree to `rel diff 5.0e-51` (exact) — refining the tessellation
  (the R2 insertion is the discrete "nested sub-Planck plaquette" regulator) leaves the value **exactly**
  unchanged. There are **no tunable per-cell DOF** ⇒ **not a fit** (the invariance IS the evidence).
  Cross-checked against the exact right-handed trefoil Jones `V = −t⁴+t³+t` (`matches_exact: True`).
- **Value vs target: does NOT hit 5.853.** `f/C_knot = 0.136` — the tessellation-invariant scalar surface
  state-sum at the **archimedean** q₀ is the ordinary trefoil Jones value, nowhere near 5.853. This is the
  expected torus-knot degeneracy (Vol=0, pinched octahedron; `PinchedOctahedronDegenerate.lean`).
- **Scalar surface-ordering correction to χ^λ = 0.** Reordering the closure word (ordered vs abelianised)
  leaves the closure character identical to 40 dps (`abs_difference = 0`) — numerically confirms §3
  (trace cyclicity). The scalar surface term adds nothing to `B(K)=m_e|Σ_λ y_λ χ^λ Δ_λ|`.

**Verdict.** The σ₁³ surface state-sum **is** tessellation-independent (a topological invariant, no fit), but
at the archimedean q₀ it is **degenerate** and does **not** reproduce the deuteron 5.853 deficit; the
character-channel correction is identically zero. The 5.853-relevant content is **not** in the
tessellation-invariant scalar/archimedean surface sector.

## 5. The precise named gap (bean qou-3q7t, sharpened) — it is NOT a missing discretization

The pincer's stated blocker — "the corpus lacks the surface discretization" — is **not** the real obstruction:

1. **The surface discretization already exists** in two canonical forms: Seifert's genus-1 CW tessellation
   (§2, now machine-verified) and the SnapPy octahedral ideal triangulation (`deuteron-octahedral-gluing`).
2. **Any tessellation gives the same answer** (§4, exact to 5e-51) — the surface term is a *topological
   invariant*, so refining or changing the tessellation is inert. There is nothing to "fix" by discretizing
   better.
3. **At the archimedean q₀ that invariant is degenerate** (σ₁³ is a torus knot: Vol=0, pinched octahedron,
   all four MSR shape-logs `= 0`, `e₂ = 0` — `PinchedOctahedronDegenerate.lean`), and the scalar/character
   channel is annihilated by trace cyclicity (§3). So no archimedean-q₀ scalar surface term can carry 5.853.

**The real, already-documented wall is the fibre → archimedean τ-transfer.** The genuine non-vanishing
surface content lives at the **fibre / root-of-unity WRT** level (the Kashaev/Turaev-Viro/BW-localization
state-sum at `q = ω`, `N → ∞` — infra: beans `bwse` (WRT = BW localization), `qou-nalu` (Whitehead-Kashaev
state-sum), `qou-d7lh` (tetraplectic state-sum);
[`2026-05-24-crystal-yekutieli-correspondence-chain.md`](2026-05-24-crystal-yekutieli-correspondence-chain.md)).
Its regular part carries the torsion `D(ζ)=∏(1−ω^{ζ+k})^{k/N}` (Garoufalidis–Kashaev A.17), a *fibre* object;
obtaining a *number* at the substrate q₀ requires the **τ-functor transfer of the pinched regular part** —
the SHARPENED WALL already recorded in
[`geometric-qdilog-lifted-amplitude`](../../computations/deltalambda/geometric_qdilog_lifted_amplitude_probe.py).
This note does **not** close that wall.

**A structurally-distinct Δ_λ candidate this note names (not a fit, not yet computed):** because the scalar
surface term vanishes but the *operator* `[a₁,b₁]` does not, the only non-cyclic extraction is the
**eigenphase-weighted per-block charge** `Σ_i θ_i^λ ⟨λ,i|[a₁,b₁]|λ,i⟩` — the per-vertex seminormal eigenphase
/ q-Reeb `Δθ_λ` (E₀-options Candidate #1, the sole survivor in qou-3q7t). Being a per-block matrix element of
a commutator it is **naturally mixed-sign with zero total**, matching the known mixed-sign / sum-to-zero Δ_λ
requirement (PROBE-4 chirality) that KL-positivity could not supply — and it is distinct from all six failed
ansätze. Computing it requires the H₁-handle holonomies of the σ₁³ surface *inside the H₆ interface braid*
(the trefoil-as-2-braid H₂ is abelian ⇒ handles collapse ⇒ degenerate; the deuteron lives at H₆ = 3A). That
identification is **not in the corpus**; it is the honest next datum.

**Honest bottom line.** Tessellation-independence holds (the surface term is a topological invariant, not a
fit); the converged archimedean value does **not** hit 5.853 (torus-knot degeneracy + trace-cyclicity
vanishing of the scalar channel). The deuteron 5.853 residual is a **fibre-level / operator-valued** quantity;
the open blocker is the fibre→archimedean τ-transfer, **not** a missing surface discretization. No closure is
manufactured. Filed on `qou-3q7t`.

## 6. Anti-fit ledger

| statement | status |
|---|---|
| σ₁³ Seifert tessellation: 2 disks + 3 bands, χ=−1, g=1, rank H₁=2 | **derived (Seifert's algorithm) + Lean `decide` (structural only)** |
| genus-1 relator `[a,b]` abelianises to `(0,0)` | **Lean `decide` sorry-free (`relator_abelianises_to_zero`)** |
| symmetrized Seifert form det = 3 = trefoil determinant | **derived + Lean `decide` (`symmetrizedSeifertDet_eq_three`)** |
| surface state-sum is **tessellation-independent** (TESS-A ≡ TESS-B to 5e-51) | **measured, 0-fit (EMPIRICAL)** |
| tessellation-invariant value at q₀ does **not** reproduce 5.853 (torus-knot degenerate) | **measured, 0-fit (EMPIRICAL)** |
| scalar surface-ordering correction to χ^λ = 0 (trace cyclicity) | **measured 0 @ 40 dps + textbook algebra** |
| trace annihilates commutators ⇒ scalar surface term excluded (scope-(b)) | **standard cyclicity (NOT re-proved as Lean); abelian shadow in Lean** |
| eigenphase-weighted per-block charge = structurally-distinct Δ_λ candidate | **structure named; H₆ handle-holonomies NOT in corpus** |
| deuteron 5.853 closure | **OPEN** (`qou-3q7t`) — fibre→archimedean τ-transfer wall; not manufactured |

The numerical surface-term → binding result is **EMPIRICAL** (probe + witness), **never** a Lean proof /
never wired (owner ruling 2026-08-02). `B_AME` used **only** as a locked diagnostic target, **never
inverted**; `free_parameters = 0`; exact mpmath (50 dps); nothing wired to production.
