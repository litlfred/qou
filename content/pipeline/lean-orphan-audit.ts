#!/usr/bin/env bun
/**
 * lean-orphan-audit — find `.lean` modules under the QOU library tree that
 * nothing imports, i.e. that sit outside `QOU.lean`'s umbrella.
 *
 * > ## ⚠ CORRECTION 2026-08-15 (bean `qou-kljb`) — READ BEFORE QUOTING A NUMBER
 * >
 * > **This tool no longer measures build coverage.** The lakefile now sets
 * >
 * >     globs = ["QOU", "QOU.+"]     # bean qou-rc7b
 * >
 * > and `QOU.+` is `Glob.andSubmodules`, so the library target covers **every**
 * > module under `lean/QOU/` whether or not `QOU.lean` imports it. Verified by
 * > direct experiment (throwaway package, v4.24.0, `globs` set): `lake build`
 * > reports `✔ Built Lib.Orphan` for a module nothing imports, and emits its
 * > olean.
 * >
 * > What this tool still measures — and it is worth measuring — is
 * > **umbrella-import hygiene**: a module outside the import closure is
 * > invisible to anything that walks imports (blueprint, doc-gen, dependency
 * > analysis, `lean-direct-cone` cones rooted at `QOU`). It is NOT invisible to
 * > the compiler.
 * >
 * > The history below is preserved because it explains why the tool was
 * > written; it describes the lakefile as it stood BEFORE `globs` landed.
 *
 * ## Why this existed (bean `qou-orph`, historical)
 *
 * `content/quantum-observable-universe/lean/lakefile.toml` then declared
 *
 *     defaultTargets = ["QOU"]
 *     [[lean_lib]]
 *     name = "QOU"
 *     srcDir = "."
 *
 * with `globs` unset. Lake's default is `Glob.one` of `roots`, and `roots`
 * defaults to the library name — so the glob was the **single module** `QOU`,
 * and `lake build` compiled exactly `QOU.lean` plus its transitive `import`
 * closure. `srcDir = "."` sets where Lake *looks*, not what it *builds*.
 *
 * The consequence, AT THAT TIME: **a file nothing imports is not in the
 * library.** It was never compiled, by `lake build` or by CI, and could be
 * broken for months in silence. Measured 2026-08-07: 761 of 1598 modules — 47.6%.
 *
 * A sample of 153 was compiled 2026-08-08 and 94.8% were green, so this is not
 * mainly a story about broken code. It is a story about **unchecked** code: the
 * eight failures were all stale references (renamed Mathlib lemmas, deleted QOU
 * declarations), i.e. exactly what a gate catches the day it happens.
 *
 * ## An orphan is not only unverified — it ships no `.olean`
 *
 * Raised by the sibling lane on PR #4762, which hit this from the other end:
 * importing the orphan `QOU.Mass.QHookDimensionBalanced` from a content-block
 * `.lean` failed with
 *
 *     error: object file '.../QOU/Mass/QHookDimensionBalanced.olean' of module
 *            QOU.Mass.QHookDimensionBalanced does not exist
 *
 * **Verified here, and the scope is narrower than "a latent build failure for
 * every future consumer" — worth stating precisely, because the two paths
 * differ:**
 *
 *   - `lake build QOU.Mass.QHookDimensionBalanced` **succeeds** (883 jobs).
 *     Lake resolves imports transitively and builds the orphan on demand, so
 *     orphan status costs a `lake` consumer inside the package nothing but time.
 *   - The `.olean` is nonetheless **absent** from the build tree, because
 *     nothing in the default target ever produced it. So every `lean`-DIRECT
 *     consumer breaks — which is precisely the content-block sibling path
 *     (`scripts/lean-verify-siblings.sh`), the one that cannot use lake.
 *
 * So: an orphan is a latent build failure for `lean`-direct and olean-cache
 * consumers, not for `lake` within the package. Still a real cost — the sibling
 * path is exactly where it bites — but claiming it breaks *every* consumer
 * would be this lane's signature error: a claim adjacent to the one measured.
 *
 * Independent corroboration of scale, by a different method (#4762): 1630
 * `.lean` sources under `QOU/` against 942 oleans on `lake-cache/qou-v4-24-0`,
 * a ~213-file gap after allowing for post-cache additions. A lower bound from a
 * stale cache; the import-reachability count below is the fuller number.
 * Different denominators, same conclusion.
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
        `lean-orphan-audit: ${offenders.length} changed module(s) are UNREFERENCED —\n` +
          `nothing imports them, so they are outside \`QOU.lean\`'s umbrella and\n` +
          `invisible to import-closure tooling (blueprint, doc-gen, dependency walks).\n` +
          `They ARE still compiled: the lakefile sets globs = ["QOU", "QOU.+"], so\n` +
          `the library target covers the whole tree (bean qou-rc7b / qou-kljb).\n`,
      );
      for (const o of offenders) console.error(`  ${o}`);
      console.error(
        `\nFix: add an \`import\` line for each to ${root}/QOU.lean (keeping it\n` +
          `alphabetical within its section), then compile it to confirm it is green\n` +
          `before pushing — \`scripts/lean-direct-cone.sh <module>\` (NOT \`lake build\`,\n` +
          `which re-resolves deps and evicts a restored lake-cache). See bean qou-kljb.`,
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
      `unreferenced by \`QOU.lean\`'s import closure.\n` +
      `  NOTE: this is umbrella-import hygiene, NOT build coverage. Since the\n` +
      `  lakefile set globs = ["QOU", "QOU.+"] these modules ARE compiled by\n` +
      `  \`lake build\` (verified by experiment — bean qou-kljb 2026-08-15).`,
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
