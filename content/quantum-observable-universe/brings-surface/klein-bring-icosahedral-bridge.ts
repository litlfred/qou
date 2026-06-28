import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:klein-bring-icosahedral-bridge",
  lean: {
    ref: "qou:QOU.KleinBringBridge.KleinBringIcosahedralBridge",
    validation: "not_checked",
  },
  title:
    "Klein icosahedral–quintic bridge: the $(2,3,5)$ force symmetries assemble the Bring ED into the icosahedral $\\mathbb{P}^1$ with quotient $S^2(2,3,5)$",
  uses: [
    "def:brings-surface",
    "rem:brings-curve",
    "rem:braid-group-action",
    "rem:fivefold-symmetry",
    "def:hyperelliptic-quintic",
    "prop:bring-trefoil-cinquefoil-channel",
  ],
  cites: ["bring1786", "klein1888", "bolza1887"],
  tags: [
    "bring-curve",
    "icosahedral",
    "klein-quintic",
    "bring-radical",
    "triangle-2-3-5",
    "s5-so3-keystone",
    "poincare-sphere",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-28",
      body: "**primary conjecture — group-theoretic core now DISCHARGED; sole residual = keystone-base quotient.** (1) Naive assembly REFUTED: canonical $\\alpha=\\exp(\\tfrac{2\\pi}{3}e_3)$, $\\beta=\\exp(\\pi e_1)$ obey $\\beta\\alpha\\beta^{-1}=\\alpha^{-1}\\Rightarrow(\\beta\\alpha)^2=1$ — the $(2,3,2)$ trefoil, not $(2,3,5)$ (Lean `dihedral_two_cycle_sq`, sorry-free). (2) Surviving core CONSTRUCTED: Klein's $S=\\zeta_5$ pentad (order 5) + $T$ icosahedral 2-fold give $c_2=T$, $c_3=TS$ with $c_2c_3=S$ order exactly 5, $\\langle S,T\\rangle\\cong A_5$ — icosahedral-angle generators with product = the corpus $\\zeta_5$ pentad (witness `scripts/keystone_klein_icosahedral_construction.py`; abstract realizability Lean-proved sorry-free `icosahedral_235_realizable`). (3) SOLE residual open content: the orbifold identification $\\mathbb{P}(V)/A_5\\cong S^2(2,3,5)$ = keystone Seifert base of $S^3/2I$ (Lean class fields `proj_orbit_constant`/`proj_separates_orbits`, no instance). Authored without a toolchain — group/arith lemmas cross-checked in Python; **not yet `lean`-direct verified**.",
    },
  ],
});
