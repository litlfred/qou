# Workplan — Mass prediction at 1 ppm

**North-star goal:** mass-prediction error ≤ 1 ppm across the isotope
table (AME2020 reference).

**Current ceiling:** 0.018 % on D (unified_lift order 0), 0.06 % on T,
0.03 % on 3He (`computations/unified_lift.py`).  The
JM-cell path (`syt_cell_tower.py`) peaks at 0.10 % on D, 0.28 % on T
and 0.22 % on 3He — slower asymptote than unified_lift on light
nuclei but no Kähler-tower dependence.  Both are ~200× off the 1-ppm
target.

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
  batches, persist to `computations/.cache/seminormal/`.
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

3. **Kähler tower to arbitrary order — DONE, NEGATIVE RESULT.**
   `unified_lift.py` now supports arbitrary order n via the Euler-
   operator exponential `exp(ℏ_q · θ) (z·V̂)`, θ = q·d/dq.  Empirical
   sweep orders 0–5 on D / T / 3He:

   | Atom | order 0 | order 1 | order 2 | order 3 | order 4 | order 5 |
   |------|--------:|--------:|--------:|--------:|--------:|--------:|
   | D    | 0.018%  | 0.022%  | 0.024%  | 0.024%  | 0.023%  | 0.023%  |
   | T    | 0.060%  | 0.776%  | 3.031%  | 4.552%  | 5.109%  | 5.242%  |
   | 3He  | 0.032%  | 0.828%  | 3.498%  | 6.002%  | 6.955%  | 7.203%  |

   **The series diverges on T / 3He.** Order 0 is already optimal
   (also for D, where higher orders drift slightly).  The formal
   ε_MeV bound (1.4 keV → 1.4 μeV) contradicts the actual error —
   the bound is wrong.  Arbitrary-order Kähler is therefore **not a
   knob for reaching 1 ppm**.

   Revised picture of this lever: stop at order 0 for A ≥ 3, or
   find a Borel / resurgent resummation that reorganises the
   asymptotic series.  The latter is an open research question
   rather than an engineering task.

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

## Prioritisation (revised post-session)

P1 is a prerequisite for every heavy-atom improvement.  Within P2:

1. **Gluon LP → full SDP** (~1 MeV expected gain on D).  Highest
   leverage.  Session probe confirmed per-nucleon H_3 optima do NOT
   transfer; full-atom H_{3A} SDP (P2.1b) to be done on this branch
   (no separate fork per user decision 2026-04-19).
2. **ILP/SDP audit** — DONE (`docs/ilp-sdp-audit.md`).  Six LP(PSD)
   files identified as SDP-in-disguise.
3. ~~**Arbitrary-order Kähler**~~ — DONE, NEGATIVE RESULT.  Series
   diverges on T / 3He; order 0 is optimal.  Not a 1-ppm lever.
4. ~~**Jet scaling (brane tower)**~~ — SATURATED.  Per-level
   damping matches the predicted ℏ_q² ≈ 0.0098, loop terminates
   at level 3 already below ppm target.  The 0.018% / 0.06% /
   0.032% residuals on D / T / 3He are STRUCTURAL to the V̂
   model within a level — not from truncating the jet sum.
   See `unified_lift.py` jet-log in the witness.
5. **E_0 unified sanity check** (diagnostic only; no per-atom fit
   per user decision).

## Levers ruled out this session

Both intra-level and inter-level perturbative knobs are exhausted:

- **Kähler orders** (intra-level q-derivatives): diverge on T / 3He.
- **Jet levels** (inter-level ℏ_q² scaling): converge at level 3;
  residuals persist.

Next frontier is therefore the V̂ model itself — the per-jet-level
aggregated volumes.  P2.1b (full-atom SDP for gluon decoration) is
the only remaining structural lever identified in this session; it
will need a separate fork per the user plan.
