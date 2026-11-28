import { chapter, section } from "../../schema/builders";

export default chapter({
  tabLabel: "I",
  title: "Introduction",
  label: "chap:speculative-intro",
  sections: [
    section({
      title: "Scope and epistemic boundary",
      label: "sec:speculative-scope",
      blocks: [
        "speculative-scope-intro",
      ],
    }),
    section({
      title: "Aether parameter conventions and cross-paper references",
      label: "sec:aether-parameter",
      blocks: [
        "aether-parameter-conventions",
      ],
    }),
  ],
});
