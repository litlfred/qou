/**
 * Regression guard for beans `qou-c7jp` / `qou-h43i`.
 *
 * A FILE-SCOPED run of the vacuity audit (the documented per-file CI gate,
 * `.github/workflows/lean-content-siblings.yml`) must NOT overwrite the
 * committed corpus-wide artifact
 * `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json`.
 *
 * History: the gate passes explicit `.lean` paths + `--quiet`, and for weeks
 * it silently rewrote the 2911-file corpus record with the tiny diff-scan
 * result — a 3,700-line deletion that reads as "the corpus is clean" over ~99
 * real defects (exit 0, no warning). Fixed by the guard in `main()`
 * (`roots.length > 0 && !jsonExplicit` ⇒ do not write the default path). This
 * test locks that invariant; there was no automated check before it.
 *
 * Run:  bun test content/pipeline/lean-vacuity-axiom-audit.guard.test.ts
 */
import { test, expect } from "bun:test";
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";
import { spawnSync } from "node:child_process";

const REPO_ROOT = resolve(import.meta.dir, "..", "..");
const ARTIFACT = resolve(
  REPO_ROOT,
  "docs/audits/2026-06-17-lean-vacuity-axiom-audit.json",
);
const SCRIPT = resolve(REPO_ROOT, "content/pipeline/lean-vacuity-axiom-audit.ts");
// Any one real corpus `.lean` file — the point is a partial (non-corpus) scope.
const ONE_FILE =
  "content/quantum-observable-universe/mass-theory/habiro-expansion-atomic.lean";

test("file-scoped vacuity audit leaves the committed corpus artifact untouched", () => {
  expect(existsSync(ARTIFACT)).toBe(true);
  const before = readFileSync(ARTIFACT);
  try {
    // Exactly the documented per-file gate invocation.
    const r = spawnSync(
      "bun",
      [
        "run",
        SCRIPT,
        ONE_FILE,
        "--quiet",
        "--fail-on",
        "proof-no-trivial-type-mismatch,lean-import-after-content",
      ],
      { cwd: REPO_ROOT, encoding: "utf8" },
    );
    // The gate must still FUNCTION (a clean/failing gate is 0/1; a crash is 2).
    expect([0, 1]).toContain(r.status);
    // The committed corpus artifact must be byte-identical after the run.
    const after = readFileSync(ARTIFACT);
    expect(after.equals(before)).toBe(true);
  } finally {
    // Fail-safe: if a future regression DID rewrite the artifact, restore its
    // committed content so this test can never leave a corrupted file staged.
    // On success this rewrites identical bytes (no diff).
    writeFileSync(ARTIFACT, before);
  }
});

test("a partial file-scoped scan may still write when an explicit --json path is given", () => {
  // The guard keys on the DEFAULT path only; a caller who names an output owns
  // it. Verify the escape hatch works so the guard cannot be "fixed" into
  // blocking legitimate scoped reports.
  const tmp = resolve(REPO_ROOT, "docs/audits/.vacuity-guard-selftest.json");
  try {
    const r = spawnSync(
      "bun",
      ["run", SCRIPT, ONE_FILE, "--quiet", "--json", tmp],
      { cwd: REPO_ROOT, encoding: "utf8" },
    );
    expect([0, 1]).toContain(r.status);
    expect(existsSync(tmp)).toBe(true);
  } finally {
    if (existsSync(tmp)) writeFileSync(tmp, ""); // truncate, then remove
    try {
      require("node:fs").unlinkSync(tmp);
    } catch {}
  }
});
