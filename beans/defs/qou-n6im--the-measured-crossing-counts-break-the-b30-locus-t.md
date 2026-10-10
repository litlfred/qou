---
# qou-n6im
title: The measured crossing counts break the b3=0 locus, then miss on sign by 8.11x
status: scrapped
type: task
priority: normal
created_at: 2026-08-31T03:07:18Z
updated_at: 2026-08-31T03:18:32Z
---

Runs `qou-6vu3`'s acceptance test against the corpus's **measured** crossing
counts, with zero freedom, and turns the outcome into a one-dimensional target.

## Setup — no fit anywhere

`QOU.MassTheory.CrossingCountAffine` records, from
`level3_em_channel_parity_probe.py` across **12 nuclei to `A = 39`**:

    n₊ = 5A − 1 + 2Z,    n₋ = 5A − 1 − 2Z

so the count multiplicity is `μ(A) = ½(n₊+n₋) = 5A − 1`, charge-free — and that
is *exactly* the multiplicity `BrunnianBindingChannel.countChannel` carries. Not a
guess, not a fit: it is what the canonical atomic braids measure.

## It passes the test, then fails on sign

| | |
|---|---|
| `μ(2), μ(3), μ(4)` | 9, 14, 19 |
| acceptance test `μ_t = 3·μ_p`? | **14 ≠ 27 — breaks the locus, passes** |
| model `b₃/b₂` | **−13/9 = −1.4444** |
| measured `b₃/b₂` | **+0.6411239316** |

So it escapes the pair-local degeneracy the Hopf/Borromean carriers sat on — the
first carrier in this arc to do so — and lands on the wrong side.

## The constraint that makes this useful

For **any** affine `μ(A) = αA + β` the cumulant is exact,
`b₃ = μ(3) − 3μ(2) = −(3α + 2β)`, so with `b₂ = 2α + β > 0`:

    b₃ > 0  ⟺  2β < −3α    ⟺    −2α < β < −³⁄₂α

and — the load-bearing part — **`b₃/b₂` depends only on `r = β/α`**, not on the
slope (`b3_ratio_depends_only_on_intercept_ratio`, checked in the probe by
rescaling the slope 10× with `r` fixed). So the search is **one-dimensional**:

| | `r = β/α` |
|---|---|
| `b₃ > 0` window | `(−2, −1.5)` |
| measured model | **−0.2** (outside) |
| required | **−1.6214** (inside) |
| off by | **8.11×** |

**The gap is not the functional form.** Affine works — the required `r` sits
inside the window and `window_is_inhabited` exhibits `(α,β) = (5,−8)` with
`b₃ > 0`. What fails is one ratio, and its required value is now known to six
figures.

## The honest limit, which is the interesting part

**`b₄` is not reproduced either** — model `17/9 = 1.889` against measured
`4.155` — and an affine `μ` has only *one* ratio, so tuning `r` to match `b₃`
does **not** free a second parameter for `b₄`. That is the right way to use this:
`r` is fixed by `b₃`, and **`b₄` then becomes a genuine prediction**, not a
second fit. Anyone matching `b₃` with an affine count owes that check.

## Artifacts

* `QOU/Mass/AffineCountMultiplicityWindow.lean` — 11 declarations, sorry-free,
  `lean`-direct exit 0, zero `sorryAx`.
* `computations/probes/affine_count_intercept_window_probe.py` — 5/5, exact
  `Fraction` arithmetic, zero free parameters.

## Scope — (a), and it excludes nothing structural

Neither the count channel nor affine models are excluded. `brunnian_binding_survives`
is untouched. What is measured is that the corpus's own crossing counts miss the
required intercept ratio by 8.11×.

**Caveat:** `μ = 5A − 1` is charge-free, so it cannot distinguish ³H from ³He —
consistent with using the isospin-averaged `B̄(3)` here, but it also means the
model says nothing about the mirror splitting. And the 12-nucleus measurement
behind `(5, −1)` is the sibling's, not re-derived here; if those counts are
revised the verdict moves.

## Related

`qou-brng` (parent), `qou-6vu3` (the acceptance test), `qou-vudb`/`qou-toul`
(the crossing-count measurement), `qou-w6vh`.


---
**🛑 RETRACTED, same session, before merge — the identification was wrong.**

This bean claimed `μ(A) = 5A − 1` from `QOU.MassTheory.CrossingCountAffine` is
*"exactly the multiplicity `BrunnianBindingChannel.countChannel` carries"*, and
built the `−13/9` result and the 8.11× intercept gap on it. **The identification
is wrong and everything downstream of it is withdrawn.** The PR was still
unmerged, so nothing reached `main`.

**Two independent reasons, either fatal.**

1. **Total vs inter-component.** `countChannel`'s `n₊, n₋` are *inter-component*
   crossings — `minimal_brunnian_bond` fixes them from *"the pairwise crossing
   pattern inside `L6a4`"*. The `5A − 1` count runs over **every** letter of the
   `A`-nucleon word, self-crossings included. In the construction the
   inter-nucleon letters are only the `A − 1` chain interfaces (`atom_braid_word_3A`
   appends one per adjacent pair, gated by `include_inter`); everything else is
   the per-nucleon words.
2. **They are not crossing numbers at all.** `atom_braid_word_3A`'s own docstring:
   *"this does NOT return a braid word … the returned object lies in `H_n(q)` and
   is NOT in the image of `ρ : B_n → H_n(q)` … there is NO SINGLE LINK behind it …
   **so NO TOPOLOGICAL quantity may be read off it — not a volume, not a crossing
   number, not a genus**."* `n₊, n₋` count Hecke **letter types** by their `d`
   coefficient; `tr_M` there is a weighted sum of `2^{2A+1}` link invariants (32
   for `²H`), not one link's.

**What survives.** The general affine result is untouched and stays: `b₃ =
−(3α + 2β)` exactly, `b₃ > 0 ⟺ −2α < β < −³⁄₂α`, and the ratio depends only on
`r = β/α`. The Lean keeps those and is **instantiated at nothing**. The
non-vacuity witness `(5, −8)` is a bare example, not a carrier.

**What does not survive:** `−13/9`, the `r = −0.2`, the 8.11× gap, "the first
carrier in this arc to break the locus", and the whole probe — deleted, not
re-scoped, because every number in it flowed from the bad identification.

**`CrossingCountAffine` is NOT impugned.** It feeds these counts to the *linear*
functional `E = n₊q − n₋q⁻¹`, which linearity transports legitimately. Reading a
*link crossing number* off them is the forbidden step, and that step was mine.
The counts themselves are sound: `n₊ + n₋ = 10A − 2` and `n₊ − n₋ = 4Z` check
exactly against the docstring's `²H` figures (23 letters, 11 `σ`, 7 `σ⁻¹`, 5
averaged `= 2A + 1`).

**The lesson, which is the durable part.** Two objects named `n₊`/`n₋`, both with
a `(n₊+n₋)/2` "count multiplicity", one a link crossing count and one a Hecke
letter-type count. Same name, same formula, different object — the arity/identity
conflation AGENTS.md's `da-arity-conflation` criterion names. I checked that the
formula matched and not that the *object* did.

**Consequence for `qou-brng`, and it is not small.** The natural move — read
crossing numbers off the canonical atom word and feed them to the binding channel
— is **blocked at the source**, not merely wrong-valued. Any derivation of carrier
crossing numbers must come from an object that *has* a link behind it. The
`A − 1` chain interfaces are the only inter-component structure the construction
carries, and a chain is what `QOU.MassTheory.ChainBondOrderDependence` already
flags as arrangement-dependent.
