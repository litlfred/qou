import { table } from "../../schema/builders";
export default table({
  label: "tbl:polynomial-bar-involution-table-data",
  title: "Data table from prop:polynomial-bar-involution",
  uses: ["prop:polynomial-bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | Theorem | Statement |\n|---|---|\n| `barPoly_X` | $\\overline X = -X$ |\n| `barPoly_neg_X` | $\\overline{(-X)} = X$ |\n| `barPoly_C c` | $\\overline{c} = c$ for $c \\in R$ |\n| `barPoly_add` | $\\overline{p+q} = \\overline p + \\overline q$ |\n| `barPoly_mul` | $\\overline{p\\cdot q} = \\overline p \\cdot \\overline q$ |\n| `barPoly_one` | $\\overline 1 = 1$ |\n| `barPoly_zero` | $\\overline 0 = 0$ |\n| `barPoly_involutive` | $\\overline{\\overline p} = p$ |\n| `barPoly_X_pow_two` | $\\overline{X^2} = X^2$ (concrete bar-symmetry) |\n| `barPoly_X_pow n` | $\\overline{X^n} = (-1)^n \\cdot X^n$ |" },
  ],
});
