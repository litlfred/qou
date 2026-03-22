import { chapter, section } from "../../schema/builders";
export default chapter({
  number: 7,
  title: "Interpretations and Speculations",
  label: "chap:interpretations",
  sections: [
    section({
      title: "Introduction",
      label: "sec:interpretations-intro",
      blocks: ["ch10-intro"],
    }),
  ],
});
