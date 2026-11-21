import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:discrete-vortex-spectrum",
  label: "rem:bec-vortex-data",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): The results below demonstrate that the $q \\to 1$ limit of the $\\mathrm{SU}_q(2)$ vortex spectrum ([Proposition](#prop:discrete-vortex-spectrum)) correctly reproduces observed BEC phenomenology." },
  ],
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
