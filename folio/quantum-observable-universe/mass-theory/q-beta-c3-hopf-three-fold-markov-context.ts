import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-c3-hopf-three-fold-markov-context",
  title: "Per-step categorical chain, empirical confirmation, and near-match tier for c_3 = -2",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  tags: ["q-beta", "c3", "hopf-link", "markov-closure", "jones"],
  uses: ["prop:q-beta-c3-hopf-three-fold-markov"],
  computation: {
    engine: "mpmath",
    script: "computations/c3_hopf_habiro_analysis.py",
    witness: "computations/c3-hopf-habiro-analysis.witness.json",
    status: "verified",
  },
});
