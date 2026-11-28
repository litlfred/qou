#!/usr/bin/env bun
/**
 * Generate QOU's Rust-crate Tool registrations in `tool-defs/`:
 *   1. `tool-defs/crates.json` — summary manifest of every crate under `crates/*`
 *   2. `tool-defs/<id>/<id>.json` — one `tool-definition/v1` folder per crate,
 *      loaded by `toolsFromFolders()` in `tool-defs/index.ts` (`crateTools()`).
 *
 * Owner decision A2 (2026-11-28, bean qou-crwk): top-level `Cargo.toml` +
 * `crates/*` manages all Rust crates, while QOU's `tools` Knowledge Graph
 * (`qou.json` `"id": "tools"`, path `"tool-defs/"`) registers every crate under
 * `crates/` as a validated `ToolDefinition` node (`bun run cat check:tools`).
 *
 * Parsed textually with zero external TOML dependencies so the generator runs
 * standalone in any checkout.
 *
 *   bun run scripts/gen-crate-tools.ts           # write crates.json + crate-<id>/crate-<id>.json
 *   bun run scripts/gen-crate-tools.ts --write   # write crates.json + crate-<id>/crate-<id>.json
 *   bun run scripts/gen-crate-tools.ts --check   # exit 1 when any file is stale
 */
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";

const ROOT = resolve(import.meta.dir, "..");
const TOOL_DEFS_DIR = join(ROOT, "tool-defs");
const OUT = join(TOOL_DEFS_DIR, "crates.json");

export interface CrateBin {
  name: string;
  path: string;
  requiredFeatures: string[];
}

export interface CrateEntry {
  /** Tool node id (`crate-<package-name>`). */
  id: string;
  /** Cargo `[package].name`. */
  name: string;
  /** Cargo `[package].version`. */
  version: string;
  /** Cargo `[package].edition`. */
  edition: string;
  /** Cargo `[package].license`. */
  license: string;
  /** Repo-relative crate directory (`crates/<dir>`). */
  path: string;
  /** Repo-relative manifest (`crates/<dir>/Cargo.toml`). */
  manifestPath: string;
  /** Cargo `[package].description`. */
  description: string;
  /** Whether listed in root `Cargo.toml` `[workspace].members` (false => `exclude`). */
  workspaceMember: boolean;
  /** `[lib]` crate types (`rlib`, `cdylib`, `staticlib`, …). */
  libCrateTypes: string[];
  /** Declared `[[bin]]` targets, sorted by binary name. */
  bins: CrateBin[];
  /** Default feature names from `[features].default`. */
  defaultFeatures: string[];
  /** Non-default feature names declared in `[features]`, sorted. */
  features: string[];
}

function stripComments(toml: string): string {
  return toml
    .split(/\r?\n/)
    .map((line) => {
      let inStr: string | null = null;
      for (let i = 0; i < line.length; i++) {
        const c = line[i]!;
        if (inStr) {
          if (c === "\\" && inStr === '"') i++;
          else if (c === inStr) inStr = null;
        } else if (c === '"' || c === "'") {
          inStr = c;
        } else if (c === "#") {
          return line.slice(0, i);
        }
      }
      return line;
    })
    .join("\n");
}

function stringList(raw: string | undefined): string[] {
  if (!raw) return [];
  return [...raw.matchAll(/"([^"]*)"|'([^']*)'/g)].map((m) => (m[1] ?? m[2])!);
}

function scalarString(section: string, key: string): string | undefined {
  const re = new RegExp(`^\\s*${key}\\s*=\\s*(?:"([^"]*)"|'([^']*)')`, "m");
  const m = re.exec(section);
  return m ? (m[1] ?? m[2]) : undefined;
}

function arrayField(section: string, key: string): string[] {
  const re = new RegExp(`^\\s*${key}\\s*=\\s*\\[([\\s\\S]*?)\\]`, "m");
  const m = re.exec(section);
  return stringList(m?.[1]);
}

interface ParsedSection {
  header: string;
  body: string;
}

function splitSections(cleanToml: string): ParsedSection[] {
  const lines = cleanToml.split("\n");
  const sections: ParsedSection[] = [];
  let current: ParsedSection = { header: "", body: "" };
  const bodyLines: string[] = [];
  const flush = () => {
    current.body = bodyLines.join("\n");
    sections.push(current);
    bodyLines.length = 0;
  };
  for (const line of lines) {
    const m = /^\s*(\[\[?[^\]]+\]?\])\s*$/.exec(line);
    if (m) {
      flush();
      current = { header: m[1]!.trim(), body: "" };
    } else {
      bodyLines.push(line);
    }
  }
  flush();
  return sections;
}

function workspaceMembers(root = ROOT): Set<string> {
  const wmPath = join(root, "Cargo.toml");
  if (!existsSync(wmPath)) return new Set();
  const clean = stripComments(readFileSync(wmPath, "utf8"));
  for (const s of splitSections(clean)) {
    if (s.header === "[workspace]") {
      return new Set(arrayField(s.body, "members"));
    }
  }
  return new Set();
}

export function parseCrateManifest(relDir: string, rawToml: string, members: Set<string>): CrateEntry {
  const clean = stripComments(rawToml);
  const sections = splitSections(clean);

  let name = relDir.replace(/^crates\//, "");
  let version = "0.1.0";
  let edition = "2021";
  let license = "MIT";
  let description = `Rust crate at ${relDir}`;
  let libCrateTypes: string[] = [];
  const bins: CrateBin[] = [];
  let defaultFeatures: string[] = [];
  const features: string[] = [];

  for (const s of sections) {
    if (s.header === "[package]") {
      name = scalarString(s.body, "name") ?? name;
      version = scalarString(s.body, "version") ?? version;
      edition = scalarString(s.body, "edition") ?? edition;
      license = scalarString(s.body, "license") ?? license;
      description = scalarString(s.body, "description") ?? description;
    } else if (s.header === "[lib]") {
      libCrateTypes = arrayField(s.body, "crate-type");
      if (libCrateTypes.length === 0) libCrateTypes = ["rlib"];
    } else if (s.header === "[[bin]]") {
      const binName = scalarString(s.body, "name");
      const binPath = scalarString(s.body, "path") ?? (binName ? `src/bin/${binName}.rs` : "src/main.rs");
      const req = arrayField(s.body, "required-features");
      if (binName) bins.push({ name: binName, path: binPath, requiredFeatures: req });
    } else if (s.header === "[features]") {
      for (const line of s.body.split("\n")) {
        const fm = /^\s*([A-Za-z0-9_-]+)\s*=\s*\[([^\]]*)\]/.exec(line);
        if (!fm) continue;
        const fKey = fm[1]!;
        if (fKey === "default") defaultFeatures = stringList(fm[2]);
        else features.push(fKey);
      }
    }
  }

  bins.sort((a, b) => a.name.localeCompare(b.name));
  features.sort((a, b) => a.localeCompare(b));

  const idSlug = name.replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase();
  return {
    id: `crate-${idSlug}`,
    name,
    version,
    edition,
    license,
    path: relDir,
    manifestPath: `${relDir}/Cargo.toml`,
    description,
    workspaceMember: members.has(relDir),
    libCrateTypes,
    bins,
    defaultFeatures,
    features,
  };
}

export function collectCrates(root = ROOT): CrateEntry[] {
  const dir = join(root, "crates");
  if (!existsSync(dir)) return [];
  const members = workspaceMembers(root);
  const out: CrateEntry[] = [];
  for (const entry of readdirSync(dir).sort()) {
    if (entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (!statSync(full).isDirectory()) continue;
    const tomlPath = join(full, "Cargo.toml");
    if (!existsSync(tomlPath)) continue;
    out.push(parseCrateManifest(`crates/${entry}`, readFileSync(tomlPath, "utf8"), members));
  }
  return out.sort((a, b) => a.path.localeCompare(b.path));
}

export function renderManifest(crates: CrateEntry[]): string {
  return `${JSON.stringify(
    {
      $comment:
        "GENERATED by scripts/gen-crate-tools.ts from crates/*/Cargo.toml and root Cargo.toml. Do not edit by hand; re-run `bun run scripts/gen-crate-tools.ts`.",
      crates,
    },
    null,
    2,
  )}\n`;
}

export function renderToolFolderJson(c: CrateEntry): string {
  const binSummary =
    c.bins.length > 0
      ? ` Binaries (${c.bins.length}): ${c.bins.map((b) => `\`${b.name}\``).join(", ")}.`
      : "";
  const featSummary =
    c.features.length > 0
      ? ` Optional features: ${c.features.map((f) => `\`${f}\``).join(", ")}.`
      : "";
  const wsStatus = c.workspaceMember
    ? "Workspace member in root `Cargo.toml`."
    : "Target-specific FFI crate listed in root `Cargo.toml` `[workspace].exclude`.";
  const invokeShell = c.workspaceMember
    ? `CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target CARGO_BUILD_JOBS=2 nice -n 15 cargo check -p ${c.name}`
    : `CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target CARGO_BUILD_JOBS=2 nice -n 15 cargo check --manifest-path ${c.manifestPath}`;

  const doc = {
    $schema: "tool-definition/v1",
    tool: {
      id: c.id,
      title: `Rust crate ${c.name} (${c.path})`,
      description:
        `${c.description} (${wsStatus} Version ${c.version}, edition ${c.edition}, license ${c.license}.` +
        `${binSummary}${featSummary} Generated from \`${c.manifestPath}\` by \`scripts/gen-crate-tools.ts\`.)`,
      install: { none: true },
      invoke: { shell: invokeShell },
      io: {
        inputs: [],
        outputs: [
          {
            name: c.name.replace(/[^A-Za-z0-9_]+/g, "_"),
            schema: { $type: "RepoPath" },
            description: `Rust crate \`${c.name}\` at \`${c.path}\` (\`${c.manifestPath}\`).`,
          },
        ],
      },
      satisfies: ["rust-crates-and-values", "compute-author"],
      subprocesses: ["rust-crates-and-values"],
      selection: {
        when: `Building, type-checking, or consuming \`${c.name}\` (\`${c.path}\`).`,
        limits: c.workspaceMember
          ? "Requires Rust/Cargo toolchain (and system GMP/MPFR when `mpfr` feature is active)."
          : "Target-specific FFI crate (`[workspace].exclude`); invoke with its target toolchain flags for release artefacts.",
        cost: "Incremental `cargo check` under shared `/tmp/qou-shared-cargo-target` (`CARGO_BUILD_JOBS=2`).",
      },
      requires: { runtime: ["cargo"], network: false },
    },
  };
  return `${JSON.stringify(doc, null, 2)}\n`;
}

function existingGeneratedCrateFolders(toolDefsDir = TOOL_DEFS_DIR): string[] {
  if (!existsSync(toolDefsDir)) return [];
  return readdirSync(toolDefsDir, { withFileTypes: true })
    .filter((e) => e.isDirectory() && e.name.startsWith("crate-") && e.name !== "crate-tools-sync-check")
    .map((e) => e.name)
    .sort();
}

if (import.meta.main) {
  const crates = collectCrates();
  const manifestText = renderManifest(crates);
  const expectedFolders = new Map<string, string>(crates.map((c) => [c.id, renderToolFolderJson(c)]));
  const existingFolders = existingGeneratedCrateFolders();

  if (process.argv.includes("--check")) {
    const stale: string[] = [];
    if (!existsSync(OUT) || readFileSync(OUT, "utf8") !== manifestText) {
      stale.push("tool-defs/crates.json");
    }
    for (const [id, content] of expectedFolders) {
      const p = join(TOOL_DEFS_DIR, id, `${id}.json`);
      if (!existsSync(p) || readFileSync(p, "utf8") !== content) {
        stale.push(`tool-defs/${id}/${id}.json`);
      }
    }
    for (const folder of existingFolders) {
      if (!expectedFolders.has(folder)) {
        stale.push(`tool-defs/${folder}/ (orphan crate folder)`);
      }
    }
    if (stale.length === 0) {
      console.log(`✓ tool-defs/crates.json and ${crates.length} crate Tool folder(s) are current`);
      process.exit(0);
    }
    console.error(`✗ stale crate Tool registration (${stale.length}):\n  ${stale.join("\n  ")}`);
    console.error("  Run: bun run scripts/gen-crate-tools.ts");
    process.exit(1);
  }

  writeFileSync(OUT, manifestText);
  for (const [id, content] of expectedFolders) {
    const dir = join(TOOL_DEFS_DIR, id);
    mkdirSync(dir, { recursive: true });
    writeFileSync(join(dir, `${id}.json`), content);
  }
  for (const folder of existingFolders) {
    if (!expectedFolders.has(folder)) {
      rmSync(join(TOOL_DEFS_DIR, folder), { recursive: true, force: true });
    }
  }
  console.log(`wrote tool-defs/crates.json + ${crates.length} tool-defs/crate-*/ folder(s)`);
}
