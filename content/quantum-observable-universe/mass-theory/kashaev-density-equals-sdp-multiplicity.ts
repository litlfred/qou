import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-density-equals-sdp-multiplicity",
  title:
    "Kashaev density prefactor equals joint-tower SDP Wedderburn multiplicity ($\\rho_F = \\nu_{\\mathrm{SDP}}$)",
  lean: {
    ref: "qou:QOU.Kashaev.KashaevDensityEqualsSdpMultiplicity",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/mass_table_ppb.py",
    witness: "folio-assistant/computations/mass-table-ppb.witness.json",
    status: "verified",
  },
  uses: [
    "rem:kashaev-as-archimedean-realization",
    "prop:atom-knot-mass-derivation",
    "def:archimedean-realization-functor",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "iwahori1964",
    "wenzl1988",
  ],
  tags: [
    "tier:E",
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
