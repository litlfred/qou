# The sub-affine shape is the only one that could carry a surface term — and it is excluded on the light nuclei. Plus a correction to #6801's own scope note

**Date:** 2026-09-05 · **Beans:** `qou-xpwx` (this), `qou-99rx` (#6801, whose scope note this
corrects), `qou-glji` (#6780), `qou-kqdn` (#6761), `qou-zy94` + `qou-pohg` (the counterexample and
its non-rescue), `qou-rav3`, `qou-brng` · **Arc:** binding law / extensive term ·
**Verdict: a NEGATIVE tranche, and it also corrects a claim I made in the last one.**
**Nothing is wired, nothing is fitted.**

## 1. The correction, first — it is the most consequential thing here

#6801 narrowed its conclusion to *affine* edge sets and reserved **max-contact sphere packing** as
an uncovered candidate, on the ground that its contact numbers "are not known to be affine". **That
was wrong.** The corpus's max-contact edge set is the convex deltahedron and its count is affine —
`computations/gap1_max_contact_a5plus.py:77-79`:

```python
# convex-deltahedron max-contact numbers (= 3A−6 for A≥3; A=2 is the single bond)
def max_contacts(A: int) -> int:
    return 1 if A == 2 else 3 * A - 6
```

Verified in the probe by loading that function out of the corpus with `ast` rather than re-typing
it. So the reserved candidate **does not exist as implemented**, and #6801's conclusion is in fact
**stronger** than it claimed: every coordination edge set derived anywhere on `main` is affine, and
all of them are inside its Part 1 exclusion. Two further corrections to that PR's wording, both the
corpus's own (bean `t7qv`): "not the same family in general" should read **"not the same family
above `A = 9`"** — within `4 ≤ A ≤ 7`, where the corpus uses it, they agree; and `3A − 6` is derived
from **Euler on a 2-sphere**, with the packing reading asserted on top, which is precisely why it
has no interior.

## 2. What this tranche then is: a new object, not a covered candidate

A *true* maximum-contact packing — which the corpus has never used — has a **sub-affine** count
`M(A) = κA − cA^θ`, `0 < θ < 1`. `QOU/Mass/MaxContactHasBulk.lean` (6 declarations, sorry-free,
axiom-clean, `lean`-direct exit 0):

| declaration | statement |
|---|---|
| `subAffine_perNucleon` | `ε·M(A)/A = εκ − εc·A^(θ−1)` — the family at **`p = 1 − θ`**; the per-nucleon exponent is the *complement* of the count's sublinear exponent |
| `subAffine_ne_affine` | `0 < θ < 1` ⇒ `p ≠ 1`, so it escapes #6801's Part 1 — the only shape in this corpus that does |
| `subAffine_hasBulk` | the implied `A_surf ∝ A^θ` passes `HasBulk`, which the chain and the deltahedron each fail |
| `maxContact_exponent_eq_inv_dim` | `θ = (d−1)/d` ⇒ `p = 1/d`; `d = 1` returns `p = 1`, so **the production chain is the family's degenerate surface-free member**, not an outsider |
| `maxContact_d3_eq_semf` / `maxContact_d2_exponent` | `d = 3 → p = 1/3` (the SEMF exponent), `d = 2 → 1/2` |

## 3. The live counterexample — `qou-zy94` excludes this exact family

`qou-zy94` (`QOU/MassTheory/AggregatorFamilyExclusions.lean`, sorry-free) runs a three-point
determinant filter: a two-parameter family `Φ(x) = c·x + a·ψ(x)` with `ψ` **fixed in advance**
leaves one residual over three points, so a non-vanishing `3×3` determinant excludes it for *every*
`(c, a)` at once, nothing fitted. Its conclusion is verbatim: *"So the volume-minus-surface form
`c·x − a·x^(2/3)` is excluded — every `(c, a)`, both grids."*

**`M(A) = κA − cA^(2/3)` with `κ, c` free and `θ` fixed at `2/3` is exactly that family.**

Reconstructed independently in this probe on `A = 2, 3, 4` (most-bound nuclide at each,
`Φ = B_AME`): normalised `det3 = 0.013144` against `zy94`'s **0.01406** — within 7 %, and the
control `ψ = x` returns exactly 0, so the filter detects real structure rather than firing on
everything.

**`qou-pohg` does NOT rescue it.** That bean refutes a *different* proposal — excluding the whole
linear-minus-concave-deficit **class** — and explicitly preserves these: *"the five shape exclusions
are about parameter counting, not about the concave-deficit structure, and they all still stand. Do
not read this as reopening them."* The distinction is that `ψ` is fixed in advance here and free
there. I checked this directly because the two beans' titles appear to contradict each other; they
do not.

**Scope of the exclusion:** **(a)**, not (b). Three light-nucleus points; the semi-empirical formula
is calibrated for `A ≳ 20` and is known to fail on light nuclei independently of this framework;
⁴He is doubly magic. But it is zero-fit and exact, and it is the counterexample this shape must
answer.

## 4. The exponent test on the full chart — discreteness cuts both ways

`p = 1/d` is a **discrete** prediction set, which is what makes it falsifiable where #6761's
continuous amplitude was not. Recomputing #6780's profiled exponent *and* its 1 %-RSS interval for
all five variants, and asking which `1/d` fall inside:

| variant | `p*` | 1 %-RSS interval | `1/d` inside |
|---|---:|---|---|
| full basis, all nuclides | 0.3640 | [0.33147, 0.39692] | **d = 3** |
| A ≥ 16 | 0.5700 | [0.53927, 0.60157] | none |
| A ≥ 40 | 0.5823 | [0.54229, 0.62446] | none |
| no pairing column | 0.4027 | [0.36933, 0.43646] | none |
| N = Z ± 1 only | 0.2292 | [0.16400, 0.29804] | d = 4, 5, 6 |

**3 of 5 admit no `d` at all**; one is too wide to discriminate; **one** picks `d = 3` uniquely.
So the discrete family is *excluded* by more variants than select it. The `d = 3` hit is worth
recording — the nearest neighbours of `1/3` are 0.167 and 0.083 away, far more than the interval's
half-width of 0.033, so landing on it was not free — but it is a consistency result on one analysis
choice, **not a measurement of the nucleus's dimension**.

**The corpus also disagrees with itself about which exponent.** A mirror-split probe measures
`p* = 0.252 ± 0.020`, putting `1/4` at 0.1σ and `1/3` at **4.1σ**; a separate diagnostic lands at
0.33. Say which quantity you are testing; this probe tests the AME per-nucleon fit, a third one.

## 5. What is NOT new, and four standing objections

**`p = 1/3` was already derived** — in my own `CoordinationSurfaceDeficit.perNucleon_surfaceLaw`
(#6761, sorry-free), from `A_surf = c·A^(2/3)`. Since `M = κA − cA^θ` and
`M = kA/2 − (k−k')A_surf/2` are the same equation, `θ = 2/3` and `A_surf ∝ A^(2/3)` are **the same
import**. This file removes no assumption; only which of the two is the primitive changes. An
earlier draft of the Lean claimed otherwise and is corrected.

Four recorded objections to reading the exponent as a dimension, all standing:

1. **The exponent is imported.** *"The ⅓ there is imported from 3-dimensional sphere packing, i.e.
   geometry, which is exactly what this attack was not allowed to use"*; the framework's fixed "3"s
   would source a cube root *"only via an undeclared '3 colours ↔ 3 spatial dimensions'
   identification, which the corpus does not make"*.
2. **`qou-rav3` asks for the argument to be internal** — *"a packing argument inside the
   framework"*. A literature citation is not one.
3. **The ambient geometry is hyperbolic.** A compact *Euclidean* cluster has `A_surf ∝ A^(2/3)`; in
   `H³` an extensive volume gives `R ∼ ½ ln V`, i.e. `ln A`, and using the geometry consistently
   **costs 2.64×** in accuracy. The sharpest structural objection.
4. **The corpus derives three-dimensionality nowhere.**

**Nothing is held.** All four `library/` tiers return only homonyms and bibliography lines for
Harborth / Bezdek / contact number / sphere packing, and `references.ts` has no packing entry (its
only `kissing` match is the surname *Kissinger*). So the sharp literature forms are **deliberately
not cited** and no constant is quoted from them; the Lean uses only the elementary boundary scaling
`A_surf ∼ A^((d−1)/d)`, with `θ` a free parameter of every theorem.

**A gap with no prepared answer, stated plainly:** I searched for a physical-realism objection —
nuclear matter is a liquid, not a close-packed crystal; nucleons are not hard spheres — and found
**none recorded**. That is a statement about the surface I searched, not evidence that no one holds
it. A referee will raise it.

## 6. Verdict

- **Correction (the main deliverable):** #6801's reserved candidate does not exist; every derived
  edge set on `main` is affine, which strengthens #6801.
- **Scope-(a) negative on the new object.** The sub-affine shape is the only one that could carry a
  surface term; it is excluded on the light nuclei by a zero-fit filter, selected by 1 of 5 variants
  on the full chart, and imports its exponent from geometry the corpus objects to four ways.
- **Not a scope-(b) exclusion of the route.** No proved invariant forbids a sub-affine edge set. The
  honest phrasing is *"this construction, alone, imports its exponent and fails the light-nucleus
  filter"* — never *"the corpus has excluded it"*.
- **`qou-brng` unchanged.**

## 7. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The correction to #6801 and the negative both land; the arc is
  where it was, with one fewer live candidate. Cost 0.
- **Re-run `zy94`'s filter on a heavy-nucleus grid.** Its exclusion rests on three light nuclei
  where the SEMF is known to fail. Three points at `A = 50, 120, 200` would say whether the shape
  is excluded where the SEMF actually works. Cost: a probe. Risk: still three points, so still
  scope-(a) — but it would move the exclusion out of the regime everyone already distrusts.
- **Take the hyperbolic objection seriously.** If the ambient geometry is `H³`, the surface law is
  `ln A`, not `A^(2/3)` — a *different* functional form, never tested against the residual. Cost:
  a formalize-first tranche. Risk: the corpus already measured that consistency costs 2.64 %→9.25 %
  on a neighbouring quantity, so the honest expectation is a worse fit and a better-founded one.
- **Do not** pursue the `d = 3` hit as a dimension measurement. Three of five variants exclude the
  whole family.

**Recommendation (judgement):** the third. It is the only option that attacks the framework's own
geometry rather than importing someone else's, it is exactly what `qou-rav3` asks for, and a
negative would be worth more than the `A^(2/3)` positive was — because a fit that is worse and
internally consistent is iterable, and one that is better and imported is not.

## 8. Verification

- `lean`-direct exit 0; 6 declarations axiom-clean `{propext, Classical.choice, Quot.sound}`;
  0 `sorry` (the two `sorry` string matches are the phrase "sorry-free" in prose).
- Probe **17/17**, mpmath 50 dps, no float64. `max_contacts` loaded out of the corpus with `ast`.
- **A probe defect caught and fixed in place:** the `zy94` reconstruction first selected "the first
  three rows with `A ≤ 4`" and got `A = [2, 3, 3]` — a repeated mass number, which degenerates the
  determinant. It now takes the most-bound nuclide at each of `A = 2, 3, 4` and asserts three
  distinct mass numbers.
- `scripts/precision-gates.sh --changed`: recorded in the PR body.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
