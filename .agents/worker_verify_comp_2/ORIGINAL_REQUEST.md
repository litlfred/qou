## 2026-06-20T11:50:45Z
You are a teamwork_preview_worker.
Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_verify_comp_2`.
The project workspace is `/Users/litlfred/space_cats/qou`.

Your objective is to:
1. Warm up the Lean toolchain and cache by running `./scripts/setup-lean-toolchain.sh`.
2. Run `lake build` to verify that the whole library compiles with zero errors.
3. Write a handoff report documenting the commands run and output results, and save it in your working directory.
4. Notify the parent agent with the path to the handoff.

Guidelines:
- When calling `run_command`, set a reasonable `WaitMsBeforeAsync` (e.g. 5000ms). If the command goes to the background, check its status and wait for it to complete.
- Verify that a final `lake build` succeeds with zero errors across the package.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Update your `progress.md` and send a message back with your handoff.md path when done.
