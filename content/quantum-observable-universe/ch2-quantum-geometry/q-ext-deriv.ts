import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-q-ext-deriv",
  label: "ex:q-ext-deriv",
  title: "$q$-Deformed exterior derivative",
  tags: ["exterior-derivative", "archimedean"],
  lean: {
    decl: "QOU.qExtDeriv",
    validation: "leanok",
  },
  uses: [
    "ex:reeb-decomposition",
    "prop:categorical-dq-squared",
  ],
});
