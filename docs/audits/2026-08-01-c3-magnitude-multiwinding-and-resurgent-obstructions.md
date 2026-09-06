# c₃ magnitude: multi-winding sum diverges, resurgent ratio is circular — two honest obstructions (2026-08-01)

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Axis:** Q_β c₃ bar-odd `S` — the **magnitude** ratio `|S_p/S_m| ≈ 4.075`
(`qou-82w7` / `qou-dtd3`). **Distinct-angle overlap authorised.** **No c_k wired;
no fit; registry untouched; no `SDeformedVolumeChannel` instance fabricated.**
Follow-up to the single-pair MISS (PR #4497): the two natural next candidates —
a multi-winding **sum** and the resurgent **prefactor** — are both ruled out or
shown circular. The magnitude stays open.

## Background

Single-pair result (#4497): at the distinguished canonical meridian/longitude
pair (ΔN=1) the even-channel exponential bridge `|δf| ~ e^{−Re𝔙/ℏ_q}` predicts
`|S_p/S_m| ≈ 1.04`, a ~3.9× miss. The obvious escalations are (1) sum over more
windings, (2) use the resurgent one-instanton prefactor. This doc records both.

Probe: [`qbeta_c3_magnitude_multiwinding_sum_probe.py`](../../computations/qbeta/qbeta_c3_magnitude_multiwinding_sum_probe.py)
(exit 0), witness
[`qbeta-c3-magnitude-multiwinding-sum.witness.json`](../../computations/qbeta/qbeta-c3-magnitude-multiwinding-sum.witness.json).

## (1) Multi-winding even-channel SUM diverges (leading truncation) — DIV

The even/cross potential is `Re𝔙₄₁(u_{m,ℓ}) = Vol(4₁) − (3/8)(ln q₀)²·N(m,ℓ)`,
`N(m,ℓ)=(2m+ℓ)ℓ`. The cross-form `N` is **indefinite and unbounded above** (e.g.
`N(1,ℓ)=(2+ℓ)ℓ → +∞`). So along those windings `Re𝔙 → −∞` and the bridge term
`e^{−Re𝔙/ℏ_q} = e^{(3/8)(ln q₀)²N/ℏ_q − Vol/ℏ_q} → +∞`. The lattice sum
`S_sum = Σ_{m,ℓ} e^{−Re𝔙/ℏ_q}` therefore **diverges**.

Verified numerically — partial sums and the max single term over the `|m|,|ℓ|≤R`
box both grow monotonically and super-linearly:

| box R | partial sum | max term |
|---|---|---|
| 1 | 1.17e-8 | 1.43e-9 |
| 4 | 1.67e-7 | 9.15e-9 |
| 6 | 1.10e-6 | 1.08e-7 |
| 10 | 1.35e-3 | 2.96e-4 |

**Scope-(a), leading-truncation.** The multi-winding even-channel sum, *in the
leading quadratic truncation of the NZ potential*, is not a convergent magnitude
object. A convergent realisation requires either the **full (non-truncated)
complex volume** `𝔙₄₁` — whose large-`|u|` growth would restore convergence — or
an **ad-hoc winding cutoff**, and a cutoff chosen to reproduce `4.075` is the
Dang–Purcell dense-fit resource. So the leading-form multi-winding sum is **not**
the parameter-free magnitude source. This is a statement about the *truncation*,
not the full `𝔙₄₁` — the even-channel ingredient is not excluded (scope-(a)).

## (2) Resurgent one-instanton magnitude ratio is CIRCULAR — CIRC

The one-instanton census form (PR #4246) is
`N_odd(q) = 𝒜·e^{−Re𝔙/(πℏ)}·sin(Im𝔙/(πℏ))`, `ℏ = log q`. The two anchors have
near-identical `q₀` (`Δ ln q₀ ≈ 1.15×10⁻⁸`), so the exponential prefactor
`e^{−Re𝔙/(πℏ)}` is equal at both to `~7×10⁻⁷` relative (probe: prefactor ratio
`≈ 1.0000007`). Hence

```
|S_p/S_m| ≈ |sin(Im𝔙_p/(πℏ)) / sin(Im𝔙_m/(πℏ))| .
```

But `Im𝔙 = S` is exactly the quantity being solved for. The resurgent prefactor
does **not independently predict** `|S_p/S_m|` — it re-expresses it in terms of
itself. The magnitude ratio via the one-instanton form reduces to the open
argument map `u(q₀)`, confirming #4246's "structurally necessary, quantitatively
open." Recorded as **CIRC**, not a fresh negative.

## Net — what stays open

The c₃ magnitude `|S_p/S_m| ≈ 4.075` is unchanged as an open object. The
even-channel exponential bridge is now tested three ways, all negative:
single canonical pair misses ~3.9× (#4497); multi-winding **leading-form** sum
diverges (this doc); resurgent prefactor ratio is circular (this doc). The
surviving, un-refuted candidates are the ones that require the **full 𝔙₄₁**
(not the quadratic truncation) or a genuinely-derived (not selected) winding
assignment — i.e. the same open argument map `u(q₀)`. **Do not route a c₃ closure
through the leading-truncation multi-winding sum or the resurgent prefactor
ratio** — the first diverges, the second is circular.

-- Ref: [manuscript] docs/coordination/udeform-spin-part-derivation.md (§Magnitude path, bean qou-dtd3)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-magnitude-exp-bridge-canonical-windings-miss.md (single-pair MISS, #4497)
-- Ref: [manuscript] docs/audits/2026-07-25-aomega-one-instanton-magnitude-probe.md (#4246 one-instanton)
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md (qou-82w7)
