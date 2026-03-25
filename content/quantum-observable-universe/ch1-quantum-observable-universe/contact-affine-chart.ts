import { definition } from "../../schema/builders";

export default definition({
  label: "def:contact-affine-chart",
  title: "Contact affine chart on $\\mathbb{P}(V)$",
  tags: ["projective", "affine-chart", "reeb", "contact"],
  lean: {
    decl: "QOU.ContactAffineChart",
    validation: "not_checked",
  },
  uses: [
    "def:projective-line-object",
    "def:categorical-reeb",
    "ex:reeb-decomposition",
    "def:weight-decomposition",
  ],
});
