#!/usr/bin/env bun
/**
 * Lean hash witness utility.
 *
 * Computes SHA-256 hashes of .lean files and manages witness files
 * for build-cache invalidation. A witness file at
 *   `<block>.lean.<hash>.witness`
 * records that the .lean file with that exact content hash was
 * successfully built by Lean. On subsequent builds, if the hash
 * matches, Lean validation can be skipped.
 *
 * Usage:
 *   bun run scripts/lean-witness.ts check <lean-file>   # check if witnessed
 *   bun run scripts/lean-witness.ts stamp <lean-file>    # create witness after build
 *   bun run scripts/lean-witness.ts dump                 # delete all witness files
 *   bun run scripts/lean-witness.ts status               # show witness status for all .lean files
 *   bun run scripts/lean-witness.ts hash <lean-file>     # print hash of .lean file
 *
 * @module scripts/lean-witness
 */

import { createHash } from "crypto";
import { readFileSync, writeFileSync, unlinkSync, existsSync } from "fs";
import { resolve, join, basename, dirname } from "path";
import { globSync } from "glob";

const REPO_ROOT = resolve(import.meta.dir, "..");
const HASH_LENGTH = 12;

// ── Core functions (exported for use by other scripts) ───────────

/** Compute 12-char SHA-256 hex prefix of a file's content. */
export function leanFileHash(filePath: string): string {
  const content = readFileSync(filePath, "utf-8");
  return createHash("sha256").update(content).digest("hex").slice(0, HASH_LENGTH);
}

/** Build the witness file path for a given .lean file and hash. */
export function witnessPath(leanFile: string, hash: string): string {
  return `${leanFile}.${hash}.witness`;
}

/** Check if a valid witness exists for the current content of a .lean file. */
export function isWitnessed(leanFile: string): { witnessed: boolean; hash: string } {
  if (!existsSync(leanFile)) return { witnessed: false, hash: "" };
  const hash = leanFileHash(leanFile);
  const wp = witnessPath(leanFile, hash);
  return { witnessed: existsSync(wp), hash };
}

/** Create a witness file for the current content of a .lean file. */
export function stampWitness(leanFile: string): { hash: string; witnessFile: string } {
  const hash = leanFileHash(leanFile);
  const wp = witnessPath(leanFile, hash);
  const meta = JSON.stringify({
    leanFile: basename(leanFile),
    hash,
    stampedAt: new Date().toISOString(),
  });
  writeFileSync(wp, meta + "\n");
  return { hash, witnessFile: wp };
}

/** Remove all witness files for a given .lean file (any hash). */
export function clearWitnesses(leanFile: string): number {
  const witnessFiles = globSync(`${leanFile}.*.witness`);
  for (const f of witnessFiles) {
    unlinkSync(f);
  }
  return witnessFiles.length;
}

/** Find all .lean files in content directories. */
export function findContentLeanFiles(): string[] {
  return globSync("content/**/*.lean", { cwd: REPO_ROOT, absolute: true });
}

/** Find all witness files in the repo. */
export function findAllWitnesses(): string[] {
  return globSync("content/**/*.witness", { cwd: REPO_ROOT, absolute: true });
}

// ── CLI ──────────────────────────────────────────────────────────

if (import.meta.main) {
  const [cmd, ...rest] = process.argv.slice(2);

  switch (cmd) {
    case "hash": {
      const file = resolve(rest[0]);
      console.log(leanFileHash(file));
      break;
    }
    case "check": {
      const file = resolve(rest[0]);
      const { witnessed, hash } = isWitnessed(file);
      console.log(JSON.stringify({ file: basename(file), hash, witnessed }));
      process.exit(witnessed ? 0 : 1);
    }
    case "stamp": {
      const file = resolve(rest[0]);
      // Clear stale witnesses first
      clearWitnesses(file);
      const { hash, witnessFile } = stampWitness(file);
      console.log(`✓ Stamped ${basename(file)} → ${basename(witnessFile)}`);
      break;
    }
    case "dump": {
      const witnesses = findAllWitnesses();
      for (const w of witnesses) {
        unlinkSync(w);
      }
      console.log(`🗑 Removed ${witnesses.length} witness file(s)`);
      break;
    }
    case "status": {
      const leanFiles = findContentLeanFiles();
      let witnessed = 0;
      let stale = 0;
      for (const f of leanFiles) {
        const result = isWitnessed(f);
        const rel = f.replace(REPO_ROOT + "/", "");
        const tag = result.witnessed ? "✓ witnessed" : "· not witnessed";
        if (result.witnessed) witnessed++;
        else stale++;
        console.log(`  ${tag}  ${rel}  (${result.hash})`);
      }
      console.log(`\n${witnessed} witnessed, ${stale} pending — ${leanFiles.length} total`);
      break;
    }
    default:
      console.error("Usage: lean-witness.ts <check|stamp|dump|status|hash> [file]");
      process.exit(1);
  }
}
