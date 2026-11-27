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
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` inhabits `QmnRecursiveMemoizedContext` over `degenerateMarkovTraceContext` with `chi = 0` and `cache_get = none`.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
  ],
});
