# The I_𝓑₃ → F_Bor bridge — invariant list (formalize-first) + per-cusp graded index table (2026-07-24)

**Tier:** audit-only; scope-(a); comparison-only; **no fit; nothing wired**. W1 of
[`2026-07-24-binding-mass-workplan-refresh.md`](../coordination/2026-07-24-binding-mass-workplan-refresh.md)
(bean `qou-gyvw`); follow-on to
[`2026-07-18-borromean-3d-index.md`](2026-07-18-borromean-3d-index.md) (idea B1)
and executor of the grading leg of idea B6
([`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md)).
Per the formalize-first discipline, §1 (the structural requirements any *derived*
index → F_Bor bridge must satisfy) was stated **before** the new graded data was
computed; §2–§3 record the computed data and count-level observations only. No
coefficient of any index series is numerically compared to F_Bor, tr_M, ρ(𝓑₃), or
any mass/binding observable.

## 1. Bridge invariants — what any *derived* I_𝓑₃ → F_Bor bridge must satisfy

Target object (production, [`canonical_mass.py`](../../computations/canonical_mass.py) /
[`m_p_substrate_identity_50dps.py`](../../computations/m_p_substrate_identity_50dps.py)):

$$F_{\mathrm{Bor}}(q) = |\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|\cdot [3]_q!/q^3,\qquad
\mathrm{tr}_M(\beta_{\mathrm{Bor}},q) = \frac{4+h^2-3h^4-h^6}{h^2+4},\ h = q-q^{-1},$$

with β_Bor = (σ₁σ₂⁻¹)³ ∈ B₃ (writhe 0), evaluated at the substrate q₀ ≈ 1.10998:
|tr_M| ≈ 0.998562, [3]_q! ≈ 6.120579, **F_Bor(q₀) ≈ 4.4691387358** (this is a single
real number, not a series). Source object: I_𝓑₃ : H₁(∂𝓑₃;ℤ) = ℤ⁶ → ℤ((q^{1/2})), the
GHHR/GHRS 3D-index of L6a4 (well-defined; 4/4 self-tests green per the B1 audit).

Any candidate bridge that is claimed *derived* (not fitted) must satisfy **all** of:

- **(a) Full cusp-symmetry equivariance.** F_Bor is a symmetric function of the
  three Borromean components (β_Bor's Markov trace is invariant under the S₃
  component symmetry). A bridge consuming the ℤ⁶ peripheral grading must therefore
  factor through the **invariants of the grading under the cusp symmetry** — at
  minimum the verified S₃ permutation action on the three (p_h, q_h) blocks, and in
  fact under the full symmetry subgroup of the isometry group of 𝓑₃ that the index
  table realises (§2 records which candidate lattice symmetries the computed table
  satisfies: S₃ permutations, global and per-cusp negation, and the global
  meridian↔longitude swap all preserve it — recorded, not interpreted). A bridge
  that privileges one cusp or one non-invariant lattice direction is not derived.

- **(b) 2–3-move / triangulation independence.** Guaranteed *for free* only if the
  bridge consumes I_𝓑₃ itself (GHRS Thm 1.1(b), self-test iv green). A bridge that
  reaches past the index into per-tetrahedron data (charges, shape parameters,
  angle structures, normal-surface coordinates of one triangulation) does **not**
  inherit this and must prove its own invariance before any physical reading.

- **(c) The two q's are different variables a priori.** The index q is the **DGG
  fugacity** — I_𝓑₃(b) ∈ ℤ((q^{1/2})) is a power series convergent for |q| < 1
  (GHRS eq (1); 1-efficiency ⇒ genuine power series, GHHR Cor 10.21). The Hecke q
  is the **substrate deformation** with archimedean evaluation at q₀ ≈ 1.10998 —
  strictly **outside** the index's disc of definition. Any identification of the
  two must be argued at the **fibre level** (the Im(q) fibre-vs-observable rule,
  AGENTS.md): both are formal deformation variables of objects attached to the same
  topological carrier, but no functor identifying them exists in the corpus. A
  bridge statement must name the map (e.g. a state-integral / analytic-continuation
  functor à la GK arXiv:1411.6062, or a q → 1 scaling limit) — never a silent
  substitution q := q₀.

- **(d) A bridge is an evaluation/limit, not a coefficient match.** The index
  coefficients grow (1, 0, 13, −16, −97, 16, 586, 992, −514, −5600, −11451, …);
  F_Bor(q₀) is one number. Any derived bridge must be a **functional** of the
  series — an evaluation inside the disc, a limit (q → 1 scaling), an asymptotic
  coefficient functional, or a state-integral continuation — with the functional
  itself derived, not selected. Matching an individual integer coefficient (or a
  finite handful) against a real number at q₀ is numerology by construction and is
  excluded without computation.

- **(e) Prune (scope-(a)-limited, invariant named): coefficientwise evaluation at
  q₀ is not an admissible bridge.** The coefficients are integers, so every
  nonzero term at |q| = q₀ > 1 has modulus ≥ q₀ⁿ; if I_𝓑₃(b) has infinitely many
  nonzero coefficients, the series diverges at q₀ and the "evaluate the q-series
  at the substrate" bridge class is empty. The observed coefficients grow through
  q¹⁰ and the index is q-holonomic of Nahm type (GHRS §1.1) with, per GHRS, "a
  meromorphic singularity at q = 0 [and] analytic continuation in the punctured
  unit disc" — i.e. the natural domain is |q| < 1. We record this as a
  **scope-(a)** exclusion of the naive-evaluation class (the polynomiality of
  I_𝓑₃(b) has not been formally refuted, so per the (a)/(b) discipline we do not
  claim a proved structural exclusion); the honest bridge classes that remain are
  the limit/continuation classes of (d), in particular:
  - **Total-index / state-integral route:** GHRS Rmk 1.13 — for a knot complement,
    I^tot_K(q) = Σ_{e∈ℤ} I_M(eμ)(q) is well-defined and "closely related to the
    state-integral invariants of Andersen–Kashaev and Kashaev–Luo–Vartanov
    [AK, KLV12]"; the state-integral ↔ q-series relation is developed in GK
    (arXiv:1411.6062, uploaded). §3 computes the 3-cusp meridian analogue for 𝓑₃
    (as a *definition* — Rmk 1.13 is stated for knots).
  - **Volume-asymptotics route (the honest candidate):** DGG arXiv:1112.5179
    §4.6, eq (4.54)–(4.57) — in the 't Hooft limit m → ∞, q → 1 (ħ → 0) with
    x = q^m ζ fixed, I_M(m; q, ζ) ~ exp((2/iħ)·V_M(x) + …) with
    Vol_M(x) = V_M(x) + (Im P)(Re X) the (boundary-condition-dependent) hyperbolic
    volume — the index's leading asymptotics carry **Vol(M)**, the same Vol(𝓑₃) =
    2·v_oct ≈ 7.327724753 that m(K) already consumes through the volume–density
    framing and that the muon anchor consumes as Vol(4₁). This is a physics-level
    derivation in DGG (not a theorem in the uploaded papers; [GZ] is cited by GHRS
    only as an *empirical* study of I^tot_{4₁} asymptotics), so any bridge built on
    it enters the corpus as a **conjecture-tier** statement (§3b discipline), never
    as a proved rung.

- **(f) Calibration / anti-fit discipline.** The bridge must be parameter-free
  given (𝓑₃, q₀): no constant chosen from a menu because it lands near
  4.4691387358, no truncation order chosen by proximity, no per-class weights
  selected post hoc. The three-calibration discipline and the Δ_λ "no fit-based
  ansatz" rule apply with full force. Additionally the target is **bar-even**
  (tr_M(β_Bor) is even in h = q − q⁻¹, Lean-proved closed form;
  [`borromean-h3-2-1-irrep-derivation.witness.json`](../../computations/borromean-h3-2-1-irrep-derivation.witness.json)
  records the (2,1)-block trace as structurally even in h) — a bridge whose
  index-side functional is not bar-symmetrizable cannot land on F_Bor's channel.

## 2. The per-cusp graded table (idea B6's grading leg)

Probe: [`computations/probes/borromean_3d_index_graded.py`](../../computations/probes/borromean_3d_index_graded.py)
(+ witness [`borromean-3d-index-graded.witness.json`](../../computations/probes/borromean-3d-index-graded.witness.json)),
reusing the validated B1 machinery with a shared-shell enumeration, **gated** by
(A) exact agreement with the committed B1 witness values on I(0), I(µ₁),
I(µ₁+λ₁) and (B) exact agreement with the original per-class machinery on 4
sample classes, before the sweep results are trusted.

**Run:** all gates PASS, exit 0 (wall ≈ 10.6 min; 69 901 admissible lattice vectors,
max 565 per class; log `/tmp/borromean_index_graded.log`, ephemeral). Structural
self-tests: no negative q-powers on any class (GHHR Cor 10.21), I(0) constant term 1,
**no half-integer q-powers on any of the 729 integral classes**, S₃ cusp-permutation
equivariance verified on the full table (729 classes × 6 permutations, direct equality).

**Summary counts (exact, to q⁶):**

- **All 729 classes are nonzero to q⁶** — the grading is fully populated at
  ℓ∞-radius 1; 165 S₃ orbits (sizes 1/3/6).
- **Verified lattice symmetry group of the table.** Menu results (each map tested
  against all 729 classes): S₃ cusp permutations ✓; global negation b → −b ✓ (the
  DGG ρ-symmetry); per-cusp full negation (p_h,q_h) → (−p_h,−q_h) ✓; global
  longitude negation (p,q) → (p,−q) on all cusps ✓; global meridian negation ✓;
  per-cusp λ-negation ✗; per-cusp µ-negation ✗; meridian↔longitude swap (global
  and per-cusp) ✗. The group generated by the verified maps acts with **24 coarse
  orbits** carrying **23 distinct series** (the one coincidence beyond the group
  is recorded below). Note the meridian and longitude directions are
  **inequivalent** (swap fails) — the grading sees the framing asymmetry of the
  cusps — while each direction is separately sign-symmetric.
- Isom(𝓑₃) has order 48; the verified lattice group is larger (per-cusp signs ×
  S₃ × a global λ-sign). Which verified maps are induced by isometries and which
  are index-theoretic symmetries (à la the ρ-symmetry) is left open — recorded,
  not interpreted.

**Coarse-orbit graded table** (orbit representative under the verified group;
size = classes in the |b|∞ ≤ 1 box; exact integer coefficients q⁰…q⁶):

| coarse-orbit representative (p₁,q₁,p₂,q₂,p₃,q₃) | size | I_𝓑₃(b), q⁰…q⁶ |
|---|---|---|
| (0,0,0,0,0,0) | 1 | `[1, 0, 13, -16, -97, 16, 586]` |
| (-1,0,-1,0,0,-1) | 24 | `[0, 1, -4, -3, 16, 61, 52]` |
| (-1,0,0,-1,0,0) | 24 | `[0, 2, -4, -6, 12, 78, 104]` |
| (0,-1,0,0,0,0) | 6 | `[0, 3, -4, -8, 4, 88, 172]` |
| (-1,0,0,-1,0,-1) | 24 | `[0, 0, 2, 0, 6, 4, -26]` |
| (-1,0,-1,0,0,0) | 12 | `[0, 0, 4, -12, -40, 56, 352]` |
| (0,-1,0,-1,0,0) | 12 | `[0, 0, 2, 0, 5, 8, -7]` |
| (-1,0,-1,0,-1,0) | 8 | `[0, 0, 2, -8, -24, 52, 256]` |
| (-1,0,0,0,0,0) | 6 | `[0, 0, 8, -16, -64, 48, 464]` |
| (-1,-1,-1,0,0,-1) | 96 | `[0, 0, 0, 2, 2, 4, -30]` |
| (-1,-1,-1,-1,-1,0) | 48 | `[0, 0, 0, 2, 6, -6, -42]` |
| (-1,-1,-1,0,-1,0) | 48 | `[0, 0, 0, -4, 10, 42, 22]` |
| (-1,-1,-1,0,0,0) | 48 | `[0, 0, 0, -6, 10, 54, 54]` |
| (-1,-1,0,-1,0,0) | 48 | `[0, 0, 0, 2, 2, 8, -20]` |
| (-1,-1,-1,-1,0,0) | 24 | `[0, 0, 0, 2, 8, -2, -40]` |
| (-1,-1,0,0,0,0) | 12 | `[0, 0, 0, -8, 8, 64, 96]` |
| (-1,-1,-1,0,-1,1) | 48 | `[0, 0, 0, 0, 2, 0, -10]` |
| (-1,-1,-1,1,0,0) | 24 | `[0, 0, 0, 0, 2, 2, -4]` |
| (-1,-1,-1,-1,0,-1) | 48 | `[0, 0, 0, 0, 0, -1, -8]` |
| (-1,-1,-1,-1,-1,-1) | 16 | `[0, 0, 0, 0, 0, -4, -18]` |
| (0,-1,0,-1,0,-1) | 8 | `[0, 0, 0, 0, 0, 1, -4]` |
| (-1,-1,-1,-1,-1,1) | 48 | `[0, 0, 0, 0, 0, 0, -2]` |
| (-1,-1,-1,1,0,-1) | 48 | `[0, 0, 0, 0, 0, 0, -2]` |
| (-1,-1,0,-1,0,-1) | 48 | `[0, 0, 0, 0, 0, 0, -4]` |

(Full per-S₃-orbit table with exact Q-pairs: the witness's `graded_table_nonzero`.)

**Recorded observations on the table** (recorded-not-interpreted):

- First nonzero orders stratify 1…6; both signs occur as leading coefficients.
- The pure-longitude orbit (0,±1,0,0,0,0) is the **lowest-order nonzero grading
  direction** (starts at q¹, coefficient 3); the pure-meridian orbit starts at q²
  (coefficient 8); the single-cusp (µ+λ) orbit starts at q³ (coefficient −8). The
  trivial class has no q¹ term.
- One series coincidence beyond the verified group survives to q⁶:
  orbits (−1,−1,−1,−1,−1,1) and (−1,−1,−1,1,0,−1) both give −2q⁶ + O(q⁷) — either
  a deeper symmetry or an accident of the truncation order; undecided here.

## 3. Structural findings (comparison-only, recorded-not-interpreted)

### 3(i) The meridian total index — a single canonical q-series attached to 𝓑₃

The 3-cusp meridian analogue of GHRS Rmk 1.13 eq (2) (a **definition** here — the
remark states the knot case; per-order finiteness is machine-certified by the exact
min-degree bound, meridian shells enumerated to ℓ∞-radius 8 with shells 7 and 8
contributing nothing to q⁶):

$$I^{\mathrm{tot}}_{\mathcal B_3}(q) := \sum_{e\in\mathbb Z^3} I_{\mathcal B_3}(e_1\mu_1+e_2\mu_2+e_3\mu_3)(q)
 = 1 + 6q + 129q^2 - 510q^3 - 1205q^4 + 4004q^5 + 15898q^6 + \cdots$$

exactly, from **246 contributing meridian classes** (the meridian sublattice is
far more slowly decaying than the ℓ∞ ≤ 1 box suggests: classes out to |e|∞ = 6
contribute to q⁶). This is the distinguished evaluation asked for by the workplan:
a *single* q-series canonically attached to 𝓑₃, the object GHRS Rmk 1.13 says is
"closely related to the state-integral invariants of Andersen–Kashaev and
Kashaev–Luo–Vartanov", with the state-integral ↔ q-series mechanics developed in
GK arXiv:1411.6062 (uploaded).

### 3(ii) Count-level comparison against the Wedderburn structure of tr_M³(β_Bor)

Recorded side-by-side; **no numerical coefficient is compared to any Hecke value**:

| Wedderburn / Hecke side (H₃(q), β_Bor = (σ₁σ₂⁻¹)³) | Index side (I_𝓑₃ to q⁶) |
|---|---|
| 3 Wedderburn blocks: λ ⊢ 3 = [3], [2,1], [1³], dims (1,2,1) | 3 cusps; ℤ⁶ grading; 24 coarse orbits / 23 distinct series / 165 S₃ orbits, all 729 box classes nonzero |
| β_Bor has writhe 0; both 1-dim characters equal 1 at β_Bor | trivial class has constant term 1 and vanishing q¹ term |
| tr_M(β_Bor) = (4+h²−3h⁴−h⁶)/(h²+4) is even in h (bar-even) | table invariant under global negation (ρ-symmetry) and under each of global µ- and λ-negation separately |
| F_Bor(q₀) ≈ 4.4691387358 (single number) | coefficients grow without bound (…586, 992, −5600, −11451 at trivial class) |

Recorded integer observations (integers only, recorded-not-interpreted, no bridge
claimed): the q¹ coefficient of I^tot is **6** (= |S₃| = [3]_q!|_{q=1}, the
classical limit of the q-factorial factor of F_Bor); the q¹ coefficient of the
pure-longitude orbit is **3** (= number of cusps = number of partitions of 3); the
q¹ coefficient of the trivial class is 0. No further count-level coincidence
between the block data (3, dims 1/2/1) and the orbit data (24/23/165) is visible
at this grading depth.

### 3(iii) The volume-asymptotics route — the honest bridge candidate (theorem-level record)

- **DGG arXiv:1112.5179 §4.6, eq (4.54)–(4.57)** (uploaded; physics derivation,
  not a theorem): in the 't Hooft limit m → ∞, q → 1 (ħ → 0) with x = q^m ζ held
  fixed, the index satisfies I_M(m; q, ζ) ~ exp((2/iħ)·V_M(x) + …), where
  Vol_M(x) = V_M(x) + (Im P)(Re X) is the hyperbolic volume of M at boundary
  condition x (flat-SL(2,ℂ) volume when no deformed hyperbolic structure exists).
  I.e. **the index's leading asymptotics in the scaling limit carry Vol(M)** — for
  𝓑₃ the same Vol(𝓑₃) = 2·v_oct ≈ 7.327724753 that the mass framing consumes, and
  for 4₁ the Vol(4₁) that the muon anchor m_μ = m_e·Vol(4₁)/ℏ_q² consumes.
- **GHRS Rmk 1.13** (uploaded): I^tot_K is well-defined (knot case) and closely
  related to AK/KLV state integrals; asymptotics of I^tot_{4₁} studied
  *empirically* in the cited [GZ].
- **Why this is the honest candidate:** m(K) already consumes Vol(K) through an
  evaluation at the substrate; a bridge in which the index enters through its
  **volume asymptotics / state-integral continuation** — rather than through
  coefficients — satisfies invariants (b), (c), (d) by construction (it consumes
  I itself, names the q → 1 scaling map, and is a limit functional). What it does
  **not** yet do is produce F_Bor's *non-volume* content (|tr_M|·[3]_q!/q³ is a
  Hecke object, not a volume); whether the subleading terms of the DGG expansion
  (the "+ …" of eq (4.56)) carry Hecke-trace data is exactly the open fibre-level
  question, and it enters the corpus only at conjecture tier (§3b discipline) if
  anyone formalizes it. **No such statement is made here.**

## Files

- Probe: [`computations/probes/borromean_3d_index_graded.py`](../../computations/probes/borromean_3d_index_graded.py)
- Witness: [`computations/probes/borromean-3d-index-graded.witness.json`](../../computations/probes/borromean-3d-index-graded.witness.json)
  (5/5 assertions pass: committed-value gate, independent-machinery gate, power-series,
  constant-term, S₃ equivariance)
- Predecessor (unchanged): [`computations/probes/borromean_3d_index.py`](../../computations/probes/borromean_3d_index.py) + its witness

## What this does and does not claim

- **Does:** state the derived-bridge invariant list (§1) *before* consuming the new
  data; extend the corpus's I_𝓑₃ knowledge from 3 peripheral orbits to the full
  |b|∞ ≤ 1 table with machine-verified S₃ equivariance and recorded extra lattice
  symmetries; define and compute the 3-cusp meridian total index; record
  count-level Wedderburn-side structure next to index-side counts.
- **Does not:** derive, propose, or fit any numerical bridge from index data to
  F_Bor, ρ(𝓑₃), the 2.89 % m_p gap, or any observable; claim the link-complement
  total index is covered by GHRS Rmk 1.13 (it is a definition here); claim the DGG
  volume asymptotics (4.56) as a theorem (it is a physics derivation; any use is
  conjecture-tier); declare any bridge class structurally excluded at scope-(b)
  (the §1(e) prune is scope-(a) with its invariant and its caveat named).
