/**
 * Discovery for script-QA targets.
 *
 * Walks the script roots declared in `SCRIPT_ROOTS` and yields one
 * descriptor per audited script. Currently covers Python compute
 * scripts under `folio-assistant/computations/`; extending to
 * TypeScript or Rust just adds another entry to `SCRIPT_ROOTS`.
 *
 * @module content/pipeline/script-walker
 */

import {
  existsSync,
  readdirSync,
  statSync,
  readFileSync,
} from "fs";
import { createHash } from "crypto";
import { join, relative, basename, extname, dirname } from "path";
import type { ScriptLanguage } from "../../folio-assistant/schemas/script-qa";

export interface ScriptTarget {
  /** Absolute path on disk. */
  abs: string;
  /** Repo-relative path (for sidecar `script_path`). */
  rel: string;
  /** Inferred source language. */
  language: ScriptLanguage;
  /** 12-char SHA-256 prefix of the script content. */
  source_hash: string;
  /** Path the QA sidecar should be written to (absolute). */
  sidecar_abs: string;
  /** Repo-relative path of the QA sidecar. */
  sidecar_rel: string;
}

/**
 * Roots to walk + which language tag to assign to matching files.
 * Order is preserved in the walk; subdirectory `script-qa/` is
 * always excluded to keep the walker from auditing its own output.
 */
export interface ScriptRoot {
  /** Repo-relative directory to walk. */
  dir: string;
  /** Extensions (with leading dot) that mark an audited file. */
  exts: string[];
  /** Language tag to assign. */
  language: ScriptLanguage;
}

export const SCRIPT_ROOTS: ScriptRoot[] = [
  {
    dir: "folio-assistant/computations",
    exts: [".py"],
    language: "python",
  },
];

const SIDECAR_DIR_NAME = "script-qa";
const SIDECAR_EXT = ".script-qa.json";

function hashFile(abs: string): string {
  const buf = readFileSync(abs);
  return createHash("sha256").update(buf).digest("hex").slice(0, 12);
}

/** Sidecar path next to a script: `<parent>/script-qa/<base>.script-qa.json`. */
export function sidecarPathFor(scriptAbs: string): string {
  const parent = dirname(scriptAbs);
  const stem = basename(scriptAbs, extname(scriptAbs));
  return join(parent, SIDECAR_DIR_NAME, stem + SIDECAR_EXT);
}

/**
 * Walk a single root and yield `ScriptTarget`s. Skips hidden
 * directories, `node_modules`, and the sidecar subdir itself.
 */
function* walkRoot(
  rootAbs: string,
  rootRel: string,
  root: ScriptRoot,
  repoRoot: string,
): Generator<ScriptTarget> {
  if (!existsSync(rootAbs)) return;
  function* recurse(d: string): Generator<ScriptTarget> {
    for (const entry of readdirSync(d)) {
      if (
        entry.startsWith(".") ||
        entry === "node_modules" ||
        entry === SIDECAR_DIR_NAME
      ) {
        continue;
      }
      const full = join(d, entry);
      const st = statSync(full);
      if (st.isDirectory()) {
        yield* recurse(full);
      } else if (root.exts.includes(extname(entry))) {
        const sidecarAbs = sidecarPathFor(full);
        yield {
          abs: full,
          rel: relative(repoRoot, full),
          language: root.language,
          source_hash: hashFile(full),
          sidecar_abs: sidecarAbs,
          sidecar_rel: relative(repoRoot, sidecarAbs),
        };
      }
    }
  }
  yield* recurse(rootAbs);
}

/** Walk all configured script roots. */
export function* walkScripts(
  repoRoot: string,
  roots: ScriptRoot[] = SCRIPT_ROOTS,
): Generator<ScriptTarget> {
  for (const r of roots) {
    yield* walkRoot(join(repoRoot, r.dir), r.dir, r, repoRoot);
  }
}
