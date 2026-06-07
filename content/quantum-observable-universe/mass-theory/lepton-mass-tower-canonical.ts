import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:lepton-mass-tower-canonical",
  lean: {
    ref: "qou:QOU.BraidKnot.LeptonMassTowerCanonical.lepton_mass_ratio",
    validation: "not_checked",
  },
  title:
    "Canonical operator-level lepton-mass-tower formula: there exists a categorical formula $\\mathfrak{m}(K_\\ell) = m_e \\cdot \\mathcal{F}_\\ell(q)$ for each lepton $\\ell \\in \\{\\mathfrak{e}, \\mu, \\tau\\}$ expressed as a per-braid Markov-trace-weighted sum over $K_\\ell$'s braid representative, **without** invoking the SUPERSEDED scalar substrate density $\\rho_q = 1/\\hbar_q^2$ as a dimensional factor.",
  uses: [
    "prop:rho-k-graded-expansion",
    "prop:per-braid-mass-tower",
    "prop:categorical-mass-markov",
    "def:typed-crossing-operator",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-24",
      body:
        "**Open conjecture (PR #1127 Phase 3 finding).** Set up the formal framework " +
        "for the lepton variant of [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md). " +
        "The atomic graded expansion `ρ_K^LO + ρ_K^single-gen + ρ_K^pair-gen + ...` is " +
        "framed for nuclei (LO piece `Z·m_p + N·m_n + Z·m_e`); for leptons (`Z = N = 0`), " +
        "the LO piece is **zero**, and the canonical formula must take a different form. " +
        "The Phase 3 audit doc " +
        "[`docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md) " +
        "established that the direct `|tr_M(muon)|/|tr_M(electron)|` ratio at q_0 is " +
        "**0.27** (NOT the CODATA 206.77), confirming that the Skein formula " +
        "`m_μ/m_e = Vol(4_1)/ℏ_q²` uses **Kashaev hyperbolic volumes + SUPERSEDED " +
        "ρ_q dimensional factor**, NOT a direct operator-level ratio. " +
        "This conjecture asserts that a canonical (non-ρ_q) operator-level formula EXISTS; " +
        "concrete derivation is open work (multi-day analytical task). " +
        "Cross-link: [`2026-05-24-superseded-rho-q-purge.md`](../../../docs/audits/2026-05-24-superseded-rho-q-purge.md). " +
        "Once derived, this conjecture promotes to a theorem; until then, the Skein " +
        "formula in [`prop:skein-mass-relation`](../../observations/skein-mass-relation.md) " +
        "is the operative (Kashaev-LIMIT) substitute.",
    },
    {
      kind: "caveat",
      date: "2026-05-24",
      body:
        "**Im(q) does not affect leading-order ratio.** By the modulus-projection " +
        "argument in the Phase 3 audit (§Implications (c)): both numerator " +
        "`|tr_M(muon)|` and denominator `|tr_M(electron)|` have the same modulus-" +
        "projection structure; the ratio is real-valued and insensitive to Im(q) " +
        "at leading order. So the canonical operator-level formula `F_ℓ(q)` is " +
        "robust against complex-q deformation, unlike the SUPERSEDED `ρ_q` factor " +
        "which is NOT bar-covariant.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-24",
      body:
        "**Conjectural form (sketch).** Expected shape: `F_ℓ(q) = ξ_ℓ(q) · Vol_q^tower(K_ℓ)` " +
        "where `ξ_ℓ(q)` is a lepton-sector dimensional factor (replacing the SUPERSEDED " +
        "`1/ℏ_q²`) and `Vol_q^tower(K_ℓ)` is the per-braid q-volume of the lepton's " +
        "braid representative (electron = trefoil $\\sigma_1^3$; muon = figure-eight " +
        "$(\\sigma_1 \\sigma_2^{-1})^2$ per canonical identification, see " +
        "[`docs/audits/2026-05-24-muon-knot-id-conflict.md`](../../../docs/audits/2026-05-24-muon-knot-id-conflict.md)). " +
        "The Kashaev `q → 1` limit should recover `Vol_q^tower(K_ℓ) → Vol_hyp(K_ℓ)`, " +
        "giving the Skein formula as the LO substrate-truncation. The OPEN question " +
        "is the explicit form of `ξ_ℓ(q)`.",
    },
  ],
  tags: [
    "tier:E",
    "lepton",
    "mass-formula",
    "operator-level",
    "non-superseded",
    "categorical",
    "open-conjecture",
    "phase-3",
  ],
  cites: [
    "kashaev1995",
    "wenzl1988",
    "jones1987",
  ],
});
