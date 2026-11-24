import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quaternionic-spectral-resolvents",
  label: "rem:quaternionic-spectral-resolvents-remark",
  title: "The balanced state and the jet-shell embedding",
  uses: ["def:quaternionic-spectral-resolvents", "rem:jet-shell"],
});
