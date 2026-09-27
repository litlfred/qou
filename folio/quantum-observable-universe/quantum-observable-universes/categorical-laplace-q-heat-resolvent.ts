import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-laplace-q-heat-resolvent",
  interprets: "def:categorical-laplace",
  title: "The categorical Laplace transform and the $q$-heat resolvent",
  tags: ["hopf-algebra", "laplace", "q-heat", "resolvent"],
  uses: [
    "def:categorical-laplace",
    "def:q-heat-equation",
    "def:q-resolvent",
  ],
});
