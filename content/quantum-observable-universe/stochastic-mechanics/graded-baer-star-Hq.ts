import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:graded-baer-star-Hq",
  title:
    "Graded Baer-* on $\\mathcal{H}_q$ across the depth filtration",
  lean: { ref: "qou:QOU.BraidKnot.GradedBaerStarHq", validation: "stub" },
  cites: ["bloch2000", "kontsevich1995"],
  tags: [
    "tier:S",
    "graded-baer-star",
    "graded-mikusinski",
    "depth-filtration",
    "explicit-witnesses",
    "bar-involution",
    "open-problem",
  ],
  uses: [
    "def:frobenius-hopf-substrate",
    "conj:gb-depth-period-correspondence",
    "prop:hecke-baer-star-generic",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open at depth $\\geq 3$**, conditional on\n[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence).\nThe depth-2 case follows from\n[`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic)\nand the Schur–Weyl identification of $\\mathrm{Li}_2^q$ values\nwith Markov-trace cell pairings.\n\n**Discharge target.** Construct an explicit projection-generation\nalgorithm at depth 3 using $\\mathrm{Li}_3^q$-Hodge theory\n(Beilinson–Levin polylogs, motivic complexes). The\nGaroufalidis–Lê 3D-index machinery is a candidate technical input.",
    },
  ],
});
