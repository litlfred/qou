# The decuplet equal-spacing rule has no discriminating power — the Ω⁻ is not a target

**Date:** 2026-08-14
**Bean:** `qou-7lio` (partial — 1 of 4 eightfold coverage gaps closed)
**Branch:** `claude/8fold-stdmodel-qou-overview-9ueo6w`
**Lean:** [`QOU/Eightfold/DecupletEqualSpacing.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/DecupletEqualSpacing.lean) — sorry-free, `lean`-direct exit 0, axioms clean
**Block:** [`rem:decuplet-equal-spacing`](../../content/quantum-observable-universe/eightfold-way/decuplet-equal-spacing.md)

---

## The question, and why it was asked

The [SM/eightfold cheat sheet](../sm-eightfold-derivation-cheat-sheet.md) §5
found that the eightfold chapter has no block for the **decuplet equal-spacing
rule** or the **Ω⁻ prediction** — the programme's historically decisive test —
which appear only as one row of the flavour dictionary table. It flagged the
question as *"cheap and currently unasked"*:

> Does the framework reproduce equal spacing, and if so does that reproduction
> carry information, or is it (like GMO) automatic for any first-order
> breaking?

It is automatic. **Same status as Gell-Mann–Okubo: zero discriminating power.**

## The result

Equal spacing holds identically, for every choice of the first-order
octet-breaking parameters `a, b, c`, over any commutative ring. The three
consecutive spacings all equal `−4b − 6c`, and the second difference vanishes
(`second_difference_vanishes`). Two arbitrarily different breaking patterns give
the same answer (`equal_spacing_cannot_discriminate`).

Stronger, and the part that reframes the history: the Ω is **not an independent
output at all**. Identically in `a, b, c`,

```
m(Ω) = 2·m(Ξ*) − m(Σ*)              (omega_eq_two_xi_minus_sigma)
```

so Gell-Mann's 1962 extrapolation reads off a value the ansatz has already
fixed. The prediction was correct and it was a genuine scientific triumph — but
what it confirmed was the *form* of the breaking (octet, first order), not any
dynamics realising that form.

## Why it collapses — the invariant, cited

The GMO mass operator is **quadratic** in the hypercharge:

```
m(I, Y) = a + b·Y + c·( I(I+1) − Y²/4 )
```

On the decuplet — and only because of the decuplet's own weight structure — the
isospin is affine in the hypercharge, `2I = Y + 2`:

| State | `Y` | `I` | `2I` | `Y+2` |
|---|---:|---:|---:|---:|
| Δ | +1 | 3/2 | 3 | 3 |
| Σ* | 0 | 1 | 2 | 2 |
| Ξ* | −1 | 1/2 | 1 | 1 |
| Ω | −2 | 0 | 0 | 0 |

Substituting collapses the quadratic term to a linear one,
`I(I+1) − Y²/4 = (3Y+4)/2` (`casimir_collapses_of_isospin_affine`), so `m` is
affine in `Y`. Consecutive states step by `ΔY = −1`, hence equal mass steps.

**The collapse is special to the decuplet.** On the baryon octet the isospin is
not even a *function* of the hypercharge — Σ and Λ share `Y = 0` with `I = 1`
and `I = 0` — so no such substitution exists
(`octet_casimir_not_function_of_hypercharge`, derived from the octet weight
data rather than asserted). Without that contrast the argument could be misread
as a fact about every `SU(3)` multiplet, which it is not.

## What remains testable — the deviation

| Spacing | MeV |
|---|---:|
| Σ* − Δ | 152.6 |
| Ξ* − Σ* | 148.8 |
| Ω − Ξ* | 139.1 |

Spread **13.6 MeV ≈ 9.2 %** of the mean — comparable to the ≈ 6 % GMO deviation
on the pseudoscalar octet, and measuring the same thing: the failure of
first-order breaking. The framework derives no second-order term and so predicts
spread **0**. A derivation producing ≈ 9 % would be a genuine prediction; a
materially different value would falsify the mechanism.

Numbers are comparators only. Nothing is fitted; nothing is wired.

## Scope

**Scope-(a) where it matters.** The null result itself is a proved identity, not
a scope-limited negative — it says what it says for all `a, b, c`. What is
*not* claimed:

- **Not** that the decuplet spectrum is uninformative — the deviation is
  informative, and is now the named target.
- **Not** that QOU fails here — QOU has not attempted it. The point is that
  attempting the *rule* would be wasted effort, and succeeding at it would not
  be evidence.
- **Not** a statement about other multiplets — see the octet contrast above.

## Why this is worth having

It removes a target that would otherwise have looked like a success. That is
the same service `GellMannOkuboIdentity.lean` performs for the octet, and per
the 2026-08-08 epistemic accounting it is the eightfold chapter's dominant mode
of contribution: **deleting false evidence.** Before this, a future agent could
have reproduced equal spacing, reported the Ω⁻ to 0.6 %, and counted it as
support. Two of the eightfold way's three headline quantitative successes — GMO
and equal spacing — are now both proved to be content-free as *targets*, with
their deviations relocated as the real content.

## What this did NOT establish

- The **vector meson nonet** (1⁻) remains uncovered and is now the highest-value
  open eightfold gap: ideal ω–φ mixing is where the octet formula genuinely
  *fails*, so unlike GMO and equal spacing it is not automatic. Bean `qou-7lio`
  stays open for it.
- The **baryon octet** (½⁺) still has no block, and **U-spin / Coleman–Glashow**
  are still unmentioned.
- No second-order term was derived, so the ≈ 9.2 % deviation is named, not
  addressed.
- The decuplet's own `N = 3` conditionality is untouched — this result is about
  the breaking ansatz, and holds whatever hosts it.
