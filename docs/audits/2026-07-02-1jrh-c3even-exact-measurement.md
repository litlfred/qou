# 1jrh — c₃^even measured (exact-rational s-series); Casoratian W₂ > 0; W₃ stays gated

**Date:** 2026-07-02
**Bean:** `1jrh` (AW one-recurrence holomorphic-tie test) — executes the gated
measurement pinned by
[`2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md).
**Probe:** [`computations/qbeta/qbeta_c3even_exact_sseries_probe.py`](../../computations/qbeta/qbeta_c3even_exact_sseries_probe.py)
→ `qbeta-c3even-exact-sseries.witness.json` (sympy exact series, 50-dps
evaluation, 132 s wall; auditOnly, no production wiring, no fit — every number
is a Taylor coefficient of an exact object).

## What was computed

The Stage-B verdict's prescribed fix, verbatim: an **exact-rational Taylor** of
the net-route (bar-even) ladder — replacing the `mp.taylor` finite differences
whose odd-order noise (~10⁴) blocked c₃⁺ in
[`2026-06-16-hoefsmit-stage-b-attempt-verdict.md`](2026-06-16-hoefsmit-stage-b-attempt-verdict.md).
Same object, same ladder definition (`R = Q_β^net/[Q_A·cos α_eff]`,
`u = b·ℏ_q²`), series in `s = q−1` to `O(s⁹)` with exact coefficients in
`ℚ[√3, …]`.

## Results (tiered)

| quantity | value | tier |
|---|---|---|
| c₂^even | **−8.0064100587** (exact expr in witness) | measured rung — **gate PASS** vs the prior robust −8.006 |
| **c₃^even** | **+86.6611630647** (exact expr in witness) | **measured rung (new)** — same exact object/method as c₂ |
| c₄^even | ≈ −1819.74 | **scale check only, NOT a rung** — the H₃ NF basis is exhausted at k≥4 (Stage-B); a genuine c₄^even needs the H₄ build |
| `[s³] log R` | `−33/8 + √3/8 ≈ −3.9085` | exact bar-odd remainder |
| `[s⁵] log R` | `−949/96 + 39√3/64 ≈ −8.8299` | exact bar-odd remainder |
| `[s⁷] log R` | `−22013/1280 + 8317√3/5120 ≈ −14.384` | exact bar-odd remainder |

**The prior 10⁴ "blowup" was mp.taylor noise.** The true odd-order (bar-odd
remainder) coefficients are modest — O(4–14) — with closed forms in `ℚ[√3]`.
This is a new structural datum for the PR #2465 remainder-`f` constraints: the
bar-odd remainder of the *even/net* route is exact and small, not divergent.

## Casoratian test status

- **W₂ ≈ +102.674 > 0** — computed at the q→1 shadow rungs
  (`c₂^odd = −1` proved; `c₃^odd → −2` shadow):
  `W₂ = c₂^even·c₃^odd − c₃^even·c₂^odd ≈ (−8.006)(−2) − (86.661)(−1)`.
  Consistent with (does not yet test) the one-recurrence hypothesis.
- **W₃ stays GATED — but with an indicative lean.** Using the two *untrusted*
  c₄ inputs (CAL-anchored `c₄^odd ≈ −0.97`; scale-check `c₄^even ≈ −1820`):
  `W₃ ≈ (86.66)(−0.97) − (−1820)(−2) ≈ −3724 < 0`, so `W₃/W₂ < 0` — which
  **would violate** the AW-positivity sign condition. **This is scope-(a)
  indicative only**: both c₄ inputs are below trust tier (one is the very
  quantity the H₃ basis cannot supply). No refutation is declared; the
  decisive test still needs the genuine c₄ rungs (H₄ Hoefsmit build for
  c₄^even; a derivation beyond CAL-anchoring for c₄^odd).

## New constraint for the kernel search (scope (a))

The even-side rung magnitudes grow rapidly — `|c₂|:|c₃|:|c₄-scale| ≈
8 : 87 : 1820` (×11, ×21) — so the even-route `∏(1+c_k u^k)` in the *single*
variable `u` is at best asymptotic. This corroborates Stage-B blocker 2 (the
scalar u-reversion is singular; `u ~ (√3/2)s²`) from the even side: whatever
object packages both parities (the fibre kernel `R(q,ξ)`), its even sector is
not a convergent u-ladder. Constraint recorded for the `R(q,ξ)` search; it
disfavors—but does not refute—a common AW recurrence *in u*.

## Discipline

No fits: c₂/c₃^even are exact Taylor coefficients; the gate is reproduction of
the prior independent rung; W₂/W₃ are arithmetic on stated tiers. The Δ_λ gate
and the (a)/(b) refutation scoping are respected throughout (no "(b)" claims).
