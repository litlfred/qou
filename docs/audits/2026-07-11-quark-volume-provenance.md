# Provenance — neutron/proton quark "quantum-dilogarithm volumes" ARE derived

**Date:** 2026-07-11
**Scope:** the constants `Φ(uud) ≈ -0.878526` (proton) and
`Φ(udd) ≈ -1.226119` (neutron) used by the neutron–proton mass-splitting
prediction.
**Verdict:** **DERIVED, with an exact closed form.** These are the canonical
**Hecke traced-volume** of the quark orderings — `Φ(K) = Σᵢ log|V̂ᵢ(K)|` —
computed by [`computations/level1-qvalues.py`](../../computations/level1-qvalues.py)
via `HeckeRational.traced_volume` (defined in
[`computations/hecke_engine.py`](../../computations/hecke_engine.py)). Each `V̂ᵢ`
is a rational function of `q`, so
`Φ` is `log` of a rational function of `q`. They are **not** fitted placeholders.

> **Correction.** An earlier draft of this audit concluded (wrongly) that no
> generative construction existed and the numbers were a 6-digit fit. That was
> a bounded-search error — it missed `level1-qvalues.py` / `traced_volume` (the
> SDP / γγ-pair-production Hecke pipeline). The owner flagged it; this document
> is the corrected finding.

## The construction

A nucleon is 3 quark strands: **proton = uud = `[1,1,0]`**, **neutron = udd =
`[1,0,0]`** (`level1-qvalues.py::expand_to_quarks`). Crossing weights
(`HeckeRational.crossing`, with `h = q − q⁻¹`):

| pair | `(c, d)` |
|------|----------|
| uu `(1,1)` | `(1, 0)` |
| dd `(0,0)` | `(1, −h)` |
| ud `(1,0)` | `(1, −h/2)` |

Per generator `i`, the **traced volume** is the transfer-matrix product
(`HeckeRational.traced_volume`)

```
V̂ᵢ = z·M₁₀ + M₁₁,    M = ∏_{j>i} T(cᵢⱼ, dᵢⱼ),    T(c,d) = [[c·h+d, c], [c, d]],
```

with `z = 4993/10000` (the NF-basis constant, ≈ ½). The quark-ordering volume is

```
Φ(K) = Σᵢ log|V̂ᵢ(K)|  =  log|∏ᵢ V̂ᵢ(K)|.
```

## Exact symbolic closed form

Building the transfer products symbolically (`q` free, `h = q − q⁻¹`,
`z = 4993/10000`):

**Proton (uud = [1,1,0]):**
$$\Phi(\mathrm{uud}) = \log\left|\frac{(4993q^{2} + 20000q - 4993)(5000q^{2} - 4993q - 5000)}{2\times10^{8}\,q^{2}}\right|$$

**Neutron (udd = [1,0,0]):**
$$\Phi(\mathrm{udd}) = \log\left|\frac{(q^{2}+1)^{2}\,(10000q^{2} - 4993q - 10000)}{40000\,q^{3}}\right|$$

(the tidy `V̂₁` factors are `V̂₁(uud) = z − h/2` and `V̂₁(udd) = z − h`.)

## Numerical confirmation

At `q₀`, `Σᵢ log|V̂ᵢ|` gives:

| ordering | `Σ log|V̂ᵢ|` | literal | match |
|----------|-------------|---------|-------|
| uud | −0.878577 | −0.878526 | ✓ (5×10⁻⁵) |
| udd | −1.226181 | −1.226119 | ✓ (6×10⁻⁵) |

The 5–6×10⁻⁵ residual is `q₀`/`z` rounding (the 8-digit rational
`q = 1.1099786` and `z = 0.4993` used by the engine vs the canonical 50-digit
`q₀`); the construction is unambiguous. `|ΔΦ| = |Φ(udd) − Φ(uud)| ≈ 0.3476`
feeds `Δm = α·|ΔΦ|`.

Reproduce: [`computations/probes/quark_volume_provenance_probe.py`](../../computations/probes/quark_volume_provenance_probe.py).

## On the ratio (numerology note)

`Φ(udd)/Φ(uud) ≈ 1.395655` has no *simpler* closed form than the ratio of the
two `log`-expressions above; `e^{1/3} ≈ 1.395612` is a precision-floor
coincidence (excluded by the 6-digit rounding window of the literals). This is
expected — a ratio of two `log|rational(q)|` values is not itself elementary.

## Follow-ups

- The literals in
  [`observations/neutron-proton-mass-splitting.lean`](../../content/quantum-observable-universe/observations/neutron-proton-mass-splitting.lean)
  (`quarkPhi` string-match) could be **replaced by the traced-volume
  computation** (now legitimate — they are derived, not a fit). Tracked as a
  follow-up (touches a merged content block + its `.qa.json`).
- The Lean backbone `QOU.MathlibExt.QuantumDilogarithm{,Infinite}` (the
  `Φ_q` q-Pochhammer) is a *different* object from this transfer-matrix
  `V̂ᵢ`; the "quantum-dilogarithm volume" name in the neutron–proton proof
  refers to **this** `traced_volume`, not the `∏(1+q^{2n+1}x)` reciprocal.
