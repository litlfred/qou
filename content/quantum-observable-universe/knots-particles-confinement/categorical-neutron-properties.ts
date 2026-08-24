import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-neutron-properties",
  interprets: "def:categorical-neutron",
  title: "Neutron: NF construction, mass, transition, and charge",
  tags: ["neutron", "hadron", "baryon", "color-tube", "knot", "categorical"],
  uses: [
    "def:categorical-neutron",
    "def:categorical-proton",
    "def:up-quark",
    "def:down-quark",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**Withdrawn: the LP-stability paragraph and the 4-versus-2 " +
        "asymmetry** (bean `qou-jqjx`). The proton block carries the full " +
        "diagnosis; the short form is that every number here came from " +
        "`computations/_deprecated/integer-lp-gluon.py`, which uses the " +
        "`tr_M(e-) = z^3` weight retired on 2026-05-19 in favour of " +
        "`h*z^2 + z`. Reproduced on the retired convention this block's " +
        "`-0.132` comes out at `-0.132224`; on the live convention D the same " +
        "element is `+0.408267`, and so is every intermediate step of the " +
        "typed build (`B_3` +0.998562, then +0.501130, +0.172959, +0.408267). " +
        "So 'remains LP unstable' and 'the sigma_0 channel violates Frobenius " +
        "positivity following the second quark crossing' are both false under " +
        "the live convention — the sigma_0 channel is never negative at any " +
        "step.",
    },
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**The asymmetry is the load-bearing loss.** This block says the " +
        "4-versus-2 gluon-crossing split 'is what carries the mass split into " +
        "Q_beta'. Under D the split does not exist. The quoted `L_+ -> L_-` " +
        "falls to rank 26 of 41 at `|tr_M| = 0.690056`, against a bare " +
        "`0.408267`; the `|tr_M|` optimum is a single `sigma_0` at ONE " +
        "crossing for the neutron and ONE for the proton, so the ratio is 1:1. " +
        "Under the minimum-crossing objective that `def:universal-ilp-" +
        "algorithm` actually states it is 0:0, since bare is feasible for " +
        "both. Either way m_n - m_p loses its stated mechanism. Nothing is " +
        "proposed in its place here — the derivation needs re-deriving, not " +
        "patching, and that is deliberately left open rather than guessed at.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Not affected: the quark content, the charge computation, the NF " +
        "coefficients themselves (which are convention-independent — the " +
        "Hecke multiplication table does not involve `tr_M`), or the " +
        "beta-decay discussion. What changes is the Markov trace evaluated " +
        "against those coefficients, hence Frobenius positivity and everything " +
        "the gluon LP selects on.",
    },
  ],
});
