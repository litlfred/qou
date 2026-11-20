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
});

describe("L4 premature q (Chapter 1 only)", () => {
  it("q tokens fail when premature", () => {
    expect(failing("its rigid trace is $\\mathrm{SU}_q(2)$", { premature: true })).toContain("L4:premature-su_q");
    expect(failing("$\\dim_q [V_n] = [n+1]_q$", { premature: true })).toContain("L4:premature-q-integer");
  });
  it("are advisory in Chapter 2 and silent where q is introduced", () => {
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
