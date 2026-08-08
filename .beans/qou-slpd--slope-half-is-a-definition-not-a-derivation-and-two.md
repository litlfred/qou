---
# qou-slpd
title: 'ROAST: slope ½ is a definition, not a derivation — and the two ½s are order vs level'
status: todo
type: task
priority: high
created_at: 2026-08-08T02:00:00Z
updated_at: 2026-08-08T04:30:00Z
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

## 2. RESOLVED against RSZ, 2026-08-08 — it is ORDER vs LEVEL

I first wrote this section as "two files use reciprocal conventions, owner must
pick one". That framing was wrong, and reading the source settled it. RSZ,
Astérisque 355 §1.3.2, verbatim:

> we introduce the space of formal series of q-Gevrey **order** `s`:
> `C[[z]]_{q;s} := { Σ aₙzⁿ | ∃A > 0 : aₙ = O(Aⁿ q^{s n²/2}) }`.
> We also say that `f ∈ C[[z]]_{q;s}` is of q-Gevrey **level** `1/s`.

So there is no ambiguity in RSZ and no competing convention to choose between.
There are **two distinct quantities with distinct names**, and they are
reciprocal. `QGevreyOrder.IsQGevreyOrder` is RSZ's *order*, on the nose.

Consequences:

* Route-B kernel `q^{m²/4}` — **order ½, level 2**.
* C1 `∞`-side `q^{n²}` — **order 2, level ½**.

Neither file wrote a wrong number. `C1FormalSolutionGrowth`'s "q-Gevrey-½
divergence" is **correct RSZ terminology for the level**. The defect was that
one word was doing two jobs.

Fixed today, as formal content rather than prose:

* `IsQGevreyLevel q d a := IsQGevreyOrder q d⁻¹ a`, with
  `isQGevreyLevel_iff_order`, `isQGevreyLevel_of_order`, `level_unique`.
* `qSquare_gaussian_level_half`, `routeB_gaussian_level_two`,
  `routeB_and_c1Inf_are_reciprocal` — so both numbers for both sequences are
  machine-checked, not asserted.
* `C1FormalSolutionGrowth` and `ThetaSlopeArithmetic` docstrings corrected and
  given precise RSZ section citations.

### What this does NOT settle, and it is sharper than before

RSZ attaches the **level**, not the order, to the Newton polygon: §2.3.2 calls
the two-slope case *"the one level case, because the q-Gevrey level `µ₂ − µ₁`
is the fundamental parameter"*, and Example 3.3.3 sets `d := µ₂ − µ₁` for
*"the level"*, with q-Borel kernel `tₙ` of growth `q^{n²/2d}` — order `1/d`,
consistent with §1.3.2.

But `theta_eq_half_gs_bridge` grounds `ThetaSlopeArithmetic.c1Slope = ½`
through `routeB_gaussian_order_half`, an **order**. RSZ would tie the slope to
the level. **Those cannot both be the Newton slope**, and the corpus currently
asserts the order route.

This is now a specific, falsifiable question rather than a convention
preference: *compute the Newton polygon of `L1` and see whether the slope
matches the Route-B order (½) or the C1 `∞`-side level (½ — same number, but of
the other sequence and the other quantity)*. That is item 4 below, and it is no
longer optional bookkeeping — it is the thing that decides whether the Door-i
obstruction is stated about the right invariant.

## 3. What would actually close this

In increasing cost:

1. ~~**Owner decision**: which convention is the paper's?~~ ✅ **RESOLVED from
   the source, 2026-08-08** — there was no convention to choose; RSZ §1.3.2
   defines order and level as distinct reciprocal notions and the corpus was
   using one word for both. See §2. **No owner input was needed.**
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

**Where this leaves it.** (1), (2) and (3) are done. On the `∞`-side the chain
now reads: *recursion* (still from a witness) ⟹ *ratio degree `2m+1`* ✅ ⟹
*`deg_q cₙ = n²`* ✅ ⟹ *order 2 / level ½* ✅. Only **(4)** remains, and it has
been promoted: it is no longer "derive the recursion for completeness", it is
"compute the Newton polygon of `L1` and settle which quantity `c1Slope` is".

`ThetaSlopeArithmetic` now says in its docstring that `c1Slope` and `ggmSlopes`
are stipulated and that the order/level identification is a premise, so nothing
downstream reads as more derived than it is.

## Why this matters more than `qou-c1ln` rows 4–6

Rows 4, 5, 6 of `qou-c1ln` serve the connection matrix / divisor / `χ`, which
`qou-c1wr` established **nothing consumes**. This chain is the one that does.
If there is Lean budget for exactly one more C1 thing, it should be item 3
above, not row 4.

Relates: `qou-c1ln`, `qou-c1wr`, `qou-wgnx`.

## Two adjacent items closed the same day

**`prop:mi-sw-abelianisation` — `not_checked` → `trivial`, and it is vacuous.**
One of the keystone's three `uses[]` premises had never been Lean-checked.
Checked it: the file builds and is sorry-free, but

```lean
theorem mi_sw_abelianisation (_bs) (n) (sw_period mi_integral : ℕ → ℝ)
    (fake_flat_abelian : ∀ k, mi_integral k = sw_period k) :
    mi_integral n = sw_period n := fake_flat_abelian n
```

the hypothesis **is** the conclusion, universally quantified, and the proof is a
projection. Steps (1)–(3) of its own proof outline (SU(2) bundle triviality →
fake-flatness → MI reduces to the contour integral) are all *assumed*. Set the
schema's `trivial` — the enum value for a trivially-true lemma — added an
author note, and flagged it at the declaration in `QOU/BringsSurface.lean`.
Matters because the keystone's premises should not read as Lean-backed when one
of them restates itself.

**`conj:qdifference-kernel-prolongation-symbol` `validation: "validated"` —
RETRACTED as a finding.** I flagged this as overstating, on the grounds that the
Lean ref is a `class` with no instance. That was a misreading of the schema:
`schemas/types.ts` defines `validated` as *"built and type-checked
successfully"* — a build-status field, not a proof-status claim. The file does
build (verified). The block is a `conjecture`, and the corpus already records
class-without-instance as the honest open state (§3b-tax). Nothing to fix.

## Method note, for the next agent

The convention question sat here for a day framed as "owner must decide". It was
answerable in one `grep` of a PDF already sitting in `uploads/`
(`0903.0853v3.pdf`, RSZ Astérisque 355 §1.3.2). **Read the cited source before
escalating a citation question to the owner** — the same lesson as the
2026-08-07 corpus-grep miss, in a different drawer.
