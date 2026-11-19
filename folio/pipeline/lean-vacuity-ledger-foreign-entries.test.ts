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
const SCRIPT = resolve(REPO_ROOT, "folio/pipeline/lean-vacuity-axiom-audit.ts");
const TMP = resolve(REPO_ROOT, "docs/audits/.ledger-foreign-selftest.json");
/**
 * Where this run's REPORT goes.  Naming it is not cosmetic — see `qou-9zh3`.
 *
 * This is a WHOLE-CORPUS scan, so `qou-c7jp`'s guard (which refuses to write the
 * committed record from a *partial* scan) does not fire, and without `--json` the
 * run overwrote `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` with
 * promotions computed against the two-entry fixture below: `total_defects` 114 ->
 * 67, `total_promoted_from_exempt` 53 -> 0.  Not a stale snapshot — a fabricated
 * one, written from a test fixture, every time `bun test` ran.
 */
const TMP_REPORT = resolve(REPO_ROOT, "docs/audits/.ledger-foreign-selftest-report.json");
/** The committed corpus record this test must leave alone. */
const CORPUS_RECORD = resolve(
  REPO_ROOT,
  "docs/audits/2026-06-17-lean-vacuity-axiom-audit.json",
);

/** A category no detector in this repo emits, carrying an agent verdict. */
const FOREIGN_KEY =
  "folio/quantum-observable-universe/lean/QOU/Nonexistent.lean::QOU.Fake.Decl::proof-borrowed-name";
/** Same shape, but in a category this audit DOES own and cannot be flagging. */
const OWNED_STALE_KEY =
  "folio/quantum-observable-universe/lean/QOU/Nonexistent.lean::QOU.Fake.Decl::proof-no-trivial-true";

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
  // Snapshot the committed corpus record so the assertion below can prove this
  // test did not touch it.
  const recordBefore = existsSync(CORPUS_RECORD)
    ? readFileSync(CORPUS_RECORD, "utf-8")
    : undefined;
  try {
    const r = spawnSync(
      "bun",
      ["run", SCRIPT, "--quiet", "--review-ledger", TMP, "--json", TMP_REPORT],
      {
        cwd: REPO_ROOT,
        encoding: "utf8",
      },
    );
    expect([0, 1]).toContain(r.status); // must still function, not crash

    // `qou-9zh3`: the run must not have rewritten the committed corpus record.
    // This is the assertion the defect would have failed, and it is deliberately
    // a byte comparison — the damage was to *values* inside a file that still
    // parsed and still looked like a report.
    if (recordBefore !== undefined) {
      expect(readFileSync(CORPUS_RECORD, "utf-8")).toBe(recordBefore);
    }

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
      for (const f of [TMP, TMP_REPORT]) {
        if (existsSync(f)) {
          try {
            unlinkSync(f);
          } catch {}
        }
      }
    }
  },
  CORPUS_SCAN_TIMEOUT_MS,
);
