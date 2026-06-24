## 2026-06-24T00:09:42Z
You are teamwork_preview_worker.
Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_acoustic_horizon_conditions/`.
Your target file to modify is `content/quantum-observable-universe/lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean`.
The corresponding mathematical explanation is in `content/quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.md`.

Please:
1. Read the math context from the `.md` file to understand the theorem.
2. Read the target `.lean` file.
3. If it uses `ℝ`, `ℕ`, or `| |`, insert `import Mathlib` at the top of the file.
4. Prove the `acoustic_horizon_conditions` theorem using the hypotheses/fields provided in the `AcousticHorizonConditionsContext` typeclass.
5. Verify the correctness of your proof by running `lake build` or `./scripts/lean-verify.sh` on the package.
6. Write a `handoff.md` report in your working directory containing details of changes, verification commands run, and compilation output.
7. Send a message to parent ("56efc00f-fa8e-46a1-9b3e-0ab04a8ddcab") when complete.
8. Maintain and update `/Users/litlfred/space_cats/qou/.agents/worker_acoustic_horizon_conditions/progress.md` with a liveness heartbeat.

MANDATORY INTEGRITY WARNING:
> DO NOT CHEAT. All implementations must be genuine. DO NOT
> hardcode test results, create dummy/facade implementations, or
> circumvent the intended task. A Forensic Auditor will independently
> verify your work. Integrity violations WILL be detected and your
> work WILL be rejected.
