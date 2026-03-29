import { definition } from "../../schema/builders";

export default definition({
  label: "def:reeb-gauge-group",
  title: "The Reeb gauge group $U_1(R)$",
  tags: [
    "gauge-group",
    "reeb",
    "U1",
    "maximal-torus",
    "connection",
    "adjoint",
    "commutative",
  ],
  lean: {
    decl: "QOU.ReebGaugeGroup",
    validation: "not_checked",
  },
  uses: ["def:contact-affine-chart"],
});
