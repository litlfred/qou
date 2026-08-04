---
# qou-j16x
title: 'GAP: multiplicative interface 4-body cumulant b4 undershoots He4 target (6.3% production / 36% bar-invariant)'
status: todo
type: task
created_at: 2026-08-02T18:36:28Z
updated_at: 2026-08-02T18:36:28Z
---


## What was attempted (Option-E front 4, 2026-08-02, PR #4605)

The **multiplicative** connected 4-body Ursell cumulant of the canonical
interface binding `B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)`, evaluated 0-fit at q₀ on the
complete-graph K_A topology, `b₄ = fourthDiff(B(A))` with isospin-symmetric B(3).

- **Result (scope-a undershoot):** production `pn=z` → b₄ = 0.5826 MeV = **6.30 %**
  of the ⁴He AME target (9.243 MeV); bar-invariant `pn=z−h/2` → 3.369 MeV = **36.4 %**.
- **Cause:** `(1−∏f)` saturates (∏f→0 with more bonds), so B→E₀·τ_vac and the only
  A-growth is the weak τ_p^Z τ_n^N. A *multiplicative* interface product cannot be
  the missing operator.
- **NOT scope-b:** the multiplicative form *does* carry connected 4-body content
  (Lean `multBinding_b4_nonvacuous` = 3 ≠ 0), unlike the additive forms
  (`BodyOrderCumulant.fourthDiff_linear/pairwise` = 0).

## Surviving gap / next honest step

The missing ~94 % (retained) / ~64 % (bar-mixed) needs a **non-saturating**
connected 4-body operator (4-body cumulant that *grows*, not saturates). On the
board, not re-attacked here:
- `A4InterfaceMagnitude` one-scalar gate: a categorical principle fixing the
  `[1⁴]` exchange magnitude `m ∈ (0,1/√5)` strictly below the naive `z`.
- The anti-self-adjoint GGM/Stokes off-block the branching leaves free
  (`A3OffBlockDerivation`, `conj:qdifference-kernel-prolongation-symbol`, bean qou-jqof).

## Artifacts
- Probe: `computations/deltalambda/b4_multiplicative_cumulant_probe.py` (+witness)
- Lean: `content/quantum-observable-universe/lean/QOU/MassTheory/B4MultiplicativeCumulant.lean`
- Audit: `docs/audits/2026-08-02-option-e-b4-multiplicative-cumulant.md`
- PR: #4605  ·  Nothing wired; B_AME diagnostic-only; free_parameters=0.

---

## Verdict on candidate (1) — the A4InterfaceMagnitude det-gate (2026-08-02, PR #4620)

**Crux answered:** can the det-gate magnitude `m` be DERIVED (not fitted)?
`b₄(m) = −ln det(I+m·S) = −ln[(1−5m²)(1−m²)]` (derived spectrum {±√5,±1}), normalized
`MeV = E₀·(−ln det)` (corpus writhe witness; E₀ ≈ 4.18598 MeV — CONFIRMED). The sibling
`A4InterfaceMagnitude` already proved this form **surjective** ⇒ inverting the target is a
FIT. This PR does the DIAGNOSTIC: required `m* = 0.416421`; test it against every derived
constant, 0-fit.

- **Forward test (plug derived constants in AS m, zero inversion):**
  `2h`=0.41812 → **102.6 %**, `h/z`=0.41869 → **103.5 %** (both OVERSHOOT);
  `z−h/2`=0.39479 → 76.1 %, and everything below (`1/√5−h/2`, `√(hz)`, `h+(q₀−1)`, …)
  → ≤46 % (UNDERSHOOT).
- **`m*` matches NO derived constant to framework precision.** Nearest is `2h`, off by
  0.41 % in `m` / 2.56 % forward (~10⁷× the L1 floor). Per the c_k near-match discipline a
  2.6 % "near-match" of `2h` is fitted-adjacent, **not** an identity.

**VERDICT: scope-(a) fit-needed — candidate (1) does NOT close.** The required magnitude
is *bracketed* by derived constants (`z−h/2` below, `2h` above) but supplied by none. No
categorical driver fixes `m`. Nothing wired; `m*`/B_AME diagnostic-only; free_parameters=0.

**Surviving sub-question:** is there a categorical principle giving a per-pair magnitude in
the band (0.395, 0.418) landing at 0.41642? The `2h`/`h/z` proximity hints a bar-odd-doubled
amplitude but is not derived — a near-coincidence to test, not a lead to wire. Candidate (2)
(A3OffBlockDerivation / qou-jqof) remains unassessed here.

- Probe: `computations/deltalambda/b4_nonsaturating_mstar_diagnostic.py` (+witness, 50 dps)
- Lean: `content/quantum-observable-universe/lean/QOU/MassTheory/B4NonSaturatingBracket.lean`
  (sorry-free, lean-direct exit 0: `required_magnitude_strictly_bracketed`,
  `no_endpoint_reproduces_target`, `detGate_no_endpoint_hits`, `a4_magnitude_bracketed_scope_a`)
- Audit: `docs/audits/2026-08-02-b4-nonsaturating-mstar-diagnostic.md`  ·  PR #4620.
