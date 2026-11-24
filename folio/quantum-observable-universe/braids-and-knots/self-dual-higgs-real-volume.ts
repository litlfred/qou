import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:self-dual-higgs-real-volume",
  title:
    "The self-dual Higgs ($4_1$) has a real complex volume ($\\mathrm{CS}=0$)",
  cites: [
    "rolfsen",
    "witten2011",
    "neumann-zagier1985",
    "neumann-reid",
    "nguyen-tran-2021",
    "koelink-stokman-2003",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  lean: {
    ref: "qou:QOU.Knot.SelfDuality.higgs_complex_volume_real",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-njry (and Finding F6 in `docs/audits/2026-11-21-expo-cite-xcheck-findings.md`): `rolfsen` and `witten2011` (§5.3) source that 4₁ is amphichiral, whereas `neumann-reid` (§3.2, Prop. 3.4) is cited strictly for the necessary arithmetic consequence that an amphicheiral hyperbolic orbifold has conjugation-closed trace field and invariant quaternion algebra.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "OWNER RULING (2026-07-05) — 'Higgs' HERE means the mass-generation " +
        "MECHANISM / muon scale, NOT the 125-GeV Higgs boson. The self-dual " +
        "figure-eight 4₁ with real Neumann–Zagier complex volume is the mass " +
        "mechanism motif (m_μ/m_e = Vol(4₁)/ℏ_q²). The Higgs BOSON H is a " +
        "distinct object: the electroweak-slot link T(2,8) = the A₊ (bar-even, " +
        "scalar) part of the Hoefsmit slot σ₅⁸ (its A₋ bar-odd part being the " +
        "U(1)_Y gauge boson B) — see " +
        "`conj:electroweak-higgs-torus-link-triplet` + " +
        "`thm:ew-triplet-charge-spin-from-involution`. Do not conflate the " +
        "self-dual mass-mechanism 4₁ with the EW-slot Higgs boson T(2,8).",
    },
  ],
  tags: [
    "figure-eight",
    "higgs",
    "amphichiral",
    "self-duality",
    "complex-volume",
    "chern-simons",
    "aj-conjecture",
    "askey-wilson",
    "keystone",
  ],
});
