# PRE-REGISTRATION: coideal (quantum-symmetric-pair) colour on (ℂ³)^⊗n (bean `qou-ni4b`)

Written and pushed before any probe code exists. Date 2026-11-22.

## Question

Earlier results on this branch:

- `qcd_colour_action/`: in the K4 class (strand-wise Hopf colour commuting with the crossing and
  carried with the strand, together with flavour), the braid relation forces q² = 1.
- `qcd_colour_full_tower/` and `qcd_d_residual_symmetry/`: convention D is the rank-2 twisted trace
  on (ℂ³)^⊗n. Its stabiliser is the Levi U_q(gl₂)×U(1), and the colour singlets lie in its radical.

The survey `qcd_colour_full_tower/LITERATURE.md` §F names one route past q² = 1: a coideal
subalgebra B ⊂ U_q(gl₃) of a quantum symmetric pair (Letzter, math/0103228; Balagović–Kolb,
arXiv:1507.06276; Kolb, math/0512581). B is not a Hopf subalgebra, and its natural braid partner is
the type-B (cylinder) braid group with a K-matrix. This probe asks whether such a B gives colour.

## Corpus check (done before writing this)

- `corpus-search` for "coideal reflection equation K-matrix type B cylinder", and separately for
  each term, at `--limit 200` (run from the main checkout). There were 0 seeds, except "type B",
  whose 24 ingested hits are unrelated.
- grep of `folio/`, `computations/`, `docs/audits/` and `beans/defs/` for coideal, reflection
  equation, K-matrix, cylinder braid, Letzter, Balagović and Kolb. Hits:
  - "Joseph–Letzter centre" in `q-casimir-unique` (unrelated);
  - `docs/audits/2026-11-15-colour-stabilizer-bridge.md` l.239: sl₃ ⊂ g₂ is not a symmetric pair,
    so the coideal framework "does not apply directly" there. That concerns g₂, not gl₃;
  - bean `qou-ni4b` names the coideal route as open.
- library: `INDEX.md` has no hit. One reference-list mention of "reflection equation" in
  `104171-rmi-1356`, which is not a source on the topic.
- So no prior computation exists. This is new work, not a re-derivation.

## Setting (fixed in advance)

- V = ℂ³ with the Jimbo U_q(gl₃) action. Coproduct variant B, the one used by the sibling probes:
  - Δ(E_i) = E_i⊗1 + K_i⊗E_i
  - Δ(F_i) = F_i⊗K_i⁻¹ + 1⊗F_i
  - S(E) = −K⁻¹E, S(F) = −FK.
  This is Kolb's convention.
- Ř = `jimbo_R(3, upper=True)`, reused from `qcd_colour_full_tower`.
- Exact sympy over ℚ(q, c₁, c₂). No float, and q₀ is not used.
- Coideal generators, standard form B_i = F_i − c_i·T_{w_X}(E_{τ(i)})·K_i⁻¹ (+ s_i K_i⁻¹), with
  X = ∅ and s_i = 0 in both cases:
  - **AI**, (gl₃, so₃): τ = id, so B_i = F_i − c_i E_i K_i⁻¹, i = 1, 2. No Cartan part.
  - **AIII/AIV**, (gl₃, gl₂⊕gl₁): τ = the diagram flip, so B₁ = F₁ − c₁E₂K₁⁻¹ and
    B₂ = F₂ − c₂E₁K₂⁻¹. The Cartan part is K₁K₂⁻¹ (plus the gl₃ centre, which is a scalar on Vⁿ).
- c_i is left **free** (symbolic). No value of c is chosen to meet a target.
  - Any test result that holds only at a chosen c is reported as a function of c, and it is labelled
    a selection if it matches a target.
  - c = 0 (the Borel half) is reported separately and is not counted as a coideal.

## Candidates and tests

**Q1: coideal action on (ℂ³)^⊗n through Δ.**

- (Q1a) Coideal property on the module: Δ(B_i) equals B_i⊗K_i⁻¹ + 1⊗F_i − c_i K_{τi}K_i⁻¹⊗E_{τi}K_i⁻¹
  as 9×9 matrices. Its first legs lie in B: for AI, K_iK_i⁻¹ = 1; for AIII, K₂K₁⁻¹ ∈ B.
- (Q1b) Δ^n(b) commutes with every σ_i, n = 2, 3.
- (Q1c) Transport: the q → 1 limit of Ř is P.

**Q2: K-matrix and the type-B (cylinder) action.**

- (Q2a) The commutant of B on ℂ³.
- (Q2b) For a non-scalar J in that commutant:
  - J satisfies the reflection equation Ř(J⊗1)Ř(J⊗1) = (J⊗1)Ř(J⊗1)Ř on V⊗V;
  - t = J⊗1⊗… commutes with Δⁿ(B), n = 2, 3;
  - the minimal polynomial of J;
  - so ⟨t, σ_i⟩ is a type-B Hecke action that commutes with B.
- (Q2c) B-invariant twists:
  - the space of T ∈ End(V) with ad*_b(T) = ε(b)T (the dual adjoint action, as in the sibling);
  - the same space on V⊗V;
  - whether any product T⊗T other than (pivotal)⊗(pivotal) is B-invariant.
- (Q2d) Product twist G = T₁⊗g^{⊗(n−1)}, with T₁ B-invariant on V and g the gl₃ pivotal
  diag(q⁻⁴, q⁻², 1). On H₃, test:
  - whether φ_G(x) = tr(Gx) is a trace;
  - its Markov behaviour on the type-A part (adding strands at the end);
  - whether it vanishes on the three-row block, which is D's radical.
- (Q2e) For each rank-2 D twist (supports {1,2}, {1,3}, {2,3}, values from the full-tower probe),
  solve ad*_b(T_S) = ε(b)T_S over c. The question is whether some coideal B_c stabilises the D
  functional.

**Q3: the sibling acceptance tests (a)–(f)**, from `qcd_colour_action/PREREGISTRATION-colour-action.md`,
applied to B on (ℂ³)^⊗3 at generic q:

- (a) The colour action is injective and is su(3): 8 independent operators with the sl₃ brackets.
  Measured by the dimension and the type of the Lie algebra spanned at q = 1 by the B generators.
- (b) It commutes with σ₁, σ₂.
- (c) Ř satisfies the Hecke and braid relations.
- (d) This is adapted, because there is no flavour factor here. It passes if some B-invariant Markov
  twist gives z = z_D = q³/(q²+1) on the type-A part. The Hecke action on the B-singlet sector of
  (ℂ³)^⊗3 is recorded.
- (e) The B-invariant subspace of (ℂ³)^⊗3 is 1-dimensional. The B-invariants of V⊗V are recorded:
  an su(3) colour has none.
- (f) Transport.

**Q4: what counts as colour (fixed now).** Colour passes only if B, at generic q, is a deformation
of an 8-dimensional sl₃ (su(3)). Measured by the q → 1 Lie closure: dimension 8, simple.

- An algebra of dimension 3 (so₃) or 4 (s(gl₂⊕gl₁)) is **not** colour.
- Calling it colour is a FAIL, whatever else passes.

## Predictions

- Q1a, Q1b, Q1c: PASS for both. (b) is structural: B ⊂ U_q(gl₃), and Δⁿ(U) commutes with Ř
  (Jimbo duality). It is therefore a sanity check, not a finding.
- Q2a:
  - AI: the commutant of B on ℂ³ is scalars only (so₃ acts irreducibly on ℂ³). So there is no
    non-trivial commuting K-matrix. The AI K-matrix is τ₀-twisted, and that twisted version is not
    tested.
  - AIII: the commutant is 2-dimensional, {1, J} with J non-diagonal.
- Q2b (AIII):
  - J satisfies the reflection equation, possibly only after a normalisation of J. Any constraint
    linking J's entries to c is reported.
  - J⊗1 commutes with Δⁿ(B).
  - J has 2 distinct eigenvalues, so the action is a type-B Hecke algebra.
- Q2c:
  - AI: the B-invariant twists on V are 1-dimensional (the pivotal).
  - AIII: 2-dimensional.
  - On V⊗V, only twists whose later strands are pivotal are invariant. The only invariant product
    T⊗T is g⊗g, up to scale.
- Q2d: on the type-A part, adding strands with g gives z₃ = q³/[3]_q, not z_D. If φ_G is a trace at
  all, the first-strand twist only contributes the second, type-B parameter.
- Q2e: no c ≠ 0 makes a rank-2 D twist B-invariant, for AI or for AIII.
- Q3:
  - (a) FAILS for both: the q → 1 Lie closure has dim 3 (AI) or 4 (AIII), not 8.
  - (b), (c), (f) PASS.
  - (d) FAILS (no z_D).
  - (e): AI gives dim 1 in V^⊗3, but also dim 1 in V^⊗2, which su(3) does not have. AIII gives
    dim > 1 in V^⊗3, classically 3.
- Q4: FAIL for both. B is not colour.

## Known coincidences declared in advance (not evidence)

1. AIII's classical fixed algebra gl₂⊕gl₁ has the same shape as the D residual U_q(gl₂)×U(1).
   Matching shape is not a derivation. A coideal (non-Levi) version of the same 2+1 breaking is
   still broken colour.
2. The so₃ invariants of V^⊗3 are 1-dimensional (the ε tensor), which is the same count as the
   SU(3) baryon. This is a coincidence of n = 3. so₃ also has an invariant in V⊗V.
3. If any trace quantity depends on c, or on a twist ratio, and equals z_D at a particular value,
   that is selection against the target, not a result.

## Decision rule

- B closes `qou-ni4b` only if it meets Q4 and (a)–(f) exactly over ℚ(q, c), for c in an open set.
  Otherwise the result is a scope-(a) negative for the searched class: Letzter coideals of
  U_q(gl₃) of types AI and AIII, s = 0, acting on ℂ³ through Δ.
- A scope-(b) label is used only where a proved invariant is cited, for example the classical
  dimension of the fixed-point algebra.
- The gluon stays open. Nothing here selects one.
