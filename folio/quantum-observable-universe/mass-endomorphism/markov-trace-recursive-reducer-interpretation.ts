import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:markov-trace-recursive-reducer",
  label: "rem:markov-trace-recursive-reducer-interpretation",
  title: "Memoisation optimisation and the categorical-mass reading of the reducer",
  tags: [
    "markov-trace",
    "recursive-algorithm",
    "memoisation",
    "categorical-mass",
  ],
  uses: [
    "prop:markov-trace-recursive-reducer",
    "prop:markov-trace-axiomatic-closed-form",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We memoise the recursive `tr_M` on $(w, n)$ via `functools.lru_cache`." },
  ],
});
