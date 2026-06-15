# Compute partial-wiring & optimization audit — where we fall back to non-canonical, and why we miss things (2026-06-15)

**Branch:** `claude/vigilant-brown-x0tzat` (PR #2325)
**Scope:** read-only audit (background `Explore` agent + this session's findings).
**Trigger:** owner — *"where do we have only partial wire-up of compute / fall back to non-canonical? … also it seems like you may not be using computational optimizations."*

## The meta-pattern (the answer in one sentence)

The canonical *exact* pipeline exists — **Rust trace engine → exact `tr_M` → `B_sym`
(Kashaev log-trace) → derived corrections** — but production repeatedly **falls back
to proxies** (linearized `B_pred`/`B_lin`, proved-only linking weight, q-CLT
extrapolation, pure-Python-slow → timeout-truncated tables). We then measure
residuals *against the proxy*, which manufactures artifacts. **This session's
q₀⁵-per-site "law" was exactly that** — a residual of `B_pred`, dissolved by `B_sym`.

## A. Binding-form fallback (the root of the session's confusion)

1. **`B_pred`/`B_lin` (linearized) is the production binding reference, not `B_sym`
   (exact log-trace).** Per-site q₀-exponent measures the gap to *whichever* form
   you reference: **5.00 vs `B_pred`**, **≈0–1 vs `B_sym`** (this PR's
   measurement). So the "fundamental" Δ_λ exponent is a `B_pred` artifact.
2. **The deuteron binding `B(D)≈2.224 MeV` has NO live producer** — its cited script
   `atomic_frobenius_codim.py` is in `_deprecated/` (compute-integration-watcher
   queue `lem:deuteron-binding-energy`). Same for
   `prop:derived-mass-formula-light-isotopes` (`derived_only_formula.py` dead) and
   `prop:mass-formula-regime-switching` (`d_chirality_probe.py` dead).
3. **Δ_λ closure is gated** — 6 ansätze failed; no derived Δ_λ → production binding
   can't use it (the keystone). The whole `B(K)=m_e·Σ y_λ χ^λ Δ_λ` path is stalled.

## B. Proven-in-Lean but NOT probed (the I1 gaps — 7 queued)

The `compute-integration-watcher` queue lists 7 real unwired theorems, headed by:
- **`prop:hecke-mass-trace`** — the **central mass = Markov-trace bridge**, *the*
  link between the algebraic Hecke element and the mass observable — **unprobed**
  (only mention is a README). The whole mass pipeline lacks a certified entry point.
- **`prop:neutron-proton-mass-splitting`** — `.md` cites a witness that *does not
  exist*; part of the L2-failing Q_β/m_n/Δ_pn trio.
- **`prop:neutron-prediction-comparison`** — Lean validation is *vacuous* (closes the
  existential with `n_obs := n_pred`, discrepancy 0); no real AME-2020 comparison.
- + `derived-mass-formula-light-isotopes`, `mass-formula-regime-switching`,
  `borromean-hopf-energy-crossover`, `eos-borromean-cfl` (author analytic-vs-probe).

## C. Calibration opacity (3-CAL purity not machine-verifiable)

- **53 free-floating CODATA literals** (938.272 / 939.565 MeV, …) outside
  `codata_constants` (P31) across `atomic_mass_via_rho_k.py`, `binding_K_direct.py`,
  `binding_canonical.py`, `canonical_tower.py`, … — inflates the calibration count.
- **51 scripts over-count** as "4-input m_p AND m_n" instead of deriving
  `m_n = m_p + Q_β` (one derivation, not two anchors).
- **117 scripts use hyperbolic volume as a *fitted* parameter** (owner-deferred
  until `R(K)` is derived — not a violation, but a known non-derived shortcut).

## D. Computational optimizations not used (your second question — confirmed)

1. **The Rust trace engine (`pyhecke_native`/`hecke-engine`) was NOT installed** in
   this sandbox → trace ran **pure-Python**, timing **doubling per nucleon**
   (⁴He 0.1s → ⁹Be 24s; A≥12 timed out). **Fixed this session:**
   `maturin build --release` + pip install → `pyhecke_native` 0.9.0 now available.
2. **`BlockCache` wiring gap** — ~21 Hoefsmit callers still do O(d_λ²) full assembly
   instead of the shared block cache (compute-audit P21; ~15–30 % on H_9+).
3. **`LaurentQ` underdeployed** (P17) and **`sympy.simplify` in hot loops** (P16,
   976 occurrences — cosmetic before `evalf` at q₀ can cost 10–30 min/atom).
4. **Good news:** all 7 catalogued **FFI round-trip** offenders are already
   discharged (ffi-roundtrip-audit, 2026-05-29).

## E. Provenance / staleness debt

- **133 scripts emit `*.witness.json` without `WitnessBuilder`** (P30) → fragile
  staleness detection (missing `engine`/`scriptFile`/`commitSha`).
- Recurrent witness drift (q0-repin staleness; schema `data:[]` vs top-level rows).

## Highest-leverage fixes (ranked)

1. **Make `B_sym` the binding reference, not `B_pred`/`B_lin`.** Dissolves the q₀⁵
   artifact; the real residual (deuteron over-binding + magic/cluster shell) is
   clean and structural (this PR's `bsym_residual_shell_structure.py`).
2. **Install/keep the Rust engine wired** (done this session) + close the
   `BlockCache`/`LaurentQ`/`simplify` gaps → unlocks heavy-A exact `tr_M` (¹⁶O
   magic test, un-degraded mass tables).
3. **Wire `prop:hecke-mass-trace`** (the central bridge) + revive the dead binding
   producers (deuteron, light-isotope formula) with live probes.
4. **Consolidate the 53 CODATA literals + 51 over-counts** into the registry so
   3-CAL purity is auditable.

## Caveat

This is a *map*, not a fix list executed. Some agent-surfaced magnitudes
(e.g. "~500 MeV binding error") are not independently verified here and are
omitted; the queue-/witness-grounded findings above are the load-bearing ones.
