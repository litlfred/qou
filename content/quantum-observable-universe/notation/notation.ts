import { chapter, section } from "../../schema/builders";

/**
 * Notation register — front-matter chapter rendered immediately after
 * the TOC. Authoritative source for every mathematical symbol used in
 * the paper, organised by the chapter where each symbol is first
 * introduced. CLAUDE.md §7aa is a pointer to this block.
 */
export default chapter({
  tabLabel: "N",
  title: "Notation",
  label: "chap:notation",
  sections: [
    section({
      title: "Symbols by introducing chapter",
      blocks: [
        "notation-register",
      ],
    }),
    section({
      title: "Key collision avoidances",
      blocks: [
        "notation-collisions",
      ],
    }),
  ],
});
