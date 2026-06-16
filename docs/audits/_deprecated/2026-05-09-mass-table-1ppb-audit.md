> **DEPRECATED on 2026-05-24.** Point-in-time status / workplan snapshot; the plan has been executed or the status superseded by later audits + integrated into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T3 for the deprecation rationale.

# Mass-Table 1ppb Audit — 2026-05-09

**Goal:** 1 ppb computational accuracy on derived nucleon / light-isotope
predictions. **First target:** the 500ppb proton mass defect.

**Witness data freshness:** primary witnesses regenerated 2026-05-06 18:36 UTC
(commit `52302c5` after PRs #534 / #547 merge). The 544k ppb proton signal IS
present in the latest data — **no rerun required** before action; rerun *after*
each phase to measure delta.

---

## 1 — Most Recent Mass / Binding-Energy / β-decay Table

Six lowest isotopes plus proton, neutron. Predicted vs experimental, in MeV
unless otherwise marked. β-decay column shows whether the channel is open and
whether Q_β is derived (no derivation; author has declined).

| # | Isotope | A | Z | N | Predicted (MeV) | Experimental (MeV) | Δ (ppb) | β-decay | Source |
|---|---------|---|---|---|-----------------|--------------------|---------|---------|--------|
| 0 | proton (¹H) | 1 | 1 | 0 | M = 937.76153 | M = 938.27209 | **+544,145** (M) | stable | proton-mass-50dps.derivation.json |
| 0' | proton (audit lift, f64 assembly) | 1 | 1 | 0 | — | — | **+14** (M) | — | low-isotope-mass-table-precision-audit.witness.json |
| 1 | neutron (n) | 1 | 0 | 1 | M (chain) | M = 939.56542 | (in lift) | β⁻, Q_β=0.7823 MeV FLAG | mass-table-best.witness.json |
| 2 | deuteron (²H) | 2 | 1 | 1 | B = 2.2488 | B = 2.2246 | **+10,903** (B, +1.09%) | stable | mass-table-best.witness.json |
| 3 | tritium (³H) | 3 | 1 | 2 | B = 8.4686 | B = 8.4818 | **−1,556** (B, −0.156%) | β⁻, Q_β=0.0186 MeV FLAG | mass-table-best.witness.json |
| 4 | helium-3 (³He) | 3 | 2 | 1 | B = 7.4889 | B = 7.7180 | **−29,686** (B, −2.97%) | stable | mass-table-best.witness.json |
| 5 | helium-4 (⁴He) | 4 | 2 | 2 | B = 29.956 | B = 28.296 | **+58,666** (B, +5.87%) | stable | mass-table-best.witness.json |
| 6 | lithium-6 (⁶Li) | 6 | 3 | 3 | null | B = 31.994 | n/a (−2.08e6 in audit lift) | stable | mass-table-best.witness.json |

**Legend:** M = total mass-energy, B = binding energy. Sign: positive = predicted high.

**Why two proton rows:** the f64 audit-lift assembly closes the proton at 14 ppb
*because* its inner Φ_q tower is calibrated against CODATA at the f64 mantissa
floor; the 50 dps derivation chain — which is the algebraic primary — exposes
the 544,145 ppb defect in the underlying empirically-fitted Φ_q tower. The
14 ppb is therefore an artefact of the calibration step, not a derivation. **The
544 kppb is the real signal.**

**Witness rerun verdict:** **NO** rerun required. The latest data captures the
signal. After each implementation phase (1→8), re-emit the affected witnesses
to measure delta against this snapshot.

---

## 2 — Survey of Last 10 Days of Commits (improvements to accuracy / speed)

**Range:** 2026-04-29 → 2026-05-09 (≈80 commits). Categorised by where each
sits relative to a 1 ppb improvement vector.

### Direct precision lifts (incremental dps / mantissa)
- `57a6f2f` — Preserve 50-dps precision in T4 q-factorial + Δ_n²
- `dbaf2aa` — WitnessBuilder + label fixes + dim semantics (Copilot PR #548)
- 60+ commits refreshing `*-mpfr-50dps.witness.json` after rebases

### Algebraic / closed-form upgrades (replace fitted with derived)
- `26851cb` — Symbolic Markov-trace closed form via axiomatic reduction
- `750ed1a` — Formal equivalence proof: `y_λ(q)` ↔ `tr_M` algorithms
- `94664d4` — Finding: `leading_coef = +2^A` (PR #546's `−1/8` falsified — substantive)

### Infrastructure / orchestration (speed, witness coverage)
- `2571ac8` — Strategy-3 atomic-braid mass table — first run + audit
- `0eb9851` — Workplan: refocused 1-ppb plan, conjecture audit
- WitnessBuilder.wrap_legacy adoption across multiple compute scripts

### Critical observation
**No commit in the 10-day window touches the SCRIPT_CITED → DERIVED frontier
on Terms 2–6** of the unified mass formula. Every commit is *measurement
infrastructure* (better witnesses, tighter mantissa, cleaner orchestration),
not *derivation closure*. The proton 544 kppb defect lives in the
SCRIPT_CITED layer that has not received a single closure commit in 10 days.
**This is exactly the bottleneck.**

### Compute-speed wins available now (logged but not landed)
- Cemetery filter ports to `universal-ilp.py`, `ch-bond-writhe-lp.py`,
  `h2-integer-lp.py` — TODO from PR #608
- `lp_dual_witness_validator` promotion `--strict-wired` → default-strict
- Geck-Pfeiffer Rust port (Phase B.1 from #522): sympy OOMs at n≥14, MPFR
  Hoefsmit times out at n≥11 — **gates A≥5 reachability entirely**

---

## 3 — Per-Element Error Breakdown + Script Audit

For each isotope, the dominant error source maps to a specific computational
artefact. **FLAG = fitted / numerology / empirical / calibrated / SCRIPT_CITED —
flagged for fix to reach 1 ppb.**

### Proton (1H) — 544,145 ppb [PRIMARY TARGET]
Step-by-step of `proton-mass-50dps.derivation.json`:

| Step | Output | Trust | Flag |
|------|--------|-------|------|
| 1. tr_M(p, q₀) at 50 dps via Markov-trace assembly | 2.12258250945273 | DERIVED (PR #480) | OK: clean |
| 2. Terms 2–6 (Phase-A precision lift) | terms_50dps | SCRIPT_CITED | no |
| 2a.  Φ_q tower formula | inner | empirically fitted | FLAG `mass_endomorphism.py:5,26` admits ~1.8% error |
| 2b.  Φ_q infinite-product truncation | inner | no closed-form bound at proton scale | FLAG `mass_endomorphism.py:80-95` |
| 2c.  per-block Φ_q refactor | NOT deployed | — | FLAG available in `per_block_phi_q.py`, not wired |
| 2d.  Euler-series Φ_q | NOT deployed | — | FLAG `d_phi_q_series.py` only on deuteron |
| 3. m_p_Hecke 4-term tower | 1.4283 | SCRIPT_CITED | FLAG `proton_mass_tower_derivation.py` |
| 4. m_e_Hecke | (hidden) | SCRIPT_CITED | no |
| 5. ratio → MeV | 937.7615 | SCRIPT_CITED | no |

**Cause:** A=1 brane tower is empty (PR #533 finding), so the additive
correction = 0; ALL proton error lives in the Φ_q tower closure inside Terms
2–6. Convention diagnostics confirmed:
- OK: Hoefsmit vs markov_peel agree to 2e-16 (sub-ULP at 50 dps) — NOT a
  Markov-Wenzl-vs-Plancherel convention bug
- OK: q₀ uniform across all proton scripts (1.1099785955541805) — NOT a q₀
  drift
- OK: q₀ stable to 2000 dps via extended PSLQ — NOT q₀-precision

**Conclusion:** the 500 ppb is an **empirical-fit residual** in the Φ_q tower.

### Neutron (n)
Same chain skeleton as proton (A=1 → empty brane tower). Q_β=0.7823 MeV is
the β⁻ decay parameter; **author has declined to derive Q_β** — sets a 780 ppb
floor on β-chain calibration regardless of substrate work.

### Deuteron (²H) — +10,903 ppb on B
- FLAG `d_phi_q_series.py:259` — `u^shift = u^(18Z+21N+1)` marked
  **EMPIRICAL CONJECTURE**
- FLAG `jsj_atom_volume.py:195` — B(D)=2.22 MeV **fitted**, n_pairs(D)=1
  hardcoded
- 11 SCRIPT_CITED weight steps in the n=6 per-λ Wedderburn weight chain
  (PR #605 deuteron chain)

### Tritium (³H) — −1,556 ppb on B
- Plan-G readiness: α* = 0.424 (largest gap). **Structural review needed**
  before tr_M work — `docs/plans/G-status-and-narrowing.md:10`
- B_5 Hoefsmit at H_9 **deferred** in `r5_full_canonical_knot_solver`
- τ̂_0 generalisation H_3 → H_9 **not implemented** (Phase A.3' from #522)
- Q_β = 0.0186 MeV — β⁻ chain FLAG (Q_β not derived)

### ³He — −29,686 ppb on B
- 5 of 7 blocks fail PSD; only ³He has α* = 1.000 unblocked
- Habiro tail validator does **NOT** cover ³He (only p, n, D)
- L_{6a4} / 8_{11} explicit braid identification at H_9 **open from #604**

### ⁴He — +58,666 ppb on B
- frobenius-codim n≥6 → FLAG **opaque fallback**
  (`frobeniusCoCasimirTraceFallback`, `knot-mass-formula-unified.lean:36`).
  This is the **T1 bottleneck** — n=2..5 closed by `rfl` via Fin enumeration
  in `frobenius-codim-universal.lean`; n=6 has 11 partitions, n=7 has 15
- Habiro reconstruction at A=4 **not validated** (only p, n, D in current
  witness)
- Per-block Φ_q at A=4 **not deployed**

### ⁶Li — null prediction (audit lift: −2.08e6 ppb)
- K_11a259 atlas constant at ~5 sig figs — **deprecated volume-match
  methodology**
- High-precision Vol(K_11a259) at 50 dps **not yet computed**

### Beta-decay channels
| Isotope | Channel | Q_β (MeV) | Status |
|---------|---------|-----------|--------|
| neutron | β⁻ → p | 0.7823 | FLAG Q_β not derived (780 ppb floor) |
| ³H | β⁻ → ³He | 0.0186 | no |
| (others stable in this table) | — | — | — |

σ_shell calibration via AME data — long-pole **P8** (per workplan); doesn't
reach 1 ppb in any near-term plan.

---

## 4 — Numerology / Fitted / Empirical / Calibrated Flags (cross-checked across all 6 elements)

Master inventory of every flag emitted by scripts in the proton + light-isotope
chain. **Each row is a 1 ppb blocker** until promoted to DERIVED.

| File:line | Flag type | Affects | Priority |
|-----------|-----------|---------|----------|
| `mass_endomorphism.py:5,26` | empirical fit (Φ_q tower, ~1.8% admitted) | p, n, all A | **P0** |
| `d_phi_q_series.py:259` | EMPIRICAL CONJECTURE (u^shift = u^(18Z+21N+1)) | D, T, ³He | **P0** |
| `n_sym_w2_retraction.py:15,55,107` | numerology / point-fit (W-2 ansatz) | all | **P1** |
| `jsj_atom_volume.py:195` | fit to B(D)=2.22 MeV | D | **P1** |
| `ocneanu_cancellation_derivation.py:266` | empirical_cross_partition_cancel | all chains | **P1** |
| `build_atom_tr_M_chains.py:18,135,156,180,201,215` | SCRIPT_CITED frontier | all chains | **P1** |
| `build_markov_trace_assembly_chain.py:24,27,125,277` | λ=(2,1) / λ=(1,1,1) weights SCRIPT_CITED | all chains | **P1** |
| `frobenius-codim-universal.lean` n≥6 | opaque fallback (`frobeniusCoCasimirTraceFallback`) | A≥4 (⁴He, ⁶Li) | **P0** (T1) |
| `MarkovTrace.lean:138` | sorry on Ocneanu-Jones-Wenzl uniqueness | substrate bridge | **P1** (T4) |
| `frobenius-antipode-lean-stub.lean:111` | opaque chiralityFactor (not q^writhe) | axial-coupling | **P2** (T6) |
| Q_β derivation declined | author rule | β chains | **floor** (780 ppb) |
| K_11a259 atlas constant | 5 sig figs, deprecated | ⁶Li | **P1** |
| q₀ CODATA anchor (m_μ/m_e ± 22 ppb) | calibration-floor | all | **structural floor** |

**P0 — primary targets to break the 500 ppb floor immediately:**
1. `mass_endomorphism.py` Φ_q tower → derive via per-block + Euler-series (root-cause diagnostic)
2. `d_phi_q_series.py:259` `u^shift` → upgrade conjectural exponent to derived
3. `frobenius-codim-universal.lean` n=6, n=7 → close mechanically (T1)

**P1 — required to push toward 1 ppb across all six isotopes**
**P2 — polish residual coupling-constant sites**
**Floor — q₀'s 22 ppb CODATA-anchored uncertainty.** Without a
non-CODATA-anchored derivation of q₀ (topological identity, modular-form PSLQ,
or substrate fixed-point proof), 1 ppb on derived predictions is structurally
impossible. Documented in `q_parameter.py:21-25`.

---

## 5 — Action Queue (ordered by ROI per agent-session)

Per the approved plan, T1→T3→T2→T5→T4→T6 with proton-first interleaving.
Phase numbering matches `/root/.claude/plans/lots-of-new-math-parallel-lagoon.md`.

| Phase | Task | Target ppb impact | ETA |
|-------|------|-------------------|-----|
| 0 | This audit doc | (documentation) | done |
| 1 | Proton root-cause: per-block + Euler-series Φ_q in proton chain | drops 544 kppb to TBD | ~4h |
| 2 (T1) | Close `hecke_n6_frobenius_codim`, `hecke_n7_frobenius_codim` | binding-energy floor → < 5 ppb | ~3h |
| 3 (T3) | `cross_check_trM_1ppb` at 60 dps + ⁴He/⁶Li/¹²C | measures T1 + finds algebraic-bridge breaks | ~2h |
| 4 (T2) | Wire LP `active_set` into `atomic_braid_mass_table` | suppresses 22 ppb noise | ~1d |
| 5 (T5) | Habiro tail validator A∈{3,4,6} | localises ⁴He algebraic break if any | ~½d |
| 6 (T4) | Discharge `MarkovTrace.lean:138` sorry | closes substrate bridge | ~4h |
| 7 (T6) | `chiralityFactor → q^writhe` | residual coupling polish | blocked on `BraidWriThe` |
| 8 | KLR substrate (3 props + crystal pruning + ℤ-grading) | structural correctness | multi-PR |
| Long-game | q₀ derivation from non-CODATA invariants | breaks the 22 ppb structural floor | research |

---

## 6 — Cross-Reference Index

**Witnesses cited:**
- `computations/proton-mass-50dps.derivation.json`
- `computations/mass-table-best.witness.json`
- `computations/low-isotope-mass-table-precision-audit.witness.json`
- `computations/mass-formula-6term-mpfr-50dps.witness.json`

**Scripts cited:**
- `computations/mass_endomorphism.py`
- `computations/_phi_q_util.py`
- `computations/d_phi_q_series.py`
- `computations/per_block_phi_q.py`
- `computations/proton_mass_tower_derivation.py`
- `computations/cross_check_trM_1ppb.py`
- `computations/substrate/q_parameter.py`
- `computations/lp_dual_solver.py`
- `computations/atomic_braid_mass_table.py`
- `computations/habiro/habiro_witness_validator.py`
- `computations/build_atom_tr_M_chains.py`
- `computations/build_markov_trace_assembly_chain.py`
- `computations/n_sym_w2_retraction.py`
- `computations/jsj_atom_volume.py`
- `computations/ocneanu_cancellation_derivation.py`

**Lean files cited:**
- `content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.lean`
- `content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.lean`
- `content/quantum-observable-universe/braids-and-knots/frobenius-antipode-lean-stub.lean`
- `content/quantum-observable-universe/lean/QOU/Hecke/MarkovTrace.lean`

**Plans cited:**
- `docs/plans/G-status-and-narrowing.md`
- `/root/.claude/plans/lots-of-new-math-parallel-lagoon.md` (the approved plan)
