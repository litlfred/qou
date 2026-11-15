import { remark } from "../../schema/builders";

export default remark({
  label: "rem:trefoil-vortex-chirality-flip",
  title: "Chirality stability of trefoil vortices",
  interprets: "prop:antiparticle-crossing-reversal",
  uses: ["rem:vortex-intensity-modes"],
  tags: [
    "vortex", "chirality", "reconnection", "trefoil",
    "fluid-dynamics", "stability", "exceptional-divisor",
  ],
  cites: ["kleckner2013", "scheeler2014"],
});
