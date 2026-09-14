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

## 5a. Only orbit 0 was addressable, and the producer said so while doing it

`ptolemy_exact_point.py` printed the NOTE above — *"the variety is NOT a single
Galois orbit, so a per-point result does not upgrade to 'for all x' for free"* —
and then, three lines later, wrote `to_point_json(genuine[0])` into one file. So
the one inference the NOTE forbids was the only one a consumer could make: orbit 1
had no artifact at all. Fixed in `674c2b6307`; each genuine orbit now gets
`<stem>-orbit<i>-ptolemy-in-K.json` and a `provenance.orbit_index`. Orbit 0 keeps
the unsuffixed filename, so every committed artifact is byte-unmoved.

## 5b. The duality test could not run on `5_2` — the bottleneck was `Aut(K/Q)`

`ptolemy_duality_generic.py` found the automorphisms of `K` by solving
`f(g(t)) ≡ 0 (mod f)` for the `deg` coefficients of `g`. That is `deg` polynomial
equations of degree `deg` in `deg` unknowns — a Gröbner basis computation inside
`sp.solve`. Two runs on the degree-4 orbit were killed at 25 and 40 minutes with
**no output past the header line**. The duality test proper is a nullspace over `K`
on a 36-column matrix and was never reached.

A root of `f` lies in `K` iff it is a root of a **linear factor of `f` over `K`**.
Factoring `f` over `K = ℚ(α)` and reading the linear factors off is the same set by
a univariate factorisation (`350e00d152`):

| | `[K:ℚ]` | solve route | factor route |
|---|---|---|---|
| `m004-c1` | 2 | 0.16 s | **0.025 s** |
| `5_2-c1-orbit0` | 4 | no answer in 40 min | **0.082 s** |
| `5_2-c1-orbit1` | 6 | never attempted | **0.316 s** |

**This is a change of algorithm, not of definition**, and it is evidenced four ways
— because a route that silently drops one automorphism reports `K/ℚ` as non-normal
when it is normal, which is a wrong claim about the manifold rather than a
performance regression:

1. **Route agreement** on `m004` (degree 2, where the solve route terminates): both
   return exactly `{t, −t−11}`.
2. **Calibration.** `m004-c1-duality-generic.json` is unchanged in every
   mathematical field — same automorphisms, same untwisted/twisted dimensions
   (2/2), same λ class, same verdict. The diff is two added fields and the order of
   the `rows` dict.
3. **Group axioms**, now `assert`ed on every run by `_check_group` using only
   polynomial arithmetic mod `f`: `f(g) ≡ 0`, identity present, closed under
   composition, every element invertible. This trusts neither route.
4. **Element orders**, now computed and recorded: `|Aut|` alone does not name the
   group, and `[1,2,2,2]` (Klein four) and `[1,2,4,4]` (cyclic `C₄`) have different
   subgroup lattices.

## 5c. The duality result, PER ORBIT — they are not pooled

**Orbit 0**, `[K:ℚ] = 4`, `|Aut(K/ℚ)| = 4` ⇒ `K/ℚ` **normal**, element orders
`[1,2,2,2]` ⇒ `Gal(K/ℚ) ≅ V₄`, the Klein four-group.

| σ | untwisted | twisted | λ |
|---|---|---|---|
| `t ↦ t` (control) | none(0) | none(0) | other |
| `t ↦ (961t³ − 16089t² + 459794t + 1449695)/274813` | none(0) | none(0) | other |
| `t ↦ (−64t³ + 3192t² − 129473t + 1285094)/88561` | none(0) | none(0) | other |
| `t ↦ (−81t³ + 657t² − 35362t + 6247)/29197` | **FOUND(4)** | **FOUND(4)** | all 1 |

**This is the first run in which the test SELECTS.** `m004` and L6a4 class 1 both
have `|Aut| = 2`, so their single non-identity candidate succeeding is compatible
with *"any non-identity σ works"*. Here there are three involutions and **exactly
one** carries an intertwiner; the other two fail untwisted *and* twisted. The
identity control fails, as it must. Schur holds: every nonzero nullspace has
dimension `[K:ℚ] = 4`.

**Orbit 1**, `[K:ℚ] = 6`, `|Aut(K/ℚ)| = 2 < 6` ⇒ `K/ℚ` **not normal**, orders
`[1,2]`. The unique non-identity σ carries an untwisted intertwiner, `FOUND(6)`,
λ ≡ 1; the identity control fails; Schur holds at dimension 6.

So untwisted `GL(3,K)` duality holds on **both** orbits of `5_2` class 1 — but as
two separate statements. Neither upgrades to the other, and §5 is why: they are
distinct components, so no Galois orbit connects them.

**Two things this does not establish.** Orbit 1's `K/ℚ` is not normal, so σ
generates a `C₂` that is *not* a quotient of a Galois group acting on all six
roots — the transport argument available on orbit 0 is not available here, even
though the intertwiner exists. And the selection in orbit 0 says σ is distinguished
among the three involutions; it does not say *which* invariant distinguishes it.
That is the open question this measurement hands to `qou-qjhc`.

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
