/**
 * The writer must record WHICH VERSION of the block it reviewed.
 *
 * An entry with no `field_hash` is neither live nor stale: it can never be
 * resolved to a block version, so no consumer can decide whether it still
 * applies, and `qa-agent-drain-queue.ts` (which gates on `field_hash.md`)
 * cannot use it to suppress a re-review. An entry whose `field_hash` omits a
 * sibling that EXISTS is worse in one specific way — it looks resolvable and
 * silently is not for that file, so a verdict about the `.lean` survives
 * arbitrary later edits to that `.lean`.
 *
 * Both were real. Measured 2026-08-29 over all 3,617 sidecars: 53,293 of
 * 99,743 agent verdicts carry no `field_hash` at all, against 179,959 script
 * verdicts of which every single one does. Separately, the writer built its
 * `field_hash` from `.md` and `.ts` only, never `.lean` (fixed in #5946).
 *
 * Both causes are now gone from the tree — the ad-hoc writers responsible were
 * deleted in `9ddf0ad9c0`, the three surviving Python writers each hash all
 * three siblings, and the `.lean` omission is fixed. This file exists because
 * nothing PREVENTED any of it: the sibling guard test pins `evidence`, and
 * `field_hash` is absent from the schema's `required` list, so the next writer
 * to be added can reintroduce the whole class in silence.
 *
 * @module content/pipeline/qa-agent-entry.fieldhash.test
 */
import { describe, expect, test } from "bun:test";
import { spawnSync } from "node:child_process";
import { mkdtempSync, readFileSync, writeFileSync, existsSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const WRITER = join(import.meta.dir, "qa-agent-entry.ts");

/** Write a throwaway block with the requested siblings; run the writer on it. */
function run(siblings: { ts?: boolean; lean?: boolean }) {
  const dir = mkdtempSync(join(tmpdir(), "qa-fh-"));
  const md = join(dir, "b.md");
  writeFileSync(md, "# block\n\nbody\n");
  if (siblings.ts) writeFileSync(join(dir, "b.ts"), "export const x = 1;\n");
  if (siblings.lean) writeFileSync(join(dir, "b.lean"), "theorem t : True := trivial\n");
  const r = spawnSync("bun", [
    "run", WRITER,
    "--block", md,
    "--criterion", "da-overclaim",
    "--result", "pass",
    "--id", "local/fieldhash-test",
  ], { encoding: "utf8" });
  const qa = join(dir, "b.qa.json");
  return {
    code: r.status,
    stderr: r.stderr ?? "",
    dir,
    md,
    entry: existsSync(qa)
      ? JSON.parse(readFileSync(qa, "utf8")).criteria["da-overclaim"].at(-1)
      : null,
  };
}

describe("qa-agent-entry field_hash guard", () => {
  test("every entry carries a field_hash", () => {
    const r = run({ ts: true, lean: true });
    expect(r.code).toBe(0);
    expect(r.entry?.field_hash).toBeDefined();
  });

  test("hashes every sibling that exists — .lean included", () => {
    const r = run({ ts: true, lean: true });
    expect(Object.keys(r.entry.field_hash).sort()).toEqual(["lean", "lean_statement", "md", "ts"]);
  });

  // A key must be ABSENT when the sibling is, not present-and-empty: a
  // consumer comparing hashes would read an empty string as a real value and
  // call an unchanged block stale on every run.
  test("omits the key for a sibling that does not exist", () => {
    const r = run({ ts: true, lean: false });
    expect(Object.keys(r.entry.field_hash).sort()).toEqual(["md", "ts"]);
    expect("lean" in r.entry.field_hash).toBe(false);
  });

  test("md alone is enough — no sibling is required", () => {
    const r = run({});
    expect(r.code).toBe(0);
    expect(Object.keys(r.entry.field_hash)).toEqual(["md"]);
  });

  // The point of the hash: it must actually track the content. A digest that
  // never moves would satisfy every test above and pin nothing.
  test("the hash tracks the .lean content, not merely its existence", () => {
    const a = run({ lean: true });
    const before = a.entry.field_hash.lean;
    writeFileSync(join(a.dir, "b.lean"), "theorem t : 1 = 1 := rfl\n");
    const r = spawnSync("bun", [
      "run", WRITER,
      "--block", a.md,
      "--criterion", "da-overclaim",
      "--result", "pass",
      "--id", "local/fieldhash-test",
    ], { encoding: "utf8" });
    expect(r.status).toBe(0);
    const after = JSON.parse(
      readFileSync(join(a.dir, "b.qa.json"), "utf8"),
    ).criteria["da-overclaim"].at(-1).field_hash.lean;
    expect(after).not.toBe(before);
  });
});
