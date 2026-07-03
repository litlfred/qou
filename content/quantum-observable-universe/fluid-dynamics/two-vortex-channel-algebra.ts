import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-vortex-channel-algebra",
  title: "Channel algebra of the two-vortex interaction",
  tags: ["vortex", "channel", "hecke", "spectral", "hopf"],
  lean: { ref: "qou:QOU.FluidDynamics.TwoVortexChannelAlgebra.braiding_sq",
    validation: "not_checked",
  },
  uses: [
    "prop:r-matrix-braiding-structure",
    "def:van-der-waals-hopf-channel",
  ],
  examples: ["rem:two-vortex-scattering-channels"],
});
