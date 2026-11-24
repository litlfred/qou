/**
 * Guard for `voice-leak-audit.ts`. Positives are verbatim passages from the
 * 2026-11-20 measurement samples; negatives are the false positives that
 * sample found (now exempt or advisory) and forms the audit must leave alone.
 */
import { describe, expect, it } from "bun:test";
import { classifyCode, scanText } from "./voice-leak-audit";

const failing = (src: string, opts = {}) =>
  scanText(src, opts).filter((h) => !h.advisory).map((h) => `${h.cls}:${h.sub}`);

describe("L1 lean-prose", () => {
  it("talk about the formalisation fails", () => {
    expect(failing("Two consequences are proved unconditionally in the Lean formalization.")).toContain("L1:lean-word");
    expect(failing("## Lean structure")).toContain("L1:lean-heading");
    expect(failing("The arithmetic of items 1--4 is machine-checked.")).toContain("L1:proof-assistant");
    expect(failing("absent from the Mathlib API")).toContain("L1:mathlib");
  });
  it("'formalises' in the mathematical sense is advisory only", () => {
    const h = scanText('This formalises "faster-than-viscous growth".');
    expect(h.map((x) => x.sub)).toEqual(["formalise"]);
    expect(h[0]!.advisory).toBe(true);
  });
  it("lowercase 'lean' and math are ignored", () => {
    expect(failing("a lean argument; $\\mathrm{Lean}$")).toEqual([]);
  });
});

describe("L2 lean-ident (backticked spans the platform strips)", () => {
  it("classifies the sample's forms", () => {
    expect(classifyCode("QOU.QBeta.lam_le_one_of_pow_bounded")).toBe("fqn");
    expect(classifyCode("SU2EmergenceRankForced.lean")).toBe("lean-file");
    expect(classifyCode("def:quantum-universe")).toBe("block-id");
    expect(classifyCode("dimQK0_eq_evDimQ_chernCharacter")).toBe("decl-name");
    expect(classifyCode("su2Character_one")).toBe("decl-name");
    expect(classifyCode("HochschildZero R A")).toBe("typeclass");
    expect(classifyCode("CommRing")).toBe("typeclass");
    expect(classifyCode("[Add H]")).toBe("typeclass");
    expect(classifyCode("binding_canonical.py")).toBe("repo-file");
  });
  it("leaves TeX, single words and numbers alone", () => {
    for (const s of ["\\sigma_i", "q", "x", "3,558", "sigma", "R-I"]) expect(classifyCode(s)).toBeNull();
  });
  it("a fenced block is not prose", () => {
    expect(failing("```lean\ntheorem foo_bar : True := trivial\n```")).toEqual([]);
  });
});

describe("L3 person", () => {
  it("first and second person fail", () => {
    expect(failing("We define the operational entropy as:")).toContain("L3:we");
    expect(failing("It remains conjectural that our specific GS order matches.")).toContain("L3:our");
    expect(failing("for the reader who prefers geometry")).toContain("L3:the reader");
  });
  it("Roman numerals and 'US' are not pronouns", () => {
    expect(failing("Regime I and Type I; Part I; the US convention")).toEqual([]);
  });
  it("person inside a quotation is the quoted author's, not the paper's", () => {
    expect(failing('Heisenberg wrote that "what we observe is not nature in itself".')).toEqual([]);
    expect(failing('> “We may assume the existence of an ether.”')).toEqual([]);
    expect(failing('Wigner, a "wonderful gift", which we keep.')).toContain("L3:we");
  });
});

describe("L4 premature q", () => {
  it("q tokens fail when premature", () => {
    expect(failing("its rigid trace is $\\mathrm{SU}_q(2)$", { premature: true })).toContain("L4:premature-su_q");
    expect(failing("$\\dim_q [V_n] = [n+1]_q$", { premature: true })).toContain("L4:premature-q-integer");
  });
  it("the scanner option still marks them advisory, and is silent where q is introduced", () => {
    expect(failing("$[2]_q$", { premature: true, prematureAdvisory: true })).toEqual([]);
    expect(failing("$[2]_q$")).toEqual([]);
  });
  it("TeX macros containing q are not the symbol q", () => {
    expect(failing("$a \\quad b \\equiv c$", { premature: true })).toEqual([]);
  });
});

describe("owner rulings 2a/3a/1b (exemption sets)", () => {
  const { CODE_BY_DESIGN, REFERENCE_TABLES } = require("./voice-leak-audit");
  it("names the code-by-design and reference chapters", () => {
    expect(CODE_BY_DESIGN.has("appendix-mass-binding-algorithms")).toBe(true);
    expect(CODE_BY_DESIGN.has("appendix-formalisation-notes")).toBe(true);
    for (const c of ["glossary", "notation", "index-of-definitions"]) expect(REFERENCE_TABLES.has(c)).toBe(true);
  });
});

describe("owner ruling 2026-11-20 (every chapter is strict)", () => {
  const { mkdtempSync, mkdirSync, rmSync, writeFileSync } = require("node:fs");
  const { join, relative } = require("node:path");
  const { audit } = require("./voice-leak-audit");
  it("no L4 hit in any chapter is advisory (live corpus + multi-chapter fixture)", async () => {
    const { reports } = await audit("folio/quantum-observable-universe", new Set(["L4"]));
    const advisory = reports.flatMap((r: any) => r.hits).filter((h: any) => h.advisory);
    expect(advisory).toEqual([]);
    const chapters = new Set(reports.map((r: any) => r.chapter));
    expect(chapters.has("introduction")).toBe(false);

    // Synthetic 3-chapter fixture so draining the live corpus to <=1 (or 0) chapters never makes this check vacuous.
    const tmp = mkdtempSync(join(process.cwd(), "folio/.tmp-l4-test-"));
    try {
      for (const ch of ["introduction", "ch-early", "ch-late"]) mkdirSync(join(tmp, ch), { recursive: true });
      const base = tmp.split("/").pop()!;
      writeFileSync(join(tmp, `${base}.ts`), `export default { chapters: [{ dir: "introduction" }, { dir: "ch-early" }, { dir: "ch-late" }] };\n`);
      writeFileSync(join(tmp, "introduction/introduction.ts"), `export default { sections: [{ label: "sec:intro", blocks: ["b0"] }] };\n`);
      writeFileSync(join(tmp, "introduction/b0.ts"), `export default { label: "prose:b0" };\n`);
      writeFileSync(join(tmp, "introduction/b0.md"), `Preview of $q$ and [later](#thm:b3).\n`);
      writeFileSync(join(tmp, "ch-early/ch-early.ts"), `export default { sections: [{ label: "sec:pre", blocks: ["b1"] }, { label: "sec:substrate-parameter", blocks: ["b2"] }] };\n`);
      writeFileSync(join(tmp, "ch-early/b1.ts"), `export default { label: "def:b1" };\n`);
      writeFileSync(join(tmp, "ch-early/b1.md"), `Premature $q$ before introduction section.\n`);
      writeFileSync(join(tmp, "ch-early/b2.ts"), `export default { label: "def:b2" };\n`);
      writeFileSync(join(tmp, "ch-early/b2.md"), `Forward [later](#thm:b3).\n`);
      writeFileSync(join(tmp, "ch-late/ch-late.ts"), `export default { sections: [{ label: "sec:late", blocks: ["b3", "b4"] }] };\n`);
      writeFileSync(join(tmp, "ch-late/b3.ts"), `export default { label: "thm:b3" };\n`);
      writeFileSync(join(tmp, "ch-late/b3.md"), `Forward [same-sec](#thm:b4).\n`);
      writeFileSync(join(tmp, "ch-late/b4.ts"), `export default { label: "thm:b4" };\n`);
      writeFileSync(join(tmp, "ch-late/b4.md"), `Clean block.\n`);
      const syn = await audit(relative(process.cwd(), tmp), new Set(["L4"]));
      expect(syn.reports.flatMap((r: any) => r.hits).filter((h: any) => h.advisory)).toEqual([]);
      const synChapters = new Set(syn.reports.map((r: any) => r.chapter));
      expect(synChapters.has("introduction")).toBe(false);
      expect(synChapters.size).toBe(2);
    } finally {
      rmSync(tmp, { recursive: true, force: true });
    }
  });
});

describe("owner ruling 2026-11-21 (conditional banners may point ahead)", () => {
  const { bannerLines } = require("./voice-leak-audit");
  it("finds single- and multi-line banners, not ordinary prose", () => {
    expect([...bannerLines("**Proposition (conditional on [X](#conj:x)).**\nbody [Y](#prop:y)")]).toEqual([0]);
    expect([...bannerLines("**Proposition (conditional on\n[X](#conj:x)).**\nbody")]).toEqual([0, 1]);
    expect([...bannerLines("**Conditional on [X](#conj:x).**\nbody [Y](#prop:y)")]).toEqual([0]);
    expect([...bannerLines("**Within a QOU with $2 \\mid \\chi(A)$; conditional on [X](#conj:x).**\nbody")]).toEqual([0]);
    expect([...bannerLines("this is conditional on [X](#conj:x).")]).toEqual([]);
  });
});

describe("owner ruling 2026-11-21 (dim_q is defined in Chapter 1)", () => {
  it("\\dim_q is not a premature q token, other q tokens still are", () => {
    expect(failing("a quantum dimension $\\dim_q(\\lambda)$", { premature: true })).toEqual([]);
    expect(failing("$\\dim_q(\\lambda) = [2]_q$", { premature: true })).toContain("L4:premature-q-integer");
  });
});
