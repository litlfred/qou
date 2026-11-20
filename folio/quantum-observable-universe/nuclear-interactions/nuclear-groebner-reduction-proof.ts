import { proof } from "../../schema/builders";

export default proof({
  label: "prf:nuclear-groebner-reduction",
  title: "Proof of nuclear groebner reduction",
  uses: ["prop:nuclear-groebner-reduction", "def:hecke-normal-form"],
  cites: ["bokut2001", "bergman1978"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Lean names relocated from the prose (voice drain, qou-d4kh). The failure of the three defining families at A = 4 is `NotAGSBasis.hecke_not_gs_basis_four`. The completed system is a GS basis for every A: `heckeCompleted_isGrobnerShirshovBasis`. Termination is `reduction_well_founded` (#8582). The Diamond Lemma is `Diamond.reductionUnique` (#8612). It replaces the former `local_confluence` axiom, which was inconsistent, and concludes uniqueness up to `CoeffEq`. The block's Lean sibling states existence of a reduced form only (`nuclear_groebner_reduction`)." },
  ],
});
