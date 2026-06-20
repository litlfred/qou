# ³He G2+G4 construction recipe — `conj:canonical-knot-id-sdp` first bite

**Date:** 2026-06-06
**Status:** executable recipe (design step); **code-writing + verification needs a
working Lean env** — the QOU SDP cone does not build against the off-pin Mathlib in
the current sandbox, and the SDP types are too entangled to mock-verify standalone.
**Parent scope:** [`docs/scope/2026-06-06-conj-canonical-knot-id-sdp-scope.md`](../scope/2026-06-06-conj-canonical-knot-id-sdp-scope.md) §5.

This turns the scope doc's "de-risked first bite" (gates **G2** real instance + **G4**
certificate, for ³He) into concrete Lean construction steps grounded in the infra that
already exists on the branch. **Honest correction to the scope doc:** after reading the
infra, the bite is *less* de-risked than §5 implied — the crux (`dualSlack PosDef` for a
*non-trivial* cost) is the real work, not sidesteppable. This recipe makes that crux
explicit and gives the two routes through it.

---

## What exists today (the trivial shell to replace)

[`QOU/BraidKnot/NucleusEmptySDPUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean):

- `nucleusEmptySDP n : SDPPrimal (heckeDim n) ℝ Empty` — cost = `1` (identity), **`ι = Empty`**
  (no constraints), optimum `Φ⋆ = 0` (`rfl`).
- `nucleusRealStrongDualityPair n : RealStrongDualityPair (nucleusEmptySDP n)` — `Φstar = 0`,
  `ystar = Empty.elim`, `dualSlack = 1` (PosDef trivially, `Finset.sum_empty`).
- `nucleus_uniqueness_closed n` — sorry-free uniqueness via
  `real_strict_complementarity_unique_of_dualSlack_posDef`. **Trivial** (optimum is 0).

The engine `real_strict_complementarity_unique_of_dualSlack_posDef`
([`QOU/MathlibExt/SDPRealUniqueness`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/SDPRealUniqueness.lean)) is **proved** and is what we ride: given a
`RealStrongDualityPair` whose `dualSlack` is **PosDef** (interior optimum), the
feasible-and-optimal matrix is unique. The B–V boundary axiom
(`strict_complementarity_unique_axiom`, gate **G3**) is **not** needed when the optimum
is interior — and ³He's R5 witness reports `α_gap = 0` (on the structural target),
which is the interior signal. **That is why ³He is the bite.**

---

## Step G2 — the real ³He instance

Replace `nucleusEmptySDP 9` with `helium3SDP : SDPPrimal (heckeDim 9) ℝ ι` carrying the
actual confinement data (`n₀ = 3·A = 9`, `A = 3`):

- **cost** — the binding-residual quadratic of the multi-term mass formula
  `ρ·[tr_M(T_w) + tower(T_w) + tr_M(C_{dimq})]·𝔈₀ − B_AME(³He)`², with `ρ = 2`,
  `B_AME = 7.7181 MeV`. Pull the numeric coefficients from
  [`r5-full-canonical-knot-solver.witness.json`](../../computations/r5-full-canonical-knot-solver.witness.json)
  (the `³He` row: PSD-feasible, α⋆ = 0, recovered word `(σ₁σ₂⁻¹)³` in the `(2,1)`
  Wedderburn block).
- **constraints `ι`** — encode the `Δ_max` Frobenius ball
  ([`prop:delta-max-uniform-bound`](../../content/quantum-observable-universe/mass-theory/)).
  `ι` is **no longer `Empty`** — this is the substantive difference from the shell.
- **rhs** — the constraint bounds.

Concretely: keep the `SDPPrimal` structure shape (`cost`, `constraint`, `rhs`) but
instantiate `ι := Fin k` for the `k` active constraints from the witness's `active_set`,
and set `cost` to the binding-residual Hessian rather than `1`.

## Step G4 — the strict-complementarity certificate

Construct `helium3RealStrongDualityPair : RealStrongDualityPair helium3SDP`:

| field | value | source |
|---|---|---|
| `Φstar` | `heckeAsMatrix` of the L_6a4 canonical element (**not** 0) | witness recovered word `(σ₁σ₂⁻¹)³` |
| `ystar` | the dual variables | witness `y_star` / `active_set` |
| `primal_feas` | feasibility of `Φstar` | witness PSD-feasible flag |
| `dualSlack_psd` | **the crux — see below** | — |
| `obj_eq_dualObj` | strong duality | witness `|primal_obj − dual_obj| ≤ 10⁻⁶` |

## The crux — proving `dualSlack PosDef`

`S(y⋆) = cost − Σ_i y⋆_i A_i`. The shell got `S = 1` for free; the real instance must
prove `S(y⋆)` PosDef. Two routes:

1. **Interior route (preferred, matches α_gap = 0).** Certify the **minimum eigenvalue**
   of `S(y⋆)` is `> 0` from the witness, then lift to a Lean `PosDef` proof
   (e.g. via `Matrix.PosDef` from a Cholesky factor or a Gershgorin/`λ_min ≥ ε > 0`
   bound emitted as a witness field). This **avoids G3's B–V axiom**. Requires the
   witness to record `dualSlack` (or its eigenvalues) — **add this to
   `r5_full_canonical_knot_solver.py`'s emitted witness** (LP/SDP dual discipline,
   AGENTS.md §"LP / SDP duals").
2. **Boundary route (fallback).** If `S(y⋆)` is only PSD (not PosDef — boundary
   optimum), invoke `strict_complementarity_unique_axiom` (gate **G3**, currently an
   axiom). Then the result is conditional on that axiom.

## Step — wire the uniqueness

Pseudocode (mirrors the proved `nucleus_uniqueness_closed` signature; the
optimum `Φstar` is L_6a4's matrix, not 0):

```lean
theorem helium3_canonical_uniqueness
    {Φ' : Matrix (Fin (heckeDim 9)) (Fin (heckeDim 9)) ℝ}
    (h_feas : helium3SDP.IsFeasible Φ')
    (h_obj  : helium3SDP.objAt Φ'
              = helium3SDP.objAt helium3RealStrongDualityPair.Φstar) :
    Φ' = helium3RealStrongDualityPair.Φstar :=
  real_strict_complementarity_unique_of_dualSlack_posDef
    helium3RealStrongDualityPair helium3_dualSlack_posDef h_feas h_obj
```

## G1 caveat (identity, not just optimum)

Even with the above, `heckeAsMatrix` is the **rank-1 `x⊗x` stub** (non-faithful), so
"unique matrix optimum" does not yet give "unique Hecke element / unique knot." For ³He
*specifically*, the χ-fingerprint match (recovered word `(σ₁σ₂⁻¹)³` = the L_6a4 KLR
canonical class) is a **weaker identity argument** that may suffice without the full
faithful Wedderburn-block representation (gate **G1**, the open Hoefsmit Lean port).
State the ³He result with that caveat; full faithfulness is a separate multi-session port.

---

## Execution checklist (fresh session, working Lean env)

1. [ ] Add `dualSlack` (+ `λ_min` certificate) to `r5_full_canonical_knot_solver.py`'s
       witness emission (per the SDP-dual discipline).
2. [ ] Define `helium3SDP` (real cost + `Δ_max` constraints, `ι ≠ Empty`).
3. [ ] Define `helium3RealStrongDualityPair` (Φstar = L_6a4 matrix, ystar from witness).
4. [ ] Prove `helium3_dualSlack_posDef` via the interior route (λ_min > 0 from witness).
5. [ ] Wire `helium3_canonical_uniqueness` through the proved interior-case engine.
6. [ ] State the G1 identity caveat (χ-fingerprint, not faithful rep).
7. [ ] `lake build QOU.BraidKnot.<module>` green; update `conj-canonical-knot-id-sdp.ts`
       `lean.ref` to the **non-trivial** theorem (replacing the trivial-shell ref).
8. [ ] Update the conj `.md` to annotate that the prior `lean.ref` was a trivial shell.

This bite closes ³He only. ²H (needs multi-term cost wiring) and ³H (needs H₅ Hoefsmit)
follow; binding-K uniqueness (gate G5) is the thread-4 object.
