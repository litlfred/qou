/**
 * Regression tests for the script-quality Python checker.
 *
 * Locks in the masking-bug fixes (sentinel exemption against the
 * original source line; `float(...)` cast scan that does not
 * double-flag inner literals) and the regex-robustness improvements
 * (PEP 515 underscores, one level of nested parens, multiline
 * casts).
 *
 * Run via the standard `bun test` harness:
 *
 *     ./scripts/tests/run-tests.sh
 *     # or
 *     cd scripts/tests && bun test qa-checkers-python.test.ts
 */

import { describe, test, expect } from "bun:test";
import { mkdtempSync, writeFileSync, rmSync } from "fs";
import { tmpdir } from "os";
import { join } from "path";
import { checkDoesNotDefaultToFloat } from "../../content/pipeline/qa-checkers-python";

function runChecker(source: string): {
  bare_literals: number;
  float_casts: number;
  hits: Array<{ text: string }>;
} {
  const dir = mkdtempSync(join(tmpdir(), "qa-checkers-python-"));
  try {
    const file = join(dir, "fixture.py");
    writeFileSync(file, source);
    const res = checkDoesNotDefaultToFloat(file);
    let bare_literals = 0;
    let float_casts = 0;
    for (const h of res.hits) {
      if (h.text.startsWith("bare float literal")) bare_literals++;
      else if (h.text.startsWith("bare `float(")) float_casts++;
    }
    return { bare_literals, float_casts, hits: res.hits };
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

describe("checkDoesNotDefaultToFloat — sentinel exemption", () => {
  test("float('inf') is exempt", () => {
    const r = runChecker('x = float("inf")\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("float('nan') is exempt", () => {
    const r = runChecker("y = float('nan')\n");
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("float('-inf') is exempt", () => {
    const r = runChecker('z = float("-inf")\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("float('infinity') is exempt (Python long form)", () => {
    const r = runChecker('a = float("infinity")\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("sentinel exemption is case-insensitive", () => {
    const r = runChecker('a = float("INF")\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });
});

describe("checkDoesNotDefaultToFloat — no double-flag", () => {
  test("float(1.0) is reported ONCE as a cast", () => {
    const r = runChecker("a = float(1.0)\n");
    expect(r.bare_literals).toBe(0);
    expect(r.float_casts).toBe(1);
  });

  test("float(x) on a name is a cast hit, no literal hit", () => {
    const r = runChecker("b = float(x)\n");
    expect(r.bare_literals).toBe(0);
    expect(r.float_casts).toBe(1);
  });
});

describe("checkDoesNotDefaultToFloat — bare literals", () => {
  test("bare float literal outside any cast is reported once", () => {
    const r = runChecker("c = 1.5\n");
    expect(r.bare_literals).toBe(1);
    expect(r.float_casts).toBe(0);
  });

  test("scientific notation literal is reported", () => {
    const r = runChecker("d = 3.14e-10\n");
    expect(r.bare_literals).toBe(1);
    expect(r.float_casts).toBe(0);
  });

  test("two bare literals on one line each report", () => {
    const r = runChecker("i = 1.0 + 2.0\n");
    expect(r.bare_literals).toBe(2);
    expect(r.float_casts).toBe(0);
  });

  test("cast + unrelated literal both report", () => {
    const r = runChecker("j = float(x) + 2.0\n");
    expect(r.bare_literals).toBe(1);
    expect(r.float_casts).toBe(1);
  });
});

describe("checkDoesNotDefaultToFloat — string + comment exemption", () => {
  test("float literal inside a `#` comment is exempt", () => {
    const r = runChecker("e = 1  # set to 1.5 later\n");
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("float literal inside a single-line string is exempt", () => {
    const r = runChecker('f = "value is 1.5 by default"\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("float literal inside a triple-quoted docstring is exempt", () => {
    const r = runChecker('"""\nDoc says 1.0 is allowed here.\n"""\ng = 1\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("mpmath.mpf('0.5') string arg is exempt", () => {
    const r = runChecker('from mpmath import mpf\nh = mpf("0.5")\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("no floats at all → pass with zero hits", () => {
    const r = runChecker("k = 1\nl = 'plain string'\n");
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });
});

describe("checkDoesNotDefaultToFloat — PEP 515 underscores", () => {
  test("1_000.5 is reported as a bare float literal", () => {
    const r = runChecker("m = 1_000.5\n");
    expect(r.bare_literals).toBe(1);
    expect(r.hits[0].text).toContain("1_000.5");
  });

  test("1.5_5e1_0 (underscore in mantissa + exponent) is reported", () => {
    const r = runChecker("n = 1.5_5e1_0\n");
    expect(r.bare_literals).toBe(1);
  });

  test("1.5e10 is reported as the full e-form, not split at the dot", () => {
    const r = runChecker("p = 1.5e10\n");
    expect(r.bare_literals).toBe(1);
    expect(r.hits[0].text).toContain("1.5e10");
  });
});

describe("checkDoesNotDefaultToFloat — nested parens", () => {
  test("float(int(x)) is captured as a single cast (one level of nesting)", () => {
    const r = runChecker("q = float(int(x))\n");
    expect(r.float_casts).toBe(1);
    expect(r.bare_literals).toBe(0);
  });

  test("float(int(1.0)) reports cast once; inner literal blanked by cast", () => {
    const r = runChecker("r = float(int(1.0))\n");
    // The cast hit captures the full call; the inner 1.0 is blanked
    // out by the cast's region so the literal scan does not see it.
    expect(r.float_casts).toBe(1);
    expect(r.bare_literals).toBe(0);
  });
});

describe("checkDoesNotDefaultToFloat — multiline casts", () => {
  test('multiline float("inf") sentinel (Black-style) is exempt', () => {
    const r = runChecker('s = float(\n    "inf"\n)\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("multiline float(1.0) (Black-style) reports cast once", () => {
    const r = runChecker("t = float(\n    1.0,\n)\n");
    expect(r.float_casts).toBe(1);
    expect(r.bare_literals).toBe(0);
  });
});

describe("checkDoesNotDefaultToFloat — trailing-comma sentinel (Black)", () => {
  test('single-line float("inf",) is exempt', () => {
    const r = runChecker('u = float("inf",)\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test('multiline float(\\n  "inf",\\n) is exempt', () => {
    const r = runChecker('v = float(\n    "inf",\n)\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test('float("nan",) is exempt', () => {
    const r = runChecker('w = float("nan",)\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });
});

describe("checkDoesNotDefaultToFloat — format-spec exemption", () => {
  test("f-string format spec {x:.2f} does not flag .2 as a bare float", () => {
    // `.2f` after `:` is a precision specifier, not code. The `:`
    // lookbehind blocks the bare-literal regex.
    const r = runChecker('aa = f"value is {x:.2f}"\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("f-string width.precision spec {x:10.5f} does not flag 10.5", () => {
    const r = runChecker('ab = f"{x:10.5f}"\n');
    expect(r).toEqual({ bare_literals: 0, float_casts: 0, hits: [] });
  });

  test("regular `.format()` spec is also exempt", () => {
    const r = runChecker('ac = "{x:.2f}".format(x=v)\n');
    expect(r.bare_literals).toBe(0);
  });
});

describe("checkDoesNotDefaultToFloat — f-string limitations (documented)", () => {
  // F-string expression regions are masked uniformly with their text
  // portions, so bare floats inside `f'{1.0}'` are CURRENTLY false
  // negatives. This is a documented heuristic limitation; the test
  // locks in the current behaviour so a future change is intentional.
  // Full f-string awareness lands in a follow-up PR.
  test("bare float inside f-string expression is a (documented) false negative", () => {
    const r = runChecker('ad = f"{1.0}"\n');
    expect(r.bare_literals).toBe(0); // current heuristic limitation
  });

  test("text-only f-string content does not produce false positives", () => {
    // The mask correctly suppresses bare-float matches inside the
    // text portion of an f-string.
    const r = runChecker('ae = f"value is 1.0 by default"\n');
    expect(r.bare_literals).toBe(0);
  });
});
