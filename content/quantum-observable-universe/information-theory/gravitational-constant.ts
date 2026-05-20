import { definition } from "../../schema/builders";

export default definition({
  label: "def:gravitational-constant",
  title: "Gravitational constant from information geometry",
  tags: [
    "gravitational-constant",
    "information-theory",
    "jacobson",
    "entropy-area",
    "speed-of-light",
    "emergent-gravity",
  ],
  lean: { ref: "qou:QOU.Information.gravitationalConstant",
    validation: "not_checked",
  },
  uses: [
    "def:information-speed-of-light",
    "rem:gr-substrate-geometry",
    "rem:c-substrate-via-levi",
  ],
  cites: [
    "jacobson1995",
    "bekenstein1981",
    "mcmullen1998",
  ],
});
