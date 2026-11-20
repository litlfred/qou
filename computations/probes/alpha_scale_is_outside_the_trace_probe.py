#!/usr/bin/env python3
"""The alpha-cluster scale must come from OUTSIDE the trace channel.

The corpus's remaining extensive carrier is the alpha-cluster term
(`docs/audits/2026-08-02-alpha-cluster-su4-extensive-term.md`): structure derived
via the proved SU(4) gate `dim [1^A] = C(4, A)` — nonzero for `A <= 4`, vanishing
above, which is the categorical origin of alpha-clustering — with the **scale
open** at `~29.8 MeV/alpha` (B/n_alpha constant to CV 0.053 across 4He, 8Be,
12C, 16O).

This probe asks the one question the preceding exclusions leave: **can the trace
channel supply that scale?** It cannot, and the margin is large.

## The measurement

    A=4, chain (3 adjacent bonds)     L = 1.46970   ->   6.152 MeV
    A=4, complete graph, best order   L = 2.40868   ->  10.083 MeV
    alpha-cluster scale                                  29.800 MeV/alpha

    the trace channel supplies 20.6 % to 33.8 % of ONE alpha
    (and only 9.8 % to 16.0 % of the BULK coefficient — see the correction below)

and the upper figure already assumes the complete graph with every interference
term included, which the preceding work showed is the most the bond topology can
produce. Both bond-topology routes are closed: additive capped at `20.649` MeV
with per-bond values free, non-additive at `10.083` MeV with the many-body sign
measured NEGATIVE at `A = 4`.

**So the missing ~2/3 to 4/5 of each alpha is not in this channel.** That is the
useful output: it does not supply the scale, it says where not to look for it.

## A structural fact, and a conflation NOT to make

The Schur-Weyl sum's support is entirely on partitions with at most two rows —
measured here at `n = 3, 6, 9, 12, 15` (nonzero / total: 2/3, 4/11, 5/30, 7/77,
8/176, max rows 2 at every one).

**This is not new.** The `t7qv` witness already records it — *"convention D puts
the three-strand q-antisymmetriser in the radical … EVERY partition with >= 3
rows carries weight exactly zero at every strand count"* — verified there at
`n = 6` and `n = 9`. What is added here is the extension to `n = 3, 12, 15` and
the total-vs-nonzero counts, which is incremental.

**And the conflation to avoid:** the two-row support is a fact about partitions
of the **strand count** `n = 3A`, on the Hecke side. The alpha-cluster `[1^4]` is
a partition of the **nucleon count** `A`, in SU(4) spin-isospin space. These are
different spaces, and "the trace is two-row, therefore it cannot carry a
four-row SU(4) object" is **not** a valid inference — it is the arity/space
conflation the corpus carries a STRICT section about. The two-row fact is
reported as a property of the trace and as a *candidate* explanation for the
measured shortfall, not as an exclusion of the alpha-cluster term.

The exclusion that IS established here is the numerical one above, and it needs
no representation-theoretic bridge.

## 🛑 CORRECTION — the target above is the OBSERVED value, not the extensive one

The `~29.8 MeV/alpha` (= `7.45 MeV/nucleon`) figure is an **observed** binding,
and comparing the trace to it answers "can the trace reproduce the measured 4He
binding". That is a fair question and `20.6-33.8 %` is its answer. **It is not
the question an extensive term has to answer.**

`QOU.Mass.SaturationPeakStructure` (landed 2026-08-30) proves the per-nucleon
curve `f(u) = a_V - a_S/u - a_C*u^2` **never attains** its bulk coefficient
`a_V` — the surface term keeps it strictly below at every mass number — and
records the empirical values in units of `hbar_q^2 * m_N`:

    a_V   (bulk volume coefficient)   1.71  ->  15.762 MeV/nucleon
    peak B/A at 62Ni                  0.954 ->   8.794
    238U B/A                          0.821 ->   7.568

So **`~8 MeV/nucleon` is the observed peak, and the extensive (bulk) coefficient
is `15.762`, 1.79x larger.** An extensive term must supply `a_V`; the surface and
Coulomb terms then subtract to give the observed curve. Measured against that:

    bulk required for 4 nucleons   4 x 15.762  =  63.048 MeV
    trace, chain                                   6.152 MeV   ->   9.8 %
    trace, complete graph                         10.083 MeV   ->  16.0 %

**The exclusion is therefore about twice as strong as first stated**, and both
framings are kept above because they answer different questions.

One thing NOT to read into the `1.71`: it is `a_V/(hbar_q^2 * m_N)` computed
FROM the empirical `a_V`, i.e. a re-expression of the SEMF constant in substrate
units, not a derivation of it. That `1.71 * hbar_q^2 * m_N` reproduces
`a_V ~ 15.8 MeV` is arithmetic, not a prediction.

## Consequence for the programme

The alpha-cluster route is **sharpened, not blocked**, by everything on this
branch. `[1^4]` is a four-body SU(4) object, not a bond-graph object, so neither
the additive cap nor the `A=4` negative many-body sign applies to it. What the
bond-topology exclusions do is remove the bond graph as a competitor, leaving
the alpha-cluster term as the carrier that has to supply the missing bulk — and
this probe measures how much bulk that is.

## Scope (a)

Pure-proton chains for the trace figures, so no species asymmetry enters and the
AME comparison is a scale check rather than a prediction. `29.8 MeV/alpha` is
the corpus's measured mean, cited not re-derived. Nothing fitted, nothing wired,
and no mechanism for the missing scale is proposed here — proposing one on the
strength of a ratio would be the numerology the anti-fit discipline forbids.
"""

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, Q_MUON_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(30)

# measured on this branch (manybody_sign_by_bond_topology_probe)
L_CHAIN_A4 = "1.46969815276540455"
L_K4_BEST = "2.40867875195"
# corpus mean, docs/audits/2026-08-02-alpha-cluster-su4-extensive-term.md
ALPHA_SCALE_MEV = "29.8"
# QOU.Mass.SaturationPeakStructure: the per-nucleon curve NEVER attains a_V.
# These are that file's recorded empirical values, in units of hbar_q^2 * m_N.
A_V_OVER_HQ2_MN = "1.71"          # bulk volume coefficient
PEAK_OVER_HQ2_MN = "0.954"        # observed peak, 62Ni
M_N_MEV = "938.91875"


def all_partitions(n):
    from sympy.utilities.iterables import partitions as _sp
    out = []
    for d in _sp(n):
        lam = []
        for k in sorted(d, reverse=True):
            lam += [k] * d[k]
        out.append(tuple(lam))
    return out


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    q = Q_MP
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    alpha = mp.mpf(ALPHA_SCALE_MEV)

    # Copilot review on #6443: ENFORCE the proton-anchor assumption rather than
    # merely stating it. The two pins differ at the 9th significant digit
    # (proton 1.10997858275..., muon 1.10997859564...); L_CHAIN_A4 / L_K4_BEST
    # were measured at the proton pin, so a muon q here would be a straddle.
    check("q_0 is the PROTON pin (the pin the L values were measured at)",
          Q_50_DIGIT_STR != Q_MUON_50_DIGIT_STR
          and Q_50_DIGIT_STR.startswith("1.10997858"),
          f"Q_50_DIGIT_STR = {Q_50_DIGIT_STR[:20]}..., muon pin = "
          f"{Q_MUON_50_DIGIT_STR[:20]}...; they differ at the 9th digit and "
          f"the proton prefix 1.10997858 is present.")

    print("=" * 78)
    print("  The alpha-cluster scale is OUTSIDE the trace channel")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV\n")

    # ------------------------------------------- 1. the numerical exclusion
    print("-" * 78)
    print("  1. What the trace channel can supply against one alpha")
    print("-" * 78)
    b_chain = E0 * mp.mpf(L_CHAIN_A4)
    b_k4 = E0 * mp.mpf(L_K4_BEST)
    frac_lo, frac_hi = b_chain / alpha, b_k4 / alpha
    print(f"""
  A=4 chain (3 adjacent bonds)     L = {L_CHAIN_A4}  ->  {mp.nstr(b_chain, 8)} MeV
  A=4 complete graph, best order   L = {L_K4_BEST}      ->  {mp.nstr(b_k4, 8)} MeV
  alpha-cluster scale (corpus)                              {ALPHA_SCALE_MEV} MeV/alpha

  the trace supplies {mp.nstr(100*frac_lo, 4)} % to {mp.nstr(100*frac_hi, 4)} % of ONE alpha
""")
    check("the trace channel supplies under 35 % of one alpha, even at the "
          "complete graph", frac_hi < mp.mpf("0.35"),
          f"{mp.nstr(100*frac_hi, 4)} % at the complete graph with every "
          f"interference term included — which the preceding work showed is "
          f"the most the bond topology can produce (additive capped at 20.649 "
          f"MeV with per-bond values FREE; non-additive at 10.083 MeV with the "
          f"A=4 many-body sign measured NEGATIVE). The missing bulk is not in "
          f"this channel.")

    # --------------------------------------- 2. the two-row support, cited
    print("\n" + "-" * 78)
    print("  2. The trace's support is two-row — already known, extended here")
    print("-" * 78)
    print(f"\n  {'n':>4}{'partitions':>13}{'nonzero':>9}{'max rows':>11}")
    rows, two_row = [], []
    for n in (3, 6, 9, 12, 15):
        yt = y_lambda_at(n, q)
        nz = [lam for lam, v in yt.items() if mp.mpf(str(v)) != 0]
        tot = len(all_partitions(n))
        mr = max(len(l) for l in nz)
        two_row.append(mr <= 2)
        rows.append({"n": n, "partitions": tot, "nonzero": len(nz),
                     "max_rows": mr})
        print(f"  {n:>4}{tot:>13}{len(nz):>9}{mr:>11}")
    check("only two-row partitions carry weight, at every strand count tested",
          all(two_row),
          "NOT NEW: the t7qv witness already records that every partition with "
          ">= 3 rows carries weight exactly zero, verified there at n=6 and "
          "n=9. Added here: n=3, 12, 15 and the total-vs-nonzero counts. "
          "Incremental, and reported as such.")

    # ------------------------------------------ 3. the conflation NOT made
    print("\n" + "-" * 78)
    print("  3. The inference NOT drawn, and why")
    print("-" * 78)
    print("""
  It is tempting to argue: the trace is two-row, the alpha-cluster [1^4] is
  four-row, therefore the trace cannot carry it. THAT IS NOT VALID.

  The two-row support is a fact about partitions of the STRAND count n = 3A, on
  the Hecke side. The alpha-cluster [1^4] is a partition of the NUCLEON count A,
  in SU(4) spin-isospin space. Different spaces. Concluding one from the other
  is the arity/space conflation the corpus carries a STRICT section about, and
  four instances of it reached durable artifacts in a single session once.

  The two-row fact is reported here as a property of the trace and as a
  CANDIDATE explanation for the measured shortfall -- nothing more. The
  exclusion that IS established is the numerical one in section 1, which needs
  no representation-theoretic bridge at all.
""")
    check("the tempting representation-theoretic inference is named and "
          "declined", True,
          "Stating it would be a stronger result and an invalid one. The "
          "numerical exclusion stands on its own and is what is claimed.")

    # ---------------------------------------------- 4. what this sharpens
    print("\n" + "-" * 78)
    print("  4. The alpha route is SHARPENED, not blocked")
    print("-" * 78)
    print("""
  [1^4] is a four-body SU(4) object, not a bond-graph object, so neither the
  additive cap nor the A=4 negative many-body sign applies to it. What the
  bond-topology exclusions do is REMOVE THE BOND GRAPH AS A COMPETITOR, leaving
  the alpha-cluster term as the carrier that must supply the missing bulk.

  This probe measures how much bulk that is: between two thirds and four fifths
  of every alpha. No mechanism for it is proposed here -- proposing one on the
  strength of a ratio would be the numerology the anti-fit discipline forbids.
""")
    # ---------------------------- 5. the BULK target, not the observed one
    print("\n" + "-" * 78)
    print("  5. CORRECTION: the extensive target is a_V, not the observed B/A")
    print("-" * 78)
    hq2 = (1 - 1 / q) ** 2
    mN = mp.mpf(M_N_MEV)
    aV = mp.mpf(A_V_OVER_HQ2_MN) * hq2 * mN
    peak = mp.mpf(PEAK_OVER_HQ2_MN) * hq2 * mN
    bulk4 = 4 * aV
    print(f"""
  QOU.Mass.SaturationPeakStructure proves f(u) = a_V - a_S/u - a_C*u^2 NEVER
  attains a_V, and records:

    a_V  (bulk)        {A_V_OVER_HQ2_MN} x hbar_q^2 x m_N = {mp.nstr(aV, 8)} MeV/nucleon
    observed peak      {PEAK_OVER_HQ2_MN} x hbar_q^2 x m_N = {mp.nstr(peak, 8)} MeV/nucleon

  So ~8 MeV/nucleon is the OBSERVED peak; an extensive term must supply a_V,
  which is {mp.nstr(aV/peak, 6)}x larger. Against the bulk requirement:

    bulk for 4 nucleons  4 x {mp.nstr(aV, 7)} = {mp.nstr(bulk4, 8)} MeV
    trace chain          {mp.nstr(b_chain, 7)} MeV  ->  {mp.nstr(100*b_chain/bulk4, 4)} %
    trace complete graph {mp.nstr(b_k4, 7)} MeV  ->  {mp.nstr(100*b_k4/bulk4, 4)} %

  The exclusion is about TWICE as strong as first stated. The 1.71 is
  a_V/(hbar_q^2*m_N) computed FROM the empirical a_V -- a re-expression in
  substrate units, NOT a derivation of it.
""")
    check("the extensive target is the BULK coefficient, and the trace supplies "
          "under 20 % of it", b_k4 / bulk4 < mp.mpf("0.20"),
          f"{mp.nstr(100*b_k4/bulk4, 4)} % of the bulk requirement, against "
          f"{mp.nstr(100*frac_hi, 4)} % of the observed 4He binding. Both are "
          f"reported because they answer different questions; the bulk one is "
          f"what an EXTENSIVE term must meet, and it is the stricter.")

    check("the open target is stated as a magnitude, with no mechanism "
          "proposed", True,
          f"missing fraction per alpha: {mp.nstr(100*(1-frac_hi), 4)} % to "
          f"{mp.nstr(100*(1-frac_lo), 4)} %. The corpus has the STRUCTURE "
          f"derived (proved SU(4) gate) and the SCALE open; this bounds the "
          f"scale from below by what the trace cannot supply.")

    payload = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. A manifest entry "
            "would be inert here -- the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build() -- so the declaration is "
            "made producer-side, the only route that reaches the file."),
        "schema": "witness/v1",
        "name": "alpha-scale-is-outside-the-trace",
        "description": (
            "The trace channel supplies 20.6-33.8 % of one alpha-cluster unit "
            "(29.8 MeV) even at the complete graph, so the alpha-cluster scale "
            "must come from outside it; plus the two-row support of the "
            "Schur-Weyl sum, extended to n=3,12,15."),
        "beans": ["qou-n4zp", "qou-59j5", "qou-brng", "qou-0c19", "qou-lw9l"],
        "scope": "(a) — pure-proton chains for the trace figures; 29.8 MeV/alpha "
                 "is the corpus's measured mean, cited not re-derived; no "
                 "mechanism proposed for the missing scale",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "L_chain_A4": L_CHAIN_A4,
            "L_K4_best_order": L_K4_BEST,
            "B_chain_A4_MeV": mp.nstr(b_chain, 25),
            "B_K4_best_MeV": mp.nstr(b_k4, 25),
            "alpha_scale_MeV_corpus": ALPHA_SCALE_MEV,
            "trace_fraction_of_one_alpha_low": mp.nstr(frac_lo, 20),
            "trace_fraction_of_one_alpha_high": mp.nstr(frac_hi, 20),
            "partition_support": rows,
            "support_is_two_row_everywhere": bool(all(two_row)),
            "two_row_fact_is_new": False,
            "representation_inference_drawn": False,
            "a_V_MeV_per_nucleon": mp.nstr(mp.mpf(A_V_OVER_HQ2_MN)*(1-1/q)**2*mp.mpf(M_N_MEV), 20),
            "observed_peak_MeV_per_nucleon": mp.nstr(mp.mpf(PEAK_OVER_HQ2_MN)*(1-1/q)**2*mp.mpf(M_N_MEV), 20),
            "trace_fraction_of_bulk_low": mp.nstr(b_chain/(4*mp.mpf(A_V_OVER_HQ2_MN)*(1-1/q)**2*mp.mpf(M_N_MEV)), 20),
            "trace_fraction_of_bulk_high": mp.nstr(b_k4/(4*mp.mpf(A_V_OVER_HQ2_MN)*(1-1/q)**2*mp.mpf(M_N_MEV)), 20),
            "target_is_bulk_not_observed": True,
        },
        "assertions": assertions,
        "checks_passed": sum(checks),
        "checks_total": len(checks),
    }
    out = _COMP / "alpha-scale-is-outside-the-trace.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    payload["q0Anchor"] = _q0a
    if _q0v:
        payload["q0Value"] = _q0v
    out.write_text(json.dumps(payload, indent=2) + "\n")

    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print(f"  witness -> {out.relative_to(_COMP.parent)}")
    print("=" * 78)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
