import { chapter, section, sectionRef } from "../../schema/builders";

/**
 * Chapter 1: Quantum Observable Universe.
 *
 * Sections can be inline or referenced by name.
 * Referenced sections resolve to `<name>/<name>.ts` in this directory.
 * Blocks within sections are atomic knowledge units (root-name .ts + .md pairs).
 */
export default chapter({
  number: 1,
  title: "Quantum Observable Universe",
  label: "chap:qou",
  sections: [
    // Inline section (simple, few blocks)
    section({
      title: "Introduction",
      label: "sec:qou-intro",
      blocks: [
        "ch1-intro",
      ],
    }),
    // Referenced section (resolves to rigid-monoidal/rigid-monoidal.ts)
    // For now, inline since we haven't created subdirectories yet
    section({
      title: "Preliminary: rigid monoidal categories",
      label: "sec:rigid-monoidal",
      blocks: [
        "rigid-monoidal-category",
        "rigid-monoidal-vect",
      ],
    }),
    // Example of section ref (uncomment when section dir exists):
    // sectionRef({ name: "rigid-monoidal" }),
  ],
});
