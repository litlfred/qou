# Deuteron +27.4 % overshoot of the log binding law: the two loci

Bean `qou-of4i`, under epic `qou-s028`. Owner ruling 2026-11-25 ("3y sibling"): investigate by derivation only.
Probe: `deuteron_overshoot_loci_probe.py` (mpmath, 70 dps, proton q₀, no float64). Output: `deuteron-overshoot-loci.json`.
Lean: `QOU/Nuclear/UniversalScaleMinimax.lean`.

No value of the scale or of the letter is chosen by its residual. Every candidate below is one the corpus already
defines. AME enters only as a comparison point.

## 0. The headline: the +27.4 % lives on a superseded word

The law is `B = E₀·ln(tr_free/tr_atom)`. The +27.4 % comes from the single-crossing interface letter `g + d_pn` of
`atom_braid_word_3A`. On 2026-11-15 the owner ruled that the γγ selection rule covers the nuclear bond letters
(`docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`). That makes this letter a record, not a current
result.

The γγ chain word has already been computed for A = 2
(`docs/audits/2026-11-22-light-nuclei-a2-a3-gg-chain.md`; `QOU/MassTheory/LightNucleiGGChainSign.lean`, sorry-free):
`μ_pn = 1.000611191`, so `B_log = −2.583 keV`. The deuteron is **unbound** for every `q > 1` and either nucleon order.
That is a scope-(b) result inside the chain, resting on the invariant `μ_x − 1 > 0`. It does not cover all-pairs bonds,
many-body vertices or a non-trace energy map.

So on the ruled word the question is not why the law overshoots the deuteron, but why it does not bind it at all. That
question is bean `qou-brng`.

## 1. Locus (a): the scale E₀

**The live producer uses the non-canonical form.** `binding_log_free_energy.py:85` calls `order_zero_scaled`
(4.185981 MeV) and cites ruling 2026-11-20 (#8590). That ruling only routes historical figures and probes through
`qbeta_e0`, labelled. It does not make order-zero canonical. `qbeta_e0.canonical()` is tower-summed (4.227483 MeV),
by the 2026-09-03 full-tower ruling, and the binding arc ruled the brane-tower form on 2026-09-05. The live
`derived_bond_graph_binding.py` uses the tower form, so two binding producers differ by 0.99 %.

**Every corpus form of E₀ makes the deuteron worse.** The tower form gives +28.62 %. No corpus scale lies below
order-zero.

**One universal scale cannot fix it in any case.** In this law the nucleon traces cancel, so E₀ multiplies only the
interface terms and is shared by every nucleus. Each nucleus needs its own scale `r_A = B_AME/L_A`:

| nucleus | L = ln(tr_free/tr_atom) | err at E₀ | err at E₀ tower | r_A (MeV) | r_A / E₀ |
|---|---|---|---|---|---|
| ²H | 0.676822 | +27.36 % | +28.62 % | 3.2868 | 0.785 |
| ³H | 1.584084 | −21.82 % | −21.05 % | 5.3544 | 1.279 |
| ³He | 1.166721 | −36.72 % | −36.09 % | 6.6152 | 1.580 |
| ⁴He | 2.073983 | −69.32 % | −69.01 % | 13.6431 | 3.259 |

`no_scale_within_minimax` (Lean) says no single E reproduces two nuclei with `r₁ < r₂` better than
`t = (r₂ − r₁)/(r₁ + r₂)` in relative error, and `harmonic_mean_attains` says the bound is sharp. Measured floors:
²H–³H 23.93 %, ²H–³He 33.61 %, ²H–⁴He 61.17 %. `lowering_scale_widens_deficit` says that lowering E₀ toward ²H
strictly widens every A ≥ 3 deficit, and the log law has no many-body term to absorb that.

Scope (a): with this letter, a rescaling alone does not resolve the deuteron. The minimax bound is a structural fact
about the form `B = E·L`, but it is measured here on the superseded letter's `L`.

**Is E₀ derived as the NN scale at all?** No. E₀ = m_e·c_q²·ℏ_q is an identity in CAL-1/2
(`energy-scale-planck`). Reading it as an energy is open (`bond-log-ratio-is-a-free-energy` §"The separate claim";
owner ruling 2026-11-22, bean `qou-91w7`). The route-T thermal reading (spectator audit §8–9, §22) was derived for
the n–p cell, not for an NN bond. The tower factor is canonical by ruling only (bean `qou-y3bm`).

## 2. Locus (b): the p–n letter weight (½ − δ/4)

The weight is **asserted, not derived**. `d_pn = −h(½ − δ/4)` is the colour-blind average of the pp letter σ and
the nn letter σ⁻¹, shifted by the mass flavour split δ (spectator audit §18: *"every construction carrying δ is
asserted"*). The δ shift moves B by 0.6 keV. Every derived alternative the corpus defines, at both scales:

| candidate letter | μ_pn | err at E₀ | err at E₀ tower |
|---|---|---|---|
| colour-weighted `−h(½ − δ/4)` (live) | 0.508230 | +27.36 % | +28.62 % |
| colour-blind `−h/2` | 0.508158 | +27.38 % | +28.65 % |
| derived crossing weight `w = 1/(q²+1)` | 0.497291 = 1/[2]_q | +31.45 % | +32.76 % |
| geometric mean `√(z(z−h))` | 0.497291 = 1/[2]_q | +31.45 % | +32.76 % |
| isospin T=0 projector μ₋ (the deuteron channel) | 0.247298 = 1/[2]_q² | +162.90 % | +165.51 % |
| isospin T=1 projector μ₊ | 0.752702 | −46.54 % | −46.01 % |
| bare σ (d = 0) | 0.612688 = z_D | −7.82 % | −6.90 % |
| bare σ⁻¹ (d = −h) | 0.403628 | +70.72 % | +72.41 % |

The three closed forms (`1/[2]_q` twice, `1/[2]_q²`) are exact under convention D, checked to 1e-71. Every derived
p–n construction (the crossing weight, the geometric mean the log law wants by AM–GM, and the isospin singlet)
overshoots by more than the live letter. Only the bare σ, which is the pp letter, comes in under AME.

Diagnostic only, not a target: AME would need `d/h = −0.11923` at order-zero E₀. The 2026-08-09 retraction in
`InterfaceScalar.lean` quotes −0.11945, and the gap between the two figures is not traced here. Picking `d` to hit
this value is a fit.

## 3. What this leaves

- On the superseded letter: no corpus scale and no corpus p–n letter reproduces ²H, and a universal rescaling is
  floored by the minimax bound. Both loci are scope-(a) negatives there.
- On the ruled γγ word: the deuteron is unbound (`μ_pn > 1`, proved). That is the live problem, bean `qou-brng`.
- The scale inconsistency between producers (order-zero against the ruled tower form) is a separate defect, worth
  0.99 %. It cannot close the gap and needs an owner decision.
