#!/usr/bin/env bun
/**
 * Export CSL-JSON references to BibTeX.
 *
 * Reads the authoritative bibliography from `schema/references.ts`
 * and writes `references.bib` in the repo root for LaTeX consumption.
 *
 * Usage:
 *   bun run pipeline/export-bibtex.ts
 *   bun run pipeline/export-bibtex.ts --out /path/to/references.bib
 *
 * @module content/pipeline/export-bibtex
 */

import { writeFileSync } from "fs";
import { resolve, join } from "path";
import type { Data as CSLData, Person as CSLPerson } from "csl-json";
import { references } from "../schema/references";

const REPO_ROOT = resolve(import.meta.dir, "../..");
const args = process.argv.slice(2);
const outIdx = args.indexOf("--out");
const outPath = outIdx >= 0 ? resolve(args[outIdx + 1]) : join(REPO_ROOT, "references.bib");

// ── CSL type → BibTeX entry type mapping ────────────────────────

const TYPE_MAP: Record<string, string> = {
  "article-journal": "article",
  "article-magazine": "article",
  "article-newspaper": "article",
  "article": "article",
  "book": "book",
  "chapter": "incollection",
  "paper-conference": "inproceedings",
  "thesis": "phdthesis",
  "report": "techreport",
  "dataset": "misc",
  "webpage": "misc",
  "manuscript": "unpublished",
  "patent": "misc",
  "personal_communication": "misc",
};

// ── Formatting helpers ──────────────────────────────────────────

/** Convert Unicode to BibTeX-safe LaTeX. */
function texEscape(s: string): string {
  return s
    .replace(/&/g, "\\&")
    .replace(/%/g, "\\%")
    // Common accented characters → LaTeX
    .replace(/\u00e9/g, "{\\'{e}}")       // é
    .replace(/\u00c9/g, "{\\'{E}}")       // É
    .replace(/\u00e8/g, "{\\`{e}}")       // è
    .replace(/\u00ea/g, "{\\^{e}}")       // ê
    .replace(/\u00eb/g, '{\\"e}')         // ë
    .replace(/\u00e0/g, "{\\`{a}}")       // à
    .replace(/\u00e1/g, "{\\'{a}}")       // á
    .replace(/\u00e2/g, "{\\^{a}}")       // â
    .replace(/\u00e4/g, '{\\"a}')         // ä
    .replace(/\u00f6/g, '{\\"o}')         // ö
    .replace(/\u00fc/g, '{\\"u}')         // ü
    .replace(/\u00dc/g, '{\\"U}')         // Ü
    .replace(/\u00f4/g, "{\\^{o}}")       // ô
    .replace(/\u0142/g, "{\\l}")          // ł
    .replace(/\u012b/g, "{\\={\\i}}")     // ī
    .replace(/\u012d/g, "{\\u{\\i}}")     // ĭ  (breve i)
    .replace(/\u012f/g, "{\\k{i}}")       // į
    .replace(/\u0131/g, "{\\i}")          // ı  (dotless i)
    // Kreĭn-specific
    .replace(/\u012c/g, "{\\u{I}}")       // Ĭ
    .replace(/\u012a/g, "{\\={I}}")       // Ī
    .replace(/\u0306/g, "{\\u{}}")        // combining breve
    // German
    .replace(/\u00df/g, "{\\ss}")         // ß
    ;
}

/** Format a CSL person as BibTeX author string. */
function formatPerson(p: CSLPerson): string {
  if (p.literal) return texEscape(p.literal);
  const parts: string[] = [];
  if (p["non-dropping-particle"]) parts.push(texEscape(p["non-dropping-particle"]));
  if (p.family) parts.push(texEscape(p.family));
  const family = parts.join(" ");
  const given = p.given ? texEscape(p.given) : "";
  if (p.suffix) return `${family}, ${texEscape(p.suffix)}, ${given}`;
  return given ? `${family}, ${given}` : family;
}

/** Format a CSL date as BibTeX year string. */
function formatYear(entry: CSLData): string | undefined {
  const issued = entry.issued;
  if (!issued) return undefined;
  if ("date-parts" in issued && issued["date-parts"]?.[0]) {
    return String(issued["date-parts"][0][0]);
  }
  if ("raw" in issued && issued.raw) {
    const m = issued.raw.match(/\d{4}/);
    return m ? m[0] : issued.raw;
  }
  if ("literal" in issued && issued.literal) return issued.literal;
  return undefined;
}

/** Wrap title in double braces to preserve casing. */
function braceTitle(title: string): string {
  return `{${texEscape(title)}}`;
}

// ── Main export ─────────────────────────────────────────────────

function entryToBibtex(entry: CSLData): string {
  const bibType = TYPE_MAP[entry.type] || "misc";
  const fields: [string, string][] = [];

  // Author
  if (entry.author?.length) {
    fields.push(["author", entry.author.map(formatPerson).join(" and ")]);
  }

  // Editor
  if (entry.editor?.length) {
    fields.push(["editor", entry.editor.map(formatPerson).join(" and ")]);
  }

  // Title
  if (entry.title) {
    fields.push(["title", braceTitle(entry.title)]);
  }

  // Journal / booktitle / container
  if (entry["container-title"]) {
    const field = bibType === "incollection" || bibType === "inproceedings"
      ? "booktitle" : "journal";
    fields.push([field, texEscape(entry["container-title"])]);
  }

  // Year
  const year = formatYear(entry);
  if (year) fields.push(["year", year]);

  // Volume, number, pages
  if (entry.volume != null) fields.push(["volume", String(entry.volume)]);
  if (entry.issue != null) fields.push(["number", String(entry.issue)]);
  if (entry.page) fields.push(["pages", entry.page.replace(/-/g, "--")]);

  // Publisher
  if (entry.publisher) fields.push(["publisher", texEscape(entry.publisher)]);

  // Series / collection
  if (entry["collection-title"]) fields.push(["series", texEscape(entry["collection-title"])]);
  if (entry["collection-number"] != null) fields.push(["number", String(entry["collection-number"])]);

  // Edition
  if (entry.edition != null) {
    const ed = String(entry.edition);
    fields.push(["edition", ed.match(/^\d+$/) ? ordinal(Number(ed)) : ed]);
  }

  // Identifiers
  if (entry.DOI) fields.push(["doi", entry.DOI]);
  if (entry.URL) fields.push(["url", entry.URL]);
  if (entry.ISBN) fields.push(["isbn", entry.ISBN]);
  if (entry.ISSN) fields.push(["issn", entry.ISSN]);

  // Thesis-specific
  if (bibType === "phdthesis" && entry.publisher) {
    // publisher is school for theses
    const schoolIdx = fields.findIndex(([k]) => k === "publisher");
    if (schoolIdx >= 0) {
      fields[schoolIdx] = ["school", fields[schoolIdx][1]];
    }
  }

  // Genre (for theses)
  // (BibTeX phdthesis type implies this, skip unless mastersthesis)

  // Note
  if (entry.note) fields.push(["note", texEscape(entry.note)]);

  // Howpublished for misc
  if (bibType === "misc" && entry.publisher && !fields.some(([k]) => k === "publisher")) {
    fields.push(["howpublished", texEscape(entry.publisher)]);
  }

  // Format output
  const maxKeyLen = Math.max(...fields.map(([k]) => k.length));
  const body = fields
    .map(([k, v]) => `  ${k.padEnd(maxKeyLen)} = {${v}},`)
    .join("\n");

  return `@${bibType}{${entry.id},\n${body}\n}`;
}

function ordinal(n: number): string {
  const s = ["th", "st", "nd", "rd"];
  const v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

// ── Build full .bib file ────────────────────────────────────────

function buildBibtex(): string {
  const header = [
    "% Bibliography for Quantum Observable Universe",
    "% AUTO-GENERATED from content/schema/references.ts — do not edit manually.",
    "%",
    "% Key convention:  <firstauthorlastname><year>  (all lower-case)",
    "% Source of truth: content/schema/references.ts (CSL-JSON)",
    "% Generator:       content/pipeline/export-bibtex.ts",
    `% Generated:       ${new Date().toISOString()}`,
    "",
  ].join("\n");

  const entries = references.map(entryToBibtex).join("\n\n");
  return header + entries + "\n";
}

// ── CLI ─────────────────────────────────────────────────────────

const bibtex = buildBibtex();
writeFileSync(outPath, bibtex);
console.log(`Exported ${references.length} references → ${outPath}`);
console.log(`  (${(bibtex.length / 1024).toFixed(1)} KB)`);

export { buildBibtex, entryToBibtex };
