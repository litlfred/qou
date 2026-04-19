# Mass-Prediction Status — 2026-04-19

Snapshot after PR #383 merge and rebase onto main (PR #385 stacks on
top).  Context: `docs/mass-1ppm-workplan.md`,
`docs/v-hat-within-level-candidates.md`,
`docs/ilp-sdp-audit.md`.

## Current ceiling

| Atom | Best pipeline                          | err     |
|------|----------------------------------------|--------:|
| D    | `unified_lift` scalar, Kähler order 0  | 0.0038% |
| T    | `unified_lift` scalar, Kähler order 0  | 0.0301% |
| 3He  | `unified_lift` scalar, Kähler order 0  | 0.0035% |

1-ppm target is ~40× beyond D (was ~200× before the gluon patch).
The 1·σ₀ gluon patch (commit `b607e3e`, 2026-04-19) dropped the
ceiling by 4.8× on D and 9.2× on 3He.

## Levers tested this session

| Lever | Tested? | Result |
|-------|--------:|--------|
| Kähler arbitrary order (intra-level q-derivatives) | ✓ | Diverges on T/3He; order 0 optimal |
| Jet scaling ℏ_q² (inter-level) | ✓ | Saturates at level 3 per geometric bound (prop:jet-tower-convergence) |
| JM cells instead of scalar V̂ | ✓ | 0.2% intrinsic ceiling; worse than scalar under production |
| Content-weighted pair V̂_{ij} | ✓ | Over-corrects 5–500× under production; structural mismatch between free and atom |
| Gram-projection of atom NF onto G-positive eigenspace | ✓ | Real Hecke products already Frobenius-valid; no change |
| Per-nucleon H_3-LP-optimal gluon | ✓ | H_3 optima don't transfer to H_{3A} |
| Full-atom LP-dual gluon search (K=5 {∅, σ₀, σ₁, L+, L−}) | ✓ | **1·σ₀ per nucleon beats 2·σ₀** uniformly on D/T/3He |
| Gluon K=9 with length-2 compositions | —  | Skipped (K=5 already shows 1·σ₀ universal) |
| Per-isotope LP-dual for magic numbers | —  | Required — not done |
| 4He full-atom gluon search | —  | Started, killed before completing |
| V̂ covariant (partition-indexed) | —  | Research-open |
| Jones–Wenzl weight | —  | User-locked out |

## What is categorically derived

**Fully first-principles (no fit parameters beyond q₀ and CODATA
m_p, m_n, m_e):**

- **Mass ratios** from q₀ (e.g. m_μ/m_e from the vertex algebra
  structure) — `mass-endomorphism.witness.json`.
- **Q-values** as mass differences via Δnet × E_0 — single
  archimedean calibration E_0 = 0.782 MeV = m_n − m_p − m_e
  (β-decay Q; `prop:categorical-mass-markov`).
- **Brane-tower structure** — three sums (descended, single-gen,
  pair) with weight z² on the pair term proved universal by
  `thm:markov-trace-factorization`.
- **Geometric-series tail bound** (`prop:jet-tower-convergence`,
  committed this session) — truncation error
  ≤ Δmax · ℏ_q^{2(N+1)} / (1 − ℏ_q²), conditional on the
  boundedness of Δ^{(n)}.
- **Frobenius positivity of real Hecke products** — verified
  numerically on all 82 isotopes; real braid products
  automatically satisfy xᵀGx ≥ 0.

**Derived but with implicit choices:**

- **Plancherel weight** w_λ = d_q(λ)² / [n]_q!.  This is the
  character-sum convention used for the atom Markov trace.  At q ≠ 1
  it does NOT satisfy the canonical Markov axioms (M2) with the
  Jones parameter z; the axiomatic trace (`markov_trace_canonical`)
  differs by ~70% on D.  The pipeline uses Plancherel for
  performance; canonical is used where feasible.
- **Wedderburn block weights** W_SYM, W_STD, W_ALT in
  `hecke_core._chain_V_full` — derived from the three-irrep
  decomposition of H_3(q) but with a specific normalization choice.
- **Kähler lift to order 2** — the symbolic q-derivative expansion
  is derived, but truncation at a specific order is a choice.

## What is guessed / chosen / untested

- ~~**Uniform 2·σ₀ gluon per nucleon** in `hecke_core.nucleon_gen_chains`~~
  **LANDED in commit `b607e3e` (2026-04-19).**  Patched to 1·σ₀.
  Empirical gain: D 4.8×, T 2.0×, 3He 9.2×.  See ceiling table above.
- **H_3-level quark-pair gluon type** (σ₀ vs σ₁ vs L±).  Per
  `integer-lp-gluon.py` the H_3 LP says 2·σ₀ for proton and L+L−
  for neutron.  Neither transfers cleanly to atom level.
- **Per-isotope LP-dual candidate set at magic numbers**.  All my
  atom-level searches use the H_3 LP-dual set uniformly; the
  H_{3A} LP-dual could differ at N or Z ∈ {2, 8, 20, 28, 50, 82, 126}.
- **Jones–Wenzl canonical Markov weight** vs Plancherel.  User
  locked out of testing JW in this session; revisit if
  Plancherel residuals prove rate-limiting for heavy atoms.
- **m_pp / m_pn / m_nn inter-nucleon crossing counts**.  Default
  (1, 1, 1) from `confinement-level-walk.witness.json`; the atom-
  level LP-dual would select these per isotope.
- **Gluon length** (how many crossings).  The ratio probe showed
  `free ∼ 0.5 · scalar, atom ∼ 10⁻³ · scalar` suggests the bare
  atom braid has gluon-count that's different from the free
  chain — i.e., gluon count should itself be A-dependent.
  Untested.

## What remains to explore

**High-leverage, concrete:**

1. **Patch `nucleon_gen_chains` to 1·σ₀**.  Propagates ~0.04%
   improvement to every downstream script.  Straightforward but
   touches a large amount of witness output.
2. **4He gluon search** (K=5, 625 combos, ~50 min cold / ~5 min
   warm cache).  First double-magic test of the per-isotope LP-
   dual picture.
3. **6Li / 9Be gluon search** (K=5, 3125 / 15625 combos).
   Requires offline seminormal cache for n=18 / n=27.  Testable on
   doubly-magic questions only at 4He in our range.
4. **Per-isotope LP-dual derivation** at magic N/Z.  A scaled-
   down H_{3A} LP over an irrep-filtered basis could give the
   correct candidate set without building the full Gram.

**Research-open:**

5. **Covariant / partition-indexed V̂**.  Defers the Plancherel
   sum past Φ_q, potentially avoiding the Kähler/content
   double-count observed in the over-correction probes.
6. **Borel / resurgent resummation of the Kähler series**.
   Addresses the divergence on T/3He at Kähler order ≥ 1.
7. **Closing `prop:jet-tower-convergence`** (proving the
   boundedness of Δ^{(n)}).

## Calibration constants

| Constant | Value | Origin |
|----------|-------|--------|
| q₀ | 1.1099785955541805 | Fit to proton/electron mass ratio (`q_parameter.py`) |
| E_0 | 0.782 MeV | β-decay Q = m_n − m_p − m_e (CODATA) |
| ℏ_q | (q−1)/q ≈ 0.0991 | Planck-q constant, derived from q₀ |
| z | 1/(q^{1/2} + q^{−1/2}) ≈ 0.4993 | Markov parameter, derived |
| m_p / m_n / m_e | CODATA 2022 | External input |
| B_AME | AME2020 | External input (binding references) |

Only q₀ is "fit" — every other quantity in the mass pipeline is
either a CODATA input or derived.

## Session open commits

- `prop:jet-tower-convergence` (`.ts/.md/.lean` triple) —
  sorry-bounded proof of geometric tail bound.
- `docs/ilp-sdp-audit.md` + `docs/v-hat-within-level-candidates.md`
  + `docs/mass-1ppm-workplan.md` (this note).
- Engine: `sdp_moment_lift.py`, `confinement_sdp.py`,
  `sdp_lift_audit.py`, `v_hat_pair_ratio_probe.py`,
  `v_hat_gram_projection_probe.py`, `binding_full_jm_cells.py`,
  `binding_full_content_pair.py`, `atom_sdp_gluon_search.py`.
- LP scripts with SDP-lift trailers (6 files).
