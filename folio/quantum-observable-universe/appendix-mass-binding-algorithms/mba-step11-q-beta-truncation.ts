import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:q-beta-truncation",
  title: "$\\beta$-decay $\\mathfrak{Q}_\\beta = Q_{\\mathrm{base}} \\cdot \\prod_k (1 + c_k\\, u^k)$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_beta_predicted.py",
    witness: "computations/cal-3-q-beta.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-25",
      body: "**Corrected 2026-08-25 (PR #5765).** This bullet read *\"$c_k$ never reported as\n'fitted'\"*, which over-reached and inverted the discipline it implements. The\nAGENTS.md anti-flip-flop rule is *\"Report TIERED (`proved` / `near-match` /\n`fitted`), never binary wired/dropped\"* — **`fitted` is one of the three tiers**, so\nforbidding the label contradicts the rule. And the authoritative\n[`ck-dk-canonical-registry.md` §3](../../../docs/coordination/ck-dk-canonical-registry.md)\napplies it: **`c_4` is \"EMPIRICAL — CODATA fit / artifact (mechanically confirmed\n2026-07-11)\"**, `−0.97157`, a CODATA residual that is *\"0 by construction\"*. The\nregistry's summary row is equally explicit: *\"Only $c_2 = -1$ is canonical … $c_3$ is\na falsified near-match; $c_4$ is a CODATA fit; $c_5+$ are open.\"*\n\nAs written, this block instructed the reader **never to apply the label the\nauthoritative registry applies** — an anti-fit-discipline inversion sitting inside the\npaper. What the rule actually forbids is collapsing the tiering into a binary\nwire/un-wire decision, which is what drove the four-session flip-flop (#1452 ↔ #1479).\n\n**Also note the whole ladder is convention-C-frame and not yet re-derived under D**\n(`qou-cds1`): `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` makes the\nC-frame ladder and the mass channel's three-row forcing mutually exclusive, so this is\nnot a $z$-swap. Treat every $c_k$ conclusion above as **C-conditional** until that\nlands.*",
    },
    {
      kind: "status",
      body:
        "Superseded status figures, moved out of the published prose during " +
        "the one-voice pass: the earlier note read \"164.0x as of 2026-05-31 " +
        "/ Habiro-exact 5.7 ppb at the pre-re-pin muon anchor\". Those " +
        "numbers describe the pre-re-pin muon anchor, not the current pin; " +
        "the live figures are in the block's Status paragraph.",
    },
  ],
  tags: [
    "mba",
    "step-11",
    "q-beta",
    "ck-truncation",
    "kashiwara-b2",
    "beta-decay",
    "canonical-chain",
  ],
});
