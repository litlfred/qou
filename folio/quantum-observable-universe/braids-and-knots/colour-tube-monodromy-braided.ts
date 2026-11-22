import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:colour-tube-monodromy-braided",
  title: "Colour-tube monodromy commutes with the colour braiding",
  tags: ["colour", "quantum-group", "brings-surface", "monodromy"],
  uses: ["def:color-tube-fibers", "prop:colour-braid-commuting-singlet"],
});
