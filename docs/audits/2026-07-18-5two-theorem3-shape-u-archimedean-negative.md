# Theorem 3 IS the 5₂ dilog closed form; the naive real-u archimedean identification is ruled out

> **⚠ INHERITED PREMISE CORRECTED (2026-08-11).** The prior step this document
> builds on named ℚ(√−7) as the bar-odd action's home. That is wrong: 5₂'s
> invariant trace field is the **cubic of discriminant −23**, and ℚ(√−7) cannot
> embed in it (`[ℚ(√−7):ℚ] = 2 ∤ [K:ℚ] = 3` — the tower law). ℚ(√−7) belongs to
> 5₂'s **Alexander** layer (`Δ = 2t²−3t+2`, `disc = −7`, `det = 7`), not its
> geometric one.
>
> **This document's own result is unaffected.** Its content is a *negative* — the
> naive real-`u` archimedean identification is ruled out — and that negative was
> established by evaluation, not by any property of the field. Correcting the
> field does not revive the ruled-out identification; if anything it removes a
> reason the identification was expected to work.
>
> What does need re-reading is the §Setup sentence below, corrected in place, and
> the *positive* half of the title. "Theorem 3 IS the 5₂ dilog closed form" was
> argued by solving `L(u) = Li₂(z₁) + 2Li₂(z₂)` numerically for `u` — one equation,
> one unknown, in an analytic function, which essentially always has solutions.
> Matching a sum's *value* is not matching the *triple*. Treat that half as
> unestablished pending a check that the arguments themselves correspond.
>
> Correction: [`2026-08-11-5two-trace-field-is-disc-minus-23.md`](2026-08-11-5two-trace-field-is-disc-minus-23.md)
> · certification: [`qbeta_5two_trace_field_disc23_not_qsqrt7.py`](../../computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py)
> · bean `qou-ynff`.

**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ · **Tier:** numerical
scope-(a) (one positive confirmation + one honest negative) · **Discipline:** no fit,
no c_k wired, nothing to production, no tier change.

## Setup

The prior step ([`…-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md))
established the bar-odd action's home = ℚ(√−7) [**retracted 2026-08-11 — the trace
field is the cubic of disc −23; ℚ(√−7) is the Alexander layer**] and pointed at Theorem 3 of the owner's
dilog paper ([`uploads/2506.10206v2.pdf`](../../uploads/2506.10206v2.pdf)):
`L(u) = Li₂(z_a)+Li₂(z_b)+Li₂(u) = E(u)`, with `E` elementary for real `u>0`. This step
tests whether that yields the bar-odd archimedean action directly.

## (+) Theorem 3 IS the 5₂ three-tetrahedron dilog closed form

[`qbeta_5two_theorem3_shape_u_probe.py`](../../computations/probes/qbeta_5two_theorem3_shape_u_probe.py):
`L(u)=E(u)` verified to 20 digits (transcription correct). Solving

> `L(u) = Li₂(z₁) + 2·Li₂(z₂)`  (the exact 5₂ three-tetrahedron plain-Li₂ sum)

converges to **three u-branches** — the three tetrahedra — each an apparent ℚ(√−7)
value. So Theorem 3 reproduces the 5₂ geometric dilog sum: it **is** the 5₂ closed form.

## (−) The naive archimedean identification is ruled out

The bar-odd action is **not** simply `E(u)` at a real-u saddle. Across real `u ∈ (0, 4/3)`,

> `Re E(u) ∈ [3.0024, 3.2830]`,

which matches **none** of the clean candidates — `π²/5=1.974`, `π²/6=1.645`,
`5π²/6=8.225`, the `π²/7`-family (nearest `2π²/7=2.820`, gap `>0.18`), nor
`3·Re Li₂((3−i√7)/8)=1.110`. So the `ħ↔2πi/N` wall connecting the Theorem-3 geometric
face to the archimedean `ρ_∞` face is **more subtle than real-u evaluation**.

## Where the bar-odd action now sits

**Localized to the block-saddle wall crossing.** The sibling M-dictionary program
(Theorem 22: exact Z₅₂ = three blocks A·A + B·B + C·C, with Δ-constants
`β_A=5πi/12 → −5π²/6`, `β_B=β_C=πi/12 → −π²/6`) is deriving exactly the block↔saddle
sheet data that the archimedean continuation needs — the **same three-fold structure**
as Theorem 3's three dilogs, with elementary π²-rational block actions. The bar-odd
action is the correct combination of those block actions across the wall, **not** a bare
`E(u)`. The two derivations (dilog closed-form ↔ block/saddle) should converge there.

## Scope (anti-laundering)

Confirms Theorem 3 = the 5₂ dilog closed form; **rules out** the naive real-u
identification of the bar-odd action (honest negative). No bar-odd action value is
claimed. No fit; no c_k; no tier change.

## Cross-references

- Prior step (ℚ(√−7) home): [`2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md)
- Paper: [`uploads/2506.10206v2.pdf`](../../uploads/2506.10206v2.pdf) (Theorem 3; Examples 5–8, ℚ(√−7))
- Sibling M-dictionary (block/saddle): `qbeta_g3_5two_block_saddle_dictionary.py`, `qbeta_5two_phi_series_engine_probe.py` (Theorem 22, β blocks)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
