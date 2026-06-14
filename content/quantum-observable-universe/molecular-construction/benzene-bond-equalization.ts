import { remark } from "../../schema/builders";

/**
 * Benzene bond equalization: all C-C bonds equal from threading link symmetry.
 */
export default remark({
  label: "rem:benzene-bond-equalization",
  title: "Bond equalization from $D_6$ symmetry of $T(2,6)$",
  interprets: "prop:benzene-threading-emergence",
  uses: ["def:benzene-molecular-braid"],
  tags: ["benzene", "bond-equalization", "D6", "aromatic", "bond-order"],
  computation: {
    engine: "python",
    witness: [
      "folio-assistant/computations/molecular-experimental-refs.witness.json"
    ],
    status: "experimental",
  },
});
