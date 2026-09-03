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
    {
      kind: "note",
      date: "2026-08-29",
      body:
        "**Crossing count corrected 13 \u2192 11 (owner-authorised).** This block " +
        "previously read that the integer LP dual selects $L_+ \\to L_-$ " +
        "(*two* Hopf links, 4 gluon crossings) for a total of 13 crossings, " +
        "and that the neutron needs more gluon crossings than the proton " +
        "(4 versus 2). Two pieces of the block's **own** evidence contradict " +
        "that. First, the paragraph immediately above states that *a single* " +
        "Hopf link $L_- = \\sigma_1\\sigma_0$ restores structural stability. " +
        "Second, building the block's own recipe gives the k-ladder " +
        "9 crossings \u2192 0.788010, **11 \u2192 0.7975664**, 13 \u2192 1.235859: the " +
        "$+0.7976$ this block prints is the *eleven*-crossing value, and " +
        "1.235859 appears nowhere in the corpus. The 4-versus-2 asymmetry " +
        "claim does not survive and has been dropped; the $\\mathrm{tr}_M$ " +
        "depth comparison it rested on is kept, being a separate " +
        "measurement. Probe: `qbeta_delta_net_four_values_probe.py` (19/19). " +
        "This settles `qou-im4m` (#5892), which established the prose/code " +
        "mismatch but left open which side was wrong \u2014 it is the prose.",
    },
    {
      kind: "caveat",
      date: "2026-08-29",
      body:
        "**Not settled here: whether two gluon crossings suffice at all.** " +
        "Evaluating Frobenius positivity as $(\\mathrm{G}x)_\\gamma = " +
        "\\mathrm{tr}_M(e_\\gamma \\cdot T_w)$ \u2014 a reading that reproduces " +
        "this chapter's own claim that the bare 9-crossing element violates " +
        "positivity, with exactly one negative channel \u2014 no adjunction of " +
        "two gluon crossings is feasible for the *proton*; the minimum is " +
        "three. That rests on a reading of the predicate rather than on the " +
        "corpus's arithmetic, so it is deliberately **not** written into " +
        "this block. Bean `qou-vtlj`; adjudication belongs to `qou-bg3w`.",
    },
  ],
});
