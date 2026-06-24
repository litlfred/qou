# Keystone G3 / Bring-fibre sub-lead: constraints from the merged binding-side `M` mapping

**Date:** 2026-06-24
**Type:** program-constraint note (no fit, no new compute — synthesises this session's merged binding-side
results into the keystone full-Hecke geometric-index program). Feeds
[`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`](../scope/2026-06-24-keystone-fullhecke-geometric-index-program.md)
phases **G3** and the **(d) Bring/Jacobian elliptic-fibre sub-lead**, which were scoped (#2727) *before*
the binding-side `M` mapping (#2708) landed.

## Why this note

The program's G3 ("identify the `a_D=lw` period map from the Seifert `S¹` monodromy on the prolonged
Picard–Fuchs system") and sub-lead (d) ("identify the q-family `E(q)` of the W-plane elliptic fibre; verify
its Gauss–Manin monodromy trace `= τ(q₀)=2.6424`") are exactly the objects this session's lever-1 work
mapped from the *binding* side (#2708, all merged to main). Three of those results **constrain how G3/(d)
must be done** — and one **sharpens a falsifiable target**. None re-derives the geometry; they pin *which*
object the geometry must produce.

## Constraint 1 — the W-plane fibre `E(q)` is the coral/descartes `E_q` (identified, j-confirmed)

Sub-lead (d) asks to *identify* the q-family `E(q)`. It is already identified: the rank-2 W-plane is the
**coral/descartes elliptic curve** `E_q` (`brings-surface/descartes-elliptic-curve.md`), and
`j(q₀)=129.86` **matches** #2710's `E = Bring/S₄` at the substrate (the j-invariant is the isogeny
invariant). Explicit Weierstrass form `y²=x³+p(q)x+r(q)` with `p,r` rational in `√q`; classical limit
`j(1)=128`, `p(1)=2/3`, `r(1)=20/27`. So **G1/G3 inherit an explicit `E(q)`** — no separate fibre-ID step.
([`2026-06-24-lever1-coral-eq-monodromy-integrality.md`](2026-06-24-lever1-coral-eq-monodromy-integrality.md))

## Constraint 2 — G3's monodromy is the abelianised `λ_SW` REAL holonomy, NOT the topological monodromy

`τ = tr B = 2.6424 ∉ ℤ`. The **topological** Gauss–Manin monodromy of an elliptic family acts on
`H¹(E,ℤ)≅ℤ²` ⟹ `SL₂(ℤ)` ⟹ **integer trace**. So G3's "Seifert `S¹` monodromy" **cannot** be the
topological Gauss–Manin monodromy — it must be the **abelianised `λ_SW` Cartan-connection holonomy**
(`SL₂(ℝ)`, hyperbolic, `τ=2cosh θ`, `θ=0.7815`). This is consistent with — and required by — the
program's own non-compact `SU_q(2)→E_q(2)` arena (`q₀>1` is not a root of unity). **G3 must extract the
flat-connection holonomy of `λ_SW`, not the integral π₁-monodromy.**
([`2026-06-24-lever1-binding-monodromy-hyperbolicity.md`](2026-06-24-lever1-binding-monodromy-hyperbolicity.md),
[`…coral-eq-monodromy-integrality.md`](2026-06-24-lever1-coral-eq-monodromy-integrality.md))

## Constraint 3 — target (2) `a_D = lw` is SEED-LIMITED (`c ≤ 3` only), not a full functional identity

The program lists target (2) as "the SW-prolonged period must equal the rule value `lw(c)` … functional-
level (same `W_λ` family), not a ~8 % number-match." **Sharpening:** the depth-2 constant-coefficient
recurrence `R = x²−τx+1` (which any genuine prolonged period `φ(Mⁿv₀)` satisfies *exactly* by
Cayley–Hamilton) **fails for `lw(c)` past the seed** — `lw(4)` off by 0.4 %, `lw(5)` by 14 %, and the
windowed kernel drifts `τ = 2.6424 → 2.6505 → 2.9933` (`lw(c)` grows super-geometrically, like the
involution numbers it q-deforms). So `a_D⁽ⁿ⁾ = lw(n−1)` holds **only at the `c = 1,2,3` anchors**, not as
a functional identity. **Implication for G3:** the geometric SW-period must reproduce the *genuine* `a_D`
(the real-holonomy prolongation, exactly depth-2 by construction), with `lw` as the **seed anchor only** —
G3 must *not* be gated on reproducing `lw(c)` for `c ≥ 4` (it would over-constrain against a non-period
sequence). ([`2026-06-24-lever1-lw-depth2-recurrence-falsified.md`](2026-06-24-lever1-lw-depth2-recurrence-falsified.md))

## Constraint 4 — the numerology guardrail is reinforced (no scalar shortcut; the OPERATOR is the deliverable)

The program's STRICT guardrail ("matching one geometric scalar to one algebraic scalar is not a
derivation … formalize the monodromy *operator*, not its trace value") is independently confirmed: the
seed `τ=2.6424` is **forced** by the three wired anchors (`1`, `lw(2)`, Family-A), is non-integer, and
**no integer `τ` reproduces the wired Family-A** — the icosahedral **golden `τ=3` (`λ=φ²`) misses by
19 %**. So there is no integer/topological/golden scalar shortcut; the G3 deliverable is the
`λ_SW`-connection **operator** (whose Habiro-element facet also feeds Q_β, per the convergence note
`2026-06-24-binding-qbeta-keystone-convergence.md`).
([`2026-06-24-lever1-lambda-sw-no-shortcut.md`](2026-06-24-lever1-lambda-sw-no-shortcut.md))

## Net (what G3/(d) inherit)

| program item | inherited constraint |
|---|---|
| (d) identify `E(q)` | **done** — coral/descartes `E_q`, `j(q₀)=129.86` = `Bring/S₄` |
| G3 monodromy object | the **abelianised `λ_SW` real holonomy** (`SL₂(ℝ)`), **not** topological `SL₂(ℤ)` |
| G3 target (2) `a_D=lw` | **seed-limited** — reproduce the genuine `a_D`; `lw` is the `c≤3` anchor only |
| guardrail | reinforced — no integer/golden scalar shortcut; deliver the operator |

The **deep piece is unchanged + still owner-gated/tool-gated**: the explicit `λ_SW` connection + its
genus-1 period integration on `E_q` (Sage-blocked in-sandbox) is the actual G3 build. This note pins
*what* that object must be, so the geometric work starts from the correct target. No fit; nothing wired;
no tier change.
