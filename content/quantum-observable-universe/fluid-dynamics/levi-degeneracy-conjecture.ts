import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:levi-degeneracy",
  title:
    "Levi degeneracy conjecture: contact non-degeneracy at vortex collision determines NS regularity",
  uses: [
    "prop:core-levi-form",
    "prop:root-of-unity-truncation",
  ],
  tags: [
    "conjecture",
    "levi-form",
    "contact-degeneracy",
    "millennium-problem",
    "root-of-unity",
    "navier-stokes",
  ],
});
