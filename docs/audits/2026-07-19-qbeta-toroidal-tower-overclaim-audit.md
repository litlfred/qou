# Q_β toroidal-tower over-claim + production-wiring audit (2026-07-19)

## Summary

`derived_masses.q_beta_toroidal_mev()` — an N=4 fixed-real-coefficient
Q_β tower `Q_Tor = Q_N1·(1 − u² − 2u³ + 2u⁴)`, `u = b·ℏ_q²` — carried two
distinct defects, both now fixed on branch
`claude/toroidal-tower-audit-kv0wjw`:

1. **Docstring over-claim (Pattern A).** The docstring called the tower
   "exact Toroidal Harmonic basis", a "rigorous Toroidal projection", and
   asserted the coefficients `(c_2=−1, c_3=−2, c_4=+2)` "correspond exactly"
   to the Parabolic-Cylinder limit. Per
   [`ck-dk-canonical-registry.md §3`](../coordination/ck-dk-canonical-registry.md):
   - `c_2 = −1` — PROVED, Taylor-exact, anchor-stable (the **only** canonical rung).
   - `c_3 = −2` — EMPIRICAL, **REFUTED as a real-q fibre element**
     (~2.6–3% cross-anchor swing; `dc_3/dq ≈ 4.6×10⁶`; no fixed real `c_3`
     holds across anchors — `SRigidityPrune`).
   - `c_4 = +2` — a Parabolic-Cylinder ansatz **estimate**; the registry's
     CODATA-residual fit for `c_4` is `−0.97157` (itself a fit/artifact),
     which disagrees with `+2` — so `+2` is not derived either.

2. **Live production-wiring violation (Pattern B).** The tower was imported
   into `canonical_mass.py::_from_formula()` as the m_n fallback
   (`m_n = m_p + q_beta_toroidal_mev() + m_e`), despite the 2026-07-06
   ruling (verdict:105) "**Do not re-wire `q_beta_toroidal_mev` into
   `canonical_mass.py`**". Worse, the fallback's Q_β
   (`0.7823334279…`) *diverges* from the canonical witness Q_β
   (`0.7823343865… = q_beta_kashiwara_n2_mev`) — so the silent fallback
   would have returned a **non-canonical** m_n whenever the witness was absent.

## Resolution (owner directive: "canonical derivation only — no silent fallback")

- **Removed `_from_formula()` entirely** from `canonical_mass.py`. The
  git-tracked substrate-identity witness (`m-p-substrate-identity-50dps.witness.json`)
  is now the **single canonical source**. A missing witness raises
  `FileNotFoundError` with a regeneration instruction — no silent
  substitution of a non-canonical value. This also removes the only
  production consumer of `q_beta_toroidal_mev()`.

- **Relabeled the `q_beta_toroidal_mev()` docstring** honestly: PROBE /
  near-match, NOT canonical, NOT wired to production, with the per-rung
  tiers above. The function is retained for comparison only.

## Verification

- `canonical_mass.proton_mass_mev()` → `938.2720894273…`,
  `neutron_mass_mev()` → `939.5654227645…` — both equal the canonical
  witness `predictions` to <1e-9 MeV.
- `prediction_uncertainty_ppb` unaffected (it independently uses
  `q_beta_kashiwara_n2_mev`).
- `grep q_beta_toroidal_mev` over `*.py`: no remaining production consumer
  (only the definition + `__all__` export in `derived_masses.py`).

## Cross-refs

- Registry: [`ck-dk-canonical-registry.md §3`](../coordination/ck-dk-canonical-registry.md)
- Q_β c_k truncation-order framing:
  [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- c_3 cross-anchor rigidity falsification:
  [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)
