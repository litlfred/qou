import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:discrete-vortex-spectrum",
  label: "rem:bec-vortex-data",
  title: "Bose--Einstein condensate vortex data and $q$-deformed predictions",
  uses: [
    "rem:vortex-intensity-modes",
    "prop:discrete-vortex-spectrum",
    "def:substrate-parameter",
    "sec:planck-reynolds",
  ],
  cites: [
    "madison2000",
    "abo-shaeer2001",
    "bretin2003",
    "gauthier2019",
  ],
  tags: ["vortex", "BEC", "observation", "quantization"],
});
