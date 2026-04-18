# Workplan — Mass prediction at 1 ppm

**North-star goal:** mass-prediction error ≤ 1 ppm across the isotope
table (AME2020 reference).

**Current ceiling:** ~0.1 % on D / T / 3He via the SYT-cell JM tower
(`folio-assistant/computations/syt_cell_tower.py`, Track 1 of the
previous guidance).  That's ~1000× off target.

## Milestones

| Stage | Target      | Light-atom test | Indicator |
|-------|-------------|-----------------|-----------|
| M1    | 1%          | D / T / 3He     | current JM already ✓ (0.1–0.3%)   |
| M2    | 0.01%       | D / T / 3He     | tower + gluon + Kähler tightened  |
| M3    | 0.0001%     | D → 6Li → 9Be   | seminormal cache populated        |
| M4    | 1 ppm       | full table to Z=30 | unified E_0, no per-atom drift |

## Phase 1 — unblock heavy-atom evaluation (P0)

The JM tower at n = 18 (6Li) is infeasible cold because
`build_seminormal_matrices` for dim ~6k partitions runs 5–10 min each
and there are ~385 partitions.  Without this the AME test (6Li / 9Be /
12C) cannot start.

Tasks:

- **P1.a** Offline-precompute seminormal matrices for n = 18 in
  batches, persist to `folio-assistant/computations/.cache/seminormal/`.
  Run as a single long-running job; resume-on-failure.
- **P1.b** Add a `--dim-cap N` audit mode to `syt_cell_tower.py` so
  the weight-dominant partitions alone give a quick estimate while
  P1.a runs in the background.  Report truncation residual per atom.
- **P1.c** Repeat for n = 27 (9Be) after n = 18 completes.  n = 36
  (12C) is parked until P2/P3 reduce the cost structurally.

## Phase 2 — structural fixes (closes M2, maybe M3)

Each of these addresses a suspected source of residual on D that was
identified in the session diagnosis:

1. **Integer-LP → SDP audit for gluon decoration.**
   Current state: `hecke_core.nucleon_gen_chains` applies a uniform
   2·σ₀ gluon tail to every nucleon.  `integer-lp-gluon.py` found the
   *per-nucleon* stable-NF optimum is proton = 1·σ₀, neutron = L₊L₋.
   These disagree.  The ILP used only Frobenius positivity (`G · NF ≥
   0`), which is the SDP feasibility predicate — so the LP is morally
   an SDP already, it just calls CVXPY's LP solver.

   Task: rewrite gluon choice as a per-atom SDP over the full 3A-strand
   Gram matrix (not H₃ only), choose gluons per-nucleon that minimise
   a physical cost functional while staying PSD.  Expect ~1 MeV
   improvement on D once the uniform gluon assumption is dropped.

2. **Full-nuclear SDP baseline audit.**
   The codebase already carries several SDP scripts:
   - `multi_level_sdp.py` — levels 3–7 PSD blocks (adjacent-pair)
   - `sdp_on_shadows.py` / `sdp_cross_channel.py` — channel PSD
   - `misdp_cross_channel.py` — MISDP joint levels

   Matching LP scripts whose PSD check is trivial (2×2 Gram) but are
   not lifted into the full SDP:
   - `integer-lp-gluon.py` (H₃ Gram), `ch-bond-lp.py`,
     `confinement-lp.py`, `atom-builder-lp.py`, `knot-operator-lp.py`,
     `molecular-*-lp.py`, `branching-lp.py`, `nuclear-binding-lp.py`,
     `nuclear_ilp.py`, `ilp-chain.py`, `h2-integer-lp.py`

   Task: per-file audit (1-line status: **LP-only / partial-SDP / full-
   SDP**) and flag those that should be upgraded.  Candidates where
   "upgrade LP → SDP" is likely to move the mass number:
   `integer-lp-gluon`, `nuclear_ilp`, `confinement-lp`,
   `knot-operator-lp`.

3. **Kähler tower to arbitrary order.**
   `unified_lift.py` hardcodes `order ∈ {0, 1, 2}`.  Each extra order
   costs another symbolic derivative but gains roughly one factor of
   ℏ_q ≈ 0.10.  On D the order-2 residual is ~1.4 keV; order-5 would
   drop it to ~10⁻³ keV, well below 1 ppm.
   Task: parametrise `unified_lift(..., order=n)` symbolically via
   `sympy.diff` so arbitrary order is a one-line change.

4. **Plancherel SYT weight μ_T kept (not Jones-Wenzl).**
   Per session decision.  Keep the current `syt_cell_tower` weight
   convention.  Noted for the workplan record.

5. **E_0 unified, no per-atom fit.**
   `E_0 = 0.782 MeV = m_n − m_p − m_e` (β-decay Q, per
   `prop:categorical-mass-markov`).  If a per-atom fit becomes
   necessary that is evidence of a missing tower order / wrong weight
   — do not accept per-atom E_0 as a fix; use it only as a diagnostic
   pointer.

## Phase 3 — content & proof alignment (parallel to P1 / P2)

- **P3.a** `mass-tower-syt-cells.md`: empirical table now links
  `thm:markov-trace-factorization` (done in this session).
- **P3.b** Once Kähler arbitrary-order lands, update
  `mass-endomorphism-jet-tower.md` to cite the arbitrary-order
  expansion (`cor:quantum-dilogarithm` already supports arbitrary
  expansion via the pentagon).
- **P3.c** If/when the integer-LP→SDP gluon step lands, promote the
  current `integer-lp-gluon` remark into a proposition with SDP
  witness and update `content-block-review`.

## Phase 4 — scale (closes M4)

Once M3 is met on 6Li / 9Be with per-atom error tracked stably:

- **P4.a** Sweep 12C, 16O (n = 36, 48) using the populated seminormal
  cache.
- **P4.b** Automate the full AME2020 comparison in
  `validate_isotope_nf_stability.py` with canonical tr_M enabled up
  to the largest feasible 3A; report per-atom residual.
- **P4.c** Unified E_0 sanity check across the table.  If drift
  remains at 1 ppm, escalate to the Jones-Wenzl weight question
  (re-opens Phase 2 step 4).

## Prioritisation

P1 is a prerequisite for every heavy-atom improvement.  Within P2:

1. **Gluon LP → full SDP** (~1 MeV expected gain on D).  Highest
   leverage.
2. **ILP/SDP audit** (map the codebase; 1 hour).
3. **Arbitrary-order Kähler** (mechanical; ~0.1 keV gain, only
   matters once P2.1 lands).
4. **E_0 unified sanity check** (diagnostic only).
