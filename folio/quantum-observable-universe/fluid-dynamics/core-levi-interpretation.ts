import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:core-levi-form",
  label: "rem:core-levi-interpretation",
  title: "Reading the Levi scalar: twist of the vortex lines, not core shape",
  uses: [
    "prop:core-levi-form",
  ],
  // conj:levi-degeneracy sits in a later section of this chapter; the remark
  // points forward to it rather than depending on it.
  foreshadows: ["conj:levi-degeneracy"],
  cites: ["beiraodaveiga2002"],
  tags: ["millennium-problem", "contact", "integrability", "interpretation"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13).** The remark previously displayed " +
        "\"NS blows up $\\Leftrightarrow$ Levi form non-degenerate at collision " +
        "$\\Leftrightarrow$ $\\kappa(t) = O(1)$\", read each outcome (non-degenerate: " +
        "tubular cores, $\\|\\omega\\|_\\infty \\ge c/(T^*-t)$, BKM divergence, " +
        "`conj:ns-counterexample` executes; degenerate: sheet, NS potentially " +
        "regular), and stated a root-of-unity constraint: truncation to " +
        "$(\\kappa-1)/2$ modes caps the core aspect ratio below " +
        "$1 + C(\\kappa-1)$, with the outcome decided by whether $O(\\kappa)$ " +
        "outpaces $O(1/(T^*-t))$. **Withdrawn:** the first equivalence is the " +
        "former branch (A) of `conj:levi-degeneracy`, refuted under this reading " +
        "by the Beltrami flow (scope (b) for that implication only); the second " +
        "identified the core aspect ratio with a Levi condition number, which is " +
        "undefined in dimension 3; the two outcome paragraphs and the " +
        "root-of-unity reading depend on those and go with them. The " +
        "aspect-ratio bound itself was never derived in this block (it rested on " +
        "the withdrawn identification), so no numerical result is lost. " +
        "**Restated:** what the Levi scalar measures, and the two surviving " +
        "statements (open branch (B); cited Beirão da Veiga–Berselli " +
        "contrapositive). `prop:root-of-unity-truncation` dropped from `uses`; " +
        "`conj:levi-degeneracy` added as a forward pointer. Bean `qou-fm7s`.",
    },
  ],
});
