import { definition } from "../../schema/builders";

export default definition({
  label: "def:information-speed-of-light",
  title: "Speed of light as Lieb--Robinson velocity",
  tags: [
    "speed-of-light",
    "information-theory",
    "lieb-robinson",
    "causal-structure",
    "q-connection",
  ],
  lean: { ref: "qou:QOU.Information.speedOfLight",
    validation: "not_checked",
  },
  uses: [
    "ex:q-connection",
    "def:operational-entropy",
    "rem:light-cone-affine",
  ],
});
