---
# qou-e4ri
title: '§7c push: HeckeAlgebra/Torsion/AlgebraicSubstrate cluster (JonesMarkovWenzl, YekutieliTriple, quantum_dilogarithm, QVonMangoldtFunction, QChebyshevFunction, WedderburnBlockDecomposition) to generic R'
status: todo
type: task
priority: normal
created_at: 2026-08-01T23:07:47Z
updated_at: 2026-08-15T14:53:56Z
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | baseRing | verdict |
|---|---|---|---|---|---|
| `JonesMarkovWenzl` | 26 | n | n | warn | **CANDIDATE** — largest in cluster |
| `YekutieliTriple` | 11 | n | n | warn | **CANDIDATE** |
| `quantum_dilogarithm` | 10 | n | n | pass | **CANDIDATE** — dilog is classically archimedean; adjudicate carefully |
| `QVonMangoldtFunction` | 3 | n | Y | pass | ℝ-typed **with** §7c banner — adjudicate |
| `QChebyshevFunction` | 5 | n | n | pass | **CANDIDATE** |
| `WedderburnBlockDecomposition` | 0 | Y | Y | warn | **DONE** — `(R : Type*) [Field R]`; the ~15-extender restructure `z1lz` deferred has since landed |

1 of 6 already done. Note the dilog files were flagged in the 2026-06-25 audit as *legitimately* archimedean — do not assume CANDIDATE means bug.


### Adjudicated: `QChebyshevFunction` is NOT a violation — correcting my own CANDIDATE call

The triage table above lists `QChebyshevFunction` as **CANDIDATE** (codeℝ=5, banner=n). **That call is wrong and is retracted.** Adjudicating the content — as the table itself demands before acting — shows the ℝ is correct:

1. **The summands are legitimately ℝ.** `psi_def` sums `Lambda_q`, the weight from the sibling `QVonMangoldtFunction`, whose own §7c note records it as *"archimedean over ℝ, since the weight `N(𝔪)^{ℏ_q}` is a real power"* (`Real.rpow`; hence its `Analysis.SpecialFunctions.Pow.Real` import). A sum of legitimately-ℝ weights is legitimately ℝ.
2. **The cut-off is an ordering.** `ideals.filter (fun m => N m ≤ X)` — ordering is archimedean content, and it is the *definitional* content of a prime-counting partial sum, not incidental.

Corroboration: `q-geometric-langlands/explicit-formula.lean`'s own `QChebyshevFunction hbar_q hbar_pos ideals X` carries a **positivity hypothesis** `hbar_pos`.

Generalising to `{R : Type*} [CommRing R]` would be *unfaithful* — it would have to drop either the real power in the weights or the order relation in the cut-off.

**Action taken instead of a port:** added the missing §7c banner to the module docstring recording exactly this, so sweeps stop re-flagging it (it read as a bare ℝ-typed module in an `AlgebraicSubstrate` namespace with no stated reason — which is precisely why it scored CANDIDATE). Compile-verified after the edit: `lean-direct-cone → ok=1`.

**Method note for the remaining CANDIDATEs in this cluster:** `banner=n` measures *documentation*, not *correctness*. Check the **sibling/definition chain** before porting — a file can inherit legitimate ℝ from the module that defines its summands. `quantum_dilogarithm` is the next most likely instance of this same pattern (the 2026-06-25 audit already lists the dilog files as legitimately archimedean).
