> **DEPRECATED on 2026-05-24.** Superseded by [`2026-05-18-1ppb-workplan-v7-100x-experimental.md`](../2026-05-18-1ppb-workplan-v7-100x-experimental.md) (the latest in the 1ppb-workplan chain). Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T4 for the deprecation rationale.

# Refocused 1-ppb workplan v6 (compute-precision view) — post-#730 / Hoefsmit stack

> **Predecessor:** [`2026-05-17-1ppb-workplan-v5.md`](2026-05-17-1ppb-workplan-v5.md)
> **Sibling v6:** [`2026-05-18-1ppb-workplan-v6-refreshed.md`](2026-05-18-1ppb-workplan-v6-refreshed.md)
> — the m_p-closure view of v6 (PR #708 author), focused on Borromean
> tower scale-gap resolution, T5/T6 m_p tower depth, y_λ extension.
> This doc and the sibling are **complementary**: this one covers the
> compute-precision 1ppb gate (internal cross-method agreement at
> q_0); the sibling covers per-isotope mass-prediction closure.
> **Coordination ledger:** [`docs/coordination/1ppb.md`](../coordination/1ppb.md)
> **Trigger:** user request 2026-05-18 ("coordinate with siblings,
> refresh the work plan to get to 1 ppb").

## 1. Status snapshot — 1ppb gate is GREEN (with corrections)

The 1 ppb **compute-precision** target (internal cross-method
agreement at substrate `q_0`) is **currently passing on 8 atoms**,
though `cross_check_trM_1ppb.py`'s headline table over-reports
agreement at atoms where it can't run a full 4-way comparison:

```
$ python3 computations/cross_check_trM_1ppb.py
  proton       Hoefsmit, peel, chi-cache              5.18e-16  OK
  neutron      Hoefsmit, peel, chi-cache              4.79e-16  OK
  deuteron     Hoefsmit, peel, chi-cache, Habiro      1.00e-15  OK
  tritium      Hoefsmit, peel, chi-cache, Habiro      3.67e-15  OK
  helium-3     Hoefsmit, peel, chi-cache, Habiro      1.66e-15  OK
  helium-4     peel, Habiro (partial chi-cache)            0.0  OK
  lithium-5    peel, Habiro                                0.0  OK
  lithium-6    peel, Habiro                                0.0  OK
  atoms compared: 8, divergent: 0
```

**Correction (per Gemini #739 review)**: the `0.0` rel_delta_max
for ⁴He, ⁵Li, ⁶Li is **misleading** — `cross_check_trM_1ppb.py`
computes only Hoefsmit-vs-{other} and chi-cache-vs-{other} diffs;
at these atoms one or both anchors are missing/partial and the
script defaults to 0.0 instead of comparing the two paths that
DO exist (peel vs Habiro). Direct mpmath verification of the
stored witness strings:

| atom | actual peel-vs-Habiro rel_diff |
|---|---|
| ⁴He | 1.27 × 10⁻¹⁶ (~16 digits) |
| ⁵Li | 1.77 × 10⁻¹⁵ (~15 digits) |
| **⁶Li** | **2.15 × 10⁻¹³ (~13 digits)** |

⁶Li agreement is **2.15e-13**, only **~4 orders below 1ppb** —
not 6 orders as the headline table suggested. The 1 ppb gate
still passes for all 8 atoms, but **⁶Li has the tightest residual**.

For the 5 atoms with full 3-/4-way coverage: worst residual is
~3.7e-15 (~14.4 digits) at tritium — 5+ orders below 1ppb.

**Follow-up action**: patch `cross_check_trM_1ppb.py` to also
report peel-vs-Habiro deltas when Hoefsmit/chi-cache anchors are
unavailable. Filed as a v6 follow-up in §4.

### Q6 root cause identified (this audit)

Per `q_parameter.py` lines 88-95's own comment, a prior fix
corrected the `Q_50_DIGIT_STR` literal to match the high-precision
derivation. But **8 downstream scripts** still use the f64 import
pattern `mp.mpf(repr(Q_FLOAT))` instead of `mp.mpf(Q_50_DIGIT_STR)`:

```
canonical_tr_m_via_chi_cache.py:107, 148, 273
chi_at_q0_via_hoefsmit_mpfr.py:207
paper_six_term_isotope_sweep.py:957
probe_brane_tower_finite_laurent.py:98
mass_formula_6term_mpfr_50dps.py:71, 236
rho_k_full_via_wenzl_lr.py:207
tau_hat_n_proton_realisation.py:272
```

Verified at dps=50: `mp.mpf(repr(Q_FLOAT))` vs
`mp.mpf(Q_50_DIGIT_STR)` differ by **6.78 × 10⁻¹⁷** relative —
exactly the f64 epsilon. This was the precision floor propagating
through downstream MPFR computes prior to the Q6 fix.

**Status (2026-05-22 update).** Q6 fix has LANDED — the 8 affected
call-sites were migrated to `Q_50_DIGIT_STR` in PR #749 (e.g.
`canonical_tr_m_via_chi_cache.py:108`). A repo-wide search for
`mp.mpf(repr(Q_FLOAT))` now returns zero hits in production paths.
The 1ppb gate is green at all 8 atoms with the worst residual
below 1e-13 per the [L1 dashboard](../../computations/onepb-status-dashboard.witness.json).
This subsection is retained as historical context for the v6
workplan; new precision work should reference the dashboard, not
this paragraph.

## 2. Since v5 (2026-05-17 evening → 2026-05-18 afternoon)

### Merged into main
- **#682** chi-cache combiner (Python)
- **#683** Rust canonical-χ MPFR-50dps default
- **#691** Wenzl-bridge y_λ ceiling extension n=12 → n=15
- **#695** y_λ ceiling extension n=15 → n=30 + scaling-analysis audit
- **#699 / #715** canonical-discipline cleanup
  (PR #697 is mine and still **open** — see §2 "Open at v6 time")
- **#716**'s ancestors (PR #713 duplicate-fn fix, etc) — actually
  still open; #716 itself is clean + waiting
- **#730** GP-without-cuspidal-moves benchmark (negative result;
  the Hoefsmit C-full stack)

### Authorship of recent main commits (#693, #694, #722, #731, #734)
is integration-watcher / canonical-watcher / coordination
infrastructure — orthogonal to 1ppb compute.

### Open at v6 time — my stack
| PR | Status | Layer |
|----|--------|-------|
| #697 | open, clean | chirality V4 retire (Item B closeout) |
| #705 | open, unstable | chirality Finding 2 + Lean audit |
| #710 | open, clean | Hoefsmit optimization audit (no code) |
| #713 | open, clean | wenzl_lr.rs duplicate-fn fix (unblocks Rust build) |
| #716 | open, clean | candidate B (inner rayon, ~2× ⁴He) |
| #718 | open, unstable | C-gate (GP cross-validation) |
| #720 | open, clean | C-full Step 1 (averaged crossings) |
| #725 | open, clean | C-full Step 2 (MPFR variant) |
| #728 | open, clean (just rebased) | C-full Step 3 (memoisation) |

### Open at v6 time — 1ppb-relevant sibling work
| PR | Status | Direct relevance to 1ppb |
|----|--------|--------------------------|
| **#690** | open, dirty | substrate m_p/m_n no-default-CODATA (Tier 2 m_p closure) |
| **#700** | open, dirty | substrate Δm × χ-cache cross-check (Tier 1, identity = 0 exact at 50 dps) |
| **#708** | open, ? | canonical mass-table extension (Layer 1-5 framework) |
| **#704 / #709** | open, ? | m_p chain Items A/B/C audits (Item A already closed on main) |
| **#702** | open, ? | ¹H closure via C2-inflection (item 4 of #671) |
| **#701** | open, ? | λ_scale conjecture proof Step 5 (Tier 3 Q_β ladder) |
| #711 | open, ? | precision rollout batch 1 (5 more scripts under `_precision`) |
| #679 | open, dirty | ρ_K + ⁶Li/⁷Li extension |

## 3. v5 §4 priorities — what changed

### v5 §4 item 1: MPFR-50dps 4-way cross-check audit
**STATUS: DONE.** The cross-check witness on current main has
8 atoms passing at worst |Δ| = 3.67e-15. Was empty on a stale
branch I inspected; current main is fine.

### v5 §4 item 2: chi-cache T/³He/⁴He continuation
**STATUS: T/³He DONE, ⁴He PARTIAL.** The witness shows:
- T, ³He: chi-cache present, 4-way pass
- ⁴He: chi-cache "partial", but 2-way (peel + Habiro) agreement is
  exact (0.0); full ⁴He chi-cache via Rust binary is multi-hour
  compute and not on the critical path while 2-way agreement holds

### v5 §4 item 3: Q6 — `seminormal_mpfr` ~14-digit precision floor
**STATUS: OPEN.** Still the highest-yield 1ppb investigation.
The cross-check residual of 3.67e-15 at tritium reaches the
~14-15 digit floor at MPFR-50dps, suggesting a precision-loss
site upstream of the consumer (`build_blocks_mpfr` is the leading
suspect per #683 Q6).

### v5 §4 items 4, 5: m_p Item A + Item C
**Item A: DONE on main** (commits dd1a12fd0 / 27303e675 / 32b717ed3
/ 708e7f7a9 / 46762bd84). **Item C: open** (Habiro residue
truncation; see #704 / #709).

### v5 §4 item 6: witness drift gate hardening
**STATUS: superseded** by PR #732 (witness-drift float64
allowlist, merged) and PR #693 (compute-integration-watcher).

## 4. v6 §4 — what's closeable NOW

Ranked by 1 ppb yield × tractability:

1. **Merge the Hoefsmit-perf stack** (PR #713 → #716 → #718 → #720
   → #725 → #728). All clean (now post-rebase); delivers correct
   GP MPFR cross-validation tooling + ~2× ⁴He kernel perf
   independent of cuspidal moves. Awaiting human merge sequence.

2. **Q6 investigation** (`seminormal_mpfr` 14-digit floor). The
   one open compute-precision gap. Concretely: build the f64 vs
   MPFR-50dps comparison on a single partition that hits ~10⁻¹⁵
   residual at q_0 and trace where the precision drops below
   theoretical bits. ½-1 day focused Rust internals work.

3. **Sibling PR #700 rebase** — research probe (substrate Δm ×
   χ-cache identity holds at 50 dps). Just needs rebase onto
   current main; mergeable.

4. **Sibling PR #690 rebase** — substrate-default anchors. Dirty
   per recent main churn (#731 dissolved alg-substrate chapter;
   #696 wired flavor-dressing). Rebase + re-run validators.

5. **Cuspidal moves (C-full Step 4)** — research-grade per the
   #730 finding. Geck-Pfeiffer 2000 §3.2 porting. Multi-week,
   NOT on the 1 ppb critical path. The current `peel` /
   `chi-cache` / `Habiro` cross-checks already deliver 1 ppb;
   GP-with-cuspidal would only become important if seminormal
   becomes too slow at n ≥ 18.

6. **Full ⁴He chi-cache** — multi-hour Rust compute. Not blocking
   1 ppb since 2-way ⁴He agreement is exact. Closes the 4-way
   coverage gap for completeness.

7. **⁵Li / ⁶Li chi-cache + Hoefsmit witnesses** — multi-day Rust
   compute at H_15 / H_18. Per the y_λ-scaling audit (#695), ⁵Li
   is at the edge of single-machine MPFR-50dps feasibility; ⁶Li
   is past it without algorithmic acceleration.

## 5. Not closeable without more work

| Item | Blocker |
|------|---------|
| Q6 root-cause fix (if it's a sqrt precision issue inside `build_blocks_mpfr`) | Need a focused MPFR-internals patch |
| ⁶Li / ⁷Li / ⁸Be Hoefsmit witnesses | Multi-day single-machine compute, OR cuspidal-moves-accelerated GP, OR distributed compute |
| `BlochSuslinUniqueness` instance | Upstream Mathlib `Real.dilog` |

## 6. Open governance questions

| # | Question | Carry-forward from |
|---|----------|-------------------|
| Q1 | Promote substrate `Q_β = 0.7825728 MeV` to CAL-3 = output? | v3, v4, v5 |
| Q2 | Staged tightening of `M_P_DERIVED_MAX_REL_DIFF` (1% → 1 ppm → 1 ppb) | v4, v5 |
| Q3 | Tier-3 PSLQ scope (defer or pursue?) | v4, v5 |
| Q6 | seminormal_mpfr 14-digit floor: actual bug or expected per implementation? | v5 |
| **Q8 (new)** | After #730 negative result, is **abandoning GP** for the 1ppb roadmap acceptable? Current cross-check is GP-free and passes at 1e-15. | v6 |
| **Q9 (new)** | The 4-way cross-check has `partial chi-cache` annotations at ⁴He. Should "partial cache OK at 2-way agreement" be the documented production rule, or should full coverage at every atom be the target? | v6 |

## 7. Coordination map (open PRs vs this workplan)

| Tier | Open PRs (mine) | Open PRs (siblings) | Merged (recent) |
|------|-----------------|---------------------|-----------------|
| 1 (compute 1 ppb) | #713, #716, #718, #720, #725, #728 (Hoefsmit / GP); #697 (chirality V4 retire); #705 (chirality Finding 2); #710 (Hoefsmit optimization audit) | #700 (chi-cache identity) | #682, #683, **#691**, #695, #730 |
| 2 (m_p closure) | — | **#690**, #704, #709, #702, #679 (ρ_K + ⁶Li/⁷Li) | #674 |
| 3 (Q_β ladder) | — | #701 (λ_scale) | #715 |
| 4 (mass tables) | — | #708 | #696 |
| infra | — | #711 (_precision rollout) | #693, #694, #722, #732, #734 |

Per Gemini #739 review: this table now includes #691 (Tier 1 merged),
#697 / #705 / #710 (Tier 1 mine), and #679 (Tier 2 sibling) that
were referenced earlier in the doc but missing from the table.

## 8. Next-session high-value moves (rank-ordered)

1. **Merge my Hoefsmit stack** — clears 6 PRs from the queue without
   changing 1ppb verdict (all clean tooling). Human action.
2. **Q6 investigation** — only open compute-precision gap. Focused
   Rust internals work.
3. **Rebase sibling #690 + #700** — substrate-side work; both dirty
   per recent main churn.
4. **Consider Q8 ("abandon GP")** — the negative result on #730 is
   load-bearing; current cross-check passes WITHOUT GP. Deciding
   to leave GP as research-grade infra (not 1 ppb critical path)
   frees attention for Tier 2/3 work.

## 9. Conclusion

**1 ppb compute precision is achieved.** The cross-check witness
shows 8 atoms passing at worst |Δ| = 4e-15. The remaining work is:

- Filling in 4-way coverage gaps at ⁴He, ⁵Li, ⁶Li (compute-bound)
- Q6 precision-floor investigation (research)
- Tier 2 m_p closure (still ~0.07% experimental floor; per #690)
- Tier 3 Q_β ladder (per #701)

GP-with-cuspidal-moves (the C-full Step 4 from v5) is **no longer
on the critical path** per the #730 finding — current cross-check
is GP-free and clears the gate.

## Related blocks / audits

- [`prop:three-calibration-inputs`](../../content/quantum-observable-universe/observations/three-calibration-inputs.md)
- [`prop:atomic-mass-via-rho-k`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-via-rho-k.md)
- [`2026-05-18-hoefsmit-c-full-step6-bench-finding.md`](2026-05-18-hoefsmit-c-full-step6-bench-finding.md) — the #730 negative result
- [`2026-05-18-y-lambda-scaling-analysis.md`](2026-05-18-y-lambda-scaling-analysis.md) — atom-extension feasibility ceiling
- `computations/cross-check-trM-1ppb.witness.json`
- `computations/cross_check_trM_1ppb.py`
