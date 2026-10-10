---
# pyhk
title: pyhecke_native BUILDS in the web sandbox (≈42s) — q-deformed compute unblocked
status: completed
type: task
priority: normal
created_at: 2026-06-20T00:35:00Z
updated_at: 2026-06-21T19:39:07Z
---

User pick (option 2, "2 y"): build pyhecke_native to unblock the keystone q-deformed shift.

## Result (2026-06-20) — built + validated; pending human close

Finding: [`docs/audits/2026-06-20-pyhecke-native-build-unblocked.md`](../docs/audits/2026-06-20-pyhecke-native-build-unblocked.md).

- **Corrects a standing belief**: the PyO3/maturin chain WAS thought unavailable in
  the web sandbox (Stage-B scope §"Infra blocker"). It is NOT — cargo/rustc 1.94.1
  are on PATH, `pip install maturin`, `maturin build --release -m
  tools/pyhecke-native/Cargo.toml` builds the wheel in ≈42s (rug compiles GMP+MPFR
  from source via cc; no clarabel-lp feature needed).
- **Validated 1e-15**: pyhecke_native Rust Hoefsmit χ on the Borromean braid matches
  my independent sympy H₃ rep on all 3 blocks (cross-confirms both the wheel and the
  h⁴-in-(2,1) localization). `docs/audits/scripts/pyhecke_native_h3_crosscheck.py`.
- **H₅ reachable**: `trace_weights_n(5,q₀)` gives the muon (3,2)=0.0617 / electron
  (3,1,1)=0.0168 block weights; `lagrange_projectors_mpfr` (the E_λ projectors §4
  needs) + `chi_lambda_braid_mpfr` all available.
- **Unblocks**: Hoefsmit Stage-B cross-anchor probe, the keystone q-deformed shift,
  ~15 importers. Added correction banners to the Stage-B scope doc + (earlier) the
  synthesis doc.
- **Discipline**: the keystone shift is now compute-ready but NOT well-posed (open
  structural inputs: which H₅ braid, E_λ-on-knot-module action). Do NOT hunt
  1.000000210 — the 210 ppb is a re-pin artifact; the next step is a bar-even,
  anchor-stable structural derivation, not a fit.
