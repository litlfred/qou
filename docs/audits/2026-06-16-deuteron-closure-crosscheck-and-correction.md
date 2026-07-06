# Deuteron-closure cross-check — and a correction: the Δ_λ Σ-formula does NOT close the deuteron (E₀×q⁻¹ does)

**Date:** 2026-06-16
**Branch:** `claude/option-e-deuteron-closure-crosscheck-2026-06-16`
**Status:** verification cross-check (canonical compute now runnable) + surgical correction of a closure-framing
conflation in the merged #2386 and the Option-E ledger.
**Discipline:** corpus-grep + critical-distance (run the canonical compute before asserting closure; correct an
overclaim honestly).

## What was cross-checked

With the compute located at `computations/`, I ran the canonical deuteron-binding script
[`computations/binding_energy_categorical_deuteron.py`](../../computations/binding_energy_categorical_deuteron.py)
to independently confirm the per-block Δ_λ binding formula. Result (reproduced verbatim):

```
B(K) = m_e × |Σ_λ y_λ χ^λ sgn f^λ|
B(D) predicted = m_e × |-0.7439| = 0.380132 MeV
B(D) AME 2020  = 2.224566 MeV
Error: -82.91%
C_knot(D) = B_AME / (m_e × |sum|) = 5.852086   <- FITTED deficit ratio, NOT derived
```

So the **`Σ_λ y_λ χ^λ(β_D) sgn(w_0^{S_{λ'}}) f^λ` formula UNDERSHOOTS the deuteron by −82.9 %** — it does
**not** close it. (The C_knot=5.852 that would close it is a fitted deficit ratio, retracted per PR #1386.)

## What actually closes the deuteron

Per [`2026-05-26-delta-lambda-binding-formula-closure.md`](2026-05-26-delta-lambda-binding-formula-closure.md)
§"Binding status (2026-05-28, post-retraction)": the deuteron binds at **+0.91 % via `E₀×q⁻¹`**, where
`E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV` (PR #1367) — "the only honestly-closed light nucleus." The closure is the
**E₀-scale formula**, a *different* object from the Δ_λ per-block Σ-formula.

## Correction (surgical)

The merged [`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md)
(#2386) opened "the deuteron Δ_λ is **CLOSED** by the structural form Δ_λ = sgn(w₀^{S_λ'})·dim". **The word
"closed" is wrong** and is corrected (banner added there):

- **Valid (unchanged):** Δ_λ = sgn(w₀^{S_λ'})·dim is the **proved categorical per-block factor** (sgn + f^λ both
  Lean-proved, PR #1305), and it decomposes as **magnitude `dim(V_λ)` × chirality sign**. This decomposition,
  and its explanation of the PROBE-4 KL-positivity prune (sign = exogenous chirality), **stand**.
- **Corrected:** the per-λ **sum** `Σ y_λ χ^λ Δ_λ` does **not close** the deuteron (−82.9 %). The deuteron
  *binding* is closed separately by `E₀×q⁻¹` (+0.91 %). The magnitude×chirality result is a statement about the
  **Δ_λ factor's structure**, NOT a closure of the binding energy.

## Ledger inconsistency flagged

The Option-E ledger ([`docs/coordination/option-e.md`](../coordination/option-e.md)) §Status "Reading:" paragraph
attributes the deuteron closure to the Σ-formula ("the deuteron is closed by a STRUCTURAL formula
B(D)=m_e×|Σ_λ y_λ χ^λ sgn f^λ|…"). That is the **same conflation**: the Σ-formula undershoots 83 %; the closure
is `E₀×q⁻¹`. The ledger §Status row itself correctly says "+0.91 % via E₀×q⁻¹"; only the "Reading" prose
mis-attributes it. Corrected in the ledger in this PR.

## Net

The deuteron binding **is** closed (+0.91 %, `E₀×q⁻¹`) — that stands. What the cross-check corrects is the
*mechanism attribution*: the Δ_λ per-block Σ-formula (the magnitude×chirality object) does **not** close it. No
math is retracted — the chirality decomposition and the PROBE-4 prune are unaffected; only the "closed-by-Σ"
framing (in #2386 and the ledger prose) is fixed. Verified by running the canonical compute.

## Cross-references

- `computations/binding_energy_categorical_deuteron.py` — the Σ-formula (−82.9 %, verified this session)
- `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md` — `E₀×q⁻¹` closure (+0.91 %)
- `docs/audits/2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md` — #2386 (corrected here)
- `docs/coordination/option-e.md` — ledger (Reading paragraph corrected here)
