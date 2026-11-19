import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:binding-qbeta-complex-volume",
  label: "rem:channel-rotation-askey-lit",
  title:
    "The channel rotation in the Askey scheme: same eigenfunctions rotated, different measures",
  lean: {
    ref: "qou:QOU.MassEndomorphism.rotation_step",
    validation: "not_checked",
  },
  uses: [
    "conj:binding-qbeta-complex-volume",
    "prop:q-gaussian-obstruction-at-q0",
  ],
  cites: [
    "terashima-yamazaki2013",
    "askey1989qhermite",
    "ismail-masson1994",
    "zhedanov1991",
    "terwilliger2001",
    "ponsot-teschner2001",
    "creutzig-milas2014",
    "garoufalidis-zagier-2024",
    "neumann-zagier1985",
  ],
  tags: [
    "complex-volume",
    "askey-scheme",
    "q-hermite",
    "bar-parity",
    "leonard-pair",
    "modular-double",
    "fibre-level",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Lean declarations (`QOU.MassEndomorphism`): `rotation_step`, `eigencolumn_eq_overlap`, and conjecture class `ChannelLeonardDuality`.",
    },
  ],
});
