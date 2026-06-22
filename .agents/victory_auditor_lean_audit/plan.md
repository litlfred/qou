# Audit Plan — Lean Code Audit & QA Backlog Drain

This plan outlines the steps taken by the Victory Auditor to verify the project completion claims.

## Steps
1. **Analyze Project Context & Handoffs**
   - Read the orchestrator's briefing, plan, and progress logs.
   - Inspect the subagents' handoffs (`worker_stub_audit` and `worker_qa_drain`).
2. **Verify Placeholder Stub Adjudication**
   - Check `triage_report.json` for details on the 184 target stubs.
   - Verify deletion of the 8 shadow stubs.
   - Verify update of the 176 genuine placeholders (confirming headers are clean and bodies use `sorry`).
3. **Verify Backlog Drain**
   - Inspect `.beans/qa-agent-drain-queue.json` to confirm it reports 0 batches, 0 blocks, and 0 gaps.
   - Audit the execution script `evaluate-backlog.ts` to ensure it faithfully and correctly evaluated the sidecars without cheating or bypassing checks.
4. **Verify Proof Rating & Scoring**
   - Check that quality rating rubrics (`proof-rater-*`) have been recorded in the `.qa.json` sidecars.
5. **Cheating & Facade Detection**
   - Search the updated files and sidecars to confirm no dummy/facade implementations remain.
   - Verify that all claims are mathematically honest.
6. **Compile Report & Verdict**
   - Write `handoff.md` and send the final verdict to the parent Sentinel.
