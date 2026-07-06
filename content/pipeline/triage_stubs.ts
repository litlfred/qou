import { readFileSync, writeFileSync, unlinkSync, existsSync, readdirSync, statSync } from "node:fs";
import { resolve, relative, join } from "node:path";

const REPO_ROOT = resolve(import.meta.dir, "../..");
const LEAN_DIR = resolve(REPO_ROOT, "content/quantum-observable-universe/lean/QOU");

function walkLean(dir: string, list: string[] = []): string[] {
  if (!existsSync(dir)) return list;
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      walkLean(full, list);
    } else if (entry.endsWith(".lean")) {
      list.push(full);
    }
  }
  return list;
}

function stripCommentLines(src: string): string[] {
  const lines = src.split("\n");
  const out: string[] = [];
  let depth = 0;
  let inString = false;
  for (const line of lines) {
    let res = "";
    let i = 0;
    while (i < line.length) {
      if (depth > 0) {
        if (line.startsWith("-/", i)) {
          depth--;
          res += "  ";
          i += 2;
        } else if (line.startsWith("/-", i)) {
          depth++;
          res += "  ";
          i += 2;
        } else {
          res += " ";
          i++;
        }
      } else if (inString) {
        if (line.startsWith('\\"', i) || line.startsWith("\\\\", i)) {
          res += line.slice(i, i + 2);
          i += 2;
        } else if (line[i] === '"') {
          inString = false;
          res += '"';
          i++;
        } else {
          res += line[i];
          i++;
        }
      } else if (line.startsWith("/-", i)) {
        depth++;
        res += "  ";
        i += 2;
      } else if (line.startsWith("--", i)) {
        res += " ".repeat(line.length - i);
        break;
      } else if (line[i] === '"') {
        inString = true;
        res += '"';
        i++;
      } else {
        res += line[i];
        i++;
      }
    }
    out.push(res);
  }
  return out;
}

interface Decl {
  kind: string;
  name: string;
  startLine: number;
  text: string;
  sig: string;
  body: string;
}

const DECL_START =
  /^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+|scoped\s+|partial\s+|unsafe\s+)*(theorem|lemma|proposition|corollary|example|def|abbrev|instance|axiom|structure|class)\s+([A-Za-z_][\w'.]*)/;

function splitDecls(origLines: string[], codeLines: string[]): Decl[] {
  const starts: { i: number; kind: string; name: string }[] = [];
  for (let i = 0; i < codeLines.length; i++) {
    const m = codeLines[i].match(DECL_START);
    if (m && /^\s{0,2}\S/.test(codeLines[i])) {
      starts.push({ i, kind: m[1], name: m[2] });
    }
  }
  const decls: Decl[] = [];
  for (let s = 0; s < starts.length; s++) {
    const { i, kind, name } = starts[s];
    const end = s + 1 < starts.length ? starts[s + 1].i : codeLines.length;
    const declLines = codeLines.slice(i, end);
    while (declLines.length > 1) {
      const last = declLines[declLines.length - 1];
      if (
        /^\s*$/.test(last) ||
        /^\s*(end|namespace|section|open|variable|universe|attribute|set_option)\b/.test(
          last,
        )
      )
        declLines.pop();
      else break;
    }
    const text = declLines.join("\n");
    const asgn = text.indexOf(":=");
    const sig = asgn >= 0 ? text.slice(0, asgn) : text;
    const body = asgn >= 0 ? text.slice(asgn + 2) : "";
    decls.push({
      kind,
      name,
      startLine: i + 1,
      text,
      sig,
      body,
    });
  }
  return decls;
}

function escapeRegExp(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function findColonEqualsIndex(text: string): number {
  let depth = 0;
  let inString = false;
  let i = 0;
  while (i < text.length) {
    if (depth > 0) {
      if (text.startsWith("-/", i)) {
        depth--;
        i += 2;
      } else if (text.startsWith("/-", i)) {
        depth++;
        i += 2;
      } else {
        i++;
      }
    } else if (inString) {
      if (text.startsWith('\\"', i) || text.startsWith("\\\\", i)) {
        i += 2;
      } else if (text[i] === '"') {
        inString = false;
        i++;
      } else {
        i++;
      }
    } else if (text.startsWith("/-", i)) {
      depth++;
      i += 2;
    } else if (text.startsWith("--", i)) {
      // Line comment: skip to next line
      const nl = text.indexOf("\n", i);
      if (nl < 0) break;
      i = nl + 1;
    } else if (text[i] === '"') {
      inString = true;
      i++;
    } else if (text.startsWith(":=", i)) {
      return i;
    } else {
      i++;
    }
  }
  return -1;
}

function runTriage() {
  console.log("Starting triage...");
  const auditPath = resolve(REPO_ROOT, "docs/audits/2026-06-17-lean-vacuity-axiom-audit.json");
  const auditData = JSON.parse(readFileSync(auditPath, "utf-8"));
  
  // Find all files flagged with proof-no-placeholder-stub in lean/QOU
  const flaggedFiles: string[] = [];
  for (const [file, hits] of Object.entries(auditData.flagged)) {
    if (file.startsWith("content/quantum-observable-universe/lean/QOU/") &&
        (hits as any[]).some(h => h.category === "proof-no-placeholder-stub")) {
      flaggedFiles.push(file);
    }
  }
  
  console.log(`Found ${flaggedFiles.length} flagged files in lean/QOU/`);
  
  // Walk all Lean files in the repo to pre-load and strip them for matching
  const allLeanFiles = walkLean(LEAN_DIR);
  console.log(`Loaded ${allLeanFiles.length} total Lean files in lean/QOU/`);
  
  const fileContents = new Map<string, { raw: string; stripped: string[] }>();
  for (const f of allLeanFiles) {
    const raw = readFileSync(f, "utf-8");
    const stripped = stripCommentLines(raw);
    fileContents.set(resolve(f), { raw, stripped });
  }
  
  const deletedShadows: string[] = [];
  const updatedPlaceholders: string[] = [];
  
  for (const relPath of flaggedFiles) {
    const absPath = resolve(REPO_ROOT, relPath);
    const fileData = fileContents.get(absPath);
    if (!fileData) {
      console.warn(`File data not found for ${relPath}`);
      continue;
    }
    
    const origLines = fileData.raw.split("\n");
    const decls = splitDecls(origLines, fileData.stripped);
    
    // Check if it's a shadow stub
    let isShadow = false;
    let shadowSourceFile = "";
    
    for (const decl of decls) {
      // Build declaration regex for other files
      const declRegex = new RegExp(
        "^\\s*(?:@\\[[^\\]]*\\]\\s*)?(?:private\\s+|protected\\s+|noncomputable\\s+|nonrec\\s+|scoped\\s+|partial\\s+|unsafe\\s+)*(theorem|lemma|proposition|corollary|example|def|abbrev|instance|axiom|structure|class)\\s+(?:[A-Za-z_][\\w'.]*\\.)?" + escapeRegExp(decl.name) + "\\b"
      );
      
      // Look for this declaration in other files
      for (const [otherPath, otherData] of fileContents.entries()) {
        if (otherPath === absPath) continue;
        
        const hasDecl = otherData.stripped.some(line => declRegex.test(line));
        if (hasDecl) {
          isShadow = true;
          shadowSourceFile = relative(REPO_ROOT, otherPath);
          break;
        }
      }
      if (isShadow) break;
    }
    
    if (isShadow) {
      console.log(`[SHADOW] ${relPath} is a shadow stub of ${shadowSourceFile}. Deleting.`);
      unlinkSync(absPath);
      deletedShadows.push(relPath);
    } else {
      console.log(`[PLACEHOLDER] ${relPath} is a genuine placeholder. Updating.`);
      
      // Update genuine placeholder
      // 1. Remove "— placeholder stub" comment from title
      let newRaw = fileData.raw;
      newRaw = newRaw.replace(/# (QOU\.[A-Za-z0-9_.]+) — placeholder stub/g, "# $1");
      
      // 2. Rewrite theorems/lemmas/propositions/corollaries to use sorry
      const newLines = newRaw.split("\n");
      const strippedLines = stripCommentLines(newRaw);
      const currentDecls = splitDecls(newLines, strippedLines);
      
      let offset = 0; // Keep track of line additions/deletions if any, though we rewrite in place
      for (const decl of currentDecls) {
        if (/^(theorem|lemma|proposition|corollary)\b/.test(decl.kind)) {
          // Get the exact lines of this declaration
          const declLineCount = decl.text.split("\n").length;
          const declOrigLines = newLines.slice(decl.startLine - 1, decl.startLine - 1 + declLineCount);
          const declText = declOrigLines.join("\n");
          
          const asgnIdx = findColonEqualsIndex(declText);
          if (asgnIdx >= 0) {
            const rewrittenDeclText = declText.slice(0, asgnIdx) + ":=\n  sorry";
            
            // Replace the declaration lines in newLines
            newLines.splice(decl.startLine - 1, declLineCount, rewrittenDeclText);
          }
        }
      }
      
      writeFileSync(absPath, newLines.join("\n"), "utf-8");
      updatedPlaceholders.push(relPath);
    }
  }
  
  console.log("\nTriage complete.");
  console.log(`Deleted ${deletedShadows.length} shadow stubs.`);
  console.log(`Updated ${updatedPlaceholders.length} genuine placeholders.`);
  
  // Write the results to a file for review
  const reportPath = resolve(REPO_ROOT, ".agents/worker_stub_audit/triage_report.json");
  writeFileSync(reportPath, JSON.stringify({ deletedShadows, updatedPlaceholders }, null, 2), "utf-8");
  console.log(`Wrote report to ${reportPath}`);
}

runTriage();
