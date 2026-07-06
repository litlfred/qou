# Data-integrity beans adhb + b0vf: empirical diagnosis (adhb) and environment block (b0vf)

**Date:** 2026-06-28
**Beans:** `adhb` (He3 R5 witness multi-term-cost re-run), `b0vf` (chi-helium-4-h12 witness 17/77)
**Compute:** driver over `computations/r5_full_canonical_knot_solver.py` (no production edit; committed
witnesses untouched).

## b0vf — environment-blocked (not fixable in this sandbox)

The producer `computations/chi_4he_via_rust_lossless.py` requires
`pyhecke_native.chi_q_via_gp` (the Rust kernel) for the H₁₂ Hoefsmit/χ evaluation. Building
`tools/pyhecke-native` here **fails**: its `clarabel` Cargo dependency is pinned to
`github.com/litlfred/Clarabel.rs` (rev `967320920c…`), a repository **outside this session's
`litlfred/qou` GitHub scope**, so the agent proxy returns **HTTP 403** for the git fetch — via both
libgit2 and `CARGO_NET_GIT_FETCH_WITH_CLI=true`. This is a hard, environment-level restriction, not a
code issue.

Additionally, even with native available, completing the witness is a long compute: the committed
partial recorded **17/77 partitions in 2241 s (~37 min)** → full ≈ **2.8 h**.

**Status:** b0vf needs an environment where `litlfred/Clarabel.rs` is reachable (or a prebuilt
`pyhecke_native` wheel) plus a dedicated ~3 h run. Out of reach in this sandbox. No change made.

## adhb — the multi-term-wired solver does NOT recover the canonical T_w (hypothesis refuted)

The bean's task: "re-run the R5-full canonical knot solver for he3 (and deuteron) with the full
multi-term cost (T2–T6), which **re-selects the canonical winner**." The current
`r5_full_canonical_knot_solver.py` **already** wires a multi-term offset
(`multi_term_offset = b23 + t4` from `mass_formula_6term`, lines 562–590) into `cost_for_candidate`.

Ran the current solver for both atoms via a cache-backed driver (H₃ Wenzl weights read from the
committed `y-lambda-wenzl-witness.json`, since `pyhecke_native` is unavailable — values match native to
3e-16 per the loader docstring). `solve_atom_b3` called directly; the committed witness was **not**
regenerated.

| atom | winner (search) | ρ* | winner rel-resid | canonical | canonical PSD? | canonical rank | recovered? |
|---|---|---:|---:|---|---|---:|---|
| deuteron | `[1,-2,1,-2,-1,-1,-1,-2]` | 2 | 0.0031 | `6_2` | **no** (α_gap=0.89) | 1051 / — | ✗ |
| he3 | `[1,1,2,2,1,1,1,1]` | 4 | 0.41 | `L6a4` | yes (α_gap=0) | 381 (psd 381) | ✗ |

Two structural reasons the canonical winner does not emerge — neither fixable by a re-run:

1. **deuteron `6_2` is not PSD-feasible** in the H₃ prototype (α_gap = 0.89; the symmetric part of its
   Hecke image has a negative eigenvalue), so it cannot win an α-gap-driven search at all.
2. **Magnitude gap.** `B_AME(he3) = 7.718` MeV, but canonical `L6a4` predicts only ~2.04 MeV even with
   the ~1 MeV multi-term offset applied (ρ=2, m_e·|tr_M|≈1.02 + offset≈1.02). The best B₃ candidate
   reaches only 4.58 MeV. The multi-term offset (~1 MeV) is **far too small** to close the ~5.7 MeV
   he3 deficit — this is the "single-term structural offset (~87–100% magnitude)" the solver's own
   docstring documents, and the present multi-term wiring does not address it.

**No-fit guard.** Tuning `w_resid` (currently 0.25) or the offset until `L6a4`/`6_2` win would be
**fitting to the known answer** — forbidden by the AGENTS.md no-fit discipline. The canonical winner
must emerge *naturally* from the correct feasibility criterion + physically-derived multi-term
formula; it does not, with the current implementation.

**Status:** adhb's "mechanical re-run" hypothesis is **refuted**. The committed witness was correctly
left frozen (PR #2836); wiring a regen would still regress. The real fix is research-grade and
unresolved: it needs (a) a feasibility criterion under which deuteron `6_2` is admissible, and (b) a
multi-term mass formula whose magnitude actually reaches `B_AME` for he3 — **not** a weight tune. No
production change made; no witness regenerated.

## Net

Of the three data-integrity beans the user queued this session: `tnjb` was already done (verified
earlier), `me3r`/`ce18`/`ct80` already reconciled (verified earlier), and `b0vf`/`adhb` are blocked —
b0vf by an out-of-scope Rust dependency repo, adhb by an unresolved magnitude/feasibility problem that
a re-run cannot fix. The value here is preventing wasted re-attempts: both are now precisely scoped.
