import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-reeb-gauge-group",
  title: "The Reeb gauge group $U_1(R)$",
  tags: [
    "glossary",
    "gauge-group",
    "reeb",
    "U1",
    "maximal-torus",
    "connection",
    "adjoint",
    "commutative",
  ],
  lean: { ref: "qou:QOU.ReebGaugeGroup",
    validation: "not_checked",
  },
  uses: ["def:contact-affine-chart"],
  defines: ["reeb-gauge-group"],
});
