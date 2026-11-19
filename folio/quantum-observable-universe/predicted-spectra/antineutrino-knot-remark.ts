import { remark } from "../../schema/builders";

export default remark({
  label: "rem:antineutrino-knot-remark",
  title: "The antineutrino in $\\beta^-$ decay",
  interprets: "def:antineutrino-knot",
  tags: ["antineutrino", "unknot"],
  uses: [
    "def:antineutrino-knot",
    "def:neutrino-knot",
    "def:beta-decay-skein",
  ],
});
