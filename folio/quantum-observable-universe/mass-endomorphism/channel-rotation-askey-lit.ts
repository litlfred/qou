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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We formalize this generically over a commutative ring $R$ equipped with a bar involution $\\sigma$ and a formal rotation element $\\iota$ satisfying $\\iota^2 = -1$. The Lean declaration `rotation_step` (sibling to [Complex-volume unification](#conj:binding-qbeta-complex-volume)) encodes this: a sequence\n\nis proved as `eigencolumn_eq_overlap`.\n\nis axiomatized by the conjecture class `ChannelLeonardDuality`." },
  ],
});
