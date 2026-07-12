# The c₃ `S` hypersensitivity is a `1/u³` ladder artifact, not a near-singular map

**Date:** 2026-07-12 · **Branch:** `claude/c3-imq-decay-projection-derivation-2026-07-12` ·
**Tier:** derived reframing + scope-(a) recalibration (C14; no fit; no `c_k` wired).
**Probe:** [`qbeta_c3_imq_qstar_ladder_amplification_probe.py`](../../computations/qbeta/qbeta_c3_imq_qstar_ladder_amplification_probe.py).

Autonomous follow-up to the merged #3600 candidate-(iii) connection and PR #3636
(the ε(q₀) decay projection). Pursuing the "third anchor to break the 2-anchor
entropy limit" lead, but with a deterministic-function evaluation rather than a
new physical anchor — which sharpens the picture and **corrects a framing**.

## What was done

The bar-odd target is `S(q) = c₃(q) + Vol(4₁)`, where `c₃(q)` is the *deterministic*
extractor [`qbeta_utils.c3_target_at`](../../computations/qbeta/qbeta_utils.py):

```
Q_A   = m_e·|q²−2q−1|·(q+1)/(2q³)
Q_N1  = Q_A·cos(α − b·ℏ_q²/2)
Q_N2  = Q_N1·(1 − u²),        u = b·ℏ_q²         (c₂ = −1, Lean-proved)
c₃(q) = (Q_β / Q_N2 − 1) / u³
```

Both committed anchors reproduce exactly. Because `c₃(q)` is a function of `q`
(with `Q_β`, `m_e` fixed physical constants), the S-zero `q*` is **root-found**,
not interpolated from two points.

## Finding 1 — `q*` to full precision (given exact inputs)

`S(q*) = 0` at

```
q* = 1.10997859303152328840…
```

`~80.3 %` of the way from the proton anchor to the muon anchor. At `q*`,
`c₃ = −Vol(4₁)` exactly — the **pure bar-even / `ε = 0`** substrate point (the
candidate-(iii) "real q₀", no decay projection).

## Finding 2 — the hypersensitivity is `1/u³` amplification, NOT a singularity

`u = b·ℏ_q² ≈ 0.008517` is the truncation small-parameter; `1/u³ ≈ 1.62×10⁶`.
The measured slope decomposes as

```
S'(q*) = 3.84×10⁶ = 2.37 × (1/u³),   prefactor 2.37 = O(1), smooth.
```

So the famous `dc₃/dq ≈ 4.66×10⁶` is the **`1/u³` ladder-inversion amplification
of a smooth `O(1)` numerator zero-crossing** — the extractor divides the smooth
quantity `(Q_β/Q_N2 − 1)` by `u³ ≈ 6.2×10⁻⁷`. It is **not** a phase "near a
quadrant boundary" and **not** a magnitude singularity.

**Scope-(a) recalibration.** Prior corpus framings read the swing as the
signature of a *near-singular substrate→u map*
([`2026-07-11-c3-wall-branch-structure.md`](2026-07-11-c3-wall-branch-structure.md)
§2 "the phase must move across that boundary rapidly — which IS the
`dc₃/dq≈4.66×10⁶`"; and this branch's own
[`qbeta_c3_imq_ratio_and_entropy_probe.py`](../../computations/qbeta/qbeta_c3_imq_ratio_and_entropy_probe.py)
"2-anchor entropy block"). The **numbers in those probes stand**; only the
"singular map / entropy-blocked" *interpretation* is re-scoped: the underlying
object `(Q_β/Q_N2 − 1)` — hence the decay projection `ε(q₀)` — is **smooth**, and
the wild `c₃` swing is a representation artifact of the `/u³` truncation
inversion. (Per AGENTS.md §"Before declaring refuted": this is a re-scope of an
over-claimed interpretation, not a deletion of a result.)

## Finding 3 — the real limit is the experimental `Q_β`, not the anchor count

`dq*/dQ_β ≈ −0.539`, so `q*` is pinned only as precisely as the neutron β-decay
Q-value is measured (`Q_BETA_MEV ≈ 0.78233`). Identifying `q*` as a mathematical
constant is therefore limited by **experimental `Q_β` precision** — and a *more
precise neutron `Q_β` measurement directly sharpens `q*`*, a concrete falsifiable
lever that more *anchors* at the same `Q_β` would not provide. This refines the
earlier "2-anchor entropy block": the function `S(q₀)` is fully computable; the
block is experimental, on identifying `q*`.

## Disposition

- **Derived / exact:** `q*` (given inputs); `S'(q*) = 2.37/u³`; `dq*/dQ_β`.
- **Recalibrated (scope-(a)):** the hypersensitivity is a `1/u³` artifact, not a
  physical singularity; `ε(q₀)` is smooth.
- **Still open (unchanged):** the *physical model* for the smooth underlying
  object — `Im 𝔙` / the Φ_b state-integral (#3596). No singular map is required;
  a smooth archimedean functor suffices.

## Cross-references
- Candidate (iii): [`conj:im-q-physical-role`](../../content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md); merged #3600.
- Linear response + Lean: PR #3636 (`fig8Trace_im_odd`).
- Extractor: [`qbeta_utils.c3_target_at`](../../computations/qbeta/qbeta_utils.py); source witness `qbeta-c3-keystone-anchor-blind`.
- Φ_b state-integral (open physical model): #3596.
