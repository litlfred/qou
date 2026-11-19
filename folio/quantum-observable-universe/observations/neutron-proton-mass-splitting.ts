import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-10-10",
      body:
        "**Convention-C site, and no detector in the repo can see it.** Measured against `main`: " +
        "`4993/10000` is the rounded $z_C$, so the convention survives here as an *integer numerator* " +
        "folded into the closed form's coefficients — there is no `z` symbol, no `Real.sqrt`, and no " +
        "`markovZ`-shaped definition anywhere in the sibling `.lean`. Both `convention-c-producer-audit.py` " +
        "and `scripts/lean-markov-convention-audit.py` report the file clean, verified by running them; " +
        "a structural scan of the whole tree for this spelling finds this declaration and its provenance " +
        "audit doc and nothing else. Recorded as a detector blind spot alongside the re-derivation under " +
        "$z_D$ in bean `qou-wgta`, whose critical item 2 this is — the other three criticals it names " +
        "(`borromean_binding_recompute.py`, `y_lambda_wenzl_bridge.py`, `hecke/hecke_symbolic.py`) are all " +
        "fixed. The coefficients are `10000·(z q² + 2q − z)`, `5000·(q² − 2z q − 1)` and " +
        "`10000·(q² − z q − 1)` at `z = z_C`; do **not** substitute $z_D$ into them to improve the " +
        "residual, which would pick a convention by its miss.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Switched to convention D (owner ruling 2026-11-15: replace convention-C values with " +
        "convention D even if worse).** This supersedes the 2026-10-10 caveat's instruction not to " +
        "substitute $z_D$. The Lean closed form is now written in `z` and evaluated at " +
        "`zD = q0^3/(q0^2+1)`; the pins are Phi(uud) = -0.614886, Phi(udd) = -0.896395 (50 dps), " +
        "model value 1.0541 MeV, -18.5 % vs CODATA. The convention-C 1.302 MeV (+0.64 %) stays in " +
        "the prose only as a labelled historical comparison.",
    },
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "**The scale step (H_α) is not derived** (owner ruling 2026-11-15: state it as a named hypothesis). " +
        "Two further points are open, recorded in `docs/audits/2026-11-15-np-splitting-error-budget.md` (PR #7966). " +
        "§11: the traced product ∏ᵢ∏_{j>i}(σᵢ+dᵢⱼ) equals the half-twist trace for uud but not for udd. " +
        "§13–§18: the first derived u/d difference is the level-2 weight q^{∓2}; its sign is derived (u = e₁), its MeV scale is not. " +
        "The tautological Lean def `same_scale_both_levels` (`m_e·volB3 = m_e·volB3 := rfl`), which stood in for (H_α), is removed.",
    },
    {
      kind: "status",
      date: "2026-11-18",
      body:
        "**Two-term categorical Lagrangian & connected 4th-order Borromean V³ QED trace formalized (Epic qou-7xl8, 0 sorry).** " +
        "`QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm` (`trace_e21p_borromeanV3`, `trace_e21_strong_cartan_diff_borromeanV3`, `QAdjn_eq_static_add_half_QAdjp`, `trace_QAdjp_borromeanV3`, `trace_QAdjn_borromeanV3_connected`, " +
        "`trace_QAdj_connected_diff_borromeanV3`), " +
        "`QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace` (`chi21Reduced_ratio_at_one`, `tMod111_neutron_eq_q_sq_mul_proton`), " +
        "and `QOU.QuantumObservableUniverses.CategoricalLagrangianTwoTermBridge` (`hadronicScale_mul_q_sq_hbar_eq_me`, " +
        "`trace_lagrangian_diff_concrete_borromean_connected`) formalize the parameter-free two-term decomposition on $W_p=(2,1)$ and $W_n=(1,2)$.",
    },
  ],
  label: "prop:neutron-proton-mass-splitting",
  title: "Neutron--proton mass splitting from quark crossing change",
  lean: { ref: "qou:QOU.NeutronProtonSplitting.splitting_value",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
