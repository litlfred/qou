import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dilogarithm-properties",
  interprets: "def:q-dilogarithm",
  title: "$\\mathrm{Li}_2^q$ as the categorical braiding potential (R-matrix)",
  tags: ["hopf-algebra", "dilogarithm", "associator", "r-matrix"],
  uses: [
    "def:q-dilogarithm",
  ],
  cites: [
    "faddeev_kashaev1994",
    "faddeev1994",
    "faddeev1995",
    "andersen-kashaev2014",
    "dusenbury2025",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Beans qou-1buz and qou-exr5: separated the compact q-Pochhammer dilogarithm (`faddeev_kashaev1994`, `faddeev1994`) from Faddeev's noncompact modular-double dilogarithm Phi_b (`faddeev1995`), and anchored the primary Andersen-Kashaev state-integral TQFT (`andersen-kashaev2014`) alongside Dusenbury's expository thesis (`dusenbury2025`) without touching `q-dilogarithm-pentagon-associator` (fenced on #9178).",
    },
  ],
});
