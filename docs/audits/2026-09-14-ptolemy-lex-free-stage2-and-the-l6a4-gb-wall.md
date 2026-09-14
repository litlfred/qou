# The `5_2` wall was the lex basis; L6a4's wall is the Gröbner basis itself

2026-09-14. Bean `qou-qjhc`, issue #7346.

## 1. What was claimed, and by whom

I recorded `5_2` obstruction class 1 as **blocked on hardware**: stage 2 of
`ptolemy_exact_point.py` reached **7.9 GB RSS at 717 s** against 182 MB free on a
swapless 16 GB container, was killed, and I wrote that it *"needs a container with
more than 16 GB — not more patience"*.

The measurement was real. The conclusion drawn from it was wrong, and it was mine.

## 2. The cause

Stage 2 asked Singular for a **lex** Gröbner basis of `(eqs, T − lin, h)` in a
**12-variable ring over ℚ**. Lex is where rational coefficients explode.
`stdfglm` does not avoid that — FGLM makes the lex basis cheaper to *reach*, it
still has to build it. The in-code comment ("the cost was the ORDERING, not the
system") was right about the ordering and wrong about the remedy.

## 3. The restructure

Nothing downstream needs a lex basis. A component needs each coordinate as a
polynomial in `T`, and where `T` is a primitive element the **shape lemma** gives
`{1, T, …, T^{d−1}}` as a basis of the component ring. So:

1. `std` in **degrevlex** — stage 1 already shows this ordering is affordable;
2. `reduce(T^i, G)` and `reduce(v, G)` — degrevlex normal forms only;
3. one small **exact linear solve** expressing each `v` over that basis.

| `5_2` class 1 | lex route | lex-free route |
|---|---|---|
| deg-4 component | > 717 s, > 7.9 GB, no result | **14.9 s** |
| deg-6 component | never reached | **17.9 s** |
| Singular RSS | 7.9 GB and climbing | **15 MB** (sampled, not peak) |

**Where it is not valid.** The route needs the shape lemma. A non-separating `T`
or a non-reduced component puts a coordinate outside the span — a real fact about
the geometry, detected and **named** (`OUT_OF_SPAN:<var>`), with the historical
lex route as fallback at its own cost. `stage2_route` records which ran.

## 4. A gap the restructure exposed

**Neither route verified its own output.** Both trusted Singular's normal forms
and wrote the point out. Coordinates are now back-substituted into the Ptolemy
equations and reduced mod `h(T)` before a point is recorded
(`equations_verified`). All four components across both manifolds pass.

## 5. `5_2` class 1 — and it is TWO orbits

    eliminant degree 10  (stage 1, 44.5 s, unchanged)
    component A  deg 4   disc  102324706325758224
    component B  deg 6   disc -700971909060291189473042937007563103715437488
    genuine 2, degenerate 0, walled 0, both verified

**The structural finding is the orbit count, not the speed.** L6a4 class 1 has one
genuine component; `5_2` class 1 has **two**. PR #7290 §1 upgrades per-point to
for-all-x by *"four distinct points in a degree-4 zero-dimensional scheme leaves no
room — the orbit IS the whole variety"*. **That argument does not transfer.** On
`5_2` a per-point duality result upgrades only within one orbit, and the two orbits
must be tested separately.

Unlike `m004` (one degenerate component, 6 of 7 coordinates zero), `5_2` has none:
`zeros = 0` on both, `u` a valid cube root of unity on both.

## 6. L6a4 class 2 — a NEGATIVE, and what it rules out

The three recorded class-2 walls (msolve RUR > 3000 s; mod-p GB > 2700 s at
0 bytes; Singular > 5400 s) are all lex/RUR walls, so the restructure was worth
testing against them. It does **not** help.

Measured on the **known-solvable class 1 as control** — the corpus holds its exact
point:

| L6a4 class 1, 27 vars / 33 eqs | result |
|---|---|
| degrevlex `std` over ℚ | **TIMEOUT at 1500 s** |
| degrevlex `std` over `F_32003` | **TIMEOUT at 900 s** |

So the L6a4 bottleneck is the **base Gröbner basis**, not the lex conversion — a
different wall from `5_2`'s, which the restructure does not touch. And because
coefficients cannot grow over a finite field, the mod-p timeout says the wall is
**not coefficient growth**: the modular + CRT family (which `msolve` leans on
internally) will not supply the missing ingredient.

**Both classes are 27 variables / 33 equations.** An earlier note of mine calling
class 2 "a variable-count wall (27 vs 7)" was comparing L6a4 against `m004`, not
class 1 against class 2, and does not explain why one class is solved and the
other is not.

### Scope — (a), not (b)

This is a **scope-limited negative**: *Singular's `std` in degrevlex on the full
27-variable Ptolemy ideal does not complete within 1500 s (ℚ) / 900 s (F_32003) on
this container (4 cores, 16 GB).*

It is **not** a structural exclusion, and the strongest evidence against reading it
as one is in the corpus itself: **the L6a4 class-1 exact point exists**, so some
route produced it. This measurement says the naive degrevlex GB is not that route
and that modular lifting is not the missing piece. It constrains the search; it
does not close it.

Contention caveat, flagged before the run rather than after: the mod-p job ran
beside the ℚ class-2 job on a 4-core box. The conclusion is qualitative — 900 s
against the *seconds* pure coefficient growth predicts — so mild CPU sharing does
not reach it. This session had already misdiagnosed one wall as mathematics when
it was memory contention, which is why the caveat was stated in advance.

## 7. What a next attempt should and should not do

- **Do not** try modular/CRT lifting on L6a4 — measured above, the wall is not
  coefficient growth.
- **Do** find how the existing class-1 point was produced; that route is unknown
  and is the only demonstrated success.
- A smaller generating set, a different variable order, or a different engine
  remain untested and are not excluded by anything here.
