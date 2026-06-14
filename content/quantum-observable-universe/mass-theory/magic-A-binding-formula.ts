import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-A-binding-formula",
  title:
    "Doubly-magic light-nucleus binding formula: $\\mathfrak{B}(^A_Z\\mathfrak{X}) = \\rho_F \\cdot \\mathfrak{m}_e \\cdot A \\cdot 8G$",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  uses: [
    "prop:binding-alpha-shift-extension",
    "prop:diagrammatic-double-magic-lr-fusion",
    "rem:strutinsky-from-graded-trace",
  ],
  defines: [],
  tags: [
    "binding",
    "magic-A",
    "doubly-magic",
    "shell-closure",
    "borromean-residue",
    "no-fitting",
    "regime-dispatch",
  ],
  lean: { ref: "qou:QOU.BraidKnot.magic_A_binding_formula" },
  authorNotes: [
    {
      kind: "status",
      body: "**Theorem (conditional on class hypothesis).** The Lean statement\n[`qou:QOU.BraidKnot.magic_A_binding_formula`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/mass-theory/magic-A-binding-formula.lean)\nasserts the formula\n$\\mathfrak{B}(^A_Z\\mathfrak{X}) = \\rho_F \\cdot \\mathfrak{m}_e \\cdot A \\cdot 8G$\nmodulo a single class hypothesis `MagicABindingFormula` recording the\nsubstrate-determined $\\rho_F$. The §3b-cond pattern (CLAUDE.md\n§3b-cond) makes this a rigorous-conditional theorem: fully verified\nmodulo the axiomatised class.\n\n**Reanalysis.** What was initially framed in this block\nas \"Open Math A\" and \"Open Math B\" turned out to be structurally\nalready answered in the framework. Both items reduce to verification\n/ formalisation, not derivation. See audit\n[`docs/audits/2026-05-31-binding-magic-A-wireup.md`](../../docs/audits/2026-05-31-binding-magic-A-wireup.md)\nfor the full reanalysis. Summary:\n\n- **$\\rho_F$ derivation (was \"Open Math A\"):** structurally answered\n  by\n  [`conj:kashaev-density-equals-sdp-multiplicity`](kashaev-density-equals-sdp-multiplicity.md)\n  (Rule-14 owner-authorised). The identity is\n  $\\rho_F = \\nu_{\\mathrm{SDP}}$, exact on the three SDP-confirmed\n  hyperbolic atoms (D, T, $^3$He). Only the $\\nu_{\\mathrm{SDP}}(^4\\mathrm{He})$\n  numerical verification (joint-tower SDP solver) is open.\n- **$A=3$ p/n asymmetry (was \"Open Math B\"):** structurally answered\n  by\n  [`conj:inter-nucleon-channel-color-tube`](../brings-surface/inter-nucleon-channel-color-tube.md)\n  (Bring color-tube weighting; proton's $(u, u, d)$ vs neutron's\n  $(u, d, d)$ color-sheet content via $\\mathrm{SO}(3)$-fiber action),\n  with the substrate-pure formula\n  $f_{\\mathrm{pn}} = z - h \\cdot (1/2 - \\delta/4)$\n  ($\\delta = \\Delta m_{n-p}/M_N \\approx 1.37 \\times 10^{-3}$, PROVED) already implemented in\n  [`closed_form_tau_M.py`](../../folio-assistant/computations/closed_form_tau_M.py)\n  under `pn_convention=\"bring_color_weighted\"`. Numerical check at\n  $q_0$: +180.9 ppm uniform correction across the four light nuclei\n  (each has one pn arc); the T vs $^3$He f-factor spread reported by\n  [`binding_shell_enhancement_derivation.py`](../../folio-assistant/computations/binding_shell_enhancement_derivation.py)\n  arises from the **arc-composition asymmetry** (T = pn+nn vs.\n  $^3$He = pp+pn) at the closed-form-ratio scale, not from a missing\n  scalar $q$-factor.\n\nThe remaining genuinely open items are: Lean formalisation of\n`conj:inter-nucleon-channel-color-tube` (conditional on\n`conj:s5-so3-fiber-action`); re-evaluation of\n`binding_shell_enhancement_derivation.py` against the\nBring-weighted ratio (does the 15% f-spread close?); SDP solver\nextension to verify $\\nu_{\\mathrm{SDP}}(^4\\mathrm{He}) = 2$. All\nthree are verification / formalisation, not derivation.",
    },
  ],
});
