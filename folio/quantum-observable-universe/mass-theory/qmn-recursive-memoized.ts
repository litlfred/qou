import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qmn-recursive-memoized",
  title:
    "Recursive memoised q-Murnaghan-Nakayama: $50\\times$ speedup + storage reduction for batch character evaluation",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.qmn_recursive_memoized",
    validation: "not_checked",
  },
  uses: ["prop:wenzl-qmn-synergy"],
  cites: ["halverson_ram_1998", "ram1991", "macdonald1995"],
  tags: [
    "q-murnaghan-nakayama",
    "recursive",
    "memoization",
    "compute-speedup",
    "storage-reduction",
    "atom-knot-id",
  ],
});
