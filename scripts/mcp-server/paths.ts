/**
 * Shared path constants for the MCP server.
 *
 * @module scripts/mcp-server/paths
 */

import { resolve } from "path";

/** Repository root directory. */
export const REPO_ROOT = resolve(import.meta.dir, "../..");

/** Content objects directory. */
export const CONTENT_DIR = resolve(REPO_ROOT, "content");

/** LaTeX chapters output directory. */
export const CHAPTERS_DIR = resolve(REPO_ROOT, "chapters");

/** Main LaTeX file. */
export const MAIN_TEX = resolve(REPO_ROOT, "main.tex");

/** Lean project directory. */
export const LEAN_DIR = resolve(REPO_ROOT, "lean");

/** Build output directory. */
export const BUILD_DIR = resolve(REPO_ROOT, "build");

/** Preference storage file. */
export const PREFS_FILE = resolve(REPO_ROOT, ".qou-prefs.json");
