# Screening generation bridges in one number: the bend annihilates both fitting knobs

**Date:** 2026-08-07
**Branch:** `claude/agent-pr-4690-stall-s9f5rt` (PR #4704)
**Bean:** `qou-htk4` (successor to `qou-lsp9`)
**Status:** screening tool + scope-(b) exclusion of the exactly-geometric
class. Sorry-free Lean, `lean`-direct exit 0.

## The problem with how `qou-lsp9` was working

`qou-lsp9` closed candidate bridges serially — first the unweighted `net`,
then every positive linear readout of `H₂(q)`. That does not scale, and it
has a worse property: a candidate `f` inside

```
  m_w = C · g^w · f(w)^p
```

carries **three** free parameters against **two** observed lepton ratios.
Something can always be made to fit. Refuting candidates one at a time is
therefore both slow and epistemically weak — each refutation is a statement
about one point in a space where fitting is always available.

## The fix: screen with a quantity the free parameters cannot touch

For a tower sampled at three consecutive generation windings, define the
**bend**

```
  bend(x, w) = x(w+2)² / ( x(w) · x(w+4) ).
```

The whole point is one identity (`bend_of_scaled_geometric_pow`):

```
  m_w = C · g^w · f(w)^p     ⟹     bend(m) = bend(f)^p
```

**`C` and `g` cancel exactly.** The overall mass scale and the
per-generation geometric factor — precisely the two knobs that make every
candidate look adjustable — drop out identically. A candidate is then
screened by **one number against one free parameter** instead of three.

The measured target is parameter-free:

```
  bend(m) = m_μ² / (m_e · m_τ) = 12.29517…
```

## Two lemmas that do most of the work

**`bend_of_geometric`** — a readout exactly geometric in the winding has
`bend = 1`. Composed with the transport law
(`geometric_readout_forces_unit_bend`), such a readout forces `bend(m) = 1`
**for every `C`, `g` and `p` simultaneously**. Against an observed 12.295
that is an outright exclusion of the entire three-parameter class — no
fine-tuning argument, no discussion of how large `p` would have to be.

**`bend_of_linear`** — a readout linear in the winding has
`bend = (w+2)²/(w(w+4))`, which at the lepton windings `(3,5,7)` is
`25/21 ≈ 1.190`, independent of its constant.

Between them these cover the two families every classical `T(2,n)`
invariant falls into.

## The screen, applied

65 dps, proton pin. All candidates parameter-free and standard.

| candidate | bend | `p` required |
|---|---|---|
| **observed leptons** | **12.29517** | — |
| net `= a_n + b_n` | 1.003767 | 667.3 |
| Markov trace `tr_M` | 1.039393 | 64.9 |
| `b_n` alone | 0.967075 | −74.9 |
| `a_n` alone | 1.314789 | 9.17 |
| determinant `= n` | 1.190476 | 14.39 |
| crossing number `= n` | 1.190476 | 14.39 |
| genus `= (n−1)/2` | 1.333333 | **8.72** |
| \|signature\| `= n−1` | 1.333333 | **8.72** |
| Alexander at `q₀` | 0.989888 | −246.9 |
| Alexander at `q₀²` | 0.967075 | −74.9 |
| braid index `= 2` | **1** | none works |
| bridge number `= 2` | **1** | none works |
| control: exactly `qⁿ` | **1** | none works |

A viable parameter-free bridge would need `bend = 12.295` at `p = 1`,
`3.506` at `p = 2`, or `2.308` at `p = 3`. The best any standard invariant
of the lepton's own knot manages is `4/3`, needing `p = 8.72`.

## A bonus that removes an objection before it is raised

The Jones polynomial's normalisation carries a writhe prefactor, and one
could object that the verdict depends on which normalisation is used. It
does not: the prefactor is of the form `a·r^w`, exactly the shape the bend
annihilates. Verified numerically rather than asserted — multiplying `tr_M`
by an arbitrary `a·r^w` moves the bend by **1.8e-71**.

So "which Jones normalisation" cannot change any row of the table.

## Honest scope

- **Scope-(b), hard** — the exactly-geometric class. Rests on the proved
  identity `bend(m) = bend(f)^p` together with `bend(geometric) = 1`; it
  excludes every `C`, `g`, `p` at once. This is a genuine structural
  exclusion, not a failed search.
- **Screen, not refutation** — for the remaining rows. "Bend near 1 needs a
  large exponent, hence a fit rather than a derivation" is a *plausibility
  judgement*, and is labelled as one both here and in the witness. `p = 8.72`
  is not proved impossible; it is merely not a natural exponent.
- **Out of scope entirely** — non-multiplicative bridges. An additive
  interface term is not of the form `C g^w f^p`, so this tool says nothing
  about it. It remains open under `qou-htk4`.

## Where this points

Every quantity screened is an invariant of the lepton's **own** knot, and
none supplies the bend. That is consistent with — and independent evidence
for — the structural diagnosis already in the corpus: `T(2,n)` are
Seifert-fibred with `Vol = 0`, while the framework's working muon mass is
`m_e · Vol(4₁)/ℏ_q²`, built from the hyperbolic **Higgs** knot. The
generation dependence, if it exists, is carried by the *coupling* to an
object outside the lepton's knot, not by any readout of the knot itself.

`qou-htk4`'s live direction — a linking/satellite quantity coupling
`T(2,n)` to `4₁` — is therefore not just unrefuted but is where the
screening says to look. Two concrete usability notes for whoever takes it:

1. Any candidate can now be tested by computing three numbers and one
   ratio, before any fitting machinery is built.
2. A candidate that only reaches `bend ≈ 1` is dead on arrival regardless
   of how good its other properties look.

## Artifacts

- **Lean (sorry-free, `lean`-direct exit 0):**
  [`lepton_tower_bend_invariant.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/lepton_tower_bend_invariant.lean)
  — `bend`, `bend_of_scaled_geometric_pow`, `bend_of_geometric`,
  `geometric_readout_forces_unit_bend`, `bend_of_linear`. Pure `[Field K]`
  algebra — no ordering, no archimedean construct, so §7c-generic.
- **Probe:** [`lepton_tower_bend_screening.py`](../../computations/lepton_tower_bend_screening.py)
  → `lepton-tower-bend-screening.witness.json`.
