import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spectrahedral-phase-collapse-prior-art",
  title:
    "Prior art for spectrahedral rank-drop boundaries, moment hierarchies, and conic phase transitions",
  interprets: "prop:spectrahedral-phase-collapse",
  uses: ["prop:spectrahedral-phase-collapse"],
  cites: [
    "gouveia-parrilo-thomas2010",
    "vinzant2014",
    "laurent2009",
    "bachoc-vallentin2008",
    "zauner-verstraete2016",
    "elshowk2012",
    "simmons-duffin2015",
    "kazakov-zheng2023",
    "donoho-tanner2009",
    "amelunxen-lotz-mccoy-tropp2014",
  ],
  tags: [
    "spectrahedron",
    "sdp",
    "phase-collapse",
    "prior-art",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Positioned strictly within the Convention-C vs Convention-D scope established in `prop:spectrahedral-phase-collapse`: under Convention D, `det G_D = 0` identically across all `q` via the three-strand `q`-antisymmetriser radical, whereas facial rank-drop and dual-certificate methods (`QOU.MathlibInfra.SymmetryReducedDualCertificate`) govern boundary selection on the quotient cone.",
    },
  ],
});
