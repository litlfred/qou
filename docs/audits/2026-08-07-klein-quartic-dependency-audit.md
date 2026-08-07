# What depends on the Klein quartic? — dependency audit after the marked-pair exclusion

**Date:** 2026-08-07
**Trigger:** `qou-8p1b` closed with a scope-(b) structural exclusion
(`s4_marked_pair_obstruction.py`): the Bring → Klein degeneration cannot
produce a non-hyperelliptic genus-3 normalization, and the Klein quartic is
non-hyperelliptic. Question raised: does the colour section rest on Klein, and
is this a structural problem?

**Answer in one line:** the colour section does **not** rest on the Klein
quartic. What dies is the claim that colour is derived from the *categorical
substrate*, not any content of the section.

---

## 1. Corpus footprint — "Klein" is four different things

A naive grep for `Klein` hits ~16 files and badly overstates the exposure.
Disambiguated:

| Sense | Files | Bears on the exclusion? |
|---|---|---|
| **Klein quartic** (the genus-3 curve) | `eightfold-way/color-su3-from-g2.md`, `eightfold-way/eightfold-open-problems.md` | **yes — these two only** |
| **Klein chart** (affine chart on Bring) | ~12, across `brings-surface/`, `mass-theory/`, `lifting-and-descent/`, `mass-endomorphism/`, `quantum-observable-universes/` | no — Felix Klein's coordinates, unrelated to the curve |
| **Klein four-group** `V_4` | `braids-and-knots/braid-twist-flip.md`, `rho-s3-holonomy-exposition.md` | no |
| **Klein's icosahedral solution** | `brings-surface/klein-bring-icosahedral-bridge.md` | no — `A_5`, `P(V)/A_5 = S^2(2,3,5)`, the Bring–Jerrard quintic |

The last row is worth calling out: the filename reads like a Bring ↔ Klein-quartic
bridge and is not one. The mass machinery's heavy "Klein" usage is entirely the
*chart*, and is untouched.

`PSL(2,7)` and `Fano` appear in exactly the same two files. Nothing outside the
eightfold chapter references either.

## 2. What the colour section actually derives, and from what

Tracing `prop:color-su3-from-g2`:

| Result | Derived from | Klein involved? |
|---|---|---|
| `PSL(2,7)` as the colour group | Fano incidence structure = octonion multiplication table; `PSL(2,7) = GL(3,F_2) = Aut(Fano)` | no |
| irreps `{1, 3, 3bar, 6, 7, 8}`, colour triplet, gluon octet | the *group*, machine-verified (`psl27_irrep_verification.py`) | no |
| `Im(O) = R (+) C^3` under `SU(3) < G_2` (Günaydin–Gürsey) | octonion algebra | no |
| `Sym^2` gate (the block's Lean ref) | dimension arithmetic | no |
| **Bring → Klein degeneration** | — | **this is the only role** |

Downstream consumers take only the octonionic part:

* `schur-weyl-eightfold.md` cites it for the Günaydin–Gürsey non-self-dual
  triple (construction direction 2 of 2);
* `dictionary-flavor-layer.md` takes `r, g, b <- G_2 stabilizer`.

Neither touches the bridge. **Nothing breaks, no number changes, no proof
depends on it.**

## 3. What is actually lost — and a framing correction

An earlier draft of this analysis said the loss was that colour is no longer
"derived from `q_0`". **That framing was wrong**, and the owner corrected it:
`q_0` is a *locally observed* value and it *varies*. Colour `SU(3)` should not
depend on it, and never should have.

The correct statement: colour should be derived from the **categorical /
fibre-level substrate** — the Bring surface, `A_5`, the Hecke layer — which is
`q`-generic, and which the framework distinguishes from the archimedean
evaluation at the local `q_0` (see the fibre-vs-observable section of
`AGENTS.md`). The Bring surface is exactly such a categorical object, and it is
load-bearing across `brings-surface/`, the magic-numbers work, the `alpha_EM`
period-matrix probe, and the categorical Fourier DFT.

So the Bring → Klein degeneration was the one construction tying colour to the
framework's own categorical substrate. With it excluded, `PSL(2,7)` / Fano /
`G_2` stand as an **external structural input** — mathematically impeccable,
but assumed rather than constructed.

The section's title is already honest about this: "Color SU(3) from
**octonionic stabilization**". It never claimed colour came from `q_0`. The
Bring → Klein material was an *additional* attempt to tie it to the substrate,
and that attempt is what died.

## 4. The sharpest consequence

`prop:color-su3-from-g2` has an **empty `uses[]`**, carrying a note that there
is no `def:octonion-algebra` anywhere in the corpus (bean `qou-8fl1`).

After this exclusion, the colour section rests entirely on an external input
that the corpus never defines. That was already a recorded gap; the exclusion
promotes it from "missing definition" to "the section's sole foundation,
undefined and unconstructed". **`qou-8fl1` is more urgent than its current
framing suggests.**

## 5. Verdict

* **Not** a structural problem for the colour section's content.
* **Is** a structural problem for the claim that colour is substrate-derived.
* Under the three-calibration discipline, importing a symmetry group is not a
  fourth calibration — it is not a numerical fit — but it is an unearned
  structure, and the corpus should say so plainly rather than leave the
  Bring → Klein chain reading as a live route.

Actions taken: the `color-su3-from-g2` abstract now states the octonion algebra
is an external input and that the bridge is refuted; the ledger row is updated;
`qou-8p1e` carries the surviving escapes.

## 6. Where a substrate-native colour construction could still come from

Recorded so the next attempt does not restart from the octonion route. Note the
chapter's own `schur-weyl-eightfold.md` already lists **two** construction
directions; direction 2 (octonionic `G_2`) is the one whose substrate bridge
just died, and direction 1 is untouched.

**The gap, stated precisely.** `RowCapObstruction.lean` already proves the
Weyl-dimension arithmetic — `weylDimAlt N = N.choose 3`,
`no_singlet_of_lt_three`, `singlet_forces_three` — so the *characterisation* of
`N = 3` is done. `a2-from-three-strands.md` explicitly disclaims supplying it
(its `A_2` is the Coxeter group on three *strands*, not the `sl_3` acting on the
fibre). What is missing is upstream of all of that: **the framework's
single-fibre construction supplies `dim V = 2`, and colour needs a
3-dimensional fibre.** Every route below should be judged on whether it
produces that object.

1. **Multi-fibre groupoid (direction 1, already named, untouched).**
   Inequivalent fibre objects whose interaction space is three-dimensional
   (T3b). The `3` is a count of objects rather than the dimension of one
   fibre. This is the most substrate-native candidate on record and it did not
   depend on Klein.
2. **Bruhat / finite-field realisation of the Hecke algebra.** `H_n(q)` is *by
   origin* the Iwahori–Hecke algebra of `GL_n(F_q)`: the convolution algebra on
   Bruhat cells `G = union of BwB`. So this is not an import — it is the
   framework's own core object's defining realisation. At `n = 3, q = 2` the
   flag count is `sum over W of 2^len(w) = 21`, the point set of `PG(2,F_2)` is
   the Fano plane, and `Aut = GL(3,F_2) = PSL(2,7)`, order
   `7 * 6 * 4 = 168`. This would make the colour group **native rather than
   imported**, with its complex `3` / `3bar` irreps supplying the fibre.
   *Open risk, and it is the whole risk:* a principled reason the colour sector
   is the characteristic-2 specialisation. Absent one, picking `q = 2` because
   it yields `168` is numerology. A candidate worth testing is the framework's
   existing bar-involution / parity (mod-2) structure, but that must be
   derived, not asserted. Note also that `F_2^3` is not a `C`-fibre; the bridge
   runs through the complex `3` of `PSL(2,7)`, not through `F_2^3` itself.
3. **"Tetraplectic" / 4-form geometry — assessed, and it does not escape the
   import.** A 4-form stabiliser on `R^8` is `Spin(7)` (the Cayley form), which
   is *more* octonionic than `G_2` (the associative 3-form on `R^7`), not less.
   The other reading, quaternionic / `Sp(n)Sp(1)`, delivers `SU(2)` — the wrong
   group, and the dimension the framework already has. Neither addresses the
   `dim V = 3` gap.
4. **Alternative approaches to the Fano plane** converge on (2). The Fano plane
   is `PG(2,F_2)`; presenting it via octonion multiplication is one
   presentation, and arguably not the primitive one. The Steiner system
   `S(2,3,7)` and the `q = 2` flag geometry are the same object reached
   differently.
