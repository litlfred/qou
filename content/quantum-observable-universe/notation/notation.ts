import { chapter, section } from "../../schema/builders";

/**
 * Notation register — front-matter chapter rendered immediately after
 * the TOC. Authoritative source for every mathematical symbol used in
 * the paper, organised by the chapter where each symbol is first
 * introduced. AGENTS.md §7aa is a pointer to this block.
 */
export default chapter({
  tabLabel: "N",
  title: "Notation",
  label: "chap:notation",
  sections: [
    section({
      title: "Symbols by introducing chapter",
      label: "sec:notation-register-section",
      blocks: [
        "notation-register-section-intro",
        "notation-register",

        "notation-register-table1-data",
        "notation-register-table2-data",
        "notation-register-table3-data",
        "notation-register-table4-data",
        "notation-register-table5-data",
        "notation-register-table6-data",
        "notation-register-table7-data",
        "notation-register-table8-data",
        "notation-register-table9-data",
      ],
    }),
    section({
      title: "Key collision avoidances",
      label: "sec:notation-collisions-section",
      blocks: [
        "notation-collisions",
      ],
    }),
  ],
});
