# `normalizedSum n q = 1` closes via the corpus general-X telescope — `qou-3quc` is no longer open math

**Date:** 2026-08-29 · **Beans:** `qou-3quc` (the gap), `qou-x4zl` / `qou-ognw` (the now-optional (B) route) ·
**Probe:** [`fake_degree_via_telescope_probe.py`](../../computations/qbeta/fake_degree_via_telescope_probe.py)
(exact `n≤5`, 3/3) · **Status:** DERIVATION (route verified exact; remaining Lean is mechanical bridging).

## The result

The open residual of the general-`n` fake-degree identity (`MolienFakeDegreeGeneralN`, PR #5948) was
`normalizedSum n q = 1`, with `normalizedSum n q = Σ_{λ⊢n} f^λ · q^{−κ_λ}/hookProd_q(λ)` (balanced
q-brackets, `κ_λ = Σ` contents). `MolienFakeDegreeGeneralN`'s docstring called it a multi-week project
(coinvariant-algebra Poincaré polynomial, or maj-Mahonian + q-RSK). **It is neither** — it closes
directly from the corpus's own **general-X Macdonald telescope**, which landed on `main` after #5948:

```text
QOU.MathlibExt.MacdonaldTelescopeGeneralX.telescope_generalX (n) (Q X : ℝ) (hQ : 1 < Q) (hgen) :
    Σ_{|ν|=n} f^ν · schurElement Q X ν.rowLens = ((1 − X)/(1 − Q))^n           (all X)
```

## The route (verified exact, `n≤5`)

Two facts, both proved exact in the probe:

1. **Convention bridge (per-λ):** the balanced fake-degree summand is the Macdonald Jones–Markov
   coefficient at `Q=q²`, `X=0`:
   `q^{−κ_λ}/hookProd_q(λ) = jonesMarkovCoeff(q², 0, λ) = schurElement(q², 0, λ)·(1−q²)^n`.
2. **Telescope at `X=0`:** `Σ_{|ν|=n} f^ν · schurElement(q², 0, ν) = (1/(1−q²))^n`.

Chaining: `normalizedSum n q = Σ f^λ jonesMarkovCoeff(q²,0,λ) = (1−q²)^n·(1/(1−q²))^n = 1`.

## The convention-bridge algebra (worked, for the Lean formaliser)

`schurElement(q²,0,λ) = Q^{n(λ)}·∏_x 1/(1−Q^{h_x})` with `Q=q²` (the `1−X·Q^{c}` factor is `1` at
`X=0`). Per cell, `1 − q^{2h} = −q^{h}(q−q^{−1})·[h]_q` (balanced), so
`∏_x 1/(1−Q^{h_x}) = (−1)^n q^{−Σh}(q−q^{−1})^{−n}/hookProd_q(λ)`. With `wenzlNormalisation(n,q²,0) =
(1/(1−q²))^n` and `(1−q²)/(q−q^{−1}) = −q`, the sign and `(q−q^{−1})` powers cancel to `(−q)^n`,
leaving `jonesMarkovCoeff(q²,0,λ) = q^{2n(λ)+n−Σh}/hookProd_q(λ)`. This equals `q^{−κ_λ}/hookProd_q(λ)`
iff the **n-statistic identity** `κ_λ = Σ_x h_x − n − 2·n(λ)` holds (`n(λ) = Σ_i i·λ_i`, 0-based) —
verified exact for every `λ⊢n`, `n≤5`.

## Consequence — re-scoping

- `qou-3quc` is **not open math**. It closes by the telescope route; what remains is **mechanical Lean
  bridging** (no open combinatorics): the per-λ convention bridge above (a `foldl` monomial/sign
  identity + the n-statistic identity), and the `Nat.Partition ↔ YoungDiagram` carrier bridge
  (`PartitionsOfBridge` / `SYTEnum.dimSYT_eq_numSYTenum`) that lets `telescope_generalX` (stated on the
  YoungDiagram carrier) apply to `normalizedSum` (stated on `Nat.Partition`).
- The **induction / addable-box (B)** route (`MolienFakeDegreeInduction`, `AddableBoxHookOneRow`,
  `qou-x4zl`/`qou-ognw`) is now an **independent second proof**, not the path. Two independent routes
  to the same identity is a strengthening (parallel-research rule), but (B) no longer needs to be
  driven to close `qou-3quc`.
- This is the affirmative answer to the convergence question posted on #5970.

## Discipline

Route verified exact in `ℚ(q)` (no float); nothing wired; `free_parameters = 0`. Honest status:
the **math** is closed; the **Lean** is reduced to two mechanical bridges to already-proved corpus
theorems, not yet discharged.
