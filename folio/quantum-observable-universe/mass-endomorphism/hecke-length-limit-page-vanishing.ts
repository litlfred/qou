import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:hecke-length-limit-page-vanishing",
  title:
    "Vanishing above the diagonal of the length-filtered limit page, at every $n$",
  uses: [
    "prop:gb-spectral-sequence",
    "prop:spectral-sequence-collapse",
  ],
  cites: ["dipper-james1986", "weibel1994"],
  tags: ["spectral-sequence", "hochschild", "coxeter-length", "shell-condensation"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body: "Owner, 2026-11-20 (option 2 of the shell-condensation card): adopt the Hecke reading of `conj:homological-shell-condensation` and prove it for all $n$. This corollary is that reading. It holds at every $n$, so it does not single out the magic numbers; the conjecture stays open for the reading the owner names (option 1). Analysis: `docs/audits/2026-11-20-homological-shell-condensation-well-posedness.md`, bean `qou-6qbv`. No Lean sibling: Mathlib has no Hochschild cohomology, which the proof needs.",
    },
  ],
});
