import { chapter, section } from "../../schema/builders";

export default chapter({
  title: "Yang--Mills Mass Gap Framing",
  label: "chap:yang-mills-framing",
  sections: [
    section({
      title: "Crossing-energy positivity versus Wightman field theory",
      label: "sec:yang-mills-framing",
      blocks: [
        "yang-mills-framing-intro",
        "yang-mills-mass-gap",
        "yang-mills-mass-gap-table-data",
        "yang-mills-surreal-bound",
      ],
    }),
  ],
});
