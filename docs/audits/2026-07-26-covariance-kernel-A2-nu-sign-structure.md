# Covariance-kernel epic (`qou-x631`) — the ν-sign structure behind FMP: Descartes narrowed, tail positivity found

**Date:** 2026-07-26 · **Branch:** `claude/covariance-nu-sign-changes-2026-07-26` · **Tier:**
route-narrowing + new structural sub-target (exact-`Fraction` probe, `n ≤ 30`) · **Discipline:**
scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack
`qou-ogrk` (A2), FMP-mechanism follow-up to
[`2026-07-26-covariance-kernel-A2-fractional-moment-family.md`](2026-07-26-covariance-kernel-A2-fractional-moment-family.md).

## Question

`M_α = Σ_v ν_v·v^α` is an exponential sum in `α`, so (Laguerre/Descartes) its number of real
zeros is at most the number of sign changes of `(ν_v)` in `v`-order. If `ν` had `≤ 2` sign
changes with the second zero of `M` on the negative axis, FMP (`M > 0` on `(0,∞)`) would follow
by pure zero-counting. Does it?

## Findings (probe [`wlambda_covariance_epic_A2_nu_sign_structure_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_nu_sign_structure_probe.py), witness [`wlambda-covariance-epic-A2-nu-sign-structure.witness.json`](../../computations/deltalambda/wlambda-covariance-epic-A2-nu-sign-structure.witness.json))

1. **Descartes as-is is insufficient (scope-(a) route-narrowing).** The sign changes of `ν_v`
   fluctuate between 5 and 9 on `n ≤ 30` — nowhere near 2. Pure coefficient-sign counting cannot
   force single-zeroness.
2. **`M` has exactly ONE real zero anyway.** The `v = 1` term is constant (`1^α = 1`) and
   `ν₁ < 0` for every `n` tested, so `M(−∞) = ν₁ < 0`; the probe finds **no** zero on the
   scanned negative axis `[−12, 0)`; `M(0) = 0`; `M > 0` on `(0, ∞)` (FMP window). So
   **FMP ⇔ `α = 0` is the only real zero of `M`** — realized with ~9 allowed zeros unused. The
   mechanism is bulk-cancellation, not sign-counting.
3. **Long-hook tail positivity (the new provable-shaped sub-target).** The sign-mixing of `ν` is
   confined to the low-`v` bulk: `ν_v > 0` uniformly for `v ≥ T(n)` with `T(n)/n` observed in
   `[0.53, 0.72]` and stabilizing near `~0.55 ≈ 1/2 + O(1/n)`. Conjecture **(TAIL)**:
   > `ν_v ≥ 0` for all `v > n/2 + O(1)`.
   This is a *discrete, per-`v` combinatorial* statement — structurally far more tractable than
   analytic positivity: a hook of length `v > n/2` is geometrically constrained (it forces a long
   arm/leg, i.e. a dominance-extreme diagram), so `N_v` for long `v` is supported on few, explicit
   partition families whose `ω₃`-covariance can plausibly be computed in closed form (the same
   locality that made the even moments polynomial).
4. `ν₁ < 0` for all `n` — the unit-hook count anti-correlates with spread (many unit hooks =
   balanced bulk diagrams = small `ω₃`); a natural companion lemma to (TAIL).

## Where this leaves the FMP program

- Not a counting argument; the plausible proof shape is now: **(TAIL) + a bulk bound** — the
  positive long-hook tail (growing weight `v^α` amplifies it) dominates the sign-mixed bulk whose
  total is pinned by the proved exact constraints (`Σν = 0`, `Σv²ν = n(n−1)(n−2)/3`, even-power
  positivity). The α-family interpolation then transports positivity down to the `α → 0⁺`
  boundary (= [A2] via the machine-checked bridge `covLnF_nonpos_of_FMP`).
- Next concrete steps: (i) exact closed forms for `ν_v` at the top values `v = n, n−1, n−2, …`
  (few contributing partitions — hand-computable, then Lean); (ii) test/prove (TAIL) at
  `v > n/2`; (iii) the Ivanov–Olshanski polynomiality of `Σ_{v>T} ν_v`-style tail aggregates.

## Honest scope

All observations exact-`Fraction` at the ν-layer, `n ≤ 30`; the negative-axis zero scan and
`v^α` evaluation are float (grid `0.05`, `[−12, 0)`). (TAIL) and FMP are conjectures; nothing
here proves A2; Descartes-as-is is a scope-(a) route-narrowing (the *method* is insufficient, the
claim is untouched). No recorded verdict overturned; nothing wired.
