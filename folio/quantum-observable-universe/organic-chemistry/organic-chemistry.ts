import { chapter, section } from "../../schema/builders";

/**
 * Chapter 10: Organic Chemistry from Hopf Chains.
 *
 * Carbon's half-filled second shell (4 open linking sites) gives it
 * unique chain-forming ability.  This chapter develops the theory of
 * molecular Hopf chains and threaded rings, introduces the threading
 * link T(2,N) whose Alexander polynomial halves the crossing energy,
 * and compares the predicted C₆ chain → benzene barrier to experiment
 * with no free parameters.
 */
export default chapter({
  title: "Organic Chemistry from Hopf Chains",
  label: "chap:organic-chemistry",
  sections: [
    // ── §1. Covalent bonding as shared sub-Hopf links ────────────────
    section({
      title: "Covalent bonding as shared sub-Hopf links",
      label: "sec:covalent-bonding",
      blocks: [
        "covalent-bonding-intro",
        "covalent-bond-types",
        "covalent-bond-types-remark",
        "carbon-valence",
      ],
    }),

    // ── §2. Molecular Hopf chains and rings ──────────────────────────
    section({
      title: "Molecular Hopf chains and rings",
      label: "sec:molecular-chains-rings",
      blocks: [
        "molecular-chains-rings-intro",
        "molecular-hopf-chain",
        "molecular-hopf-chain-crossing-energy",
        "threading-link",
        "threading-link-remark",
        "threading-link-alexander",
        "threading-link-weight",
        "molecular-hopf-ring",
        "hopf-ring-rigidity",
        "chain-spring-modes",
        "ring-closure-barrier",
        "ring-closure-superstability",
      ],
    }),

    // ── §3. Carbon chains, benzene, and organic chain taxonomy ───────
    // P11 fold (2026-05-18): sec:organic-taxonomy (2 blocks: intro +
    // remark) had a 1-block remark backed by a draft prose intro. Per
    // detangler watcher proposal: fold the taxonomy as a coda of the
    // carbon-chains-benzene section. Result: 3 sections of densities
    // 2/5/7 (was 2/5/4/2), all within the 3-18 band, eliminates the
    // 50% cross-section ratio finding on this chapter.
    section({
      title: "Carbon chains, benzene, and organic chain taxonomy",
      label: "sec:carbon-chains-benzene",
      blocks: [
        "carbon-chains-benzene-intro",
        "carbon-chain-c6",
        "benzene-ring",
        "chain-ring-energy",
        "chain-ring-comparison",
        "chain-ring-comparison-interpretation",
        "chain-ring-open-problems",
        "chain-ring-comparison-table3-data",
        "chain-ring-comparison-table2-data",
        "chain-ring-comparison-table1-data",
        "organic-taxonomy-intro",
        "organic-chain-taxonomy",
        "outro-organic-chemistry",
      ],
    }),
  ],
});
