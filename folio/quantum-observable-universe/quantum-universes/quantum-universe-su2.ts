import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-universe",
  label: "ex:quantum-universe-su2",
  title: "$\\mathrm{SU}(2)$ as a quantum universe",
  lean: { ref: "qou:QOU.Examples.su2QuantumUniverse", validation: "not_checked" },
  tags: ["su2", "quantum"],
  uses: [
    "def:frobenius-pairing",
    "ex:rigid-monoidal-vect",
  ],
  foreshadows: ["prop:braiding-induced-ordering", "ex:su2-characters-and-quantum-dimension"],
  cites: ["kassel1995"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Item (v) added by the running-example audit (bean qou-zq1r): the example at q = 1 does not satisfy axiom 1 as written, because the flip is symmetric and prop:braiding-induced-ordering supplies the ordering only for a non-symmetric braiding. The example is presented as the symmetric point of the SU_q(2) family; the Lean sibling's SU2QuantumUniverseData carries no braiding field, and a QuantumUniverse instance for the q ≠ 1 family is the open Lean item.",
    },
  ],
});
