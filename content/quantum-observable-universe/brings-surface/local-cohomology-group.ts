import { definition } from "../../schema/builders";

export default definition({
  label: "def:local-cohomology-group",
  title: "Local cohomology at the unit defect",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.LocalCohomologyGroup",
    validation: "not_checked",
  },
  uses: ["def:maximal-ideal-defect"],
  tags: ["local-cohomology", "defect", "H1", "derived-functor"],
  cites: ["yekutieli2015",
    "yekutieli2010",
  ],
});
