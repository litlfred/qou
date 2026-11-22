import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Fermion-rule ruling (owner card, 2026-11-21 14:31Z, option 'Scope the rule, mark it open'): prop:fermion-boson-knot-link is a statement about the T(2,n) family only. The electron is sigma_0 sigma_1 sigma_0 in B_3 (closure: the Hopf link); its statistics are not classified by that proposition and are open. Issue #8822. The added paragraph scopes the statement; the Lean (fermion_iff_odd, boson_iff_even on T(2,n)) is unchanged." },
  ],
  label: "prop:fermion-boson-knot-link",
  title:
    "Fermions are knots, bosons are links",
  tags: [
    "fermion",
    "boson",
    "knot",
    "link",
    "torus-knot",
    "component",
    "reeb-flow",
    "vertical",
  ],
  lean: { ref: "qou:QOU.Braiding.fermion_boson_knot_link",
    validation: "not_checked",
  },
  uses: ["def:borromean-baryon"],
});
