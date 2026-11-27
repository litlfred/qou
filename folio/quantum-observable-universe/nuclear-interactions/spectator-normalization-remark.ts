import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spectator-normalization-remark",
  title: "Origin and sign of the spectator normalization",
  interprets: "def:spectator-normalization",
  uses: [
    "def:spectator-normalization",
    "def:per-nucleon-channel-decomposition",
  ],
});
