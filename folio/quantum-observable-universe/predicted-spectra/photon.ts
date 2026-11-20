import { definition } from "../../schema/builders";

export default definition({
  label: "def:photon",
  title: "Photon (four-term Hecke element)",
  tags: ["photon", "hecke-algebra", "colored-photon", "gamma-gamma", "definition"],
  defines: ["photon", "bare-photon", "colour-weights"],
  lean: { ref: "qou:QOU.Photon.photon", validation: "not_checked" },
});
