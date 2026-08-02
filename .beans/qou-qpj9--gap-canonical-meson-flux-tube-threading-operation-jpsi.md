---
# qou-qpj9
title: 'GAP: define canonical meson flux-tube threading braid (J/ψ underived)'
status: open
type: task
priority: normal
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-08-02T00:00:00Z
---

## The wall

J/ψ = c̄c targeted as a hyperbolic bound-state braid volume
(`computations/jpsi_boundstate_mass_probe.py`,
`docs/audits/2026-08-02-jpsi-boundstate-mass.md`, branch
`claude/jpsi-boundstate-mass-2026-08-02`).

**In-range but underived.** With the scale fixed only on the proton
(Borromean → 938 MeV, 128.044 MeV/Vol), J/ψ needs Vol ≈ 24.19 and η_c
needs Vol ≈ 23.30 — both reachable by simple hyperbolic braids (positive:
distinguishes J/ψ from the neutrino's scope-(b) volume exclusion). But **no
derived c̄c braid**:

1. The proton's own family `(σ₁σ₂⁻¹)^k` misses J/ψ at every integer winding
   (k=6→2770, k=7→3336; J/ψ=3097 falls between).
2. The volume spectrum is dense near target (~4% of 196 simple braids land in
   the 230-MeV band).
3. J/ψ and η_c — the same c̄c system split by only 3.7% hyperfine — are best-fit
   by DIFFERENT-topology braids (4-str `(σ₁σ₂⁻¹σ₃)⁴`→3085 vs 5-str
   `(σ₁σ₂⁻¹σ₃σ₄⁻¹)³`→2964). Per-state fitting signature.

## The precise open item

**"Thread c̄c through the gluon T(2,9) color tube" is topologically
under-defined.** Satellite/companion, cable, connected-sum (non-hyperbolic),
and strand-insertion each give a different volume; the framework specifies no
canonical operation. A prediction requires a **single canonical parameter-free
topological operation** that fixes strand count + insertion sites + winding from
the c̄c + gluon quantum numbers *without reference to 3097 MeV*, then check once
against J/ψ AND η_c jointly (same base braid, hyperfine as perturbation).

## Suggested next honest step

Derive the meson flux-tube operation from the proton's 3-tube Borromean vertex
by the Y-junction → single-tube reduction (baryon → meson). If that reduction
fixes a unique braid a priori, it is a genuine derivation; check it once.
Anything that picks the braid to land on 3097 is a fit and worthless.
