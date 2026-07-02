# λ_A excision — consumer lane classification (execution ledger)

**Parent ruling:** [`2026-06-24-lambda-a-fit-excised-per-knot-density.md`](2026-06-24-lambda-a-fit-excised-per-knot-density.md)
(λ_A is a CODATA-implied fit — excised; absolute mass routes through the
muon-anchored [`canonical_mass.py`](../../computations/canonical_mass.py) facade;
per-knot `vol_density_per_block` is valid for **binding/ratios only**).

**Bean:** `4f2d` (λ_A excision: per-knot Hecke density across QOU).
**Branch:** `claude/4f2d-lambda-a-excision-672zpe`.

## Why the previous attempt stalled (bean `0voz`)

`0voz` framed the excision as a uniform swap
`vol_density_borromean → vol_density_per_block` across ~64 scripts. Per the
🔵 CORRECTION in the parent ledger, that swap is **wrong for absolute mass**
(m_p ≈ 406 MeV, −57%): the per-knot density fixes the *density*, but the
`1/ℏ_q²` still lands on `Vol(𝓑₃)` instead of the muon anchor `Vol(4₁)`.
The blind swap broke every absolute-mass producer, so the migration stalled.

The unblocker is a **per-file lane classification**: each consumer gets the
replacement appropriate to what it computes, and files that reference λ_A
*in order to document or refute it* keep the reference.

## Lanes

| Lane | Meaning | Action |
|------|---------|--------|
| `INFRA` | defines / re-exports the deprecated functions | keep (deprecation warnings already in place) |
| `AUDIT-KEEP` | audits / probes / refutations *about* λ_A or global-vs-per-knot | keep — the reference is the subject |
| `ABS-MASS-MIGRATE` | computes an absolute mass (MeV) via the λ_A path as a live input | route through `canonical_mass.proton_mass_mev` / `neutron_mass_mev` / `nucleon_mass_mev` |
| `BINDING-OK` | density used only where scale cancels (binding / trace ratios) | `vol_density_per_block` (per-knot `tr_M(K)`) |
| `GATED` | GAP-A-4 per-knot absolute-density frontier probes | **do not touch** (owner-gated; "no seventh fit ansatz" stands) |
| `DOC-ONLY` | name appears only in comment / docstring / deprecation notice | no action |

## Classification table

*(populated from the per-file classification pass — pending)*

## Migration log

*(one entry per migrated file: old call → new call, verified value vs oracle
`canonical_mass.proton_mass_mev() ≈ 938.272 MeV` / `neutron_mass_mev() ≈ 939.565 MeV`)*
