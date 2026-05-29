import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:kashaev-density-equals-sdp-multiplicity",
  title:
    "Kashaev density prefactor equals joint-tower SDP Wedderburn multiplicity ($\\rho_F = \\nu_{\\mathrm{SDP}}$)",
  lean: {
    ref: "qou:QOU.Kashaev.DensityEqualsSDPMultiplicity",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/mass_table_ppb.py",
    witness: "folio-assistant/computations/mass-table-ppb.witness.json",
    status: "verified",
  },
  uses: [
    // The underlying Kashaev volume conjecture this refines:
    "prop:kashaev-volume-conjecture",
    "rem:kashaev-volume-density",
    "rem:kashaev-as-archimedean-realization",
    // The Wedderburn / joint-tower SDP infrastructure:
    "def:hecke-normal-form",
    // Algorithm step 3 of atom-knot-mass-derivation supplies ν_SDP:
    "prop:atom-knot-mass-derivation",
    // The wider categorical menu under which this falls:
    "def:archimedean-realization-functor",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "iwahori1964",
    "wenzl1988",
  ],
  tags: [
    "kashaev",
    "density",
    "sdp-multiplicity",
    "wedderburn",
    "rule-14-conditional",
    "macmahon-partition-algebra",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
