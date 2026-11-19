import { example } from "../../schema/builders";

export default example({
  label: "ex:per-nucleon-channel-decomposition",
  title: "Per-nucleon channel data for proton and neutron",
  interprets: "def:per-nucleon-channel-decomposition",
  uses: [
    "def:per-nucleon-channel-decomposition",
    "def:typed-crossing-operator",
  ],
});
