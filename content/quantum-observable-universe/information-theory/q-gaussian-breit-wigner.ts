import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-gaussian-solves-q-heat",
  label: "rem:q-gaussian-breit-wigner",
  title: "Breit--Wigner as a uniform scale-mixture of $q$-Gaussians",
  tags: [
    "breit-wigner",
    "lorentzian",
    "resonance",
    "q-gaussian",
    "tsallis",
    "scale-mixture",
    "physicist-friendly",
  ],
  uses: [
    "prop:q-gaussian-solves-q-heat",
    "rem:q-laplacian-expansion",
  ],
});
