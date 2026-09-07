# The block-and-bond product reaches `c₄` — 7/7 live, 6/6 against independent measurement

Completes the order ladder opened by `qou-qqm4`'s closed form. Beans `qou-yaig` /
`qou-qqm4`. Companion to
[`2026-09-06-c3-under-borromean-the-second-order-is-the-only-bad-one.md`](2026-09-06-c3-under-borromean-the-second-order-is-the-only-bad-one.md).

## The result

Adding one order-4 term per nucleon and per bond — each measured on a smaller
object, none fitted to any `c₄` — reproduces every checked row.

```
nucleon   a(1 + r·ε + q·ε² + s·ε³ + t·ε⁴)      t_p = -37/2   t_n = -57/2
bond      (1/2)(1 + ρ·ε + τ·ε² + υ·ε³ + χ·ε⁴)  χ_pp = 1/4, χ_pn = 31/12, χ_nn = 9/4
```

| case | A | `c₄ = a₃ + a₄` | status |
|---|---|---|---|
| pp | 2 | −585/128 | **matches measured** |
| pn | 2 | 109/192 | **matches measured** |
| nn | 2 | 27/32 | **matches measured** |
| 3p | 3 | 3197/256 | open prediction (never measured) |
| T | 3 | 743/384 | **matches measured** |
| ³He | 3 | 10001/1536 | **matches measured** |
| 3n | 3 | −1233/128 | open prediction (never measured) |
| ⁴He | 4 | **43079/6144** | **matches measured** |
| ⁵He | 5 | 73097/24576 | open prediction (never measured) |

**Two independent verifications, and they are different in kind:**

- **7/7 live.** The `--order=4` run (14 h wall) recomputed the exact ε-series for
  every `n ≤ 9` case and compared the **full coefficient vector**, order 0
  through 4, against the product's prediction. All seven agree.
- **6/6 against independent measurement.** Every `c₄` this corpus has measured by
  a different route — `c4_two_nucleon_probe` at `A = 2`, `c4_a3_a4_long_compute_probe`
  at `A = 3, 4` — is reproduced.

**⁴He is the row that carries the weight.** `43079/6144` came from an exact
series at `P = 6` (465 s, 12 controls), measured *before* this form was extended,
and feeds no input here.

## 🛑 Two corrections to my own reporting

**The run's printed table was mislabelled.** It shows headers `a4`/`c4` over
`a3`/`c3` values — the process started before the index fix
(lines 251/260/269/270 hardcoded 2 and 3 instead of `K−1`, `K`). **The verdict is
unaffected**: the pass/fail test compares the full coefficient vector, so an
order-4 disagreement would still have been caught. The table above is regenerated
with the corrected indices from the cached inputs.

**I called ⁴He an "open prediction" and it is not.** That was true when I wrote
the check-in guidance, and stopped being true a few hours later when
`c4_a3_a4_long_compute_probe` measured it — my own run, recorded in this bean and
in the merged `c₃` audit doc. Left uncorrected it would have *understated* the
result by dropping its strongest row. Guidance written mid-arc goes stale inside
the same session.

## What the order ladder now says

```
c0   product        (qou-qqm4)
c1   product        (qou-qqm4)
c2   product        (qou-qqm4)
c3   product        7002, 8/8
c4   product        here, 7/7 live + 6/6 recorded
```

Multiplicativity over blocks and bonds is **not** an order-2 or order-3 accident.
The `c₂` claim I retracted in #6983 — *"`c₁`'s per-letter additivity is special to
first order and does not propagate"* — is now wrong at four consecutive orders.

## 🛑 Scope — and one caveat here is now weaker than the probe says

The probe's own scope note reads *"SORTED orderings only; `pnp` remains the
discriminating untested case."* **That is stale as of `2aa6959078`**, which
parameterised the inter-nucleon ordering and tested `pnp` at orders 0–2:
6/6, with a control confirming `pnp` and `ppn` genuinely differ. So the ordering
caveat is partly discharged — by a sibling, at orders 0–2, for one unsorted word
at `A = 3`.

What remains:

- **`A ≤ 5`**, and `A = 5` only as an unverified prediction.
- **NOT PROVED.** The disjoint-block trace law the whole form rests on has **no
  Lean statement** — `BraidJuxtapositionMonoid` proves the monoid and the
  commutation of disjoint blocks, not trace-multiplicativity over them.
- **Unsorted orderings at order 3 and 4** are untested; `pnp` reached order 2.
- **`c₅` and beyond** are unbounded by anything here, and cost ~13× per order:
  `c₃` took 23 min, `c₄` took 14 h.
- **Nothing is wired.** These are exact rational ε-coefficients; no `q₀` is
  evaluated anywhere and no witness is emitted.

## The honest next step

Not `c₅` — the cost curve makes it a poor trade, and four orders already settle
the question the ladder was asking. **The gap that matters is the Lean one**: the
product form is now measured at five consecutive orders and rests on a trace law
nothing has stated formally.
