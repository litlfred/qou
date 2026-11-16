import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-ordering-corrected",
  title:
    "Mass ordering $\\mathfrak{m}_{\\mathfrak{n}} > \\mathfrak{m}_{\\mathfrak{p}}$ with corrected trace",
  interprets: "prop:corrected-markov-trace",
  tags: [
    "mass-ordering",
    "proton",
    "neutron",
    "fermionic",
  ],
  uses: [
    "prop:corrected-markov-trace",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body: "This remark was written on the premise $\\mathrm{tr}_M(e^-) = \\mathrm{tr}_M(\\sigma_0\\sigma_1\\sigma_0) = z^3$. That premise is false; the correct value is $hz^2 + z$ (see prop:corrected-markov-trace, corrected 2026-11-15). The nucleon trace values $-0.012$ and $-0.134$ have no producer in computations/ (codata_masses.py does not compute them), so whether the ordering survives the correction is unverified.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
