import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-infra-discharges-goncharov-zeta5",
  title:
    "QOU's Hecke-NF + Bring-$S_5$ infrastructure discharges Goncharov's depth-3 conjecture at $F = \\mathbb{Q}(\\zeta_5)$",
  lean: { ref: "qou:QOU.AppendixSurreals.QouInfraDischargesGoncharovZeta5", validation: "stub" },
  uses: [
    "prop:depth-2-identification-bloch-suslin",
    "rem:conway-kt-vol-injectivity-test",
  ],
  cites: ["bloch2000", "kontsevich1995", "zagier1986"],
  tags: [
    "goncharov-conjecture",
    "depth-3",
    "bring-S5",
    "hecke-NF",
    "qou-infra-program",
    "graded-mikusinski",
    "research-program",
    "open-problem",
  ],
});
