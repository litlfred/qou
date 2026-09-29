import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qou-obstruction-reduction",
  title:
    "Conditional on the Wigner axiom: the obstruction is the Euler characteristic of the base",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.qou_obstruction_reduction",
    validation: "not_checked",
  },
  uses: [
    "conj:wigner-axiom",
    "def:classical-limit-obstruction",
    "thm:qu-to-qou",
    "rem:three-euler-characteristics",
  ],
  tags: [
    "obstruction",
    "classical-limit",
    "hochschild-cohomology",
    "observability",
    "frobenius-duality",
    "euler-characteristic",
    "kummer",
  ],
  cites: ["yekutieli2010", "brown-zhang-2008", "feng-tsygan-1991", "hadfield-krahmer-2005", "weibel1994"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "**RESTATED as conditional on `conj:wigner-axiom` (owner selection C, 2026-09-15).** The former part (a) claimed `dim HH^2(U_q, Ad) = 1` as a theorem. Its proof (i) stated Van den Bergh duality as cohomology-to-dual-cohomology, untwisted, where Brown–Zhang's form is cohomology-to-homology with the Nakayama twist and the untwisted form fails at `q != 1` (dimension drop); (ii) counted \"the unique deformation direction `q`\" as an outer derivation, conflating `HH^1` with `HH^2`; and (iii) is contradicted at `q = 1` by Whitehead's lemma. The one-dimensionality is now the hypothesis (the Wigner axiom); (a) derives the integer from it by Poincaré–Hopf with no HKR step; (b) is unchanged in substance. **The Lean carrier `qou_obstruction_reduction.lean` predates this restatement**: its `INPUT` class fields (`vdb_duality`, `drinfeld_rigidity`, `trace_pairing`, `chern_character`) are the content of the Wigner axiom and it still carries 6 `sorry`; bringing it into line is bean `qou-6tdg`'s cheat-sheet pass. Analysis: `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.4.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The single `ℝ` here, `phi_1_image`, is only ever equated to an " +
        "integer cast (`phi_1_image = (chi_A : ℝ)`), so on its own content " +
        "this block would be a regenericisation candidate. It is **blocked by " +
        "an `extends` edge**: `QouObstructionReductionContext` is extended by " +
        "`CollatzContactBoundaryContext` in " +
        "`lean/QOU/AlgebraicSubstrate/collatz_contact_boundary.lean` and " +
        "consumed by four further library files, so parameterising it " +
        "rewrites downstream instance binders — the blast radius that blocked " +
        "`qmn_recursive_memoized`, and one of the affected files is currently " +
        "owned by another branch. Recorded here so the next agent does not " +
        "re-derive the diagnosis.",
    },
  ],
});
