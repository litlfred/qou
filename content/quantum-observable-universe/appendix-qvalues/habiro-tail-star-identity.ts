import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-tail-star-identity",
  lean: {
    ref: "qou:QOU.QBeta.HabiroTailStar.star",
    validation: "not_checked",
  },
  title:
    "Habiro-tail star identity: the $5_2$ Masbaum cyclotomic datum equals its bar-inverted $q$-Borel transform, with the quadratic $k$-exponent collapsed to linear",
  tags: [
    "habiro-tail",
    "masbaum",
    "cyclotomic-expansion",
    "gaussian-binomial",
    "bar-involution",
    "q-borel",
  ],
  uses: ["def:ecalle-borel-resummation"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-26",
      body:
        "**Proved sorry-free at every order $n$** — Lean " +
        "`QOU.QBeta.HabiroTailStar.star` (lean-direct exit 0, zero sorry " +
        "warnings). Two inversion lemmas carry it: `gaussBinom_inv` " +
        "($[n,k]_q = q^{k(n-k)}[n,k]_{q^{-1}}$, unconditional) collapses each " +
        "summand's quadratic $a$-exponent, and `qPoch_sq_inv` " +
        "($(q;q)_n^2 = q^{n(n+1)}(q^{-1};q^{-1})_n^2$) absorbs the residual " +
        "prefactor. Corollaries in `QOU.QBeta.HabiroTailCorollaries`: `That` " +
        "(the RHS named), `star_That`, `That_split` (transient structure), " +
        "`qPoch_succ`. Base ring generic `Field R`, no archimedean construct " +
        "(§7c, pre-wall).",
    },
    {
      kind: "note",
      date: "2026-07-26",
      body:
        "History: established computationally first — exact integer-Laurent " +
        "dict equality for $n \\le 32$ " +
        "(`computations/qbeta_habiro_tail_util.py`, witness " +
        "`qbeta-habiro-tail-util.witness.json`), numerically to $10^{-497}$ " +
        "for $n \\le 64$ (`qbeta-5two-gbar-pole-ladder.witness.json`). The " +
        "Lean proof discharges that computation for all $n$. The two " +
        "ANALYTIC consequences recorded in those witnesses — " +
        "$c_\\infty = (\\tilde q;\\tilde q)_\\infty^2$ as a convergent " +
        "infinite product, and the pole ladder at $w = -q_0^k$ — are limit " +
        "statements about the archimedean evaluation and are deliberately " +
        "NOT claimed by this block; only their algebraic skeleton is.",
    },
  ],
});
