/**
 * Regression guard: `--review-ledger` must keep agent notes on entries that
 * are still `needs-agent`.
 *
 * History: on 2026-11-20 PR #8568 ran `--review-ledger`. The re-seed branch
 * rebuilt every `needs-agent` entry as a bare
 * `{category, pattern, line, verdict, file_sha}`, which stripped 374 fields of
 * earlier adjudication from 75 entries (`evidence`, `reviewer`, `disposition`,
 * `stale_prev_verdict`, `reviewed_at`, `source`, `agent_note`). #8576 restored
 * them from git. The owner approved fixing the tool (#8526, [W8b ask]).
 *
 * The test copies the committed ledger, plants a marker note on one live
 * `needs-agent` entry, runs `--review-ledger` against the copy, and checks
 * that the marker and the entry's existing notes survive.
 *
 * Run:  bun test folio/pipeline/lean-vacuity-ledger-needs-agent-notes.test.ts
 */
import { test, expect } from "bun:test";
import { readFileSync, writeFileSync, existsSync, unlinkSync } from "node:fs";
import { resolve } from "node:path";
import { spawnSync } from "node:child_process";

const REPO_ROOT = resolve(import.meta.dir, "..", "..");
const SCRIPT = resolve(REPO_ROOT, "folio/pipeline/lean-vacuity-axiom-audit.ts");
const COMMITTED = resolve(REPO_ROOT, "docs/audits/lean-vacuity-review-ledger.json");
const TMP = resolve(REPO_ROOT, "docs/audits/.ledger-notes-selftest.json");
/** Report goes here, never over the committed record (see `qou-9zh3`). */
const TMP_REPORT = resolve(REPO_ROOT, "docs/audits/.ledger-notes-selftest-report.json");
const CORPUS_RECORD = resolve(REPO_ROOT, "docs/audits/2026-06-17-lean-vacuity-axiom-audit.json");
const MARKER = "selftest: this note must survive --review-ledger";

test(
  "--review-ledger preserves agent notes on needs-agent entries",
  () => {
    const led = JSON.parse(readFileSync(COMMITTED, "utf-8"));
    // A live needs-agent entry whose file still exists, so it is among this
    // run's candidates and goes through the re-seed branch.
    const key = Object.keys(led.entries).find((k) => {
      const e = led.entries[k];
      return (
        e.verdict === "needs-agent" &&
        e.evidence !== undefined &&
        existsSync(resolve(REPO_ROOT, k.split("::")[0]))
      );
    });
    expect(key).toBeDefined();
    const before = led.entries[key!];
    led.entries[key!] = { ...before, agent_note: MARKER };
    writeFileSync(TMP, JSON.stringify(led, null, 2) + "\n");
    const recordBefore = existsSync(CORPUS_RECORD)
      ? readFileSync(CORPUS_RECORD, "utf-8")
      : undefined;
    try {
      const r = spawnSync(
        "bun",
        ["run", SCRIPT, "--quiet", "--review-ledger", TMP, "--json", TMP_REPORT],
        { cwd: REPO_ROOT, encoding: "utf8" },
      );
      expect([0, 1]).toContain(r.status);
      if (recordBefore !== undefined) {
        expect(readFileSync(CORPUS_RECORD, "utf-8")).toBe(recordBefore);
      }
      const after = JSON.parse(readFileSync(TMP, "utf-8")).entries[key!];
      expect(after).toBeDefined();
      expect(after.verdict).toBe("needs-agent");
      expect(after.agent_note).toBe(MARKER);
      expect(after.evidence).toBe(before.evidence);
      if (before.reviewer !== undefined) expect(after.reviewer).toEqual(before.reviewer);
    } finally {
      for (const f of [TMP, TMP_REPORT]) {
        if (existsSync(f)) {
          try {
            unlinkSync(f);
          } catch {}
        }
      }
    }
  },
  300_000,
);
