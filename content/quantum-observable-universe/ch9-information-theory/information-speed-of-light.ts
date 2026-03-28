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
  lean: {
    decl: "QOU.Information.speedOfLight",
    validation: "not_checked",
  },
  uses: [
    "def:operational-entropy",
    "def:planck-time",
    "prop:reeb-operations-per-planck",
    "def:light-cone-affine",
  ],
});
