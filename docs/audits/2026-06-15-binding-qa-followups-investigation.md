# Binding / QA follow-ups — investigation + blockers (2026-06-15)

**Status:** handoff. Five follow-ups were surfaced while landing PRs #2314,
#2319, #2322, #2324, #2316. This doc records what was resolved and — for the
items blocked by the same-day platform refactor — the exact root cause and the
environment needed to finish them. Investigated from a **qou-only** sandbox
*after* the ~42-commit refactor that moved the platform code + QA pipeline out
of `qou` (`folio-assistant/computations/` → top-level `computations/`;
`folio-assistant/` platform + `content/pipeline/` checkers migrated to the
standalone folio-assistant repo).

## 1 — figure-eight-reeb-rotation Lean: ✅ VERIFIED

`content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.lean`
on `main` compiles **clean, sorry-free** (lean-direct, exit 0). PR #2319 removed
the unused generic-`R` helper `hecke_generator_det_neg_one`; the three surviving
theorems (`figure_eight_det_one`, `unit_modulus_of_det_one_small_trace`,
`figure_eight_unitary_on_standard`) are intact and self-contained.

Method (the env's `lake build` is firewalled off `release.lean-lang.org`, but
the oleans are warm): restore from `lake-cache/qou-v4-24-0`, set `LEAN_PATH` to
the restored olean dirs, run `lean` directly on the file (do **not** `lake
build` — it wipes the restored oleans). See
`.claude/skills/local/lean-environment-setup.md` §"VERIFY a single file with
lean-direct".

## 2 — c-q-q0 derivation-chain staleness: ✅ RESOLVED (chain re-pinned)

**Resolved 2026-06-15.** The self-contained proton-anchor solver in
`computations/substrate/q_parameter.py` (`_solve_q_proton_f64`: m_p/m_e +
Vol(4₁) → q, needs **no** `qou_substrate`/`pyhecke`) yields q₀ =
**1.1099785955573347** — exactly `qou_substrate.Q` / the validator's `Q_0`. So
the canonical proton-anchor q₀ is `…955573347`, and the `c-q-q0.derivation.json`
+ `q-pinning-50-digit.witness.json` (both `…827513808`) were stale
(pre-2026-05-28 re-pin). The chain is now re-pinned (target_value
`9.092678397394828`, q₀ `…955573347`; `1/(q₀−1)` matches to 2e-17 ≪ the 1e-12
gate). **Still stale (separate, full-env regen):**
`q-pinning-50-digit.witness.json` at 50-dps + any downstream `*_at_q0_50dps`
witnesses — those need `qou_substrate`'s exact high-precision inputs to
regenerate faithfully.

The original disagreement that flagged this:

| source | q₀ | c_q = 1/(q₀−1) |
|---|---|---|
| `computations/q-pinning-50-digit.witness.json` **and** `computations/c-q-q0.derivation.json` (step 5 + `target_value`) | `1.1099785827513808…` | `9.0926794561…` (matches the chain target) |
| `qou_substrate.constants.Q` (what `derivation_chain_validator.py` imports as `Q_0`) | `1.1099785955573347` | `9.0926783974` |

`derivation_chain_validator.py` flagged `c-q-q0` (rel_diff **1.16e-07** vs
`target_tolerance` 1e-12) when last run (PR #2322, on pre-refactor `main`). So
the chain agrees with the **q-pinning witness** but disagrees with
**`qou_substrate.Q`**. Either (a) `qou_substrate.Q` is the post-2026-05-28
proton-anchor-re-pin canonical and the witness + chain are stale, or (b) the
witness is canonical and `qou_substrate.Q` drifted.

**Why blocked here:** `qou_substrate` was removed from `qou` by the refactor, is
not on PyPI, and its source is gone from the sandbox — so the validator cannot
even run in qou-only, and the current canonical q₀ cannot be read. Pinning a
1e-12 gold check to an unverifiable value would only spread the inconsistency.
Resolution requires the `qou_substrate` package to confirm the canonical q₀,
then regenerating `q-pinning-50-digit.witness.json` + `c-q-q0.derivation.json`
(and any `*_at_q0_50dps` witnesses) consistently. This is an instance of the
known q₀-repin stale-witness class (`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`).

## 3 — q-usage-archimedean-in-categorical-chapter findings: ⛔ BLOCKED

The 4 `q-usage-archimedean-in-categorical-chapter` major findings recorded by
PR #2324's drain (on `TrMHopfSigma1SqClosedForm.lean`, figure-eight) cannot be
re-evaluated or cleared in `qou`: the QA checker pipeline
(`validate.ts`, `qa-sweep.ts`, `qa-checkers-*.ts`, `qa-criteria-registry.ts`)
moved to the standalone folio-assistant repo. `content/pipeline/` retains a
single file; the `content/package.json` `validate`/`qa-sweep`/`qa-staleness`
scripts are now stale references. Whether a `.md` archimedean-acknowledgment
clears the q-usage flag (as it does for `wall-side-correct`) cannot be checked
without the checker source.

## 4 — B_canonical/B_pred → B_lin rename: ⛔ DEFER (large + unverifiable)

#2316's catalogue established `B_lin` as canonical and **explicitly deferred**
the code-level rename. Current scope: **594** non-`_deprecated` occurrences
across ~50 `.py` files, 157 in dict-key/witness-field position, and **68
`*.witness.json`** files whose data keys use `B_pred`/`B_canonical` (those need
producer re-runs, not a text rename). Many `B_pred` are generic "predicted
binding" locals, not the canonical `B_lin` — the rename needs semantic
judgment, and the scripts can't be run/verified in qou-only (`qou_substrate` /
`pyhecke` external). Recommend a dedicated full-env pass, not a blind sweep.

## 5 — Δ_λ q₀⁵-per-chain-site mechanism: 🔬 OPEN (research-grade)

Recorded already in #2316 (`docs/audits/2026-06-15-delta-lambda-q5-per-site-mechanism-start.md`
+ bean `qb5s`). Honest framing (per #2320 coordination): `B_sym` (the
Kashaev/exp form) already absorbs most of `Δ_λ` (Δ_λ^sym ≈ 1 on T/³He), so the
"5-per-site" residual must be measured against `B_sym`, not `B_lin` — otherwise
the `s → −ln(1−s)` linearization is read as a `q⁵` factor.

**Magnitude check (2026-06-15) — the literal `q₀^{5(2A−1)}` exponent fails.** A
back-of-envelope test against #2320's own one-pipeline numbers
(`B_sym/B_lin = Δ_λ^lin ÷ Δ_λ^sym`, q₀ ≈ 1.10998):

| nucleus | A | 2A−1 | `q₀^{5(2A−1)}` *(claim)* | `B_sym/B_lin` *(#2320)* | off | fit exp/site |
|---|---|---|---|---|---|---|
| D | 2 | 3 | 4.8 | 1.54 | 3× | 1.39 |
| T | 3 | 5 | 13.6 | 2.44 | 6× | 1.71 |
| ³He | 3 | 5 | 13.6 | 2.02 | 7× | 1.35 |
| ⁴He | 4 | 7 | 38.6 | 3.04 | 13× | 1.52 |
| ⁶Li | 6 | 11 | 310.7 | 4.85 | 64× | 1.38 |
| ⁷Li | 7 | 13 | 882.0 | 6.06 | **145×** | 1.33 |

Two failures: **(i) wrong functional form** — the miss is not a constant
offset, it grows 3×→145× with A (`q₀^{5(2A−1)} ~ 2.7^A` explodes; the actual
ratio grows ~linearly, 1.5→6 over A=2→7); **(ii) the exponent that fits is
≈ 1.4 per site, not 5** (last column; roughly constant modulo the
deuteron/bond-type anomalies). That ≈ 1.4/site is just the `−ln(1−s)/s`
exp-vs-linear correction #2320 already named (s grows ≈ with site count), **not**
a q₀-power law — so "5 = Bring-quintic degree, q₀⁵/site" reads as **fitted**
(to a couple of small-A points, or to `B_lin`, which folds in the
linearization). **Before investing in the complex-q/Kashaev "why q₀⁵"
mechanism, the exponent has to be shown to exist; by this check it largely does
not.** The real keystone — and any genuine residual — should be re-derived
against `B_sym` (where Δ_λ^sym ≈ 1 already), with the deuteron over-binding and
the magic-shell deficit as the actual targets.

Caveats: back-of-envelope from #2320's transcribed table + q₀ ≈ 1.110, and the
real binding compute can't run in this qou-only sandbox (`qou_substrate` /
`pyhecke` blocked, §2) — the full-env numbers should confirm. But a 145×
runaway at ⁷Li is far outside any transcription/precision slack. This is a
**pruning, not a derivation**.

## Root cause + how to finish 2/3/4

The 42-commit refactor relocated the compute substrate (`qou_substrate`,
`pyhecke`) and the QA checker pipeline to the external folio-assistant repo /
unpublished packages. A **qou-only** session cannot execute or verify items
2/3/4 (and could not add the external repo — `list_repos`/`add_repo` were not
available). Finish them in a session that has the folio-assistant repo +
`qou_substrate`/`pyhecke` installed (or once those are published to PyPI).
