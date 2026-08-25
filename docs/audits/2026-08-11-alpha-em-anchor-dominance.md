# α_EM is ~1.7 ppb, not 0.155% — and the anchor choice is the whole residual

**Date:** 2026-08-11
**Beans:** `qou-4jut` follow-on, under epic `qou-qia8`
**PR:** [#4961](https://github.com/litlfred/qou/pull/4961)
**Lean:** [`FormLadderAnchorDominance.lean`](../../content/quantum-observable-universe/lean/QOU/AlphaEM/FormLadderAnchorDominance.lean)
**Witness:** `computations/alpha-em-form-ladder.witness.json`

## 1. The retraction

Earlier in this session I read `alpha_k_per_force_assembly.py`'s
`inv_alpha_residual_rel ≈ −0.001553` and reported it as the framework's α_EM
accuracy: *"the prediction sits ~1.55×10⁶ ppb (0.155 %) from CODATA."*

That is the residual of the **leading term alone**. The form is

```
1/α  =  q[9]_q[10]_q  +  2g/(4π(g−1))  +  αH(1 − h²α)  +  Δ₂,   g = 4 (Bring genus)
      H = [2]_q/(8π),   h = q − q⁻¹ (Hecke structure constant),
      Δ₂ = uncomputed archimedean two-loop (weight-3; NOT the −h²Hα² above)
```

> **Notation, corrected 2026-08-15.** This document originally wrote the third
> and fourth terms together as a bare `O(a)`. That was retired corpus-wide by
> `2d40f31ad2` (bean `qou-p0u0`) — the symbol was hiding two **derived** terms
> behind a notation that reads as "unspecified", and it obscured the form's most
> important structural feature: **α appears on both sides**, so this is a
> self-consistent relation solved as a *fixed point*, not a series in an
> auxiliary parameter. The sweep updated
> [`FormLadderAnchorDominance.lean`](../../content/quantum-observable-universe/lean/QOU/AlphaEM/FormLadderAnchorDominance.lean)
> but not this audit doc; corrected here. **No number moves** — the ladder
> witness's fixed points already carried these terms (proton `137.035999313169`,
> muon `137.036010116763`, unchanged), so only the notation was stale.
>
> Do not read `h` as the mass-chain `ℏ_q = 1 − q⁻¹`; they differ by ~2.11×.

and `alpha_k_per_force_assembly` computes only `q[9]_q[10]_q = 136.8232…`. The
assembled ladder is in a different producer:

| anchor | fixed point | residual |
|---|---:|---:|
| **proton** | 137.035999313169 | **1.6723 ppb** |
| muon | 137.036010116763 | 80.5100 ppb |

So the figure I quoted was wrong by about **six orders of magnitude**, and it
was wrong in the direction that makes the framework look worse. The author
caught it from memory ("at one point I thought we had α_EM better").

`leading_term_residual_dwarfs_full_form` records the size of the error: the
leading-term residual exceeds the full form's proton-anchored residual by more
than `5·10⁵×`.

## 2. What that reverses

I had also reported, from the `alpha-k` q₀ front, that the muon→proton pin shift
of **−78.96 ppb** on `1/α_EM` was *"~20 000× smaller than the standing gap, i.e.
bookkeeping."* Against the real form:

```
muon residual    80.51 ppb
proton residual   1.67 ppb
difference       78.84 ppb      ← vs the −78.96 ppb measured independently
```

The pin shift **is** essentially the entire α_EM residual — not noise inside a
large gap, but the difference between an 80 ppb result and a 1.7 ppb one. It is
~47× *larger* than the proton-anchored residual, the opposite of negligible.
`anchor_gap_dominates_proton_residual` proves the `> 40×` bound; a negative
control at `> 60×` correctly fails, so `40` is a real bound rather than slack.

That the two figures (78.84 from the ladder witness, 78.96 from the independent
`alpha-k` re-run) agree to ~0.1 ppb is a cross-check on both.

## 3. What is proved

`FormLadderAnchorDominance.lean` — 14 declarations, sorry-free, `lean`-direct
exit 0, `#print axioms` clean, three negative controls rejected.

### Part 1 — the ladder's integers need no minimal-strand convention

The witness calls its integers *"structurally derived (Bring genus 4; crossing
numbers of `T(2,9)`, `T(3,5)`)"*. The property that makes that phrase safe is
that the torus crossing number `c(T(p,q)) = min(p(q−1), q(p−1))` is **symmetric**
under `p ↔ q` (`crossingNumberTorus_symm`), so `T(p,q) ≅ T(q,p)` gets one value
with no choice of presentation. Both carriers are computed and both are
transposition-stable: `c(T(2,9)) = c(T(9,2)) = 9`, `c(T(3,5)) = c(T(5,3)) = 10`.

**This is precisely what the neighbouring `δ_q` writhe rule fails to do**, and it
ties the two threads of this PR together. `w(T(m,p)) = (m−1)p` is *not*
symmetric — `writheTorus_not_symm` gives `w(T(2,3)) = 3 ≠ 4 = w(T(3,2))` for the
trefoil either way — which is exactly why
[`torus-knot-delta-q-writhe.md`](../../content/quantum-observable-universe/mass-theory/torus-knot-delta-q-writhe.md)
needed the minimal-strand guard `m ≤ p` and why
`rosso_jones_three_strand_delta_q.py` now raises on a swapped pair.
`crossing_number_needs_no_convention` states the contrast as one proposition.

### Part 2 — anchor dominance

| theorem | content |
|---|---|
| `anchor_gap_eq_prediction_gap` | the reference value **cancels** from the difference of residuals, so "which anchor" is independent of the CODATA vintage — not idle, since the ladder witness scores against `137.035999084` while `alpha-k-per-force-assembly` carries `137.035999177` |
| `no_anchor_blind_affine_correction_closes_gap` | any further term that does not itself depend on the anchor acts as one affine `x ↦ s·x + c`; for `s ≠ 0` the anchors stay distinct. So the spread cannot be absorbed by a better *anchor-blind* remainder — **only an anchor-dependent ingredient can move it** |

> **What that leaves, now that the remainder is written out (2026-08-15).** With
> the form stated explicitly, the theorem's scope is sharper than when it was
> written against a bare `O(a)`. The `αH(1 − h²α)` term **is** anchor-dependent —
> `H = [2]_q/(8π)` and `h = q − q⁻¹` are both functions of `q`, and `q₀` differs
> between the pins — so it is *not* excluded by the theorem. But it is also
> already **in** the ladder: the fixed points above were computed with it, and the
> spread is still 78.84 ppb. So the one anchor-dependent term the form currently
> names does not close the gap, and the only remaining candidate inside this form
> is `Δ₂`.
>
> That is a narrowing, not a route: `Δ₂` is uncomputed, and nothing here says it
> is the right size or sign. Claiming otherwise would be exactly the
> fit-shaped reasoning this document is a retraction of.
| `degenerate_correction_is_vacuous` | the one escape, `s = 0`, does equalise them — by discarding the prediction. Named so the exclusion is not over-claimed |
| `anchor_gap_dominates_proton_residual` | gap `> 40×` the proton-anchored residual |
| `leading_term_residual_dwarfs_full_form` | leading term alone misses by `> 5·10⁵×` the full form's residual |

### The genus term, division-free

`IsGenusTerm g p T := 4·p·(g−1)·T = 2·g` is stated **cleared of denominators**,
so it holds over an arbitrary `CommRing` with no `p ≠ 0`, no `g − 1 ≠ 0`, and
**no characteristic hypothesis** — a quotient form would force `4 ≠ 0` and
silently exclude characteristic 2. At `g = 4` it reads `12·p·T = 8`
(`isGenusTerm_four_iff`). The closed form enters as `3·p·T = 2` and implies the
relation unconditionally (`isGenusTerm_four_of_three_mul`); the converse needs
`4` cancellable and carries that hypothesis in its name
(`three_mul_of_isGenusTerm_four_of_four_cancellable`), per the `_of_` convention.

## 4. Honest scope

**Scope-(a), and none of this makes α_EM correct.** The witness's own caveats
stand and are *not* discharged:

- **(A) Conjectural** — three unproved classes in the derivation. The integers
  are structurally derived (Bring genus 4; crossing numbers of `T(2,9)`,
  `T(3,5)`), and no coefficient is fitted.
- **(B) Anchor-dependent** — which is Part 2's *subject*, not its refutation.
- **(C)** The witness's "~80 ppb = ~530× σ_a, not at target" is written against
  the **muon** anchor. Under the 2026-08-07 proton default the figure is
  1.67 ppb, so that caveat is stale in the same way the `c_knot` prose was.

**On (B), stated plainly because it cuts both ways.** This is *not*
anchor-shopping: the proton pin was chosen for q₀ on precision grounds
(0.06 ppb vs 22 ppb) on 2026-05-28, independently of and prior to α_EM. α_EM
landing at 1.7 ppb under an independently-motivated pin is therefore a genuine
conditional success — and it means α_EM is now a **second** strong witness for
the proton pin, which should be said out loud rather than left implicit. But
`no_anchor_blind_affine_correction_closes_gap` also says the μ–p spread in α_EM
cannot be argued away by improving the truncation; it is the μ–p substrate
tension showing up in a second observable.

Nothing here is wired to production, and no number in the corpus changes.
