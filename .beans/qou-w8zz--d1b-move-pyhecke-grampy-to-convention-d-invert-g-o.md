---
# qou-w8zz
title: 'D1(b): move pyhecke gram.py to convention D, invert G on the quotient H3/rad'
status: todo
type: task
priority: normal
created_at: 2026-08-11T11:21:04Z
updated_at: 2026-08-14T21:00:10Z
---

## Update 2026-08-14 — both blocking uncertainties measured (PR #5025)

`computations/probes/gram_radical_exact_probe.py`. The banner's decision rested
on two factual claims; neither survives contact.

**1. The degeneracy is EXACT.** The banner had to quote `det = 3.998e-17`,
`cond 4.9e+16`, and noted that even mpmath at 60 dps "bottoms out at f64 noise,
not a resolved eigenvalue". That is the NF path's float64 limitation, not the
question's. `z_D = q³/(q²+1)` and `h = q − 1/q` are **rational** in q, so at
rational q the Gram is exactly rational:

| q | det(G) under D | rank D | nullspace dim | rank C |
|---|---|---|---|---|
| 11/10 | **0 exactly** | 5 | 1 | 6 |
| 7/5 | **0 exactly** | 5 | 1 | 6 |
| 13/7 | **0 exactly** | 5 | 1 | 6 |

**2. The null direction has a closed form** — and it is the q-antisymmetriser:

```
v = Σ_w (−1/q)^ℓ(w) T_w
  = γ − q⁻¹(σ₀ + σ₁) + q⁻²(L₊ + L₋) − q⁻³ e⁻
```

`G @ v == 0` exactly at all three q. This is an **independent confirmation of
`qou-u2jg` from the Gram side**, and it gives the repair an explicit projector
rather than a numerically-extracted null vector.

**3. `G_INV` has ZERO arithmetic consumers.** The banner says it is "exported at
import into constants.py, atom.py, molecular.py, sdp.py and nine corpus
consumers" and that "every consumer expects a 6×6 inverse". Surveyed over `.py`
sources: `constants.py` 0, `molecular.py` 0, `sdp.py` 0, `atom.py` 1 (a
**comment** recording the M2b move), `__init__.py` export list only. Nothing
multiplies by it — no `@`, no `.dot`, no indexing.
`computations/gram-matrix-dual.py` inverts a Gram but builds its **own**
(line 179) and imports only `z`/`NF_BASIS`/`NF_NAMES`/`TR_M` — a second instance
of the hazard, not a consumer of this one.

### What this changes

The blocker is **narrower than recorded**. A convention-D switch breaks exactly
one thing: a test asserting `G @ G_INV ≈ I`, an identity convention D makes
FALSE. That is the test reporting the mathematics correctly, not a regression.

### What is still gated

Switching `gram.py` itself, because `z`, `TR_M` and `G` **do** have consumers and
moving them moves numbers. That is untouched by this survey and remains the
owner's call. The probe removed the two factual uncertainties the decision was
resting on; it did not make the decision.
