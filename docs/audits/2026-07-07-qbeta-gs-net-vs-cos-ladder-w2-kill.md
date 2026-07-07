# Q_β crossing weight from the H₃ GS reducer — W1 PASS, W2 KILL (scope-(a))

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone, forward direction ·
**Executes:** the pre-registered W1/W2 gates of
[`docs/scope/2026-07-07-qbeta-crossing-weight-hecke-determination.md`](../scope/2026-07-07-qbeta-crossing-weight-hecke-determination.md)
(PR #3477) · **Builds on:** [KC19](2026-07-07-qbeta-crossing-weight-affine-narrowing.md)
(PR #3473) · **Tier:** symbolic-exact + numeric cross-check · **No `c_k` value,
no wiring** (registry §8 guard).

## Enabling note — the compute was not actually firewalled

The scope PR #3477 recorded the W1–W4 runs as "gated on `pyhecke` (firewalled)".
That was wrong: `pyhecke` is a **local** package (`tools/pyhecke/python`) and the
H₃ GS reducer (`qbeta_h4_nucleon_assembly.py`) is **pure sympy** — the only block
was a missing `numpy` (`pip install numpy`) + the source path. With that, the
gates run exactly.

## W1 — PASS (counit reproduction)

- **Numeric Frobenius pairing** (`pyhecke.gram`): `⟨(n−p)_{N=0}, G⁻¹𝟙⟩_G =
  h²/2 − h = −0.18720719…` to 15 digits; `ω = G⁻¹𝟙 = (0.601, 0.188, 0.188,
  0.396, 0.396, 0.026)` reproduces the net-ansatz cointegral exactly.
- **Symbolic**: the full GS `Δ(net)` agrees with the counit `h²/2 − h` through
  `O(ℏ_q²)` (both `= −2ℏ_q + ℏ_q² + …`); first deviation at `ℏ_q³`
  (`Δ(net)` has `−ℏ_q³`, counit `+ℏ_q³`).

Also verified: `Q_A = |counit · E₀|` exactly, with `E₀ = m_e/(q(q−1))` — the
production base `Q_A = m_e|q²−2q−1|(q+1)/(2q³)` **is** the N=0 counit times `E₀`.

## W2 — KILL (scope-(a)): the full GS net is not the production ladder

Take the first-principles categorical net as `Q_β^GS = |Δ(net)|·E₀` (the
`net`-ansatz relation). Then `Q_β^GS/Q_A = Δ(net)/counit`, exact:

`Q_β^GS/Q_A = 1 + ℏ_q² − 2ℏ_q³ − (57/4)ℏ_q⁴ − …`  — **cosh-like** (leading `+ℏ_q²`).

The production base is `Q_N1 = Q_A·cos(α − b·ℏ_q²/2)` (cos-**like**, `< 1`), and
the ladder variable is `u = b·ℏ_q² = (√3/2)ℏ_q² + …`, so `u ~ O(ℏ_q²)` and the
ladder `Σ_{k≥2} c_k u^k` starts at `u² ~ O(ℏ_q⁴)`. But

`Q_β^GS/Q_N1 − 1 = (9/8)ℏ_q² + …`

carries a **leading `O(ℏ_q²) = O(u)` term** (`9/8`), **below** where the
`c_2 u²` rung lives. So the full GS augmentation is **not** of the pure ladder
shape `cos·(1 + c_k u²)`; it disagrees with the production ladder at `O(u)`.

**Numeric corroboration at q₀** (proton-pinned): the full GS net gives
`Q_β = +0.746%` vs CODATA, **4.5× worse** than the N=0 truncation `Q_A`
(`+0.166%`). `Q_β^GS/Q_A = 1.00579 > 1` (cosh-like) vs the production
`Q_N1/Q_A = 0.99840 < 1` (cos-like). The categorical higher orders push Q_β
**away** from the ladder.

## Scope — what this does and does not say

**(a) scope-limited.** This refutes the hypothesis *"the full first-principles
GS augmentation `Δ(net)` equals the production `cos·(1+c_k u²)` ladder."* It does
**not** refute:

- the production ladder ansatz or any `c_k` (which is a separate cos+`c_k` object
  fit differently, not `|Δ(net)|·E₀` beyond N=0);
- the `|Δ(net)|·E₀` relation **at N=0** (W1 confirms it — the +0.17% is a
  genuine N=0 / `Q_A` property);
- any KC19 result (the affine narrowing is exact and untouched).

The finding is that the **+0.17% accuracy is an N=0 (`Q_A`) property, and the
GS higher orders spoil rather than improve it** — the effective crossing weight
the GS net implies (`w−1 = ℏ_q² − 3ℏ_q³ − …`, KC19 variables) is cosh-like, not
the cos-dressed ladder.

**Consequences for the forward direction (W3/W4 rescoped).** The naive
"full GS augmentation → ladder" route is closed (scope-(a)); the productive
question becomes *why* the categorical net is cosh-like while the observable
ladder is cos-like — i.e. what archimedean/analytic-continuation step maps the
bar-even categorical growth to the bar-odd decay face (the two-saddle Rogers↔
Faddeev structure, [torus-CS geometry scope](../scope/2026-07-06-qbeta-fmap-torus-knot-cs-phase-geometry.md)).
The `w−1` departure remains the object; its cosh-like GS value is the new
datum. **W3 (does the stabilization reproduce `c_2=−1`) is moot** for the
full-GS-net hypothesis under this kill.

## Reproducibility

Probe [`computations/qbeta/qbeta_crossing_weight_hecke_probe.py`](../../computations/qbeta/qbeta_crossing_weight_hecke_probe.py)
→ [witness](../../computations/qbeta/qbeta-crossing-weight-hecke.witness.json)
(7/7; sympy-exact series + `pyhecke` numeric pairing + mpmath q₀ accuracy). The
symbolic gates use no CODATA and no anchor; the accuracy line is a reported
numeric evaluation, not a fit. GS reducer:
[`qbeta_h4_nucleon_assembly.py`](../../computations/qbeta/qbeta_h4_nucleon_assembly.py)
(reproduces the committed `free-neutron-decay` witness at N=0). Production
ladder: [`qbeta_utils.py`](../../computations/qbeta/qbeta_utils.py).
