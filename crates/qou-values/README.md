# `qou-values` — Fast MPFR Proton-Pinned Witnessed-Value Evaluator & CLI

`crates/qou-values` provides a general, zero-`f64`, `>= 80`-dps MPFR (`rug::Float`) Rust library and command-line tool (`qou-values`) for instant (`< 15 ms`) evaluation of QOU's derived mathematical constants, [`ACCURACY.md`](../../ACCURACY.md) scorecard rows, and monograph `:val[...]` directives, complete with central-difference MPFR Fréchet–Jacobian calibration uncertainty propagation with respect to `(m_e, m_p/m_e, m_{\pi^\pm})`.

## Discipline & Anchor Policy

- **Zero `f64` calculations:** All internal arithmetic runs in MPFR (`>= 368` bits by default, configurable via `--dps 15..=250`). Special functions (`Vol(4_1) = 2 Cl_2(\pi/3)`, `Vol(5_2) = 3 D(z_0)`, `\mathrm{Li}_3(q_0^{-2})`, `\zeta(3)`, Catalan's `G`, Hahn–Exton `q`-Bessel `J_{1/2}`) and fixed-point cubics are solved in-process to arbitrary precision.
- **Proton-pin default (`2026-11-28` owner ruling):** `q_0^{(p)}` is solved directly from `2(\mathrm{Vol}(4_1)/\hbar_q^2)F_{\mathrm{Bor}}(q) - 12 = m_p/m_e`. The historical muon-ratio pin is gated `on_hold` unless `--allow-on-hold-muon-comparison` is explicitly passed for cross-anchor diagnostics.
- **Zero fitting:** Only `(m_e, m_p/m_e, m_{\pi^\pm})` enter as physical calibration inputs; CODATA-2022, PDG-2024, NIST, and AME2020 values enter strictly at the comparison boundary.

## CLI Quick Reference

Always build with the shared target directory and low CPU priority:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
export CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target CARGO_BUILD_JOBS=2

# 1. List all registered observables and :val[...] keys
nice -n 15 cargo run --release -p qou-values -- list

# 2. Query any observable or :val[...] key at 80-200 dps (< 10 ms once built)
nice -n 15 cargo run --release -p qou-values -- get ":val[atlas_m_mu_MeV]" --dps 80
nice -n 15 cargo run --release -p qou-values -- get alpha_em_inv_form_c --dps 120 --json
nice -n 15 cargo run --release -p qou-values -- get "t3_bond_count(56)" --json

# 3. Dump the entire scorecard & :val[atlas_*] dictionary as JSON
nice -n 15 cargo run --release -p qou-values -- all --dps 80 --json

# 4. Emit a schema-valid proton-pinned .witness.json
nice -n 15 cargo run --release -p qou-values -- emit-witness \
  --name qou-values-smoke \
  --out /tmp/qou-values-smoke.witness.json \
  --dps 80

# 5. Run the unit test suite (< 1e-48 / < 1e-75 verification against committed witnesses)
nice -n 15 cargo test --release -p qou-values
```
