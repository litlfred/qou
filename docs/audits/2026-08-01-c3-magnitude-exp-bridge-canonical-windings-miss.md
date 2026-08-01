# c₃ magnitude via the even-channel exponential bridge at canonical windings — honest MISS (2026-08-01)

**Axis:** Q_β c₃ bar-odd `S` — the **magnitude** ratio `|S_p/S_m| ≈ 4.075`
(`qou-82w7` / `qou-dtd3`). **Distinct-angle overlap authorised.** **No c_k wired;
no fit; registry untouched; no `SDeformedVolumeChannel` instance fabricated.** This
doc records a recorded MISS; it does not close the map.

## What was tested (the stated next probe)

`docs/coordination/udeform-spin-part-derivation.md` §"Magnitude path" states the
open next step verbatim: with the **sign** now understood as a discrete
winding-lattice datum (`sign Im 𝔙₄₁ = sign G(m,ℓ)`, [W]), the **magnitude** route is
the *other* channel of the same complex volume — the bar-even / cosh channel — via
the exponential bridge `|δf| ~ e^{−Re 𝔙 / ℏ_q}`, with the lattice-quantized even
potential

```
Re 𝔙₄₁(u_{m,ℓ}) = Vol(4₁) − (3/8)(ln q₀)² · (2m+ℓ)·ℓ      [even/cross form]
```

so the predicted magnitude ratio between two windings is
`|S_p/S_m|_pred = e^{−ΔRe𝔙/ℏ_q} = e^{(3/8)(ln q₀)²·ΔN/ℏ_q}`,
`ΔN = N(m_p,ℓ_p) − N(m_m,ℓ_m)`, `N(m,ℓ) = (2m+ℓ)ℓ`. The corpus flagged the check
as *"derive-then-check, canonical windings only, no tuning … A miss is recorded as
a miss."*

Probe: [`qbeta_c3_magnitude_exp_bridge_windings_probe.py`](../../computations/qbeta/qbeta_c3_magnitude_exp_bridge_windings_probe.py)
(50 dps, exit 0), witness
[`qbeta-c3-magnitude-exp-bridge-windings.witness.json`](../../computations/qbeta/qbeta-c3-magnitude-exp-bridge-windings.witness.json).

## Result — MISS (scope-(a))

| Quantity | Value |
|---|---|
| target `|S_p/S_m|` | `4.075127` |
| distinguished canonical pair | meridian `(1,0)` (N=0) / longitude `(0,1)` (N=1) ⇒ **ΔN = 1** |
| `(3/8)(ln q₀)²/ℏ` (ℏ_q=1−q₀⁻¹) | `0.041205` ⇒ pred `|S_p/S_m| = 1.0421` |
| `(3/8)(ln q₀)²/ℏ` (ℏ=log q₀) | `0.039128` ⇒ pred `|S_p/S_m| = 1.0399` |
| ΔN needed for target (ℏ_q / log q₀) | `34.10` / `35.91` |
| cross-form spectrum `|m|,|ℓ|≤3` | `{−9,−8,−5,−4,−3,−1,0,1,3,4,5,7,8,9,12,15,16,21,27}` |
| is ΔN≈34 a canonical pair-difference? | **no** |

- The genuinely distinguished canonical pair (meridian/longitude — the pair with no
  choice freedom) predicts `|S_p/S_m| ≈ 1.04` under **both** ℏ conventions,
  undershooting `4.075` by **~3.9×**.
- The ΔN that *would* match (`≈34`) is not the canonical pair, and is not even a
  cross-form pair-difference within the `|m|,|ℓ|≤3` box. Reaching it requires
  deliberately selecting large/extreme windings — the **Dang–Purcell dense-fit
  resource** the corpus already flagged (cusp shapes dense in Teichmüller space ⇒
  choosing a knot/winding to hit a number is unbounded fitting, not evidence).

## Why this is a real (if negative) result

1. **It executes the stated open probe with an honest outcome.** The even-channel
   exponential bridge at canonical windings is now a *tested-and-missed* magnitude
   route, not an untested hope. Search narrowed (scope-(a)).
2. **It is consistent with the [W]/[D4] honest negatives** ("sign is
   lattice-arithmetic, magnitudes are not at scale `ln q₀`"): the same `(3/8)(ln q₀)²`
   scale that makes the sign an exact lattice datum makes the magnitude *ratio*
   near-unity per unit ΔN (`e^{0.041} ≈ 1.04`), so the observed `4.075` cannot come
   from a canonical ΔN of order 1.
3. **Scope-(a), not (b).** This does not exclude the even-channel / exponential-bridge
   *ingredient* — a multi-winding sum, a different (derived, not selected) winding
   assignment, or a resurgent prefactor could still supply the magnitude. It excludes
   the *canonical-single-pair, leading-form, no-tuning* realisation as reproducing the
   ratio by itself. Per the (a)/(b) discipline, the ingredient is not ruled out; the
   as-stated closure is.

## What stays open

The c₃ magnitude `|S_p/S_m| ≈ 4.075` is unchanged as an open object. The surviving
candidates the corpus already names (multi-winding even-channel sum; the resurgent
`e^{−Re𝔙/ℏ}` prefactor from the one-instanton census, PR #4246; the Q_β Habiro
element) are untouched by this negative. **Do not route a c₃ closure through the
canonical-winding exponential bridge** — it misses by ~3.9× and matching it is the
dense-fit trap.

-- Ref: [manuscript] docs/coordination/udeform-spin-part-derivation.md (§Magnitude path, bean qou-dtd3)
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md (qou-82w7)
-- Ref: [manuscript] docs/coordination/keystone-sdeformedvolume-channel-attack.md
