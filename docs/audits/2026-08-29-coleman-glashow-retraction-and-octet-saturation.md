# RETRACTED: Coleman–Glashow was not a new result on this branch — and the ansatz saturates the octet

**Date:** 2026-08-29
**Bean:** `qou-bn8e`
**Branch:** `claude/standard-panel-qou-derivation-ixuolx` (PR #5744)
**Lean:** [`QOU/MassTheory/ChargeQuadraticSumRule.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ChargeQuadraticSumRule.lean) — sorry-free, `lean`-direct exit 0, axioms `[propext, Classical.choice, Quot.sound]`
**Probe:** [`coleman_glashow_charge_quadratic_probe.py`](../../computations/probes/coleman_glashow_charge_quadratic_probe.py)

---

## What was claimed, and what is wrong with it

On 2026-08-29 this branch committed (`e8ae6a68e4`) the claim that the
Coleman–Glashow relation *"falls out parameter-free"* from a quadratic-in-charge
electromagnetic term, described it as **"the first parameter-free consequence the
EM sector yields on this branch"**, and called it **"a genuine prediction rather
than a postdiction"** whose measured residual `0.0643 MeV` (`0.80 %` of the
largest term, `0.29σ`) made the EM sector *over-determined and falsifiable*.

Two things are wrong, and the corpus already contained both refutations.

### 1. It is not new

[`QOU/Eightfold/ColemanGlashowIdentity.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/ColemanGlashowIdentity.lean)
proves the relation sorry-free (`coleman_glashow_identity`) over any commutative
ring, from a **strictly weaker** premise: the EM self-energy is constant on a
U-spin multiplet, with *three* free shifts `a, b, c` at charge `+1, 0, −1`. The
quadratic-charge ansatz is a two-parameter **specialisation** of that family, so
CG follows a fortiori and this branch added nothing to it.

The block [`eightfold-way/u-spin-coleman-glashow.md`](../../content/quantum-observable-universe/eightfold-way/u-spin-coleman-glashow.md)
already records the *same measured residual* — `−0.064 MeV`, `0.8 %` of the
largest splitting — that this branch reported as its own measurement.

### 2. It is not evidence, and the corpus says so in as many words

The same block states the epistemics directly:

> **Reproducing Coleman–Glashow would therefore be no evidence for this
> framework, or for any other.**

The branch's framing — "over-determined and falsifiable" — contradicts a
corpus block that exists to argue the opposite. `cg_cannot_discriminate` is the
machine-checked form of it.

## How the check failed

This is the **seventh** object-grep failure of this arc, and the most avoidable:
the corpus file is named `u-spin-coleman-glashow.md`, i.e. the search term is
*in the filename*. The grep that was run matched the **topic** ("isospin EM
splitting", "charge structure") and never the **object** ("Coleman", "Glashow").
`scripts/prior-art-probe.py` — written on this same branch precisely for this
failure mode — was not run for this claim.

The repo's own rule states it: *grep the claim SHAPE, not only the topic*. The
shape here was a named relation, and a named relation has a name to grep for.

## What survives, and one thing that is genuinely new (and negative)

The arithmetic was never in question; only the significance was. What stands:

* **Two invariants, not one.** Symmetric quadratics in three charges span a
  2-dimensional space — self `Σqᵢ²` and interaction `Σᵢ<ⱼqᵢqⱼ`, with `Q²` not
  independent. The corpus's `NeutronProtonEMSign` uses the interaction term
  alone, i.e. sets `A = 0`. That is the standard renormalisation convention; it
  is **not derived and not flagged** in that block.
* **The nucleon datum is degenerate.** `p` and `n` differ by `1/3` in *both*
  invariants, so `E(p) − E(n) = (A + B)/3` and the nucleon splitting constrains
  only the sum. The corpus's sign result survives and generalises: it needs only
  `A + B > 0`, weaker than `B > 0`.

And the new result, which is a **negative** one and is this file's own:

> **The ansatz saturates the octet, so it predicts nothing there.**
> The octet's observable EM content is 2-dimensional (three splittings, one CG
> relation among them; an overall shift of `a, b, c` is unobservable). In terms
> of the couplings those observables are `a − b = (A+B)/3` and
> `b − c = (A−2B)/3`, a linear map of determinant **−1/3 ≠ 0** — a *bijection*.
> Hence `octet_em_pattern_surjective` (exhibiting `A = 2u+v`, `B = u−v`): **every**
> octet EM pattern is reproduced by some `(A, B)`.

Two corollaries, both sharpening `qou-bn8e` rather than closing it:

1. **CG could not have failed here**, so its holding is no evidence for the
   ansatz. A test that no member of a class can fail discriminates nothing.
2. **The octet *fits* `A` and `B` rather than constraining them.** The
   bijection is the obstruction, not a route. Any derivation of the couplings
   must come from data the octet does not contain — which is why `qou-bn8e`
   stays open, and why adding the Σ triplet does not close it.

## Scope

Scope-(a) throughout. Nothing is wired to production. The retraction concerns
the significance claimed for an identity, not the identity, and not the corpus's
own CG treatment, which was correct before this branch touched the subject.
