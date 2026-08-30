/**
 * Regression tests for the `proof-dependent-conjecture-not-conditional`
 * block-level check — `uses[]` reachability and multi-label banner scanning.
 *
 * WHY THESE EXIST. On 2026-08-30 the criterion reported 3 hits, of which 2
 * were false positives and the 1 true positive was under-reported by half
 * (bean `qou-s3zd`). Each behaviour pinned below is one of those failures, and
 * two of them are mistakes made while writing the fix rather than before it:
 *
 *   1. A block-level claim was checked against the Lean BINDER. An `.md`
 *      banner names an upstream result the block depends on EDITORIALLY while
 *      the Lean's conditionality sits on a proximate context class, so that
 *      check is a category error. It flagged `root-of-unity-truncation` and
 *      `phi-q-aj-machinery-identification`, both well-formed §3b-cond blocks.
 *   2. The scan matched `conj:` only, so a second missing dependency in the
 *      SAME banner was invisible: `magic-A-binding-formula.md` declares itself
 *      conditional on `conj:magic-numbers-bring` AND
 *      `prop:gravity-spectral-prefactor`, both unrecorded, one reported.
 *   3. The scan took one label per trigger phrase, so a label introduced by
 *      "and" was missed even after the kind was widened — which is the same
 *      defect as (2) surviving its own first fix.
 *   4. The `uses[]` array was matched non-greedily to the first `]`, so a `]`
 *      anywhere in a comment inside the array truncated the capture and the
 *      block read as having NO dependencies. Found because the comment written
 *      to document the fix in (2) contains the string `uses[]`, which zeroed
 *      that block's edges and made the dependency it was documenting look
 *      unrecorded.
 *
 * These are unit tests over the parsing and graph-walking behaviour, expressed
 * against fixtures on disk, so they do not depend on the corpus staying still.
 */
import { describe, expect, test } from "bun:test";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

/** The `uses[]` parser, mirrored from `usesGraph()` in the audit script. */
function parseUses(ts: string): string[] {
  const noComments = ts
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/(^|[^:])\/\/[^\n]*/g, "$1");
  const um = /uses:\s*\[([\s\S]*?)\]/.exec(noComments);
  return um ? [...um[1].matchAll(/"([^"]+)"/g)].map((m) => m[1].toLowerCase()) : [];
}

/** The banner scanner, mirrored from `scan` in `classifyConjectures`. */
function scanBanner(text: string): string[] {
  const out: string[] = [];
  const trigger =
    /(?:conditional on|assuming|given|depends on|modulo)\s+(?=[[`\s]*[a-z]+:[a-z0-9-]+)/gi;
  for (const t of text.matchAll(trigger)) {
    const from = (t.index ?? 0) + t[0].length;
    const rest = text.slice(from, from + 300);
    const end = rest.indexOf("**");
    const clause = end === -1 ? rest : rest.slice(0, end);
    for (const m of clause.matchAll(/([a-z]+):([a-z0-9-]+)/gi))
      out.push(`${m[1].toLowerCase()}:${m[2].toLowerCase()}`);
  }
  return [...new Set(out)];
}

function reachable(
  g: Map<string, string[]>,
  from: string,
  target: string,
  maxDepth = 5,
): boolean {
  if (!g.has(from)) return false;
  const seen = new Set([from]);
  let frontier = [from];
  for (let d = 0; d < maxDepth; d++) {
    const next: string[] = [];
    for (const n of frontier)
      for (const c of g.get(n) ?? []) {
        if (c === target) return true;
        if (!seen.has(c)) {
          seen.add(c);
          next.push(c);
        }
      }
    if (next.length === 0) return false;
    frontier = next;
  }
  return false;
}

describe("uses[] parsing", () => {
  test("a `]` inside a comment does not truncate the array", () => {
    const ts = `export const b = {
  label: "prop:x",
  uses: [
    // documented against the uses[] graph — this bracket pair is the hazard
    "conj:a",
    "prop:b",
  ],
};`;
    // Without comment-stripping this returns [] — the block reads as having
    // no dependencies at all, which is how the fix hid its own subject.
    expect(parseUses(ts)).toEqual(["conj:a", "prop:b"]);
  });

  test("a block with no uses[] parses as no edges, not as a crash", () => {
    expect(parseUses(`export const b = { label: "prop:x" };`)).toEqual([]);
  });

  test("block comments are stripped too", () => {
    const ts = `export const b = {
  uses: [
    /* an array [ with brackets ] in a block comment */
    "conj:a",
  ],
};`;
    expect(parseUses(ts)).toEqual(["conj:a"]);
  });
});

describe("banner scanning", () => {
  test("takes every label in the clause, not just the first", () => {
    const md =
      "**Theorem (conditional on [`conj:magic-numbers-bring`](../x/y.md)\n" +
      "and [`prop:gravity-spectral-prefactor`](z.md)).**\n";
    // Reporting only the first is defect (2)+(3): the second is introduced by
    // "and", so neither widening the kind nor the trigger alone finds it.
    expect(scanBanner(md)).toEqual([
      "conj:magic-numbers-bring",
      "prop:gravity-spectral-prefactor",
    ]);
  });

  test("takes non-conj kinds", () => {
    expect(scanBanner("**Prop (conditional on [`prop:foo-bar`](a.md)).**")).toEqual([
      "prop:foo-bar",
    ]);
  });

  test("stops at the end of the bold banner, not running into prose", () => {
    const md =
      "**Prop (conditional on [`conj:a`](a.md)).**\n\n" +
      "Ordinary prose mentioning def:not-a-dependency and prop:also-not.\n";
    expect(scanBanner(md)).toEqual(["conj:a"]);
  });

  test("markdown paths and URL schemes are not mistaken for labels", () => {
    const md =
      "**Prop (conditional on [`conj:a`](../obs/magic-numbers-bring.md), " +
      "see https://example.org/x).**";
    expect(scanBanner(md)).toEqual(["conj:a"]);
  });

  test("a plain prose mention with no trigger phrase is not a claim", () => {
    expect(scanBanner("This relates to conj:something in passing.")).toEqual([]);
  });
});

describe("uses[] reachability", () => {
  const g = new Map<string, string[]>([
    ["prop:root", ["prop:mid", "prop:other"]],
    ["prop:mid", ["conj:target"]],
    ["prop:other", []],
    ["conj:target", []],
    ["conj:orphan", []],
  ]);

  test("a direct edge is reachable", () => {
    expect(reachable(g, "prop:mid", "conj:target")).toBe(true);
  });

  test("a two-hop path is reachable — this is the acquittal that matters", () => {
    // `root-of-unity-truncation` reaches `conj:q-aubin-lions` this way and may
    // NOT list it directly: uses[] carries immediate neighbours only and
    // prune-transitive-deps.ts strips the redundant edge. Flagging it was a
    // false positive.
    expect(reachable(g, "prop:root", "conj:target")).toBe(true);
  });

  test("an unreachable label is reported — the true-positive case", () => {
    expect(reachable(g, "prop:root", "conj:orphan")).toBe(false);
  });

  test("an unknown start node is not reachable, and does not throw", () => {
    expect(reachable(g, "prop:absent", "conj:target")).toBe(false);
  });

  test("a cycle terminates", () => {
    const cyclic = new Map<string, string[]>([
      ["a", ["b"]],
      ["b", ["a"]],
    ]);
    expect(reachable(cyclic, "a", "zzz")).toBe(false);
  });

  test("depth is bounded", () => {
    const chain = new Map<string, string[]>();
    for (let i = 0; i < 12; i++) chain.set(`n${i}`, [`n${i + 1}`]);
    chain.set("n12", []);
    expect(reachable(chain, "n0", "n3", 5)).toBe(true);
    // Beyond the bound the answer is "not established", not "reachable".
    expect(reachable(chain, "n0", "n11", 5)).toBe(false);
  });
});

describe("end-to-end on fixtures", () => {
  test("a recorded dependency passes and an unrecorded one is caught", () => {
    const dir = mkdtempSync(join(tmpdir(), "usesreach-"));
    try {
      mkdirSync(join(dir, "c"), { recursive: true });
      writeFileSync(
        join(dir, "c", "good.ts"),
        `export const b = { label: "prop:good", uses: ["conj:dep"] };`,
      );
      writeFileSync(
        join(dir, "c", "bad.ts"),
        `export const b = { label: "prop:bad", uses: ["prop:unrelated"] };`,
      );
      const g = new Map<string, string[]>([
        ["prop:good", parseUses(`uses: ["conj:dep"]`)],
        ["prop:bad", parseUses(`uses: ["prop:unrelated"]`)],
        ["conj:dep", []],
        ["prop:unrelated", []],
      ]);
      const banner = "**Prop (conditional on [`conj:dep`](d.md)).**";
      const claimed = scanBanner(banner);
      expect(claimed).toEqual(["conj:dep"]);
      expect(claimed.filter((l) => !reachable(g, "prop:good", l))).toEqual([]);
      expect(claimed.filter((l) => !reachable(g, "prop:bad", l))).toEqual([
        "conj:dep",
      ]);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
});
