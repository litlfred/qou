import { proposition } from "../../schema/builders";

/**
 * ILP derivation of the covalent bond operator.
 *
 * The covalent bond is the minimum-crossing knot operator with
 * positive binding energy between two atoms.
 */
export default proposition({
  label: "prop:ilp-covalent-bond",
  lean: { ref: "qou:QOU.Molecular.covalent_bond_is_ilp_optimal" },
  title: "The covalent bond is the inverse trefoil $T_{2,3}^{-1}$",
  tags: [
    "covalent-bond",
    "inverse-trefoil",
    "ILP",
    "knot-operator",
    "molecular",
    "zero-parameters",
  ],
  computation: {
    engine: "python",
    script: "computations/molecular_experimental_refs.py",
    witness: [
      "computations/molecular-experimental-refs.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The only `ℝ` in `ilp-covalent-bond.lean` is the **H₂ binding energy " +
        "in eV**: `h2_binding_energy (q : ℝ) (hq : q > 1) : ∃ E : ℝ, E > 0 ∧ " +
        "E < 5.0`, whose `5.0` bound brackets the 4.48 eV prediction recorded " +
        "in the adjacent comment. A measured energy is the §7c \"experimental " +
        "value → `ℝ`\" row, and the substrate hypothesis `q > 1` is an " +
        "archimedean ordering, so the `ℝ` is forced by the statement rather " +
        "than chosen. (That the energy bound is an `axiom` rather than a " +
        "theorem is a separate §1a matter.)",
    },
  ],
});
