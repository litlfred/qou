# Δ_λ: the Borromean 3-body MAGNITUDE lift — H₉ joint-trace, scope-(a) NEAR-MISS LEAD (2026-07-26)

**Branch.** `claude/deltalambda-borromean-magnitude-lift-2026-07-26` (PR #4364).
**Predecessors (proved, merged).** #4360 (`BorromeanThreeBodyCluster`, sorry-free)
— Borromean cluster **sign** `c₃^Borr = E₀·(1−τ_Borr) > 0` supplies μ₃=+0.4708>0;
#4354 (`Mu4RhoFCluster`, sorry-free) — the pairwise multiplicative route is
provably `≤ 0`; #4320 (`AdditiveResidualSimplex`) — the Δ_λ residual moments
`μ₂=0, μ₃=+0.4708, μ₃=−4.591`.

## The one honest gap #4360 left

#4360 derived the Borromean cluster **sign** but at the **bare `H₃`** level:
`c₃^Borr = E₀·(1−τ_Borr) ≈ +0.006 MeV`, **~78×** below μ₃=+0.4708 (~264× below the
ρ_F ~1.5 MeV joint-trace scale). Sign derived; **magnitude open.** The bare `H₃`
value is not the same computational level as the ρ_F pairwise cluster it is
compared against — #4354's `⟨T,³He⟩ = −1.587 MeV` was the **H₉ joint-trace**
`g(word) = Σ_{λ⊢9} y_λ·|χ_λ(word)|·E₀` (`three_body_joint_trace_a3.py`), a
nucleon-dressed 9-strand trace with the `y_λ` Wedderburn weighting.

## The apples-to-apples test (this session)

Lift the Borromean cluster to the **same H₉ perblock level** ρ_F used, 0-fit:
- **Same** `E₀`, **same** `y_λ` over partitions of 9, **same** `_perblock` kernel
  (`chi_q_atomic_all_partitions(9,·)`) as `three_body_joint_trace_a3._perblock`.
- **Faithful cabled Borromean linking** `inter = (Δ_A·Δ_B⁻¹)³`, each nucleon a
  width-3 **cable**: `Δ_{a=0,w=3} = (σ₂σ₁σ₀)(σ₃σ₂σ₁)(σ₄σ₃σ₂)` (descending-run
  block-transposition), `Δ_B` its shift to gens 3..7. Every crossing a Hecke
  element `c·σ_g+d·I` (`σ_g→(1,0,g)`, `σ_g⁻¹→(1,−h,g)`). 54 elementary crossings.
- **Level FIXED** (H₉, three cables) ⇒ **0 free parameters.** μ₃ never inverted.

Probe: [`computations/deltalambda/borromean_h9_magnitude_lift_probe.py`](../../computations/deltalambda/borromean_h9_magnitude_lift_probe.py)
· witness `borromean-h9-magnitude-lift.witness.json`.

## Result — the numbers (0-fit)

| Level | dimensionless deficit | c₃ (MeV) | vs μ₃=0.4708 |
|---|---|---|---|
| bare `H₃` (#4360) | `1−τ_Borr` = 0.00144 | +0.006 | ~78× short |
| **H₉ bare 9-strand cable** | 0.0494 | **+0.207** | 0.44× |
| **H₉ atom-dressed `T`** | 0.0717 | **+0.273** | 0.58× |
| **H₉ atom-dressed `³He`** | 0.0732 | **+0.321** | 0.68× |
| **H₉ ⟨T,³He⟩ mean** | — | **+0.297** | **0.63× (~1.6× short)** |

- Same **+ sign** at every level (sign derived, #4360).
- **~49× lift** over bare-`H₃` (0.006 → 0.297 MeV), recovering the **order of
  magnitude** of μ₃ (0.63×), 0-fit.

## Why the lift is a DERIVED coefficient enhancement, not a fit (the key check)

**MEASURED leading `h`-exponent of the cabled deficit = 4.098** (fit across
q∈{1.02,1.04,1.08}) ⇒ **`O(h⁴)` CONFIRMED.** The cabling **preserves** the
Brunnian order-suppression: exactly like the bare `H₃` closed form
`1−τ_Borr = h⁴(3+h²)/(h²+4)`, the cabled 54-crossing trace is `O(h⁴)` — every
2-sub-link trivial kills `O(h), O(h²), O(h³)`. Channel deficits confirm the
cancellation: `(Δ_A)³ = −0.125`, `(Δ_B⁻¹)³ = +0.973` are large/non-Brunnian, but
the Borromean combination `(Δ_A·Δ_B⁻¹)³ = +0.049` is the small `O(h⁴)` value.

Therefore the `~49×` lift lives **entirely in the `h⁴`-coefficient** `κ_{H₉}/κ_bare`
(three width-3 cables ⇒ `~49×` more `h⁴` strand-pairs) — a **derived coefficient
rescale**, NOT an order change and NOT a tuned factor. This is formalized:
[`QOU/MassTheory/BorromeanMagnitudeLift.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BorromeanMagnitudeLift.lean)
(sorry-free, lean-direct exit 0):

- `brunnianDeficit κ h = h⁴·κ h`; `bare_deficit_eq_brunnian`, `kappaBare_pos`.
- **`lift_is_coefficient_ratio`** — two levels' lift = `κ₁/κ₂` (the `h⁴` cancels):
  a level lift **cannot change the leading `h`-order**.
- `magnitude_closes_iff` / **`not_closed_at_H9`** (`0.297 ≠ 0.4708`) /
  `borromean_H9_near_miss` (positive AND not `= μ₃`).

## Verdict — scope-(a) NEAR-MISS LEAD (STRICT honesty)

**NOT a closure**: the derived H₉ value 0.297 does not land +0.4708 (~1.6× short).
**NOT a fit**: level fixed, 0 params, μ₃ never inverted, no multiplicity/width
tuned to the target. **NOT a hard wall**: right **sign** and right **order** (`O(h⁴)`,
0.63× μ₃). The residual **1.6×** is a **coefficient** question (cable width / tower
height), NOT an order one. Closing it by a tuned cabling/multiplicity to hit
+0.4708 would be a **FIT** and is **declined** ("no seventh fit-based ansatz";
PROBE-4 KL-prune stands).

**Standing:** the Borromean route now has the derived **sign** (#4360) AND the
derived **order of magnitude** (this session, 0-fit, 0.63× μ₃ at the fixed H₉
level). The exact coefficient identity `E₀·κ·h⁴ = μ₃` is **OPEN**. Free-param
count **0**. Nothing wired.

**Next derive-or-refute (no fit).** The residual 1.6× is a coefficient; a *derived*
route to it would be: (i) the s5-so3 `W_λ` level = nucleon-count enhancement (WRT
invariant, owner-opened keystone) computed as `κ_{W_λ}`; (ii) the A=4 tower `H₁₂`
coefficient for μ₄; (iii) an independent derivation of `κ` from the cabling
framing. Each must land the coefficient 0-fit or wall; μ₃ stays a target only.
