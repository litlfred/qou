# q₀ as a varying local field — Im(q) as the c₃ anchor-carrier: FALSIFIABLE TEST + honest verdict

**Date:** 2026-07-26 · **Branch:** `claude/q0-varies-imq-c3-anchor-2026-07-26` · **PR:** #4326 ·
**Axis:** c₃ / Q_β bar-odd anchor-swing / q₀ · **Tier:** scope-(a) negative (no closure) ·
**Discipline:** no fit; NO residual inverted to define Im(q); nothing wired;
`conj:algebraic-geometric-dilog-equivalence` stays OPEN.

## The reframe under test

Owner reframe (capstone [#4297] / `2026-07-25-c3-categorical-exclusion-capstone.md`): q₀ is
not a universal real constant but our **local, measured** substrate value — a field that
VARIES and generically carries **Im(q) ≠ 0**. The merged c₃ exclusion chain proved the swing
is non-categorical at *strictly real* q₀; #4293 (`QOU.QBeta.ArgUPhaseBranchSelection`,
sorry-free) specifically showed the bar-odd phase channel

`S(r,φ) = (√3/2)·r²·sin(2φ)`,  `φ = arg(u)`,  `u = 2 log q₀`

is a **maximal-leverage** DOF (`∂S/∂φ|₀ = √3 r² ≠ 0`) that is **frozen** at real q₀ because
`arg(u)=0`. The reframe's content: `Im(q₀)≠0 ⇒ arg(u)≠0 ⇒` the phase **unfreezes**. So a
nonzero c₃ swing is (by the chain) a proof-by-contradiction that q₀ is not strictly real, and
its size *measures* Im(q₀) via the proved `∂S/∂φ`.

**The whole risk (honesty guardrail).** "q₀ varies" must not become a free per-observable
knob: Im(q) fitted per anchor fits anything (an unfalsifiable "seventh ansatz"). A **single
constrained/predicted Im(q₀)** that accounts for the swing *across* observables is a lead; a
**per-anchor-fitted Im(q)** is a FIT. This audit runs that test.

## The `arg(u) ↔ Im(q₀)` relation (exact — `computations/qbeta/qbeta_imq_anchor_carrier_probe.py`)

For `q₀ = q_r + i·ε`, `u = 2 log q₀`, the phase's leading response is **linear** in `ε`:

`d arg(u)/dε |₀ = 1/(q_r log q_r)`  — numeric = analytic = `8.63427` at `q_r = 1.10998`.

Composing with `∂S/∂φ|₀ = √3 r²` (`r = |u| = 2 log q_r`), the phase-channel **linear response**
coefficient is

`k ≡ dS/d(Im q)|₀ = √3 r² / (q_r log q_r) = 4√3·log(q_r)/q_r = 0.651275`  (exact = numeric).

So the model **measures** Im(q₀): `S ≈ k·ε` with `k` fixed. `k` is anchor-invariant to the
`22 ppb` q_r difference between the anchors (`(k_p−k_m)/k_p = 1.9×10⁻⁷`) — the `(swing)/(Im q₀)`
ratio is the SAME at both anchors. That is the "good news," and, as the test shows, also the fatal
problem.

## The falsifiable test — two ways, both fail

The proton-pin and muon-pin are two pins of the **same** q₀, differing only `~22 ppb` in q_r.

**(1) Single global Im(q₀) — ORDER-MISMATCH WALL.** With one substrate `ε`, both anchors get the
same imaginary part; the swing is driven only by the `22 ppb` q_r difference:

`swing_global(exact, ε = 0.061) = 7.42×10⁻⁹`   vs   `|S_p − S_m| = 0.0492`
⇒ **order-mismatch factor `6.63×10⁶`.**

This is the registry `dc₃/dq ≈ 4.6×10⁶` obstruction (`SRigidityPrune.lean` "What is NOT excluded")
reappearing through `arg(u)`. Structurally it is `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
for the Im(q) channel: an anchor-invariant Im(q₀) is anchor-invariant DATA and cannot produce a
swing. (The amplitude ceiling `(√3/2)r² = 0.0377` at fixed `r` is already below `|S_p| = 0.0395`.)
No physical-magnitude single Im(q₀) — even `|ε|~q_r` — reaches the swing.

**(2) Per-anchor Im(q) — UNFALSIFIABLE KNOB / FIT.** Reproducing each residual directly:

| anchor | S residual | required Im(q) = S/k | Im(q)/q_r |
|--------|-----------:|---------------------:|----------:|
| proton | −0.0395    | **−0.0607**          | −5.5 %    |
| muon   | +0.0097    | **+0.0149**          | +1.3 %    |

The two required values have **opposite sign** (forced by the merged `fig8Trace_im_odd`,
`sign S = sign ε`) and differ `4.07×` in magnitude. Two free parameters fit two data points; the
sign is set by *which lepton/baryon ratio pins q₀* — a **pinning choice** with no independent
predictor. The needed scale `~0.06` (≈5 % of q_r) is **free** — not derived, not bounded from any
independent substrate physics.

## Verdict — NOT a lead (scope-(a)). The guardrail fires.

Both failure modes fire together:

- **order-mismatch wall** — any anchor-invariant Im(q₀) is `~10⁶`–`10⁷` too small;
- **unfalsifiable knob** — per-anchor Im(q) fits any residual pair, sign-flipping on a pinning
  choice, at a free `O(10⁻²)` scale.

The reframe, tested against #4293's **proved** `∂S/∂φ`, does **not** survive as a
constrained/predicted model. "q₀ varies with Im(q) reproduces c₃" is a **per-anchor fit** unless an
independent Im(q)-scale is derived — and the only independent scales available (the `11.5–22 ppb`
μ–p residual / anchor difference) fall `~7 orders` short. This is exactly the honesty guardrail's
purpose: it keeps "q₀ varies" from being laundered into a c₃ closure.

**What would flip it to a lead** (recorded so a future route is testable, not to soften the
verdict): a *derived* Im(q₀) scale (a substrate correlation length / running / distribution width)
that predicts the two required per-anchor values `−0.061 / +0.015` — including their sign-flip —
from independently-known quantities. Because both anchors share q_r to `22 ppb`, no *smooth* running
`Im(q)=f(q_r)` can do it (same `6.6×10⁶` wall); the only remaining home is the **fibre** level,
where Im(q) is free (AGENTS.md "Im(q) at fibre vs observable level") and the *value* is already
proved measurement-limited (`no_anchor_invariant_realizes_swing`, `MeasurementLimitedFloor`). The
observable anchor comparison cannot access it.

## Lean (sorry-free, ℝ, verified lean-direct exit 0)

`content/quantum-observable-universe/lean/QOU/QBeta/ImQAnchorCarrier.lean`
(imports #4293 `ArgUPhaseBranchSelection`, Mathlib-leaf):

- `phaseResponse k ε := k·ε` — the arg(u)↔Im(q₀) linearization; `phaseResponse_real_zero` (ε=0 ⇒ 0),
  `phaseResponse_odd` (parity), `phaseResponse_hasDerivAt` (fixed slope = measurement leg).
- `global_imq_cannot_realize_swing` — one anchor-invariant Im(q₀) ⇒ same S both anchors ⇒ can't
  equal `Sp ≠ Sm`.
- `peranchor_imq_fits_anything` — `∀ Sp Sm ∃ εp εm` realizing them (unfalsifiable knob).
- `required_imq_opposite_sign` — `Sp<0<Sm ⇒ εp<0<εm` (sign-flip on a pinning choice).
- `global_imq_zero_swing_when_slopes_equal` — equal slopes ⇒ zero swing (order-mismatch root).

## Discipline

No `c_k` value produced; NO Q_β/CODATA residual inverted to define Im(q); nothing wired to
production. `conj:algebraic-geometric-dilog-equivalence` stays OPEN. Scope-(a): the Im(q) phase
channel ALONE, with a single substrate Im(q₀), does not reproduce the c₃ swing; no structural-(b)
exclusion of Im(q) as an *ingredient* is claimed (the fibre-level home remains open, value
measurement-limited).

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
