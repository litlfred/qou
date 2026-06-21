import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-symmetric-three-layer-synthesis",
  lean: {
    ref: "qou:QOU.BraidKnot.BarSymmetricThreeLayerSynthesis",
    validation: "not_checked",
  },
  title:
    "Bar-symmetric three-layer synthesis: the symmetric $\\mathrm{Li}_2^q$ (series), the $\\cos(\\alpha - b\\hbar_q^2/2)$ factor at the $N{=}1$ rung (phase), and the per-$Z$ step gain $\\alpha_Z \\approx [3]_q^2\\cdot\\cosh(h)$ (gain) are all bar-symmetric projections of a common bar-anti-symmetric Hecke kernel; the bar-anti-symmetric (Faddeev $\\Phi_q$-alone, $\\sin$, $\\sinh$) projection is the one the framework empirically rejects. Conjectural-class structure per AGENTS.md §3b-cond — provable algebraic identities (bar-involution, $P_{\\mathrm{avg}}$ idempotency, $\\cos/\\cosh$ bar-symmetry on bar-anti-symmetric arguments) are carved out from the unproved unifying conjecture.",
  uses: [
    "def:bar-involution",
    "prop:averaging-resonance-rule",
    "prop:c5-involution-leibniz-decomposition",
    "prop:silver-ratio-beta-decay-null",
    "prop:neutron-qvalue-symbolic",
  ],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
    "geckpfeiffer2000",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "categorical-action",
    "kac-sunada",
    "conditional-class",
    "open-rd",
  ],
  computation: {
    engine: "python",
    script: "computations/ck_sector_classifier.py",
    status: "experimental",
  },
});
