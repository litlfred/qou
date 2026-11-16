---
# qou-ozyt
title: Lean-prove the colour-cubic discriminant assertions (palindromic, reciprocal, disc = -2^7*5^4)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-09-06T09:30:03Z
updated_at: 2026-10-10T14:48:58Z
parent: qou-8lxd
---

---

## 🛑 THIS BEAN'S OWN TITLE INSTRUCTS THE NEXT AGENT TO LEAN-PROVE A FALSE STATEMENT (measured 2026-10-10)

The title reads *"...(palindromic, reciprocal, disc = -2^7*5^4)"* and the bean is
**14 lines — title-only, no body**, so nothing anywhere corrects it. Taken at face
value by an agent who opens it cold, the third assertion is **false of the object
the bean is named after**.

### Measured, exactly, three ways

Integer-exact Sylvester resultant over `fractions.Fraction` (no float anywhere;
`disc(f) = (-1)^{n(n-1)/2} a_n^{-1} Res(f, f')`):

| polynomial | discriminant | factored |
|---|---:|---|
| the **sextic** `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16` | `-5120000000000` | **`-2^19 * 5^10`** |
| the reduced **w-cubic** `16w³+24w²-13w+2` | `-80000` | `-2^7 * 5^4` |
| the **trinomial** `u³ - u + 2/5` | `-8/25` | `-2^3 / 5^2` |

So `-2^7*5^4` is the **w-cubic's** discriminant, never the sextic's. The two differ
by `2^12 * 5^6`, which is the `z³ * (125/4)` substitution chain `qou-z03j` records.

### Where the corpus already agrees, and the one site that does not

Four sites attribute `-80000` correctly to the reduced cubic:

- `computations/probes/colour_cubic_discriminant_structure_probe.py:37,220` — in a
  live `check()` assertion, naming `16w³+24w²-13w+2` in the same sentence.
- `folio/quantum-observable-universe/lean/QOU/Brings/ColourCubicBranchLocus.lean:33`
  — *"**That cubic** has discriminant `-80000 < 0`"*, two lines under the line that
  introduces the w-cubic.
- `qou-z03j`'s correction table, rows 26-27.
- This bean, only if the reader supplies "of the w-cubic" themselves.

**The defective site is one docstring sentence:**
`folio/quantum-observable-universe/lean/QOU/Brings/ColourCubicDiscriminant.lean:42`

    The sextic's own discriminant is `-80000 = -2⁷·5⁴`.

It is wrong, and it is wrong **against its own file**: the substitution chain at
lines 35-37 of that same docstring names `16w³+24w²-13w+2` as a *different*
polynomial from the sextic, and the trinomial figure `-8/25 = -2³/5²` three lines
down is correct. One number in a three-number docstring.

### What is ALREADY Lean-proved of this bean's three assertions

Checked by declaration, not by grep for the bean's words:

| assertion | status |
|---|---|
| palindromic | **proved** — `QOU.Brings.ColourCubicBranchLocus.w_cubic_of_palindromic` |
| reciprocal | **proved twice** — `ColourCubicBranchLocus.disc_inv_mul` (over `ℂ`) and `QOU.Mass.ColourCubicDiscriminant.colourDiscriminant_reciprocal` (over generic `[Field K]`), plus `branchLocus_inv_mem` / `colourDiscriminant_root_iff_inv` |
| `disc = -2^7*5^4` | **not a theorem anywhere** — prose only, at the two sites above |

The double proof of reciprocity is **deliberate, not drift**: `qou-z03j` records that
the generic-`[Field R] [CharZero R]` statements "would not compose against the
`ℂ`-specific originals", and the file says so at its top. Do not consolidate them
as a duplicate without reading that.

### So this bean is two thirds done and its last third is mis-stated

The honest remaining work is **not** "Lean-prove `disc = -2^7*5^4`". It is one of:

1. Lean the w-cubic's discriminant as `-80000` (a `norm_num`/`decide` on integers,
   and true), retitling this bean to say *of the reduced cubic*; or
2. Lean the sextic's discriminant as `-2^19*5^10` (true, measured above, and a
   number the corpus has never recorded anywhere — a new claim, not a corpus-derived
   one); or
3. both, which is what makes the `2^12*5^6` ratio checkable.

### NOT fixed here, and why

Correcting line 42 would be exemption 2 of §🟥 ASK THE OWNER for the *removal* (the
corpus fixes that `-80000` is the cubic's), but **not** for the *replacement*:
`-2^19*5^10` is my computation, not a corpus artifact, so writing it into a Lean
docstring is a new mathematical claim in a math repo. Owner call. The measurement
stands either way and is reproducible from the table above.

### Provenance

Found via a read-only cross-session pre-read of the 15 open `8f-colour` beans
(notes at `/mnt/project-files/eightfold/8f-colour-preread.md`), which named the
file path verbatim and hand-verified that `-80000` belongs to the cubic. Its
companion figure `-2^19*5^10` for the sextic — which it flagged as unverified and
which appears nowhere in this corpus — is **confirmed exactly** above.

**My own error, recorded because it is the taxonomy's own failure mode.** I first
reported the pre-read's finding as *refuted*, having searched
`QOU/Mass/ColourCubicDiscriminant.lean` (no `80000` at all) and
`QOU/Brings/ColourCubicBranchLocus.lean` (`80000` present, correctly attributed) and
concluded the path given was a blend of the two names. The path was **verbatim
correct**; a *third* file, `QOU/Brings/ColourCubicDiscriminant.lean`, exists and is
the one that carries the defect. Three files whose names are permutations of
`{Brings, Mass} x {ColourCubicDiscriminant, ColourCubicBranchLocus}`, two of which
exist, and I treated a correct path as approximate. Do not second-guess a path that
resolves.

## 2026-10-10: the removal half is now done; the replacement value is still the owner's

`QOU/Brings/ColourCubicDiscriminant.lean`'s docstring no longer attributes
`−80000 = −2⁷·5⁴` to the sextic. It now says that value is the discriminant of the
reduced cubic `16w³ + 24w² − 13w + 2`, as `ColourCubicBranchLocus.lean:33` states,
and not of the sextic. That is exemption 2: the corpus already fixes the attribution.

The sextic's own value `−2¹⁹·5¹⁰` is **deliberately not written in**, for the reason
given above: it is a computation and not a corpus artifact. It has now been
re-confirmed independently, by a separate integer-exact Sylvester resultant in a
different session, so two sessions agree. Writing it into the file, and either Lean
theorem (options 1 to 3 above), waits on the owner.

One practical note for whoever proves it. Mathlib's `Cubic.discr` lives in
`Mathlib.Algebra.CubicDiscriminant`, which imports `Mathlib.Algebra.Polynomial.Splits`.
Neither olean is in the restored `lake-cache/qou-v4-24-0` paper tree as of this date,
so the cone has to be built with lean-direct first.

## Progress Note (2026-11-16)
- Formalized the reduced colour w-cubic discriminant `cubicDiscriminant 16 24 (-13) 2 = -80000 = -(2^7 * 5^4)`, the depressed trinomial discriminant `-8/25 = -2^3/5^2` (scaling factor `2^4 * 5^6 = 250000`), and the full palindromic sextic discriminant `-2^19 * 5^10 = -5120000000000` in `QOU/Eightfold/T29FluxTubeLatticeAndColourDisc.lean` (`colour_w_cubic_and_trinomial_discriminant_certificate`) + 50-dps Cardano root check in `t29_flux_tube_lattice_and_colour_disc_probe.py` (PR `litlfred/qou#8168`, head `bca84d0884fa3fb226f06011fff4d42b6b78d003`).
