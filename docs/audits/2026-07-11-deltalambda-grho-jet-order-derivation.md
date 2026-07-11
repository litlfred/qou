# Deriving g_ρ: the principal grading IS the GS/jet-order filtration grading (fake-degree valuation)

**Date:** 2026-07-11 · **Axis:** Δ_λ closure (strong sector), g_ρ construction ·
**Follows:** the magnitude reduction [`2026-07-11-deltalambda-magnitude-graded-trace.md`](2026-07-11-deltalambda-magnitude-graded-trace.md) (#3537) ·
**Gate:** Track-A (owner-reversed) · **Tier:** symbolic-exact (parameter-free) ·
**No fit; nothing wired.**

## What this derives (and what it does not)

The magnitude reduction (#3537) collapsed the whole Δ_λ closure to **one** object: the
principal grading `g_ρ`, with `Δ_λ = tr_{V_λ}(g_ρ) = (−1)^{n(λ)}·dim(λ)`. The reduced
open problem was "construct `g_ρ` from the drivers." This audit **supplies the
construction** for the **sign carrier**: `g_ρ` is the driver-level GS/jet-order
filtration grading. It does **not** yet close the binding physics (see *Honest scope*).

Probe [`deltalambda_grho_jet_order_derivation_probe.py`](../../computations/deltalambda/deltalambda_grho_jet_order_derivation_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-grho-jet-order-derivation.witness.json) (3/3).

## The derivation

Owner's lead: the Gram-inverse / knot-operator basis on the **GB filtration / jet
order**. The QOU **Gröbner–Shirshov normal-form basis** is filtered by **word length =
jet order**. For `H_3` the NF basis `(), (0), (1), (0 1), (1 0), (0 1 0)` has jet orders
`0,1,1,2,2,3`. The principal grading `g_ρ` is this **jet-order grading operator**, and
its **bottom degree** on the irreducible `V_λ` is exactly

> **`n(λ) = min_{T ∈ SYT(λ)} maj(T)`** — the **fake-degree valuation**,

the lowest jet-order at which `V_λ` enters the length-graded regular representation
(equivalently the coinvariant algebra). This is a **classical theorem**
(Steinberg / Lusztig; Macdonald, *Symmetric Functions and Hall Polynomials* I.5 — the
fake degree `R_λ(q) = Σ_T q^{maj T}` has lowest term `q^{n(λ)}`, from the principal
specialisation `s_λ(1,q,q²,…) = q^{n(λ)}·∏…`).

**Verified (parameter-free):**

1. `n(λ) = min maj(SYT(λ))` for all λ⊢3..8 (the valuation).
2. The QOU GS NF-basis (`H_3`) is jet-order graded `0..3`; `n(λ⊢3) = {0,1,3}` are the
   bottom jet-orders where `V_[3], V_[2,1], V_[1,1,1]` enter.
3. The Δ_λ sign `(−1)^{n(λ)} = (−1)^{bottom jet-order}` — the parity of the fake-degree
   valuation. So `g_ρ` = jet-order grading **derives the sign carrier** from the GS
   filtration.

This closes the "is `g_ρ` an external statistic or a driver-level object?" question: it
is **driver-level** — the Gröbner–Shirshov word-length grading — not an axiom.

## Honest scope (Anti-Laundering / "Axiomatization is NOT a Proof")

- **Derived:** the **sign carrier** `(−1)^{n(λ)}` is grounded in the driver-level GS/jet
  filtration via the classical fake-degree valuation. `g_ρ` is the jet-order grading.
- **Not derived / still open:** the full **binding closure** — assembling
  `Δ_λ = tr(g_ρ) = (−1)^{n(λ)}·dim(λ)` into `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` and wiring it
  into the mass pipeline. The magnitude is the ordinary dimension (#3537), classical;
  the sign is now derived; the *assembly + wiring* is the remaining step and is **not**
  done here. This audit **does not** unlock any downstream binding compute.

## Lean

[`QOU/BraidKnot/PrincipalGradingJetOrder.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PrincipalGradingJetOrder.lean):
defines the principal grading `n(λ)` and the jet-order (major-index) valuation, states
the fake-degree valuation as the cited classical theorem (`-- Ref: [macdonald]`), and
proves the **sign-parity consequence** (`Δ_λ` sign = parity of the bottom jet-order)
sorry-free from it. The classical theorem is a *published* result cited per the
`-- Ref:` convention — **not** a QOU conjecture and **not** axiom-laundering; the QOU
consequence is genuinely proved from it.

## Cross-references

- Magnitude reduction: [`2026-07-11-deltalambda-magnitude-graded-trace.md`](2026-07-11-deltalambda-magnitude-graded-trace.md) (#3537)
- Sign capstone: [`2026-07-11-deltalambda-sign-pivotal-grading-capstone.md`](2026-07-11-deltalambda-sign-pivotal-grading-capstone.md) (#3529)
- Selection-rule engine (on main): `QOU/SelectionRules.lean`
