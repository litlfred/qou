---
# qou-xx9f
title: ""
status: todo
type: task
priority: normal
created_at: 2026-08-10T18:07:20Z
updated_at: 2026-08-11T00:46:59Z
---

# GAP: GSWZ (287) input-series identification — printed digits unreproduced

## Context

`computations/probes/gswz_psi_section_division_probe.py` builds the
m=1 fibre of the GSWZ module generator Ψ_ξ (Def 3.9, arXiv:2412.04241)
and runs the (287) division experiment on the 5₂ series. The
STRUCTURAL result holds: the 5-pole cancellation (mod-5 shadow of
module membership) passes and is construction-specific (1 of 14
variant classes in a 28-point grid), and the Ψ-expansion coefficients
(−Li₀/24 · h + 7·Li₋₂/5760 · h³) are archimedean-validated (mpmath,
error scaling h³/h⁵ exact). The dilog inputs are full-precision
(gswz_coleman_li2_full_precision_probe.py, 8/8).

**What fails**: digit-by-digit reproduction of printed (287) x¹..x³
coefficients — under every grid variant (Bernoulli offset, fibre
Frobenius twists, signs) and any scalar (1+x)^λ prefactor (the
mismatch has α-components). Computed digits recorded in
`gswz_psi_section_division.witness.json`.

## Candidate explanations (adjudicate one)

1. The pdf's displayed subscript "f₅(x)" in (287) is genuine — the
   m=5 fibre series is unprinted, so inputs are unavailable. BUT the
   printed coefficients show no ζ₅, which argues for m=1.
2. f₁ as normalized in (281) carries an unprinted α-dependent
   prefactor vs the printed Φ series (footnote 5 in GSWZ §4.5 warns
   of q-power and ζ₈ factor differences vs [26, Eq. 4]).
3. Transcription mangling of the (287) digit groups (pypdf).

## Session narrowing (2026-08-02)

1. **Transcription ruled out**: pypdf plain + layout modes agree on all
   (287) digit groups.
2. **q^lambda single-exponent hypothesis**: solving the alpha-dependent
   lambda from the x^1 mismatch CONFIRMS x^2 mod 25 (~6 digits,
   nontrivial) but FAILS x^3 mod 5 -> the unprinted normalization is a
   SERIES with a nonzero h^3 term (or the f_5 fibre reading is
   genuine). No further solve attempted (would be a fit: x^4 unprinted,
   nothing left to falsify against).
3. **[26] identified + in uploads**: GZ "Knots, Perturbative Series and
   Quantum Modularity" = library/arxiv-2111.06645v3/2111.06645v3.pdf (SIGMA 20 (2024) 055).
   Its 5_2 series conventions (the ones GSWZ footnote 5 says differ by
   "factors of q and zeta_8") use different notation — the exact
   normalization map GZ-(their Eq 4 region)-vs-GSWZ-(281) is the
   remaining read.
4. **(281) layout extraction**: f_1^{5_2}(x) = <e^w psi_{0,z,1}(w,x)^3>
   / sqrt(delta_52) — NO (1+x)^{1/8}-style prefactor visible (unlike
   the 4_1's (276)); delta_52 vs the printed Phi's sqrt(3a-2) is a
   CONSTANT ratio (absorbed by C, cannot explain the mismatch).
5. Owner is eyeballing the pdf for: (a) the f-subscript in (287)
   (f_5 vs f_1); (b) any factor between (281)'s f_1 and (282)'s Phi_1.

## Next steps

- Read [26] (= GSWZ's ref for the 5₂ series normalization) if
  uploaded, to pin the (281) prefactor exactly.
- Alternatively re-extract page 57 of library/arxiv-2412.04241v2/2412.04241v2.pdf with a
  different tool to rule out (3).
- If (2): solve for the α-dependent prefactor from the x¹ mismatch
  and CONFIRM on x²/x³ (falsifiable — 8 independent digits).

## Key files

- computations/probes/gswz_psi_section_division_probe.py (construction)
- computations/probes/gswz_psi_section_division.witness.json (computed digits)
- docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md Addendum 10

## Second narrowing (2026-08-02, post-#4585)

GZ §8.1 read: the C_r are Taylor coefficients of log(1 − e(1/6 + w))
— Li_{−r}-type values with a 1/6-Bernoulli offset (peak M = m + 5/6),
i.e. the E-factor is itself a Pochhammer tail with a DIFFERENT shift
than Def 3.9's q^{1/2}. Two zero-free-parameter hypotheses tested
against the solved lambda digits (const mod 5, alpha/alpha2 mod 25):

- uniform-shift: lambda = (B2(s)−B2(1/2))/2 · Σ c_j Li0(ζ_j) over the
  full shift grid s ∈ {a/b : b | 24}, both signs → NONE.
- parallel-scalar: lambda = D · Σ c_j Li0(ζ_j), any rational D with
  |num|,den ≤ 72 (5-unit) → NONE.

CONCLUSION (scope-(a)): the E-factor's tail arguments are NOT the
(275) roots of unity — most plausibly the Nahm z-variable data of the
psi_{0,z,1}(w,x)^3 Gaussian bracket in (281). Next: extract the 5_2
Nahm data (GSWZ §4.5-4.6 / GZ §8.2-8.3) and re-run the shifted-tail
hypothesis with those arguments.
