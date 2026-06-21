# Q_β c_k — Hahn–Exton trivial-kernel identification refuted (class C14) (2026-06-20)

**Status:** audit — formalize-first *refutation*. Advances the Q_β Stage-C kernel
hunt (bean `qkhc`; registry
[`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)).
EXPLORATORY — no fit, no production rewire, proposes no c_k value.

## Context

Stage C's open object is the kernel `R(q,ξ)` of the q-difference equation
`F(qξ) = R(q,ξ)·F(ξ)` whose Habiro element `F(q)` generates the c_k ladder; only
`c_2 = −1` is canonical, and the c_k live in the fibre (AGENTS.md §"Im(q) at fibre
vs observable level"). The Hahn–Exton q-Bessel coefficients satisfy the exact
first-order q-holonomic recurrence (`QBesselContiguityRecurrence.lean`), with
ratio

    r_k(q,ν) = c_{k+1}/c_k = −q^k / [(1−q^{k+1})(1−q^{ν+1+k})].

The natural first hypothesis is the **trivial kernel**: that the Q_β ladder *is*
the Hahn–Exton family for a single order ν. This probe tests it
normalization-free (via ratios), pinning ν from the one trusted ratio and
predicting the next.

## Findings

[`computations/qbeta/qbeta_hahn_exton_kernel_test.py`](../../computations/qbeta/qbeta_hahn_exton_kernel_test.py)
· witness `computations/qbeta/qbeta-hahn-exton-kernel-test.witness.json`.
Empirical: `r_2 = c_3/c_2 = +2`, `r_3 = c_4/c_3 ≈ +0.4858`.

**Level A — substrate anchor q₀ (real ν): forbidden-gap exclusion.**
With `q₀ > 1` the factor `(1−q³) < 0`, so as `q^{ν+3}` ranges over `(0,∞)` the
achievable Hahn–Exton ratio `r_2` covers `(−∞, 0) ∪ (q²/(q³−1), ∞)`. At q₀ the
upper edge is `q²/(q³−1) ≈ 3.3521`, so the interval `(0, 3.3521)` is
**structurally unreachable** for any real ν. The empirical `r_2 = +2` lies inside
that gap: reproducing it needs `q^{ν+3} = −0.676 < 0`, impossible for real ν.

**Level B — q=1 classical-Bessel shadow.** The fibre object's classical limit is
`b_k = (−1)^k/(k!(ν+1)_k)` with shadow ratio `ρ_k = −1/[(k+1)(ν+k+1)]`. Pinning
`ν = −3.1667` from `ρ_2 = r_2^emp` and predicting the next rung gives
`ρ_3 = −0.300` against `r_3^emp = +0.486` — a **sign flip** (rel err −162 %).

Both levels refute the trivial kernel; recorded as **class C14 (trivial-kernel
Hahn–Exton identification)**.

## What this buys

- **The bare Hahn–Exton ratio is excluded as the Q_β kernel.** The exclusion is
  *structural*, not numerical-fit: at q₀ the target ratio is in a forbidden gap;
  at the q=1 shadow a single ν cannot carry two consecutive rungs (sign flip).
  This is the forward (formalize-first) complement to the registry's refuted-class
  map — it closes the simplest kernel hypothesis cleanly.
- **A non-trivial kernel R(q,ξ) is required** — exactly the OPEN-keystone status
  the registry records. The gap edge `q²/(q³−1)` and the shadow sign structure
  are concrete constraints any genuine kernel must thread (it must move `r_2` out
  of the elementary Hahn–Exton range, e.g. via the extra factor structure of a
  Habiro element rather than a single q-Pochhammer order).

## Discipline

Tests one named kernel hypothesis and records its refutation; **no c_k value
proposed, no free parameter fitted** (ν is pinned by one ratio then *used to
predict*, not tuned to all rungs). No production rewire, no LP solve. The genuine
construction of `R(q,ξ)` / `F(q)` stays the OPEN keystone.

## References

- `docs/coordination/ck-dk-canonical-registry.md` — c_k canonical registry + refuted-class map.
- `docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md` — classes C1–C13.
- `content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean` — the exact Hahn–Exton recurrence.
- `computations/qbeta/qbeta_hahn_exton_kernel_test.py` — this probe.
