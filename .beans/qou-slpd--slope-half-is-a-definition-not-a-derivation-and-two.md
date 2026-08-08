---
# qou-slpd
title: 'ROAST: slope ½ is a definition, not a derivation — and two files use reciprocal q-Gevrey conventions'
status: todo
type: task
priority: high
created_at: 2026-08-08T02:00:00Z
updated_at: 2026-08-08T02:00:00Z
---

Found while looking for the *one* C1 result that has a downstream consumer.
Per `qou-c1wr`, the connection matrix / divisor / `χ` arc is orphaned; what
**is** consumed by `conj:qdifference-kernel-prolongation-symbol` (and through
it by `predicted-spectra/schwinger-measure-computational-time.ts`) is route
(A)/(B)/Door-i: the **Newton-polygon slopes** `{½,½}` for C1 versus `{−1,+1}`
for GGM, and the isoclinicity obstruction built on them.

So that chain is where Lean effort actually pays. It turns out to be thinner
than it looks.

## 1. The consumed chain, and what is actually proved in it

| step | status |
|---|---|
| C1 `∞`-side recursion `c_{m+1} = c_m(1 + (q−1)qᵐ + (q−1)q^{2m})` | from a witness — **not Lean** |
| ⟹ ratio q-degree `= 2m+1` | **asserted in a docstring**, not derived |
| ⟹ `deg_q cₙ = n²` | Lean ✅ `c1FormalDeg_eq_sq` — but it is "the sum of the first `n` odd numbers is `n²`" |
| ⟹ C1 slope `= ½` | **`def c1Slope : ℚ := 1/2`** — a definition |
| ⟹ no ramified pullback reaches GGM | Lean ✅ `pullback_cannot_reach_ggm` — ℚ arithmetic, *given* the two definitions |

`ThetaSlopeArithmetic.lean` is honest that it is "pure ℚ arithmetic on slopes".
What it does **not** say is that `c1Slope` and `ggmSlopes` are inputs rather
than outputs, so the "permanent invariant" conclusion inherits their status
(numerical / literature-read), not the status of a theorem.

To be fair to it: `bar` and `prodSlope` are *not* free-floating definitions —
`QGevreyOrder.bar_negates` and `QGevreyOrder.prod_adds` derive exactly those
laws from `IsQGevreyOrder`. It is specifically the two **slope values** that
are stipulated.

## 2. The convention clash (fixed today, at least as a flag)

`QGevreyOrder.IsQGevreyOrder q s a` ⟺ `‖aₙ‖ ∼ Cⁿ q^{s n²/2}`. Under it:

* `routeB_gaussian_order_half` — `q^{m²/4}` has order `½`. ✅ proved
* `qSquare_gaussian_order_two` — `q^{n²}` has order **2**. ✅ proved today

But `C1FormalSolutionGrowth.lean` called its `q^{n²}` growth "the q-Gevrey-½
divergence". Both conventions are in the literature — order `s` as `q^{s n²/2}`
(this corpus, and RSZ for the Newton-polygon slope) versus order `s` as
`q^{n²/(2s)}` (Ramis–Zhang elsewhere) — and they are **inverses**. So the two
files cannot both be using the formalised one, and the number `½` is what gets
carried across them by prose.

Done today: added `qSquare_gaussian_order_two` next to
`routeB_gaussian_order_half` so the clash is visible in one file, and corrected
`C1FormalSolutionGrowth.lean`'s docstring to flag it. **Deliberately not
silently flipped** — which label is *intended* is an owner call, and getting it
backwards would invert the Door-i argument's direction.

## 3. What would actually close this

In increasing cost:

1. **Owner decision**: which convention is the paper's? One line, unblocks the
   rest.
2. **Derive the ratio degree.** `1 + (q−1)qᵐ + (q−1)q^{2m}` as a `Polynomial ℤ`
   has `natDegree = 2m+1` (leading term `(q−1)q^{2m}`; the `m = 0` case has
   leading coefficient `2` rather than `1`, so it needs its own branch). Then
   define the coefficients by the polynomial recursion and get
   `natDegree (cₙ) = n²` from `natDegree_mul` instead of from an asserted
   ratio degree. Small — a few dozen lines — and it makes `c1FormalDeg_eq_sq`
   load-bearing rather than decorative.
3. **`IsQGevreyOrder` for the actual sequence.** Currently the order theorems
   are about the explicit functions `q^{m²/4}` and `q^{n²}`, not about C1's
   `cₙ`. With `(q−1)q^{2m} ≤ M_m ≤ (2q−1)q^{2m}` and a squeeze on
   `2 log_q cₙ / n²`, `IsQGevreyOrder q 2 (c1InfCoeff q)` is provable — ~100
   lines. This is what would let `c1Slope` be a **theorem** about the C1
   sequence rather than a stipulation.
4. **Derive the recursion itself** from `L1 = (q²x−1)σ² − (q−1)σ − (q−1)`.
   Currently from a witness. This is the real bottom of the stack.

(3) is the one that changes the epistemic status of the consumed conclusion.
(2) is cheap and worth doing regardless.

## Why this matters more than `qou-c1ln` rows 4–6

Rows 4, 5, 6 of `qou-c1ln` serve the connection matrix / divisor / `χ`, which
`qou-c1wr` established **nothing consumes**. This chain is the one that does.
If there is Lean budget for exactly one more C1 thing, it should be item 3
above, not row 4.

Relates: `qou-c1ln`, `qou-c1wr`, `qou-wgnx`.
