import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-vertex-left-projector",
  title: "The weak vertex insertion is proportional to the left projector",
  lean: {
    ref: "qou:QOU.QuarkState.WeakVertexLeftProjector.weakVertex_sub_letter",
    validation: "not_checked",
  },
  uses: ["rem:force-knot-identification"],
  cites: ["jones1987"],
  tags: ["weak", "chirality", "hecke-letter", "skein", "left-line", "scope-a"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body:
        "Owner decision D-H3 (bean `qou-hlx7`, 2026-11-15): record \"the weak vertex is " +
        "proportional to the left projector\" and try to derive it. The one-crossing form was " +
        "derived, so on the owner's choice it is recorded as a proposition, together with the " +
        "exact negative for the weak knot T(3,5). Lean: " +
        "`QOU/QuarkState/WeakVertexLeftProjector.lean` (`weakVertex_sub_letter`, " +
        "`weakVertex_eq_split`, `one_sided_iff_smul_leftLine`, `skein_dominant_root`), on top " +
        "of `LeftLineDefinition.lean`. Probe: `computations/probes/weak_knot_left_line_split_probe.py`. " +
        "Audit: `docs/audits/2026-11-15-weak-vertex-left-projector.md`. The identification of " +
        "the vertex with the physical weak coupling is not made (scope (a)).",
    },
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "Provenance (owner question \"what chose corpus vertex?\", bean `qou-g0jn`): W = " +
        "(one-sided-flip ansatz, `OneSidedWeakVertex.lean`) + (owner definition of left, " +
        "`LeftLineDefinition.lean`) + uniqueness (`eq_of_eigen_action`). W_L = q⁻¹J and " +
        "W_R = qJ (`oneSidedL_eq`, `oneSidedR_eq`). Emission probes: under the reading " +
        "'emission = W − letter' the mirror emits more on the γγ nucleon word V³ (#7981, " +
        "#7984); under the reading 'emission = Ř coefficient' the corpus/mirror ratio is " +
        "q⁻⁴ for every word tested (`emission_reading_chirality_probe.py`), i.e. only the " +
        "overall scale q² between the two one-sided elements.",
    },
  ],
});
