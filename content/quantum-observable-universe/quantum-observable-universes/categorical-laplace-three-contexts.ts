import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-laplace-three-contexts",
  interprets: "def:categorical-laplace",
  title: "The categorical Laplace transform across $\\mathbb{F}_p$, $\\mathbb{Q}_p$, $\\mathbb{C}_p$",
  tags: ["hopf-algebra", "grouplike", "laplace", "p-adic", "finite-field"],
  uses: [
    "def:categorical-laplace",
    "rem:q-exp-finite-field-obstruction",
    "rem:q-exp-p-adic",
  ],
});
