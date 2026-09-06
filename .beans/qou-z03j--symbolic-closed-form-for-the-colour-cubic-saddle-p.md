---
# qou-z03j
title: Symbolic closed form for the colour-cubic saddle points via the palindromic reduction
status: todo
type: task
created_at: 2026-09-06T09:30:03Z
updated_at: 2026-09-06T09:30:03Z
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
