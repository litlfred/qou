# Do counts on the proton object produce the 2 and the 12? (2026-11-21)

Identity under test (production, convention D):
m_p = 2 · m_μ · F_Bor(q) − 12 · m_e, F_Bor = tr_M(β_Bor)·[3]_q!/q³, β_Bor = (σ₀σ₁⁻¹)³ ∈ B₃.
The 12 was selected against m_p (owner ruling 2026-11-18, `computations/canonical_mass.py`).

Already excluded, not redone here (PR #8804 and `2026-11-21-proton-minus-twelve-origin.md`):
12 ≠ κ·μ for q-independent κ; 12 is not the 𝒟² state count (3/8) nor a Cartan-weight count (3);
the −12 cannot come from the Borromean tower; 12 = 2·F_Bor(1) = 4·F_e(1) = 2·|S₃| = 2·c(β_Bor)
are recorded readings.

## 1. Pre-registration (committed before any computation in this file was run)

Proton object: P = β_Bor = (σ₀σ₁⁻¹)³ ∈ B₃, its image in H₃(q) with (σ − q)(σ + q⁻¹) = 0,
and its closure L (the Borromean rings). Targets: a = 2 (multiplier of the tower) and
b = 12 (coefficient of m_e). One definition per candidate; no second definition is tried
if a candidate misses.

| id | family | the one definition | predicted value |
|---|---|---|---|
| K1 | rep multiplicity | dim over ℚ(q) of the centraliser Z_{H₃(q)}(P), generic q | 4 |
| K2 | rep dimension | dim over ℚ(q) of the subalgebra ℚ(q)[P] ⊂ H₃(q) (degree of the minimal polynomial of P) | 3 |
| K3 | crossing count | for each unordered pair of components of L, the number of crossings of the word P between those two components | 2 for each of the 3 pairs |
| K4 | strand count | number of components of L (cycles of the permutation of P) | 3 |
| K5 | Euler characteristic | χ of the Seifert surface that Seifert's algorithm gives on the closed braid P̂: χ = (strands) − (crossings) | −3 |
| K6 | index | [PSL(2,ℤ[i]) : Γ_L], Γ_L the holonomy group of the complete hyperbolic structure on S³∖L; computed as Vol(L)/covol(PSL(2,ℤ[i])) | 24 |
| K7 | orbit count | size of the orbit of the word P under cyclic rotation of its 6 letters | 2 |

Honesty note: the agent knew or could guess several of these values before writing them down
(K4, K5, K6 in particular). Pre-registration here guards against retries and against choosing
the definition after seeing a value; it does not make the agent ignorant.

Criterion for "derived". A candidate derives a or b only if both hold:
(i) its value equals the target, and (ii) a map already in the corpus puts that integer into
the slot (multiplier of m_μ·F_Bor, or coefficient of m_e). A value match without (ii) is a
reading. Products or sums of candidates are not considered.

Predicted verdict: no candidate gives 12. The value 2 is produced by K3 and K7 (besides the
recorded dim V_(2,1) = 2), so 2 is over-determined and none is selected. Criterion (ii) fails
for every candidate.

Lean: K1, K2 (at a specialisation, see below), K3, K4, K5, K7. K6 is not in Lean
(hyperbolic volume is not in Mathlib); it is computed at 50 dps and the containment
Γ_L ⊂ PSL(2,ℤ[i]) is cited.

## 2. Result

Probe: `computations/probes/proton_two_twelve_count_probe.py` (sympy over ℚ(q); mpmath 50 dps for K6;
no float), output in `proton_two_twelve_count_probe.out.txt`. Lean:
`folio/quantum-observable-universe/lean/QOU/MassTheory/ProtonTwoTwelveCounts.lean`, core Lean 4.24.0
only, `lean` exit 0, no `sorry`, `#print axioms` on the main theorems: no axioms.

**Every prediction held. No candidate gives 12. Two give 2.**

| id | value | Lean | equals 2? | equals 12? |
|---|---|---|---|---|
| K1 centraliser dim | 4 | at q = 2 (`bor21_not_scalar`, `bor_one_dim_blocks`); generic q by sympy | no | no |
| K2 dim ℚ(q)[P] | 3 | at q = 2 (`bor21_no_eigenvalue_one`); generic q by sympy | no | no |
| K3 crossings per component pair | 2, 2, 2 (no self-crossings) | `pairCrossings_bor` | **yes** | no |
| K4 components | 3 | `components_bor` | no | no |
| K5 Seifert χ | −3 | `seifertChi_bor` | no | no |
| K6 [PSL(2,ℤ[i]) : Γ_L] | 24 (exactly: Vol(L) = 2V_oct = 8G, covol = G/3, G Catalan) | not in Lean | no | no |
| K7 rotation orbit of the word | 2 | `rotationOrbit_bor` | **yes** | no |

Generic q for K1, K2. On the (2,1) block P has determinant 1 and characteristic polynomial
x² − t x + 1 with t ≠ 2 (sympy, exact), so P is not scalar there and 1 is not an eigenvalue;
P acts as 1 on the blocks (3) and (1,1,1). Hence dim Z(P) = 1 + 2 + 1 = 4 and the minimal
polynomial is (x − 1)(x² − t x + 1), degree 3. The Lean proofs check these facts at q = 2.
They pass to generic q because "not scalar" and "1 is not an eigenvalue" are each the
nonvanishing of a rational function of q, and a rational function nonzero at q = 2 is not
identically zero.

### Criterion (ii): does any corpus map put a count in the slot?

No. Searched `computations/**/*.py` outside `probes/` for an integer times `m_e`. Every hit
for `12*m_e` or `6*m_e` is the identity itself or an attempt to read it
(`phase5/phase2b_dim_v21_bridge_derivation.py`, `phase2b2_dim_v21_categorical_bridge.py`,
`phase2c_derive_correction_tower.py`, `me_additive_term_structure.py`). None of them computes
a count of the kinds above and feeds it into the formula. The mass map in the corpus is
m = m_e·Vol(K)/ℏ_q²·F; no map turns a count on β_Bor into an m_e-scale term. This is a
search result over that surface, not a proof that no such map can exist.

### Verdict

- **The 12.** Scope (a): none of the seven pre-registered counts equals 12, and none is
  placed in the m_e slot by any corpus map. Together with PR #8804 and the 2026-11-21 −12 audit,
  the count families named in the brief (representation dimensions and multiplicities,
  crossing and strand counts of β_Bor, Euler characteristic, index and orbit counts) do not
  produce 12 under a single definition. The 12 stays a selected constant.
- **The 2.** Over-determined. 2 = crossings per component pair (K3) = rotation orbit of the
  word (K7) = dim V_(2,1) (recorded) = size of the bar pair {(3),(1,1,1)}
  (`phase2b2_dim_v21_categorical_bridge.py`, a sketch). Several unrelated structures give 2,
  and no corpus map selects one of them as the multiplier of m_μ·F_Bor. So the 2 is a
  reading too.
- **Not considered, by the pre-registration.** 24 = 2·12 (K6) is a product. The Whitehead link,
  a different link, has index 12 in PSL(2,ℤ[i]); using it would change the object, so it
  is out of scope and is not evidence.

### What would count as a derivation

Unchanged from the −12 audit: a map in the framework that produces m_e·N with N a
q-independent integer, N = 12 on β_Bor, by construction. This survey adds a scope-(a) negative: the map is not "take one of the seven
pre-registered counts K1–K7", since none of them equals 12. Other counts were not tested.

No number moves.

## 3. The 3 in −12 = −k²·3 (owner request 2026-11-21: "derive 3, show it follows from the mass derivation pipeline")

Reading taken: the −12 audit reduced the term to τ(R_p∘R_p) = −k²·dim W_p, where W_p is the
proton weight space that `hReebP` traces over with the unnormalised `Matrix.trace` on `Fin 3`.
Until now the 3 was the size of that matrix. Lean: `QOU/MassTheory/ProtonWeightSpaceDim.lean`
(core Lean, exit 0; `dim_proton_weight_space`, `charge_iff_one_d`, `kostka_split` use no axioms,
`twelve_iff_weight_two` and `large_weight_misses` use propext and Quot.sound).

**Derived, with two steps cited.** dim W_p = 3 follows from three inputs the pipeline already fixes:
(1) three strands, β_Bor ∈ B₃; (2) V = C² per strand (level-2 Jimbo, `NucleonWeightSpaceTraces`);
(3) the proton sector is the K^{⊗3}-eigenspace of eigenvalue q (`Kp = q • 1`). A state with d
copies of e₂ has weight q^(3−2d); the exponents on (C²)^{⊗3} are 3, 1, −1, −3, so for q not a
root of unity weight q means d = 1, and there are exactly 3 such states, the corpus basis
e₁e₁e₂, e₁e₂e₁, e₂e₁e₁ (`protonStates_eq`). Charge +1 with Q = diag(2/3, −1/3) cuts out the
same 3 states (`charge_iff_one_d`); the neutron sector (charge 0, weight q⁻¹) also has
dimension 3 (`neutron_dim`). Lean proves the exponent step (weight exponent 1 ⇔ d = 1,
`weight_one_iff_one_d`). That q^e = q forces e = 1 for q not a root of unity is stated in prose.
Schur–Weyl splits W_p as V_(3) ⊕ V_(2,1), 3 = 1 + 2. That decomposition is cited. Lean checks only
the arithmetic (`kostka_split`) and that S₃ acts transitively on the three states
(`transitive_on_proton`).

**Scope.** This is the 3 of the two-term Lagrangian route (`CategoricalLagrangianTwoTermBridge`),
which the scoreboard uses by the 2026-11-21 ruling. The production identity in
`canonical_mass.py` uses the H₃ Markov trace and has no weight space in it, so this does not
derive anything in that formula. Input (2), C² per strand, is the corpus's set-up for the
weight-space files, not itself derived here.

**What remains.** With the 3 derived, the −12 holds iff the Reeb square is the scalar −k²·𝟙 with
k = ±2 (`twelve_iff_weight_two`, `large_weight_misses`). Neither the scalar form nor k = 2 is
derived. The current hypothesis `hReebP` is not scalar (`ProtonTwelveOrigin.reebSlot_not_constant`).

## §4. The Reeb weight k, on the KZ realisation (option 1, 2026-11-21)

**Question.** In `−12 = −k²·3`, §3 derived the 3. Does the corpus fix `k`?

**What fixes R.** In the two-term bridge, `R = L_p.dirac.reeb` is free data
(`CategoricalDiracOperator.reeb`). The corpus has one concrete realisation:
`LagrangianKZIdentification.arnold_euler`. It applies on the KZ sector, under that file's
postulates P1–P3, none of which is derived. There the Reeb part is the Euler contraction
`R = Σ_{i<j} 2κ(P_{ij} − c)`. Here `q = e^{2πiκ}` (Lean normalisation, §5.2 of the
Drinfeld–Kohno audit), and the shift `c` is free: the Hecke factorisation holds for every `c`.

**Results.** Lean file `QOU/MassTheory/ProtonReebKZWeight.lean`: sorry-free, `lean -DautoImplicit=false` exit 0. Exact sympy twin: `computations/probes/proton_reeb_kz_weight_probe.py`.

1. On `W_p`, `Σ_{i<j} P_{ij}` is the all-ones matrix `J` (`transpositionSum_eq_ones`).
2. `R∘R` is scalar on `W_p` **iff** `c = 1/2`, for `κ ≠ 0` (`reeb_sq_scalar_iff`). That value is the
   traceless 𝔰𝔩₂ Casimir `P − ½`. This answers the "Reeb square is scalar" gap of §3
   conditionally: it holds on this realisation exactly in the 𝔰𝔩₂ normalisation. It fails at
   the 𝔤𝔩₂ value `c = 0`, where the eigenvalues are 36κ² and 0.
3. At `c = 1/2`, `R∘R = 9κ²·𝟙`, with trace `27κ²` (`trace_reeb_sq_sl2`).
4. That trace equals −12 iff `9κ² = −4`, i.e. `k² = −9κ² = 4` (`trace_eq_neg_twelve_iff`).

**Comparison point (not a proof input).** At the proton pin `q₀`,
`κ₀ = ln q₀ /(2πi)`. This gives `k² = 9(ln q₀)²/(4π²) ≈ 0.002482`, so `k ≈ 0.0498`. Getting
`k = 2` would need `q = e^{±4π/3}` (≈ 65.94 or 0.01516).

**Verdict: scope (a).** On the corpus's one concrete realisation of the Reeb part, `k = 2` is
not produced at the pinned `q₀`; it misses by a factor ≈ 40. The 12 therefore stays a fit
(owner ruling 2026-11-18).

What this does **not** exclude:
- a different realisation of `R`;
- a different coupling normalisation, i.e. a rescaled `κ`.

A rescaling chosen so that `k = 2` would be selection against the target.

## §5. The Reeb weight k, on the Bring-cone Reeb triad (2026-11-21)

**Which realisation.** The corpus has a second concrete Reeb operator. `QOU/BringCone.lean`
defines the Reeb triad as right multiplication `M_u p = p·u` on `ℍ`, for `u ∈ {i, j, k}`.
Right multiplication commutes with left multiplication, so `M_u` is linear for the left
complex structure, with `ℍ = ℂ·1 ⊕ ℂ·j`.

This matches the per-strand `C²` of §3 under `e₁ ↦ 1`, `e₂ ↦ j`, which is a set-up
identification and not derived. In that basis `M_i = diag(i, −i)`. A vector field acts on
three strands by the Leibniz rule: `R = Σ_s M_u^{(s)}`.

**Results.** Lean file `QOU/MassTheory/ProtonReebBringWeight.lean`: sorry-free,
`lean -DautoImplicit=false` exit 0. The sympy twin, `computations/probes/proton_reeb_bring_weight_probe.py`,
builds the matrices from quaternion products.

1. **`u = i`, the K-weight direction.** `R` preserves `W_p`, and `R∘R = −1` on it. So `R∘R` is
   scalar, `k = 1`, and `τ_{W_p}(R∘R) = −3`, not −12 (`reeb_trace_proton`).
2. **Parity.** A state with `d` copies of `e₂` has weight `(3 − 2d)·i`. So `k = |3 − 2d|` is odd
   on three strands, and no weight space has `k = 2` (`weight_ne_two`). The same holds for
   every odd strand count (`weight_odd_of_odd`).
   This is a **scope-(b)** exclusion *within this realisation*, and the invariant is parity.
3. **`u = j` or `k`.** `R` does not preserve `W_p`. The compressed square is not scalar
   (diagonal −3, off-diagonal −2). The Casimir `Σ_u R_u²` on `W_p` has eigenvalues −15 (once)
   and −3 (twice), so it is not scalar either.

The Reeb direction `u` is a recorded open freedom in `BringCone.lean`. For a general pure unit
`u = a·i + b·j + c·k`, the sympy twin shows that `R_u` preserves `W_p` iff `b = c = 0`, i.e.
`u = ±i`. That check is not in Lean.

**Combined with §4.** Neither concrete realisation of `R` in the corpus gives `k = 2`:

| realisation | k on `W_p` |
|---|---|
| KZ (`arnold_euler`) | `3|κ|`; ≈ 0.0498 at `q₀` |
| Bring triad | the odd integer 1 |

The 12 stays a fit. A third realisation, or a rescaling of the triad by 2, would have to be
derived. Choosing either to make `k = 2` would be selection against the target.
