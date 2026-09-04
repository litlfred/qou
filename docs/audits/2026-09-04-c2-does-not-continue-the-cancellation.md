# `c₂` does not continue the cancellation — it is the order at which the expansion stops being one

**Question asked:** do `c₂`, `c₃` continue the cancellation that takes the strongly
A-dependent leading order to a flat sum by `k = 11`?

**Answer, at A = 2 and A = 3: no, and the reason is sharper than "no".** The
second-order coefficient does not damp the A-dependence — it *grows* with A, fast
enough that by A = 3 the second-order term **equals** the first at the physical
`ℏ_q`. Beans `qou-brng` / `qou-pdg9`.

## Measured

Re-running `computations/probes/c1_leading_coefficient_derived_probe.py` on
`main` (it already computes `c₂` for the small cases; nothing new was written to
get these):

    case    A       c1        c2      c1·ℏ     c2·ℏ²    ratio
    pp      2   2.3750   11.1562   0.23532   0.10952    0.465
    pn      2   2.3125   12.5938   0.22913   0.12364    0.540
    nn      2   2.2500   13.5625   0.22293   0.13315    0.597
    T       3   2.5469   25.6641   0.25235   0.25195    0.998
    3He     3   2.6562   26.9609   0.26319   0.26468    1.006

at `ℏ_q = 1 − 1/q₀ = 0.099081716044258508` (proton pin, `q₀ = 1.1099785827513808`).
Exact values: `c₂ = 357/32, 403/32, 217/16, 3285/128, 3451/128`.

`c₁` was already known to be flat-then-decaying across A (2.31 at A = 2, 2.02 at
A = 4, 0.84 at A = 6). **`c₂` does the opposite**: ~11–13.6 at A = 2, ~25.7–27.0
at A = 3 — roughly doubling in one step.

## What that means

**The ratio column is the finding.** At A = 2 the `ℏ²` term is about half the
`ℏ¹` term, which is what an expansion should look like. At A = 3 it is
**1.00** — the two orders contribute equally. Two independent cases at A = 3
(different Z,N) agree on that to **0.8 %**, so it is a signal, not scatter.

An expansion whose second term has caught the first is not ordering anything.
So the honest reading is not "the cancellation continues at second order" nor
"it stops" — it is that **by A = 3 the `ℏ_q` expansion has lost the property
that makes `c₁` the leading behaviour at all.**

This is consistent with, and independently corroborates, the convergence defect
recorded in PR #6427: `|uic|` at ⁴He runs 1.52 → 2.15 → 3.71 → 5.67 → 8.20 across
`k = 7…11` with the increments still *growing*. Two different objects, two
different methods, the same conclusion — the series is not converged in the
region where the physics is being read off.

## The change of variable, verified rather than assumed

The probe reports `c₂ = a₁ + a₂` where `aₖ` are coefficients in `ε = q − 1`.
That is correct and worth writing out, because it is the kind of step that is
easy to take on trust:

    ℏ = 1 − 1/q = (q−1)/q = ε/(1+ε)   ⟹   ε = ℏ/(1−ℏ) = ℏ + ℏ² + ℏ³ + …

    f = a₀ + a₁ε + a₂ε² + …
      = a₀ + a₁(ℏ + ℏ² + …) + a₂(ℏ + …)² + …
      = a₀ + a₁ℏ + (a₁ + a₂)ℏ² + …

so the `ℏ²` coefficient is `a₁ + a₂`. Checked independently here; it is not
being carried over from the source's own claim.

## Scope, and what is NOT established

**Scope-(a), and narrower than the question asked.**

- **`c₃` is not measured.** Nothing here says anything about third order. The
  question asked about `c₂` *and* `c₃`; only `c₂` is answered.
- **A = 4 is not in hand.** `P_OF["4He"] = 3` and `a₂` is taken only
  `if d.p > 2`, so `c₂` at ⁴He may not survive the pipeline's precision loss.
  A run was in flight when this was written. **Two A values is a thin trend** —
  the same weakness that sank the `E ≈ 5.4 × C(A,2)` target on #6427, and it is
  flagged here for the same reason rather than after the fact.
- **A = 6 is far out of reach by this route.** ⁶Li is `n = 3A = 18` strands
  against ⁴He's 12; the ⁴He case is already the slow one at `P = 3`.
- **This does not contradict #6427's flatness result.** That measured the summed
  `unified_iterative_correction` at matched truncation and found the *total*
  flat. This measures individual coefficients of a different expansion. A
  non-convergent series can still have a flat partial sum; the two facts sit
  together and neither explains the other.

## What would settle it

The clean discriminator is `c₂` at **A = 4** — one more point, and the first that
could show the ratio exceeding 1. That needs `P_OF["4He"]` raised until `d.p > 2`
survives, which is a precision cost on the already-slowest case, not a new
derivation.
