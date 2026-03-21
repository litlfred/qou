import { chapter, section } from "../../schema/builders";
export default chapter({
  number: 10,
  title: "Interpretations",
  label: "chap:interpretations",
  sections: [
    section({
      title: "Introduction",
      label: "sec:interpretations-intro",
      blocks: ["ch10-intro"],
    }),
  ],
});
