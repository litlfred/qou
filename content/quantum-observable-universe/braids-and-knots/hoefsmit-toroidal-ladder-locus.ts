import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-toroidal-ladder-locus",
  title:
    "Toroidal locus of the Hoefsmit mixing ladder: $(n,\\mu) = (d - \\tfrac{1}{2}, \\tfrac{1}{2})$ is forced",
  lean: { ref: "qou:QOU.BraidsAndKnots.toroidal_locus_forced" },
  uses: ["prop:hoefsmit-binding-amplitude"],
  cites: ["wenzl1988c", "whipple1917", "lebedev1965"],
  tags: [
    "hoefsmit",
    "toroidal-harmonics",
    "legendre-ladder",
    "channel-interpolation",
    "half-integer-degree",
    "lepton-meson-bridge",
  ],
});
