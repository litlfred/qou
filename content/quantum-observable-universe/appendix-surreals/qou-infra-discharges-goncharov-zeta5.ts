import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-infra-discharges-goncharov-zeta5",
  title:
    "QOU's Hecke-NF + Bring-$S_5$ infrastructure discharges Goncharov's depth-3 conjecture at $F = \\mathbb{Q}(\\zeta_5)$",
  uses: [
    "conj:gb-depth-period-correspondence",
    "prop:depth-2-identification-bloch-suslin",
    "prop:borel-partial-resolution",
    "conj:bring-trilog-depth-3-witness",
    "conj:joint-galois-braid-action",
    "prop:explicit-central-idempotent",
    "rem:conway-kt-vol-injectivity-test",
    "rem:k-theory-period-rosetta",
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
