/**
 * Citation extraction utility.
 *
 * Parses \cite{key1, key2} patterns from markdown content
 * and returns deduplicated, sorted citation keys.
 *
 * Used by:
 * - export-json.ts to auto-populate block-level cites[]
 * - build.ts to aggregate chapter-level bibliographies
 * - validate-references.ts for cross-checking
 *
 * @module content/pipeline/citations
 */

/**
 * Extract all citation keys from markdown content.
 *
 * Handles:
 * - \cite{key}
 * - \cite{key1, key2, key3}
 * - \cite[Thm.~1.7]{key}
 * - \cite[\S3]{key}
 *
 * Returns deduplicated, sorted array of citation keys.
 */
export function extractCitations(md: string): string[] {
  const keys = new Set<string>();
  // Match \cite with optional [...] argument, then {keys}
  const pattern = /\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g;
  let match;
  while ((match = pattern.exec(md)) !== null) {
    for (const key of match[1].split(",")) {
      const trimmed = key.trim();
      if (trimmed) keys.add(trimmed);
    }
  }
  return [...keys].sort();
}

/**
 * Merge explicit cites[] from manifest with auto-extracted ones from .md.
 *
 * Explicit cites take precedence (they may include keys not in the .md,
 * e.g. for citations in Lean companion files).
 */
export function mergeCitations(
  explicit: string[] | undefined,
  mdContent: string,
): string[] {
  const fromMd = extractCitations(mdContent);
  if (!explicit?.length) return fromMd;
  const merged = new Set([...explicit, ...fromMd]);
  return [...merged].sort();
}
