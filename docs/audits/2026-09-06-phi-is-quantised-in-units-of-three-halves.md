# `φ` is quantised in units of `3/2`, both canonical words are global extrema of it — and the ruled word sits near the bottom

**Completes bean `qou-97on`** by exhausting both nucleon letter-orbits — every
one of 16 170 distinct orderings, exact `Fraction`. Beans `qou-97on` /
`qou-hu1f` / `qou-brng`.

## What was open

#6919 showed the word-level `f₁/f₀` is exactly additive across the two nucleons,
reducing the 22-letter atom-word problem to a function `φ` of an **11-letter word
on two adjacent generators**. Three facts about the canonical word were then
**sampled or local**, not proved:

- #6905 — the grouped word is a **1-swap local** maximum (0 of 196 neighbours
  beat it). 196 of 9240 is 2 % of the orbit.
- #6714 — canonical largest of **40 random shuffles**, `p ≈ 1/41`.
- #6919 — contiguity does **not** determine `φ`; that says what fails to drive
  it, not what does.

## Measured — both orbits, complete

```
proton    9240/9240 words   42.6 min   0 raised
  canonical 21/2 : 1232 attain it, 0 EXCEED it   →  GLOBAL MAXIMUM
  range −3/2 .. 21/2,  9 distinct values

neutron   6930/6930 words   32.2 min   0 raised
  canonical 8    :  990 attain it, 0 EXCEED it   →  GLOBAL MAXIMUM
  range −5/2 .. 8,     8 distinct values
```

Both computed at `n = 3` rather than `n = 6`, which is what made this ~75 min
instead of the ~7 h the bean estimated. Two invariances licensed that and **both
are gated in the probe, not assumed**: `φ` is strand-count independent (`21/2` at
`n = 3, 4, 6` alike) and translation-invariant in the generator index (the
neutron's letters on `{3,4}` at `n = 6` give `8`; remapped to `{0,1}` at `n = 3`
they give `8`).

## The finding: `φ` is quantised

```
proton  : 21/2  9  15/2  6  9/2  3  3/2  0  −3/2
          1232 528 1364 1210 1166 1518 1166 924  132

neutron :    8  13/2  5  7/2   2  1/2   −1  −5/2
           990   660 1067 902 1166 660 1089  396
```

Every consecutive gap in **both** spectra is exactly `3/2`. Nine thousand two
hundred and forty words produce **nine** values; six thousand nine hundred and
thirty produce **eight**. There are no gaps in either ladder and nothing off it.

The two lattices are **offset**: proton values lie on `(3/2)ℤ`, neutron values on
`(3/2)ℤ + 1/2`. That the quantum is shared while the offset is not is a
structural fact about the two letter multisets, and is not explained here.

## The canonical words sit at opposite ends of that ladder

| word | proton `φ` | rung | neutron `φ` | rung |
|---|---|---|---|---|
| grouped | `21/2` | **top (7 of 7)** | `8` | **top (7 of 7)** |
| borromean | `3/2` | 1 of 7 | `−1` | 1 of 7 |

The grouped word is the **global maximum of both orbits**; the Borromean word —
the one made canonical by the 2026-09-05 owner ruling (`7db032fb48`, bean
`qou-hu1f`) — sits **one rung above the bottom of each**.

**This is a measurement, not an argument against the ruling**, and it should not
be read as one. `φ` is the leading `ℏ_q`-coefficient of a trace difference; being
large is not by itself a reason to prefer a word, and the ruling was made on
grounds this document does not address. What it does say is that the two words
are not near each other in this spectrum — they are its extremes — which is why
so much downstream moved when the default changed (`c₁` by a factor of 37, and
#6559's crossover finding entirely).

## What this upgrades

- **#6905's local maximum → global.** Not just unbeaten in the 1-swap
  neighbourhood but unbeaten in the whole orbit, both nucleons.
- **#6714's `p ≈ 1/41` → exhaustive.** No sampling argument remains.
- **And a refinement that cuts the other way: the canonical word is NOT unique.**
  1232 proton words (13.3 %) and 990 neutron words (14.3 %) attain the maximum.
  So "the canonical ordering maximises `φ`" is true, and "the canonical ordering
  is picked out by maximising `φ`" is **false** — the maximum is a large plateau,
  not a point. Anyone reaching for extremality as a *selection principle* for the
  canonical word should read that number first.

## What is NOT established

- **Scope-(a), `A = 2`.** One nucleon pair's letter multisets, `include_inter =
  False`. Nothing here about the inter-nucleon terms, which is where the binding
  lives and which is exactly what breaks the disjoint-strand premise the
  reduction rests on.
- **The `3/2` quantum is unexplained.** It is measured, twice, on two different
  multisets. No derivation is offered and none should be inferred from the
  coincidence that `3/2` also happens to be the Borromean proton value.
- **The lattice offset is unexplained** likewise.
- **Nothing about heavier nuclei.** The orbits grow factorially; `A = 3` is not
  reachable this way.

## Cost, for whoever extends it

    proton   9240 words   42.6 min      (n = 3, P = 3, exact Fraction)
    neutron  6930 words   32.2 min
    per word ~0.28 s at n = 3, ~2.8 s at n = 6

The `n = 3` reduction is a 9× saving and is the only reason this is a routine
run rather than an overnight one.
