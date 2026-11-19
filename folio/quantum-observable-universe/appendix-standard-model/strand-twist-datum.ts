import { definition } from "../../schema/builders";

export default definition({
  label: "def:strand-twist-datum",
  title: "Per-strand framing (twist) datum",
  lean: {
    ref: "qou:QOU.StandardModel.TwistDatum",
    validation: "not_checked",
  },
  uses: ["def:gauge-action-groupoid", "def:coulomb-charge"],
  cites: ["habiro2000", "bilson-thompson2005", "baez-huerta2010"],
  defines: ["strand-twist-datum"],
  tags: ["appendix", "standard-model", "framing", "ribbon", "hypercharge"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**The prose claim was corrected; the Lean witness still " +
        "overstates (beans qou-7dzg, qou-w1j9).** This block used to say " +
        "the datum *is* the framing the ribbon structure carries, AND " +
        "that it varies at fixed braid word. Those are incompatible: a " +
        "ribbon twist is determined by the braiding (Habiro, on e_n it is " +
        "(-1)^n A^{n(n+2)}), so it cannot vary at fixed object. The prose " +
        "now says the datum is an independent label. Two things remain " +
        "open. (1) TwistSeparationContent.lean observes that the witness " +
        "exists_same_writhe_ne_totalTwist mentions NO braid word in its " +
        "type -- every mention of braid/writhe/word in that file is a " +
        "comment -- so what is proved is that two integer vectors can " +
        "have different sums, not that a braid word admits distinct " +
        "framings. (2) conj:sm-hypercharge-invariant still rests on the " +
        "separation; the correction weakens its ground from a categorical " +
        "fact to a property of a label the corpus chose to attach.",
    },
    {
      kind: "status",
      date: "2026-08-01",
      body:
        "**Step (a) of the hypercharge programme (beans qou-4tul, " +
        "qou-q377).** The datum + gauge invariance + bar negation + " +
        "writhe-independence are proved sorry-free in the Lean sibling. " +
        "Whether the normalised candidate Y = 2(Q_twist - I3) passes the " +
        "GMN and Z6-spectrum batteries is the open content of " +
        "conj:sm-hypercharge-invariant; the enumeration probe is " +
        "computations/strand_twist_y_battery.py (exploratory, not wired).",
    },
    {
      kind: "note",
      date: "2026-08-02",
      body:
        "**Total-twist reduction (PR #4561, bean htw2).** The candidate " +
        "Y = 2(totalTwist/3 - I3) is a function of the TOTAL twist alone " +
        "(TwistDatum.Ycand_factors_totalTwist), and reproducing the SM " +
        "spectrum is equivalent to totalTwist = 3(I3 + Y/2) = 3Q " +
        "(TwistDatum.totalTwist_pinned_of_Ycand) - both sorry-free. So the " +
        "total-twist vector (u,d,nu,e) = (2,-1,0,-3) = 3Q is unique; the " +
        "battery's 4/10000 survivors are 1*2*2*1, the multiset multiplicity " +
        "of the pinned totals, Y-invisible. The open object is unchanged and " +
        "sharper: per-chiral-fermion framed braid words (compute totalTwist, " +
        "don't invert the SM target). Audit: " +
        "docs/audits/2026-08-02-hypercharge-strand-twist-total-reduction.md.",
    },
    {
      kind: "note",
      body: "Vertical stabilization shift of writhe referenced in the horizontal/vertical orbit comparison is `writhe_stabilize` in `QOU/StandardModel/WritheMarkovInvariance.lean`.",
    },
  ],
});
