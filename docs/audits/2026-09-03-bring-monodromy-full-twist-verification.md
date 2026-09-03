# The Bring colour-monodromy braid lift, verified by a different route — full twist and SL(2,ℤ)

*2026-09-03 · bean `qou-xhih` (Front 1 of `qou-icj2`) · branch
`claude/8-fold-way-qou-derivation-qj9uzv` (PR #6458).*

**Probe:** [`computations/probes/bring_monodromy_full_twist_probe.py`](../../computations/probes/bring_monodromy_full_twist_probe.py)
· witness `computations/probes/bring-monodromy-full-twist-probe.witness.json`
· Lean [`QOU/Eightfold/BorromeanBraidPure.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/BorromeanBraidPure.lean).

**Verifies (does not re-derive):** PR #6449, branch
`claude/colour-sign-line-canonical-2026-09-03`, bean `qou-dg07` —
`computations/probes/bring_monodromy_braid_lift_probe.py` (the six lifts),
`computations/probes/colour_mu_bar_monodromy_probe.py` (image = `B₃`, `μ̄₁₂₃ = −1`),
and `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md` §10–§11.

## 1. What was at stake

The bean asked for the `S₃ → B₃` lift of the six local monodromies of the Bring
colour cubic `X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)` and the subgroup they
generate. By the time this session started, #6449 had done it: six half-twists
of exponent sum `−1`, reducing (as words) to `σ₁⁻¹` (loops 0, 3),
`σ₂σ₁⁻¹σ₂⁻¹` (loops 1, 2), `σ₂σ₁σ₂⁻¹σ₁⁻¹σ₂⁻¹` (loop 4), `σ₁⁻¹σ₂⁻¹σ₁` (loop 5),
with `σ₁ = g₀⁻¹` and `σ₂⁻¹ = g₀⁻¹g₁g₀`, hence image `= B₃`, hence the
Borromean braid `(σ₁σ₂⁻¹)³` is in the image with `μ̄₁₂₃ = −1`.

Per the parallel-work policy, this session's job became: confirm those words
by a route sharing as little as possible with theirs, and add a check that
constrains the six words *jointly* — which neither of their probes has.

## 2. What is different in this probe

| | #6449 (`bring_monodromy_braid_lift_probe`) | this probe |
|---|---|---|
| crossing reader | roots projected on the **real axis** | roots projected on a **generic direction** `e^{iθ}`, `θ = 37/100` rad (exact) |
| base point | `2 + i/2` | `5/2 + 3i/4` |
| degenerate-projection defect (their §10.1 item 2) | fixed by moving the base point off ℝ | **cannot occur**: for a conjugate root pair the `u`-coordinates differ by `2 Im(w) sin θ` |
| per-loop guards | one adjacent swap / step, positive real gap, cycle type vs continuation | one adjacent swap / step, positive `u`-gap, step `< ½` root separation, loop **partition** by `S₃` image vs both earlier probes |
| joint check on the six words | none | **full-twist identity** (§4) |
| generation | word search (`σ₁`, `σ₂⁻¹` as words in the lifts) | **surjection onto `SL(2,ℤ)` + `Δ² ∈` image** (§5) |

Sign convention (stated because it fixes every sign below): strands ordered by
`u = Re(w e^{−iθ})`; an adjacent exchange is `σᵢ⁺¹` if the strand that was on
the left has the larger `v = Im(w e^{−iθ})` (passes in front), `σᵢ⁻¹` otherwise.
It is #6449's convention with the axis rotated, so the words are comparable.
Under it a counter-clockwise half-turn of two roots is `σ⁻¹`.

Runtime **146 s** at 50 dps (first full run; the second run with the added
`(ab)³` check is the committed witness). No `float(`; the witness carries
strings, integers and booleans only.

## 3. The six lifts, and agreement with #6449 up to conjugacy

```
loop  bp                          my word            e-sum   S₃ image
0     (−0.9748, −0.2230 i)        σ₁ σ₂⁻¹ σ₁⁻¹        −1      (2 1 0)
1     (−0.9748, +0.2230 i)        σ₁⁻¹                −1      (1 0 2)
2     ( 0.1058, −0.9371 i)        σ₁⁻¹                −1      (1 0 2)
3     ( 0.1058, +0.9371 i)        σ₂⁻¹ σ₁⁻¹ σ₂        −1      (2 1 0)
4     ( 0.1190, −1.0536 i)        σ₁ σ₂⁻¹ σ₁⁻¹        −1      (2 1 0)
5     ( 0.1190, +1.0536 i)        σ₂⁻¹ σ₁⁻¹ σ₂⁻¹ σ₁ σ₂  −1      (1 0 2)
```

Guards: max adjacent swaps per step `1`; smallest `u`-gap at a recorded
crossing `1.08e−5` (positive; the trap #6449 hit reads `0.0` here); worst
step-over-separation `0.018`. All six are half-twists of exponent sum `−1`,
as a positively oriented loop around a simple branch point must be under this
convention. The partition of the six loops by `S₃` image — `{0,3,4} | {1,2,5}`
— is a relabelling invariant and agrees with both #6449 and
`bring_cubic_monodromy_probe`'s A7.

**Comparison with #6449's words.** A different base point and projection
change each lift by conjugation, so literal equality is not expected and does
not hold for any loop. Conjugacy was decided in two layers:

- **Necessary:** equal exponent sum, equal `S₃` cycle type, equal
  characteristic polynomial of the reduced Burau matrix over `ℚ(t)` — all six
  give `(λ − 1)(λt + 1)/t`, the polynomial of `σ₁⁻¹`. Stated as necessary
  only: equal Burau characteristic polynomial does not imply conjugacy.
- **Sufficient, and found:** an explicit conjugator `c` with `c·w·c⁻¹ = s`,
  checked by equality of Artin automorphisms of `F₃` (faithful). For all six
  loops `c = σ₂`. That *proves* per-loop conjugacy.

So the two probes **agree**: same six conjugacy classes, loop for loop.

### 3.1 One correction to #6449's wording — "four distinct words" are TWO elements

§11.1 of the #6449 audit says the six lifts "reduce to only **four distinct
braid words**". As *reduced words* that is true; as *elements of `B₃`* it is
not. Measured here by the Artin action:

- #6449 loop 4, `σ₂σ₁σ₂⁻¹σ₁⁻¹σ₂⁻¹`, **equals** `σ₁⁻¹` in `B₃`
  (`σ₂σ₁σ₂⁻¹ = σ₁⁻¹σ₂σ₁`, then cancel);
- #6449 loop 5, `σ₁⁻¹σ₂⁻¹σ₁`, **equals** `σ₂σ₁⁻¹σ₂⁻¹` (invert
  `σ₂σ₁σ₂⁻¹ = σ₁⁻¹σ₂σ₁`).

Their six lifts are therefore **two** elements, `σ₁⁻¹` on loops `{0,3,4}` and
`σ₂σ₁⁻¹σ₂⁻¹` on loops `{1,2,5}` — exactly the `S₃` partition, lifted. Mine are
likewise two: `a = σ₁⁻¹` on `{1,2,5}` and `b = σ₁σ₂⁻¹σ₁⁻¹ = σ₂⁻¹σ₁⁻¹σ₂` on
`{0,3,4}` (the labels are swapped relative to theirs because the base
configuration is read in a different frame). Nothing in #6449's generation
argument depends on the count — `g₀` and `g₁` are one representative of each
class — so its conclusion stands; only the sentence needs "words" → "elements",
and "four" → "two".

## 4. The new check: the six lifts multiply to the full twist

The six lassos, multiplied in the angular order seen from the base point, are
homotopic to a large circle enclosing all six branch points. The circle's
braid was computed **independently** by direct transport around
`|z − z₀| = 4` (8000 samples; the same guards). Two things are forced a priori:
by A5 of `bring_cubic_monodromy_probe` (unramified at `∞`) its permutation is
trivial, and since at large `|z|` the roots are `z·(roots of Y³+Y²+Y+1)`, one
turn of `z` turns all three roots once, so the braid is a full twist
`Δ^{±2}`, `Δ² = (σ₁σ₂)³`.

Measured: the large-circle word has length 6, trivial permutation, exponent
sum `−6`, and **equals `Δ⁻²`** (`k = −1`, the sign the convention predicts).

The angular order of the lassos from `z₀` is `[5, 3, 1, 0, 2, 4]`; the product
of my six words in that order **equals the large-circle braid** (Artin action)
and is `Δ⁻²`. Because the `S₃` classes alternate along that order
(`a b a b a b`), this is the identity

```
(a b)³ = Δ⁻²        a = σ₁⁻¹ (loops 1,2,5),   b = σ₁σ₂⁻¹σ₁⁻¹ (loops 0,3,4)
```

— the `B₃` lift of `rem:holonomy-trefoil`'s `(H₁H₂)³ = id`, which holds only in
`S₃`. In `B₃` the cube of the product of the two distinct local monodromies is
the (negative) full twist, the central element, **not** the identity.

**How discriminating the check is.** Exactly **72 of the 720** orderings of
the six words give `Δ⁻²` — `2·(3!)² = 72`, i.e. precisely the orderings that
interleave the two classes. Any single wrong word among the six would break
the identity; the reverse angular order also passes (it is an interleaving),
so this test does not by itself pin the orientation of the lasso product — the
sign of `k` does that, and it matches the convention.

**Applied to #6449's words** in the angular order from *their* base point
`2 + i/2` (which is the same `[5, 3, 1, 0, 2, 4]`): the product is `Δ⁻²` (same
`k = −1`), and again 72 of 720 orderings pass. **Their six words pass a joint
check they were never subjected to.**

## 5. Generation, by `SL(2,ℤ)` rather than word search

Reduced Burau at `t = −1`: `σ₁ ↦ A = [[1,1],[0,1]]`, `σ₂ ↦ B = [[1,0],[−1,1]]`.
Checked in code: `ABA = BAB`, `det = 1`, `(ABA)² = −I` so `ρ(Δ²) = −I`,
`ρ(Δ⁴) = I`; and the integer matrices agree with the symbolic Burau of `Δ²`
at `t = −1`. This is the standard surjection `ρ : B₃ → SL(2,ℤ)`.

BFS over the images of the six lifts and their inverses finds

```
T = g₁⁻¹                (depth 1)
S = g₁ g₁ g₀            (depth 3)
−I = g₀ g₀ g₁ g₀ g₀ g₁  (depth 6)
```

each product re-evaluated and asserted. `S, T` generate `SL(2,ℤ)`, so
`ρ(H) = SL(2,ℤ)` for `H = ⟨lifts⟩`. With `Δ⁻² ∈ H` from §4 (so `Δ² ∈ H`) and the
**imported** fact `ker ρ = ⟨Δ⁴⟩` (Magnus 1934; Milnor, *Introduction to
Algebraic K-theory* §10 — not verified here):

> for `g ∈ B₃` pick `h ∈ H` with `ρ(h) = ρ(g)`; then `g h⁻¹ ∈ ⟨Δ⁴⟩ ⊆ ⟨Δ²⟩ ⊆ H`,
> so `g ∈ H`. Hence **`H = B₃`**.

This reproduces #6449's conclusion without using their generator words; the
only shared input is the geometry of the cubic. What it does *not* do: it is
not a proof from scratch — it rests on `ker ρ = ⟨Δ⁴⟩`, which is cited, and on
the six numerically read words, which are guarded and now jointly constrained.

## 6. Lean (sorry-free, `lean`-direct exit 0)

[`QOU/Eightfold/BorromeanBraidPure.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/BorromeanBraidPure.lean)
formalises words in the signed Artin generators of `B₃`, the rewriting relation
`BraidStep` (free cancellation and `σ₁σ₂σ₁ = σ₂σ₁σ₂` in any context) and its
equivalence closure `BraidEq`, and proves:

| declaration | statement |
|---|---|
| `permOfWord_braidEq`, `expSum_braidEq` | the `S₃`-image and the exponent sum are `BraidEq`-invariant — i.e. genuine `B₃` invariants |
| `borromean_perm_eq_one` | the `S₃`-image of `(σ₁σ₂⁻¹)³` is `1` (`decide`) |
| `borromean_equiv_perm_eq_one` | hence every word equal to it in `B₃` has trivial image: **the Borromean braid is pure** |
| `borromean_expSum` | its exponent sum is `0` |
| `expSum_conj_gen` | any conjugate `c g c⁻¹` of a single letter has exponent sum `±1` |
| `borromean_not_halfTwist` | **no half-twist is equal in `B₃` to the Borromean braid** |
| `perm_s1_s2_ne`, `perm_braid_relation` | the two transpositions do not commute, and the braid relation holds in `S₃` — the invariance is not vacuous |

`#print axioms` on all nine: `propext`, `Quot.sound`, and (for the `Perm`
statements) `Classical.choice`; no `sorryAx`. Imports are the specific modules
`Mathlib.GroupTheory.Perm.Basic`, `Mathlib.Data.Fintype.Basic`,
`Mathlib.Logic.Relation`, `Mathlib.Algebra.BigOperators.Group.List.Basic`.
Verified with the restored-olean `lean`-direct recipe (no `lake build`; the
tree carries `.lake/RESTORED-NO-TRACES`).

What the Lean is honest about: `B₃` is not constructed as a group; the results
are about words modulo the presentation, which is the same information. The six
lifts being half-twists is the probe's numerical result, consumed not proved.

## 7. Task C — does it lift to two nucleons (six strands)?

**Scope-(a) negative: there is no object to lift.** Greps over `content/` and
`computations/` for a six-sheeted / degree-6 colour cover find none. What the
corpus *does* have at six strands is Hecke-algebra material, not a fibration:

- `computations/probes/block_transposition_lift_probe.py` (PR #6415, bean
  `qou-brng`): the two-nucleon exchange as the block-swap braid
  `(σ₃σ₂σ₁)(σ₄σ₃σ₂)(σ₅σ₄σ₃) ∈ B₆` acting on the 11 Wedderburn blocks of `H₆`,
  with the trace-blind blocks `(4,1,1)`, `(3,2,1)`, `(3,1,1,1)`;
- `computations/probes/lifting_the_isospin_grading_to_six_strands_probe.py`
  (same exchange operator, spectrum `±q^k`);
- the `B₆` mentions in `hoefsmit-ew-cell-content.lean` and
  `electroweak-triplet-far-commuting-minimal.md` are the far-commuting triple
  `(σ₁⁴, σ₃⁶, σ₅⁸)`, unrelated to a cover.

These are *elements and representations* of `B₆`; a monodromy lift needs a
branched cover of `ℙ¹` whose six sheets are the six colour tubes, and the
corpus does not carry one. One structural remark, stated as a remark and not
measured: any two-nucleon fibre built from **two copies of the same cubic over
the same base** (disjoint union, six sheets) has monodromy in the
block-diagonal `S₃ × S₃`, lifting into `B₃ × B₃ ⊂ B₆`, which does **not**
contain the block-swap braid the `H₆` probes use as the exchange operator. So
if a tower rung exists it needs a genuinely irreducible degree-6 cover, which
would have to be constructed first. Not attempted; not in scope of `qou-xhih`.

## 8. What this closes, and what it does not

**Closes / corroborates.**
- #6449's six loop lifts: confirmed loop-by-loop up to conjugacy with explicit
  conjugators, by a reader immune to the defect their first version had.
- #6449's "image is `B₃`": reproduced by an independent argument
  (`SL(2,ℤ)` surjection + `Δ² ∈` image).
- New joint identity: the six lifts multiply, in angular order, to `Δ⁻²`,
  equal to the independently transported large circle — `(ab)³ = Δ⁻²`, the
  `B₃` lift of the holonomy-trefoil cube. Their words pass it too.
- Sorry-free Lean that the Borromean braid is pure and is not a half-twist.

**Corrects (wording only).** "Four distinct words" in #6449 §11.1 are two
distinct elements of `B₃` (§3.1). The conclusion is unaffected.

**Does not touch.**
- **Statement B's premise is unchanged**: that the baryon state occupies the
  sign isotype `Alt³` is still an input. This audit is entirely about the
  monodromy of the colour cover, not about which isotype the physical state
  sits in.
- `μ̄` of any closure — #6449's `colour_mu_bar_monodromy_probe` is the carrier.
- The A6 identification of the sheets with the colour tubes — consumed.
- `ker(B₃ → SL(2,ℤ)) = ⟨Δ⁴⟩` — imported, cited, not proved.

**Scope.** Positive result. The exact parts (conjugacy, `SL(2,ℤ)` generation,
the Lean) are unconditional; the six words are numerical and remain
conditional on the guarded transport — now with the full-twist identity as a
second, joint, guard. The Task C negative is scope-(a): "no six-sheeted cover
exists in the corpus", not "none can exist".
