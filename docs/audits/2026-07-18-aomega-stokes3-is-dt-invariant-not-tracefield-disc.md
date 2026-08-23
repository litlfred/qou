# A_ω: the 4₁ Stokes `−3` is a DT/BPS invariant (constants {3,4}), NOT the trace-field discriminant

**Date:** 2026-07-18 · **Branch:** `claude/pr-3660-merge-pipeline-ephmw4` ·
**Bean:** `qou-t3jv` (A_ω odd channel) · **Probe:**
[`qbeta_aomega_stokes3_tracefield_probe.py`](../../computations/qbeta/qbeta_aomega_stokes3_tracefield_probe.py) (+ witness) ·
**Tier:** primary-source read (GGM 2012.00062, pymupdf) + exact arithmetic ·
**Scope:** (a) — refutes a specific identification; the trace-field fact stands.

## The question

The A_ω frontier (#3813, #3872) narrowed to one open item — the
coefficient↔Stokes dictionary — whose load-bearing datum #3813 records as the
integer `−3` in the classical Stokes matrix `S⁰ = [[1,0],[−3,1]]` of the
figure-eight. The corpus separately has `ℚ(√−3)` as the 4₁ invariant trace
field (disc `−3`, #3571) and the even-channel action Lean-certified in `ℚ(√3)`
(`κ₁ = 11√3π/108`; `Qsqrt3SaddleArithmetic.lean`). Natural hypothesis (H1): the
Stokes `−3` **is** the trace-field discriminant, unifying the two channels'
"3".

## Verdict — H1 refuted (scope-a), with the invariant cited

Reading GGM 2012.00062 **directly** (pymupdf; the sandbox's `pdfminer` is
broken, `pymupdf` is not), the 4₁ Stokes matrices at `q→0` are (Eq 96, p21):

```
S+(0) = Sσ₃σ₁ · Sσ₃σ₂ · Sσ₁σ₂
      = [[1,0,0],[0,1,0],[−3,0,1]] · [[1,0,0],[0,1,0],[0,3,1]] · [[1,4,0],[0,1,0],[0,0,1]]
```

and the assembled off-diagonal **Stokes-constant matrix** (Eq 98, p22) is

```
[[ 0,  4,  3],
 [−4,  0, −3],
 [−3,  3,  0]]
```

So the 4₁ Stokes constants are **{3, 4}** (up to sign), and the paper is
explicit (§1.2, §5.5) that these integers are the **Donaldson–Thomas / BPS
invariants** of the 3d `N=2` theory `T[4₁]` (Conjecture 4: `S+ =` the rotated
3D-index).

**The `−3` is the `(σ₃,σ₁)` DT invariant — but a `4` co-occurs** (`(σ₁,σ₂)`).
If `−3` were the number-field discriminant, the co-occurring `4` has no
discriminant meaning. The Stokes data is the DT/BPS *spectrum*, not the trace
field's discriminant; identifying the single `−3` with `disc(ℚ(√−3))` was the
small-integer coincidence the anti-numerology discipline guards against.

**Scope (a):** this refutes the *disc-identification of the Stokes `−3`*. It
does **not** touch the established fact that `ℚ(√−3)` is the 4₁ trace field.

## What still stands — the cross-channel arithmetic bridge (verified exactly)

Independent of the Stokes question, the probe verifies (numeric, 50 dps, ≤1e-40):

| # | fact |
|---|---|
| V1 | 4₁ ideal-tetra shape `z = e^{iπ/3} = ½ + i√3/2`, a primitive 6th root |
| V2 | trace field `ℚ(√−3)`, field disc `−3` (since `−3 ≡ 1 mod 4`); `√−3 = i√3` |
| V3 | `Vol(4₁) = 2·Im Li₂(e^{iπ/3}) = 2.029883…` (angle `π/3`) |
| V4 | `√3 = ζ₁₂+ζ₁₂⁻¹` (real) and `i√3 = ζ₃−ζ₃⁻¹` (imag) — even saddle field `ℚ(√3)` and odd trace field `ℚ(√−3)` share `|disc|=3`, related by `√−3 = i√3`, both inside `ℚ(ζ₁₂)` |

The even channel's `√3` (Lean-certified) and the odd channel's `√−3` (trace
field) **are** the same arithmetic refracted through `i` — but the Stokes
*integers* are the DT spectrum `{3,4}`, a different object.

## Implication for the A_ω dictionary (coordination)

The coefficient↔Stokes dictionary needs the **DT spectrum `{3,4}`** = the
rotated 3D-index (GGM Conjecture 4) — exactly the object **#3872's annihilator /
3D-index route** and **#3813's 4₁ 3D-index assembly** already target. A
discriminant identity is *not* the tool. This sharpens the open item and closes
one tempting numerological side-path.

**Discipline:** primary-source read; no fit; no `c_k` wired; no A_ω value
claimed; registry untouched. Refutation scoped (a) with the invariant (DT
spectrum, Conjecture 4) cited, per the "before declaring refuted" rule.

## Cross-references
- GGM 2012.00062 Eq 96/98 (`library/arxiv-2012.00062v3/2012.00062v3.pdf`)
- Even-channel `ℚ(√3)`: [`2026-07-11-fmap-action-qsqrt3-saddle-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-block.md); `QOU/QBeta/Qsqrt3SaddleArithmetic.lean`
- A_ω scouts: #3813 (3D-index assembly), #3872 (annihilator certificate)
