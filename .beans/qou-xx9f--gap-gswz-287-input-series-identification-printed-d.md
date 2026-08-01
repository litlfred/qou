---
id: qou-xx9f
type: task
status: todo
priority: normal
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

## Next steps

- Read [26] (= GSWZ's ref for the 5₂ series normalization) if
  uploaded, to pin the (281) prefactor exactly.
- Alternatively re-extract page 57 of uploads/2412.04241v2.pdf with a
  different tool to rule out (3).
- If (2): solve for the α-dependent prefactor from the x¹ mismatch
  and CONFIRM on x²/x³ (falsifiable — 8 independent digits).

## Key files

- computations/probes/gswz_psi_section_division_probe.py (construction)
- computations/probes/gswz_psi_section_division.witness.json (computed digits)
- docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md Addendum 10
