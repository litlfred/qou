# T₃ wired into meson operator-selection — charm/strange degeneracy resolved, tube geometry still open

**Date:** 2026-08-02
**Bean:** `qou-2udt` (child of the convergence epic `qou-20sx`)
**PR:** #4625
**Branch:** `claude/t3-meson-operator-selection-2026-08-02`
**Inputs:** #4618 (`WeakIsospinT3Grading.lean`, T₃ derivation, bean `qou-tdrd`) ·
#4614 (`MesonFluxTubeReduction.lean` + `2026-08-02-meson-fluxtube-junction-reduction.md`, bean `qou-qpj9`)
**Lean:** `content/quantum-observable-universe/lean/QOU/ParticleInteractions/MesonOperatorSelectionT3.lean`
— sorry-free, `lean`-direct **exit 0** (5.4 s, 6990 restored oleans).

## The gate this addresses

PR #4614 proved (`winding_content_not_injective`, sorry-free) that the meson
operator-selection input — the unsigned generation winding `n ∈ {3,5,7}` — is a
**symmetric** function of the two quark windings and therefore cannot separate
up-type charm from down-type strange (both `n = 5`). Under the meson
crossing-count rule `n₁ + n₂`, the open-charm D̄⁰ meson `c̄u = {5,3}` **collides**
with the kaon `K⁻ = ūs = {3,5}` (both 8 crossings). The `gg → c̄c`
operator-selection thus had no charm-specific channel; the D-meson braid was
under-determined. The audit named the precise missing datum: a **weak-isospin
`T₃` grading orthogonal to `n`**.

PR #4618 then **derived** that grading as the *sign of the signed writhe*:
`κ = sign(κ)·|κ|`, magnitude `|κ| = n` (generation), sign `∈ {+,−}` (weak type),
`T₃ = sign(κ)/2 ∈ {±½}`; charm `= σ₁^{+5}` (`T₃ = +½`), strange `= σ₁^{−5}`
(`T₃ = −½`). Gell-Mann–Nishijima `Q = T₃ + Y/2` was proved sorry-free as a
derive-then-check.

## What this PR establishes

The operator-selection input is refined from the **unsigned** winding multiset
to the **signed writhe** multiset. The refinement is not a fit: an antiquark is
the orientation reversal (mirror) of the quark braid, and orientation reversal
negates the writhe, so an antiquark contributes `−κ`. This is a topological
fact, applied uniformly.

### Result 1 — the selection is no longer degenerate (real win)

| Lean lemma | Content |
|---|---|
| `signedWrithe_injective` | `signedWrithe` separates all six quarks (the `(n, sign)` label is complete). |
| `selectionInput_injective` | the refined demand input `(genWinding, sign) = (n, 2T₃)` is injective. |
| `charmBlock_ne_strangeBlock` | charm `(5,+1)` and strange `(5,−1)` are **distinctly selectable** — the datum the unsigned winding lacked. |
| `unsigned_D_kaon_collide` | reproduces the #4614 blocker: D̄⁰ `{5,3}` ≡ kaon `{3,5}` (unsigned). |
| `unsignedContent_not_injective` | reproduces `winding_content_not_injective`. |
| `graded_D_kaon_distinct` | **the signed content separates D̄⁰ from the kaon** (`c̄` = −5 vs `ū` = −3). |
| `gradedContent_injective_on_dictionary` | the signed content is injective on the four-meson dictionary `{π, K, η/φ, D}`. |

So on the exact domain where the blocker lived, the operator-selection input is
now injective. The named degeneracy is resolved.

### Result 2 — the D-meson braid is NOT canonically fixed a priori (honest negative)

Two distinct gaps remain, both formalized:

1. **Residual content collision (needs a third grade or the ordered bar).**
   Admitting the neutral kaon `K⁰ = d̄s`, the signed *multiset* collides D̄⁰
   `{−5,+3}` with K⁰ `{+3,−5}` (`graded_D_K0_collide`,
   `gradedContentExt_not_injective`). Reason: `(n,T₃)` grades by
   *(generation, weak-sign)*, and the charm-antiquark `c̄` (`κ = −5`) shares that
   grade with the strange quark `s` (`κ = −5`), while `u` (`κ = +3`) shares it
   with `d̄` (`κ = +3`). It is broken only by keeping the quark/antiquark
   orientation (the "bar") as *ordered* data (`orderedContent_injective`) — itself
   topological, but a datum the audit's *symmetric-multiset* content model does
   not carry — or by a further flavour grading (charm number `C` vs strangeness
   `S`), a *third* index beyond `(n, T₃)`.

2. **Tube geometry untouched (Obstruction A / `qou-qpj9`).** Even a fully-fixed
   graded content only pins the *carrier quantum numbers* — the `Vol = 0` torus
   data (`MesonFluxTubeReduction.twoStrand_winding_bijective`). The *hyperbolic*
   braid word at `H₃(q)` whose closure volume yields the **mass** is a separate,
   still-open construction. Packaged as the content-bearing conjecture class
   `CanonicalHyperbolicMesonBraid` with **no instance** (§3b-tax honest open
   state). `mass_from_graded_content_cannot_separate` proves the point sharply:
   any mass map that is a *function of the graded content* assigns D̄⁰ and K⁰ the
   *same* mass, so the mass datum is provably **not** a function of `(n,T₃)`.

### Anti-fit note

Because no braid is canonically fixed a priori, the joint D-mass check
(1864.84 / 1869.66 MeV) was **not** run — no braid was hand-picked to hit 1865.
`T₃` resolves the *selection*, not the *geometry*.

## Bottom line

- **Selection degeneracy: RESOLVED.** The `(n, T₃)`-graded input is injective on
  the quarks and on the four-meson dictionary; charm is distinctly selectable
  from strange. This is a permanent, sorry-free contribution.
- **D-meson braid: STILL under-determined.** The residual `D̄⁰ ≡ K⁰` collision
  needs the ordered bar / a third flavour grade, and — the load-bearing gap —
  the hyperbolic tube geometry (`qou-qpj9`) is untouched. The mass is provably
  not a function of `(n, T₃)`.

## Next honest steps

- The **flux-tube reduction** (`qou-qpj9`): a canonical hyperbolic braid word at
  `H₃(q)` from the graded content (an instance of `CanonicalHyperbolicMesonBraid`).
- The **third flavour grade** (charm number vs strangeness) if the
  symmetric-multiset content model is kept; otherwise wire the ordered-bar
  orientation into the operator-selection input.
