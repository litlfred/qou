/**
 * Guard for `paper-commentary-audit.ts`. Positives are the verbatim passages
 * found in chapters 1-2 on 2026-10-11; negatives are the forms the audit must
 * leave alone (a Lean declaration named in a link, mathematics, the one brief
 * status remark an open conjecture is allowed).
 */
import { describe, expect, it } from "bun:test";
import { scanCommentary } from "./paper-commentary-audit";

const crit = (src: string, ctx = {}) =>
  scanCommentary(src, ctx).filter((h) => !h.advisory).map((h) => h.criterion);

describe("positives (found in chapters 1-2)", () => {
  it("formalisation bookkeeping", () => {
    expect(crit("(`QOU.X.assoc_pentagon`, sorry-free).")).toContain("commentary-formal-status");
    expect(crit("The implication above is established in narrative here and is not formalised.")).toContain("commentary-formal-status");
    expect(crit("pending shuffle-Hopf infrastructure absent from Mathlib")).toContain("commentary-formal-status");
  });
  it("corpus history", () => {
    expect(crit("This axiom is what earlier drafts asserted, less directly.")).toContain("commentary-corpus-history");
    expect(crit("an earlier formulation derived \"which subgroup\"")).toContain("commentary-corpus-history");
    expect(crit("Earlier statements of this definition wrote $\\epsilon$ as …")).toContain("commentary-corpus-history");
  });
  it("repository furniture", () => {
    expect(crit("Both rows are proved in\n`lean/QOU/BraidsAndKnots/Foo.lean`")).toContain("commentary-repo-ref");
    expect(crit("tracked in bean `qou-ab12`")).toContain("commentary-repo-ref");
    expect(crit("see docs/audits/2026-01-01-x.md")).toContain("commentary-repo-ref");
  });
  it("provenance and agent speech", () => {
    expect(crit("measured on 2026-08-30 at 70 dps")).toContain("commentary-provenance");
    expect(crit("an agent found that this session")).toContain("commentary-agent");
  });
});

describe("negatives", () => {
  it("a linked Lean declaration name is not a repo ref", () => {
    expect(crit("[`QOU.X.thm`](../lean/QOU/X/Thm.lean) proves the biconditional.")).toEqual([]);
  });
  it("mathematics in math mode and fences is ignored", () => {
    expect(crit("$\\text{sorry-free}$\n```tex\nearlier version\n```")).toEqual([]);
  });
  it("plain mathematics", () => {
    expect(crit("The pair $(\\mathrm{ev}, \\mathrm{coev})$ exhibits $A$ as its own dual.")).toEqual([]);
  });
});

describe("open-conjecture brief-status exception", () => {
  const brief = "The analytic relation at $q \\neq 1$ remains open.";
  it("passes silently in a conjecture block", () => {
    expect(scanCommentary(brief, { kind: "conjecture" })).toEqual([]);
  });
  it("is advisory, not failing, outside a conjecture", () => {
    const hits = scanCommentary(brief, { kind: "remark" });
    expect(hits.length).toBe(1);
    expect(hits[0]!.advisory).toBe(true);
  });
  it("fails when the status remark is not brief", () => {
    const long = Array(4).fill("This step remains open.").join(" ");
    expect(crit(long, { kind: "conjecture" })).toContain("commentary-open-status");
  });
});
