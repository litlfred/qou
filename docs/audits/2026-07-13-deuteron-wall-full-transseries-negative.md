# The deuteron wall is not closed by the alien-calculus resummation — full trans-series undershoots ~37×

**Date:** 2026-07-13 · **Branch:** `claude/deuteron-entanglement-dual-transseries-2026-07-13` ·
**Probe:** [`deuteron_wall_full_transseries_probe.py`](../../computations/deltalambda/deuteron_wall_full_transseries_probe.py)
(+ witness) · **Scope:** (a) negative, no fit. Completes the resummation attempt
opened in [`2026-07-13-last-5-days-machinery-for-mass-binding.md`](2026-07-13-last-5-days-machinery-for-mass-binding.md)
(#3723).

## The attempt

Owner direction ("resummation = Borel? add alien calculus"; "alien calculus for
the entanglement energy dualized"). The Hopf-link deuteron has perturbative
`Vol=0`, so — in the entanglement-dual frame — its binding is carried entirely by
the non-perturbative channel: the resummed Gevrey-1/2 binding period
`a_D^(n)=I(n)/n` (`I` = involution numbers). The upgrade over the earlier
leading-term probe is the **full** level-1/2 Borel–Laplace median sum,

`P(x) = ∫_0^∞ e^{−u}·B̂_{1/2}(x√u) du`, `b_n = a_D^(n)/Γ(n/2+1)`,

median (contour ±ε around the real-axis singularity) plus the alien jump. The
deuteron candidate is `B = m_e·M_2·P(x) = m_e·P(x)` at the substrate-fixed
coupling `x` (**no tuning**). Constants are derived: singularity at `ξ=1/√2`,
level 1/2 (both Lean-proved).

## The result — undershoots ~37×

| coupling `x` | `m_e·ReP` | % of `B_D` | alien jump |
|---|---|---|---|
| `ℏ_q² = 0.0098` | 0.005 MeV | 0.2% | 0.0005 |
| `ℏ_q = 0.099` | 0.056 MeV | 2.5% | 0.006 |
| `t = ln q₀ = 0.104` | **0.060 MeV** | **2.7%** | 0.007 |
| 0.35 | 0.302 MeV | 13.6% | 0.14 |
| 0.50 | 0.423 MeV | 19.0% | 0.52 |

Best substrate value **0.060 MeV = 2.7% of `B_D = 2.225 MeV`** — undershooting by
**~37×**. The median sum reaches `B_D` only as `x → 1/√2 ≈ 0.707`, the Borel
radius, where the sum diverges *through* the singularity — and `1/√2` is **not** a
substrate quantity. So a match would require tuning the coupling to the
singularity, which is a fit (forbidden — this is exactly the laundering flagged
in the CKRecursion review).

## Verdict (scope-(a), no fit)

The **full** alien-calculus resummation of the dualized entanglement energy does
**not** close the deuteron parameter-free. This is stronger than the earlier
leading-term result: with the whole level-1/2 median Borel–Laplace summed, the
value at the physical substrate coupling is still ~37× short. The deuteron wall
is therefore a **distinct-mechanism** problem, not a resummation-coupling
problem — and the resummation hypothesis for the deuteron is closed negatively.

**What does work for the deuteron (not this route):** the separate q-rotational
channel `μ₀·ℏ_q·J_q²(j=1)` with `μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV` (derived)
reproduces `B_D` to −9% with 0 parameters (cheat-sheet "Bind" row, PR #1417).
That — not the Gevrey-1/2 resummation — is the physical deuteron binding
mechanism; the entanglement-dual resummation is the A≥3 volume tower's companion,
which the Hopf `Vol=0` structurally silences at A=2.

## Honesty note

I proposed the entanglement-dual resummation route and, held to the same anti-fit
standard as the CKRecursion review, computed it in full and report the negative
rather than tuning the coupling to fake a closure. The derived constants
(`ξ=1/√2`, level 1/2) are correct; only the *coupling* would be free, and it is
not derived — so the route is not parameter-free. No wiring; no tier change.
