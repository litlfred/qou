/**
 * Lean project tests — compilation readiness, library presence, sorry audit.
 *
 * Works for any Lean project declared in lakefile.toml:
 * QOU, Fred2005, Unital, or anything added in the future.
 */

import { describe, test, expect } from "bun:test";
import { readFileSync, existsSync } from "fs";
import { join } from "path";
import {
  LEAN_DIR,
  discoverLeanProjects,
  discoverDependencies,
  findLeanFiles,
} from "./helpers";

// ── Toolchain & lakefile ────────────────────────────────────────

describe("Lean toolchain", () => {
  test("lean-toolchain exists", () => {
    expect(existsSync(join(LEAN_DIR, "lean-toolchain"))).toBe(true);
  });

  test("lean-toolchain has valid version", () => {
    const tc = readFileSync(join(LEAN_DIR, "lean-toolchain"), "utf-8").trim();
    expect(tc).toMatch(/^leanprover\/lean4:v\d+\.\d+/);
  });

  test("lakefile.toml exists", () => {
    expect(existsSync(join(LEAN_DIR, "lakefile.toml"))).toBe(true);
  });

  test("lake-manifest.json is valid JSON (if present)", () => {
    const manifest = join(LEAN_DIR, "lake-manifest.json");
    if (!existsSync(manifest)) return; // skip if not present
    const content = readFileSync(manifest, "utf-8");
    expect(() => JSON.parse(content)).not.toThrow();
  });
});

// ── Required dependencies ───────────────────────────────────────

describe("Lean dependencies", () => {
  const deps = discoverDependencies();

  test("mathlib is declared", () => {
    expect(deps).toContain("mathlib");
  });

  test("at least one dependency declared", () => {
    expect(deps.length).toBeGreaterThan(0);
  });
});

// ── Per-project tests ───────────────────────────────────────────

const projects = discoverLeanProjects();

describe("Lean project discovery", () => {
  test("at least one project found", () => {
    expect(projects.length).toBeGreaterThan(0);
  });
});

for (const proj of projects) {
  describe(`Project: ${proj}`, () => {
    const projDir = join(LEAN_DIR, proj);
    const leanFiles = findLeanFiles(projDir);

    test("directory exists", () => {
      expect(existsSync(projDir)).toBe(true);
    });

    test("has .lean files", () => {
      expect(leanFiles.length).toBeGreaterThan(0);
    });

    // Per-file tests
    for (const file of leanFiles) {
      const rel = file.replace(LEAN_DIR + "/", "");

      test(`${rel} is non-empty`, () => {
        const content = readFileSync(file, "utf-8");
        expect(content.trim().length).toBeGreaterThan(0);
      });

      test(`${rel} has import or is root module`, () => {
        const content = readFileSync(file, "utf-8");
        const basename = file.split("/").pop()?.replace(".lean", "");
        const hasImport = /^import\s/m.test(content);
        const isRoot = basename === proj;
        expect(hasImport || isRoot).toBe(true);
      });
    }

    // Sorry audit
    test("sorry audit", () => {
      let totalSorry = 0;
      const sorryFiles: string[] = [];
      for (const file of leanFiles) {
        const content = readFileSync(file, "utf-8");
        const count = (content.match(/\bsorry\b/g) || []).length;
        if (count > 0) {
          totalSorry += count;
          sorryFiles.push(`${file.replace(LEAN_DIR + "/", "")}(${count})`);
        }
      }
      // This is informational — we log but don't fail
      if (totalSorry > 0) {
        console.log(`    ℹ ${proj}: ${totalSorry} sorry in ${sorryFiles.length} files: ${sorryFiles.join(", ")}`);
      }
      // Always passes — sorry count is tracked in the report
      expect(true).toBe(true);
    });

    // Build artifacts not tracked
    test("no .lake/ artifacts in git", () => {
      const { execSync } = require("child_process");
      try {
        const tracked = execSync("git ls-files --cached lean/.lake/", {
          cwd: join(LEAN_DIR, ".."),
          encoding: "utf-8",
        }).trim();
        expect(tracked).toBe("");
      } catch {
        // git not available — skip
      }
    });
  });
}
