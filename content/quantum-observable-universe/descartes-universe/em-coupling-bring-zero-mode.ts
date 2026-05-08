import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:em-coupling-bring-zero-mode",
  title:
    "Conjectured closed form $1/\\alpha_{EM} = q\\cdot[9]_q\\cdot[10]_q + 2g/(4\\pi(g-1))$ via Bring's-surface photon zero-mode",
  uses: [
    "prop:em-coupling-projection",
    "prop:force-carrier-bring-uniqueness",
    "prop:exterior-square-borromean",
    "conj:archimedean-functor-uniqueness",
    "rem:figure-8-archimedean-illustration",
  ],
  cites: ["jones1987", "kassel1995", "suslin1991", "bloch2000"],
  tags: [
    "alpha-em",
    "fine-structure",
    "brings-surface",
    "genus-4",
    "zero-mode",
    "gauss-bonnet",
    "conjecture",
    "derivation-lead",
  ],
});
