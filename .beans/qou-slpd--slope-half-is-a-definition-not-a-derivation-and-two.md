---
# qou-slpd
title: 'ROAST: slope ½ is a definition, not a derivation — and two files use reciprocal q-Gevrey conventions'
status: todo
type: task
priority: high
created_at: 2026-08-08T02:00:00Z
updated_at: 2026-08-08T03:30:00Z
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
2. ~~**Derive the ratio degree.**~~ ✅ **DONE 2026-08-08.**
   `natDegree_c1MultPoly` — the multiplier `1 + (q−1)qᵐ + (q−1)q^{2m}` read as a
   `Polynomial ℤ` in `q` has degree exactly `2m+1`; `natDegree_c1CoeffPoly`
   chains it through `natDegree_mul` to `natDegree cₙ = n²`. So `n²` now comes
   from the recursion rather than from a docstring. Both sorry-free,
   `[propext, Classical.choice, Quot.sound]`, in
   `QOU/Mass/C1FormalSolutionGrowth.lean`. The `m = 0` branch is the only
   wrinkle: there `(q−1)qᵐ` and `(q−1)q^{2m}` coincide, so the leading
   coefficient is `2` rather than `1` (degree unchanged).
3. ~~**`IsQGevreyOrder` for the actual sequence.**~~ ✅ **DONE 2026-08-08.**
   `c1InfCoeff_order_two : IsQGevreyOrder q 2 (c1InfCoeff q)` — not the explicit
   function `q^{n²}`, the **actual sequence** defined by the recursion. Sandwich
   `(q−1)ⁿ q^{n²} ≤ cₙ qⁿ ≤ (2q−1)ⁿ q^{n²}` by induction from
   `(q−1)q^{2m} ≤ M_m ≤ (2q−1)q^{2m}`, then squeeze: both sides of the bound on
   `2 log_q cₙ / n²` are `2 log_q(const)/n + 2 − 2/n → 2`. Sorry-free,
   `[propext, Classical.choice, Quot.sound]`, in `QOU/Mathlib/QGevreyOrder.lean`
   §MI-3(c), together with `c1InfCoeff_lower` / `c1InfCoeff_upper`.

   Note `theta_eq_half_gs_bridge` in that same file *already* flagged this gap
   — "what remains probe-only is that the kernel's actual coefficient sequence
   realises order ½". It is now closed for one actual sequence, and the answer
   is **2**.
4. **Derive the recursion itself** from `L1 = (q²x−1)σ² − (q−1)σ − (q−1)`.
   Currently from a witness. This is the real bottom of the stack.

**Where this leaves it.** (2) and (3) are done, so on the `∞`-side the chain now
reads: *recursion* (still from a witness) ⟹ *ratio degree `2m+1`* ✅ ⟹
*`deg_q cₙ = n²`* ✅ ⟹ *q-Gevrey order* ✅ **= 2**. Only (1), the owner's
convention call, and (4), deriving the recursion from `L1`, remain — and (1) is
now the blocker, because until it is answered we have a machine-checked `2`
sitting next to a stipulated `c1Slope := 1/2` with no stated relation between
them. That is a better place to be than before (the number is no longer purely
asserted anywhere), but it is not resolved.

Note the two are not *necessarily* in conflict: under the reciprocal convention
`2` and `½` are the same statement. That is exactly why (1) has to be answered
by someone who knows which the manuscript means.

## Why this matters more than `qou-c1ln` rows 4–6

Rows 4, 5, 6 of `qou-c1ln` serve the connection matrix / divisor / `χ`, which
`qou-c1wr` established **nothing consumes**. This chain is the one that does.
If there is Lean budget for exactly one more C1 thing, it should be item 3
above, not row 4.

Relates: `qou-c1ln`, `qou-c1wr`, `qou-wgnx`.
