# Workplan — keystone geometric `W_λ` realization tranche (A/B/C)

**Date:** 2026-06-25
**Branch:** `claude/keystone-geometric-wlambda-2026-06-25`
**Owner-gate status:** the hard core (**G1** — the differential-geometric construction of the
S³/2I Seifert–Chern–Simons equivariant index whose Reeb-equivariant evaluation reproduces `W_λ`)
is the owner-authorized (2026-06-19 narrow reversal) but **research-level DG** object. It is **not**
attempted here — faking a DG derivation would violate the no-fit / honesty discipline. This tranche
lands the **tractable, on-target slices around** G1, per the
[full-Hecke geometric-index program](../scope/2026-06-24-keystone-fullhecke-geometric-index-program.md)
(phases G1–G4) and the keystone ledger [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).

## Context (what is already done — do NOT re-derive)

The geometric leg is heavily mapped already: the Beasley–Witten mechanism (`w_λ = d_q²/D²`, #2524),
`Reeb = Res^{S₅}_{S₃}` (#2704), the proved defect cubic `144·C(n) = −n(n−1)(2n−13)` with the n=7
sign flip (`WLambdaDefectClosedForm.lean`), the normalization story `w_Planch = (F/D²)·W_Key`
(`WLambdaNormalizationInvariance.lean`), and — new on main this session — the genuine
**conjugation symmetry** `W_λ = W_{λ′}` (`qPlancherelWeight_conj`, #2794). The SU(2)/WRT sub-route is
foreclosed (#2717); the arena is full-Hecke principal specialization.

## This tranche

### B — formalize the **G2 falsifiable gate** (lead deliverable)

The decisive gate (program §G2): *the equivariant index's 2nd heat-kernel coefficient `a₂(n)` must
equal the proved cubic `C(n)` for every `n`, including the n=7 sign flip.* New file
`KeystoneG2Gate.lean` formalizes this as a machine-checkable specification with **teeth**:

- a carrier `WLambdaHeatKernelCandidate` for a candidate index's cleared 2nd coefficient `a₂ : ℤ → ℤ`;
- `PassesDefectGate I := ∀ n, I.a₂ n = WLambdaDefect.n144C n`;
- `defectGate_unique` — the gate pins `a₂` uniquely (two passing candidates agree);
- `defectGate_forces_cubic` — passing ⇒ `a₂ n = −n(n−1)(2n−13)`;
- `defectGate_forces_sign_flip` — passing ⇒ `a₂ 6 > 0 ∧ a₂ 7 < 0` (**the falsifiable n=7 discriminant**:
  any geometric index passing G2 *must* exhibit the sign flip).

Honest scope: this formalizes the *specification a candidate must meet*; it does **not** construct the
index (G1). It also records, as a separate predicate, the per-λ conjugation-symmetry target (4),
which is an *independent* condition (a summed-defect match does not force per-λ symmetry — the two
targets are genuinely distinct).

### A — de-vacuify `Cl3Zeta5GeometricRealization` (bean 5e79 / T1)

The §3b conjecture class currently carries a **free** `cl3Zeta5 : ℝ` field, which makes
`exists_realization : ∃ g, realize g = cl3Zeta5` near-vacuous (the target value is unconstrained).
The available infra (`Cl3Zeta5OrbitSum.orbit_sum_identity`: `Cl₃(2π/5)+Cl₃(4π/5) = −(24/25)ζ(3)`,
`Infra.Polylogarithm`) has **no concrete Clausen `Cl₃` evaluation** — so the value cannot be pinned
to a closed number. The faithful slice: constrain `cl3Zeta5` by the **proved orbit-sum identity**
(wire the class field to `cl3OrbitSumPredicted`), so the realised value is no longer arbitrary.
Residual gap (a Mathlib Clausen-at-root-of-unity formalization) is flagged, not faked.

### C — Bring/Jacobian monodromy **operator** (program §(d) sub-lead; numerology-guarded)

Formalize the W-plane elliptic fibre `E = Bring/S₄` monodromy as a structural **operator**
(`conjecture`/§3b class), never the `τ = 2.6424` trace value (the numerology guardrail: matching one
scalar is not a derivation). Honest outcome is a faithful conjecture-class capturing the
Gauss–Manin monodromy hypothesis, with the falsifiable functional-level target (the whole
`(n−1,1)` family, not a one-number coincidence) stated — not a closure.

## Discipline

No fit; `q₀` only as an evaluation point; the no-7th-ansatz rule stands. Every file lands with
`lean`-direct verification (`lake build` rebuilds Mathlib from source in-sandbox, so lean-direct is
the gate per CLAUDE.md). G1 stays owner-gated and explicitly out of scope.
