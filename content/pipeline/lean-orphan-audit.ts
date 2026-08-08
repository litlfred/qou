#!/usr/bin/env bun
/**
 * lean-orphan-audit — find `.lean` modules under the QOU library tree that
 * `lake build` never compiles.
 *
 * ## Why this exists (bean `qou-orph`)
 *
 * `content/quantum-observable-universe/lean/lakefile.toml` declares
 *
 *     defaultTargets = ["QOU"]
 *     [[lean_lib]]
 *     name = "QOU"
 *     srcDir = "."
 *
 * with `globs` unset. Lake's default is `Glob.one` of `roots`, and `roots`
 * defaults to the library name — so the glob is the **single module** `QOU`,
 * and `lake build` compiles exactly `QOU.lean` plus its transitive `import`
 * closure. `srcDir = "."` sets where Lake *looks*, not what it *builds*.
 *
 * The consequence: **a file nothing imports is not in the library.** It is
 * never compiled, by `lake build` or by CI, and can be broken for months in
 * silence. Measured 2026-08-07: 761 of 1598 modules — 47.6%.
 *
 * A sample of 153 was compiled 2026-08-08 and 94.8% were green, so this is not
 * mainly a story about broken code. It is a story about **unchecked** code: the
 * eight failures were all stale references (renamed Mathlib lemmas, deleted QOU
 * declarations), i.e. exactly what a gate catches the day it happens.
 *
 * ## Modes
 *
 *   bun run content/pipeline/lean-orphan-audit.ts
 *       Report the whole orphan set, counted by directory. Exit 0 always —
 *       this is a survey, not a gate.
 *
 *   bun run content/pipeline/lean-orphan-audit.ts --diff <files...>
 *       **Gate.** Given the `.lean` files a PR touches, fail if any of them
 *       lives under the library tree and is orphaned. Diff-scoped on purpose:
 *       a whole-tree gate would block every PR on a ~750-module backlog, the
 *       same reason `lean-content-siblings.yml` diff-scopes its own gates.
 *       Paths not under the library tree are ignored, so it is safe to pass a
 *       PR's entire `.lean` diff.
 *
 * Flags: `--quiet` (suppress the per-directory table), `--root <dir>`.
 */

import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, relative, resolve } from "node:path";

const DEFAULT_ROOT = "content/quantum-observable-universe/lean";

function walk(dir: string, out: string[] = []): string[] {
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (e.endsWith(".lean")) out.push(p);
  }
  return out;
}

/** `<root>/QOU/A/B.lean` → `QOU.A.B` */
function moduleOf(root: string, file: string): string | null {
  const rel = relative(resolve(root), resolve(file));
  if (rel.startsWith("..") || !rel.endsWith(".lean")) return null;
  if (rel !== "QOU.lean" && !rel.startsWith(`QOU/`)) return null;
  return rel.slice(0, -".lean".length).split("/").join(".");
}

function qouImports(text: string): string[] {
  return [...text.matchAll(/^import (QOU\.[\w.]+)/gm)].map((m) => m[1]);
}

function main(argv: string[]): number {
  const quiet = argv.includes("--quiet");
  const rootIdx = argv.indexOf("--root");
  const root = rootIdx >= 0 ? argv[rootIdx + 1] : DEFAULT_ROOT;
  const diffIdx = argv.indexOf("--diff");
  const diffFiles =
    diffIdx >= 0
      ? argv.slice(diffIdx + 1).filter((a) => !a.startsWith("--"))
      : null;

  const qouDir = join(root, "QOU");
  const files = walk(qouDir);
  const imports = new Map<string, string[]>();
  const all = new Set<string>();
  for (const f of files) {
    const m = moduleOf(root, f);
    if (!m) continue;
    all.add(m);
    imports.set(m, qouImports(readFileSync(f, "utf8")));
  }

  // transitive closure of the library root
  const seen = new Set<string>();
  const stack = qouImports(readFileSync(join(root, "QOU.lean"), "utf8"));
  while (stack.length) {
    const m = stack.pop()!;
    if (seen.has(m)) continue;
    seen.add(m);
    stack.push(...(imports.get(m) ?? []));
  }
  const orphans = [...all].filter((m) => !seen.has(m)).sort();

  // ---- gate mode -----------------------------------------------------------
  if (diffFiles) {
    const offenders: string[] = [];
    for (const f of diffFiles) {
      const m = moduleOf(root, f);
      if (m && m !== "QOU" && !seen.has(m)) offenders.push(`${m}  (${f})`);
    }
    if (offenders.length) {
      console.error(
        `lean-orphan-audit: ${offenders.length} changed module(s) are ORPHANED —\n` +
          `nothing imports them, so \`lake build\` never compiles them and no gate\n` +
          `will ever notice if they break.\n`,
      );
      for (const o of offenders) console.error(`  ${o}`);
      console.error(
        `\nFix: add an \`import\` line for each to ${root}/QOU.lean (keeping it\n` +
          `alphabetical within its section), then \`lake build <module>\` to confirm\n` +
          `it actually compiles before pushing. See bean qou-orph.`,
      );
      return 1;
    }
    if (!quiet) console.log("lean-orphan-audit: no new orphans in this diff.");
    return 0;
  }

  // ---- survey mode ---------------------------------------------------------
  const pct = ((100 * orphans.length) / all.size).toFixed(1);
  console.log(
    `lean-orphan-audit: ${orphans.length} of ${all.size} modules (${pct}%) are ` +
      `never built by \`lake build\`.`,
  );
  if (!quiet && orphans.length) {
    const byDir = new Map<string, number>();
    for (const o of orphans) {
      const d = o.split(".").slice(0, 2).join(".");
      byDir.set(d, (byDir.get(d) ?? 0) + 1);
    }
    console.log("\n  orphans by directory:");
    for (const [d, n] of [...byDir].sort((a, b) => b[1] - a[1]).slice(0, 20)) {
      console.log(`    ${String(n).padStart(4)}  ${d}`);
    }
    console.log(
      "\n  This is a survey, not a gate — exit 0 regardless. Use --diff <files>" +
        "\n  to fail on newly-added orphans.",
    );
  }
  return 0;
}

process.exit(main(process.argv.slice(2)));
