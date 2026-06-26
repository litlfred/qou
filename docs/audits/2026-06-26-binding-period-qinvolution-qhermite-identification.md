# Binding period `a_D^(n)` = q-deformed involution number (q-Hermite moment) — identification + two prunes

**Date:** 2026-06-26
**Branch:** `claude/z2bn-qbessel-lw-exactness-2026-06-26`
**Bean:** `z2bn` (Lever-1: derive/test the fibre q-difference kernel `R(q,x)`)
**Probes:**
[`computations/sw_period_qinvolution_identification_probe.py`](../../computations/sw_period_qinvolution_identification_probe.py),
[`computations/sw_period_bessel_half_falling_factorial_probe.py`](../../computations/sw_period_bessel_half_falling_factorial_probe.py)
**Builds on:** PR #2795 (fork settled), #2800 (`BindingQBesselKernel`, `BindingQHermiteOscillator`)

> **STATUS — crossing-moment-as-binding-object: CLOSED (2026-06-26, owner directive.)**
> The empirical dashboard test (option C, `/dashboard-sweep`) showed the crossing
> q-Hermite moment `μ_q` **collapses** at high isotope relative to the quantum-dim
> selection rule: `μ_q/a_D` runs −0.3 % (⁴He) → −96 % (²⁴Mg) → **−100 %** (⁴⁰Ca),
> because `μ_q` grows only ~involution-rate while `Σ_λ dim_q` grows ~`q^{A²/4}`. So
> `μ_q` is **not** a viable binding object past the light nuclei. Per owner directive
> the exploration was **dropped, not carried into production**: the q-Hermite dashboard
> column (`mass_binding_dashboard.py`) and the Lean formalization
> (`QOU/Mass/CrossingMomentBarEven.lean` — bar-even / positive / monotone, proven
> sorry-free) were prototyped during the exploration and are **not** part of this
> (audit-only) PR or the paper — they survive only in the exploration's git history.
> **This audit is kept as the closed record.** The findings below — the q-involution
> *identification*, the two prunes, and the no-low-order-kernel *fork* — are about the
> **quantum-dim** selection rule `Σ_λ dim_q` and stand unaffected; only the "adopt
> `μ_q` as the binding object" conclusion is closed (negative, by the collapse above).

## Question

PR #2795 settled that the binding period `a_D^(n) = lw(n−1) = (1/n)Σ_{λ⊢n} dim_q(λ)`
is **super-exponential** (the √-branch of the colour cubic; not the depth-2 SL₂
germ). This explores **what** super-exp object it is — to point the z2bn kernel
`R(q,x)` at its structural home — staying inside the no-fit / formalize-first
discipline (test structurally-motivated hypotheses, do not tune a kernel to `lw`).

## Identification (positive, verified)

Write `T_q(n) := Σ_{λ⊢n} dim_q(λ) = n·a_D^(n)`. Then

$$
T_q(n) \;\xrightarrow{\;q\to 1\;}\; \sum_{\lambda\vdash n} f^\lambda \;=\; I(n),
$$

the **involution / telephone numbers** (OEIS A000085: `1, 1, 2, 4, 10, 26, 76,
232, 764, 2620, 35696, 140152, …`).

**This holds for ALL `n` — it is a classical theorem, not a finite check.** Two
all-`n` facts compose:

1. **`Σ_{λ⊢n} f^λ = I(n)`** — the Frobenius–Schur involution identity, proved for
   all `n` by the **RSK correspondence**: RSK sends a permutation `σ` to a pair of
   equal-shape SYT `(P, Q)` with `Q = P` **iff** `σ` is an involution, so
   `#{involutions} = #{SYT} = Σ_λ f^λ`.
2. **`dim_q(λ) ─q→1→ f^λ`** — the q-hook-length formula `[n]_q!/∏_c [h(c)]_q`
   degenerates to the ordinary hook-length formula `n!/∏_c h(c) = f^λ`.

Composing (2) then (1): `Σ_{λ⊢n} dim_q(λ) ─q→1→ I(n)` for every `n`. The probe's
`sp.limit` run for `n = 1..12` is **not** where the generality lives — it
confirms (2) is computed correctly by `dim_q_via_quantum_hooks` (each limit lands
on `f^λ`, summing to `I(n)`); the all-`n` statement rides on the RSK theorem.

**Scope caveat.** This all-`n` identification is about the **q→1 limit** — it fixes
the structural *family* (q-involutions / q-Hermite moments). It does **not**
determine the q-deformed object at the substrate `q0`, i.e. the actual kernel
recurrence `R(q,x)`; that remains open (the `[n−1]_q` shortcut is pruned below,
the exact q-statistic is unknown).

**⇒ `a_D^(n) = lw(n−1) = T_q(n)/n` is the q-deformation of `I(n)/n` — a
q-involution number.** Involutions are the moments of the Hermite (Gaussian)
weight; their q-analogue is the **Rogers–Szegő / q-Hermite moment** sequence.
This is exactly the family of [`QOU.Mass.BindingQHermiteOscillator`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Mass/BindingQHermiteOscillator.lean)
(#2800). The identification:

- **explains the super-exp growth** — `I(n) ~ n^{n/2} e^{√n − n/2 − 1/4}/√2`,
  faster than any geometric (SL₂) rate, slower than `n!`;
- **pins the kernel's home** — the z2bn `R(q,x)` is the q-Hermite-moment
  recurrence, *not* a generic q-Bessel guess.

## Prune 1 (scope-a) — not a single Bessel-½ falling factorial

The √-branch order is `ν = 1/2`, so the *per-branch-point* period carries the
falling factorial `(1/2)_n`. But `lw` itself is **not** `scale · ∏[1/2−k]_q`:
the ratio `lw/|∏[1/2−k]_q|` decays monotonically (≈4.01→0.028 over `n=2..10`,
successive ratios ≈0.89→0.38), so **no rescaling closes it** — classical *or*
q-symmetric.

Structural reason (decisive, not numerical): `lw(n−1) = (1/n)Σ_{λ⊢n} dim_q` is a
**SUM over `p(n)` partitions**; a Bessel-½ falling factorial is a **single
product**. Per [`prop:sw-period-residue-sum`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/brings-surface/sw-period-residue-sum.md)
(residues = per-block Wedderburn weights, summed), the falling factorial is the
**per-block / per-branch-point period**; `lw` is the residue **sum** over blocks.

## Prune 2 (scope-a) — not the naive depth-2 q-telephone

`I(n)` obeys the depth-2 P-recursion `I(n) = I(n−1) + (n−1)·I(n−2)` — depth-2 with
an **n-dependent** coefficient (why `a_D^(n)` is super-exp and the *constant*-
coefficient SL₂ fails). The naive q-analogue

$$
T_q(n) \;\overset{?}{=}\; T_q(n-1) + [n-1]_q\,T_q(n-2)
$$

(symmetric q-bracket) is **exact at `n=3`** (rel 9e-51) but **drifts** for `n≥4`
(rel 0.003 → 0.088 by `n=10`). A separate q-holonomic guess (depth-2, Laurent
coefficients in `q^n` up to degree 3, solved + held-out-verified to 55 digits)
**did not close** either — best held-out residual ≈ 1.5e-3.

**⇒ the exact q-coefficient is not the bare `[n−1]_q`.** This is *not* a structural
exclusion of a depth-2 q-recurrence — it prunes the naive bracket. The exact
q-statistic on involutions (the Rogers–Szegő moment recurrence) is the open
frontier.

## Net for z2bn

| Hypothesis for the binding period `a_D^(n)` | Verdict |
|---|---|
| depth-2 SL₂ (`τ = tr B`) constant-coefficient | refuted at n≥5 (PR #2795) |
| single Bessel-½ falling factorial `∏[1/2−k]_q` | **pruned (a)** — it's the per-block period; `lw` is the block sum |
| naive depth-2 q-telephone `[n−1]_q` | **pruned (a)** — exact only at n=3 |
| **q-deformed involution number `I_q(n)/n` (q-Hermite moment)** | **identified (q→1 exact)** — the structural home; exact q-statistic open |

The kernel target sharpened — and then the **kernel search (below) found the
key obstruction**: the **clean** Rogers–Szegő / q-Hermite moment recurrence
`μ_q(n)=μ_q(n−1)+[n−1]_q μ_q(n−2)` belongs to the **crossing**-counted q-Hermite
moment, which **forks** from the quantum-dimension binding period `Σ_λ dim_q`
past `n=3`. The binding period itself has **no** low-order q-holonomic `R(q,x)`
(precision-confirmed). So z2bn's kernel either lives at higher order for
`Σ_λ dim_q`, or the physical binding object is the crossing moment (which *does*
sit in #2800's `BindingQHermiteOscillator` and *has* the clean kernel). No fit was
performed: every hypothesis was structurally motivated and either verified
(q→1=I(n)) or held-out-refuted.

## Kernel search — `R(q,x)` does not close at low order for the quantum-dim period

`prop:binding-genfun-qdifference` posits a **bounded-depth** q-difference kernel
`R(q,x)` for the binding generating function — equivalently, `T_q(n)` should be
**q-holonomic** (obey `Σ_j a_j(qⁿ) T_q(n+j) = 0` with `a_j` Laurent in `qⁿ`). A
high-precision search (`sw_period_qholonomic_kernel_search.py`, 90 dps, NMAX=24)
solving each candidate on its minimal set and **verifying on held-out `n`** finds
**no closure**:

| depth | Laurent deg in `qⁿ` | params | held-out | held-out max rel |
|--:|--:|--:|--:|--:|
| 2 | `[-1,1]` | 8 | 13 | 0.151 |
| 2 | `[-2,2]` | 14 | 7 | 6.7e-4 |
| 3 | `[-1,1]` | 11 | 9 | 2.45 |

The higher-degree apparent improvement is **overfitting** — the residual shrinks
only as the held-out *count* collapses, never reaching the precision floor
(~1e-80). **Decisive:** the depth-2 `[-2,2]` held-out residual is **identical at
70 and 140 dps** (6.7e-4) — precision-*independent*, hence a genuine approximation
error, not numerical. **⇒ no low-order (depth ≤3, deg ≤3) q-holonomic recurrence
for `T_q(n)`** (scope-(a): the searched range; not a proof of non-holonomicity at
all orders). Heuristic for *why*: `dim_q = [n]_q!/∏[h]_q` is a hook-**quotient**
q-term, and a partition **sum** of such quotients is generically non-holonomic;
the `q=1` case is rescued by the RSK bijection (`Σ f^λ = I(n)`) — a `q=1` miracle,
not `q`-stable.

### The fork — two q-deformations of `I(n)`

| n | `T_q(n)=Σ_λ dim_q` (quantum-dim, **the binding period**) | `μ_q(n)` (crossing q-Hermite moment, `q`-telephone `[n−1]_q`) | rel diff |
|--:|--:|--:|--:|
| 3 | 4.0109 | 4.0109 | 0 |
| 4 | 10.131 | 10.098 | 0.0032 |
| 6 | 81.359 | 79.299 | 0.025 |
| 8 | 926.61 | 853.79 | 0.079 |

Both `→ I(n)` at `q=1`; they **diverge at `q₀`**. The **clean depth-2 kernel**
`μ_q(n)=μ_q(n−1)+[n−1]_q μ_q(n−2)` belongs to the **crossing** q-Hermite moment
(2) — *not* the quantum-dimension selection rule (1) that defines the binding
period. **z2bn decision:** either the bounded-depth kernel hypothesis needs a
higher-order `R(q,x)` for `Σ_λ dim_q`, or the physical binding object is the
crossing q-Hermite moment (which *has* the clean kernel). The two are not
interchangeable past `n=3`.

## Reproduce

```bash
cd computations
python3 -u sw_period_qinvolution_identification_probe.py       # q→1 = I(n) + q-telephone prune
python3 -u sw_period_bessel_half_falling_factorial_probe.py    # falling-factorial prune
python3 -u sw_period_qholonomic_kernel_search.py               # no low-order R(q,x) + the fork
```
