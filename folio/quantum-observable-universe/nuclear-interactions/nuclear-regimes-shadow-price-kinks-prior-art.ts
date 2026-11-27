import { remark } from "../../schema/builders";

export default remark({
  label: "rem:nuclear-regimes-shadow-price-kinks-prior-art",
  title:
    "Prior art for toric chamber flips, magic-shell shadow-price kinks, and finite-nucleon phase walls",
  interprets: "prop:nuclear-operator-regimes",
  uses: [
    "prop:nuclear-operator-regimes",
    "prop:nuclear-chamber-groebner-basis",
  ],
  cites: [
    "bokut2001",
    "kangleeleeoh2002",
    "graver1975",
    "billera-gelfand-sturmfels1990",
    "conti-traverso1991",
    "sturmfels-thomas1997",
    "mayer1949",
    "haxel-jensen-suess1949",
    "perdew-parr-levy-balduz1982",
    "verstichel-vanaggelen2009",
    "zauner-verstraete2016",
    "viro2001",
    "lee-yang1952",
  ],
  tags: [
    "nuclear-binding",
    "magic-numbers",
    "shadow-price",
    "groebner-fan",
    "prior-art",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Backed by `QOU.MathlibInfra.piecewise_linear_concave_of_parametric_lp`, `piecewise_linear_kink_shadow_price_jump`, `exists_chamber_neighborhood_kink_jump`, and `graver_test_set_certifies_global_ip_min` in `folio/quantum-observable-universe/lean/QOU/MathlibInfra/SymmetryReducedDualCertificate.lean`, together with `NuclearChamberGS.lean`.",
    },
  ],
});
