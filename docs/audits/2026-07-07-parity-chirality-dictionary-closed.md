# The parity ↔ chirality dictionary, closed: even = amphichiral 4₁, odd = chiral Hopf cubic

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (odd-channel chiral source)
· **Tier:** proved-lean (algebra) + structural-exact (roots/discriminants)
· **Discipline:** no fit, no c_k value, no wiring, no tier change. Confirms two
existing corpus files; adds the synthesis, the complex-root computation, and the
Lean formalization.

## The dictionary

The bar-involution `q ↦ q⁻¹` is the mirror/chirality operation, so bar-parity ↔
knot chirality ↔ the arithmetic type of the channel:

| channel | trig | datum | knot | chirality | arithmetic |
|---|---|---|---|---|---|
| **bar-EVEN** | cosh | m_π (CAL-3) | pion = half-4₁ | **amphichiral** (CS=0) | 𝔙 **real**; `e_k ∈ ℚ(√3)` |
| **bar-ODD** | sinh | Q_β (CAL-2) | Hopf link | **chiral** (2-crossing) | cubic, disc **< 0**, **complex** roots |

The **even** row is the amphichirality result of [#3482](https://github.com/litlfred/qou/pull/3482)
(`4₁` amphichiral ⇒ `CS(4₁)=0` ⇒ `𝔙(4₁)=Vol` real; the resurgence action is real
≈0.69) — itself a re-derivation of the corpus's
[`self-dual-higgs-real-volume.md`](../../content/quantum-observable-universe/braids-and-knots/self-dual-higgs-real-volume.md)
("the bare Higgs knot contributes only the real volume (mass) face; its imaginary
(decay) face vanishes").

The **odd** row is the corpus's
[`qbeta-odd-carrier-hopf-cubic.md`](../../content/quantum-observable-universe/mass-theory/qbeta-odd-carrier-hopf-cubic.md):
the bar-odd carrier collapses (in `y = q²+q⁻² = 2cosh2λ`) to `C(y) = y³−4y²+3y−2`,
whose cubic is sourced **entirely by the chiral Hopf sector**.

## What this tranche adds (probe 9/9 + Lean, sorry-free)

Probe [`qbeta_hopf_cubic_complex_roots.py`](scripts/qbeta_hopf_cubic_complex_roots.py),
Lean [`HopfCubicOddCarrier.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/HopfCubicOddCarrier.lean):

1. **Sector decomposition, exact:** `C = C_Hopf + C_unknot` with
   `C_Hopf = y³−6y²+10y−6`, `C_unknot = 2y²−7y+4` (Lean `cTotal_eq_cHopf_add_cUnknot`).
2. **The odd channel's complex source is arithmetic, not hyperbolic.**
   `disc(C_Hopf) = −76 < 0` ⇒ one real root + a **complex-conjugate pair**
   `1.1154 ± 0.5897i`. So "chiral ⇒ complex" is realized by a **negative-discriminant
   cubic** — *not* a hyperbolic knot's `iCS` (the Hopf link is non-hyperbolic,
   Vol=0). The shared **prime 19** (`disc C_Hopf=−76=−2²·19`, `disc C=−152=−2³·19`)
   is the arithmetic fingerprint (Lean `cHopf_discriminant_eq`,
   `prime_19_divides_both_discriminants`).
3. **Classical anchor `C_Hopf(2) = −2` exactly** = `J_Hopf(q=1)` = the empirical
   `c_3` near-match (Lean `cHopf_at_two`). At `q=1` the Hopf sector alone gives −2.
4. **Fibre carrier, not the swing.** At the substrate `y₀ ≈ 2.0437`,
   `C_Hopf(y₀) ≈ −2.087 ≈ c_3`, but **anchor-invariant** (cross-anchor swing `9×10⁻⁹`
   vs c_3's 2.4%). So the cubic is the **fibre carrier**, and the c_3 swing is the
   archimedean **S leak** — precisely the split proved by
   `SRigidityPrune.no_anchor_invariant_realizes_swing` (#3474). The complex-root real
   part ≈ q₀ (rel 0.5%) is **flagged, not claimed**.

## Why this matters for the keystone

The odd channel's complex/chiral structure is now **located and typed**: it is the
complex-conjugate root pair of the Hopf cubic (an `S₃` degree-3 field, prime 19),
sitting at the **fibre** level. This confirms (arithmetically) why S resists a
real-q closure — a degree-≤2 / real-q anchor can never be a root of an irreducible
cubic (the corpus's structural argument), which is the arithmetic face of the
rigidity prune. **It does not derive S**: the fibre cubic is anchor-invariant; the
anchor-dependent leak (S = Q_β/E₀, CAL-2) remains Subgoal-2. The dictionary tells us
*where* the complex structure lives (Hopf cubic, fibre) and *where it does not*
(the amphichiral even sector, and not in a hyperbolic iCS).

## Cross-references

- Lean: [`HopfCubicOddCarrier.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/HopfCubicOddCarrier.lean)
- Probe: [`qbeta_hopf_cubic_complex_roots.py`](scripts/qbeta_hopf_cubic_complex_roots.py)
- Odd carrier (corpus): [`qbeta-odd-carrier-hopf-cubic.md`](../../content/quantum-observable-universe/mass-theory/qbeta-odd-carrier-hopf-cubic.md)
- Even partner (corpus): [`self-dual-higgs-real-volume.md`](../../content/quantum-observable-universe/braids-and-knots/self-dual-higgs-real-volume.md)
- Amphichirality (this session): [#3482 real action](2026-07-07-borel-pade-action-real-amphichiral.md)
- Rigidity prune: [#3474 S rigidity](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)
