import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:root-of-unity-truncation",
  label: "rem:root-of-unity-truncation-interpretation",
  title: "Vortex-core aspect ratio versus contact twist at collision",
  uses: ["conj:root-of-unity-truncation", "prop:core-levi-form"],
});
