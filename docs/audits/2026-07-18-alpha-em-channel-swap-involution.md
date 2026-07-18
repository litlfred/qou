# α_EM per-loop `2` unification: which involution swaps the Hecke channels — the bar involution FIXES them; `q↦−q⁻¹` swaps them (and carries the global sign)

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure (the single load-bearing wall) ·
**Tier:** exact `ℚ(q)` algebra (scope-(a) — refutes + corrects a named hypothesis;
does NOT close the wall) · **Discipline:** no fit, nothing wired, `1/(8π)` stays a
phase-4 identification.

## Context — the named unification hypothesis

The sibling conjecture-statement audit
([`2026-07-18-alpha-em-perloop-conjecture-statement.md`](2026-07-18-alpha-em-perloop-conjecture-statement.md),
landed on main) reduced the per-loop wall to a two-clause conjecture and put
**three readings of the `2`** in `8π = 2·(4π)` on main simultaneously — GB
(`|χ|`, genus-independent), Hodge doubling (`b₁ = 2g`, #3920), Hecke channels
(`e₊/e₋`). It **named** a unification hypothesis (explicitly "not derived"):

> "the bar involution `q ↔ q⁻¹` swaps `e₊/e₋` exactly as complex conjugation
>  swaps `H^{1,0} ⊕ H^{0,1}`,"

so a τ-functor correspondence would identify the Hecke channel pair with the
Hodge conjugate pair (#3920) and collapse the three readings to one object.

This audit verifies the algebraic core of that hypothesis **exactly** (sympy over
`ℚ(q)`) and finds it must be corrected.

## Result (exact, machine-checked)

The two Hecke idempotents are the eigen-projectors of `σ`
(`(σ−q)(σ+q⁻¹)=0`): `e₊ = (σ+q⁻¹)/[2]_q` (eigenvalue `q`),
`e₋ = (q−σ)/[2]_q` (eigenvalue `−q⁻¹`), `e₊+e₋=1`.

| involution | action on `σ` | effect on `e₊/e₋` | effect on `[2]_q` |
|---|---|---|---|
| **bar** `q↦q⁻¹` | `σ↦σ⁻¹ = σ−(q−q⁻¹)` | **FIXES both** (`bar(e₊)=e₊`, `bar(e₋)=e₋`) | `[2]_q` (invariant) |
| **eigenvalue-exchange** `q↦−q⁻¹` | — (coefficient sub) | **SWAPS** (`e₊↦e₋`, `e₋↦e₊`) | `−[2]_q` (sign flip) |

- **The named hypothesis is REFUTED as literally stated.** The Hecke bar
  involution `q↦q⁻¹`, `σ↦σ⁻¹` **fixes** each idempotent — it does not swap the
  channels. (`bar` is a ring homomorphism that fixes the eigen-projectors of the
  bar-invariant element `σ+σ⁻¹`.)
- **The correct channel-swap is `q↦−q⁻¹`** — the exchange of the two Hecke
  eigenvalues `q` and `−q⁻¹`. It swaps `e₊↔e₋` exactly, and additionally sends
  `[2]_q ↦ −[2]_q`. That sign flip **is** the derivability map's separately-
  underived **global "−" alternation** — so a *single* involution carries both
  the multiplicity-`2` channel swap and the global dressing sign.

## Corrected unification bridge (scope-(a), sharper — not derived)

A τ-functor unifying the Hodge `2` (complex conjugation `H^{1,0} ↔ H^{0,1}`,
#3920) with the Hecke `2` (`e₊ ↔ e₋`) must map complex conjugation to the
eigenvalue-exchange `q ↦ −q⁻¹`, **not** to the bar involution `q ↦ q⁻¹`.

Because `q ↦ −q⁻¹` sends the real substrate `q₀ ≈ 1.11` to `≈ −0.90`
(real-negative — not a conjugation of a real number), the identification is
necessarily a **fibre-level** statement: it lives where `q` is a formal/complex
variable with `Im q` unconstrained (AGENTS.md fibre-vs-observable banner); at the
observable anchor `q₀` (`Im q₀ = 0`) the map `q ↦ −q⁻¹` is not conjugation. This
is consistent with the c_k/Δ_λ guidance that closures of this shape live at the
fibre, evaluated archimedean-ly per anchor.

## What this does and does NOT establish

- **DOES (exact):** refutes the literal "bar swaps the channels" (bar fixes
  them); identifies the channel-swap as `q↦−q⁻¹`; shows it carries `[2]_q↦−[2]_q`
  (unifying the multiplicity-`2` with the global sign); places any Hodge↔Hecke
  correspondence at fibre level.
- **DOES NOT:** derive the unification or close the wall. The correspondence
  "complex conjugation ≙ `q↦−q⁻¹` under τ" remains the open conjecture; this
  probe only fixes **which** involution it must be.

## Scope discipline (anti-laundering)

Exact `ℚ(q)` algebra, machine-checked; no CODATA read; no convention tuned toward
`8π`; the correspondence is stated OPEN. No `α_k` wired; no fit; no tier change.

## Cross-references

- The two-clause conjecture + three readings of the `2` (the hypothesis this refines): [`2026-07-18-alpha-em-perloop-conjecture-statement.md`](2026-07-18-alpha-em-perloop-conjecture-statement.md)
- Hodge doubling reading (`b₁ = 2g`, real vs holomorphic): [`2026-07-18-alpha-em-multiplicity2-realcomplex-count.md`](2026-07-18-alpha-em-multiplicity2-realcomplex-count.md)
- Reciprocal-form consolidation (Vol(J)=1, the located `1/2`): [`2026-07-18-alpha-em-reciprocal-form-consolidation.md`](2026-07-18-alpha-em-reciprocal-form-consolidation.md)
- Probe + witness: [`../../computations/alpha_em/alpha_em_channel_swap_involution_probe.py`](../../computations/alpha_em/alpha_em_channel_swap_involution_probe.py), `computations/alpha_em/alpha-em-channel-swap-involution.witness.json`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
