# Coordination ledger — `conj:s5-so3-fiber-action` (the s5-so3 fibre-action keystone)

**Goal.** Discharge the keystone the QOU framework's open derivation math reduces to: the geometric
fibre map `S₅ ⊃ A₅ ≅ I ⊂ SO(3)` tying the partition-wise Wedderburn action on `H₅(q)` (combinatorial)
to icosahedral rotations on Bring's quintic surface (geometric). It is the single open object for
m_τ (lepton tower), GAP-A-3 binding Δ_λ, and GAP-A-4 mass λ(K).

**Status (2026-06-16).** Reduced — by formalize-first pruning — to **one differential-geometry
problem**. Everything combinatorial / representation-theoretic / algebraic is done or refuted; no fit
was introduced anywhere.

## Current state

| Layer | Status |
|---|---|
| Combinatorial backbone `Res^{S₅}_{S₃}` + `SO(3)↓A₅↪S₅` bridge | ✅ verified |
| Geometry: 2I spin lift; geometric A₅ forced to icosahedral T₁; chirality = T₁/T₂ | ✅ verified |
| Algebraic functor target (Bratteli = box removal; Ocneanu trace) | ✅ forced |
| Strand fibre = colour ℂ³ (Schur–Weyl: spinor ℂ² kills the electron (3,1,1)) | ✅ forced |
| Static coupling `V_ℓ→E_λ` (Schur: dim Hom = 1) | ✅ forced |
| **Generation selection ℓ→λ = the Hopf moment map μ** (spatial SO(3)-equivariance) | ✅ **realized** |
| 210 ppb muon mechanism (Wedderburn-projector correction) | ❌ refuted (6–8 orders too coarse) |
| colour⊗spin = (3,1,1) dim-6 shortcut | ❌ refuted (spin-parity mismatch) |
| Reeb-eigenvalue resonance | ❌ refuted (no parameter-free ≥3-anchor match) |
| **OPEN:** Markov-trace weighting `W_λ` via Wu-manifold SU(3)/SO(3) Sasakian equivariant index | ⛔ differential geometry (owner-gated) |

**The single open object.** Does the SU(3)/SO(3) (Wu-manifold) Sasakian with spatial-SO(3)_colour Reeb
admit a structure whose S¹-equivariant index reproduces the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!`?
(dim 5 odd ✓; χ(Wu)=0 ✓ — Boothby–Wang necessary conditions met, not obstructed at that level.) The
sibling A≥3 operator-branching compute (#2369/#2371/#2372) produces `W_λ` algebraically; the open piece
is its *geometric origin*.

## Refutations not to re-walk (canonical-no-negative-result discipline)

1. **210 ppb muon via (1,1,1) sign-block / Wedderburn projector** — the correction is O(16 %) (sign-block)
   to ×15 (channel ratio), 6–8 orders too large for the 209.8 ppb gap; the bare `m_e·Vol(4₁)/ℏ_q²` is
   already good to 209.8 ppb. The structural identity `χ^{(1,1,1)}(β_Bor)=1` is exact but magnitude-wrong.
2. **electron block (3,1,1) = colour ℂ³ ⊗ spin ℂ²** — refuted on the central character (spin parity): (3,1,1)
   is an A₅ rep (central +1), ℂ³⊗ℂ² has central −1. dim-6 = chirality T₁⊕T₂, not a tensor.
3. **Reeb-eigenvalue resonance** — the ℓ=1,2 content matches (`c(λ)=ℓ(ℓ−1)`) are non-unique and fail at ℓ=3
   (tau, multi-block). No parameter-free ≥3-anchor resonance.

## Sessions log

| Date | PR | What landed |
|---|---|---|
| 2026-06-16 | #2352 | S₅↓S₃ backbone + SO(3)↓A₅↪S₅ bridge verified; ing-4/5 close-out (210 ppb **refuted**) |
| 2026-06-16 | #2361 | propagate refutation to the GAP-A-4 doc; ingredient-4 geometric-leg formalize-first prune |
| 2026-06-16 | #2364 | Schur–Weyl: strand fibre forced to colour ℂ³ (spinor kills electron) |
| 2026-06-16 | #2367 | two-Sasakian decomposition; static coupling Schur-forced |
| 2026-06-16 | #2368 | Reeb-eigenvalue resonance **refuted** (numerology-guarded negative) |
| 2026-06-16 | #2370 | canonical coupling = Hopf moment map μ; round-S⁵ colour Reeb transverse; **selection realized by μ** |
| 2026-06-16 | #2373 | Markov-weighting scope: forced `W_λ` + Wu-manifold Sasakian handoff |
| 2026-06-16 | #2369 (sibling) | coordination note: A≥3 `tr_M` compute = algebraic realization of the open weighting |

## Key artifacts

- Audit docs: `docs/audits/2026-06-16-s5so3-*.md` (branching-backbone-verified, ingredient4-fibre-schur-weyl-constraint,
  two-sasakian-construction-attempt, reeb-resonance-probe-negative, hopf-coupling-and-reeb-obstruction,
  markov-weighting-sasakian-scope) + the corrected `2026-06-13-gap-a4-operator-valued-muon-branching.md`.
- Verifiers (all exit 0): `docs/audits/scripts/s5so3_*.py` (branching backbone, ingredient 4/5 markov shift,
  fibre Schur–Weyl, coupling Schur, Reeb resonance, Hopf coupling obstruction, markov weighting facts).
- Lean scaffold: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` (open `partition_to_rotation`).

## Cross-references

- Synthesis: [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md)
- Construction program: [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md)
- Sibling A≥3 compute cluster: #2369 / #2371 / #2372 (produces `W_λ` algebraically)
