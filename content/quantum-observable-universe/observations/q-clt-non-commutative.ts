import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-clt-non-commutative",
  title:
    "q-Central Limit Theorem for Hecke transfer matrices — categorical q-convolution converges to the q-Gaussian attractor",
  lean: {
    ref: "qou:QOU.Observations.QCltNonCommutative",
    validation: "not_checked",
  },
  uses: [
    "rem:non-commutative-probability-dictionary",
    "prop:algebraic-gns-embedding",
    "prop:q-plancherel-asymptotic-skeleton",
    "thm:jones-markov-trace",
  ],
  cites: [
    "blitvic2012",
    "marsh2006",
    "biane1998",
    "feray2010",
  ],
  tags: [
    "q-clt",
    "non-commutative-probability",
    "q-gaussian",
    "central-limit-theorem",
    "tsallis-entropy",
    "blitvic",
    "issue-649",
    "conditional-class",
  ],
});
