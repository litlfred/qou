/**
 * Guard for `paper-commentary-audit.ts`.
 *
 * Covers:
 * - Class L1 (`commentary-lean-prose`): fourth-wall Lean / Mathlib / formalisation mentions,
 *   including positive "Lean carrier / sibling / backing / structure" mentions that the
 *   previous negative-verb regex missed;
 * - Class L2 (`commentary-lean-ident`): backticked Lean FQNs (`QOU.X.thm`, `Mathlib.…`,
 *   `CategoryTheory.…`), `.lean` files, raw block IDs (`def:foo`), and Lean snake/camel
 *   declaration/type identifiers (`dimQK0_eq_evDimQ_chernCharacter`, `su2Character_one`,
 *   `CommRing`, `[Add H]`, `HochschildZero R A`);
 * - Class L4 (`commentary-reading-order`): premature post-Ch1 concepts in Chapter 1
 *   (`quantum-universes`) and forward `](#label)` cross-references in Chapters 1–2;
 * - Formalisation status, corpus history, repository furniture, provenance, agent speech,
 *   and the brief-status allowance on open conjectures.
 */
import { describe, expect, it } from "bun:test";
import { scanCommentary, classifyLeanIdentBacktick } from "./paper-commentary-audit";

const crit = (src: string, ctx = {}) =>
  scanCommentary(src, ctx).filter((h) => !h.advisory).map((h) => h.criterion);

describe("Class L1 — fourth-wall Lean and Mathlib prose mentions", () => {
  it("flags positive Lean carrier/sibling/backing/structure mentions (former loophole)", () => {
    expect(crit("The Lean carrier records the pairing over any commutative ring.")).toContain(
      "commentary-lean-prose",
    );
    expect(crit("The Lean sibling establishes the converse implication.")).toContain(
      "commentary-lean-prose",
    );
    expect(crit("## Lean structure\n\nThe bundle is packaged as a record.")).toContain(
      "commentary-lean-prose",
    );
    expect(crit("**Lean.** The coercion commutes with tensor product.")).toContain(
      "commentary-lean-prose",
    );
  });

  it("flags bare Lean, Mathlib, proved formally, and formalised in", () => {
    expect(crit("This identity is verified in Lean 4 without axioms.")).toContain(
      "commentary-lean-prose",
    );
    expect(crit("The braided hexagon follows from Mathlib coherence.")).toContain(
      "commentary-lean-prose",
    );
    expect(crit("Both directions are proved formally from the trace axioms.")).toContain(
      "commentary-lean-prose",
    );
    expect(crit("The construction is formalised in the companion module.")).toContain(
      "commentary-lean-prose",
    );
  });

  it("does not flag lowercase English verb 'lean' in plain prose", () => {
    expect(crit("The two branches lean toward opposite signs.")).toEqual([]);
  });

  it("exempts introduction/authors-note.md book-level formalisation overview", () => {
    expect(
      crit(
        "Every proof in this paper possesses a corresponding Lean 4 formalisation.",
        { chapter: "introduction", blockName: "authors-note" },
      ),
    ).toEqual([]);
  });
});

describe("Class L2 — backticked Lean identifiers and raw block IDs in prose", () => {
  it("flags backticked Lean FQNs, including inside markdown link labels", () => {
    expect(crit("[`QOU.X.thm`](../lean/QOU/X/Thm.lean) proves the biconditional.")).toContain(
      "commentary-lean-ident",
    );
    expect(crit("See `Mathlib.CategoryTheory.Monoidal.Braided.Basic` for coherence.")).toContain(
      "commentary-lean-ident",
    );
    expect(crit("The class `CategoryTheory.BraidedCategory` supplies the hexagon.")).toContain(
      "commentary-lean-ident",
    );
  });

  it("flags backticked .lean filenames, raw block IDs, Lean types, and snake/camel decls", () => {
    expect(crit("See `ConventionDC3AndTailSelectionDerivation.lean`.")).toContain(
      "commentary-lean-ident",
    );
    expect(crit("By `def:frobenius-hopf-substrate`, the counit is central.")).toContain(
      "commentary-lean-ident",
    );
    expect(crit("The hypothesis stays at `CommRing` with `[Add H]` and `HochschildZero R A`.")).toContain(
      "commentary-lean-ident",
    );
    expect(crit("Theorem `dimQK0_eq_evDimQ_chernCharacter` and `su2Character_one` close it.")).toContain(
      "commentary-lean-ident",
    );
    expect(classifyLeanIdentBacktick("exteriorSquareDim_ne_zero_iff")).toBe("lean-decl-or-type");
  });

  it("exempts registered domain tokens and plain prose markdown links", () => {
    expect(crit("The Cartan weightings `plain`, `KnKp`, and `Kp3` act on `nuc11_interleaved`.")).toEqual(
      [],
    );
    expect(crit("[the associativity theorem](#thm:assoc) establishes the biconditional.")).toEqual(
      [],
    );
  });
});

describe("Class L4 — Part-I reading-order anachronisms", () => {
  it("flags premature substrate-parameter, Hecke, and [n]_q concepts in Chapter 1", () => {
    expect(
      crit("At the substrate parameter $q$, the quantum integer $[2]_q$ enters.", {
        chapter: "quantum-universes",
      }),
    ).toContain("commentary-reading-order");
    expect(
      crit("Crossing the archimedean wall into the Hecke algebra $H_3(q)$.", {
        chapter: "quantum-universes",
      }),
    ).toContain("commentary-reading-order");
    expect(
      crit("The cyclotomic factor $\\Phi_6(q)$ vanishes at primitive roots.", {
        chapter: "quantum-universes",
      }),
    ).toContain("commentary-reading-order");
    expect(
      crit("The cochain map $\\phi_1 \\colon A \\to B$ is $R$-linear.", {
        chapter: "quantum-universes",
      }),
    ).toEqual([]);
  });

  it("flags forward cross-references in Chapters 1-2 while allowing backward refs", () => {
    const labelMap = new Map<string, number>([
      ["def:early", 2],
      ["thm:later", 9],
    ]);
    expect(
      crit("See [early definition](#def:early).", {
        chapter: "quantum-universes",
        readingOrder: { sourceIndex: 5, labelToIndex: labelMap },
      }),
    ).toEqual([]);
    expect(
      crit("See [later theorem](#thm:later).", {
        chapter: "quantum-universes",
        readingOrder: { sourceIndex: 5, labelToIndex: labelMap },
      }),
    ).toContain("commentary-reading-order");
  });
});

describe("existing commentary categories (formal-status, history, repo-ref, provenance, agent)", () => {
  it("formalisation bookkeeping", () => {
    expect(crit("(`QOU.X.assoc_pentagon`, sorry-free).")).toContain("commentary-formal-status");
    expect(crit("The implication above is established in narrative here and is not formalised.")).toContain(
      "commentary-formal-status",
    );
    expect(crit("pending shuffle-Hopf infrastructure absent from Mathlib")).toContain(
      "commentary-formal-status",
    );
  });
  it("corpus history", () => {
    expect(crit("This axiom is what earlier drafts asserted, less directly.")).toContain(
      "commentary-corpus-history",
    );
    expect(crit('an earlier formulation derived "which subgroup"')).toContain(
      "commentary-corpus-history",
    );
    expect(crit("Earlier statements of this definition wrote $\\epsilon$ as …")).toContain(
      "commentary-corpus-history",
    );
  });
  it("repository furniture", () => {
    expect(crit("Both rows are proved in\n`lean/QOU/BraidsAndKnots/Foo.lean`")).toContain(
      "commentary-repo-ref",
    );
    expect(crit("tracked in bean `qou-ab12`")).toContain("commentary-repo-ref");
    expect(crit("see docs/audits/2026-01-01-x.md")).toContain("commentary-repo-ref");
  });
  it("provenance and agent speech", () => {
    expect(crit("measured on 2026-08-30 at 70 dps")).toContain("commentary-provenance");
    expect(crit("an agent found that this session")).toContain("commentary-agent");
  });
});

describe("negatives (math mode, display math, fenced code, plain mathematics)", () => {
  it("mathematics in inline math, multi-line display math, and fences is ignored", () => {
    expect(
      crit("$\\text{Lean sorry-free}$\n$$\n\\text{Lean}\\quad `QOU.X`\n$$\n```lean\ntheorem foo_bar : True := trivial\n```"),
    ).toEqual([]);
  });
  it("plain Milnor-voice mathematics passes cleanly", () => {
    expect(crit("The pair $(\\mathrm{ev}, \\mathrm{coev})$ exhibits $A$ as its own dual.")).toEqual(
      [],
    );
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
