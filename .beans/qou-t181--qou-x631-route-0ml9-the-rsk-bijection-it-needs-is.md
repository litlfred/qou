---
# qou-t181
title: 'qou-x631 route 0ml9: the RSK bijection it needs is now available in Lean, axiom-clean'
status: done
type: task
created_at: 2026-09-06T12:49:42Z
updated_at: 2026-09-06T12:49:42Z
---


Two contributions to `qou-x631` — the epic conjecturing
`cov(k) = Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0`, the sole open input of the
Δ_λ super-exponential growth bound. **Neither is a step toward the proof**, and
that is stated plainly because the epic has already eliminated five routes and
does not need encouragement mistaken for progress.

## 1. Route `qou-0ml9`'s formalisation dependency has landed

That route is *"RSK increasing-subsequence combinatorial interpretation of
χ^{sh(w)}(3-cyc)"*, and it needs `sh(w)` — the RSK shape of a permutation — as a
Lean object. When the route was written, the corpus had no usable RSK.

It does now, and it is unconditional:

    QOU.Mathlib.Schensted.rskEquiv (n) :
      Equiv.Perm (Fin n) ≃ { X : Σ μ : YoungDiagram, SYT μ × SYT μ // X.1.cells.card = n }

`[propext, Classical.choice, Quot.sound]` — the full bijection `w ↦ (P(w), Q(w))`
with common shape, so `sh(w)` is `(rskEquiv n w).1.1`. Measured 2026-09-06 after
building the ~48-module `QOU/Mathlib/Schensted*` cone (46 ok / 2 up-to-date /
0 errors).

**This does not advance route 0ml9's mathematics one step.** The combinatorial
identity relating `χ^{sh(w)}(3-cyc)` to increasing subsequences is exactly as
unproved as before. What changed is that the route no longer needs to build RSK
first, which is what it would have discovered on starting.

## 2. Numerical verification extended, 40 → 52

`computations/qbeta/qbeta_covariance_kernel_extend_probe.py`. `cov(k) < 0`
strictly for every `3 ≤ k ≤ 52`; `cov(2) = 0`. 43 s.

Exact integers throughout — `f^λ` by hook length in Python `int`, `Σc²` and
`C(k,2)` integral — so the **sign** is exact. Deliberate: at k = 52, `f^λ`
exceeds 10²⁵ and `(f^λ)³` exceeds 10⁷⁶, where a double would have lost the sign
of a near-cancelling sum long before the answer. The probe self-checks the hook
formula against `Σ(f^λ)² = 4!` and `f^{(2,1)} = 2` before trusting it at k = 52.

**Evidence, not support.** A conjecture with five eliminated routes is short of an
argument, not of confidence. Twelve more values of k change nothing about the
proof; the only outcome that would have mattered is a counterexample, and there
is none below 52. The probe's docstring says this so the number is not later
quoted as if it strengthened the case.

## Not attempted

The conjecture. Five routes eliminated across phases 0–2 is the work of a serious
effort, and producing a sixth in one sitting is not something to claim.
