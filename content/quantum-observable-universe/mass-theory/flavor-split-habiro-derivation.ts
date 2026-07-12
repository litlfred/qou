import { conjecture } from "../../schema/builders";

/**
 * Habiro element for the nucleon flavor split.
 *
 * Conjectures that the ≈ 0.128% residual of the Δ_pn baseline coupling
 * X_baseline(q) = (q−1)²(1−q⁻⁴)/3 closes through the H_4(q) alternating
 * (sign-block) channel of the weak two-vertex insertion, weighted by
 * 1/[4]_q! — the weak-force analog of the α_EM Schwinger factor
 * [2]_q·(1 − h²α).
 *
 * The Lean sibling proves the two supporting identities sorry-free over
 * a generic commutative ring (§7c): the crossing-reversal central
 * scalar σ³ − σ⁻³ = h(h² + 3) = q³ − q⁻³, and the alternating-channel
 * expansion q² = 1 + h·q. Neither of these proves the conjectured
 * closure; the exact H_4 alternating projection polynomial is open.
 */
export default conjecture({
  label: "conj:flavor-split-habiro-derivation",
  title:
    "Habiro element for the flavor split $\\mathfrak{m}_{\\mathfrak{n}} - \\mathfrak{m}_{\\mathfrak{p}}$ via the $H_4$ alternating channel",
  lean: { ref: "qou:QOU.FlavorSplit.topological_flavor_split" },
  uses: [
    "prop:neutron-proton-splitting",
    "prop:alpha-em-habiro-bar-involution",
  ],
  computation: {
    engine: "python",
    script: "computations/mn_flavor_split_h4_plancherel.py",
    witness: "computations/mn-flavor-split-h4-plancherel.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-07-12",
      body:
        "$X_{\\mathrm{baseline}}(q) = (q-1)^2(1-q^{-4})/3$ is a structured " +
        "near-match (residual $\\approx 1.76\\times10^{-6}$, matching the " +
        "H$_4$ Plancherel probe's $-0.1277\\%$ control), **not** a derived " +
        "closed form — do not wire it to production as canonical. The " +
        "committed witness verifies the baseline numerics and leaves the " +
        "higher-rank Plancherel closure as a candidate.",
    },
    {
      kind: "note",
      date: "2026-07-12",
      body:
        "Integrated from an orphan `.md` (a `.lean` sibling existed but no " +
        "manifest) per the 2026-07-12 exposition-drain ledger §5. The " +
        "draft's alternating-channel line " +
        "$\\langle\\sigma_i^{-2}\\rangle_{\\mathrm{alt}} = 1 - hq^{-1} " +
        "\\approx 1 - h^2$ was corrected to the proved algebra " +
        "$(-q^{-1})^{-2} = q^2 = 1 + hq$ (the $1 - hq^{-1} = q^{-2}$ form " +
        "is the *photon singlet* evaluation of $\\sigma_i^{2}$, not the " +
        "crossing-reversed weak insertion). Process-voice framing " +
        "('we will write out') replaced by an explicit open-step " +
        "statement.",
    },
  ],
  tags: [
    "flavor-split",
    "delta-pn",
    "habiro-element",
    "hopf-antipode",
    "h4-alternating-channel",
    "wenzl-weight",
    "near-match",
    "open-conjecture",
  ],
});
