import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:two-filtration-bridge-general",
  title:
    "Two-filtration bridge map in full generality: bar-class determines iterated-integral depth (self-conj $\\to$ 2, chiral pair $\\to$ 3) for all partitions",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral.bridge_map_general",
    validation: "not_checked",
  },
  uses: ["prop:cyclotomic-cl3-orbit-sum-general", "prop:cellular-depth-filtration"],
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - Joint action discharge: [Joint motivic-Galois $\\times$ braid action commutes on every bi-filtration cell — discharged](#prop:joint-galois-braid-discharged)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - Small-cases verification: [Two-filtration bridge map verified at small partitions ($n \\leq 4$)](#prop:two-filtration-bridge-small-cases)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Comparison, not a consequence.**\n[General orbit-sum identity: $\\sum_k \\mathrm{Cl}_3(2\\pi k/N) = -(N^2-1)/N^2 \\cdot \\zeta(3)$ at every $N \\geq 2$](#prop:cyclotomic-cl3-orbit-sum-general)\nand\n[Trilogarithm imaginary part at $\\zeta_n$: closed form $(n - 1)(n - 2)\\pi^3 / (3 n^3)$ for every root of unity](#prop:cyclotomic-trilog-imaginary-closed-form)\ncount the depth-3 content over $\\mathbb{Q}(\\zeta_N)$ for prime $N$ as\n$\\lfloor (N - 1)/2 \\rfloor - 1$ new real numbers. That these pair with\nchiral-pair cells of some $H_n(q)$ would need the realisation $\\Phi$ above;\nit does not follow from this conjecture as stated." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [Two-filtration bridge map verified at small partitions ($n \\leq 4$)](#prop:two-filtration-bridge-small-cases)\nverified the bridge map $d_{\\mathrm{II}}$ at all partitions of $n \\leq 4$.\n*This conjecture proposes the extension to **all** partitions of any $n$." },
    { kind: "status", date: "2026-11-16", body: "Restated 2026-11-16: the provable core is item 4 of prop:cellular-depth-filtration (conditional parity transfer under H-match and H-parity, Lean-checked). The 'otherwise' branch of d_II is empty, so the boxed formula restates the definition; the 'Generalisation' and cyclotomic corollary sentences were not consequences and are reworded as comparison. No compute impact." },
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
