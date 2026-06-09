# Handover — matrix-M tier complete; A=8,9 path mapped

**Author**: prior agent session (Claude Code)
**Date**: 2026-06-09
**Author availability**: AWAY ~1 week
**Branch state at handover**: `claude/matrix-m-determinism-2026-06-09` (PR #2023 open)

> Read this once, then check the live PR list — sibling agents have
> almost certainly merged new work onto `main` while the author was
> away.

## TL;DR

The entire **matrix-M optimization tier** (Tier 0 sympy → Tier 1
mpfr → Tier 2 Rust port → PyO3 binding → consumer wire-in) is now
on `main`. The catalogue extends to **A=6 (727 cells, ⁶Li)**. The
**critical enabling step for A=8, A=9 is Phase 1.3 (μ_p, μ_n)
sub-block extraction**, which has a validated sympy prototype on
`main` but is not yet wired into the production mpfr backend.

The one open PR from the session, **#2023**, is a small mechanical
determinism fix on the Rust matrix-M and should merge after a
Copilot pass.

## What landed in this session (chronological, all merged)

| PR | tier | scope | merged commit |
|----|------|-------|---------------|
| [#1980](https://github.com/litlfred/qou/pull/1980) | T0 | sympy q-rational Hoefsmit substrate | — |
| [#1985](https://github.com/litlfred/qou/pull/1985) | T0 | block-scoped sp.Rational backend | — |
| [#1987](https://github.com/litlfred/qou/pull/1987) | T0 | multi-bridge generalisation (⁴He cross-over) | — |
| [#1993](https://github.com/litlfred/qou/pull/1993) | T1 | mpfr backend — ⁴He 1.34× faster than Rust GP | — |
| [#2000](https://github.com/litlfred/qou/pull/2000) | T1 | `chi_lambda_at_q0` consumer wire-in (catalogue 100-300× faster) | — |
| [#2004](https://github.com/litlfred/qou/pull/2004) | T1 | `chi_at_q0_via_matrix_m_mpfr.py` producer | — |
| [#2012](https://github.com/litlfred/qou/pull/2012) | data | catalogue → ⁶Li (727 cells) + A=8,9 optimization audit | — |
| [#2013](https://github.com/litlfred/qou/pull/2013) | T1.3 | Phase 1.3 prototype — q-Young symmetrizers (9/9 pass) | — |
| [#2015](https://github.com/litlfred/qou/pull/2015) | T2 | Rust port `tools/hecke-engine/src/matrix_m_mpfr.rs` (2/2 pass) | — |
| [#2017](https://github.com/litlfred/qou/pull/2017) | T2 | PyO3 binding `pyhecke_native.chi_via_matrix_m_mpfr` (24.4×) | — |

The matrix-M trace identity has been **independently re-verified at
every tier** on every λ ⊢ 6 for the deuteron probe `σ_1·σ_3·σ_5`
plus extensions to A=3 toy / A=4 probe / production deuteron braid.

## Open PR from this session

**#2023 — `claude/matrix-m-determinism-2026-06-09`**:
[matrix-M follow-up #2017: deterministic block iteration order](https://github.com/litlfred/qou/pull/2023)

- Addresses Copilot's L342 comment on #2017 about `HashMap::values()`
  iteration nondeterminism + non-associative mpfr addition producing
  bit-different decimal strings across runs.
- Fix: sort blocks by μ_p key (`Vec<usize>`) before the trace sum.
  O(B log B), B ≤ p(k_split). Trivial cost.
- New test `chi_via_matrix_m_is_deterministic_across_calls` runs 5
  independent (cache, chi) pairs and asserts decimal strings match.
- 3/3 Rust tests pass.
- Awaiting Copilot re-review (Gemini quota out for ~24h after
  01:00 UTC).

## Recommended next concrete steps (priority order)

### 1. Merge #2023

Small mechanical fix. Should pass Copilot cleanly. Use rebase-merge
(CLAUDE.md rule 8). After this, the matrix-M tier is fully
deterministic.

### 2. **Phase 1.3 mpfr backend wire-in** (medium effort, 1-2 sessions) — **THE UNBLOCKER**

This is the single highest-leverage piece of remaining work. Per
[`docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md`](docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md),
Phase 1.3 (μ_p, μ_n) sub-block extraction is what makes A=8, A=9
tractable. Without it, no amount of Rust porting saves them —
they remain 8-year sweeps. With it, ⁹Be drops to **2.5 minutes**
on existing mpmath; **seconds** after Tier 2 Rust port.

**Concrete plan**:

1. **Extend `folio-assistant/computations/derived_chi_catalogue_matrix_m_mpfr.py`**:
   - `precompute_block_tables_mpfr` already extracts per-μ_p blocks
   - Add a second level: within each μ_p block, apply the q-Young
     symmetrizer (port from PR #2013 prototype) for each μ_n ⊢ 3
   - Extract `M(μ_p, μ_n, λ; q_0)` as a small `c_LR · dim_p · dim_n`
     matrix (≤ 4 typically)

2. **Reference implementation**: PR #2013 prototype at
   `folio-assistant/computations/derived_chi_catalogue_matrix_m_mu_n.py`
   has the q-Young symmetrizer formula, validated on 9/9 blocks for
   λ ⊢ 6. Port to mpmath.

3. **Cross-validate**: the (μ_p, μ_n) backend must match the existing
   μ_p-only backend on D / T / ³He / ⁴He / ⁵Li / ⁶Li within 10⁻⁴⁵
   at dps=50. Use the existing catalogue cells as the gold standard.

4. **Add `--use-mu-n-blocks` flag** to
   `chi_at_q0_via_matrix_m_mpfr.py` so callers can pick the backend
   tier.

### 3. A=7 catalogue extension

Run `derived_chi_catalogue_sweep.py --max-A=7 --merge-existing`.

Without Phase 1.3: ~hours (acceptable for an overnight job, but
fragile — use the long-compute logging discipline per CLAUDE.md
"5-min idle trigger"). With Phase 1.3 wired in: ~10 minutes.

After this lands: 7Li / 7Be cells in the catalogue (~1500
additional cells).

### 4. A=8 then A=9 catalogue extensions

Both require Phase 1.3 mpfr wire-in to be tractable. Per the audit
projection at dps=50:

- A=8 (⁸Be, 1575 partitions): ~30-60 s on mpmath after Phase 1.3
- A=9 (⁹Be, 3010 partitions): ~2-3 min on mpmath after Phase 1.3

Subsequent Rust port of Phase 1.3 (next item) drops both to seconds.

### 5. Phase 1.3 Rust port + PyO3 binding

After (2) is validated empirically. Concrete plan:

1. Extend `tools/hecke-engine/src/matrix_m_mpfr.rs` with
   `q_young_symmetrizer_mpfr` (port from PR #2013 prototype).
2. Add `precompute_block_tables_mu_n_mpfr` building (μ_p, μ_n) blocks.
3. Add `chi_via_matrix_m_mu_n_mpfr` (Σ_{(μ_p, μ_n)} Tr formula).
4. Expose via `pyhecke_native.chi_via_matrix_m_mu_n_mpfr` PyO3 binding.

Expected total speedup vs Rust GP at A=9: ~10⁶× per partition
(`dim²` reduction + native arithmetic).

### 6. Eventual organic-chem extension

Not started. Per CLAUDE.md user accessibility section (and earlier
session direction): the framework will eventually need to extend
beyond Be to organic chemistry braid words. The matrix-M tier
makes this tractable.

Likely steps:
- Identify the organic-molecule braid words (`atom_braid_word_3A`
  generalisation)
- Re-validate parabolic structure (assumes single σ_3 bridge per
  nucleon pair — true for current isotopes; needs check for
  branched molecular structures)
- Extend catalogue producer to cover molecule labels

## Reference docs (read these first)

- **[`docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md`](docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md)** — critical path analysis. Read §2 (tier table), §3 (alternative optimizations), §4 (recommended path), §6 (conclusion).
- **[`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)** — original Tier 1 LR factorisation theory. §5 (deuteron), §6.2 (recursive multi-bridge).
- **`folio-assistant/computations/derived_chi_catalogue_matrix_m_mu_n.py`** — Phase 1.3 sympy prototype with validated q-Young symmetrizers. Port from this for the mpfr wire-in.
- **`folio-assistant/computations/derived_chi_catalogue_matrix_m_mpfr.py`** — production mpfr backend. Extend with `(μ_p, μ_n)` layer here.
- **`tools/hecke-engine/src/matrix_m_mpfr.rs`** — Rust port. Mirror the Python mpfr backend.

## Coding rules to honor (from CLAUDE.md)

- **NO f64 in production compute path**. mpfr (`mpmath.mpf` or
  `rug::Float` at dps ≥ 50) is the canonical precision. Decimal
  strings cross the language boundary.
- **Δ_λ-gate**: every closure / per-partition compute must be a
  structural rearrangement of the Markov-trace identity, not a fit.
  Six closure ansätze have failed; do not propose a seventh.
- **3-calibration discipline**: only `m_e`, `m_μ/m_e`, `m_π` are
  calibrated. Q_β is derived. Substrate q_0 is owner-declined
  (2026-05-08).
- **Branch + PR workflow STRICT**: every work tranche gets a
  `claude/<theme>-<utc-ymd>` branch + immediate PR. Default
  merge method is **rebase-merge** (preserves commits) per CLAUDE.md
  rule 8 — overrides any prepare-merge skill default.
- **Reviews**: address every Gemini/Copilot comment with explicit
  `accept` / `accept-with-modification` / `reject-with-reason`, then
  post a consolidated status comment per the `local/coordinate`
  skill §5.

## Sibling PR awareness at handover

19 other open PRs from other agent sessions. None overlap matrix-M
scope at handover time. Don't touch them; they're other agents'
work.

If a sibling PR re-touches `tools/hecke-engine/src/matrix_m_mpfr.rs`,
`folio-assistant/computations/derived_chi_catalogue_matrix_m*.py`,
or `docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md`,
coordinate via the `local/coordinate` skill before proceeding.

## Things to NOT do

- Don't re-pitch KLR / crystal-graph as a matrix-M speedup. The
  audit at [`docs/audits/2026-05-30-klr-dialog-assessment.md`](docs/audits/2026-05-30-klr-dialog-assessment.md)
  ruled 0/6 candidate proofs would shorten with a KLR layer.
- Don't re-introduce `λ_scale` or `Geom_full(K)` (both purged).
- Don't reinvent the q-Young symmetrizer derivation — port from PR
  #2013's `derived_chi_catalogue_matrix_m_mu_n.py` directly.
- Don't merge into `main` without explicit user authorization. The
  user is away for ~1 week.

## If you're the user reading this on return

The clean handoff state is: matrix-M tier on `main`, #2023 awaiting
merge, Phase 1.3 mpfr wire-in is the next concrete unblocker for
A=8, A=9. If you want to extend the catalogue further during your
absence, an agent running this plan should reach A=9 in this state
within a few sessions.

---

_Generated by [Claude Code](https://claude.ai/code/session_01BkJRCaeJ8ybmQDauQ34frg)_
