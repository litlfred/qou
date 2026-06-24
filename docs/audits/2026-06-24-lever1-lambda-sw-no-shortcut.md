# Lever-1 continuation (a): no topological / integer / golden shortcut to `τ=2.6424` — the residual is genuinely the owner-gated `λ_SW` holonomy

**Date:** 2026-06-24
**Probe:** [`computations/substrate/lever1_lambda_sw_no_shortcut.py`](../../computations/substrate/lever1_lambda_sw_no_shortcut.py)
**Witness:** [`computations/substrate/lever1-lambda-sw-no-shortcut.witness.json`](../../computations/substrate/lever1-lambda-sw-no-shortcut.witness.json) (4/4)
**Status:** continuation (a) of the `θ_binding` derivation — confirms no algebraic shortcut and holds the numerology guard against the icosahedral golden ratio. No fit; symbolic + 50-dps. Follows [`2026-06-24-lever1-lw-depth2-recurrence-falsified.md`](2026-06-24-lever1-lw-depth2-recurrence-falsified.md).

## The seed `τ` is forced by the *wired* anchors — and it is non-integer

`τ_seed = (a_D⁽²⁾ + a_D⁽⁴⁾)/a_D⁽³⁾` with the three **production-wired** anchors:

| anchor | value | source |
|---|---|---|
| `a_D⁽²⁾` | `1` | muon (c=1) |
| `a_D⁽³⁾` | `lw(2) = (q+1)²/(3q)` | c=2 selection rule |
| `a_D⁽⁴⁾` | `Family-A = (3q²+4+3q⁻²)/4` | **proton, bit-for-bit `linking_weight_family_a`** |

⇒ `τ_seed = 2.6423863…` — **non-integer, strictly between 2 and 3.** Since these anchors are the
*actual production multipliers* (not free choices), `τ_seed` is not adjustable.

## No integer `τ` reproduces the wired `Family-A` — incl. the golden `τ=3`

A topological Gauss–Manin monodromy of an elliptic family lies in `SL₂(ℤ)` → **integer trace**. For
each integer candidate, the depth-2 recurrence predicts `a_D⁽⁴⁾ = τ·a_D⁽³⁾ − a_D⁽²⁾`, to be compared
against the **wired** `Family-A = 2.5328`:

| `τ` | predicted `a_D⁽⁴⁾` | miss vs wired Family-A |
|---|---|---|
| 2 (parabolic) | 1.674 | 34 % |
| **3 (golden, `λ=φ²`)** | **3.011** | **19 %** |
| 4 | 4.348 | 72 % |

**Numerology guard — the golden `τ=3` is refuted, not forced.** The Bring surface is icosahedral
(`A₅`, golden ratio pervasive), so `τ=3 ↔ λ=φ² = (3+√5)/2` (`θ_golden = arccosh(3/2) = 0.9624`) is the
seductive "natural" monodromy. It is **tested and rejected**: it overshoots the wired `Family-A` by
19 %. No integer `τ` lands the wired anchor. *(b)-exclusion of every integer/topological `τ`, invariant:
`SL₂(ℤ)`-trace integrality plus the fixed wired-anchor constraint.*

## Net — the residual is genuinely the owner-gated `λ_SW` real holonomy

Combining the three lever-1 probes:

1. **Curve:** the rank-2 `W` is the coral/descartes `E_q` (`j(q₀)=129.86`, confirmed).
2. **Not topological:** `τ=2.6424 ∉ ℤ` — `B` is not the integral monodromy ([integrality audit](2026-06-24-lever1-coral-eq-monodromy-integrality.md)).
3. **Not a recurrence rate of `lw`:** `lw(c)` fails the depth-2 recurrence past the seed ([falsification audit](2026-06-24-lever1-lw-depth2-recurrence-falsified.md)).
4. **No integer/golden shortcut:** this probe — the wired seed forces a non-integer `τ`, and no integer (incl. golden `τ=3`) fits.

So there is **no algebraic shortcut** to `τ=2.6424`. The genuine object is the **abelianised `λ_SW`
real connection holonomy** on the coral `E_q` — `SL₂(ℝ)`, hyperbolic, `θ_binding=0.7815` — which is
the owner-gated keystone `M` restricted to the elliptic factor. **Concrete owner-gated next step:**
integrate the Seiberg–Witten differential `λ_SW = x dz` on `E_q` and its Gauss–Manin prolongation to
recover the real-holonomy 2×2 `B` with `tr B = 2.6424` (needs the genus-1 period integration the
sandbox Sage cannot currently do; the sibling `mass-open-keystone-w-l2-root` holds the curve side
`E = Bring/S₄`, `Jac(Bring) ~ E⁴`). **Not a closure** — a clean mapping of the residual with all
shortcuts ruled out. No fit; nothing wired; no tier change.
