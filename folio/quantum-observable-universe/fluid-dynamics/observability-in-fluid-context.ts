import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:observability-fluid-context",
  title:
    "Observability for the brane fluid",
  uses: ["prop:core-levi-form"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13).** Withdrawn: (i) the \"contact-geometric translation\" — " +
        "\"The Levi form $\\mathcal{L}_\\varTheta$ operates non-degenerately " +
        "everywhere. The horizontal distribution $\\ker(\\varTheta)$ stays maximally " +
        "non-integrable\"; (ii) fluid item 2, \"Vortex cores are tubular: the " +
        "core-Levi equivalence ensures that non-degenerate Levi form caps the core " +
        "aspect ratio\"; (iii) two bullets of the alternative, \"a 1-dimensional " +
        "foliation embedded in the contact distribution\" and \"a structural " +
        "mechanism enabling vortex cores to unroll into sheets\". Reason: on the " +
        "3D flow domain the Levi datum of $\\ker\\varTheta = \\xi^\\perp$ is the " +
        "single scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$ (`prop:core-levi-form`); it " +
        "carries no core-shape information (a straight anti-parallel pair has " +
        "scalar 0 for every core shape), and no result links its non-vanishing to " +
        "$\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$. The categorical, gauge " +
        "and remaining fluid readings are untouched and were not re-examined here; " +
        "the leak sentence's \"integrable direction\" now reads \"preferred " +
        "direction\", the term the list above it introduces. " +
        "Bean `qou-fm7s`.",
    },
  ],
  tags: [
    "observability",
    "fluid-dynamics",
    "contact",
    "vortex",
    "interpretation",
  ],
});
