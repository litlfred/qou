# Uploaded-papers sweep → binding / mass derivation gap-closing ideas (2026-07-18)

**Tier:** coordination / survey (scope-(a); no fit; nothing wired). Twelve papers uploaded
2026-07-18 (`library/`, 14:46 UTC batch) deep-read and mapped against the open binding /
mass derivation gaps. Corpus-grep checklist run for every idea (greps over `docs/audits/`,
`docs/coordination/`, `content/`, `computations/`); everything already tried or closed is
cited, not re-proposed. The only computations run were one-line decisive checks (a
j-invariant digit check, a sextic root, an η-quotient verification, an exact
Vol(𝓑₃) confirmation); no wide searches, no fits.

## The papers

### Cluster A — Bring's curve geometry

| File | Paper |
|---|---|
| `the-period-matrix-of-bring-s-curve-1hik02mwva.pdf` | Riera–Rodríguez 1992 (RR92), *The period matrix of Bring's curve*, Pacific J. Math 154(1) 179–200 |
| `sigma12-065.pdf` = `1206.6004v2.pdf` | Braden–Northover (BN12), *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, SIGMA 8 (2012) 065 |
| `2402.08782v1.pdf` | Kattan–Singerman 2024 (KS24), *Hecke–Farey coordinates for Bring's surface* |
| `2208.13692v1.pdf` | Braden–Disney-Hogg 2022 (BDH22), *Bring's curve: old and new* |

### Cluster B — 3D-index / complex Chern–Simons

| File | Paper |
|---|---|
| `1108.4389v1.pdf` | Dimofte–Gaiotto–Gukov (DGG), *Gauge Theories Labelled by Three-Manifolds* |
| `1112.5179v1.pdf` | DGG, *3-Manifolds and 3d Indices* |
| `1208.1663v2.pdf` | Garoufalidis (+ Zwegers), *The 3D index of an ideal triangulation and angle structures* |
| `1303.5278v1.pdf` | GHRS, *1-efficient triangulations and the index of a cusped hyperbolic 3-manifold* |
| `1604.02688v1.pdf` | GHHR, *The 3D-index and normal surfaces* |
| `1411.6062v2.pdf` | Garoufalidis–Kashaev (GK), *Evaluation of state integrals at rational points* |
| `2012.00062v3.pdf` | Garoufalidis–Gu–Mariño (GGM), *Peacock patterns and resurgence in complex Chern–Simons theory* |

## Already in-flight today (not re-proposed)

- DGG tetrahedron-index triality pinned + 4₁ 3D-index gluing closed
  ([`2026-07-18-tetrahedron-index-triality-pin.md`](2026-07-18-tetrahedron-index-triality-pin.md),
  [`2026-07-18-figure-eight-3d-index-closed.md`](2026-07-18-figure-eight-3d-index-closed.md); PR #3805 lineage).
- 5₂ exact-Z Theorem-22 blocks (main commit `57f97aed`); odd-channel geometric search CLOSED
  ([`2026-07-18-qbeta-odd-channel-cornering-capstone.md`](2026-07-18-qbeta-odd-channel-cornering-capstone.md)).
- Bring Jacobian Epstein det′Δ θ-factorization (PR #3934, unpolarized);
  [`2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md`](2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md)
  (BDH22 Thm 2.12 / Prop 4.6 deep-read).
- Δ_λ attack-vector map ([`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md)):
  sign derived, magnitude reduced to one scalar `m ∈ (0, 1/√5)`; Vector 2 (icosahedral `1/√5`
  S-matrix bridge) flagged highest value.
- W_λ geometric value-map search CLOSED
  ([`2026-07-17-wlambda-geometric-route-closed-real-gap-is-leg-b.md`](2026-07-17-wlambda-geometric-route-closed-real-gap-is-leg-b.md)) —
  nothing here reopens it. The 8we6 "H₄" closure
  ([`2026-07-18-8we6-h4-connected-sigma2-route-closed.md`](2026-07-18-8we6-h4-connected-sigma2-route-closed.md))
  concerns the 4-strand **Iwahori–Hecke algebra** H₄(q); KS24's **Hecke group** H₄ = C₂∗C₄ is a
  different object — no conflict.

---

## Executive synthesis — top cross-cluster leads

1. **Vector-2 double pincer on the Δ_λ magnitude scalar `m`** (ideas A5 + B4). Two cheap,
   falsifier-first, exact computations attack the same `1/√5` from opposite sides: the Bring
   real-structure/involution spectrum vs the `{±√5, ±1}` exchange spectrum (one page of
   integer linear algebra — with the naive Gram identification *already refuted by
   inspection*, `spec(G²) = {5,5,1,1} ≠ {5,5,5,1} = spec(c)`), and the Garoufalidis–Kashaev
   exact ζ₅ evaluation whose Cor 1.2 carries an explicit `1/√5` prefactor from a finite Gauss
   sum. If both land, the magnitude ceiling is tied to level-5 geometry from two independent
   directions; KS24's level-5 congruence parallelism (icosahedron = M₃(5), Bring = M₄(5))
   is the candidate common origin (idea A7).
2. **I_𝓑₃ — the Borromean 3D-index** (idea B1). The nucleon carrier's index is well-defined
   (GHRS Rmk 1.10 + Thm 1.5), computable on today's validated `J_Δ` machinery (8 tetrahedra,
   ℤ⁵ lattice sum, ℤ⁶ peripheral grading = per-cusp quantum numbers), and appears in neither
   the corpus nor, apparently, the cited literature. First integer-count invariant of 𝓑₃.
3. **The Γ₀(5) hauptmodul gate `t₅(τ₀) = −10` + polarized det′Δ on `τ_B = τ₀(5I−J)`**
   (ideas A2 + A1). RR92 Thm 1 proves the residual gauge on Bring's modulus is Γ₀(5); this
   session verified the genus-0 hauptmodul takes the *exact rational value* −10 at τ₀ (Fricke
   partner −25/2 = j(5τ₀)). Any q₀ ↦ τ dictionary (the open input named in
   [`2026-07-18-alpha-em-tau-correspondence.md`](2026-07-18-alpha-em-tau-correspondence.md))
   is physical only through Γ₀(5)-invariants and must land on t₅ = −10 — a discrete,
   parameter-free gate in the style of `144·C(n)`. And BDH22 Thm 2.12's symplectic form
   `τ₀·(5I−J)` (spectrum {1,5,5,5}) is exactly the principally-polarized object PR #3934's
   unpolarized computation says is missing.
4. **Collective binding term as a normal-surface generating series** (idea B3). GHHR Cor 8.2
   writes the index as a sum over embedded normal-surface classes graded by `−χ(S*)+δ(S*)` —
   genuinely many-body (a surface spans many tetrahedra), and carrying per-cusp boundary
   grading that **can** distinguish (Z,N) where the Slater-antisymmetrizer trace (A-only,
   pn-blind by proved invariant) cannot. Shape-matches the #3943 collective residual.
5. **Angle-structure LP ↔ confinement SDP dual dictionary** (idea B2). Casson–Rivin duality
   pairs the angle polytope with the normal-surface cone (GHHR Prop A.3 is literally a
   Gauss–Bonnet LP-duality pairing); the repo's mandated LP/SDP dual infra is the ready-made
   consumer. A count-level falsifier decides it in an afternoon.

---

## Cluster A — ranked ideas (Bring's curve)

### A1. Polarized photon determinant on the canonical symplectic Riemann matrix τ_B = τ₀·(5I−J)
- **Target gap:** α_EM `1/(8π)` magnitude leg / calibration-H¹ structure.
- **Paper evidence:** BDH22 Thm 2.12 (τ_B = τ₀·M_S, M_S = 5I−J, symplectic; spectrum {1,5,5,5});
  Prop 4.6 + remark (the E₂³×E₁ block form is **not** symplectic; a Jacobian's canonical ppav is
  irreducible); BN12 eq (4.2) explicit 8×8 basis change; RR92 §4 θ-factorization machinery
  (mᵗcm = diag(5,5,5,1); lattices L₁, L₂ of index 2; each θ summand = product of three
  θ(·;5τ) and one θ(·;τ)).
- **Corpus status:** open and *named* — PR #3934 computed the **unpolarized** isogeny-block
  det′Δ (7.00188·10⁻²⁶; raw measure ≈ 1.472·10¹² is not 8π-shaped) and the bring-s4 audit
  lists the polarized determinant as the honest replacement. Nobody has used τ₀·(5I−J).
- **Next probe (formalize-first):** 5I−J diagonalizes over ℚ ((1,1,1,1) ↦ 1; std-rep 3-space
  ↦ 5), so the heat-kernel θ splits into a 1-dim τ₀-mode and a 3-dim 5τ₀-isotypic block
  *inside the polarized lattice* — no 8-dim grid, no Siegel reduction; RR92 §4's L₁/L₂
  bookkeeping gives the exact θ-characteristic sum. Compare against #3934's unpolarized
  1.472·10¹²; the delta measures the polarization contribution.
- **Risk:** the photon is a 1-form (analytic torsion) — scalar det′Δ still needs the 1-form
  dressing; and "8.226 ≈ 8" stays recorded-not-interpreted per the bring-s4 STRICT guard.

### A2. The W-plane modulus is a point of X₀(5); its invariant coordinate is exactly rational: t₅(τ₀) = (η(τ₀)/η(5τ₀))⁶ = −10
- **Target gap:** q₀ substrate derivation / CAL-2 modulus pinning / calibration-H¹ structure.
- **Paper evidence:** RR92 Thm 1 (stabilizer of Bring's half-plane in Sp(8,ℤ) is
  SpS₅ × SpΓ₀(5), Möbius on τ; τ unique mod Γ₀(5)); Thm 2 + BDH22 §2.2 (τ₀ fixed by
  j(τ₀) = −121945/32, j(5τ₀) = −25/2; τ₀ transcendental by Schneider). Session check: the
  sextic (t²+250t+3125)³ + (121945/32)·t⁵ = 0 has real root **t = −10 exactly**; η-quotient
  at τ₀ ≈ −0.5+0.186676i confirms (−9.99998, residual = 6-d.p. truncation of τ₀).
  Corollary: the bring-s4 audit's per-factor measure ratio is algebraic,
  m(τ₀)/m(5τ₀) = √5·10^(−1/3) = 1.03789… — the 4-factor product reduces to **one**
  transcendental (η(5τ₀)) times exact algebraic data.
- **Corpus status:** open. No corpus object carries the Γ₀(5)-gauge statement, the
  hauptmodul, or any numeric τ₀; today's alpha-em-tau-correspondence audit names the
  q₀ ↔ period dictionary as the open DOF with no gauge constraint.
- **Next probe (formalize-first):** a Lean lemma / conditional class: *any q₀ ↦ τ dictionary
  is physical only through Γ₀(5)-invariants and must land on the class t₅ = −10* (cite RR92
  Thm 1). Discrete gate, `144·C(n)`-style: a candidate dictionary missing t₅ = −10 is refuted
  with no precision search. Also collapses the "compute Bring τ" unowned sub-step
  ([`2026-07-17-alpha-em-keystone-shared-bring-tau.md`](2026-07-17-alpha-em-keystone-shared-bring-tau.md)):
  τ₀ is published; record it in a witness.
- **Risk:** τ₀ itself has no closed form (transcendental) — only its invariants are exact;
  conflating the two re-imports the precision trap.

### A3. Integer-trace prune: the lever-1 "SL₂(ℤ) monodromy" framing is impossible — tr B = 2.6424 ∉ ℤ
- **Target gap:** W-plane / lever-1 binding kernel periphery (tr B target).
- **Paper evidence:** RR92 Thm 1 + BN12 §5.2: automorphisms/monodromies act on H₁(B,ℤ) by
  **integer** symplectic matrices (entries 0,±1); any elliptic-surface Gauss–Manin monodromy
  is in SL₂(ℤ), whose traces are integers.
- **Corpus status:** the inconsistency is live in
  [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
  ("M ∈ SL₂(ℤ) … char. poly x²−(tr M)x+1" next to tr = 2.6423863,
  [`2026-06-24-lever1-trB-geometric-target.md`](2026-06-24-lever1-trB-geometric-target.md)).
- **Next probe:** five-line Lean lemma (integer matrix ⇒ integer trace ⇒ no M ∈ SL₂(ℤ) with
  char-poly x²−2.6424x+1) + re-scope of the E(q) sub-question: the family realizing
  tr M(q₀) = 2.6424 is a real-analytic **SL₂(ℝ) transfer-matrix** family, not the integral
  monodromy of an algebraic elliptic surface. Prunes the whole "search algebraic elliptic
  fibrations / modular monodromies for trace 2.6424" class before anyone runs it. Legitimate
  scope-(b) with cited invariant; **re-scope the 2026-06-24 audit, don't delete it**.
- **Risk:** none to correctness; possibly the older audit meant SL₂(ℝ) informally.

### A4. X₀(50) enters the corpus: C₁ = B/⟨(12)(34)⟩ *is* X₀(50); the W-plane curves are the conductor-50 ℚ-isogeny class 50a
- **Target gap:** calibration-H¹ structure + the lever-1 E(q) family (indirectly q₀).
- **Paper evidence:** BDH22 §4.3 eq (10) (C₁: B² = A⁶+4A⁵+10A³+4A+1, the RR92 genus-2
  quotient, is a model of X₀(50)); Prop 4.5 (Jac of the P⁴ model is ℚ-isogenous to (50a)⁴;
  50b/50a merge over ℚ(√5)); §2.2 (full ℚ-isogeny class with periods τ₀, 3τ₀, 5τ₀, 15τ₀;
  j(3τ₀) = 5·211³/2¹⁵, j(15τ₀) = −5²·241³/2³).
- **Corpus status:** X₀(50) appears only as one line in today's bring-s4 audit; no witness, no
  block, no use of the modular parametrization. Keystone-ledger inoculation #4 (cyclotomic /
  period-axis trap, twice re-walked) is respected by targeting the **archimedean W-plane /
  calibration axis**, not the keystone coupling.
- **Next probe (formalize-first):** gate first — a modular W-plane family E(q) must carry the
  50a newform's **integer** Hecke data (a_p list + Atkin–Lehner signs w₂, w₅): discrete,
  parameter-free pass/fail. Bounded first computation: check whether any corpus object (e.g.
  lever-1 recurrence coefficients at special q) reproduces those integers; if none, record
  the negative and stop.
- **Risk:** highest numerology-adjacency in Cluster A — mitigated by the integers-only,
  gate-first framing (no continuous matching).

### A5. Vector-2 falsifier: exact spectral audit of the [1⁴] exchange matrix G against Bring's S₅ period data
- **Target gap:** Δ_λ magnitude scalar `m ∈ (0, 1/√5)` (attack-map Vector 2).
- **Paper evidence:** RR92 §2: the S₅-equivariant Gram is **unique up to scale**
  (c = [[4,1,−1,1],[1,4,1,−1],[−1,1,4,1],[1,−1,1,4]], spectrum {5,5,5,1}, det 125);
  mᵗcm = diag(5,5,5,1); BDH22 Prop 4.4 (M′ = 5M⁻¹ integral); 50a/50b merge over ℚ(√5);
  BN12 explicit real structure (anti-involution matrix S′ on homology) and intersection form C.
- **Corpus status:** Vector 2 open (declared today); the Bring-side √5 objects have never been
  compared to the #3924 exchange matrix G.
- **Next probe (falsifier-first, already partially executed):** exact spectra:
  spec(G) = {±√5, ±1} ⇒ spec(G²) = {5,5,1,1} ≠ {5,5,5,1} = spec(c) = spec(M_S) — so "G is an
  equivariant square root of the period Gram" is **refuted by inspection** (recorded here).
  The surviving precise question: G is odd under an involution (± paired spectrum) while c is
  positive — the natural Bring counterpart is the **real-structure/involution action** (BN12's
  S′, or the odd part of the intersection form C). Compute the exact spectrum of C·(anti-involution)
  restricted to the two std blocks and compare to {±√5, ±1}. Cheap (8×8 integer matrices, all
  printed in the papers), decisive, no fit. Match ⇒ m's ceiling tied to the Bring real
  structure; mismatch ⇒ the Bring route for Vector 2 closes in one page.
- **Risk:** the S₄ (antisymmetrizer) vs S₅ (Bring) equivariance bookkeeping must be honest;
  sloppy identification would manufacture the coincidence Vector 2 wants.

### A6. Unique S₅-invariant theta characteristic + explicit vector of Riemann constants as the canonical spin normalization
- **Target gap:** fermion-determinant normalization / the v² = q sign; feeds A1.
- **Paper evidence:** BN12 Thm 3 (K_Q = (1/10)(3,2,−2,−3) + Im(τ₀)·(1,−2,−2,1)·i, base point
  the order-5 fixed point Q; Smith-normal-form torsion method) and Thm 4 (**unique**
  Aut-invariant spin structure); BDH22 Prop 5.11/5.13 (the invariant characteristic
  explicitly; = the Szegő-kernel divisor, verified to 10⁻¹¹⁸).
- **Corpus status:** open/unwired.
  [`sign-as-spin-structure.md`](../../content/quantum-observable-universe/quantum-observable-universes/sign-as-spin-structure.md)
  has no Bring/K_Q content; "Riemann constants" absent from the corpus.
- **Next probe (formalize-first):** the forcing lemma — S₅ acts on the 2⁸ theta
  characteristics with exactly one fixed point, so any S₅-natural sign object is **forced**
  onto it (trivial Lean); record K_Q + the invariant characteristic in a witness for A1's
  polarized θ-sum to consume. No search.
- **Risk:** the physical identification (worldline spin ↔ Bring spin structure) is a
  framework hypothesis — keep it a conditional class.

### A7. Level-5 congruence parallelism: icosahedron = M₃(5), Bring = M₄(5)
- **Target gap:** the "why" of the icosahedral bridge (structural support for A5/B4).
- **Paper evidence:** KS24 Thm 3.2 (Bring = compactified H/H₄(5), H₄ = C₂∗C₄ over ℤ[√2],
  index μ₄(5) = 120, regular map {5,4}: 30/60/24); Ex 5.1 (the Farey map mod 5, M₃(5), **is
  the icosahedron**); first *proved* 20-gon side-pairing table (k↔k+3 for k≡2 mod 4, k↔k+9
  for k≡3 mod 4) — RR92/BN12 gave it without proof.
- **Corpus status:** open; no corpus object references Hecke groups H_q, Farey maps, or
  ℤ[√2]-congruence structure. (Not the closed 8we6 Iwahori–Hecke route.)
- **Next probe:** scoping note only — both the S-matrix side (A₅ ⊂ PSL(2,5) on the
  icosahedron) and the Bring side (S₅ = H₄/H₄(5)) arise from reduction mod 5; the candidate
  bridge is the reduction functor. Falsifier: does the H₄(5) quotient carry a natural
  ℤ[√2]/(5) ≅ F₂₅ structure whose norm map to F₅ reproduces the Farey-mod-5 icosahedron data
  (5 inert in ℤ[√2])? If the norm-functor statement fails, drop the idea.
- **Risk:** high — pure structure-hunting; keep below the falsifier-gated ideas and never
  near a numerical match claim.

---

## Cluster B — ranked ideas (3D-index / complex CS)

> Background correction (to this session's own briefing, not the corpus): Vol(𝓑₃) = 2·v_oct
> = 8·Catalan ≈ 7.327724753 — the corpus value in
> [`binding_link_volumes.py`](../../computations/binding_link_volumes.py) is correct; the
> briefing's "Vol(𝓑₃) = 2·Vol(4₁)" was wrong (ratio is 3.61, not 2).

### B1. Compute I_𝓑₃ — the Borromean 3D-index as the integer-graded nucleon-carrier invariant
- **Target gap:** ρ(𝓑₃) density / the 2.89% m_p gap (integer-graded handle); bar-even channel.
- **Paper evidence:** DGG 1108.4389 §4.5 (ideal octahedron: 4- and 5-tetrahedron
  decompositions with internal-edge data); GHRS 1303.5278 Thm 1.8 (index of X^EP
  triangulations is a topological invariant), Thm 1.9 (EP ⇒ semi-angle structure),
  Rmk 1.10 (**all link complements in S³** admit the strict-angle-structure hypothesis)
  ⇒ I_𝓑₃ well-defined; index valued in Z((q^{1/2}))^{H₁(∂M;ℤ)} with H₁(∂M;ℤ) = ℤ⁶ —
  a 6-fold peripheral grading = per-cusp quantum numbers.
- **Corpus status:** OPEN. 4₁ machinery validated/closed today; no Borromean index exists in
  the corpus, and the 7 papers never compute it (grep 0/7) — likely new to the literature
  they cite.
- **Next probe (formalize-first):** SnapPy `L6a4` → Neumann–Zagier gluing data (not guessed);
  ℤ⁵ lattice sum of products of 8 validated `J_Δ`'s (Ex 4.1 pattern generalized; n=8, r=3
  cusps ⇒ rank n−r = 5). Three self-tests **before** any physics: (i) no negative q-powers
  (1-efficiency, GHHR Cor 10.21); (ii) constant term 1; (iii) **S₃ cusp-permutation symmetry**
  of I_𝓑₃(b) under permuting the three ℤ² blocks — a theorem-level invariant the assembly
  must pass. Then triangulation-independence via a 2-3 move (GHRS Thm 1.1(b)). Only after
  3/3 green: comparison-only table vs F_Bor = |tr_M(β_Bor)|·[3]_q!/q³ data.
- **Risk:** ℤ⁵ sum is heavier than 4₁'s ℤ¹ but q-degree grows ~quadratically in the summation
  vector ⇒ O(N^{5/2}) terms to order q^N — feasible. Main failure mode: no canonical bridge
  from index coefficients to ρ(𝓑₃); the deliverable is the invariant + graded structure, not
  a number-match.

### B2. Angle-structure LP ↔ confinement SDP: the dual dictionary
- **Target gap:** collective binding term / binding channels; structural underpinning for
  "active channels = most receptive sub-braids".
- **Paper evidence:** 1208.1663 Thm 2.12 (I_T well-defined ⟺ index structure; exists given a
  strict angle structure), §2.2 ("generalized angle structures are linearizations of the
  gluing equations… intimately connected with normal surfaces"), eq (2.7) (the LP
  constraints); GHHR 1604.02688 **Prop A.3**: χ(S) = −Σ_q α(q)x_q/π + ρ_α(∂S)/2π — an
  explicit bilinear pairing between the angle polytope and the normal-surface cone
  (Casson–Rivin/Luo–Tillmann duality as an LP pairing).
- **Corpus status:** OPEN — never proposed; the LP/SDP dual-emission infra
  ([`lp_dual_solver.py`](../../computations/lp_dual_solver.py), AGENTS §LP/SDP duals) is the
  ready-made consumer.
- **Next probe (formalize-first):** exact rational LP on the 𝓑₃ triangulation (8 tetrahedra,
  24 angle variables, ~8 edge constraints); emit primal (strict angle structure — must exist
  per Rmk 1.10) + dual (y★ ≥ 0 supported on vertex normal surfaces) through the standard dual
  fields. Then comparison-only: LP-dual active surface classes vs the confinement-SDP
  `active_set` for β_Bor. Claim to check before any sweep: both duals price
  Frobenius-positivity-type constraints (quad-indexed vs Wedderburn-block-indexed) — look for
  a rank/count coincidence, not a numeric fit.
- **Risk:** may be a functor-level analogy rather than an isomorphism; failure is cheap and
  decisive (count mismatch kills it in an afternoon).

### B3. The collective binding term as an embedded-normal-surface generating series
- **Target gap:** Δ_λ collective term; the ³H/³He mirror-split deficit (1.22× observed vs
  2.25× per-pair-predicted, #3943).
- **Paper evidence:** GHHR Def 8.1 / Cor 8.2: I⁰_T(0) = Σ over normal-surface classes of
  I([S]); I([S]) = (−q^{1/2})^{−χ(S*)}·J(S*), min-degree d([S]) = −χ(S*) + δ(S*) (§8.1
  eq (32); δ = double arcs); Thm 8.6 (rays kS contribute degree −kχ(S) — the "additive"
  content; everything off-ray is collective). The index carries per-cusp grading
  b ∈ H₁(∂M;ℤ) = ℤ⁶ and boundary classes [∂S] — an object that **can** distinguish (Z,N)
  where the Slater-antisymmetrizer trace (A-only; pn-blind by proved invariant, attack-map
  §2.1) cannot.
- **Corpus status:** OPEN; nothing normal-surface-based has been tried. Complements (does not
  duplicate) attack-map Vectors 1/4 — this is the *surface-level* refinement of "the missing
  term is a graph object".
- **Next probe (formalize-first):** enumerate the vertex normal surfaces of the 𝓑₃
  triangulation exactly (small Hilbert-basis computation on 8 tetrahedra) with their
  (χ, [∂S], [S]₂) data. Structural question before any physics: does the cone contain classes
  whose [∂S] distinguishes the three cusps asymmetrically (candidate carriers of a
  p/n-asymmetric collective term)? Pure integer computation, no q₀, no fit.
- **Risk:** highest modeling risk of the B-list — needs a postulated map {isotope} →
  {peripheral class} before any comparison; without that map stated as a conjecture block,
  any match is laundering. Keep at structure-hunt tier.

### B4. ζ₅ exact state-integral evaluation — an exact 1/√5 for the magnitude scalar m
- **Target gap:** Δ_λ magnitude scalar; fibre-level ζ₄/ζ₅ handles; c_k Habiro (secondary).
- **Paper evidence:** GK 1411.6062 Thm 1.1 (at b² = M/N the 1-dim state integral evaluates in
  closed form: root-of-unity prefactor × Rogers-type exponentials × cyclic quantum
  dilogarithms D_N(θ,ζ_N^M) [finite products] × finite Gauss-type state sum G_{M,N});
  **Cor 1.2** (M = 1) carries the explicit **1/√N** factor; worked examples 4₁, 5₂,
  (−2,3,7)-pretzel.
- **Corpus status:** OPEN as a route; Vector 2 has no exact-evaluation handle yet; the ζ₄
  sign result is Lean-closed (`PrincipalGradingJetOrder.lean`). Nothing in the corpus
  evaluates state integrals at rational points.
- **Next probe (formalize-first):** compute D₅(θ, ζ₅) and the finite Gauss sum G₅ for the 4₁
  data of Cor 1.2 at N = 5 **symbolically** and identify the full algebraic number
  multiplying 1/√5. Only then ask whether m = (that number)·(1/√5) has an object-level
  derivation — the honest bridge candidate: **both** √5's are discrete-Fourier/Gauss-sum
  √5's at ζ₅ (the Σ(2,3,5) S-matrix is itself a ζ₅ Fourier kernel). One exact evaluation,
  no search.
- **Risk:** the 1/√N is a Gaussian-integration normalization — could be a coincidence of
  normalizations; anti-numerology gate applies with full force (structure only until an
  object-level S-matrix ↔ Gauss-sum map exists).

### B5. GGM Conjecture 4 on the bar-even (mass) channel: exact rotated-index Stokes data
- **Target gap:** G3 follow-on (bar-even side); the c₄-even ladder; eventually ρ(K).
- **Paper evidence:** GGM 2012.00062 Conj 4 + eq (21): S⁺_{σ₁σ₁}(x;q) = Ind^rot_K(0,x;q)
  **exactly, proved for 4₁ and 5₂** (Thm 1; verification eqs (194)–(198)); Conj 3 (peacock
  singularity lattice); holomorphic-block factorization eq (19); Thm 22 (5₂ descendant
  state-integral ↔ blocks — the object main commit `57f97aed` implements).
- **Corpus status:** partly in-flight — odd channel CLOSED (capstone audit); 4₁ Stokes = 3
  GGM-proved (#3872); 5₂ Theorem-22 blocks landed today. The **unclaimed slice**: the
  bar-even/mass-side integer amplitudes from Ind^rot(0,x;q), and the x-deformed (u ≠ 0)
  index no sibling has assembled.
- **Next probe:** expand Ind^rot_{4₁}(0,x;q) (one extra fugacity sum over the validated
  Ex-4.1 gluing) to low order; comparison-only vs the committed even κ-tower / c₄-even
  exact-rung data ([`2026-07-18-c4even-exact-rung`-lineage audits](2026-07-18-1ppq-action-plan.md)).
- **Risk:** overlap with the #3805 lineage — intent posted on #3805 with the distinct angle
  ("bar-even / x-deformed rotated index", this PR's coordination comment). Conj 4 is proved
  for knots only — do **not** extrapolate to 𝓑₃ without flagging it as conjecture.

### B6. Index convolution along cusps as the M_n(K) coordination-graph combiner
- **Target gap:** per-isotope M_n(K) edge-set / coordination-graph closure (Subgoal-2,
  open-for-all).
- **Paper evidence:** DGG 1108.4389 §2.2 (gluing = gauging: sum over magnetic flux +
  fugacity integration on shared torus data), §3.1 (Sp(2N,ℤ) action); 1112.5179 §4.1
  (gluing steps 1–5), §4.4 (mapping tori; T[SU(2)] duality wall — the genuine
  torus-boundary composition object).
- **Corpus status:** OPEN; no index-composition object exists. Related-but-distinct:
  attack-map Vector 1 (per-pair volume on K₄) is the *volume* graph object; this is its
  *index/integer* counterpart.
- **Next probe (formalize-first):** verify the composition law on pure topology first: glue
  two 4₁ copies via the T[SU(2)] wall (§4.4) and check against the glued manifold's own
  triangulated index. Only if the machine works, model a 2-carrier bond.
- **Risk:** highest speculation tier — "gluing cusps = a bond" is a modeling postulate with
  large freedom; rank last among compute ideas.

### B7. 1-efficiency as the carrier-stability selection principle (cheap, structural)
- **Target gap:** carrier-menu justification (no numeric gap).
- **Paper evidence:** GHRS Thm 1.2 (index structure ⟺ 1-efficient), Rmk 1.3 (⟹ irreducible +
  atoroidal ⟹ hyperbolic or small Seifert-fibred), Rmk 1.4 (explicit: 4₁#5₂ and the
  Whitehead double of 4₁ admit **no** index on any triangulation, though their Jones/Kashaev
  invariants exist).
- **Corpus status:** OPEN; nothing cites 1-efficiency. Cheap remark/conjecture-block
  candidate; zero compute.
- **Risk:** interpretive only — phrase as a selection *observation*, not a derivation of the
  carrier set.

---

## New exact facts established this session (decisive one-line checks)

1. **τ₀ digit adjudication:** BDH22's τ₀ ≈ −0.5 + 0.186676i is correct; BN12's printed
   0.185576 fails the j-test by 6% (j → −4039.6 vs target −3810.78) — a typo in BN12.
2. **Hauptmodul:** t₅(τ₀) := (η(τ₀)/η(5τ₀))⁶ = **−10 exactly** (real root of
   (t²+250t+3125)³ + (121945/32)t⁵; η-quotient confirms numerically); Fricke partner
   5³/t₅ = −25/2 = j(5τ₀).
3. **Per-factor measure ratio is algebraic:** m(τ₀)/m(5τ₀) = √5·10^(−1/3) exactly
   (= 1.03789…, matching the bring-s4 audit's 1.74146/1.67789).
4. **Integer-trace obstruction:** tr B = 2.6423863 ∉ ℤ ⇒ no SL₂(ℤ) monodromy has char-poly
   x² − 2.6424x + 1 (the 2026-06-24 E⁴ audit needs an SL₂(ℝ) re-scope; scope-(b), invariant
   cited).
5. **Vector-2 naive identification refuted by inspection:** spec(G²) = {5,5,1,1} ≠
   {5,5,5,1} = spec(c) = spec(M_S); the surviving comparison is against the Bring
   real-structure/involution action (A5).
6. **Vol(𝓑₃) confirmed:** 2·v_oct = 8·Catalan ≈ 7.327724753 (corpus value correct).
7. **#3934 cross-check:** Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀} **confirmed** (BDH22 Prop 4.6 /
   [GAR00]) as a complex-torus isomorphism, with the explicit caveat that the block form is
   **not symplectic** (the polarization caveat #3934's "polarization is essential" finding
   relies on); RR92 §4 gives the isogeny version diag(5τ,5τ,5τ,τ) + Serre's E⁴ observation.

## Facts-extracted appendix — Cluster A (Bring)

- **RR92:** B ⊂ P⁴: Σxᵢ = Σxᵢ² = Σxᵢ³ = 0; (2,4,5) triangle group; 20-sided fundamental
  polygon; H₁ ≅ **2 × (4-dim standard irrep)** of S₅; Thm 1: period matrices fixed by SpS₅
  form the one-parameter family Z = τ·c, c = [[4,1,−1,1],[1,4,1,−1],[−1,1,4,1],[1,−1,1,4]];
  stabilizer of Bring's half-plane = SpS₅ × SpΓ₀(5); τ unique mod Γ₀(5). Thm 2: τ₀'s class
  fixed by j(τ₀), j(5τ₀) (RR92 swapped the two equations — corrected by BN12 fn 5 / BDH22).
  §4: mᵗcm = diag(5,5,5,1); Jac isogenous to diag(5τ,5τ,5τ,τ); Serre: 4 copies of
  y² = x³−675x−79650 (j = −25/2); Schottky form vanishes to first order exactly at τ₀.
- **BN12:** period matrix from the Hulek–Craig sextic (Ramanujan theta parameterization);
  corrected j-values j(τ₀) = −29³·5/2⁵ = −121945/32, j(5τ₀) = −25/2; τ₀ print typo (see
  exact fact 1); explicit real structure S′; Thm 3: K_Q = (1/10)(3,2,−2,−3) +
  Im(τ₀)·(1,−2,−2,1)·i; K_C ~ a + 2b + 3c at the three order-5 fixed points; Thm 4:
  **unique invariant spin structure**.
- **KS24:** H₄ = ⟨z↦z+√2, z↦−1/z⟩ ≅ C₂∗C₄ over ℤ[√2]; Thm 3.2: Bring = compactified
  H/H₄(5), index 120, regular map {5,4} (30 vertices / 60 edges / 24 faces); 24 Hecke–Farey
  coordinates mod 5; first proved 20-gon side pairings (k↔k+3 for k≡2 mod 4, k↔k+9 for
  k≡3 mod 4); Ex 5.1: M₃(5) = the icosahedron; M₄(3) = the cube.
- **BDH22:** Thm 2.12: τ_B = τ₀·M and (symplectic-equivalent) τ_B = τ₀·M_S, M_S = 5I−J,
  spectrum {1,5,5,5}; τ₀ = −0.5 + 0.186676i (6 d.p.), transcendental (Schneider);
  §2.2/§4.4: ℚ-isogeny class of order 4 with periods τ₀, 3τ₀, 5τ₀, 15τ₀;
  j(3τ₀) = 5·211³/2¹⁵, j(15τ₀) = −5²·241³/2³; §4.3: C₁ ≅ X₀(50) (eq (10)); Prop 4.4
  (ℂ-isogeny class E₃⁴; M′ = 5M⁻¹ integral); Prop 4.5 (ℚ-class (50a)⁴; 50b/50a merge over
  ℚ(√5)); Prop 4.6 (Jac(B) ≅ E₂³ × E₁ as complex torus, **not** as ppav);
  H^{1,0}(B) = standard irrep (4,1) ⇒ H¹ = 2·std (matches corpus `s5_bring_hodge_depth`);
  60 weight-1 Weierstrass points, Aut-transitive; 19 odd + 20 even theta-characteristic
  orbits with an unexplained "threeness"; unique invariant even characteristic = Szegő
  divisor (Props 5.11/5.13).

## Facts-extracted appendix — Cluster B (3D-index)

- **Multi-cusp gluing shape:** I: triangulations → Z((q^{1/2}))^{H₁(∂M;ℤ)} (GHRS eq (1));
  n tetrahedra, r cusps ⇒ lattice sum over ℤ^{n−r} of products of n tetrahedron indices,
  charges linear in the summation vector + peripheral class. 1-cusp worked case = GHHR
  Ex 4.1 (the validated 4₁ gluing). For 𝓑₃: n = 8, r = 3 ⇒ ℤ⁵ sum, grading b ∈ ℤ⁶.
  Normalization dictionary: I⁰_T(2eμ−mλ) [GHHR] = I_T(m,e) [DGG] (GHHR Rmk 8.4).
- **Angle-structure theorem (1208.1663):** Thm 2.12 — I_T well-defined ⟺ index structure;
  exists if a strict angle structure does (eq (2.7)); 3-2 moves always preserve the index,
  2-3 moves conditionally (§6); counterexample m136 (semi-strict only, index still exists).
- **1-efficiency (GHRS):** Thm 1.1 (well-defined ⟺ index structure; 2-3-invariant);
  Thm 1.2 (⟺ 1-efficient); Thm 1.5 (semi-angle ⇒ 1-efficient); Thm 1.8 (X^EP ⇒ topological
  invariant I_M); Thm 1.9 (EP ⇒ semi-angle); Rmk 1.10 (all link complements in S³ qualify);
  Rmk 1.13 (I^tot related to Andersen–Kashaev state integrals).
- **Normal-surface expansion (GHHR):** Def 8.1/Cor 8.2 (index = generating series over
  normal-surface classes); d([S]) = −χ(S*) + δ(S*); Thm 8.6 (convergence ⟺ 1-efficient);
  Cor 10.21 (1-efficient ⇒ genuine power series — the sibling's self-test); Prop A.3
  (Gauss–Bonnet pairing of angle structures with normal coordinates).
- **Rational-point evaluation (GK):** Thm 1.1 (state integral at b² = M/N = prefactor ×
  Rogers terms × cyclic dilogs D_N, D_M × finite Gauss sum G_{M,N}); Cor 1.2 (M = 1,
  explicit 1/√N); examples 4₁, 5₂, (−2,3,7).
- **Stokes ↔ 3D-index (GGM):** Conj 3 (peacock lattice); **Conj 4 + eq (21)** (Stokes
  matrix = rotated index; S⁺_{σ₁σ₁}(x;q) = Ind^rot_K(0,x;q), proved for 4₁ and 5₂, Thm 1,
  eqs (194)–(198)); Conj 5/Thm 6 (Â-polynomial refinement); Thms 9–12 (4₁/5₂ Wronskians);
  Thm 22 (5₂ descendant state-integral ↔ blocks).
- **Borromean in the papers:** appears explicitly in **none** of the 7 (grep 0/7); closest
  objects are the ideal-octahedron decompositions (DGG §4.5) and the link-complement
  guarantee (GHRS Rmk 1.10). I_𝓑₃ would be new to the corpus and to these papers'
  literature.

## Coordination

- **#3934** (Bring Epstein det′Δ): Prop 4.6 confirmation + polarization caveat + the
  polarized-lattice route (A1) and t₅(τ₀) = −10 (A2) posted as a comment.
- **#3805 / `57f97aed` lineage** (G3 3D-index): intent posted; B5's distinct angle is the
  bar-even / x-deformed rotated index; B1 (𝓑₃) is unclaimed territory.
- **#3808** (binding frontier R11): B3 (normal-surface collective term) flagged as the
  surface-level refinement of the collective residual; no overlap with the R11 3-factor
  closure fronts.
- Attack-vector map Vector 2: A5's inspection-refutation + surviving involution comparison
  and B4's ζ₅ route both recorded here as the two live legs.
