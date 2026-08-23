# The Lean convention-C surface, measured

**Date:** 2026-08-19
**Bean:** `qou-um5h`
**Companion:** [`2026-08-19-bar-involution-is-isospin-conjugation.md` §4g](2026-08-19-bar-involution-is-isospin-conjugation.md)

The convention-C detector
([`scripts/convention-c-producer-audit.py`](../../scripts/convention-c-producer-audit.py))
walks `rglob("*.py")` and parses Python ASTs; the detector before it walked
`content/**` only. **Neither has ever read a `.lean` file.** So the standing
instruction to treat the remaining C surface as *unmeasured rather than clear*
applies to the Lean tree in full. This is that measurement.

## The headline: 97 hits, 5 sites

| | count |
|---|---:|
| raw hits on the C shape (`√q + 1/√q`, either spelling) | **97** |
| files containing at least one | **52** |
| of those hits, lines that are code rather than prose | **11** |
| **genuine convention-C `z`-definitions** | **5** |

Counting hits over-reports by ~19×; counting files by ~10×. **The Lean C surface
is overwhelmingly documentation** — 86 of 97 hits are docstrings and comments
describing the parameter, not defining it.

## The five real sites

| file | line | form |
|---|---|---|
| `Braiding/HnMarkovTrace.lean` | 82 | instance field `z := 1/(√q + 1/√q)`, in a docstring calling it *"the canonical Wenzl Markov parameter"* |
| `BraidKnot/JonesNuclearQuotient.lean` | 70 | `noncomputable def markovZ q := 1/(√q + 1/√q)` |
| `BraidKnot/QBetaPerBlockChiClosedForms.lean` | 1037 | `noncomputable def markov_parameter q := √q/(1+q)` — the *other* C spelling; the theorem at 1051 proves the two spellings agree |
| `BraidKnot/QBetaQStarClosedFormExclusion.lean` | 78 | `let z := 1/(√q + 1/√q)`, feeding `alpha := (z-1)·h/2` |
| `BraidKnot/volume_perturbation.lean` | 64 | class field `z_def : z = 1/(√q + 1/√q)` |

Two observations on these. `QBetaPerBlockChiClosedForms` carries **both** C
spellings plus a proof they coincide — a self-consistent C site, and a reminder
that a detector keyed on one spelling would miss the other. And
`QBetaQStarClosedFormExclusion`'s `z` feeds `α = (z−1)h/2`, so that `α` — the
same object this session identified as `(ε − tr_M)/2` — is **C-frame**.

## The false-positive classes, which are the point

A naive grep counts all of these as violations. None is one.

**1. The Jones loop factor `δ`.** `BraidKnot/JHopfQOneProvenance.lean:69`:

```lean
/-- **The Jones loop factor** `δ(q) = −(√q + 1/√q)` — the value of a single
    unknotted loop, and the base of the `(δ)^{n−1}` prefactor in Jones's
    normalization of the Markov trace. -/
noncomputable def loopValue (q : ℝ) : ℝ := -(Real.sqrt q + 1 / Real.sqrt q)
```

`δ` and `z` share the `√q + 1/√q` shape and are **different objects**. `δ` is the
loop value; `z` is the Markov parameter. Flagging `loopValue` as a convention
violation would be a false positive, and *fixing* it would be a defect.

**2. Notational identities.** `MathlibExt.lean:197` proves
`q^(1/2) + q^(-1/2) = √q + 1/√q` — a statement about `Real.rpow` versus
`Real.sqrt`, convention-neutral.

**3. Side conditions.** `hden`, `hsum`, `hsum_pos` are positivity obligations
discharged next to a definition already counted. Same site, extra hits.

This is the `.lean` analogue of the standing warning that *a grep for the bad
name does not imply a bad number* — here inverted: a grep for the bad **shape**
does not imply the bad **object**.

## What this does and does not license

- It does **not** authorise a migration. Five sites is small, but
  `HnMarkovTrace`'s C-frame Hopf closed form
  `(q^{5/2} − q^{1/2} + q² + q)/(q² + q)` is a *proved* result whose
  re-derivation under D is its own piece of work, and `QBetaQStarClosedForm‑
  Exclusion`'s `α` is load-bearing for the `q*` exclusion argument.
- It does record that **`MarkovTraceTower` should not be used as the base for
  new D-frame work** — which is why
  [`QOU/MathlibExt/MarkovBondRule.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/MarkovBondRule.lean)
  is built on `MarkovNormalisation` instead.
- If a Lean C-detector is ever written, it must separate `δ` from `z` and must
  match **both** C spellings. Keying on the shape alone reproduces the 19×
  over-count above.

## Method, so the numbers can be rechecked

Fixed-string `grep -rn` over `content/quantum-observable-universe/lean/QOU`
for `Real.sqrt q + 1 / Real.sqrt q`, `√q + 1/√q`, `√q+1/√q`,
`q^{1/2} + q^{-1/2}`, `q^{1/2}+q^{-1/2}`, plus `√q/(q+1)` / `Real.sqrt q / (q + 1)`
for the second spelling (4 further hits). Code-vs-prose split by presence of
`:=`, `let `, `def `, `have `, or `: ℝ` on the line. The five sites were then
read individually — the classification is by inspection, not by pattern.

## Follow-through on one site: the `q*` exclusion is safe, the landmark is not

`QBetaQStarClosedFormExclusion`'s C-frame `α` was the one site that looked like
it might endanger a live argument. Checked:

**The exclusion argument is convention-independent.** `qstarRootStrictMonoInAnchor`
and `qstarRootUniqueInAnchor` are stated about an *abstract* `Φ : ℝ → ℝ` with a
`StrictMonoOn` hypothesis; they never mention `qstarShape`, `z` or `α`. And the
numerical premise survives: `Φ'(q*) = −3.606` under D against `−3.631` under C —
nonzero and same sign either way. `qstarShape` is a C-frame `def` that nothing in
the file consumes.

**The landmark itself moves, a lot.** `α = (z−1)h/2` shifts 23% between
conventions (`−0.052336` → `−0.040487`), and rooting `Φ(q) = Q_codata/m_e`:

| | `q*` | position |
|---|---|---|
| C | 1.10997859340 | **inside** the `[proton, muon]` anchor interval |
| D | 1.11023370740 | **19,921 anchor-gaps outside** it |

The anchor interval is `1.281e-8` wide; D displaces `q*` by `2.55e-4`.

So [`rem-qstar-decay-sector-q0.md`](../../content/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md)'s
sentence *"It lies ≈ 80.3% of the way from the proton anchor toward the muon
anchor"* is **convention-C-frame**. Under D, `q*` is not between the anchors at
all. Tracked as `qou-iax1`.

The block's *skeptical conclusion* is unaffected and arguably strengthened: it
argues the 80.3% is "a reading of `Vol(4₁)`'s own value" — every constant in a
window of width `0.0491` places a zero between the anchors — so the position was
never evidence. Under D it is not even in the window.

**Caveat on my own number.** My `Φ` is a reconstruction from the Lean `def`, not
the block's producer; under C it lands `3.35e-10` from the block's stated `q*`,
which is 2.9% of the anchor gap. **So my C-frame percentage is not reliable and
must not be quoted against the block's 80.3%.** The D result is insensitive to
that — a 20,000-gap displacement survives any plausible constant-vintage
difference.

## What this audit did not do

- It did **not** scan `.ts` manifests or `.md` content blocks; this is the Lean
  tree only.
- It did **not** verify that the five sites are *wrong* — they are C, and C was
  excised as the canonical convention on 2026-08-15, but each may be locally
  correct for a C-frame result it is stating.
- It did **not** write a detector.
