import { remark } from "../../schema/builders";

export default remark({
  label: "rem:time-reversal-energy-barrier",
  title: "Time reversal requires infinite energy in the observable sector",
  interprets: "prop:antiparticle-crossing-reversal",
  uses: ["rem:pair-creation-energy"],
  tags: [
    "time-reversal", "energy-barrier", "topological-protection",
    "electron", "proton", "neutron", "feynman-stueckelberg",
  ],
});
