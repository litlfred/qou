# prepare-merge drift validators: the two "pre-existing failures" diagnosed

Date: 2026-07-19. Context: during `/prepare-merge` of PR #4096 two of the
five witness-drift validators failed identically on the feature branch and
on a clean `origin/main` worktree. Both are environment/invocation
artifacts, **not corpus regressions**:

1. **`derivation_chain_validator.py` (exit 2).** The only failing
   assertion was `c-q-q0.derivation.json`: stored target
   `c_q(q₀) = 9.092678397…` is the **muon-q₀** value (the
   `computations/` layer is muon-canonical per AGENTS.md §q₀ anchor
   convention), while the bare invocation re-evaluates at the runtime
   **proton-pinned** package q₀ (`1.10997858275…` → `9.092679456…`,
   rel_diff 1.16e-7 ≫ the 1e-12 tolerance). With `QOU_Q0_ANCHOR=ideal`
   the validator exits 0. Fix applied: `.claude/commands/prepare-merge.md`
   now prefixes all five validator invocations with `QOU_Q0_ANCHOR=ideal`
   (matching the error message `cross_check_trM_1ppb.py` itself emits).

2. **`cross_check_trM_1ppb.py` (exit 1).** Two sandbox gaps, no code bug:
   missing `numpy` (`pip install numpy` fixes) and the missing
   `pyhecke_native` Rust wheel (`chi_lambda_braid_mpf` raises
   `NotImplementedError: precision=mpfr_50dps requires the Rust kernel`;
   `maturin build` in `tools/pyhecke-native/` + `pip install` of the wheel
   fixes). On CI/owner machines with the wheel installed the validator is
   expected green under `QOU_Q0_ANCHOR=ideal`.

Practical rule for agents: run the five drift validators with
`QOU_Q0_ANCHOR=ideal`; treat a `cross_check` import error as an
environment gap and either build the wheel or document the skip — do not
report either failure as a branch defect without the clean-main control.
