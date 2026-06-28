import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:klein-bring-icosahedral-bridge",
  lean: {
    ref: "qou:QOU.KleinBringBridge.KleinBringIcosahedralBridge",
    validation: "leanok",
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
      body: "**primary conjecture — group-theoretic core now DISCHARGED; sole residual = keystone-base quotient.** (1) Naive assembly REFUTED: canonical $\\alpha=\\exp(\\tfrac{2\\pi}{3}e_3)$, $\\beta=\\exp(\\pi e_1)$ obey $\\beta\\alpha\\beta^{-1}=\\alpha^{-1}\\Rightarrow(\\beta\\alpha)^2=1$ — the $(2,3,2)$ trefoil, not $(2,3,5)$ (Lean `dihedral_two_cycle_sq`, sorry-free). (2) Surviving core CONSTRUCTED: Klein's $S=\\zeta_5$ pentad (order 5) + $T$ icosahedral 2-fold give $c_2=T$, $c_3=TS$ with $c_2c_3=S$ order exactly 5, $\\langle S,T\\rangle\\cong A_5$ — icosahedral-angle generators with product = the corpus $\\zeta_5$ pentad (witness `scripts/keystone_klein_icosahedral_construction.py`; abstract realizability Lean-proved sorry-free `icosahedral_235_realizable`). (3) Orbifold target ESTABLISHED (sorry-free): cone orders $60/\\{12,20,30\\}=\\{5,3,2\\}$, $\\chi_{\\mathrm{orb}}=1/30=2/60$ ⇒ $\\mathbb{P}(V)/A_5=S^2(2,3,5)$ = Seifert base of $S^3/2I$ [klein1888]. (4) GROUP CANONICITY established: $\\langle\\zeta_5\\,\\mathrm{pentad},\\,\\mathrm{trefoil}\\rangle=A_5$ (both even — `pentad_even`/`trefoil_even`); EM involution is parity-ODD (`em_involution_odd`), the chirality coset — explains the dihedral failure; no generator imposed. (5) MÖBIUS REALIZATION explicit: Klein forms $f_{12},H_{20},T_{30}$ with syzygy $T^2+H^3=1728f^5$ (`klein_syzygy`), pentad-anchored; the icosahedral equation $I=H^3/1728f^5$ is the quotient map $\\mathbb{P}(V)\\to S^2(2,3,5)$, branch $(\\infty,0,1)$ cone orders $(5,3,2)$. (6) SOLE residual sliver: the spectral identification $\\eta\\leftrightarrow w$ (corpus trefoil acts on spectral $\\eta$, pentad on base $z$; Klein's resolvent must identify them) — Lean fields `proj_orbit_constant`/`proj_separates_orbits`, no instance. Scope: V_λ/geometry side — does NOT produce the Hecke-dual $W_\\lambda$. **`lean`-direct VERIFIED sorry-free** (Lean 4.24.0, exit 0; the degree-60 `klein_syzygy` `ring` proof compiles in ~4 s); also cross-checked in Python.",
    },
  ],
});
