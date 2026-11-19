import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-angular-momentum",
  label: "rem:q-angular-momentum-interpretation",
  title: "Jones polynomial connection, building block values, and nuclear $q$-angular momentum",
  tags: [
    "angular-momentum",
    "jones-polynomial",
    "nuclear",
    "spin",
    "q-deformed",
  ],
  uses: ["def:q-angular-momentum"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py",
    witness: "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
    status: "verified",
  },
});
