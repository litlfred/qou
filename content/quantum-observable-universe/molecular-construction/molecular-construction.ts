import { chapter, section } from "../../schema/builders";

/**
 * Chapter 12: Molecular Construction from Nucleon Braids.
 *
 * Extends the iterative atomic braid constructor (Ch 11) to molecules.
 * Atoms are built bottom-up from nucleons, then joined via shared
 * electron trefoils (covalent bonds).  The LP dual finds optimal
 * binding at each stage.
 *
 * Computational progression:
 *   H₂ → CO → CO₂ → CH₄ → C₂H₆ → C₆H₆
 * Each molecule is computed iteratively: build atoms, then assemble
 * the molecular braid and optimize binding.
 */
export default chapter({
  title: "Molecular Construction from Nucleon Braids",
  label: "chap:molecular-construction",
  sections: [
    // ── §1. From atoms to molecules ─────────────────────────────────
    section({
      title: "The molecular Hecke algebra",
      label: "sec:molecular-hecke-algebra",
      blocks: [
        "molecular-hecke-algebra-intro",
        "molecular-braid",
        "molecular-crossing-table",
        "covalent-bond-shared-trefoil",
        "ilp-covalent-bond",
      ],
    }),

    // ── §2. Electron shells as braid capacity ───────────────────────
    section({
      title: "Electron shells and bonding capacity",
      label: "sec:electron-shells",
      blocks: [
        "electron-shells-intro",
        "electron-shell-braid-capacity",
        "shell-filling-rule",
        "valence-from-braid",
        "shell-closure-nf-term-count",
        "palindromicity-orbital-type",
      ],
    }),

    // ── §3. H₂: the covalent bond prototype ────────────────────────
    section({
      title: "Hydrogen molecule $H_2$: the covalent bond prototype",
      label: "sec:h2-computation",
      blocks: [
        "h2-computation-intro",
        "h2-molecular-braid",
        "h2-lp-dual-binding",
        "h2-binding-energy",
        "h2-bond-length-interpretation",
      ],
    }),

    // ── §4. CO: heteronuclear bonding ───────────────────────────────
    section({
      title: "Carbon monoxide: heteronuclear bonding",
      label: "sec:co-computation",
      blocks: [
        "co-computation-intro",
        "co-molecular-braid",
        "co-lp-dual-binding",
        "co-triple-bond-energy",
      ],
    }),

    // ── §5. CO₂: linear triatomic ──────────────────────────────────
    section({
      title: "Carbon dioxide: linear triatomic molecule",
      label: "sec:co2-computation",
      blocks: [
        "co2-computation-intro",
        "co2-molecular-braid",
        "co2-lp-dual-binding",
        "co2-double-bond-symmetry",
      ],
    }),

    // ── §6. CH₄: tetrahedral methane ────────────────────────────────
    section({
      title: "Methane: tetrahedral bonding from braid optimization",
      label: "sec:ch4-computation",
      blocks: [
        "ch4-computation-intro",
        "ch4-molecular-braid",
        "ch4-lp-dual-binding",
        "ch4-tetrahedral-symmetry",
      ],
    }),

    // ── §7. C₆H₆: benzene and delocalization ──────────────────────
    section({
      title: "Benzene: delocalization from threading links",
      label: "sec:benzene-computation",
      blocks: [
        "benzene-computation-intro",
        "benzene-molecular-braid",
        "benzene-threading-emergence",
        "benzene-bond-equalization",
        "outro-molecular-construction",
      ],
    }),
  ],
});
