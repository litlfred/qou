import { describe, expect, test } from "bun:test";
import { spawnSync } from "child_process";
import { mkdtempSync, writeFileSync, readFileSync, existsSync } from "fs";
import { tmpdir } from "os";
import { join } from "path";

/**
 * An agent `fail`/`warn` with no evidence asserts a defect nobody can check,
 * re-adjudicate, or act on — and it survives every `qa-sweep` run, because the
 * sweep re-runs SCRIPT criteria only.
 *
 * `block-qa.schema.json` already states the contract, on `result`: "fail =
 * violated (evidence must cite file:line + verbatim quote)". But that is
 * prose — `evidence` is absent from the entry's `required` list, and the only
 * consumer that reads the schema at all is `qa-flag-preservation-audit.ts`. So
 * nothing checked it, and by 2026-08-24 **303 of the corpus's 1,442 agent
 * fail/warn verdicts carried an empty evidence string**, six criteria at 100 %
 * (`expo-milnor-clarity` 210/210, `da-referee-verdict` 16/16,
 * `da-lean-narrative-divergence` 9/9, `fit-section-chapter` 7/7).
 *
 * This is the agent-side mirror of the rule the platform already pins for
 * script checkers in `checker-missing-evidence.test.ts`: a checker that cannot
 * read its evidence has not verified anything.
 *
 * The bar is NON-EMPTY, not quote-shaped, and that is deliberate: some
 * legitimate evidence is a bare `file.lean:1` pointer, and demanding a quote
 * would push authors toward inventing one. Whether evidence is *quotable* is
 * measured separately and advisorily by `scripts/qa-stale-agent-evidence.py`.
 */
const ENTRY = join(import.meta.dir, "qa-agent-entry.ts");

function run(args: string[], cwd: string) {
  return spawnSync("bun", ["run", ENTRY, ...args], {
    cwd,
    encoding: "utf-8",
    timeout: 60_000,
  });
}

/** A block .md + .ts pair the writer will accept, in a throwaway dir. */
function fixture(): { dir: string; md: string } {
  const dir = mkdtempSync(join(tmpdir(), "qa-agent-entry-"));
  const md = join(dir, "sample-block.md");
  writeFileSync(md, "A statement about the mathematics.\n");
  writeFileSync(
    join(dir, "sample-block.ts"),
    'export default { kind: "lemma", label: "lem:sample-block", title: "Sample" };\n',
  );
  return { dir, md };
}

describe("qa-agent-entry refuses an evidence-free fail/warn", () => {
  for (const result of ["fail", "warn"]) {
    test(`--result ${result} with no --evidence exits non-zero`, () => {
      const { dir, md } = fixture();
      const r = run(["--block", md, "--criterion", "trap-superlative", "--result", result], dir);
      expect(r.status).not.toBe(0);
      expect(r.stderr).toContain("requires --evidence");
      // and it must not have written a sidecar
      expect(existsSync(join(dir, "sample-block.qa.json"))).toBe(false);
    });

    test(`--result ${result} with whitespace-only --evidence also exits non-zero`, () => {
      const { dir, md } = fixture();
      const r = run(
        ["--block", md, "--criterion", "trap-superlative", "--result", result, "--evidence", "   "],
        dir,
      );
      expect(r.status).not.toBe(0);
      expect(r.stderr).toContain("requires --evidence");
    });
  }

  test("--result fail WITH evidence is accepted and records it", () => {
    const { dir, md } = fixture();
    const r = run(
      [
        "--block", md, "--criterion", "trap-superlative", "--result", "fail",
        "--evidence", "sample-block.md:1 'A statement about the mathematics.'",
      ],
      dir,
    );
    expect(r.status).toBe(0);
    const sidecar = join(dir, "sample-block.qa.json");
    expect(existsSync(sidecar)).toBe(true);
    const d = JSON.parse(readFileSync(sidecar, "utf-8"));
    const entry = d.criteria["trap-superlative"].at(-1);
    expect(entry.result).toBe("fail");
    expect(entry.evidence).toContain("sample-block.md:1");
  });

  // The guard must not spread to verdicts that have nothing to evidence.
  for (const result of ["pass", "n/a"]) {
    test(`--result ${result} with no --evidence is still accepted`, () => {
      const { dir, md } = fixture();
      const r = run(["--block", md, "--criterion", "trap-superlative", "--result", result], dir);
      expect(r.status).toBe(0);
    });
  }
});
