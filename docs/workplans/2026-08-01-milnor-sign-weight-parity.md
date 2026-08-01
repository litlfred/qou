# Work-plan — Milnor deficit sign vs weight bar-parity (Option 2)

**Branch:** `claude/milnor-sign-weight-parity-derivation-2026-08-01` · **Axis:** Δ_λ / Milnor-parity
sign law (#4389) · **Builds on:** #4399 Tie B (the `(−1)^{A−1}` convergence). **Discipline:**
formalize-first, honest scope, no fit.

## Question

Does the Milnor-parity deficit sign `sign(1 − τ_A) = (−1)^{A−1}` (#4389: A=3 `+` proved, A=4 `−`
measured, general **open**) **provably descend** from my weight bar-sign `sgn = (−1)^{n-1}`
(the `(q−q⁻¹)^{n-1}` Ocneanu-weight parity, #4399), which **at `n = 3A`** (and only using that relation,
not arbitrary `n`, `A`) reduces to `(−1)^{3A−1} = (−1)^{A−1}`?

## Finding (verified) — the derivation route is REFUTED (scope-(a))

The Borromean deficit closed form (proved) is `1 − τ_Borr = h⁴(3+h²)/(h²+4)`:

- **leading order `h⁴ = h^{2(A−1)}`** (Milnor / `(A−1)`-fold commutator depth), **not** `h⁸ = h^{n−1}`;
- the `(q−q⁻¹)^{n-1}` Ocneanu-weight prefactor is **ABSENT** — because `τ_A` is a *normalized*
  (link/unlink) ratio, the weight prefactor **cancels**;
- the deficit is **bar-even** (a function of `h²`), so its sign is a leading-**coefficient** effect,
  **not** a bar-parity flip.

Therefore the weight bar-parity **cannot** be the mechanism of the deficit sign. The two `(−1)^{A−1}`
values arise from **distinct-order objects** — the weight prefactor (`h^{3A−1}`, cancelled, subleading)
vs the Milnor deficit (`h^{2(A−1)}`, leading). The `(−1)^{A−1}` match is a **convergence via distinct
mechanisms**, not a derivation.

This **sharpens #4399 Tie B** (from "candidate derivation, not proved" to "this specific route
refuted") and is an **anti-laundering safeguard**: it prevents the coincidence from being mis-sold as a
derivation of the sign #4389 explicitly left open. Other derivations of the sign law remain open.

## Steps (microcommits)

1. **[this]** work-plan.
2. **Lean** `MilnorWeightParityConvergence.lean` — the order facts: deficit order `2(A−1)` is even
   (always bar-even); weight order `3A−1 > 2(A−1)` (subleading/cancelled); `(−1)^{3A−1} = (−1)^{A−1}`
   (the parity coincidence). Register in the umbrella. Sorry-free.
3. **Probe** — verify the cancellation (deficit leading `h⁴`, weight `h⁸` absent), bar-evenness, the
   order table, and the convergence-not-derivation classification.
4. **Audit** — the honest scope-(a) refutation + the sharpening of Tie B.

## Scope

DERIVED: a scope-(a) refutation of the weight-parity ⇒ deficit-sign route (the weight cancels in the
normalized trace). NOT a derivation of the sign law (which stays open, #4389). No fit; nothing wired.
