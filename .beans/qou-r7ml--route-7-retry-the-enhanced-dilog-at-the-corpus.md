---
# qou-r7ml
title: 'Route 7: retry the enhanced-dilogarithm reading at the corpus modulus ℂ/2π²ℤ'
status: completed
type: task
priority: normal
tags:
    - qbeta
    - dilogarithm
    - 5two
    - refuted
created_at: 2026-08-07T15:20:00Z
updated_at: 2026-08-07T15:58:00Z
parent: 0yqu
---


## ✅ RESOLVED 2026-08-07 — Route 7 REFUTED scope-(a). See "Verdict" at the bottom.

**The motivating hypothesis (the modulus) was wrong, and the probe found a real
defect in Route 6's stated reasoning anyway.** Read the verdict section before
the framing below it, which is preserved as written *before* the computation.

## What is open

Route 6 (`qou-0yqu`, 2026-08-07 night) tested Zagier's **enhanced dilogarithm**

    D̃(ẑ) = Li₂(z) + ½·u·v    on   X̃ = {(u,v) : eᵘ + eᵛ = 1}

against the 5₂ sum rule and refuted it **scope-(a)**: no integer branch offset
matches, residual exactly `πi(2b+k)u − b²π²`, leaving
`Σⱼ Re D̃(yⱼ) = π²/2 − (2/3)πθ` with `πθ ∉ π²ℚ`.

`D̃` is valued in **`ℂ/(π²/2)ℤ`** — Zagier's modulus.

**But the corpus has independently established, for these exact `Vⱼ`, that
`V` is `ℂ/2π²ℤ`-valued** (`docs/coordination/1ppq-qbeta.md`, 2026-07-18, GGM
§6.1 5₂ port; σ3-pair positions are lattice representatives). That is a
**factor-4 different modulus** from the one Route 6 imported.

Route 6's refutation is **scope-(a)** and explicitly declines to exclude "a
formulation at a different covering point or Bloch element". The corpus's own
`2π²` lattice is exactly such a candidate and **was never tried**.

## Why it is worth trying

* `−3π²/2 = −(3/4)·2π²` — the sum-rule target is a **quarter-lattice point** of
  the corpus modulus. Either the mechanism or a coincidence; cheap to tell apart.
* Route 6's residual `πi(2b+k)u − b²π²` has a `b²π²` term. Under a `2π²` modulus
  the admissible `b` are constrained differently than under `π²/2`, so the
  offset search Route 6 ran does **not** transfer — it must be redone.
* The relevant torsion fact is already Lean-proved on this branch:
  `d[yⱼ]` is **3-torsion**, not zero (`three_smul_wedge_eq_zero`). A correct
  formulation has to track that; note `3 | 3π²/2` in the obvious way.

## How to test it — cheap, before any Lean

Numerical, against the existing 80-dps data. Search integer branch offsets under
the `2π²` lattice and check whether `Σⱼ Re D̃(yⱼ)` lands on `−3π²/2` for some
admissible assignment. **Control required**: run the same search on the control
cubics (`y³−y²+2y−1`, and the four `Πy = 1` controls from `qou-0yqu`). If a
match appears on the controls too, it is bookkeeping, not 5₂ arithmetic — the
same trap that killed Route 2.

## Prior art / do not redo

* Route 6's setup, roots on `2u = 3v + 2πik`, and its exact residual — reuse the
  algebra, change only the modulus.
* `Σⱼ D(yⱼ) = 0` is automatic (Route 2). The **individual** value is not:
  `3·D(y₊) = Vol(5₂)` to 20 digits (#4666). Do not re-derive either.

## Honest prior

Six routes tried, six not closing. This is the seventh and it is a **retry of a
refuted route with one parameter changed** — the base rate for that is poor.
Kill it fast on the controls if it does not separate 5₂ from them.

## Refs

* parent: `qou-0yqu`; ledger `docs/coordination/1ppq-qbeta.md`
* `QOU/QBeta/FiveTwoSaddleCurve.lean` — `u0_cubic_discriminant`, sorry-free
* Zagier, *The Dilogarithm Function* §II.1 B — `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf`
* PR #4658

---

## Verdict (2026-08-07) — REFUTED scope-(a), and the stated motivation was wrong

Probe `computations/probes/qbeta_5two_route7_enhanced_dilog_branch_freedom_probe.py`,
witness `computations/qbeta-5two-route7-enhanced-dilog-branch-freedom.witness.json`,
8 gates, 60 dps, all pass.

### 1. The modulus hypothesis is WRONG — `2π²` vs `π²/2` is irrelevant

The branch shift contributes `−2π²·aⱼbⱼ`, which is a multiple of `2π²` **and**
of `π²/2` alike. No statement in this setup can distinguish the two moduli.
The quarter-lattice coincidence `−3π²/2 = −(3/4)·2π²` that motivated this bean
**was not the mechanism.** Recorded so nobody re-runs it on the same hunch.

### 2. But Route 6's *stated reason* is incomplete — a real defect

Route 6's witness gate G3 ("`Σⱼ Re D̃` is an exact rational multiple of `π²/2`")
was evaluated at the **principal branch only** — one number,
`2.777534425978115064062537`, ratio `0.5628…`, not an integer, refuted. **It
never varied the branch integers for the sum.** (Its G1 does scan `(n,m) ∈
[−2,2]²`, but for the different per-root claim `Vⱼ = 3·D̃`.)

With `u = log y + 2πia`, `v = log(1−y) + 2πib`, the shift adds
`−π·bⱼ·arg(yⱼ) − π·aⱼ·arg(1−yⱼ) − 2π²·aⱼbⱼ` — **two** free integers per root.
Using `Σⱼ Re L = π²/2 − (2/3)πθ` and `arg(1−y₁) = (2/3)(θ−π)` (both verified to
61 digits), the `θ` term cancels iff

    3(b₁ − b₂) + 2(a₁ − a₂) = −2

**Route 6's `a = 0` reduces this to `3(b₁−b₂) = −2`, insoluble over `ℤ`** — which
is exactly why it saw "no integer branch offset matches". With `a` free it *is*
soluble, and exact rationality *is* reachable. So the refutation held for the
wrong reason.

### 3. The rationality is worthless — it is generic bookkeeping

The reachable set is exactly

    Σⱼ Re D̃(yⱼ) / π²  ∈  11/6 + 2ℤ

derived (`1/2 + (2/3)k − 2m`, `k = a₁−a₂ ≡ 2 mod 3`, `m = Σaⱼbⱼ`) and
brute-forced over `a,b ∈ [−4,4]` (64 values, all `≡ 11/6 mod 2`).

**The kill:** every control cubic `y^p = (1−y)^q` lands in its own `π²ℚ` coset
with the same modal spacing 2 — including the bean's named control
`y³−y²+2y−1`, which *is* `y³ = (1−y)²`. Rationality separates nothing. **Same
failure mode as Route 2:** the property is generic to the shape, not arithmetic
of the 5₂ trace field.

### 4. And both targets are excluded anyway

Neither `−1/2` (the Route-6 witness's own target, from `V = 3·D̃`) nor `−3/2`
(the raw sum-rule constant) lies in `11/6 + 2ℤ`.

### Scope

**scope-(a).** This formulation fails, now with an *exact reachable set* rather
than a failed search — strictly sharper than Route 6. It does **not** exclude a
formulation at a different covering point or Bloch element; no such invariant is
claimed.

**Route count now 7 tried, 7 not closing. Sum rule: verified to 80 dps,
unproved — UNCHANGED.**
