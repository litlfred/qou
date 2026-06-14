# Compute vacuity analogue — Rust + Python stack audit & check design

**Date:** 2026-06-14
**Scope:** the compute-side sibling of
[`lean-proof-vacuity-audit`](../../.claude/skills/local/lean-proof-vacuity-audit.md) /
[`2026-06-14-lean-vacuous-proof-audit.md`](2026-06-14-lean-vacuous-proof-audit.md).
**Question:** does the Rust + Python compute stack carry the *compute analogue* of
vacuous proofs — tests that assert nothing, producers that bake in the answer they
claim to compute — and if so, how should an analogous detector wire in?

**Executive summary.** Test hygiene in the compute stack is strong; the witness
layer has one systemic anti-pattern. Concrete counts actually found: **0** empty
Rust tests (`fn …(){}`), **0** `assert!(true)` / `assert_eq!(x,x)`, **0** permanent
untracked `#[ignore]`, **0** untracked `@pytest.mark.skip` (the one that exists
carries a tracked P3-vendoring reason), **0** pytest functions that truly assert
nothing (2 AST-flagged were false positives — schema `.validate()` calls that
raise). The real finding is in the witness producers: **153 live
`add_assertion(name, computed=L, expected=L)` calls where both sides are the same
literal** (`folio-assistant/computations/`), which always set `passed:true`
independent of any computation — the witness analogue of `proof-no-trivial-true`.
Of these, **146** are the `computed=1, expected=1` boolean "did-this-run" idiom and
**7** embed real physical literals; the strongest faked-compute cases are two `c_3`
"match" assertions that compare `-2==-2` instead of comparing the empirical value
they name.

## Part A — Structure map

| Library | Purpose (1-line) | Key modules/files | Tests live | How tested |
|---|---|---|---|---|
| `tools/hecke-engine/` | Rust Layer-1 canonical compute core (GS reducer, Hoefsmit, Markov trace, Clarabel SDP) | `src/lib.rs`, `gb_nf_reducer.rs`, `seminormal_mpfr.rs`, `tr_m_atomic_mpfr.rs`, `sdp_*`, `wenzl_lr.rs`; 40+ `src/bin/*.rs` demo binaries; `src/archive/v{2..7}.rs` | Inline `#[cfg(test)]` (30 files) | `cargo test` — **195** `#[test]` fns. No `tests/` integration dir; all inline. |
| `tools/pyhecke-native/` | PyO3 wheel binding `hecke-engine` into Python | `Cargo.toml`, `src/lib.rs` | none in-crate | **0** `#[test]`; exercised via `pyhecke` Python tests + Python importers |
| `tools/hecke-engine-wasm/` | WASM binding (Tier-2) | `src/lib.rs` | inline | `cargo test` — 13 `#[test]` |
| `tools/hecke-engine-node/` | napi-rs Node binding | `src/lib.rs` | none in-crate | **0** `#[test]` (JS-side harness) |
| `tools/hecke-engine-jvm/` | JVM binding (Tier-3) | `src/lib.rs` | inline | `cargo test` — 12 `#[test]` |
| `tools/hecke-engine-c/` | C ABI binding (Tier-3) | `src/lib.rs` | none in-crate | **0** `#[test]` |
| `tools/pyhecke/` | Python Layer-2b (Hecke/Gram/Markov trace facade; 19 in-repo importers) | `python/pyhecke/{gram,trace,sdp,partition,wedderburn,lp_dual_solver,bridge}.py` | `tools/pyhecke/tests/` | `pytest` — **14** test files (best-covered Python pkg; cross-checks Rust↔Python Gram at 1e-14, schema validation, roundtrips) |
| `tools/qou-substrate/` | Python Layer-2a (q₀, mpmath precision, `WitnessBuilder`) | `python/qou_substrate/{constants,precision,witness}.py` | `tools/qou-substrate/tests/` | `pytest` — 2 files (`test_smoke.py`, `test_ephemeral_mask_sync.py`) |
| `qou-mass/` | Python external-researcher facade (`predict()`, `compute_tr_M()`, `canonical_braid()`) | `src/qou_mass/{prediction,api}.py`, `_internal/*` | `qou-mass/tests/` | `pytest` — 2 files (`test_public_api_shape.py`, `test_p2_integration.py`) |
| `tools/witness-schema/`, `tools/block-qa-schema/` | Cross-language interchange schemas | `python/*/__init__.py` + Zod/JSON mirrors | `tests/test_python.py` (1 each) | `pytest` — schema-roundtrip |
| `folio-assistant/computations/` | Python **witness producers** (Layer-3 in-repo) | **849** `*.py` → **921** `*.witness.json`; `lp_dual_solver.py`, `lp_dual_witness_validator.py` (existing validator) | **No dedicated test dir** | Self-validating via `WitnessBuilder.add_assertion` (the locus of the anti-pattern); 562 `_deprecated/*.py` excluded from live counts |

**Notes.** `add_assertion(name, computed, expected, tolerance)` sets
`passed = (computed==expected)` when `tolerance is None`, else
`|computed-expected| <= tolerance`
(`tools/qou-substrate/python/qou_substrate/witness.py:194-201`). The
`computations/` tree is the only compute area with **no unit-test harness** — its
correctness contract is entirely the in-producer assertions, which is why the
vacuity risk concentrates there. Rust + `pyhecke` have genuinely good hygiene.

## Part B — Anti-pattern catalog (compute vacuity family)

### B1. Empty / no-op tests — **0 found**
- *Misleading because:* a test that runs nothing reports green coverage for code it never touches.
- *Heuristic:* `#\[test\][^\n]*\nfn\s+\w+\s*\(\)\s*\{\s*\}` (Rust); `^\s*pass\s*$` / `^\s*assert True\s*$` body (pytest).
- *Instances:* **zero.** No empty Rust test bodies across `tools/`; no pytest test with only `pass`/`assert True`.

### B2. Tautological assertion (`x == x`, literal == same literal) — **153 found (the headline)**
- *Misleading because:* `Assertion.passed` returns `computed == expected`; when both are the same literal, `passed:true` is recorded in the witness JSON **regardless of whether any computation succeeded or matches reality.** This is the exact witness analogue of Lean `proof-no-trivial-true` / `: x = x := rfl` and of `assert_eq!(x, x)`.
- *Heuristic (multiline):* `add_assertion\(.*?computed\s*=\s*(-?[\d.]+).*?expected\s*=\s*\1\b.*?\)` over `folio-assistant/computations/**/*.py`.
- *Instances (live, `_deprecated` excluded):* **153 total**, split:
  - **146 boolean-flag literals** (`computed=1, expected=1, tolerance=0`) — a "this code path executed / this property held" idiom. Examples: `per_bond_growth_a3.py:104` (`kernel_ran`), `three_body_joint_trace_a3.py:101` (`kernel_ran`), `eigenvalue_reeb_extension_h4_h5.py:172` (`extends_beyond_h3`), `meson_spectrum_predictions.py:141` (`kaon_predicted`), `mass_vol_density.py:301` and `:305`. These are *honest-but-misleading*: the JSON shows a passing value-check that is really a status flag.
  - **7 real-physical-literal cases** (the ones that warrant agent scrutiny):
    - `folio-assistant/computations/probes/khovanov_at_q0_probe.py:222` — `c_3_match_at_q1`, `computed=-2, expected=-2` while the genuine `empirical_c3` is computed two lines up (`c_3_empirical`, line 213) but **never compared**. The honest form is `computed=float(empirical_c3), expected=-2`.
    - `folio-assistant/computations/probes/khovanov_klr_rank_cohomology_probe.py:231` — `c_3_exact_match`, same `-2==-2` pattern, source literally says "matches empirical c_3 exactly" yet asserts the constant against itself.
    - `folio-assistant/computations/m_p_m_e_li2q.py:126` — `codata_mp_me_loaded`, `computed=1836.152, expected=1836.152`. This one is benign (a CODATA load self-check, honestly named); the real predicted `mp_me` is used in the error computation at line 98.
    - `probes/qbeta_complex_c3_fibre_probe.py:293` (`computed=4.0==4.0`), `probes/additive_composition_categorical_probe.py:268` (`…supported_by_all_4_hypotheses`, `4==4`), `alpha/alpha_em_habiro_taylor_investigation.py:245` (`habiro_taylor_coefficients_extracted`, `5==5`), `qbeta/qbeta_habiro_depth15_interpretation.py:623` (`6==6`) — these encode a *count* (of hypotheses / extracted coefficients) as a tautology rather than asserting the count was actually produced.

### B3. Hardcoded-witness producer (literal baked in as "computed") — **0 strict, ~2 borderline**
- *Misleading because:* a producer that writes a literal numeric result it claims to compute is the self-assuming-projection analogue — the witness "proves" a number the script never derived.
- *Heuristic:* `(value|result|computed)\s*[:=]\s*-?\d+\.\d{3,}` in producer bodies that emit JSON, cross-checked against whether the value flows from a computation.
- *Instances:* **No strict cases in live producers.** Numeric literals found are CODATA/experimental constants used as *comparison targets* (`codata_mp_me = 1836.152`, `codata_mn_me = 1838.684` at `m_p_m_e_li2q.py:96-97`) — legitimate. The two `c_3` cases in B2 are the closest borderline: they hardcode the categorical value `-2` into the assertion's `passed` flag instead of comparing the empirical quantity, so the *assertion* is faked even though the *witness data* (`c_3_empirical`) is real. (Deprecated `_deprecated/trefoil-quark-nucleon-nf.py:508 phi_val = 0.0486…` exists but is dead code.)

### B4. Tests with no assertions (run-but-never-check) — **0 found** (2 false positives)
- *Misleading because:* exercises a path but verifies nothing about the output.
- *Heuristic:* AST — test function with no `ast.Assert` and no `.raises/.warns/.assert*` call.
- *Instances:* AST flagged `tools/pyhecke/tests/test_rust_gram.py:28` and `tools/pyhecke/tests/test_schema.py:42`, but both are **false positives**: they call `jsonschema.validate(...)` / `pyhecke_schema.validate(...)`, which **raise on failure** — the validation call *is* the check (run-but-raises, not run-but-never-check). Net real: **zero.**

### B5. `unwrap()`-only smoke test (executes, asserts ~nothing) — **1 found, weak-not-vacuous**
- *Misleading because:* checks only "didn't panic," not the value.
- *Heuristic:* Rust `#[test]` body containing `unwrap` but no `assert`/`panic!`/`matches!`/comparison op.
- *Instances:* **1** — `tools/hecke-engine/src/tr_m_atomic_mpfr.rs:218 proton_word_smoke`. It is honestly scoped (comment: "verify the result is finite and parseable") and does carry an implicit assertion via `Float::parse(...).expect("result string must parse as Float")`. Classify as a **weak smoke test**, not vacuous — a reviewer might ask it to assert the magnitude, but it is not misleading.

### B6. Permanently skipped / ignored tests with no tracking — **0 found**
- *Heuristic:* `#[ignore]` (Rust); `@pytest.mark.skip` / `@pytest.mark.xfail` decorators (pytest), minus conditional `skipif`/in-body `pytest.skip(reason=import-failure)`.
- *Instances:* **0** `#[ignore]` anywhere in `tools/`. The only unconditional `@pytest.mark.skip` is `qou-mass/tests/test_p2_integration.py:79`, and it carries an explicit tracked reason ("P2 only ships pre-computed shard rows… deep transitive deps … P3 vendoring work") — legitimate. All 16 `pytest.skip()` calls in `tools/pyhecke/tests/` are **conditional** (guarded by "not importable" / "upstream not available") — the correct pattern, not the anti-pattern.

## Part C — Check-design proposal

Mirror the Lean approach: a registry criterion + a skill for the judgment cases,
with a regex/AST automated layer for the cheap cases, reusing
`lp_dual_witness_validator.py` as the scanning model.

**Automatable vs. agent-judgment split.** B1 (empty tests), B4 (no-assert tests),
B5 (unwrap-only), B6 (untracked skip/ignore) are **cheaply regex/AST-automatable**
— a CI script can flag them deterministically. B2/B3 need a **two-stage**
treatment: a regex finds every `computed==expected` literal assertion (cheap), but
**classifying** each as legit-status-flag vs. faked-numeric-match needs **agent
judgment** (is `-2==-2` an honest construct or a skipped empirical comparison? is
`1836.152==1836.152` a CODATA load-check or a faked prediction?) — exactly the Lean
self-assuming-projection discriminator (does the assertion *exercise the quantity
it names*?).

**Wiring steps (actionable):**

1. **New automated validator** `folio-assistant/computations/tautological_assertion_validator.py`,
   structurally cloned from `lp_dual_witness_validator.py` (same walk-producers →
   flag → warn-only-default / `--strict` exit-1 shape). It greps every
   `add_assertion(...)` call where `computed`/`expected` are the same bare literal,
   splits into **flag class** (`{0,1,0.0,1.0}`) and **physical-literal class**
   (everything else), and prints `file:line + name`. Wire into
   `witness-pipeline.yml` warn-only, matching the LP-dual validator's CI posture.

2. **New QA criteria** in `content/pipeline/qa-criteria-registry.ts`, added to the
   existing `COMPUTE` array (auto-flows into the compute watcher axis), mirroring
   the `proof-no-*` family:
   - `compute-no-tautological-assertion` (automated regex layer = the validator in
     step 1; agent-confirmed for the physical-literal class) — analogue of
     `proof-no-trivial-true`.
   - `compute-no-faked-witness-match` (`automated: false`, agent-checked) — the
     assertion names a quantity but compares a constant to itself instead of the
     computed value (the `c_3` case) — analogue of `proof-no-self-assuming-projection`.
   - `compute-no-empty-test`, `compute-no-assertionless-test`,
     `compute-no-untracked-skip` (`automated: true`, regex/AST) — analogues of the
     run-but-never-check family.

3. **New skill** `.claude/skills/local/compute-vacuity-audit.md` (the COMPUTE
   sibling of `lean-proof-vacuity-audit.md`), `roles: [collaborator]`. It documents
   the B1–B6 family, the **single discriminator** ("does the assertion exercise the
   quantity it names, or compare a constant to itself?"), the legit-vs-anti list
   (status-flag `computed=1,expected=1` and CODATA load-checks are *honest*; faked
   empirical matches are *anti*), and the fix recipe: rewrite `computed=L,
   expected=L` → either (a) `computed=<actual_computed_var>, expected=<target>`
   when a real quantity exists (the `c_3` fix), or (b) keep the flag but **rename**
   to a non-value form (a dedicated `add_flag()` / `add_data("…_ran", True)`) so the
   witness JSON stops advertising a value-check that is really a status bit.

4. **Producer-API hardening (root-cause fix).** Add an optional
   `WitnessBuilder.add_flag(name, ran=True, source=...)` to
   `tools/qou-substrate/python/qou_substrate/witness.py` for the 146 boolean cases,
   and have the validator (step 1) recommend it. Separately, **fix the propagating
   template**: the `add_assertion` docstring at `witness.py:15` ships
   `computed=2.0298, expected=2.0298` as its example — that literal-equals-literal
   exemplar is what authors copy. Change the docstring example to compare a computed
   variable against a reference (`computed=vol_computed, expected=2.0298`).

5. **Dispatch row** in `.claude/skills/local/compute-integration-watcher.md` → route
   flagged physical-literal assertions to an agent running the new skill, which
   writes the `reviewer.kind="agent"` verdict into the block sidecar — identical to
   how `proof-integration-watcher` dispatches `lean-proof-review` for the
   `proof-no-*` criteria.

**Reuse note.** `lp_dual_witness_validator.py` already solves the hard
infrastructure (walk all witnesses, sibling-script resolution via `_sibling_script`,
hint-matching, warn/strict modes, CI integration) — the new validator is a ~1-day
clone, not greenfield. The agent-judgment criteria add **zero new checker files**
(per the Lean precedent's §"Minimal wiring": `qa-sweep` marks `automated:false`
criteria `needs-agent`, the watcher dispatches).

**Honest bottom line.** The compute stack does **not** have a vacuous-proof epidemic
the way the Lean tree did (219 stubs). Rust (`hecke-engine`, 195 tests) and
`pyhecke` (14 test files, real cross-engine numeric checks) are well-tested. The
single systemic issue is the **153 tautological witness assertions** — mostly a
benign-but-misleading status-flag convention (146) that should be renamed away from
value-check semantics, plus **~5–7 genuinely worth fixing** where a named empirical
quantity is asserted against a hardcoded constant instead of itself (strongest: the
two `c_3` `-2==-2` probes). That is the concrete, prioritizable backlog a
`compute-vacuity-audit` skill would drain.

## Status

This document is the **design + audit** deliverable (option 3 of the 2026-06-14
proof-vacuity work tranche). Implementation of the validator (step 1), criteria
(step 2), skill (step 3), and producer-API hardening (step 4) are follow-up work,
not yet landed.
