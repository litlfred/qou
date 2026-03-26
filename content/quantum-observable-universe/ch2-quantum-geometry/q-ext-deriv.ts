import { example } from "../../schema/builders";

export default example({
  label: "ex:q-ext-deriv",
  title: "$q$-Deformed exterior derivative",
  tags: ["exterior-derivative", "archimedean"],
  lean: {
    decl: "QOU.qExtDeriv",
    validation: "leanok",
  },
  uses: ["def:categorical-q-ext-deriv", "ex:reeb-decomposition", "prop:categorical-dq-squared"],
});
