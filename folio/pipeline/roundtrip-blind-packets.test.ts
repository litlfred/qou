import { describe, expect, test } from "bun:test";
import {
  extractFocusedLeanViews,
  scrubBlindProofMarkdown,
  splitInlineProof,
  stripLeanComments,
  stripProofFromTheoremChunk,
} from "./roundtrip-blind-packets";

describe("roundtrip-blind-packets scrubber", () => {
  test("strips nested /- ... -/ docstrings and -- comments while keeping string literals", () => {
    const src = `
/-! # Secret physics title
   /- nested comment -- still comment -/
   Spoiler: proton mass! -/
def foo (s : String := "-- not a comment /- neither -/") : Nat := -- inline spoiler
  42
`;
    const out = stripLeanComments(src);
    expect(out).not.toContain("Secret physics title");
    expect(out).not.toContain("proton mass");
    expect(out).not.toContain("inline spoiler");
    expect(out).toContain('"-- not a comment /- neither -/"');
    expect(out).toContain("def foo");
    expect(out).toContain("42");
  });

  test("replaces top-level theorem proof with sorry without breaking default binder := args", () => {
    const chunk = `theorem bar (n : Nat := 3) (h : 0 < n) : n = n := by
  rfl`;
    expect(stripProofFromTheoremChunk(chunk)).toBe(
      `theorem bar (n : Nat := 3) (h : 0 < n) : n = n := sorry`,
    );
  });

  test("extractFocusedLeanViews keeps helper defs, strips target proof for RT-1, keeps proof for RT-2", () => {
    const raw = `
/-! Module spoiler -/
def helperVal (x : Int) : Int := x + 1

/-- Docstring spoiler -/
theorem target_thm (x : Int) : helperVal x > x := by
  unfold helperVal
  omega

theorem unrelated_later (y : Int) : y = y := by rfl
`;
    const { signatureOnly, fullTargetProof } = extractFocusedLeanViews(raw, "QOU.Foo.target_thm");
    expect(signatureOnly).toContain("def helperVal (x : Int) : Int := x + 1");
    expect(signatureOnly).toContain("theorem target_thm (x : Int) : helperVal x > x := sorry");
    expect(signatureOnly).not.toContain("omega");
    expect(signatureOnly).not.toContain("unrelated_later");
    expect(signatureOnly).not.toContain("spoiler");

    expect(fullTargetProof).toContain("omega");
    expect(fullTargetProof).not.toContain("unrelated_later");
  });

  test("splits inline **Proof.** and scrubs #anchor spoilers", () => {
    const md = `**Theorem.** For $q > 1$, [Hecke normal form](#def:hecke-normal-form) holds.\n\n**Proof.** By [the lemma](#lem:secret-name), $q > 0$.`;
    const { stmtMd, inlineProofMd } = splitInlineProof(md);
    expect(stmtMd).toContain("For $q > 1$");
    expect(stmtMd).not.toContain("lem:secret-name");
    expect(inlineProofMd).toBeDefined();
    const scrubbed = scrubBlindProofMarkdown(inlineProofMd!);
    expect(scrubbed).toBe("By the lemma, $q > 0$.");
  });
});
