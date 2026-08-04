import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ew-slot-far-commutation-obstruction",
  title:
    "The far-commuting slots cannot carry $\\mathrm{SU}(2)_L$: non-abelianness is localized to the inter-slot linking",
  lean: {
    ref: "qou:QOU.ParticleInteractions.su2L_nonabelianness_not_in_slots",
    validation: "not_checked",
  },
  // NB: cites conj:categorical-linking-operation and the group-assignment
  // postulate only in PROSE (they are where the non-abelianness must instead
  // live) — this proposition does NOT logically depend on them, so they are
  // NOT in uses[] (no conjectural propagation). The result is pure algebra:
  // a proved structural exclusion over a generic ring.
  uses: [
    "thm:hoefsmit-ew-cell-content",
    "thm:ew-triplet-charge-spin-from-involution",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Far-commutation obstruction (Task 1, primary target of PR #3397). The " +
        "three disjoint-pair slots σ₁,σ₃,σ₅ (strands 1-2|3-4|5-6) far-commute " +
        "(|i−j|≥2), so the submonoid they generate is mutually abelian " +
        "(`slotSubmonoid_commutative`, sorry-free via the centralizer submonoid). " +
        "su(2)_L is non-abelian (adjoint triplet, nonzero Lie bracket); a nonzero " +
        "bracket forbids commutation (`nonabelian_bracket_forbids_commute`). Hence " +
        "the capstone `su2L_nonabelianness_not_in_slots`: the two su(2)_L adjoint " +
        "generators cannot BOTH be realized in the slot subalgebra — proved as a " +
        "structural exclusion, AGENTS.md case (b), the invariant being commutator " +
        "vanishing on a commutative subalgebra. This NARROWS `EWGroupAssignment` " +
        "(thm:ew-triplet-charge-spin-from-involution): the non-abelian gauge " +
        "structure is localized to the inter-slot linking — σ₂,σ₄ (which do NOT " +
        "far-commute, `interSlot_not_farApart`) and the categorical linking " +
        "operation Lk_R (conj:categorical-linking-operation). Base ring generic " +
        "(no ℝ, §7c). lean-direct exit 0 on lake-cache/qou-v4-24-0.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Task 2 (which vector slot is the neutral Cartan W³→Z) is NOT closed by " +
        "this obstruction. The obstruction says non-abelianness is not among the " +
        "slots; it does not by itself pick which slot is Cartan. That selection " +
        "remains the open EWGroupAssignment input (the (W³,B)→(Z,γ) Weinberg " +
        "mixing data, conj:weinberg-angle-categorical). What IS now sharper: the " +
        "Cartan/root split is a property of the LINKING (bracket-carrying) data, " +
        "not of the individual far-commuting slots — consistent with the prior " +
        "which_slot_is_W_free result that no single-slot topological invariant " +
        "forces the label. See docs/audits/2026-07-05-ew-group-assignment-attack.md.",
    },
  ],
  tags: [
    "electroweak",
    "su2",
    "far-commutation",
    "obstruction",
    "non-abelian",
    "categorical-linking",
    "weak-sector",
  ],
});
