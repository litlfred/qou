# Pre-registration: coloured (Yokonuma) strands and the n–p sign (2026-11-21)

Written before the probe `np_yokonuma_flip_probe.py` is run. Owner chose this route on 2026-11-21
("Coloured / Yokonuma strands"). It extends §12 of `docs/audits/2026-11-15-np-splitting-error-budget.md`,
which found n − p = 0 for the half and the full twist at x = 0. That probe was re-run on 2026-11-21 and
reproduced.

## Setup (fixed in advance)
- Algebra Y_{2,3}(q), presentation and basis t^a g_w (48 elements) exactly as in
  `np_yokonuma_coloured_probe.py`. Exact over Q(q, z, x), plus symbolic photon coefficients.
- Juyumaya trace solved from its defining linear system; z = z_D = q³/(q²+1).
- u ↦ t-eigenvalue +1, d ↦ −1. Colour flip φ: t_j ↦ −t_j, g_i ↦ g_i.
- Words: the ruled γγ core V³ = (g₁g₂⁻¹)³, the two ruled photon factors γ(0,0,qh) and γ(0,0,−q⁻¹h)
  with γ(φ₀,φ₁,φ₀₁) = 1 + φ₀g₁ + φ₁g₂ + φ₀₁g₁g₂⁻¹, the generic photon with symbolic φ's, the half twist
  and the full twist. Proton placements: uud, udu, duu. Neutron placements: their flips ddu, dud, udd.
- Nothing is fitted. No CODATA value is used.

## Predictions
- **Y1.** φ is an algebra automorphism: φ(XY) = φ(X)φ(Y) for all 48 × 48 basis pairs.
- **Y2.** At x = 0 the trace is φ-invariant on all 48 basis elements. At symbolic x it is not:
  tr(φ(b))(x) = tr(b)(−x).
- **Y3.** At x = 0, for every listed word W and every proton placement c,
  tr(π_{flip c} W) = tr(π_c W). So n = p for every word, and every trace → mass reading gives
  m_n = m_p. The neutron-heavier question then has no sign to settle.
- **Y4.** At symbolic x, tr(π_{flip c} W)(x) = tr(π_c W)(−x). The n − p difference is odd in x. A sign
  would therefore require choosing the sign of x. The E-system allows only x ∈ {1, 0, −1}, and ±1 kills
  one colour sector (§12). So no admissible x gives a sign.

If Y1 or Y2 fails, the flip argument is wrong and Y3 must be read word by word.
