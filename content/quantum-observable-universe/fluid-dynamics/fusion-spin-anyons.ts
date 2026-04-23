import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fusion-spin-anyons",
  title: "Fusion rules, fractional spin, and anyons",
  tags: ["fusion", "anyons", "ribbon-twist", "fractional-spin"],
  uses: [
    "def:observable-mtc",
    "rem:berry-vortex-moduli",
  ],
  interprets: "def:observable-mtc",
  cites: ["kitaev2006"],
});
