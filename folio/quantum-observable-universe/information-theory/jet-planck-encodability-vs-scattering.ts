import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:jet-planck-encodability-vs-scattering",
  title: "Encodability versus scattering onset",
  tags: [
    "jet-bundle",
    "planck-time",
    "scattering",
    "encodability",
    "crossing-number",
    "virtual-particles",
    "information-theory",
  ],
  uses: [
    "rem:jet-planck-particle-spectrum",
    "rem:virtual-particles-exceptional-divisor",
  ],
});
