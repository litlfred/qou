# Yekutieli volume-join derivation — does the q-volume functional supply the 2.38× bridge?

**Date:** 2026-06-01
**Branch:** `claude/yekutieli-volume-join-derivation-2026-06-01`
**Scope:** DERIVE-OR-REFUTE, order by order. No fit, no hard-coded factor,
no tuning to m_p / B_AME. Builds on the three sibling audits of 2026-06-01:
- `2026-06-01-geom-full-compute-vs-paper-audit.md` (PR #1613, order-by-order)
- `2026-06-01-geom-full-perblock-wiring-fix.md` (PR #1614, RED 2.38× gate)
- `2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md` (PR #1611, Stokes wiring)
- `2026-06-01-geom-full-derivation-trace.md` (PR #1608, derivation trace)

**Compute:** [`yekutieli_volume_join.py`](../../folio-assistant/computations/yekutieli_volume_join.py),
witness [`yekutieli-volume-join.witness.json`](../../folio-assistant/computations/yekutieli-volume-join.witness.json).

---

## The question

Production computes m_p from a GLOBAL scalar
`linking_weight = (3q²+4+3q⁻²)/4` (an H₄ Wedderburn average, partitions of
**4**). The paper's per-block object is the H₃ Markov trace
`J_{𝓑₃} = Σ_{λ⊢3} w_λ χ_λ(β)/dim λ`. These differ by ≈ 2.38× at q₀, and
the sibling audit proved the ratio is **4** at h² (Jones norm), **5/2** at
h⁰, and DIVERGES at h⁴ — so no constant factor reconciles them.

**Hypothesis to derive (not fit):** the Yekutieli non-abelian Stokes step
— surface-ordered exponential → boundary holonomy = tr_M → q-hyperbolic
VOLUME evaluation → MeV — is the missing q-dependent bridge. Does the
genuine q-volume functional applied to the H₃ tr_M reproduce production at
ALL orders (verdict A), or does it give something else (B production-wrong
/ C genuinely-open)?

(Findings populated by the probe below — this is the opening stub committed
before the PR; numbers land in the next commits.)
