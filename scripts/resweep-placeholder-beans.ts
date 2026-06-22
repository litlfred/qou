#!/usr/bin/env bun
/**
 * resweep-placeholder-beans.ts — reconcile the auto-generated
 * "Resolve N placeholders/TODOs in <scope>" beans against the honest counter.
 *
 * The 2026-06-22 bean sweep produced ~40 beans whose counts came from a naive
 * marker grep (claimed total ~1038). This driver maps each bean's scope to a
 * filesystem path, runs `count-actionable-placeholders.ts`, and:
 *   - honest == 0  (status todo)      → completes the bean (false-positive-only)
 *   - honest  > 0                     → appends the corrected count to the body
 * Beans whose scope is a single file, a missing path, the lean-root overlap
 * (`qou/lean`, which double-counts every subdir bean), already completed, or
 * already re-swept are flagged and left untouched (idempotent).
 *
 *   bun scripts/resweep-placeholder-beans.ts            # dry-run (default)
 *   bun scripts/resweep-placeholder-beans.ts --apply    # write via `beans` CLI
 */
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { resolve, join } from "node:path";

const REPO = resolve(import.meta.dir, "..");
const BEANS = join(REPO, ".beans");
const COUNTER = join(REPO, "scripts/count-actionable-placeholders.ts");
const apply = process.argv.includes("--apply");
const today = new Date().toISOString().slice(0, 10);

function mapScope(scope: string): string | null {
  if (scope === "qou/lean") return null; // whole-tree overlap — skip
  if (scope.startsWith("qou/lean/"))
    return join(REPO, "content/quantum-observable-universe/lean/QOU", scope.slice("qou/lean/".length));
  if (scope.startsWith("qou/"))
    return join(REPO, "content/quantum-observable-universe", scope.slice("qou/".length));
  if (scope === "schema") return join(REPO, "content/schema");
  if (scope === "unital-groebner-bases") return join(REPO, "content/unital-groebner-bases");
  return join(REPO, scope);
}

function honestCount(path: string): number | null {
  const r = Bun.spawnSync(["bun", COUNTER, path]);
  const m = r.stdout.toString().match(/TOTAL:\s*(\d+)/);
  return m ? parseInt(m[1], 10) : null;
}

function beansUpdate(args: string[]): void {
  const home = process.env.HOME ?? "";
  const r = Bun.spawnSync(["beans", ...args], {
    env: { ...process.env, PATH: `${home}/.local/bin:${home}/go/bin:${process.env.PATH}` },
  });
  if (r.exitCode !== 0) console.error(`  ! beans ${args.slice(0, 3).join(" ")} → exit ${r.exitCode}`);
}

let toComplete = 0, toAnnotate = 0, skipped = 0;
for (const f of readdirSync(BEANS).sort()) {
  if (!/resolve-.*placeholderstodos.*\.md$/.test(f)) continue;
  const id = f.split("--")[0];
  const txt = readFileSync(join(BEANS, f), "utf-8");
  const title = (txt.match(/^title:\s*(.*)$/m) ?? [])[1] ?? "";
  const status = (txt.match(/^status:\s*(.*)$/m) ?? [])[1]?.trim() ?? "";
  const claimed = parseInt((title.match(/Resolve\s+(\d+)/) ?? [])[1] ?? "0", 10);
  const scope = (title.match(/ in (.+)$/) ?? [])[1]?.trim() ?? "";
  const path = mapScope(scope);

  if (status === "completed" || /resweep \d{4}-\d{2}-\d{2}:/.test(txt)) {
    console.log(`${id}  claimed=${claimed}  [skip: already done]  ${scope}`);
    skipped++; continue;
  }
  if (path === null) { console.log(`${id}  claimed=${claimed}  [skip: lean-root overlap]  ${scope}`); skipped++; continue; }
  if (!existsSync(path)) { console.log(`${id}  claimed=${claimed}  [skip: no path]  ${scope}`); skipped++; continue; }
  if (statSync(path).isFile()) { console.log(`${id}  claimed=${claimed}  [skip: single-file scope]  ${scope}`); skipped++; continue; }

  const honest = honestCount(path);
  if (honest === null) { console.log(`${id}  claimed=${claimed}  [skip: counter error]  ${scope}`); skipped++; continue; }

  if (honest === 0 && status !== "in-progress") {
    console.log(`${id}  claimed=${claimed}  honest=0  [COMPLETE]  ${scope}`);
    if (apply) {
      beansUpdate(["update", id, "--body-append",
        `resweep ${today}: honest counter = 0 actionable (claimed ${claimed}); markers are sweep false positives (cited §3b sorrys / comment-mentions / sidecars). Closed.`]);
      beansUpdate(["update", id, "--status", "completed"]);
    }
    toComplete++;
  } else {
    console.log(`${id}  claimed=${claimed}  honest=${honest}  [ANNOTATE${status === "in-progress" ? ", in-progress" : ""}]  ${scope}`);
    if (apply) beansUpdate(["update", id, "--body-append",
      `resweep ${today}: honest counter = ${honest} actionable (claimed ${claimed}) via scripts/count-actionable-placeholders.ts.`]);
    toAnnotate++;
  }
}
console.log(`\n${apply ? "APPLIED" : "DRY-RUN"}: ${toComplete} complete, ${toAnnotate} annotate, ${skipped} skip`);
