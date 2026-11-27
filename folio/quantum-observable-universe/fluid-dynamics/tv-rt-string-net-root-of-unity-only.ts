import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:root-of-unity-truncation",
  label: "rem:tv-rt-string-net-root-of-unity-only",
  lean: { ref: "qou:QOU.BringsSurface.RealQNotRootOfUnity.realGtOne_not_rootOfUnity" },
  title: "State-sum and string-net constructions apply only at a root of unity",
  uses: ["prop:root-of-unity-truncation", "def:substrate-parameter"],
  cites: ["turaev-virelizier2010", "balsam2010", "bruguieres-virelizier2008", "levin2005"],
  tags: ["root-of-unity", "turaev-viro", "reshetikhin-turaev", "string-net", "fusion-category", "scope"],
});
