import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:strangelet-crossing-energy",
  lean: { ref: "qou:QOU.Observations.strangelet_crossing_energy", validation: "not_started" },
  title:
    "Crossing energy of strange quark matter is purely strong",
  tags: [
    "strangelet",
    "strange-quark-matter",
    "crossing-energy",
    "coulomb-charge",
    "electromagnetic-neutrality",
    "witten",
  ],
});
