import { describe, expect, test } from "bun:test";
import { compare, shrink, type Counts } from "./voice-leak-ratchet";

const base: Counts = { "a.md": { "L3:we": 2, "L2:fqn": 1 }, "b.md": { "L1:lean-word": 1 } };

describe("voice-leak-ratchet", () => {
  test("unchanged counts pass", () => {
    expect(compare(base, base).grown).toEqual([]);
  });
  test("a count above baseline fails", () => {
    const v = compare(base, { ...base, "a.md": { "L3:we": 3, "L2:fqn": 1 } });
    expect(v.grown).toEqual(["a.md  L3:we: 2 -> 3"]);
  });
  test("a new file with a leak fails", () => {
    expect(compare(base, { ...base, "c.md": { "L3:our": 1 } }).grown).toEqual(["c.md  L3:our: 0 -> 1"]);
  });
  test("a new sub-kind in a known file fails", () => {
    expect(compare(base, { ...base, "b.md": { "L1:lean-word": 1, "L2:decl-name": 1 } }).grown.length).toBe(1);
  });
  test("drained counts pass and are reported", () => {
    const v = compare(base, { "a.md": { "L3:we": 1 } });
    expect(v.grown).toEqual([]);
    expect(v.drained.length).toBe(3);
  });
  test("shrink never raises and never adds", () => {
    const s = shrink(base, { "a.md": { "L3:we": 5 }, "c.md": { "L3:our": 4 } });
    expect(s).toEqual({ "a.md": { "L3:we": 2 } });
  });
});
