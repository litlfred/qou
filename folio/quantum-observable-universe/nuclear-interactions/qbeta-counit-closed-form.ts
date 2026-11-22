import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-counit-closed-form",
  lean: {
    ref: "qou:QOU.Interactions.QBetaEnergyScale.Qbeta_closed",
    validation: "not_checked",
  },
  title:
    "Closed form of the counit $Q$-value $\\varepsilon(\\Delta)\\cdot\\mathfrak{E}_0$",
  uses: [
    "def:typed-crossing-operator",
    "rem:energy-scale-planck",
  ],
  tags: [
    "beta-decay",
    "q-value",
    "frobenius-counit",
    "markov-trace",
    "symbolic",
    "lean-verified",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Formalized as `QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one`." },
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved from prose: Scope-(a) throughout: none of this shows the $Q$-value wrong. It records which functional the construction evaluates, and that it is excluded by the canonical convention. See beans `qou-99qc` (the open decision), `qou-xzrj` (the residual), and `docs/audits/2026-08-26-qbeta-epsilon-is-inadmissible-under-convention-d.md`.",
    },
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**$\\Delta$ as written here does not name a unique element of " +
        "$H_3(q)$.** The statement opens *\"let $\\Delta = \\mathrm{NF}(n) " +
        "- \\mathrm{NF}(p)$ be the single-wrap normal-form difference of the " +
        "neutron and proton typed-crossing elements\"*, and the corpus " +
        "carries **six** constructions answering to that description, with " +
        "$\\mathrm{net}$ spread over $0.046$ — about a quarter of the " +
        "value $\\varepsilon(\\Delta) = h^2/2 - h$ that this block and the " +
        "whole $Q_\\beta$ ladder consume. Five are priced and one is struck: " +
        "the short model $\\Delta_S$ ($-0.187207194529$, the element whose " +
        "closed forms are the two asserted above); `build_nucleon_nf` at 9 " +
        "crossings ($-0.188290601471$); the `categorical-*-properties` " +
        "blocks *as stated* ($-0.2089$) — **not an element at all**, being " +
        "the difference of two quoted numbers at 5 and 4 significant " +
        "figures, so it has no word, no NF vector and no $\\mathrm{tr}_M$; " +
        "those blocks' own recipe *as constructed* ($-0.2137638$, excluded " +
        "scope-(b), exact Sturm count 0 on the octic); `build_atom_nf_exact` " +
        "at 11 interleaved crossings ($-0.227159711766$); and " +
        "`hecke_core`'s 11 gen-grouped crossings ($-0.233197711316$). The " +
        "last two carry the same multiset of typed crossings and differ only " +
        "in order, which is a genuine difference because $H_3(q)$ is not " +
        "commutative across generators. **Consumers must name which builder " +
        "they mean**; the two closed forms above hold for $\\Delta_S$ and " +
        "fail for the long models. Bean `qou-bg3w` (the open owner call on " +
        "which element the decay channel is about); measured in " +
        "`qbeta_delta_element_fork_pricing_probe.py`, " +
        "`qbeta_d1_categorical_candidates_probe.py` and " +
        "`qbeta_delta_net_four_values_probe.py`. Nothing above is a number " +
        "this changes — scope-(a), an identification caveat only.",
    },
    {
      kind: "note",
      date: "2026-09-03",
      body:
        "**Where the $\\Delta$ choice lands.** On $\\Delta_S$ the relation " +
        "$2\\alpha = \\varepsilon(\\Delta) - \\mathrm{tr}_M^z(\\Delta)$ " +
        "gives $\\alpha = (z-1)h/2$ identically, from the two closed forms " +
        "above — which is exactly the eigenphase axiomatised in " +
        "[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation), and " +
        "the functional form PR #6264 excluded exhaustively over the " +
        "admissible set $\\{q, z_D\\}$. On every long model the same " +
        "relation is quadratic in $z$ with $h = 0$ as its only real root, so " +
        "it is unavailable there. Either way $\\alpha$ is undetermined in " +
        "that form; what the choice decides is whether the corpus records " +
        "the axiom as derived-and-refuted or as unsupported. Recorded " +
        "because it is not stated in either bean.",
    },
  ],
});
