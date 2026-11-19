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
    script: "computations/mass_table_ppb.py",
    witness: "computations/mass-table-ppb.witness.json",
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
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/probes/he4_nu_sdp_binding_arbiter.py.",
    },
    {
      kind: "status",
      date: "2026-09-05",
      body:
        "**Status of the density prefactor** (migrated out of the block prose per §4d — " +
        "it tracks how the rule got here, not what the block claims). The canonical " +
        "formalism previously carried the density rule $\\rho_F \\in \\{1, 2\\}$ as " +
        "*\"pending formal justification\"*, with no derivation behind it. With the " +
        "conditional adoption, $\\rho_F$ is: (1) **named canonically** (`nu_sdp` in the " +
        "code), connecting to the existing $\\nu_{\\mathrm{SDP}}$ notation in " +
        "`prop:atom-knot-mass-derivation`; (2) **identified as a partition-algebra " +
        "count** (MacMahon type); (3) **conditional on a class** that the full SDP solver " +
        "will eventually inhabit — replacing the open-ended \"pending formal " +
        "justification\" with an explicit conjectural dependency.",
    },
    {
      kind: "caveat",
      date: "2026-09-05",
      body:
        "**The evidence base is two points, not three.** The ${}^{2}\\mathrm{H}$ row was " +
        "removed from the evidence table on an owner ruling. It assigned the deuteron the " +
        "census knot $6_2$; the canonical deuteron knot is the braid closure with " +
        "$\\mathrm{Vol} = 0$, and since the identity's formula is " +
        "$B_{\\mathrm{pred}} = \\rho_F\\,\\mathfrak{m}_e\\,\\mathrm{Vol}_{\\mathrm{hyp}}$, " +
        "at $\\mathrm{Vol} = 0$ it returns $0$ for **every** $\\rho_F$ — so that row could " +
        "not constrain the prefactor even in principle. Note what this costs: the " +
        "surviving two points both read $2$, so the *variation* in the advertised " +
        "$1, 2, 2$ pattern came entirely from the row now removed. Read alongside the " +
        "separate finding that six operational definitions of $\\nu_{\\mathrm{SDP}}$ were " +
        "computed and none reproduces the legacy triple, the committed values carrying " +
        "methodology `\"manual-historical-volume-match\"`.",
    },
  ],
});
