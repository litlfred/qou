import { remark } from "../../schema/builders";

export default remark({
  label: "rem:standard-part-classical-limit",
  title: "Standard-part as the exact classical-limit substitute",
  tags: [
    "surreal-numbers",
    "standard-part",
    "classical-limit",
    "jackson-derivative",
    "archimedean",
  ],
  interprets: "def:standard-part-functor",
  uses: ["def:birthday-grading"],
});
