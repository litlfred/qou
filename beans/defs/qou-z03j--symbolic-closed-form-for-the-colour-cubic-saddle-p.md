---
# qou-z03j
title: Symbolic closed form for the colour-cubic saddle points via the palindromic reduction
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-09-06T09:30:03Z
updated_at: 2026-10-10T13:50:13Z
parent: qou-8lxd
---


---

## 🛑 CORRECTION — most of what I "found" the corpus already had, Lean-proved

`QOU.Brings.ColourCubicBranchLocus` (sorry-free, **2026-09-03**, bean `qou-qx7j`,
audit `2026-09-03-enclosed-pole-set-E-is-not-identifiable.md`) already proves:

| I claimed as new | already there |
|---|---|
| the sextic is palindromic / self-reciprocal | `disc_inv_mul`, `branchLocus_inv_mem` |
| `w = z + 1/z` gives `16w³+24w²−13w+2` | `w_cubic_of_palindromic` |
| discriminant `−80000` | in that audit's table |
| no rational root ⟹ irreducible | same |
| `|w| < 2 ⟹ |z| = 1` exactly | `normSq_root_eq_one` |
| the 2+4 split, reciprocal moduli `0.9430955890717590` / `1.06033790380066254` | same |

**How I missed it.** My corpus-grep filtered audit **filenames** on
`alien|resurg|borel|stokes|gevrey|divergen|transseries|dladder`. That audit is
called `enclosed-pole-set-E-is-not-identifiable` — it matches none of them. I
also ran a `saddle`∧`Bring` content grep that returned 38 files and **did not
read them**, and that hit list would have caught it. A filename filter is a
convenience, not the checklist.

## What survives as new

Checked by grep against that Lean file (0 hits for `u^3 - u`, `2 / 5`,
`trinomial`, `Cardano`):

1. **The depression** `w = t − 1/2` → `32t³ − 50t + 25`.
2. **The scaling** `t = (5/4)u` → **`u³ − u + 2/5`** — the trinomial normal form,
   linear coefficient exactly `−1`, discriminant `−8/25 = −2³/5²`.
3. **The composite chain** `colourSextic(z) = z³·(125/4)·(u³−u+2/5)`.
4. **The Cardano closed form** for the real root,
   `u = −[(1/5−√6/45)^{1/3} + (1/5+√6/45)^{1/3}]`.
5. The `ξ = 1/√2` negative.

The three duplicated theorems are kept in `ColourCubicDiscriminant.lean` only
because the new ones are stated over a generic `[Field R] [CharZero R]` and would
not compose against the `ℂ`-specific originals. The file now says so at the top.

## And this bears on `qou-l155` (pin λ_SW) — it may be already answered

That same audit's §2 concludes: **under the classical-jet prolongation every
residue vanishes individually, so every subset `E` gives period zero**
(`ddz_residue_slot_eq_zero`, `period_eq_zero_of_all_residues_vanish`), and **the
unit circle is not an admissible contour** because it passes through two branch
points. If that holds as stated, the thimble-action route to `ξ` is not merely
unpinned but **zero on the natural prolongation** — which would change
`qou-p443` from "uncomputed" to "computed and vanishing". **Not verified by me
yet**; read that audit before spending anything on `qou-l155`.


---

## The sextic's own discriminant, measured — and this bean's table row 27 is CORRECT (2026-10-10)

The correction table above lists *"discriminant `−80000`"* as already held, and it is
right to: `−80000` is the discriminant of the **reduced w-cubic** `16w³+24w²−13w+2`,
the row immediately above it. Confirmed exactly (integer Sylvester resultant over
`fractions.Fraction`, no float):

| polynomial | discriminant |
|---|---:|
| sextic `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16` | **`−2^19 · 5^10` = `−5120000000000`** |
| reduced cubic `16w³+24w²−13w+2` | `−2^7 · 5^4` = `−80000` |
| trinomial `u³ − u + 2/5` (surviving item 2) | `−2^3 / 5^2` = `−8/25` |

The sextic figure is **new to the corpus** — it appears in no file, bean or witness —
and it is the missing arithmetic check on this bean's surviving item 3, the composite
chain `colourSextic(z) = z³·(125/4)·(u³−u+2/5)`: the two discriminants differ by
exactly `2^12 · 5^6`, which is what that chain predicts. So item 3 now has an
independent confirmation it did not have when written.

**One live defect, in a Lean docstring, not in this bean.**
`folio/quantum-observable-universe/lean/QOU/Brings/ColourCubicDiscriminant.lean:42`
reads *"The sextic's own discriminant is `−80000 = −2⁷·5⁴`"*, which is the w-cubic's
value attached to the sextic — and it contradicts lines 35-37 of its own docstring,
where the chain introduces the w-cubic as a distinct polynomial. The trinomial figure
beside it is correct. Tracked with the full measurement on **`qou-ozyt`**, whose
*title* carries the same mis-attribution and which is title-only, so an agent opening
it cold would Lean-prove a false statement. Not edited: the removal is corpus-derived
but the replacement value is mine, so it is an owner call.

**Not closed**, despite the closed-form (item 4, Cardano) being delivered: items 1-5
are stated in this body and **none of them is Lean or witnessed**, and the bearing on
`qou-l155` in the section below is still an open question rather than a recorded
answer. A bean whose results live only in its own body is the thing §path-6 of the
corpus-grep checklist exists to catch, not a completed bean.

## Progress (2026-11-16T19:43:48Z)
- **Status:** `in-progress` (awaiting human review; no unilateral closure).
- **PR:** `litlfred/qou#8173` (head `ad97deb87bc648e5c129faba2fa1d69d9619253c`, script commit `bdc558a8f10d26666ba057c81bf22753e6d0aca0`).
- **Summary:** Formalized exact palindromic reduction y = x + 1/x of the degree-6 reciprocal colour polynomial to a depressed/reduced cubic and verified all 6 roots in QOU/Eightfold/BoltzmannOSPositivityAndColourSaddle.lean + 50-dps witness probe in PR litlfred/qou#8173 (head ad97deb87bc648e5c129faba2fa1d69d9619253c).
