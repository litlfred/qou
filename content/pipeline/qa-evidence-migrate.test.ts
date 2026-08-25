/**
 * Pins the migration's safety properties.
 *
 * This script rewrites 1302 entries across 645 committed sidecars, so the
 * properties that matter are the ones that keep it from doing damage:
 * it must never invent evidence, never move text out of a field live
 * consumers read, never touch an already-evidenced entry, and be safe to
 * re-run.
 *
 * @module content/pipeline/qa-evidence-migrate.test
 */
import { describe, expect, test } from "bun:test";
import { spawnSync } from "node:child_process";
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const SCRIPT = join(import.meta.dir, "qa-evidence-migrate.ts");

function corpus(entry: Record<string, unknown>) {
  const root = mkdtempSync(join(tmpdir(), "qa-mig-"));
  mkdirSync(join(root, "ch"), { recursive: true });
  writeFileSync(join(root, "ch", "b.md"), "# b\n");
  writeFileSync(
    join(root, "ch", "b.qa.json"),
    JSON.stringify({
      $schema: "block-qa/v1",
      criteria: {
        "da-overclaim": [
          { reviewer: { kind: "agent", id: "t" }, result: "fail", ...entry },
        ],
      },
    }),
  );
  return root;
}
const run = (root: string, apply = true) =>
  spawnSync("bun", ["run", SCRIPT, "--root", root, ...(apply ? ["--apply"] : [])], {
    encoding: "utf8",
  }).stdout;
const entryOf = (root: string) =>
  JSON.parse(readFileSync(join(root, "ch", "b.qa.json"), "utf8")).criteria[
    "da-overclaim"
  ][0];

describe("qa-evidence-migrate", () => {
  test("copies `notes` into `evidence` verbatim", () => {
    const root = corpus({ notes: "b.lean:22:28: error(unknownIdentifier)" });
    run(root);
    const e = entryOf(root);
    expect(e.evidence).toBe("b.lean:22:28: error(unknownIdentifier)");
  });

  test("LEAVES `notes` in place — live consumers read it", () => {
    // qa-flag-preservation-audit.ts, proof-axis-dashboard.ts, qa-sweep.ts and
    // qa-merge-findings.ts all read `.notes`. Moving would break them all to
    // fix a schema-conformance problem.
    const root = corpus({ notes: "the claim outruns the Lean" });
    run(root);
    expect(entryOf(root).notes).toBe("the claim outruns the Lean");
  });

  test("falls back to `referee_argument` when there are no notes", () => {
    const root = corpus({ referee_argument: "open-objection: b.md:4" });
    run(root);
    expect(entryOf(root).evidence).toBe("open-objection: b.md:4");
  });

  test("NEVER invents evidence when no reason exists", () => {
    // Fabricating a justification is the precise failure this whole effort
    // is about; the entry must be left alone and counted as skipped.
    const root = corpus({});
    const out = run(root);
    expect(entryOf(root).evidence).toBeUndefined();
    expect(out).toContain("skipped, no reason to copy: 1");
  });

  test("does not overwrite evidence that is already present", () => {
    const root = corpus({ evidence: "original", notes: "a note" });
    run(root);
    expect(entryOf(root).evidence).toBe("original");
  });

  test("leaves structured evidence alone", () => {
    const root = corpus({ evidence: [{ text: "b.md:1 'x'" }], notes: "n" });
    run(root);
    expect(entryOf(root).evidence).toEqual([{ text: "b.md:1 'x'" }]);
  });

  test("is idempotent — a second run migrates nothing", () => {
    const root = corpus({ notes: "reason" });
    expect(run(root)).toContain("entries migrated : 1");
    expect(run(root)).toContain("entries migrated : 0");
  });

  test("dry run writes nothing", () => {
    const root = corpus({ notes: "reason" });
    const out = run(root, false);
    expect(out).toContain("DRY RUN");
    expect(entryOf(root).evidence).toBeUndefined();
  });

  test("ignores pass verdicts and script reviewers", () => {
    const pass = corpus({ result: "pass", notes: "n" });
    run(pass);
    expect(entryOf(pass).evidence).toBeUndefined();

    const script = corpus({ reviewer: { kind: "script", id: "s" }, notes: "n" });
    run(script);
    expect(entryOf(script).evidence).toBeUndefined();
  });
});
