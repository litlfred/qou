import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:braid-twist-flip",
  label: "rem:holonomy-trefoil",
  title: "Holonomy generators and the trefoil",
  computation: {
    engine: "python",
    script: "computations/probes/colour_mu_bar_monodromy_probe.py",
    witness:
      "computations/probes/colour-mu-bar-monodromy-probe.witness.json",
    status: "verified",
  },
  tags: ["holonomy", "trefoil", "braid-group", "branched-cover"],
  uses: ["def:braid-twist-flip", "def:su2-generators"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/holonomy-trefoil-0.svg", blockIndex: 0, hash: "6771329130f7" },
  ],

});
