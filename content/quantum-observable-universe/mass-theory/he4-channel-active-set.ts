import { proposition } from "../../schema/builders";

/**
 * ⁴He compositional channel active set via operator-selection LP.
 *
 * The ⁴He = (Z=2, N=2) bound state admits three primary
 * compositional channels (each summing to A = 4 nucleons):
 *
 *   D ⊕ D    : deuteron ⊕ deuteron
 *   T ⊕ p    : tritium  ⊕ proton
 *   ³He ⊕ n : helium-3 ⊕ neutron
 *
 * Define the **channel binding residual**
 *
 *   t_i := Δ_cat(⁴He) − Δ_cat(constituents of channel i)
 *
 * (how much ⁴He binding is left for the magic-shell coupling
 * after subtracting the channel's free-constituent sum).  From the
 * empirical anchor witness
 * (magic-shell-empirical-instantiation.witness.json):
 *
 *   t_{DD}  = 24.16 MeV    (4.05 sum, 24.16 residual)
 *   t_{Tp}  = 20.38 MeV
 *   t_{3He+n} = 21.18 MeV
 *
 * The operator-selection LP (prop:operator-selection-lp) with
 *
 *   primal:   minimise  t · x   subject to   G x ≥ 0,  Σ x ≥ n_target
 *   dual:     find shadow prices y_0, y_i ≥ 0
 *   G:        channel × channel pairing, identity at leading order
 *   n_target: Δ_coupling(2,2) = Δ_cat(⁴He) − 2·Δ_cat(³He) = 13.197 MeV
 *
 * solves uniquely at q_0 (strong duality holds, gap = 0):
 *
 *   primal weights x* = (0, 13.197, 0)
 *     ⇒ T⊕p channel is the *primal-saturating* decomposition.
 *
 *   dual shadow prices y* = (3.778, 0, 0.796)
 *     ⇒ D⊕D has the highest receptivity (most binding for a
 *       given coupling perturbation); ³He⊕n is secondary.
 *
 *   active_set = {DD, ³He+n}
 *     ⇒ the two channels whose dual constraints are tight.
 *
 * **Proposition.** The ⁴He operator-selection LP has
 *   1. unique primal optimum at the T⊕p channel,
 *   2. active set = {DD, ³He+n} (constraints tight),
 *   3. dual ordering y*_{DD} > y*_{³He+n} > y*_{Tp} = 0.
 *
 * **Conditional on** the empirical witness anchors
 * (Δ_cat values from magic-shell-empirical-instantiation.witness.json)
 * and the LP solution from he4-sdp-compositional-probe.witness.json.
 *
 * Per CLAUDE.md §3b-cond the Lean version is axiomatised as a
 * class `HasHe4ChannelActiveSet` whose instance encodes the
 * witness-verified ordering.
 *
 * Used by:
 *   - rem:he4-magic-shell-fingerprint — physical interpretation:
 *     T⊕p decomposes the energy; D-pairing receives the magic
 *     shell.
 *
 * Witness:
 *   folio-assistant/computations/he4-sdp-compositional-probe.witness.json
 * Probe:
 *   folio-assistant/computations/probe_he4_sdp_compositional.py
 * Audit:
 *   docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He
 */
export default proposition({
  label: "prop:he4-channel-active-set",
  title:
    "$^4\\mathrm{He}$ operator-selection LP: primal $\\mathrm{T} \\oplus p$, active set $\\{\\mathrm{D} \\oplus \\mathrm{D},\\,{}^3\\mathrm{He} \\oplus n\\}$",
  uses: [
    "prop:operator-selection-lp",
  ],
  computation: {
    engine: "scipy",
    script: "folio-assistant/computations/probe_he4_sdp_compositional.py",
    witness: "folio-assistant/computations/he4-sdp-compositional-probe.witness.json",
    status: "verified",
    requires: ["numpy", "scipy"],
  },
  lean: { ref: "qou:QOU.BraidKnot.He4ChannelActiveSet.HasHe4ChannelActiveSet" },
  tags: [
    "he4",
    "doubly-magic",
    "operator-selection-lp",
    "shadow-price",
    "active-set",
    "compositional-channels",
    "f1-fingerprint",
    "deuteron-pairing",
    "verified-empirically",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "Per the conditional-class pattern (CLAUDE.md §3b-cond) the Lean\nversion is a class `HasHe4ChannelActiveSet` whose instance\nencodes the witness-verified ordering; the empirical\n$\\Delta_\\mathrm{cat}$ anchors and the LP solution are the sole\n`sorry` inputs.",
    },
  ],
});
