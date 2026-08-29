---
# qou-ia6f
title: 'joint-tower-sdp-rust: declare the f64 tier — 11,057 fields, but the q0 it evaluates at is 251 ppm off the pin'
status: completed
type: task
priority: normal
created_at: 2026-08-29T10:09:49Z
updated_at: 2026-08-29T12:21:07Z
---

## Landed: PR #6007 — the source fixes

Branch `claude/joint-tower-f64-declaration-2026-08-29`. Four defects, all in
`tools/hecke-engine`, all fixed at the producer:

1. skipped Wedderburn blocks emitted `min/max_eigenvalue: 0.0` +
   `psd_symmetric_part: false` and printed `NOT PSD` — 51 of 169 on `main`,
   every one `d_lambda > 500`. Now `Option`/`None` + `skipped_dim_cap`.
2. `q_0_numeric` was the literal `1.1097` while `args.q0` fed the arithmetic.
3. `n_atoms` was `reg.len()`, not `certs.len()` — 12 vs 11 under `--max-n 12`.
4. `precision_tier: "float64"` + `deprecated` now declared.

118 evaluated blocks reproduce bit-identically; 212 lib tests pass.

## STILL OPEN — the witness is not reproducible from the repo

This is the reason the ratchet does NOT move and the carve-out is not yet in
effect. `main`'s witness is 493 KB; the producer emits 13 MB, in a different
shape:

| | `main` (493 KB) | producer output (13 MB) |
|---|---|---|
| jet log | `jet_log_summary: {n_steps_total, truncated_for_repo: true}` | full `jet_log` |
| filtration | `by_grade[g] = {n_terms, sample_perm}` | full term lists |

**Nothing in the tree performs that compression.** `grep -rl truncated_for_repo`
over `*.py *.rs *.sh *.ts` returns nothing — it was a one-off, uncommitted step.
Consistent with the witness's own `scriptCommitSha: "unknown"`.

**And its thresholds are not recoverable from the file.** Measured per atom:

    jet_log kept in full : n_steps <= 20  (helium3-3He, 20 steps)
    jet_log summarised   : n_steps >= 238 (deuteron-canonical-3A)
      => cut somewhere in (20, 238]

    by_grade full        : max n_terms <= 14 (tritium-3H)
    by_grade compressed  : max n_terms >= 28 (tritium-canonical-3A)
      => cut somewhere in (14, 28]

Picking values would be inventing them, not reconstructing them.

**Decision needed before any regeneration** (this is the author's call, not the
agent's — it is a repo-size and shape question, not a math one):

- **(a) commit the full 13 MB witness.** Reproducible by construction from a
  committed producer, and it restores the exact ℚ(q) structural data the
  truncation discarded. Costs 26× on one file. Risk: near zero — grepped
  2026-08-29, NO Python consumer reads `jet_log`, `jet_log_summary`,
  `filtration_certificate` or `by_grade` from this witness. Commits to
  carrying 13 MB of JSON in-tree.
- **(b) add an explicit `--truncate-for-repo` flag** with named threshold
  args, regenerate at chosen values, and say in the witness that the values
  are a documented choice rather than a reconstruction of the original.
  Costs a modest amount of Rust. Risk: the file stops matching `main`'s shape
  in whatever way my thresholds differ from the unknown originals.
- **(c) retire the producer.** It reaches no production location, its
  `consumed_by` edge is one-way, its five consumers are probes, and its
  structural half is read by nothing. Costs nothing; commits to losing the
  probes' input unless they are re-pointed.
- **(d, default) do nothing.** The source stays correct for future runs, the
  stale witness stays on `main` as recorded, and the 11,057 fields stay
  counted in the raw-float64 ratchet — 23.8% of the remaining 46,461.

**Recommendation (my judgement, not a finding): (a).** The size is the only
real cost, the reproducibility gain is permanent, and (b) spends Rust to
manufacture a shape nobody can verify against the original anyway.

## Separate finding, not acted on

`q_0 = 1.1097` is 251 ppm from the canonical proton pin. Whatever happens
above, no number in this witness should be quoted as a value — the input
error is five orders of magnitude coarser than the L2 ppb targets. Changing
the default to the proton pin would move all 10,796 eigenvalues and every
downstream probe conclusion, so it is deliberately NOT done here.


## RESOLVED 2026-08-29 — owner said "do all 4"; all four options executed

**(b) the truncation flag** — `--truncate-for-repo` plus
`--truncate-jet-log-max-steps` (default 20) and `--truncate-by-grade-max-terms`
(default 20), recorded in a `truncation` block IN the witness. Verified rather
than asserted: the defaults reproduce `main`'s shape on **all 11 atoms**, at
502 KB against main's 493 KB. They are not claimed to BE the originals — those
stay unknowable inside (20, 238] and (14, 28] — only to be inside the brackets
and to reconstruct the artifact.

**(a) regenerate and commit** — done, at FULL fidelity. The 13 MB figure that
made this look expensive was the raw one; measured, git stores **795 KB**
gzipped (vs ~118 KB truncated), and the corpus-wide float64 audit still runs in
**4.3 s** with it in tree. All 118 evaluated blocks reproduce bit-identically.

**(c) record the retirement** — `computations/README.md` row said "Production
R1+R2+R3+R4+R5min in Rust"; replaced with the measurement (five probe
consumers, one-way `consumed_by` edge, q₀ 251 ppm off pin, shape-checks-not-
values) and the regeneration command.

**(d)** superseded.

### The blocker turned out to be TWO uncommitted halves, not one

The bean recorded the missing truncation. Diffing a fresh run against main
turned up a second gap: six provenance fields the Rust binary never emits and
main has anyway — `scriptFile`, `scriptHash`, `scriptCommitSha`, `commitSha`,
`q0Anchor`, `durationMs`. Regenerating without restoring them would have been
a provenance REGRESSION on the unreproducible witness. Fixed as
`computations/stamp_joint_tower_witness.py`, routing through
`WitnessBuilder.stamp_staleness_metadata` so the Rust witness gets provenance
by the same code path as every Python producer. `scriptCommitSha` now resolves;
`"unknown"` on main was the fingerprint of a stamper that could not find its
own file.

### Result

Raw-float64 ratchet: **11,057 → 0** on this file, corpus **46,467 → 35,400**,
0 new dirty, 0 regressions. The file leaves the baseline entirely. The
deprecated-f64 carve-out goes 80,675 → 91,732 across 6 witnesses — reclassified
and reported, not hidden.

### Two findings surfaced by smoke-testing the consumers first

- `alpha_star_dominant_partitions.py` **could not run at all**: the Phase-5
  subdirectory refactor moved it into `alpha/` and left the witness read at
  `__file__.parent`. Fixed to use `_path_bridge.witness_path`, as its sibling
  already does. Re-run confirms identical numbers.
- `probe_4_li6_rectangular_conjecture` **cannot run either**, and this one is
  not fixable here: it needs `lithium6-canonical-3A`, an atom the producer
  reaches at H_18 and is SIGKILLed on memory computing (4m36s, exit 137). Its
  error message says "re-run with ⁶Li registered" — ⁶Li IS registered now, so
  the blocker moved from registration to memory. Left as a real compute limit.

So of five "live consumers", two were dead. That strengthens rather than
weakens the `not_production` claim.

PR #6007.
