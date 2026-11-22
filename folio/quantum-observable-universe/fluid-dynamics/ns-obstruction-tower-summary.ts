import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-obstruction-tower-summary",
  title: "The NS obstruction as a local-cohomology residue",
  interprets: "prop:ns-obstruction-tower",
  uses: ["conj:levi-degeneracy"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13).** Previous text: \"It remains nonzero (confirming NS-singular " +
        "blowup) if and only if the local cohomology $H^1_{\\mathfrak{m}_p}(A)$ " +
        "holds a nonzero value at collision points. This matches the exact " +
        "condition where the Levi form evades degeneracy (maintaining a bounded " +
        "core aspect ratio). The Levi degeneracy conjecture isolates whether " +
        "$\\kappa_n|_\\Sigma$ collapses or survives through the strict $q \\to 1$ " +
        "limit.\" Withdrawn with proof step (d) of `prop:ns-obstruction-tower` " +
        "(no Levi eigenvalue pair in dimension 3). Restated: the proposition is " +
        "conditional, its criterion is non-discriminating as its own proof notes, " +
        "and `conj:levi-degeneracy` (branch (B), on $\\xi\\cdot\\mathrm{curl}\\,\\xi$) " +
        "is not connected to $\\kappa_n|_\\Sigma$ by any result. Bean `qou-fm7s`.",
    },
  ],
  tags: ["navier-stokes", "obstruction", "local-cohomology", "levi-form"],
});
