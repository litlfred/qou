# Holography and q-Navier–Stokes claims of an external essay: critical review

Date: 2026-11-25. Owner request recorded in `docs/coordination/owner-rulings.md`
(row 2026-11-25). PR #9428. The Hecke, Bring-spectral and cocenter threads of the
same essay are reviewed on #9415 (sibling session); this document covers the
holography and q-NS claims.

Photon form in scope (owner ruling, strict): γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹.
None of the claims below depends on the photon form.

## Evidence produced

- **Exact probe** `computations/probes/bring54_cochain_complex_probe.py`
  (witness `bring54-cochain-complex.witness.json`, 11/11 checks). It builds the
  regular {5,4} map with orientation-preserving group S₅ (darts = S₅, vertex
  rotation g↦g·y with |y| = 4, edge involution g↦g·t with |t| = 2, face rotation
  g↦g·ty with |ty| = 5, ⟨y,t⟩ = S₅), which is the tessellation of Bring's surface
  described by Riera–Rodríguez (`library/pjm-v154-n1-p09-s`) and
  Braden–Northover (`library/arxiv-1206.6004v2`). Every number is an integer, a
  rational rank, or an exact algebraic number. No float64.
- **Lean** `folio/quantum-observable-universe/lean/QOU/BringsSurface/TraceCochainObstructions.lean`.
  Verification status is recorded in §Verification below.

| quantity | value | how |
|---|---|---|
| V, E, F, χ, flags | 30, 60, 24, −6, 240 | cycle counts of the map |
| d1·d0 | 0 | integer matrix product |
| Betti over ℚ | (1, 8, 1) | rank d0 = 29, rank d1 = 23 |
| dim ker Δ₀, Δ₁, Δ₂ (unit weights) | 1, 8, 1 | rational ranks |
| harmonic 1-cochains | all satisfy d1h = 0, d0ᵀh = 0 | exact nullspace |
| 1ᵀ·d1 | 0 | column sums |
| charpoly Δ₀ | λ(λ−2)¹¹(λ−4)⁵(λ−5)⁴(λ−6)⁵(λ−7)⁴ | sympy over ℤ |
| charpoly Δ₂ | λ(λ−4)⁵(λ−6)⁵(λ−10)(λ²−10λ+20)⁶ | sympy over ℤ |
| λ₁(Δ₀), λ₁(Δ₂) | 2, 5 − √5 | exact roots |
| ℤ₂ homological code | n = 60, k = 8, vertex-graph systole 6, dual-graph systole 4 | exhaustive simple-cycle enumeration |

## Verdicts, one row per assertion

Scope labels follow AGENTS.md §"Before declaring refuted": (a) = this
construction alone does not do what is claimed; (b) = structurally excluded,
with the invariant cited.

### 1. "The Pachner 2–2 flip is the braid relation σ₀σ₁σ₀ = σ₁σ₀σ₁."

**Refuted, scope (b).** Invariant: the 2–2 flip of a surface triangulation is an
F-move (the associator, a 6j-symbol), and Turaev–Viro invariance under it is
defined for every spherical fusion category, braided or not (Turaev–Virelizier
1006.3501; Balsam–Kirillov `library/arxiv-1004.1533v3`). `Vec_{S₃}` is a
spherical fusion category with no braiding, because S₃ is nonabelian
(`perm3_not_commutative`, Lean), so δ_g ⊗ δ_h = δ_{gh} and δ_h ⊗ δ_g = δ_{hg}
are non-isomorphic simples for some g, h. Flip invariance holds there with no
braid group in sight, so it cannot be the braid relation. In a braided category
the braid relation comes from the hexagon axioms and naturality, which relate R
to F; the two are distinct axioms that interact, and neither is the other.

### 2. "Turaev–Viro = RT(Z(C)) and Levin–Wen string nets apply to QOU at q₀."

**Scope (a), not established.** Both constructions need C to be spherical fusion:
finitely many simples, semisimple (Turaev–Virelizier; Levin–Wen
cond-mat/0404617; Bruguières–Virelizier, `library/arxiv-0812.2426v1`, recalling Müger's centre theorem). For
generic q the Hecke algebras H_n(q) are semisimple, but `Rep U_q(sl₂)` has
infinitely many simples V_n with nonzero quantum dimension, so it is not fusion.
The standard finite (fusion) quotient exists only when q is a root of unity.
`realGtOne_not_rootOfUnity` (Lean, `QOU/BringsSurface/RealQNotRootOfUnity.lean`) proves that a real q > 1, in particular
q₀ ≈ 1.10998, is not one. The implication "fusion quotient ⇒ root of unity" is
cited, not proved here.

What does transfer:
- the generic-q 6j-symbols and the pentagon/Biedenharn–Elliott identities
  (they hold for any q), so a *formal* state sum can be written down; at real q it
  has infinitely many labels, like Ponzano–Regge at q = 1, and is not known to
  converge;
- at a root of unity q = e^{iπ/κ} the corpus already has a truncation,
  `prop:root-of-unity-truncation` (`fluid-dynamics/`), and TV/RT apply to *that*
  truncated category. Relating its κ → ∞ behaviour to q₀ is a separate, open
  analytic question (volume-conjecture territory), not a consequence of TV = RT.

### 3. "Observables project onto triangulation cochains: Π₀ = tr_D(ψ) on vertices, Π₁(ψ)(w_e) = tr_D(ψ·w_e) on edges, face value = evaluate V₀; this is a chain map."

**Refuted as stated, scope (b) for two of its three parts.**
- *Edge values are not a 1-cochain.* A 1-cochain changes sign when its edge is
  reversed. Reversing an edge sends w_e to w_e⁻¹. From the Hecke relation alone,
  tr σ⁻¹ = tr σ − h·tr 1 (`trace_inverse_eq`, derived). With convention D,
  tr 1 = 1 and tr σ = q³/(q²+1), so tr σ + tr σ⁻¹ = (q⁴+1)/(q(q²+1)) > 0 for every
  q > 0 (`trace_add_inverse_conventionD_pos`). The edge assignment fails the
  cochain axiom at ψ = 1 already. Invariant: positivity of (q⁴+1)/(q(q²+1)).
  The obvious repair, antisymmetrising (tr(ψw_e) − tr(ψw_e⁻¹))/2, is a cochain but
  is a different proposal and has not been tested.
- *A constant face value is not a coboundary.* On a closed oriented surface the
  face–edge incidence has zero column sums (checked exactly on the Bring map:
  1ᵀ·d1 = 0), so Σ_f (dα)(f) = 0 for every 1-cochain α
  (`sum_coboundary_eq_zero`). A face value V₀ ≠ 0 on all 24 faces sums to 24·V₀,
  so Π₂ = d∘Π₁ is impossible (`const_eq_zero_of_coboundary`). Invariant:
  discrete Stokes. No chain map was exhibited in the essay; this shows none of
  the stated shape exists.
- *Gauge.* The sibling (#9415) proved that an inner automorphism θ maps the
  element W to its mirror without changing any trace. So an assignment of W
  versus its mirror to an edge is not detected by any trace observable: edge
  labels by these elements are not trace-observable data. Cited from #9415, not
  re-proved here.

- *Non-abelian replacement (owner question, 2026-11-25: Yekutieli's non-abelian
  Stokes instead).* Put group- or Hecke-valued holonomies on edges, with an
  edge reversed giving the inverse, and take path-ordered face holonomies (as in
  `QOU.MathlibExt.YekutieliIntegration.holonomy`). This map **is**
  well-defined. A vertex gauge conjugates each closed face holonomy
  (`gaugeHol_closed`). Any class function, Markov traces included, of a face
  holonomy is gauge-invariant and basepoint-independent
  (`classFun_gaugeHol_closed`, `classFun_basepoint`). What does **not** survive
  the trace is the Stokes relation: non-abelian Stokes relates *products* of
  face holonomies, and the trace of a product is not a function of the traces
  of its factors (`perm3_fixCount_product_not_determined`, S₃: factor traces
  (1, 1) give product traces 3 or 0). So the result is per-face trace
  observables with no linear "Π₂ = dΠ₁" among them. Only the abelian shadow
  gives back discrete Stokes. Lean: `QOU/BringsSurface/NonabelianStokesTrace.lean`
  (lean-direct exit 0, no `sorryAx`). Still open (`qou-b7fc`): the explicit
  closed-surface identity ∏_f (conjugated face holonomies) = ∏_{i=1}^{4} [A_i, B_i]
  on the Bring map, which needs a fundamental-polygon spanning tree.

### 4. "Bring's triangulation prevents Navier–Stokes blow-up."

**Scope (a). The parts that are true are generic; the part that is specific is false.**
- A finite-dimensional dissipative ODE on any finite complex has global
  solutions. That says nothing about the Clay problem, which is about smooth
  solutions on ℝ³ or T³. Bring's surface is two-dimensional, and 2D
  Navier–Stokes has global regularity classically (Ladyzhenskaya), so a 2D
  surface could not separate the two cases even in the continuum.
- λ₁ > 0 holds on any compact connected surface, and on any connected finite
  complex. On the Bring map λ₁(Δ₀) = 2 exactly; this is not an S₅ effect.
- "No ungapped zero mode" is **false for velocity**: dim ker Δ₁ = 8 = 2g. The
  eight harmonic 1-cochains are steady solutions of the linear Stokes problem
  that never decay.
- What survives is about **enstrophy**: harmonic modes have zero vorticity
  (d1h = 0), and every vorticity d1v has zero total (Stokes), so it is
  orthogonal to ker Δ₂ and decays at rate at least λ₁(Δ₂) = 5 − √5 under the
  linear part. That is true of every closed oriented surface with its own gap,
  and it is a statement about the linear part only.
- Cross-checked independently by the sibling session (PR #9430, probe
  `computations/probes/photon_jet_spectral/bring_map_hodge_probe.py`, generators
  S = (1 2 3 4), A = (0 1)): same counts, rank ∂₁ = 29, rank ∂₂ = 23, dim ker
  Δ₁ = 8, harmonic modes closed and co-closed. Its
  `QOU/BringsSurface/BringRegularMap.lean` (sorry-free, on #9430) proves the
  group facts: element orders 4/2/5, generation of S₅, coset indices 30/60/24,
  χ = −6, genus 4, and 240 (2,4,5) triangles. Cite that file for those facts.
  The Hodge kernel itself is exact-rank in both probes, not Lean.

### 5. "ℏ_q > 0 plays the role of the kinematic viscosity ν_q."

**A renaming the corpus already makes, not a derivation.** `q-navier-stokes.md`
*introduces* ν_q = ½(1 − q⁻¹) = ℏ_q/2 in the equation and calls it "an induced
parameter"; the Lean (`fluid-dynamics/q-navier-stokes.lean`) carries it as a
default field `viscosity : ℝ := (1 - q⁻¹) / 2`. The factor ½ is chosen. Searched:
`fluid-dynamics/`, `stochastic-mechanics/` (which mentions Nelson stochastic
mechanics) for a diffusion coefficient, η/s, or a horizon condition fixing ν. No
derivation found; this is a statement about the corpus searched, not a proof that
none exists. The natural candidate is Nelson's diffusion constant ℏ/(2m), which
has the same ½. In Nelson's theory, however, that constant governs an osmotic
term of an inviscid (Madelung) fluid, so the match would still need an argument.
In fluid/gravity, η/s = 1/4π is fixed by the horizon. The corpus has no
analogue.

**Follow-up from the ν_q child (PR #9434, bean `qou-0nqs`).** Generic Lean there
proves `energy_equality` (dE/dt = −νΩ), `lap1_harmonic` (harmonic fields are
steady) and `harmonic_circulation` (only advection changes harmonic
circulation). These match the DEC probe `bring54-dec-qns`. On ν it tested three
regularity conditions (`ViscosityRegularityRoutes.lean`):
- dissipation positivity leaves ν free;
- explicit-step stability on the q-ladder forces ν = 0;
- Habiro integrality excludes ℏ_q/2.

None forces ℏ_q/2, so item 5's verdict (a renaming, not a derivation) stands.
`TwistedHarmonicBound.lean` shows that any flat rank-r twist on Bring keeps
dim H¹ ≥ 6r.

### 6. "Bredberg–Keeler–Lysov–Strominger give holographic fluid dynamics without a metric."

**Overstated, scope (a).** Their bulk is flat Rindler space with a finite cutoff
surface: a metric bulk solving Einstein's equations (1101.2451). The result is
"Navier–Stokes from Einstein near a cutoff", not "without a metric".

### 7. The genuine link: HaPPY and {5,4}.

The HaPPY pentagon code (Pastawski–Yoshida–Harlow–Preskill 1503.06237) is built
on the {5,4} tessellation of the hyperbolic disc, and Bring's surface is a
compact quotient of {5,4}. Caveat: a compact quotient has no asymptotic
boundary, so HaPPY's bulk-to-boundary isometry has nothing to map to. What the
compact quotient does carry is a homological ℤ₂ code: n = 60 qubits on edges,
k = 2g = 8 logical qubits, with distances bounded by the vertex-graph systole 6
and the dual-graph systole 4 (exact, probe C8). That is an observation about the
Bring map. It needs the hyperbolic-surface-code literature before it is written
into the paper; that literature is not yet in `library/`.

## What is usable from the ingested papers

Owner question, relayed 2026-11-25: *"what is usable from the ingested papers?"*
Every row is grounded in the ingested text (`library/<doc-id>/sections/`; the
full text of the 11 new papers lives in `litlfred/qou-private` (PR #2) under the
same paths, per the owner ruling of 2026-11-25; public qou keeps their metadata), page
numbers from the section front matter), and every quote was spot-checked.
"Use" is one of cite / Lean-formalise / compute / scope-limit.

| Paper | Usable part (section, pages) | Use | Attaches to | Does not apply at real q₀, because |
|---|---|---|---|---|
| Turaev–Virelizier 2010 (`arxiv-1006.3501v5`) | Thm 11.1, §11, pp. 34–35: TV = RT(Z(C)) for spherical fusion C, dim C ≠ 0. Appendix 6j-symbols, pp. 69–70 (pre-fusion layer) | cite; scope-limit | `fluid-dynamics/root-of-unity-truncation.md`; `qou-r4ky` | §4.2, pp. 10–13: fusion = finitely many simples; the state sum (§5.2, pp. 13–14) needs a finite representative set. At q₀ the category is pre-fusion with infinitely many simples. It is also a 3-manifold invariant, not a surface one |
| Levin–Wen 2004 (`arxiv-cond-mat-0404617v2`) | §4.2, pp. 6–8: exactly soluble Hamiltonian for every (F, d) satisfying the pentagon and unitarity | cite (source of the string-net hypotheses) | `qou-r4ky` | needs N+1 labels (finite) and Σd_i² finite (§4.2); trivalent nets (§3, pp. 3–4). The Bring map is 4-valent |
| Pastawski–Yoshida–Harlow–Preskill 2015 (`arxiv-1503.06237v2`) | §3, pp. 8–11, Thm 1: the pentagon-tiling network is a bulk-to-boundary isometry on {5,4}. §4.1, pp. 11–13, Thm 2 (Ryu–Takayanagi) | cite; scope-limit | `qou-r43g` | Thm 2 assumes a simply connected planar network with a boundary (§4.1). Bring is closed, genus 4. Our [[60,8]] is a homological code, not HaPPY; QOU has no perfect tensors |
| Bhattacharyya–Hubeny–Minwalla–Rangamani 2008 (`arxiv-0712.2456v4`) | §4.5, p. 24: η/s = 1/4π from the bulk; §6, p. 34: second-order coefficients | cite (example of a *derived* viscosity) | `qou-0nqs`; `fluid-dynamics/q-navier-stokes.md` | input is AdS₅ gravity with a conformal boundary (§2, pp. 6–9). QOU has no bulk metric or horizon area |
| Bredberg–Keeler–Lysov–Strominger 2011 (`arxiv-1101.2451v2`) | §4, pp. 5–7: a smooth horizon *forces* η = r_c ("any value … other than (12) … singularity") | cite (shape of argument for `qou-0nqs`: viscosity fixed by regularity) | `qou-0nqs` | Minkowski region inside a cutoff Σ_c (§1, pp. 3–4); r_c has no counterpart in q. It assumes NS existence and uniqueness (§5.4, p. 10), so it says nothing about regularity |
| Mohamed–Hirani–Samtaney 2016 (`arxiv-1508.01166v2`) | §3.3, pp. 10–16: DEC NS scheme on surfaces; §5, pp. 29–32: exact discrete conservation of mass and vorticity | compute (operator template for `qou-k5jb`) | `qou-k5jb` | needs a pairwise-Delaunay simplicial mesh with circumcentric stars (§3.1, pp. 7–8), and it is float numerics. **Caveat for our use:** its stream-function form U = ∗d∗dΨ makes every velocity coexact, so on genus 4 it drops the 8 harmonic modes. The paper does not discuss topology |
| Grans-Samuelsson–Jacobsen–Saleur 2020 (`arxiv-2010.12819v2`) | §2.4, pp. 10–11: Koo–Saleur generators from TL e_j; §8, p. 36: commutators converge only up to an anomalous central term, which the paper leaves conjectural | scope-limit; cite | `braids-and-knots/tl-is-the-xxz-chain.md`; sibling #9415/#9430 | q = e^{iγ} on the unit circle (§2.2, pp. 8–9). At real q₀ > 1 the XXZ chain is massive, so there is no Virasoro continuum limit |
| Chmutov–Lando 2007 (`arxiv-0704.1313v1`) | Introduction, pp. 1–3: an invariant is mutant-blind iff its weight system depends only on intersection graphs; Jones/HOMFLY are mutant-blind. §4, pp. 7–8, Thm 3: sl(2) weight systems | scope-limit: any mass or binding assignment built only on Jones/HOMFLY traces cannot separate mutant knots | `mass-theory/vassiliev-filtration-mass-tower.md` (calls c₂ "mass-discriminating") | it *does* apply at q₀, and that is the point. It covers oriented knots only (Introduction), so not links such as Borromean or Hopf. Follow-up (compute child, bean `qou-63be`): no trace-only mass assignment in the corpus claims to separate mutants. One real error, in `intro-mutant-jones-bloch-group.md` (Vol(KT) ≠ Vol(Conway), contrary to Ruberman), is fixed on branch `claude/mutant-volume-fix-20261125`, which cites Chmutov–Lando Thm 3 |
| Ciubotaru–He 2014 (`arxiv-1409.0902v1`) | §1.2, pp. 2–4, Thm 1.1(1): basis of the rigid cocenter; §1.3, p. 4, Thm 1.3(1): trace map injective for admissible q | cite (for the sibling's cocenter thread) | `braids-and-knots/affine-hecke-homology-prior-art.md`; sibling #9415 | admissibility holds (Def 6.5, §6.3, pp. 14–15: "q ∈ ℂ× has infinite order"), but the theorems concern the *affine* Hecke algebra. QOU's finite H_n(q) is semisimple and its cocenter is already the block traces |
| Fortier Bourque–Petri 2023 (`arxiv-2302.02540v3`) | §9.2, pp. 33–36: m₁(Bring) ≥ 4 from S₅ representations; §8.2, pp. 26–28, Table 3: genus-4 λ₁ bounds | cite; compute: decompose the probe's exact eigenspaces into S₅ irreducibles | `brings-surface/brings-smoothness.md`; sibling #9415 | Laplace–Beltrami on the hyperbolic metric via Selberg (§1, pp. 1–3). It does not bound our combinatorial λ₁(Δ₀) = 2 or λ₁(Δ₂) = 5 − √5, and it notes the 1.91556 is "not rigorous" |
| Mårdby–Rowlett 2024 (`arxiv-2406.18369v2`) | §2.1, pp. 4–12, Thm 2.5 (Weyl's law); §4.2, pp. 17–33 (χ is a heat invariant) | cite only, as background | none | continuum and asymptotic in λ → ∞; a 30/60/24-dimensional operator has no such limit. Nothing Bring-specific |
| Riera–Rodríguez 1992 (`pjm-v154-n1-p09-s`) | PDF pp. 3–5 (journal pp. 180–182): integral S₅ action on H₁(B,ℤ) by 8×8 matrices, "twice the following irreducible representation" (PDF p. 5); Thm 1, PDF p. 7 | compute: check that the probe's 8 harmonic cochains carry 2 × (4-dim irreducible); Lean: the integer matrix identities | `nuclear-interactions/x5-bring-prym-jacobian.md`; probe; `qou-b7fc` | the period matrix and τ are complex-analytic, fixed by a transcendental (Schottky) equation (PDF p. 2), unrelated to q₀. Only the topological H₁ action transfers |
| Braden–Northover 2012 (`arxiv-1206.6004v2`) | §4.2, pp. 7–9: explicit change of basis to the RR basis; §4.4, pp. 12–15; §5.3, pp. 17–19: unique invariant spin structure | compute: express the [[60,8]] logical basis in the RR basis; Lean: the spin-structure count is finite ℤ₂ arithmetic | `nuclear-interactions/x5-bring-prym-jacobian.md`; `qou-r43g`; `qou-b7fc` | τ₀ and the Riemann constants come from floating-point Maple output (`extcurves`, §4.4), so they are not admissible as QOU numbers. The paper has no q |
| Cook 2021 thesis (`210811825v1`) | App. E, pp. 144–150: FreeFEM λ₁ ≈ 1.91556, multiplicities 6, 5, 5, 5, 4, 6, …; GAP gives the full symmetry group C₂ × S₅, order 240 | cite as numerical, non-rigorous data; qualitative multiplicity comparison | `brings-surface/brings-smoothness.md` (already cites it); sibling #9415 | continuum finite-element computation in floating point, conjectural by its own account. **Do not equate 1.91556 with our combinatorial λ₁(Δ₀) = 2**: they are different operators |

Net: nothing in the 14 papers makes TV/RT, string nets, HaPPY holography or
fluid/gravity apply at q₀ as stated. What is usable:
1. Citations that scope those claims.
2. Mohamed et al. as the DEC template, which needs a harmonic-mode fix on genus 4.
3. The Riera–Rodríguez / Braden–Northover integer H₁ data, as an exact S₅ cross-check on the probe.
4. Chmutov–Lando's mutant-blindness, as a scope limit on trace-only mass assignments.

## What the paper can take

1. Citations: Turaev–Virelizier, Levin–Wen, Pastawski et al., Bhattacharyya
   et al., Bredberg et al., Mohamed–Hirani–Samtaney (DEC Navier–Stokes), and the
   Bring-surface spectral papers (Bourque–Petri, Mårdby–Rowlett), all ingested on
   this branch.
2. A scope-limited remark: TV/RT/string-net constructions apply only at a root
   of unity, where `prop:root-of-unity-truncation` lives; at q₀ they do not
   apply as stated.
3. The exact Bring cochain data (table above) as a computational fact with a
   witness.
4. A DEC q-NS probe on the Bring map (Mohamed et al.'s scheme, exact or mpmath)
   as a follow-up. It would measure decay rates of the linearised flow, and is
   framed as a model computation, not as evidence about 3D regularity.

## What remains open

- Whether an antisymmetrised trace assignment gives a chain map, and from which
  complex.
- Any derivation of ν_q from the substrate.
- The κ → ∞ relation between root-of-unity TV data and q₀.

## Verification

- Lean: `lean -DautoImplicit=false -s 65536 QOU/BringsSurface/TraceCochainObstructions.lean`
  against the restored olean cache, exit 0. `#print axioms` on all six exported
  theorems lists only `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`.
- Probe: 11/11 checks; `scripts/precision-gates.sh --changed`: all blocking
  gates green.
- Library: the 11 cited papers are ingested (`library/arxiv-1006.3501v5`,
  `arxiv-1503.06237v2`, `arxiv-cond-mat-0404617v2`, `arxiv-0712.2456v4`,
  `arxiv-1101.2451v2`, `arxiv-1508.01166v2`, `arxiv-2302.02540v3`,
  `arxiv-2406.18369v2`, `arxiv-0704.1313v1`, `arxiv-1409.0902v1`,
  `arxiv-2010.12819v2`). `library-ingest-fidelity-probe.py`: recall 100 % for
  ten, 92.3 % for cond-mat/0404617. The claims quoted in items 1, 6 and 7 were
  checked against the ingested text (Turaev–Virelizier assume spherical fusion;
  Bredberg et al. start from the flat Rindler metric; HaPPY tiles by pentagons,
  four per vertex).

## Beans

Epic `qou-qrrb`; tasks `qou-k5jb` (DEC probe), `qou-b7fc` (antisymmetrised
trace, open), `qou-0nqs` (ν_q derivation, open), `qou-r43g` (surface-code
literature), `qou-fzdu` (licence decision), `qou-r4ky` (scope remark, needs
owner approval).
