import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:discrete-vortex-spectrum",
  label: "rem:bec-vortex-data",
  title: "Bose--Einstein condensate vortex data and $q$-deformed predictions",
  uses: ["prop:discrete-vortex-spectrum"],
  cites: [
    "madison2000",
    "abo-shaeer2001",
    "bretin2003",
    "gauthier2019",
    "fetter2009",
    "navon2021",
  ],
  tags: ["vortex", "BEC", "observation", "quantization"],
});
