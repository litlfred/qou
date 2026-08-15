---
# qou-g2wr
title: 'Read GGM 2012.00062 / GGMW 2111.04763 for the REAL part of the 5₂ sum rule'
status: completed
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - 5two
    - literature
    - refuted
created_at: 2026-08-07T15:20:00Z
updated_at: 2026-08-07T16:20:00Z
parent: 0yqu
---


## What is open

`qou-0yqu` names **GGM (2012.00062)** and **GGMW (2111.04763)** twice as "the
realistic direct sources … which compute precisely these `Vⱼ`, and are already
in `library/`" — and **neither has been read for the sum rule.** Broadhurst was
read (2026-08-07 b); these were not.

## Why they are the right target and not another dead literature lead

The disc −23 literature (Zagier, Zagier–Gangl, Browkin–Gangl) evaluates
**`ζ_F(2)` via the Bloch–Wigner `D`** — the **imaginary / volume** side. Our sum
rule is the **real part** (Chern–Simons / second-regulator side). So the
classical ladders are *adjacent, not a drop-in* — this is the caveat recorded
prominently in `qou-0yqu` and in PR #4658, and it is correct.

GGM/GGMW are different: they compute the **`Vⱼ` themselves**, not just `ζ_F(2)`.
The corpus already has deep machinery ported from GGM — the whole 4₁ Stokes lane
is complete and GGM §6.1's 5₂ curve is Lean-proved
(`FiveTwoSaddleCurve.lean`). So this is an **internal seam**, not a cold read.

## What to look for, specifically

1. Any closed form or functional equation for `Re V` (not `|Im V| = Vol`, which
   the corpus already reproduces to 1e-10).
2. The **modulus/lattice** convention for `V` — GGM is the source of the
   `ℂ/2π²ℤ` statement the corpus carries. Confirm it and get the exact
   normalization. **This directly feeds `qou-r7ml`.**
3. Whether `Σⱼ Vⱼ` (or its real part) appears as a total-index / Stokes-data
   identity, which is where a `−3π²/2` would naturally come from.

## Watch for

The corpus's own over-claim trap: `|Im V(σ1)| = Vol(5₂)` and
`ι_12(0) = Vol(5₂)/π` are **already established**. Finding those again is not
progress on the sum rule — it is the volume side, which Route 2 showed carries
no information about our identity. Only a **real-part** statement counts.

## Refs

* parent: `qou-0yqu`; ledger `docs/coordination/1ppq-qbeta.md` (GGM entries
  2026-07-18 onward)
* `library/` — both papers present
* PR #4658

---

## ✅ READ 2026-08-07 — the papers do NOT contain the sum rule. Closed as a lead.

Both PDFs extracted in full and swept
(`library/arxiv-2012.00062v3/2012.00062v3.pdf` = GGM *Peacock patterns and resurgence in complex
Chern–Simons theory*, Garoufalidis–Gu–Mariño; `library/arxiv-2111.04763v2/2111.04763v2.pdf` = GGMW).

### The negative — this is the point of the bean

* **`Σⱼ Vⱼ` appears nowhere.** No saddle-sum identity, no `−3π²/2`, in either
  paper.
* **"real part" occurs exactly ONCE in GGM and ZERO times in GGMW.** The single
  GGM occurrence is the §6.1 prescription already ledgered 2026-07-26 — "*Note
  for σ₃, we only keep the real part of V*" — which selects a branch for the
  real connection. **It is not a statement about `Re V`.**
* No `Bloch` in either paper; no `regulator` in either. GGMW's three `Rogers`
  hits are **Rogers–Ramanujan** (modular q-hypergeometric), *not* the Rogers
  dilogarithm. **Flagged so nobody chases it.**

**The literature hope in `qou-0yqu` is therefore closed.** GGM/GGMW compute the
`Vⱼ` and their resurgence/Stokes structure; they say nothing about the real part
of their sum. Combined with the disc −23 ladder literature being the *volume*
side, there is now no known published source for this identity.

### What the read DID establish

**1. The `ℂ/2π²ℤ` modulus is GGM's, confirmed at source (eq 234):**

    V(u,v) = Li₂(y) + Li₂(xy) + Li₂(x⁻¹y) + (log(−y))²

"is a holomorphic **`ℂ/2π²ℤ`-valued** function on the exponentiated curve `S*`".
At `x = 1` this is the corpus's `V = 3Li₂(y) + (log(−y))²`, reproducing
`Σⱼ Re Vⱼ = −3π²/2` to 50 dps. So `qou-r7ml`'s premise was correctly sourced
even though Route 7 refuted.

**2. `b = (−1,+1,+1)` is *exactly* principal `Log(−yⱼ)` — verified to exact
zero at all three roots.** GGM writes `(log(−y))²`, not `(log y + bπi)²`. This
independently confirms the Lean theorem `branch_shift_eq_log_neg`.

**3. ⚠ STRUCTURAL — `Re Vⱼ` is only defined mod `2π²`.** `2π²` is *real*, so
GGM's quotient acts on the real part. In GGM's own quotient the sum rule reads

    Σⱼ Re Vⱼ ≡ π²/2   (mod 2π²)

and the **exact** value `−3π²/2` is a statement about *chosen representatives*.
Consequences:

* Any proof routed through GGM's `V` alone can only ever deliver the
  **mod-`2π²`** statement. The exact form needs the representatives pinned —
  which is precisely what `branch_shift_eq_log_neg` does. **That theorem is
  load-bearing, not bookkeeping**, contrary to how PR #4658's own summary
  framed it.
* Consistency check: GGMW's `V_GGMW = V_GGM + 2π²/3` shifts the sum by exactly
  `2π²` = **one lattice step**, giving `Σⱼ Re V_GGMW = π²/2` *exactly*. The two
  published conventions sit on adjacent lattice representatives. Verified 50 dps.

**4. GGMW §4.1 states disc −23 outright** — "*The trace field of the 5₂ knot is
the cubic field of discriminant −23, with a distinguished complex embedding σ₁
…, its complex conjugate σ₂ and a real embedding σ₃*". So PR #4658's headline
was not merely already in the corpus (`u0_cubic_discriminant`) — it is **stated
in one sentence in a paper sitting in `library/`**. Third independent source.

**5. The `σⱼ` ARE the three embeddings of the trace field** (GGMW §4.1,
explicitly). So `Σⱼ Re Vⱼ` is a sum over *all* embeddings — a **trace**. That is
the structural reason Route 5 works at all: `pₙ = Σⱼ yⱼⁿ` are rational integers
because they are traces, which is why `∏ⱼ(1−yⱼz)` has ℤ coefficients and the
integral `−∫₀¹ log P(z)/z dz` is over a *rational* polynomial. Worth stating in
the write-up; it does not evaluate the integral.

**Status unchanged: verified to 80 dps, unproved.**
