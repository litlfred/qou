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
      body: "**primary conjecture (SHARPENED after a proof attempt).** Classical skeleton (Bring–Jerrard root variety, $(2,3,5)\\cong A_5$, Klein's icosahedral solution) is established. The proof attempt **refuted the naive assembly**: the corpus's canonical generators $\\alpha=\\exp(\\tfrac{2\\pi}{3}e_3)$, $\\beta=\\exp(\\pi e_1)$ satisfy the established dihedral relation $\\beta\\alpha\\beta^{-1}=\\alpha^{-1}$, hence $(\\beta\\alpha)^2=1$ — the $(2,3,2)$ trefoil $S_3$, NOT $(2,3,5)$ (Lean `dihedral_two_cycle_sq`, sorry-free; numerically cross-checked $\\mathrm{tr}\\,R_\\beta R_\\alpha=-1$). So the bridge needs icosahedral-angle generators distinct from the trefoil pair. Open content (sharpened): existence of that distinct icosahedral $A_5$ on $\\mathbb{P}(V)$ (Klein's resolvent) with $(c_2 c_3)^5=1$, and $\\mathbb{P}(V)/A_5\\cong S^2(2,3,5)$ = keystone Seifert base. Lean §3b-tax primary-conjecture class (content-bearing, no instance); authored without a toolchain — **not yet `lean`-direct verified**.",
    },
  ],
});
