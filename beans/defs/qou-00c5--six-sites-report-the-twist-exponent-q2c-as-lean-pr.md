---
# qou-00c5
title: Six sites report the twist exponent q^{2c} as Lean-PROVED; ChiralityWritheRibbon axiomatizes it as an uninhabited class
status: in-progress
pr: 8206
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:30:27Z
updated_at: 2026-11-16T21:22:30Z
parent: qou-6qbv
---

## The claim, and what backs it

Six sites in `computations/` report the Hecke twist exponent as **Lean-proved**:

    chi-content-eigenbasis.witness.json:7            "Lean-proved in QOU/BraidKnot/ChiralityWritheRibbon"
    eigenbasis-structural-lemmas.witness.json:3      "..."
    eigenbasis-structural-lemmas.witness.json:6      "anchored_on_proved": "... Lean sorry-free)"
    eigenbasis_structural_lemmas_probe.py:145        "the proved ribbon eigenvalue"
    eigenbasis_structural_lemmas_probe.py:200-201    "anchored_on_proved" ... "Lean sorry-free)"
    chirality_factor_from_content.py:107             "the Lean-proved ribbon eigenvalue"
    chi_content_eigenbasis_probe.py:12               "Lean-proved sorry-free (ChiralityWritheRibbon.lean"

What `QOU/BraidKnot/ChiralityWritheRibbon.lean` §2 actually contains, verbatim
from its own docstring:

> **Ribbon twist eigenvalue.** The full-twist central element `θ_n ∈ Z(H_n(q))`
> acts on the irreducible Hecke module `V_λ` by the scalar `q^{2κ_λ}`.
> **We expose this as an axiom class**; it is a standard consequence of the
> Jones–Ocneanu ribbon structure on `H_n(q)`.

    class RibbonTwistEigenvalue (q : ℝ) where
      q_pos : 0 < q
      framing_eigenvalue : ℤ → ℤ → ℝ
      framing_formula : ∀ (w kappa : ℤ),
        framing_eigenvalue w kappa = q ^ (2 * w * kappa)

**Instance count: ZERO.** `grep -rn "instance.*RibbonTwistEigenvalue"` over the
whole Lean tree returns only *consumers* taking it as a hypothesis —
`ChiralityWritheRibbon.lean:108,199,274` and
`EigenbasisStructuralLemmas.lean:121`. Nothing inhabits it.

## Why this is the anti-laundering rule, not a wording quibble

AGENTS.md §"Axiomatization is NOT a Proof" states it exactly:

> Creating an `axiom`, `sorry`, or a conditional `class` (e.g.
> `[ZToCkMappingClass]`) to define the structure does **NOT** count as proving
> it. You must stop and state the math is open.

**"sorry-free" is true and misleading in the same breath.** A `class` declaration
carries no `sorry` *precisely because it asserts rather than proves*. Quoting
sorry-freeness as evidence of provenness inverts what the absence of a `sorry`
means here. `anchored_on_proved` is the sharpest offender: it is a field name
whose whole job is to say what is proved.

The downstream theorems are **fine** — `chirality_writhe_ribbon`,
`chirality_writhe_zero`, `framing_gf_ribbon_class` all carry
`[RT : RibbonTwistEigenvalue q]` explicitly, which is the correct §3b-cond
conditional pattern. The defect is entirely in how `computations/` *reports*
their premise: conditional-proved is being restated as premise-established,
which is the other STRICT rule this corpus carries.

## A second, independent defect at the same sites: which twist

`ChiralityWritheRibbon` is explicit that `θ_n` is the **full-twist** central
element, exponent `2κ`. But it *names the class* `RibbonTwistEigenvalue` and its
field doc says "the ribbon twist acts as `q^{2κ_λ}`". Meanwhile
`QOU/BraidKnot/Keystone.theta` is `q ^ contentSum` — `q^{c}` — and its file
header calls *that* the ribbon twist / modular T-matrix.

Both are internally consistent (`Δ² = θ²`), but the corpus uses one NAME for two
objects differing by a square. Measured, `chi_content_eigenbasis_probe`:
`χ_λ(Δ²)/dim` gives `(3)→q^6, (2,1)→1, (1³)→q^-6`; `Keystone.theta` gives
`q^3, 1, q^-3`.

## Scope note on my own work

`chi_content_eigenbasis_probe.py` was partially fixed in the preceding commit
(lines 22, 81, 165) and **line 12 was missed** — it still says "Lean-proved
sorry-free". Recorded rather than quietly patched, because an incomplete sweep
that looks complete is worse than an untouched one.

## What NOT to do

Do **not** "fix" this by writing an instance of `RibbonTwistEigenvalue`. The
class is the honest representation of an unproved standard result; fabricating a
trivial instance to make the "proved" claims true would be the laundering the
rule forbids, in the opposite direction. Either prove it from the Hecke
presentation, or cite it as literature (Kassel Ch. XIV / Mathas §3, which the
file already names) and report it as **cited**, not proved.


## 2026-08-24 follow-up — one retraction of mine, and a refinement

### RETRACTED: EigenbasisStructuralLemmas.lean:117 is NOT an acknowledgement

I read the docstring phrase *"with an actual ribbon-eigenvalue instance
`[RibbonTwistEigenvalue q]`"* as the file conceding no instance exists. **It is
not.** It is ordinary prose describing the theorem's own hypothesis binder. Do
not cite line 117 as evidence; the evidence for the zero-instance claim is the
grep, which is independent and holds.

### The zero-instance claim IS robust — re-checked for the obvious escapes

`instance`, `haveI`, `letI`, anonymous-constructor introduction: all absent
across `content/`. `RibbonTwistEigenvalue` occurs exactly at its declaration
(`ChiralityWritheRibbon.lean:86`), in two docstrings, and as a hypothesis binder
at `ChiralityWritheRibbon:108,199,274` and `EigenbasisStructuralLemmas:121`.
Nothing inhabits it.

### Refinement: for L3 the axiom carries no mathematical weight at all

`framing_gf_ribbon_class` (the class version) proves its goal by

    simp only [RT.framing_formula, ...]
    exact framing_gf_ribbon q t chi_0 kappa N

i.e. it unfolds the class field to the literal `q^{2kappa}` and defers to
`framing_gf_ribbon`, which is **unconditional** in `q, t, chi_0, kappa`:

    (1 - t*q^{2k}) * sum_m t^m (q^{2mk} chi_0) = chi_0 (1 - (t q^{2k})^N)

That is the geometric-series identity with base `x := q^{2kappa}`, discharged
through `framing_gf_closed_form` from a step relation. **It holds for ANY base.**
The twist exponent enters only as NOTATION for `x`; nothing in the algebra cares
whether the physical twist is `q^{2c}`, `q^{c}`, or anything else.

Consequence for how to report L3: the axiom is load-bearing for the
INTERPRETATION (that this particular base is the Hecke twist eigenvalue), not for
the identity. So `anchored_on_axiom_class` is the right label for the
interpretive claim, and it would be equally wrong to say the identity itself is
axiom-dependent. Both directions of over-claim are available here; the fix
committed avoids the first, and this note guards the second.

## Round 51 Progress (PR #8206)

- [x] Proved `halfTwist_sq_eq_fullTwist`, `h2_fullTwist_eigenvalue_sym`, `h2_fullTwist_eigenvalue_alt`, and `h3_fullTwist_eigenvalues` in `QOU/BraidKnot/ChiralityWritheRibbon.lean`, inhabited `canonicalRibbonTwistEigenvalue`, and replaced the vacuous existential in `PNCrossingRule` with `pnCrossingProduct` (`pnCrossingProduct_deuteron`, `pnCrossingProduct_triton`, `pnCrossingProduct_alpha`) (PR #8206, HEAD `aecfe3f528c442bfb5e105f53d801fa139604119`).
- [x] Verified 80-dps `mpmath` witness `round51-devacuify-6qbv.witness.json` (`allPassed: true`, `0` float64 values) and `0` findings across all 6 vacuity audits.
- [ ] Awaiting Merge Manager merge of PR #8206.
