/**
 * Pins the bucketing in qa-evidence-audit.
 *
 * The case worth guarding hardest is STRUCTURED evidence. A first cut of this
 * audit tested `typeof ev === "string"`, which reported 35 of the
 * best-evidenced entries in the corpus — `[{ text: "file.md:18-20 '<quote>'" }]`,
 * precisely the file:line + verbatim quote the schema asks for — as
 * evidence-free. An audit that flags good evidence as missing is worse than no
 * audit, so that shape is pinned here.
 *
 * @module content/pipeline/qa-evidence-audit.test
 */
import { describe, expect, test } from "bun:test";
import { spawnSync } from "node:child_process";
import { mkdirSync, mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createHash } from "node:crypto";

const AUDIT = join(import.meta.dir, "qa-evidence-audit.ts");
const sha12 = (s: string) =>
  createHash("sha256").update(s).digest("hex").slice(0, 12);

/** Build a one-block corpus and audit it. `hash` picks the bucket. */
function audit(entry: Record<string, unknown>, hash: "match" | "wrong" | "none") {
  const root = mkdtempSync(join(tmpdir(), "qa-ev-"));
  mkdirSync(join(root, "ch"), { recursive: true });
  const md = "# block\n";
  writeFileSync(join(root, "ch", "b.md"), md);
  const field_hash =
    hash === "none"
      ? undefined
      : { md: hash === "match" ? sha12(md) : "0".repeat(12) };
  writeFileSync(
    join(root, "ch", "b.qa.json"),
    JSON.stringify({
      $schema: "block-qa/v1",
      criteria: {
        "da-overclaim": [
          { reviewer: { kind: "agent", id: "t" }, ...entry, ...(field_hash ? { field_hash } : {}) },
        ],
      },
    }),
  );
  const r = spawnSync("bun", ["run", AUDIT, "--root", root, "--json"], {
    encoding: "utf8",
  });
  return JSON.parse(r.stdout);
}

const FAIL = { result: "fail" };

describe("qa-evidence-audit", () => {
  test("structured evidence counts as present, not empty", () => {
    const out = audit(
      { ...FAIL, evidence: [{ text: "b.md:18-20 'claims exact'" }] },
      "match",
    );
    expect(out.empty_evidence).toBe(0);
  });

  test("an array of blank entries is still empty", () => {
    // The unwrap must not turn "structured" into "unconditionally present".
    const out = audit({ ...FAIL, evidence: [{ text: "  " }] }, "match");
    expect(out.empty_evidence).toBe(1);
  });

  test("plain-string evidence counts as present", () => {
    const out = audit({ ...FAIL, evidence: "b.md:1 quote" }, "match");
    expect(out.empty_evidence).toBe(0);
  });

  test("a matching field_hash buckets as live", () => {
    const out = audit(FAIL, "match");
    expect(out.by_bucket).toMatchObject({ live: 1, stale: 0, unhashed: 0 });
    expect(out.live_blocks).toBe(1);
  });

  test("a superseded field_hash buckets as stale, not live", () => {
    const out = audit(FAIL, "wrong");
    expect(out.by_bucket).toMatchObject({ live: 0, stale: 1 });
  });

  test("a missing field_hash buckets as unhashed, not live", () => {
    // Neither live nor stale: it can never be resolved to a block version.
    const out = audit(FAIL, "none");
    expect(out.by_bucket).toMatchObject({ live: 0, stale: 0, unhashed: 1 });
  });

  test("pass verdicts are never reported, evidence or not", () => {
    expect(audit({ result: "pass" }, "match").empty_evidence).toBe(0);
    expect(audit({ result: "n/a" }, "match").empty_evidence).toBe(0);
  });

  test("script-authored entries are out of scope", () => {
    const out = audit(
      { ...FAIL, reviewer: { kind: "script", id: "s" } },
      "match",
    );
    expect(out.total_agent_fail_warn).toBe(0);
  });

  // The distinction the audit exists to make. Its first cut counted an empty
  // `evidence` as "this verdict says nothing", which measured 1302 such
  // entries corpus-wide. Every one of them turned out to record a substantive
  // reason under `notes` — citing file:line, e.g. "...braid.lean:22:28:
  // error(...)". The truly-silent count is ZERO. Reporting a schema-key
  // mismatch as an accountability void is a far more serious claim, and false.
  test("a reason under `notes` is misfiled, not silent", () => {
    const out = audit(
      { ...FAIL, notes: "b.lean:22:28: error(lean.unknownIdentifier)" },
      "match",
    );
    expect(out.empty_evidence).toBe(1);
    expect(out.by_accountability).toMatchObject({ misfiled: 1, silent: 0 });
    expect(out.live_silent).toBe(0);
  });

  test("`referee_argument` also counts as misfiled, not silent", () => {
    const out = audit({ ...FAIL, referee_argument: "open-objection: b.md:4" }, "match");
    expect(out.by_accountability).toMatchObject({ misfiled: 1, silent: 0 });
  });

  test("no reason under any key is silent", () => {
    const out = audit(FAIL, "match");
    expect(out.by_accountability).toMatchObject({ misfiled: 0, silent: 1 });
    expect(out.live_silent).toBe(1);
  });

  test("--strict ignores a misfiled reason and fires only on a silent one", () => {
    const root = mkdtempSync(join(tmpdir(), "qa-ev-strict-"));
    const run = () =>
      spawnSync("bun", ["run", AUDIT, "--root", root, "--strict"], {
        encoding: "utf8",
      }).status;
    expect(run()).toBe(0); // empty corpus
    mkdirSync(join(root, "ch"), { recursive: true });
    const md = "# b\n";
    writeFileSync(join(root, "ch", "b.md"), md);
    const write = (extra: Record<string, unknown>) =>
      writeFileSync(
        join(root, "ch", "b.qa.json"),
        JSON.stringify({
          criteria: {
            c: [
              {
                reviewer: { kind: "agent", id: "t" },
                result: "fail",
                field_hash: { md: sha12(md) },
                ...extra,
              },
            ],
          },
        }),
      );

    // A live verdict whose reason sits in `notes` is misfiled, not silent —
    // that is a key migration, and failing the gate on 1302 of them would
    // make it unusable on arrival.
    write({ notes: "b.md:1 — the claim outruns the Lean" });
    expect(run()).toBe(0);

    // No reason under any key: this is what the gate is for.
    write({});
    expect(run()).toBe(1);
  });
});
