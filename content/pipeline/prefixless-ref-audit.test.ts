/**
 * Guard for `prefixless-ref-audit.ts`.
 *
 * The audit returns "35 legitimate, 0 dangling" on the live corpus and has
 * never returned anything else, so its two interesting branches — a bare
 * reference to a MISSING block, and a bare reference to a block whose kind
 * DOES require a prefix — have no live coverage. AGENTS.md records this exact
 * trap twice (`qou-t0wm`: "zero hits is not the same as verified sound"), so
 * the branches are exercised here instead.
 */
import { describe, expect, it } from "bun:test";
import { bareRefsOf, classifyTarget } from "./prefixless-ref-audit";

describe("bareRefsOf", () => {
  it("finds a prefix-less entry and ignores the prefixed ones", () => {
    const rows = bareRefsOf("tbl:x-data", "table", {
      uses: ["tm-notation", "def:transfer-matrix-operator", "prop:foo"],
    });
    expect(rows.map((r) => r.ref)).toEqual(["tm-notation"]);
    expect(rows[0]!.field).toBe("uses");
    expect(rows[0]!.srcKind).toBe("table");
  });

  it("covers interprets and the other list fields, and dedupes within a field", () => {
    const rows = bareRefsOf("rem:x", "remark", {
      uses: ["a-bare", "a-bare"],
      foreshadows: ["b-bare"],
      proofs: ["c-bare"],
      examples: ["d-bare"],
      interprets: "e-bare",
    });
    expect(rows.map((r) => r.ref).sort()).toEqual([
      "a-bare", "b-bare", "c-bare", "d-bare", "e-bare",
    ]);
  });

  it("does not treat a cross-paper or absolute reference as bare", () => {
    const rows = bareRefsOf("rem:x", "remark", {
      uses: [
        "unital-groebner-bases:cor:pbw",
        "https://folio.example.org/papers/foo#def:bar",
      ],
    });
    expect(rows).toEqual([]);
  });

  it("ignores non-string junk rather than throwing", () => {
    const rows = bareRefsOf("rem:x", "remark", { uses: [1, null, "ok-bare"], interprets: 7 });
    expect(rows.map((r) => r.ref)).toEqual(["ok-bare"]);
  });
});

describe("classifyTarget", () => {
  it("calls a missing target dangling — the branch the live corpus never reaches", () => {
    expect(classifyTarget(undefined)).toBe("dangling");
  });

  it("accepts the kinds whose label prefix is optional", () => {
    for (const k of ["prose", "equation", "diagram"]) expect(classifyTarget(k)).toBe("ok");
  });

  it("flags a bare reference to a kind that requires a prefix", () => {
    for (const k of ["definition", "proposition", "theorem", "table", "remark"])
      expect(classifyTarget(k)).toBe("convention");
  });
});
