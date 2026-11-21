import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-transfer-matrix",
  lean: { ref: "qou:QOU.CategoricalTransferMatrix", validation: "not_checked" },
  title: "Categorical transfer matrix",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "equivalence-class", "braiding", "configuration-space",
    "interaction-filtration",
  ],
  uses: [
    // conj:crystal-graph-realization removed (qou-tm3c): the definition does not mention crystals.
    "rem:knot-factorization",
    "rem:jet-planck-steps",
    "rem:observation-braid",
    "def:operational-entropy",
  ],
  cites: [
    "brundankleshchev2009",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "**The `lean.ref` named the wrong structure, and the two are not " +
        "variants of one thing.** It read " +
        "`qou:QOU.Torsion.CategoricalTransferMatrix`, which is a REAL and " +
        "live library structure in `QOU/Torsion/MassGap.lean` — a spectral " +
        "mass-gap object (`eigenvalues : N -> R`, `vacuum_eigenvalue`, " +
        "`eigenvalues_mono`, `gapValue`), with consumers in " +
        "`QOU.BraidKnot.MassGapKeystone` and `MassGapFrontier`. This block's " +
        "`.md` describes something else entirely: an equivalence class of " +
        "braiding operations on a hadron under equal vertex volume. That is " +
        "the SIBLING's `QOU.CategoricalTransferMatrix` (insertion " +
        "configuration + bi-filtration + vertex volume). Two different " +
        "objects sharing a base name across namespaces, and the ref picked " +
        "the one that does not match the prose. Repointed to " +
        "`qou:QOU.CategoricalTransferMatrix`; the `.jsonld` leanRef and the " +
        "definition-index row follow. The sibling is NOT deleted — it is the " +
        "object the .md is about.\n\n" +
        "**The bare `axiom transfer_matrix_level_independence` was FALSE.** " +
        "It asserted `T1.base = T2.base -> T1.vertex_volume = " +
        "T2.vertex_volume`, and `vertex_volume` is a free field, so two " +
        "matrices may share a base and carry any two values. " +
        "`level_independence_false_as_stated` now proves that refutation. " +
        "The defect is the .md's own reasoning being dropped in the " +
        "encoding: the block says the class is well-defined *because* the " +
        "volume 'depends only on the Markov trace of the Hecke-reduced " +
        "element'. Carrying it as free data discards exactly that. " +
        "`DerivedVertexVolume` restores it, and the true statement " +
        "hypothesises equal FILTRATION, not equal base.\n\n" +
        "Also: `base` is now a type parameter. `ExceptionalDivisor` is " +
        "unreachable (a sibling) and, in the library, lives in " +
        "`ArchimedeanUniverse` — the archimedean side of the ss7c wall, " +
        "while this file is over `R_q`.",
    },
  ],
});
