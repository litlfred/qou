/**
 * The writer must refuse a verdict that asserts a violation without saying
 * what it found.
 *
 * `block-qa.schema.json` already states the rule on `result` — "fail =
 * violated (evidence must cite file:line + verbatim quote)" — but it lives in
 * a `description` string, and `evidence` is absent from the entry's `required`
 * list. The writer then did `if (evidence) entry.evidence = evidence;` and
 * wrote the verdict either way, so the corpus accumulated fail/warn entries
 * whose reason is nowhere on record.
 *
 * These tests pin the guard at the only place that can prevent more of them:
 * the writer. They are the agent-side counterpart of the rule already pinned
 * for script checkers — a checker that cannot read its evidence has not
 * verified anything.
 *
 * @module content/pipeline/qa-agent-entry.guard.test
 */
import { describe, expect, test } from "bun:test";
import { spawnSync } from "node:child_process";
import { mkdtempSync, readFileSync, writeFileSync, existsSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const WRITER = join(import.meta.dir, "qa-agent-entry.ts");

/** Run the writer against a throwaway block; return exit code + stderr. */
function run(result: string, evidence?: string) {
  const dir = mkdtempSync(join(tmpdir(), "qa-guard-"));
  const md = join(dir, "b.md");
  writeFileSync(md, "# block\n");
  const argv = [
    "run", WRITER,
    "--block", md,
    "--criterion", "da-overclaim",
    "--result", result,
  ];
  if (evidence !== undefined) argv.push("--evidence", evidence);
  const r = spawnSync("bun", argv, { encoding: "utf8" });
  // Since #7642 the derived report is under the instance's results tree; a
  // block outside any instance is its own instance root (block-qa-io.ts).
  const qa = join(dir, "test", "results", "block-qa", "b.qa.json");
  return {
    code: r.status,
    stderr: r.stderr ?? "",
    wrote: existsSync(qa),
    doc: existsSync(qa) ? JSON.parse(readFileSync(qa, "utf8")) : null,
  };
}

describe("qa-agent-entry evidence guard", () => {
  for (const result of ["fail", "warn"]) {
    test(`${result} without --evidence is refused, and writes nothing`, () => {
      const r = run(result);
      expect(r.code).toBe(2);
      expect(r.stderr).toContain("requires --evidence");
      // The refusal must be total: a rejected verdict that still landed in
      // the sidecar would be the very thing this guard exists to prevent.
      expect(r.wrote).toBe(false);
    });

    test(`${result} with whitespace-only --evidence is refused`, () => {
      // "   " is non-empty as a string but says exactly as much as "".
      const r = run(result, "   ");
      expect(r.code).toBe(2);
      expect(r.wrote).toBe(false);
    });

    test(`${result} with real evidence is accepted and recorded`, () => {
      const r = run(result, "b.md:1 — claims 'exact' on a float64 agreement");
      expect(r.code).toBe(0);
      expect(r.doc.criteria["da-overclaim"][0].evidence).toContain("float64");
    });
  }

  // The other half of the rule: a verdict that found nothing has nothing to
  // evidence. Spreading the guard to pass/n-a would hollow out the sweep from
  // the opposite side, so these must keep working bare.
  for (const result of ["pass", "n/a"]) {
    test(`${result} without --evidence still succeeds`, () => {
      const r = run(result);
      expect(r.code).toBe(0);
      expect(r.doc.criteria["da-overclaim"][0].result).toBe(result);
      expect(r.doc.criteria["da-overclaim"][0].evidence).toBeUndefined();
    });
  }

  test("an empty --evidence string is never recorded as a field", () => {
    const r = run("pass", "");
    expect(r.code).toBe(0);
    expect("evidence" in r.doc.criteria["da-overclaim"][0]).toBe(false);
  });
});
