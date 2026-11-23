import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hopf-link-non-magic",
  title:
    "Hopf link as the canonical non-magic knot operator (lowest cohomological degree)",
  interprets: "prop:knot-operator-selection",
  uses: ["prop:torus-knot-shell-binding"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "The withdrawal of the T(2,n_s) shell-size rule is an owner ruling of 2026-11-21 (docs/coordination/owner-rulings.md). The ruling attribution was moved here from the prose on QA review of #8837." },
    { kind: "note", date: "2026-11-21", body: "Owner ruling 2026-11-21: the nuclear Regime-I shell-size rule T(2,n_s) is withdrawn. The citation of prop:torus-knot-shell-binding now says so instead of using it as a result." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): It contributes only the $E^{0, *}$\ncomponent of the SDP optimum\n([prop:knot-operator-selection](#prop:knot-operator-selection))." },
  ],
  tags: [
    "hopf-link",
    "knot-operator",
    "cohomology",
    "non-magic",
    "torus-knot",
    "spectral-sequence",
  ],
});
