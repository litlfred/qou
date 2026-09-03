# The μ–p tension is ALREADY convention-D — re-deriving the pins cannot move it

**Date:** 2026-08-24
**Verdict:** the proposed "re-derive both pins under convention D" work item is a
**no-op**. Proved algebraically, not measured.

## TL;DR

The μ–p tension is **11.537118 ppb in q₀ ≈ 240 ppb in m_p**, and that figure is
**convention-independent**:

* the **muon** pin contains no Markov parameter at all, so no convention can
  touch it;
* the **proton** pin's closed-form Markov trace is **already `z = q³/(q²+1)`**,
  i.e. convention **D**.

So the C→D migration — which moved `z` by **+22.70 %** and moved α\* by
14.741 % (bean `qou-2zjp`) — leaves this tension exactly where it is. Anyone
proposing to re-derive the pins to see whether the tension survives should read
this first and spend the time elsewhere.

## Why anyone would think otherwise

The reasoning that motivates the re-derivation is sound as far as it goes: the
2026-08-15 owner ruling makes convention D canonical, AGENTS.md records that
C-frame results need re-derivation under D, and α\* is a measured case of a
published value moving 14.741 % for exactly that reason. Applying the same
suspicion to the two q₀ pins is the obvious next step.

It is also wrong, and the reason is worth stating because it generalises:
**"derived before the C→D commit" is not the same as "C-frame."** A quantity is
convention-dependent only if `z` reaches its arithmetic. For these two pins it
does not, or it already reaches it as D.

## The muon pin has no `z`

`qou_substrate.constants.q_muon_at`:

    q = 1 / (1 − √( Vol(4₁) / (m_μ/m_e) ))

`Vol(4₁) = 2·Cl₂(π/3)` is a hyperbolic volume — a mathematical constant, no
`q`, no braid, no trace. `m_μ/m_e` is CODATA. There is no Markov parameter
anywhere in the expression, so the muon pin is convention-independent in the
strongest sense: the question does not arise.

## The proton pin's closed form IS convention D — proof

`qou_substrate.constants._solve_q_proton_f64` solves

    m_p/m_e = 2·(Vol(4₁)/ℏ_q²)·F_Bor(q) − 12

with the Borromean braid `β_Bor = (σ₁σ₂⁻¹)³ ∈ B₃`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`,
and the trace given in closed form, "self-contained ⇒ no Hecke machinery":

    |tr_M(β_Bor)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4),   h = q − 1/q

To find which convention that closed form encodes, the Ocneanu trace of
`(σ₁σ₂⁻¹)³` was computed in `H₃(q)` with **`z` symbolic** — building the algebra
from `σᵢ² = (q − q⁻¹)σᵢ + 1`, the braid relation, `σ⁻¹ = σ − (q − q⁻¹)`, and the
defining rule `tr(x σ₂ y) = z·tr(xy)`. Substituting each convention and
simplifying:

| convention | `z` | `raw(z) − closed_form` |
|---|---|---|
| **D** | `q³/(q²+1)` | **`0`** — identically, for all `q` |
| C | `√q/(q+1)` | a nonzero rational function carrying half-integer powers of `q` |

The D result is an exact symbolic zero from `sympy.simplify`, not a numerical
agreement. Numerically at the proton pin, for the record: closed form
`0.99856216383679`, D `0.99856216383679`, C `0.99836662258572`.

The half-integer powers in the C residual are the structural tell: convention C
is `z = √q/(q+1)`, so any C-frame closed form in `h = q − 1/q` must carry
`√q`. This one does not, and could not.

## What this closes and what it does not

**Closed.** "Re-derive the two q₀ pins under convention D and re-measure the
tension." There is nothing to re-derive. The 11.5 ppb is the D-frame number.

**Not closed.** Everything else about the tension is untouched:

* it remains **irreducible** — no single `q₀` zeroes both residuals;
* the ~240 ppb floor in `m_p` stands, and with it the rule from
  [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md)
  that any fit closing an observable below the floor is modelling the tension as
  signal;
* the proton formula's own ~6.7 % formula-to-exact gap (exact `tr_M_atomic(1,0)`
  in the formula gives ≈1960, not 1836) is a far larger discrepancy than the
  tension sitting on top of it, and is where the physics work actually is.

**Strengthened.** The tension is now known to be convention-independent, which
makes it a more robust target than it was. It cannot be explained away as an
artifact of a superseded trace convention — that escape route is measured shut.

## Method note

The check that matters here is not "was this file edited before 2026-08-15" but
"does `z` reach the arithmetic, and as which convention". The first is a
timestamp and answers nothing; the second is decidable in closed form and took
one symbolic substitution. The same distinction is what separated the 4 genuinely
stale producers from the 1 false positive in `qou-2zjp`'s candidate set.
