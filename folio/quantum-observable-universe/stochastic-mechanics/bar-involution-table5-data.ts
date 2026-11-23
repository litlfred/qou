import { table } from "../../schema/builders";
export default table({
  label: "tbl:bar-involution-table5-data",
  title: "Data table 5 from def:bar-involution",
  uses: ["def:bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | Combination | Result | Lean theorem |\n|---|---|---|\n| sym + sym | sym | `IsBarSymmetric.add` |\n| sym $\\times$ sym | sym | `IsBarSymmetric.mul` |\n| anti + anti | anti | `IsBarAntiSymmetric.add` |\n| **anti $\\times$ anti** | **sym** | `IsBarSymmetric.of_mul_antisym` |\n| sym $\\times$ anti | anti | `IsBarAntiSymmetric.of_sym_mul` |\n| $-$sym | sym | `IsBarSymmetric.neg` |\n| $-$anti | anti | `IsBarAntiSymmetric.neg` |\n| $h^{2n}$ (h anti) | sym | `IsBarAntiSymmetric.pow_two_mul` |\n| $h^{2n+1}$ (h anti) | anti | `IsBarAntiSymmetric.pow_two_mul_add_one` |\n| $\\mathrm{bar}(-x) = -\\mathrm{bar}(x)$ | identity | `bar_neg` |" },
  ],
});
