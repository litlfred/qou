/**
 * Regression guard for bean `qou-sycn`.
 *
 * `--review-ledger` must NOT delete entries in categories this audit does not
 * produce. The review ledger is SHARED — other tools and hand adjudications
 * write into it under their own category names — and the "drop entries whose
 * candidate no longer flags (resolved/fixed)" loop cannot tell one of those
 * from a finding that has been fixed.
 *
 * History: measured on `main` 2026-08-30, a single `--review-ledger` run
 * deleted **116 of 268 entries** — 104 `proof-borrowed-name`, 7
 * `proof-zero-placeholder`, and one each of `name-overload`,
 * `proof-docstring-body-mismatch`, `proof-vacuous-hypotheses` — taking **38
 * `genuine`, 56 `legit` and 22 `advisory` agent verdicts** with them. None of
 * those five categories is emitted by any script in the tree, so the verdicts
 * were not recoverable by re-running anything. The run's printed summary said
 * only "N candidate(s)"; nothing announced the loss.
 *
 * The fix derives an OWNED set from `SEVERITY` and skips anything outside it.
 * This test locks it, because the guard is a `continue` inside a delete loop —
 * precisely the shape a later refactor removes as redundant.
 *
 * Run:  bun test content/pipeline/lean-vacuity-ledger-foreign-entries.test.ts
 */
import { test, expect } from "bun:test";
import { readFileSync, writeFileSync, existsSync, unlinkSync } from "node:fs";
import { resolve } from "node:path";
import { spawnSync } from "node:child_process";

const REPO_ROOT = resolve(import.meta.dir, "..", "..");
const SCRIPT = resolve(REPO_ROOT, "content/pipeline/lean-vacuity-axiom-audit.ts");
const TMP = resolve(REPO_ROOT, "docs/audits/.ledger-foreign-selftest.json");

/** A category no detector in this repo emits, carrying an agent verdict. */
const FOREIGN_KEY =
  "content/quantum-observable-universe/lean/QOU/Nonexistent.lean::QOU.Fake.Decl::proof-borrowed-name";
/** Same shape, but in a category this audit DOES own and cannot be flagging. */
const OWNED_STALE_KEY =
  "content/quantum-observable-universe/lean/QOU/Nonexistent.lean::QOU.Fake.Decl::proof-no-trivial-true";

// A full `--review-ledger` run scans the whole corpus (3269 `.lean` as of
// 2026-08-30, ~60 s). Bun's 5 s default kills it mid-run, and the process then
// reports `status: null` — which reads as a crash rather than as a timeout.
const CORPUS_SCAN_TIMEOUT_MS = 300_000;

test(
  "--review-ledger preserves entries in categories this audit does not produce",
  () => {
  const seeded = {
    $schema: "lean-vacuity-review/v1",
    updated_at: "2026-08-30T00:00:00.000Z",
    entries: {
      [FOREIGN_KEY]: {
        category: "proof-borrowed-name",
        pattern: "borrowed-name",
        line: 1,
        verdict: "genuine",
        file_sha: "deadbeefcafe",
      },
      [OWNED_STALE_KEY]: {
        category: "proof-no-trivial-true",
        pattern: "placeholder-true",
        line: 1,
        verdict: "genuine",
        file_sha: "deadbeefcafe",
      },
    },
  };
  writeFileSync(TMP, JSON.stringify(seeded, null, 2) + "\n");
  try {
    const r = spawnSync("bun", ["run", SCRIPT, "--quiet", "--review-ledger", TMP], {
      cwd: REPO_ROOT,
      encoding: "utf8",
    });
    expect([0, 1]).toContain(r.status); // must still function, not crash

    const after = JSON.parse(readFileSync(TMP, "utf-8"));

    // The foreign entry survives, verdict intact. This is the whole point:
    // another tool's adjudication is not this audit's to resolve or discard.
    expect(after.entries[FOREIGN_KEY]).toBeDefined();
    expect(after.entries[FOREIGN_KEY].verdict).toBe("genuine");

    // The owned entry names a file that does not exist, so it cannot be among
    // this run's candidates and IS correctly dropped as resolved. Asserting
    // this keeps the guard honest: a version that simply stopped deleting
    // anything would pass the check above while breaking the ledger's ability
    // to retire fixed findings.
    expect(after.entries[OWNED_STALE_KEY]).toBeUndefined();
    } finally {
      if (existsSync(TMP)) {
        try {
          unlinkSync(TMP);
        } catch {}
      }
    }
  },
  CORPUS_SCAN_TIMEOUT_MS,
);
