# W2 briefing to all workstreams — Q_β, u/d representation, six-term sweep (2026-11-20)

Owner instruction 2026-11-20: inform every sibling. Record of the arc: [`docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md`](../audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md). Posted to the coordinator channel (#8526) and to beans qou-99qc, qou-cds1, qou-0whz, qou-wkcd, qou-2tuv, qou-10v9, qou-qs0e, qou-47sx.

## 1. What is settled (merged; Lean has no `sorry` and no extra axioms)
- **Q_β depends on one number.** For every block-weighted trace, Q_β = (h[2]/2)·y₃·E₀, where y₃ = τ(J) is the chirality expectation (`QBetaChiralityReduction.lean`). The nucleon's own isospin-½ block contributes 0, because χ₍₂,₁₎(Δ_S) = 0. **Only the weight on the isospin-3/2 (3) block matters.** CODATA needs y₃ ≈ 0.889 with the order-zero E₀, or 0.880 with the tower E₀.
- **The ruled ε (the Markov trace at z_D, y₃ = 0.5054, −43 %) is explained twice.**
  - It is the flavour round trip on label A: `FlavourRoundTrip.roundTrip_A`, tr(Lu σ₂ Ld σ₂) = (q⁴+1)/(q²+1)².
  - It is also the whole-space quantum trace Tr(K^⊗3·) on (ℂ²)^⊗3.
- **Label B (J₄ lines, flipped only by the strand-4 γγ vertex σ₂σ₃⁻¹) gives y₃ = cJ/2 = [2]²[2]_{q²}/[3]² = 0.8921**, so Q_β is **+0.33 %** (order-zero E₀) or +1.32 % (tower E₀). This is proved in `roundTrip_B` and `roundTrip_B_gg`. **It is NOT adopted.** J₄ labels the (3) vs (2,1) sector, i.e. isospin 3/2 vs ½, not n ↔ p, and choosing it for its residual would be selection against the target.
- **Label C (u/d as T³ weights, the physical n ↔ p label) is measured** (probes, exact over ℚ(q)). None of these comes close:

  | construction | y₃ | Q_β |
  |---|---|---|
  | one charge sector | 1/3 | −62.5 % |
  | nucleon block | 0 | 0 |
  | single-quark E/F flip | q⁴/(2(q⁴+q²+1)) = 0.202 | −77 % |

  No braid word changes T³ (qou-0whz C2).
- **Owner choice "3 2":** there is NO label ruling. A and B stay side by side, ε stays the 2026-09-08 ruling, and research on label C continues.

## 2. Corrections — stop using these
- **"ε = Markov trace" is a RULING, not a derivation.** Δ (typed crossings) is a definition, and E₀ is posited.
- **The decay formula's Δ and E₀ are not the mass channel's objects.** The mass-channel scale is 2m_μ[3]_q!/q³ = 945.76 MeV per unit trace; applied to this Δ it gives Q_β ≈ 100–177 MeV.
- **The "+0.17 % Q_β" (Form A) needs z = 1 and the order-zero E₀.** Both are superseded. With the tower E₀ it is +1.16 %.
- **The "~1 ppm Q_β" needs Form A plus the convention-C Kashiwara ladder.** Convention C is excised. With the convention-D phase it is +602 ppm.
- **The April Breit–Wheeler nucleon run (`fsh-guts/deprecated/.../breit-wheeler-nucleon-nf.py`) is circular.** Its E₀ = Q_β(AME)/Δnet, to 1e-13.
- **u and d are NOT "one representation with opposite orientation".** They are separate lines of the (3,1) rep of H₄(q) (`QOU/QuarkState/FlavourDoubletFourStrands.lean`). `def:up-quark` / `def:down-quark` still say orientation-only. They are cited by 9 blocks, and 36 blocks say "typed crossing". They will be rewritten once the owner picks a label, so do not build on them in the meantime.
- **The m_μ "8.06 ppb" is superseded** by the owner's 16:44 ruling: all-pairs covariant QED gives 211.2 ppb, the same as the one-term value.

## 3. Compute changes merged today (W2)
- **#8521: per-generator volumes are now convention D (z·a+b), in Python AND Rust.** The Rust half was missing, and the native wheel was silently returning the old mixture. Under D the proton and neutron volumes (1.2824, 1.1337) lie **past the Φ_q pole at q₀**.
- **#8578: the six-term sweep.**
  - The −2.43e15 MeV was a truncated divergent series. The fix uses `_li_2_q_util.li_2_q`, the continuation; in li2q mode −Li₂^q(−V) is finite for every V > 0.
  - `brane-legacy` (Φ_q) now reports inf instead of hiding it. Its Term 2 was 0 for every isotope in every convention, because a swallowed TypeError hid the failure.
  - The formula still misses every isotope by about 97 %.
- **#8082:** 50-dps q₀/mass in the dashboard and in `canonical_mass`.
- **#7443:** float64 `q_int` excised; `_DPS_DEFAULT` raised from 50 to 70.
- **#8540:** the Q_β ladder threads are consolidated. The derived c₂ rung recovers about 0 % of the gap, and no cosine can close it, because F_required > 1.

## 4. Where to pick up
Bean `qou-99qc` is the live front. The next target is to derive why the decay functional weights the isospin-3/2 block at about [2]²[2]_{q²}/[3]². Related beans: qou-cds1, qou-0whz, qou-wkcd, qou-2tuv, qou-10v9.

