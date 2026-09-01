# Growth rates, truncation error, support, and stability of the Magnus Ω₂ sign

**Date:** 2026-08-30
**Question (owner):** for high A we cannot exhaust the partitions. Can we bound the
number needed for a target precision (e.g. 60 dps)? What is the support — can we
reduce it? More symmetries? Closed forms?

**Object.** `P(A) = Σ_{λ⊢n} c_λ`, `c_λ = y_λ·tr(ρ_λ Ω₂_λ)`, `y_λ = d_q(λ)²/[n]_q!`,
`n = 3A`. Order parameter: **`b(λ) = n − λ₁`** (boxes below the first row). Probe:
`magnus_sign_growth_analysis.py`.

## 1. The contribution concentrates on low `b` — measured

| `b` | A=3 share of Σ\|c\| | A=4 share (partial) | ratio to `b−1` |
|---|---|---|---|
| 1 (reflection rep) | 86.5% | 92.2% | — |
| 2 | 11.3% | 7.2% | ~0.08–0.13 |
| 3 | 1.24% | 0.43% | ~0.06–0.11 |
| ≥4 | <0.5% | <0.2% | — |

Low `b` dominates, and **the `b=1` share GROWS with A** (86%→92%). The high-`b`
levels are small and noisy (and A=4 is partial), so the *asymptotic* rate is not
yet cleanly measured.

## 2. 🛑 The weight bound does NOT concentrate — the key negative

The a-priori bound `|c_λ| ≤ (q^L·‖Ω₂_λ‖)·y_λ·dim_λ` (worst case `|tr|≈dim`) is
computable from hook-length formulas alone. Grouped by `b`, `Σ_λ y_λ·dim_λ`:

| A | `b=1` share | tail `b>1` | tail `b>2` | tail `b>3` | tail `b>5` |
|---|---|---|---|---|---|
| 3 | 4.08% | 0.551 | 0.531 | 0.519 | 0.506 |
| 4 | 2.74% | 0.514 | 0.507 | 0.504 | 0.503 |
| 6 | 1.11% | 0.501 | 0.500 | 0.500 | 0.500 |
| 8 | 0.42% | 0.500 | 0.500 | 0.500 | 0.500 |

**The bound tail PLATEAUS at 0.5 for every K and every A.** So the observed
concentration of `|c_λ|` is **not** a property of the weight `y_λ` — it is driven
entirely by `|tr(ρ_λ Ω₂_λ)|` being *small* for high-`b` (fat) partitions. **The
naive norm bound `|tr| ≤ q^L·dim` is uselessly loose** and a rigorous error bound
cannot be built from the weights. (`tr(Ω₂)=0` exactly — the control — so the trace
is a cancellation that fat partitions kill.)

## 3. Representation stability — the framework (opposite trends with A)

Compare §1 and §2: the `b=1` share of `Σ y·dim` **decreases** with A
(4.08%→0.42%), while the `b=1` share of `Σ|c|` **increases** (86%→92%). Therefore
`|tr(ρ_λ Ω₂_λ)|/dim_λ` **decays *more* steeply with `b` as A grows.** That is the
signature of **representation stability** — the sequence of `S_n`-representations
stabilising (Church–Ellenberg–Farb FI-module theory), where a quantity organised
by "shape below the first row" converges to a limit depending only on that shape,
not on `n`. If the germ-trace is FI-stable, each `b`-level's (normalised)
contribution has a **stable closed form computable at small n and reused for all
A** — the symmetry and the closed forms the question asks for.

## 4. Support and the partition count — A-independent count, poly cost

`#{λ⊢n : b(λ)=k} = p(k)` for `k ≤ n/2` — **independent of n**. So the support up to
level `K` has `Σ_{k≤K} p(k)` partitions, **A-independent**:

| K | support `Σ_{k≤K} p(k)` |
|---|---|
| 1 | 2 | (sign lives here) |
| 3 | 7 |
| 5 | 19 |
| 10 | 139 |
| 12 | 272 |

The per-partition **dimension** at level `k` grows `~n^k`, so the cost of level `k`
is `~n^{2k}·L` — **polynomial in A for fixed `K`**. Consequences:

- **Sign / few digits: K≈1–3, a handful of small reps, cost ~A⁴–A⁶.** Cheap,
  A-bounded count.
- **60 dps: `K` is set by the tr-decay rate `r` via `r^K < 10^{-60}`.** With the
  low-`b` rate `r≈0.1`, `K≈60` and support `Σ_{k≤60}p(k)~10⁶`; but the rate appears
  to *slow* at higher `b`, so this `K` is a lower bound until the asymptotic `r` is
  measured. The dims at those levels are large, so 60 dps is poly-but-expensive —
  the sign and modest precision are the cheap regime.

## 5. The leading term (reflection rep) — closed-form target

`tr(ρ_{(n-1,1)} Ω₂)` for A=2..6 (dim `3A−1`, trivially computable):

| A | dim | `L` | `tr(ρΩ₂)` | ratio A/(A−1) |
|---|---|---|---|---|
| 2 | 5 | 23 | −337.955 | — |
| 3 | 8 | 35 | −2271.09 | 6.72 |
| 4 | 11 | 47 | −12210.8 | 5.38 |
| 5 | 14 | 59 | −58915.2 | 4.82 |
| 6 | 17 | 71 | −266114.4 | 4.52 |

**Negative for all A, with a converging inter-A ratio** ⇒ a closed form of the type
`poly(A)·μ^A`. This single term is the dominant part of the sign and needs no
representation theory beyond the `(3A−1)`-dim standard rep. Fitting/deriving it
(C2) gives the sign's leading behaviour in closed form.

## 6. Answers, plainly

- **Bound #partitions for a target precision?** The *count* is A-independent
  (`Σ_{k≤K}p(k)`), `K` set by the tr-decay rate. For the **sign and modest
  precision, K is O(1)** ⇒ trivially few partitions, any A. For **60 dps we cannot
  yet bound it rigorously** — it needs the tr-decay theorem (§2), the one open item.
- **What is the support / can we reduce it?** The effective support is the low-`b`
  partitions (`λ₁` near `n`). It is already small; a *rigorous* reduction needs the
  tr-decay proof.
- **More symmetries / closed forms?** Transpose `λ↔λ′` is REFUTED (measured, 14/14
  pairs, prior audit). The real structure is the **`b`-level / representation-
  stability organisation** (§3) — the route to per-level closed forms — with the
  reflection-rep `poly(A)·μ^A` (§5) as the leading one.

## 7. The open item (what would make it rigorous)

Prove `|tr(ρ_λ Ω₂_λ)|` decays with `b(λ)` (equivalently, FI-stability of the germ-
trace with an effective decay rate). This converts §1's heuristic into a rigorous
truncation bound and pins the 60-dps partition count. It is a cumulant/cluster-
expansion statement (`tr` of the traceless curvature `Ω₂` against fat partitions),
directly matching the newly ingested Procacci–Yuhjtman (Penrose tree-graph) and
Rebenko (canonical virial) papers. This is the highest-value theoretical target.
