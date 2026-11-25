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
cond-mat/0404617; Müger's centre theorem, `library/arxiv-0812.2426v1`). For
generic q the Hecke algebras H_n(q) are semisimple, but `Rep U_q(sl₂)` has
infinitely many simples V_n with nonzero quantum dimension, so it is not fusion.
The standard finite (fusion) quotient exists only when q is a root of unity.
`realGtOne_not_rootOfUnity` (Lean) proves that a real q > 1, in particular
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
- Sibling #9415 is proving dim ker Δ₁ = 8 independently; results were exchanged.

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
