import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:parity-violation-skein",
  label: "rem:parity-violation-skein-interpretation",
  title: "Physical interpretation: maximal parity violation and CP",
  uses: ["prop:parity-violation-skein", "def:beta-decay-skein"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): relabelled the electron from the trefoil T_{2,3} to the word sigma_0 sigma_1 sigma_0 in B_3 (closure: Hopf link). Wording only; no number moved." },
  ],
});
