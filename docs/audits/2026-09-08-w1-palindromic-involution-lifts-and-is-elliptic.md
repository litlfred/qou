# The palindromic involution `z ↦ 1/z` lifts to Σ, it is the elliptic involution, and it still cannot be the q-shift

**Date:** 2026-09-08 · **Bean:** `qou-ei4q` · follows `qou-hmrm` (#7114), `qou-lmnq` (#6769), `qou-7fnr` (#6738), `qou-1z28` (#6695)
**Lean:** [`QOU/Mass/PalindromicInvolutionLift.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/PalindromicInvolutionLift.lean) — sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, `#print axioms` on all 16 declarations gives `propext / Classical.choice / Quot.sound` and no `sorryAx`
**Probe:** [`w1_palindromic_involution_lifts_probe.py`](../../computations/probes/w1_palindromic_involution_lifts_probe.py) — 32/32; exact sympy over ℚ for every conclusion-bearing step; no witness by design
**Cited, not re-derived:** the palindromy of `D` and the `w = z + 1/z` reduction ([`2026-05-19-delta-lambda-exploration-findings.md`](2026-05-19-delta-lambda-exploration-findings.md) §H3); the genus of Σ (#7114); the dilation rigidity (#6769)

## What was asked, and why this is not a repeat of #6769

W1 (`qou-d8de`) wants a q-difference prolongation `D_q` on the colour spectral
curve `Σ : P(X,z) = 0`. Route 1 — a q-shift on the base — is closed in all three
charts, the last of them by showing that **no dilation `z ↦ l·z` with `l ≠ 1`
preserves the branch locus**, hence none lifts to Σ.

#7114 named what that argument does *not* reach, verbatim:

> *"#6769 closed dilations `z ↦ λz`; the palindromic symmetry `z ↦ 1/z` is not of
> that form and is not covered by it."*

The branch sextic `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16` is palindromic, so
`ι : z ↦ 1/z` maps the branch locus to itself. It passes the necessary condition
that kills every dilation. So the question was open on its own terms.

**None of this is the corpus discovering that `D` is palindromic.** That has been
known and used since at least 2026-05-19, at the *coefficient* level: the
substitution `w = z + 1/z` collapses `D` to the reciprocal cubic
`16w³ + 24w² − 13w + 2`, whose three roots index the three Galois orbits. What was
never recorded is whether `ι` **lifts to the curve**.

## It does, and the identity is one line

The colour cubic's coefficients are truncated geometric sums,
`a_k = 1 + z + ⋯ + z^{3−k}`, so `a_k(1/z) = z^{k−3} a_k(z)`, and therefore

  **`z³ · P(X/z, 1/z) = P(X, z)`**  for every `z ≠ 0`

(`colorCubic_inv_lift`, sorry-free; probe T3 cancels the difference to `0` in
`ℚ(X,z)`). Hence if `P(X₀,z₀) = 0` with `z₀ ≠ 0` then `P(X₀/z₀, 1/z₀) = 0`: the map

  **`ι̃ : (X, z) ↦ (X/z, 1/z)`**

carries Σ to Σ, covering `ι`, and `ι̃ ∘ ι̃ = id`. **This is the first nontrivial
automorphism of Σ the corpus records.**

## And it is the only inversion that does

`inversion_rigid`: if `z ↦ l/z` sends `D` to a constant multiple of itself then
`l = 1`. The proof is the same two-coefficient elimination as #6769's, one index
apart — the `z⁶` coefficient forces `c = 1`, the `z⁵` coefficient then forces
`l = 1`.

Probe T5 runs the same elimination three ways: on inversions (unique solution
`l = c = 1`), on dilations as a **cross-check against #6769** (same), and on a
deliberately non-palindromic sextic `D + z` as a **control** — which returns *no*
solution. Without that control a singleton answer would not be evidence the
method can also say "none".

## Σ is elliptic and ι̃ is its elliptic involution

Fixed points of `ι̃` need `z = 1/z`, so `z = ±1`, and both fibres are unramified
(`branchSextic_at_one = 200`, `branchSextic_at_neg_one = 4`, both sorry-free):

| over | fibre | `ι̃` acts by | fixed |
|---|---|---|---|
| `z = 1` | `X³+2X²+3X+4`, separable (disc `−200`) | `X ↦ X` | **all 3** |
| `z = −1` | `X(X²+1)` | `X ↦ −X` | **1** (`X = 0`, and `(0,−1) ∈ Σ`) |
| `z = 0`, `z = ∞` | `(X+1)(X²+1)` each | swapped by `ι` | 0 |

So `ι̃` has exactly **4** fixed points. Σ has genus 1 (#7114: degree 3, six simple
finite branch points, unramified at ∞). Riemann–Hurwitz for the degree-2 quotient
gives `2·1 − 2 = 2(2g′ − 2) + 4`, so `g′ = 0`:

**`Σ/ι̃ ≅ P¹`, and `ι̃` is the elliptic (hyperelliptic) involution.** Its four
fixed points are the 2-torsion for a suitable choice of origin.

A pleasing consistency check, and a piece of self-knowledge the corpus lacked:
the base quotient coordinate is `w = z + 1/z`, and probe T7 re-derives
`16w³+24w²−13w+2` as the pushforward of `D`. **The corpus has been computing on
the quotient of Σ by this involution since 2026-05-19 without recording that that
is what the reciprocal cubic is.**

## The prune — scope (b), and it is much wider than #6769

The load-bearing step is structural and exact (probe T9a): the fixed points of a
Möbius map `(az+b)/(cz+d)` solve the quadratic `cz² + (d−a)z − b = 0`, so three
distinct fixed points force `b = 0, c = 0, d = a` — the identity. Hence

  **`Stab(B) ↪ Sym(B) = S₆`**

for the 6-element branch locus `B`, so **every base automorphism preserving `B`
has order at most 6 — finite, always.** This holds for *any* squarefree sextic
branch locus, not just this `D`.

The substrate shift has infinite order: `q₀ = 1.109978582751380807591669 > 1`
(probe T8, proton pin at 60 dps), so `q₀ⁿ ≠ 1` for every `n ≥ 1`.

**Therefore no base automorphism of `P¹` supplies the W1 q-shift** — not merely no
dilation (#6769), and not merely no order-2 map. `dilation_gt_one_not_involutive`
and `qsquare_shift_not_involutive` carry the algebraic core in Lean.

The explicit count, probe T9b: `Stab(B) = {id, ι} ≅ ℤ/2`. This is a **120-dps
numerical** determination by cross-ratio, not an exact one, and it is reported
with its margin — matching gaps `≤ 1.5e-121` against non-matching `≥ 3.6e-2`,
**119 orders of magnitude** apart. The two realised permutations of the roots are
the identity and `(0 1)(2 5)(3 4)`: `ι` acting *freely* on `B`, as it must, since
`D(±1) ≠ 0` puts no root at a fixed point of `ι`. It sharpens the picture; the
prune does not rest on it.

## Scope — what is NOT excluded

Fixed before the argument was run:

- **A q-difference structure not arising from a base automorphism at all.** The
  prune is about `Aut(P¹, B)`. Nothing here constrains an operator built
  otherwise.
- **Route 3** (Ramis–Sauloy–Zhang / Sauloy framework import) — untouched, and now
  better supplied than after #7114: it has a genus *and* a distinguished
  involution with its quotient identified.
- **Anything built from the monodromy representation** rather than from an
  automorphism (the standing scope note of #7114).
- `D_q` is **not constructed.** No fit, nothing wired.

**Not formalised, prose only** — as in #6769 and #7114: the covering-space step
(an automorphism of Σ covering a base automorphism permutes the branch locus), and
the finiteness of `Stab(B)`, whose elementary proof is stated above and measured
in T9a but which would need Möbius machinery Mathlib does not carry in usable
form.

## One error worth recording

`base_involution_ne_id` — "`ι` is not the identity" — is **false in
characteristic 2**: `𝔽₂`'s only unit is `1` and `1⁻¹ = 1`, so `ι` *is* the
identity on `𝔽₂ˣ`. Lean caught it; the lemma now carries `[CharZero K]` and a
docstring saying why. It is a small thing, but it is the kind of thing a probe
over ℚ cannot see and a generic-ring Lean statement can.

## How this composes

| where | closed by |
|---|---|
| route 1, base coordinate `z` | #6695 |
| route 1, ramified local coordinate `t` | #6738 |
| route 1, Σ itself (dilations) | #6769 |
| route 2, `q` = the local fibre-monodromy eigenvalue | #7114 |
| **every base automorphism of `P¹`, dilation or not** | **this tranche** |

The pattern noted in #7114 holds and tightens: each tranche has replaced a
specific negative with a more structural one. This one subsumes #6769's result
rather than sitting beside it — and it is the first to return a **positive**
structural fact about Σ along the way.

## Reproduce

```bash
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/w1_palindromic_involution_lifts_probe.py

# Lean, from SOURCE rather than against the cache snapshot.  ColorSpectralCubicGeometry's
# olean is 2026-08-08 against a 2026-09-04 source, and DilationBranchLocusRigidity merged
# after the cache was taken, so both must be rebuilt before the target means anything:
scripts/lean-shadow-verify.sh \
  content/quantum-observable-universe/lean/QOU/Mass/PalindromicInvolutionLift.lean
```

That script needed a fix to work at all in this container — it was choosing a
2-olean tree over the restored 2442-olean one, because a SessionStart `lake build`
was filling the paper package while it ran. Fixed in this branch; see the commit.
