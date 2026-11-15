# Results: which quark tails does γγ + reading 3 admit?

Pre-registration: [`preregistration.md`](preregistration.md), commit `5ad34aec2`, pushed before
computing. Producer `gg_quark_tail_probe.py`, witness `gg-quark-tail.witness.json`. Exact sympy over
ℚ(q), proton pin as an exact rational, convention D, H₃. Formulas are imported unchanged from
`gg_gluon_segment_probe.py`. Run time about 40 s.

One code fix after the first run, before any result was read: the bar-closure helper misparsed
letter names and crashed. The verdicts were not computed in that run.

## Calibration: 5/5 pass

- C1: census tails with gluon σ₀² give χ_(2,1) = −0.2805933509 (p) and −0.3719563247 (n).
- C2: census tails with gluon V give +0.2170281485 (p) and +0.4294149854 (n).
- C3: the seminormal 2×2 matrices agree with the trace formula on 20 random words (seed 0).

## Pre-registered readouts

| gluon | tails passing reading 3 at q₀ | census TAIL_p, TAIL_n | closed under φ (σ₀↔σ₁) | closed under letter bar |
|---|---|---|---|---|
| V = σ₀σ₁⁻¹ (γγ) | **112 / 216** | both pass | no | no |
| σ₀² (current element) | **108 / 216** | both fail | no | no |

**Outcome (ii).** Reading 3 does not fix the tail: about half of the alphabet passes, under either
gluon. Neither symmetry maps survivors to survivors, so the survivor set is not a single orbit of
an obvious symmetry.

## Observation, not pre-registered: the generator placement nearly decides the verdict

The 216 tails split into 8 generator placements (which generator each of the three letters sits
on) × 27 parity choices (σ, σ⁻¹ or the average on each). Counting passes per placement:

| placement | gluon V: pass / 27 | gluon σ₀²: pass / 27 |
|---|---|---|
| 000 | 1 | 23 |
| 001 | **27** | 7 |
| 010 | 15 | 4 |
| 011 | 1 | 26 |
| 100 | 23 | 7 |
| 101 | 14 | 4 |
| 110 | 5 | **27** |
| 111 | 26 | 10 |

- With the γγ gluon V, **exactly one placement passes for every parity choice: 001**. That is the
  builder's placement, the one both census tails use. Placements 000 and 011 are rejected for
  26 of 27 parity choices.
- With σ₀², the one fully admitted placement is 110 instead, and 001 is mostly rejected. This is
  why the census tails pass with V and fail with σ₀².
- The parity letters (the flavour content) are what reading 3 does *not* see on 001: all 27
  parity choices pass there. So, on this alphabet, γγ + reading 3 fixes the placement and leaves
  the flavour sign map free. This matches #7781's finding that no γγ rule names a flavour.

This table was read off the witness after the run. It was not a pre-registered criterion, and
"passes for every parity choice" is not an owner rule. It is recorded as a pattern for the owner
to judge.

## What this leaves open

- **Flavour** (which parities are u and which are d) is untouched by the test on placement 001.
  It needs a flavour-to-line rule. The n = 4 corner doublet is not that rule (Stream 11).
- **Proton vs neutron:** reading 3 does not read flavour, so no survivor is labelled p or n.
- **The gluon choice** (V vs σ₀²) is still the owner's open decision (`qou-ggls`). The placement
  pattern depends on it.

Scope (a): this six-letter alphabet, H₃, the proton pin. Other tower levels are not computed here;
on three-strand families they coincide with H₃ (#7702 × #7733).

## Addendum (2026-11-15, not pre-registered): step-3 tail rules with the k = 1 gluon

Producer `step3_rules_with_gluon.py`, exact sympy over ℚ(q), proton pin. Calibration: without the gluon, it reproduces the step-3 table (main `b611c74d815`) exactly. Rules: R1 = (σ₀, σ₁⁻¹), R2 = (σ₀⁻¹, σ₁), R4 = the bar-fixed average on both generators. Element: CORE·T·V. χ_(3) > 0 throughout, so χ_(2,1) decides reading 3.

| rule | passes at q₀, no gluon | passes at q₀, with V |
|---|---|---|
| R1 | 000, 011, 101, 110 | **001, 010, 100, 111** |
| R2 | 001, 010, 100, 111 | 000, 001, 101, 110 |
| R4 | 001, 010, 100, 111 | 001, 010, 100, 111 |

- Every rule still passes on exactly 4 of 8 placements, so appending the gluon does not make any rule decide the placement.
- With V, R1 and R4 pass on the same four placements, and that set includes the builder placement 001. R1@001 flips from fail (−0.42477) to pass (+0.26331; root 1.495025, which is the k = 2 gluon root).
- **Exact identity.** χ_(2,1)(CORE·TAIL_p·V) = −(q⁴+1)/(4q²) · χ_(2,1)(CORE·σ₀σ₀σ₁⁻¹) and χ_(2,1)(CORE·TAIL_n·V) = −(q²+1)²/(4q²) · χ_(2,1)(CORE·σ₀σ₀σ₁⁻¹). So the census-tail element with the k = 1 gluon is, on the (2,1) block, a negative multiple of R1@001 without the gluon. This is why both share the root 1.429157. They are different words, so the identity is about characters only.
- As before, nothing here names a flavour: R1, R2 and R4 give identical elements for p and n.

Full table: run the producer. Nothing is ranked or selected.
