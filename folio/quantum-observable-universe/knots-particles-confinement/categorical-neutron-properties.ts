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
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Earlier text, removed from the prose 2026-11-15: (1) \"the bare 9-crossing element remains LP unstable; the sigma_0 channel violates Frobenius positivity after the second quark crossing\"; (2) \"L_+ -> L_-, 4 gluon crossings, 13 total\" (bean qou-vtlj: the stated net(n) = +0.7976 is the eleven-crossing value); (3) \"the dd crossing creates a deeper instability than the proton's (tr_M = -0.132 vs -0.006)\" (bean qou-jqjx: those figures came from fsh-guts/deprecated/computations/integer-lp-gluon.py on convention C with tr_M(e^-) = z^3, a weight retired 2026-05-19; reproduced there as -0.132224 and -0.005936). Both corrections were needed: fixing the crossing count removed the 4-vs-2 asymmetry and moved the claim onto the two convention-C numbers.",
    },
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**Withdrawn: the LP-stability paragraph and the 4-versus-2 " +
        "asymmetry** (bean `qou-jqjx`). The proton block carries the full " +
        "diagnosis; the short form is that every number here came from " +
        "`fsh-guts/deprecated/computations/integer-lp-gluon.py`, which uses the " +
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
      date: "2026-09-03",
      body:
        "**RETRACTED (this note's earlier text, dated 2026-08-29).** It read " +
        "that evaluating Frobenius positivity as $(\\mathrm{G}x)_\\gamma = " +
        "\\mathrm{tr}_M(e_\\gamma \\cdot T_w)$ is *\"a reading that " +
        "reproduces this chapter's own claim that the bare 9-crossing element " +
        "violates positivity, with exactly one negative channel\"*, and " +
        "concluded that no two-gluon adjunction is feasible for the proton, " +
        "the minimum being three. **Three things are wrong with that, and the " +
        "hedge it carried \u2014 that this rests on a reading of the predicate " +
        "\u2014 is the only part that survives.**\n\n" +
        "**1. The corroboration cites struck text.** *\"This chapter's own " +
        "claim\"* is the sentence one paragraph above, struck through since " +
        "2026-08-24 by [`qou-jqjx`](#rem:gluon-stabiliser-ledger): the bare " +
        "element's instability was an artefact of the retired weight " +
        "$\\mathrm{tr}_M(e^-) = z^3$, retired 2026-05-19. Reproducing a " +
        "withdrawn number is evidence *against* a reading, not for it.\n\n" +
        "**2. The numbers did not reproduce it in the first place.** The " +
        "withdrawn claim was $\\mathrm{tr}_M(T_w) < 0$ (retired-weight " +
        "$-0.0059$ proton, $-0.1322$ neutron). The probe's $\\gamma = 1$ " +
        "channel gives $+0.5444$ \u2014 which is `qou-jqjx`'s corrected live " +
        "value $+0.544370$ to the digit. So it agreed with the *correction* " +
        "and was described as agreeing with the *bug*.\n\n" +
        "**3. The basis was over-complete.** " +
        "[`def:stable-atom`](#def:stable-atom) defines $\\mathrm{G}$ over the " +
        "primitive Wedderburn-block operators $\\{e_\\lambda\\}_{\\lambda " +
        "\\vdash k}$, of which $H_3(q)$ has **three**. The probe built " +
        "**six**, and the extra ones carry the single negative pairing " +
        "($-0.02275$) the note reported. Re-run of " +
        "`computations/probes/nucleon-lp-convention-probe.py` on 2026-09-03: " +
        "under convention D every step of both nucleons is positive \u2014 " +
        "proton $\\min(\\mathrm{G}x) = +0.342489, +0.279195, +0.339149$; " +
        "neutron $+0.277726, +0.172959, +0.217525$. No negative channel.\n\n" +
        "**What is genuinely open** is narrower than the note claimed and is " +
        "not settled by either side: the definition names the " +
        "primitive-idempotent basis, the live probe uses `pyhecke.gram`'s " +
        "NF-word Gram, and the partition-indexed decomposition the definition " +
        "asks for **does not exist** (rank 4 against augmented rank 5). Which " +
        "object $\\mathrm{G}$ is remains the open question; nothing above " +
        "answers it. Scope-(a). Bean `qou-vtlj`.",
    },
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**The surviving $L_-$ sentence disagrees with the live ranking, and " +
        "is not struck.** The paragraph above still states that the integer " +
        "LP dual *selects $L_-$ as the minimum-action stabiliser*. Under " +
        "convention D, measured by " +
        "`computations/probes/nucleon-lp-convention-probe.py` (re-run " +
        "2026-09-03), the neutron's $L_+ . L_-$ ranks **26 of 41** feasible " +
        "configurations at $|\\mathrm{tr}_M| = 0.690056$, against bare " +
        "$0.408267$ with no gluon at all; the min-$|\\mathrm{tr}_M|$ optimum " +
        "is a **single $\\sigma_0$ at one crossing** ($0.217525$), and under " +
        "the minimum-crossing objective that " +
        "[`def:universal-ilp-algorithm`](#def:universal-ilp-algorithm) " +
        "actually states it is **zero** crossings. The same holds for the " +
        "proton ($\\sigma_0 . \\sigma_0$ ranks 10/41 at $0.615273$ against " +
        "bare $0.544370$). So the selection sentence, the 11-crossing total " +
        "it feeds, and the $\\mathfrak{m}_{\\mathfrak{n}} - " +
        "\\mathfrak{m}_{\\mathfrak{p}}$ mechanism that rests on it are all " +
        "in tension with the live convention. `qou-jqjx` proposed nothing in " +
        "place of them deliberately \u2014 the derivation needs re-deriving " +
        "rather than patching \u2014 and that judgement is not revisited " +
        "here. Flagged, not resolved. Scope-(a).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): See [Table](#tbl:categorical-neutron-table-data)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The crossing pairs appear in [Table: Neutron crossing pairs](#tbl:categorical-neutron-table-data)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([energy scale](#rem:beta-decay-energy-scale))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([formation chain](#rem:meson-to-proton-via-borromean))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([local substrate](#prop:local-substrate-q))" },
  ],
});
