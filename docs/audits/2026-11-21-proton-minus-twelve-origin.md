# Origin of the −12 m_e in the proton identity (2026-11-21)

Lean: `folio/quantum-observable-universe/lean/QOU/MassTheory/ProtonTwelveOrigin.lean`. Probe: `computations/probes/proton_twelve_origin_probe.py`. No number moves.

## 1. Pre-registration (written before the probe ran)

Identity under test (convention D, production): m_p/m_e = 2 (Vol(4₁)/ℏ_q²) F_Bor(q) − 12,
F_Bor = tr_M(β_Bor)·[3]_q!/q³, β_Bor = (σ₀σ₁⁻¹)³ = γ(0,0,qh)·γ(0,0,−q⁻¹h) with the ruled photon
γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹. m_μ = m_e Vol/ℏ_q², ℏ_q = 1 − q⁻¹. Electron (ruling 2026-11-21):
σ₀σ₁σ₀ ∈ B₃, Hopf closure. Exact arithmetic (sympy ℚ(q)); q₀ values at 70 dps mpmath, no float.

### Candidates and predictions

C1. Classical limit of the same observable. Prediction: T(q)/m_e = 2Vol·F_Bor/ℏ² has a pole of
    order 2 at q = 1, so it has no finite classical limit; its ℏ⁰ Laurent coefficient carries Vol
    and is not 12. C1 fails as a derivation.
C2. Rewrite in the tower's own scale: 12 m_e = 2 m_μ·ℏ_q²·F_Bor(1)/Vol. Prediction: exact
    algebra; it shows the −12 is an O(ℏ²) term carrying 1/Vol, which no ℚ(q) trace of β_Bor
    supplies. So the −12 must be a separate m_e-scale sector, not a correction to F_Bor.
C3. Two-term Lagrangian slot. τ(L) = q⁻²τ(∇²) + q⁻¹ℏτ(∇R+R∇) + ℏ²τ(R²) + q⁻¹τ(ψ̄ψ∇) + ℏτ(ψ̄ψR).
    Under the scale m_e/ℏ_q², only the Reeb-square term is ℏ-free. Prediction: with the
    corpus hypothesis τ(R_p²) = q·tr(V³_A) (CategoricalLagrangianTwoTermBridge, hReebP) its q = 1
    value is ±3, not ±12, and it is q-dependent at O(h²). C3 fails by a factor of 4 as stated.
C4. Electron-strand subtraction: F_e(q) = tr_M(σ₀σ₁σ₀)·[3]_q!/q³. Prediction: F_e(1) = 3, so
    12 = 4F_e(1) is one more integer reading; F_e is q-dependent at O(h²), so 4F_e(q₀) ≠ 12 by
    O(h²) ≈ 4 %, which would move m_p by O(10 ppm).
C5. Pure integers equal to 6: F_Bor(1), |S₃|, crossing number of V³, −χ(Bring). Prediction: all
    six-valued; nothing in the framework selects one, so each is a reading.

Diagnostic only (not a proof input, not a ranking criterion): at the muon pin the constant that
would make m_p exact is 12 − 4.48·10⁻⁴; a q-deformed constant 12 + a h² needs |a| ≈ 0.01.
Effect on m_n: production m_n = m_p + Q_β + m_e, so any change δc in the constant moves m_n by
exactly −δc·m_e, the same as m_p.

Expected overall verdict: no derivation in classes C1–C4; the −12 is a separate q-independent
m_e-scale term whose origin is not fixed by the framework (scope (a) except C1, which is (b) by
the pole-order invariant).

## 2. Result

Repo `litlfred/qou` @ `845e2f820`. Pre-registration: section 1 above (written before the probe).
Probe: `computations/probes/proton_twelve_origin_probe.py` (exact H₃(q) with sympy, q₀ values at 70 dps mpmath, no float),
output reproduced verbatim on this branch. Lean: `ProtonTwelveOrigin.lean` (12 statements, `import Mathlib.Tactic` only;
compiled, see the end). Framework used: ruled photon γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹, so
β_Bor = (σ₀σ₁⁻¹)³ = γ(0,0,qh)·γ(0,0,−q⁻¹h); electron σ₀σ₁σ₀ ∈ B₃ (Hopf closure); two-term
Lagrangian trace from `CategoricalLagrangianTwoTermBridge.lean`.

### Verdict

**The −12 is not derived, and the framework as it stands cannot derive it as a correction to the
Borromean tower.** Every prediction in the pre-registration held. What the work does establish:

1. **Rewritten in the tower's own scale, the −12 carries 1/Vol.**
   m_p = 2 m_μ (F_Bor(q) − ℏ_q²·F_Bor(1)/Vol(4₁)) (`identity_in_tower_scale`). F_Bor is a rational
   function of q with no Vol in it. So the −12 is not a piece of the Borromean observable. It is a
   separate term at the electron scale m_e (CAL-1), with no ℏ_q and no Vol.
2. **"Subtract the classical limit" fails as a derivation, structurally.** The tower
   T/m_e = 2 Vol F_Bor/ℏ_q² has a pole of order 2 at q = 1 (`tower_has_double_pole`). Exact Laurent
   series in ℏ = ℏ_q: 2F_Bor/ℏ² = 12/ℏ² − 36/ℏ + 58 − 56ℏ + O(ℏ²). So the classical limit is
   infinite, and the ℏ⁰ coefficient is 58·Vol, not 12. The 12 equals the **pole coefficient with Vol
   stripped off**. Stripping Vol (equivalently, swapping the scale m_μ → m_e) is the step nothing in
   the framework supplies. Scope (b) for this reading, by the pole-order invariant.
3. **The two-term Lagrangian has exactly one slot of the right shape, and it gives −3, not −12.**
   With scale m_e/ℏ_q², τ(L) = q⁻²τ(∇²) + q⁻¹ℏτ(∇R+R∇) + ℏ²τ(R∘R) + q⁻¹τ(ψ̄ψ∇) + ℏτ(ψ̄ψR); only
   the Reeb square ℏ²τ(R∘R) lands at scale m_e with no ℏ. Under the corpus hypothesis
   τ(R_p∘R_p) = q·tr(V³_A) (`hReebP`), its value at q = 1 is −3 (`reebSlot_one`) and it moves at
   O(q−1). Off by a factor of 4. Scope (a).
4. **The electron strand gives another integer reading, not a derivation.** tr_M(σ₀σ₁σ₀) =
   q³(q⁴+1)/(q²+1)² (`trMe_closed`), F_e(1) = 3 (`fE_one`), F_e = 3 + (17/2)(q−1)² + …. So
   12 = 4·F_e(1) too. Scope (a).
5. **The value 12 is over-determined by readings.** 12 = 2·F_Bor(1) = 4·F_e(1) = 2·|S₃|
   (`twelve_readings`), and also 2 × (crossings of V³) and −2·χ(Bring), the last flagged as
   numerology in the 2026-11-15 sidecar review (`qou-zxuy`). Nothing in the framework picks one, so
   each is a reading. The corpus already records this (2026-05-25 audit, 2026-06-01 re-exam: "4
   natural categorical candidates hit 12 exactly").

### Diagnostic (comparison only, not a proof input, not a ranking)

At the muon pin (CODATA 2022, q₀ = 1.1099785956427…), the constant that would make m_p exact is
c = 11.99955. A q-deformed constant 12 + a·h² needs |a| ≈ 0.01. Every q-dependent candidate above
has |a| of order 1:

| constant used | value at q₀ | m_p vs CODATA (ppb) | shift of m_p and m_n vs c = 12 |
|---|---|---|---|
| 12 (production) | 12 | −243.9 | 0 |
| 4·F_e(q₀) | 12.3735 | −203 640 | −0.191 MeV |
| −4·q·tr(V³_A)(q₀) | 13.2939 | −704 939 | −0.661 MeV |
| 2·F_Bor(q₀) | 8.9383 | +1 667 223 | +1.565 MeV |

So whatever the −12 is, the data say it must be q-independent at the 1 % level of h²: a count or a
dimension, not a trace evaluated at q₀. This narrows the search; it does not pick a candidate.

### What it does to m_p and m_n

- No number moves. Keeping c = 12 leaves m_p at −243.9 ppb (muon pin), as before.
- m_n = m_p + Q_β + m_e in production, so the −12 enters m_n one-for-one: any change δc moves m_n
  by −δc·m_e, exactly as it moves m_p. The 4.5·10⁻⁴ m_e gap at the muon pin is 0.23 keV.
- For sibling (2) (m_n by its own identity): a neutron analogue m_n/m_e = 2(Vol/ℏ²)F_n − c_n has
  the same problem. c_n would be a second selected integer unless the origin of c is found first.

### What would count as a derivation

A map in the framework that produces a term m_e·N with N a q-independent integer and N = 12 on the
proton, by construction rather than by matching. The obvious place is the Reeb-square slot (finding
3): it needs τ(R_p∘R_p) = −12 for all q, where the current hypothesis gives q·tr(V³_A) = −3 + O(q−1).
That is a statement about the Reeb operator, and the corpus does not derive τ(R∘R) at all (it is a
hypothesis in the bridge file).

### Lean status

`ProtonTwelveOrigin.lean` compiles with lean-direct (Lean 4.24.0, restored Mathlib cache), exit 0, no warnings, no `sorry`. `#print axioms` on the five main theorems: `propext, Classical.choice, Quot.sound` only.

## 3. The Reeb square τ(R_p∘R_p) as the −12

Pre-registered before any computation (R1–R3): for the Reeb-square slot to *be* the −12 m_e term,
τ(R_p∘R_p) must equal −12 for every q.

Corpus grep (2026-11-21): τ(R∘R) is never derived. It appears only as the hypothesis `hReebP`
(τ(R_p∘R_p) = q·tr(V³_A)) in `CategoricalLagrangianTwoTermBridge.lean`, and as the Stokes
hypothesis `hStokes` (R∘R = leftMul(hol w) ≫ massIntegrand, with w free) in
`reeb_holonomy_leftTrace_eq_functional_hol`. No file fixes a Reeb weight or charge for the proton.

Results (all in `ProtonTwelveOrigin.lean`, sorry-free, axioms propext/Classical.choice/Quot.sound):

- **R1, `reebSlot_not_constant`.** No constant equals q·tr(V³_A) for all q (−3 at q = 1,
  1509/32 at q = 2). So `hReebP` cannot be the −12 term at any normalisation. Scope (b), by
  non-constancy, for the `hReebP` reading only.
- **R2, `trace_scalar_square`, `weight_space_weight_eq_two`, `normalised_no_integer_weight`.**
  If the Reeb generator acts as a circle action of integer weight k (R∘R = −k²·𝟙), then
  τ(R∘R) = −k²·dim. On the 3-dimensional (2,1) weight space that `hReebP` traces over, −12 forces
  k = ±2. With a normalised trace (τ(𝟙) = 1) no integer weight gives −12. A Casimir reading
  (−ℓ(ℓ+1), ℓ = 3, the T₂/G level in `ReebChiralitySeparation.lean`) gives 12 too.
- **R3.** R1 and R2 are incompatible: a scalar Reeb square has constant trace, `hReebP` does not.

**Verdict.** The Reeb-square route does not derive the −12. It reduces it to one statement,
"the proton's Reeb weight on its weight space is 2", which nothing in the corpus fixes, and it
shows that `hReebP` must be dropped if the −12 is to come from this slot. This is a reduction,
not a derivation; the −12 stays a selected constant.
