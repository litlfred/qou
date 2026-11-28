import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-open-problems",
  title: "Open problems around P versus NP in the QOU",
  tags: ["P-vs-NP", "open-problems", "cellular-automata", "outer-automorphism", "intent"],
  uses: [
    "sec:p-vs-np-boundary-intro",
    "prop:block-rigidity",
    "prop:bounded-width-trace-cost",
    "prop:jvw-tractable-orders",
    "def:observation",
    "prop:q-game-of-life",
    "prop:reeb-turing-completeness-classical",
  ],
  cites: [
    "jaeger1990",
    "bakergillsolovay1975",
    "razborovrudich1997",
    "aaronsonwigderson2009",
    "geckpfeiffer2000",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-28",
      body:
        "Owner instruction 2026-11-28: 'Write and lean prove what you can. Discuss in remark open problems'. Item 8 restates the open target of `docs/audits/2026-11-27-observer-intent-outer-automorphisms.md`; the proved part is `QOU.IntentHolonomy.flux_not_gauge` / `flux_coboundary_is_gauge`. Item 1's carriers are the instance-free classes `QouPNeqNp`, `ResidueFaithfulness`, `JonesComplexityCitations`, `CountingDecisionWorld.Transfer`.",
    },
  ],
});
