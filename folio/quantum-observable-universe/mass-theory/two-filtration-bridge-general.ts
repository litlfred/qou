import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:two-filtration-bridge-general",
  title:
    "Two-filtration bridge map in full generality: bar-class determines iterated-integral depth (self-conj $\\to$ 2, chiral pair $\\to$ 3) for all partitions",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral.bridge_map_general",
    validation: "not_checked",
  },
  uses: ["prop:cyclotomic-cl3-orbit-sum-general"],
  cites: ["bloch2000"],
  tags: [
    "two-filtration-bridge",
    "general-partitions",
    "bar-eigenspace",
    "self-conjugate",
    "chiral-pair",
    "graded-mikusinski",
    "conditional",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:two-filtration-bridge-general -> conj:two-filtration-bridge-general." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "**Corrected 2026-11-16 (QA finding: da-non-sequitur, critical).** Step 1 of the " +
        "proof claimed $\\mathrm{bar}(e_\\lambda) = e_{\\lambda'}$. That is false: bar fixes " +
        "every $e_\\lambda$ (checked exactly in $H_2$). The transposing involution is the " +
        "Goldman involution $\\sigma_i \\mapsto -\\sigma_i^{-1}$. The statement is now marked " +
        "conditional on `conj:two-filtration-bridge` and on matching that involution with " +
        "orientation reversal. Under §3b this block should become a `conjecture` (or a " +
        "non-degenerate conditional class); the Lean `bridge_map_general` is a projection " +
        "of a class field equal to its conclusion. Both are queued for the weak-proofs pass. " +
        "No compute impact.",
    },
  ],
});
