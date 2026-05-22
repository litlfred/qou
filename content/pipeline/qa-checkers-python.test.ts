/**
 * Regression tests for `qa-checkers-python.ts`.
 *
 * Standalone driver, no test framework — `bun run`:
 *
 *   bun run content/pipeline/qa-checkers-python.test.ts
 *
 * Exits non-zero on any failure. Each test fixture is a short Python
 * snippet written to a temp file; we run the checker and assert on
 * the resulting hit set. The fixtures here lock in the cluster-B
 * fixes from PR #872 (sentinel masking, double-flag avoidance,
 * string + comment exemption) so future regex tweaks can't silently
 * break them.
 *
 * @module content/pipeline/qa-checkers-python.test
 */

import { mkdtempSync, writeFileSync, rmSync } from "fs";
import { tmpdir } from "os";
import { join } from "path";
import { checkDoesNotDefaultToFloat } from "./qa-checkers-python";

interface Case {
  name: string;
  source: string;
  expect: {
    /** Number of bare-float-literal hits expected. */
    bare_literals: number;
    /** Number of `float(...)` cast hits expected. */
    float_casts: number;
  };
}

const CASES: Case[] = [
  {
    name: "float('inf') sentinel is exempt",
    source: 'x = float("inf")\n',
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "float('nan') sentinel is exempt",
    source: "y = float('nan')\n",
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "float('-inf') sentinel is exempt",
    source: 'z = float("-inf")\n',
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "float(1.0) is reported ONCE as a cast (no double-flag)",
    source: "a = float(1.0)\n",
    expect: { bare_literals: 0, float_casts: 1 },
  },
  {
    name: "float(x) on a name is a cast hit, no literal hit",
    source: "b = float(x)\n",
    expect: { bare_literals: 0, float_casts: 1 },
  },
  {
    name: "bare float literal outside any cast is reported once",
    source: "c = 1.5\n",
    expect: { bare_literals: 1, float_casts: 0 },
  },
  {
    name: "scientific notation literal is reported",
    source: "d = 3.14e-10\n",
    expect: { bare_literals: 1, float_casts: 0 },
  },
  {
    name: "float literal inside a `#` comment is exempt",
    source: "e = 1  # set to 1.5 later\n",
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "float literal inside a single-line string is exempt",
    source: 'f = "value is 1.5 by default"\n',
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "float literal inside a triple-quoted docstring is exempt",
    source: '"""\nDoc says 1.0 is allowed here.\n"""\ng = 1\n',
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "mpmath.mpf('0.5') string arg is exempt",
    source: 'from mpmath import mpf\nh = mpf("0.5")\n',
    expect: { bare_literals: 0, float_casts: 0 },
  },
  {
    name: "two bare literals on one line each report",
    source: "i = 1.0 + 2.0\n",
    expect: { bare_literals: 2, float_casts: 0 },
  },
  {
    name: "cast + unrelated literal both report (separately)",
    source: "j = float(x) + 2.0\n",
    expect: { bare_literals: 1, float_casts: 1 },
  },
  {
    name: "no floats at all → pass with zero hits",
    source: "k = 1\nl = 'plain string'\n",
    expect: { bare_literals: 0, float_casts: 0 },
  },
];

function bucketHits(hits: { text: string }[]): {
  bare_literals: number;
  float_casts: number;
} {
  let bare_literals = 0;
  let float_casts = 0;
  for (const h of hits) {
    if (h.text.startsWith("bare float literal")) bare_literals++;
    else if (h.text.startsWith("bare `float(")) float_casts++;
  }
  return { bare_literals, float_casts };
}

function run(): void {
  const dir = mkdtempSync(join(tmpdir(), "qa-checkers-python-"));
  let failures = 0;
  let passes = 0;
  try {
    for (const c of CASES) {
      const file = join(dir, "fixture.py");
      writeFileSync(file, c.source);
      const res = checkDoesNotDefaultToFloat(file);
      const got = bucketHits(res.hits);
      const ok =
        got.bare_literals === c.expect.bare_literals &&
        got.float_casts === c.expect.float_casts;
      if (ok) {
        passes++;
        console.log(`  PASS  ${c.name}`);
      } else {
        failures++;
        console.log(
          `  FAIL  ${c.name}\n` +
            `        expected bare=${c.expect.bare_literals} ` +
            `casts=${c.expect.float_casts}\n` +
            `        got      bare=${got.bare_literals} ` +
            `casts=${got.float_casts}\n` +
            `        hits:\n` +
            res.hits
              .map((h) => `          - ${h.text.slice(0, 80)}`)
              .join("\n"),
        );
      }
    }
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
  console.log(`\n  ${passes} passed, ${failures} failed`);
  if (failures > 0) process.exit(1);
}

run();
