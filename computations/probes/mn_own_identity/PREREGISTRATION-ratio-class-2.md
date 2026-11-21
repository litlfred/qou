# Pre-registration: second ratio class (the missing factor 6)

Written and committed 2026-11-21 before `mn_pairing_ratio_class2_probe.py` was run. Owner: "1 2".

Context: §15 found `⟨X_N⟩/⟨X_e⟩ = 2` at `q = 1` (mixed sector average), against a target of `12`.

Same representation as class 1 (Jimbo `Ř` on `V^{⊗3}`, `K = diag(q, q⁻¹)^{⊗3}`), electron
`X_e = ρ(σ₀σ₁σ₀)` with the whole-space mixed expectation, nucleon `X_N = ρ((σ₀σ₁⁻¹)³)`. Variants,
all fixed now, all reported:

- **P1, pure weight states.** Each standard basis vector `b` of the proton sector (2 up, 1 down) and
  of the neutron sector (1 up, 2 down): `⟨b|K X_N|b⟩ / ⟨b|K|b⟩`, divided by `⟨X_e⟩`. Every basis
  vector is reported; none is chosen.
- **P2, unnormalised closed traces.** `tr_sector(K X_N) / tr_whole(K X_e)`, proton and neutron
  sectors.
- **P3, Hecke symmetriser.** `X_N` replaced by `X_N · Σ_{w ∈ S₃} T_w` (reduced-word lifts, six
  terms), sector mixed average, divided by `⟨X_e⟩`.

Pass: exactly `12` for all `q`. Reported also at `q = 1`. Nothing outside this list will be run
under this pre-registration.
