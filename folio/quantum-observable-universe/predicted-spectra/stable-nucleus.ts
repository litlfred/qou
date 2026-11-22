import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-nucleus",
  title: "Stable nucleus (Skein energy minimum)",
  tags: [
    "nucleus",
    "stability",
    "hadron",
    "proton",
    "neutron",
    "binding",
    "beta-stability",
    "lagrangian",
  ],
  lean: { ref: "qou:QOU.Torsion.StableNucleus",
    validation: "not_checked",
  },
  uses: ["def:categorical-neutron", "prop:beta-stability"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): the appended electrons are written e^- (the word sigma_0 sigma_1 sigma_0) rather than the trefoil T_{2,3}." },
  ],
});
