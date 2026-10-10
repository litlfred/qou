import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:descartes",
  label: "rem:universality-general",
  title: "Universality for a given Euler characteristic",
  tags: ["archimedean-universe", "universality", "euler-characteristic"],
  uses: [
    "thm:descartes",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "The moduli were indexed by `chi(S)`, the Euler characteristic of the state bundle; by multiplicativity that is `2 chi_eu(M_0)` for the sphere bundle and is not the invariant the Descartes condition fixes. Re-indexed by `chi_eu(M_0)`, the base curve, per the 2026-09-15 separation of the three Euler characteristics.",
    },
  ],
});
