#!/usr/bin/env python3
"""A1 / bean `qou-78pt` — is the un-normalised-trace option a fit, or is it refuted?

⚠ WITHDRAWN 2026-08-31 — THE VERDICT BELOW ("A1 REFUTED") DOES NOT STAND
------------------------------------------------------------------------
The refutation rests on one comparison: the convention family spans 1.33x while
the deficit is 6x-15x, "two orders of magnitude too small to be the thing that
closes the gap". **The deficit figure was an energy-scale artifact.**

This probe multiplies its dimensionless logs by `m_e = 0.511 MeV`, with no reason
given. The corpus's binding machinery uses the hadronic energy unit
`E_0 = m_e/(q_0(q_0-1)) = 4.18598 MeV` — `b_over_a_evaluator.py`, the `B_sym`
linear chain (`alpha = E_0`, CAL-1), and the ROAST's own `E_0 log N`. At `E_0`:

    family:            8.722 ... 11.597 MeV/nucleon   (was 1.065 ... 1.416)
    vs B/A plateau 8.5:  every member is OVER          (was 6.0x-8.0x short)
    vs a_V 15.8:       1.36x ... 1.81x short           (was 11x-15x short)
    span:              1.33x  —  now the SAME SIZE as the deficit

So the argument inverts. When the span is comparable to the gap, choosing the
member that lands on `a_V` **is** a fit — which is exactly what the ROAST charged
and what this probe claimed to have disposed of. **A1 returns to
"unfalsifiable as written", and pinning the normalisation from the axioms is
again the actual work.** See
`computations/probes/extensive_term_energy_scale_reconciliation_probe.py`.

The section "A NUMBER I COULD NOT REPRODUCE" below is also resolved: the ROAST's
2.91 MeV/strand is `E_0`-scaled, and `2.91/E_0 = 0.6952` is `ln 2` to 0.3 % —
the ROAST's own stated construction. At `m_e` the figure is *unreachable*: it
would need a normaliser with `log = 5.69`, against a family whose logs span
0.694-0.923. My inability to reproduce it was the tell, and I logged it as an
open discrepancy instead of chasing it.

What survives untouched: the framing factor `(1+q^2)/(q+1/q) = q` (exact, a
ratio, scale-free), and the *discreteness* of the convention family.

THE CHARGE
----------
`docs/audits/2026-08-07-l2-attack-options-ROAST.md` §A1 rules attack A1
("the extensive term is the Markov normalisation we divide out")
**unfalsifiable as written**:

    "Just don't normalize" is not a well-defined instruction — it is a
    one-parameter family. Kauffman bracket, Ocneanu/Markov trace, and the
    HOMFLY specialization differ by factors of (−q^{1/2}−q^{−1/2}) and by
    writhe-dependent a^{−w} terms. Each gives a different extensive
    coefficient. Choosing the member that lands on a_V ≈ 15.6 IS a fit.

and concludes that pinning the convention from the axioms is "the actual work;
everything else is downstream".

WHAT THIS PROBE FINDS
---------------------
Pinning is not required, because the charge does not survive measurement. The
convention family is **discrete and narrow**, and **no member reaches the
target** — so there is nothing to fit.

1. The two leading candidates differ by **exactly one factor of `q` per strand**:

       (1 + q²) / (q + q⁻¹) = q          [assertion 1, exact]

   That is the framing/writhe factor the ROAST names. It is one discrete step,
   not a free continuous parameter.

2. Across every normaliser the family offers — `[2]_q`, `[2]_{q²}`, the
   Kauffman variable `q^{1/2}+q^{-1/2}`, the bracket `δ`, and an over-shoot
   control — the extensive coefficient spans

       1.065 … 1.416 MeV/nucleon   (a factor of **1.33**)

   against a deficit of **6.0×–8.0×** versus the `B/A` plateau and
   **11×–15×** versus `a_V`. The freedom is two orders of magnitude too small
   to be the thing that closes the gap.

3. What closure would actually require, at 3 strands/nucleon: a loop value of
   ≈ 256 (the family offers ≈ 2.0–2.5), or ≈ 21 strands per nucleon (the corpus
   fixes 3, from `n_strands = 12` at ⁴He). Neither is a convention.

So A1 is **falsifiable after all, and it fails** — uniformly over the family,
not at a chosen member. That is a stronger outcome than "unfalsifiable": it
closes the option instead of parking it.

A NUMBER I COULD NOT REPRODUCE
------------------------------
The ROAST reports "the N=2 reading gives ~2.91 MeV/strand". Every member of the
family measured here gives 0.355–0.472 MeV/strand — 6–8× smaller. The ROAST does
not show its construction and this probe does not reconstruct it. Recorded as an
unreconciled discrepancy rather than silently overridden; if 2.91 is right, the
conclusion here strengthens (the deficit shrinks but the *span* argument is
unchanged, since span is a ratio).

Usage:
    python3 computations/probes/markov_normalisation_convention_span_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

M_E_MEV = mp.mpf("0.51099895069")   # CODATA
STRANDS_PER_NUCLEON = 3             # corpus: n_strands = 12 at ⁴He
B_OVER_A_PLATEAU = mp.mpf("8.5")    # MeV/nucleon, empirical
SEMF_A_V = mp.mpf("15.8")           # MeV, semi-empirical mass formula


def main() -> int:
    q = Q_MP
    Q_NUM = q  # local alias used in the scale-qualified assertion source below
    w = WitnessBuilder("markov-normalisation-convention-span-probe")
    w.set_description(
        "A1/qou-78pt: measures the span of the Markov-normalisation convention family "
        "against the extensive-term deficit. The family is discrete and 1.33x wide. "
        "VERDICT WITHDRAWN 2026-08-31: the 6-15x deficit was an m_e-vs-E_0 energy-scale "
        "artifact; at E_0 the deficit is 1.36-1.81x, the same size as the span, so A1 "
        "reverts to unfalsifiable-as-written. See the SCALE_CORRECTION data block."
    )

    # ---- assertion 1: the framing step is exactly one factor of q -----------
    framing = (1 + q ** 2) / (q + 1 / q)
    w.add_assertion(
        "framing_factor_between_normalisers_is_q",
        computed=mp.nstr(framing, 30),
        expected=mp.nstr(q, 30),
        tolerance="1e-35",
        source="ratio of the corpus partition-function normaliser (1+q^2) to the unframed "
               "loop value [2]_q, vs the substrate constant q0 read from q_parameter",
    )

    # ---- the family ---------------------------------------------------------
    family = {
        "[2]_q = q + 1/q (unframed Jones/TL loop)": q + 1 / q,
        "[2]_Q = 1 + q^2 (corpus partition function)": 1 + q ** 2,
        "q^(1/2) + q^(-1/2) (Kauffman variable)": mp.sqrt(q) + 1 / mp.sqrt(q),
        "|-q^(1/2) - q^(-1/2)| (Kauffman bracket delta)": abs(-mp.sqrt(q) - 1 / mp.sqrt(q)),
        "1 + q^4 (over-shoot control)": 1 + q ** 4,
    }
    rows, per_nucleon_vals = [], []
    for name, delta in family.items():
        per_strand = mp.log(delta) * M_E_MEV
        per_nucleon = per_strand * STRANDS_PER_NUCLEON
        per_nucleon_vals.append(per_nucleon)
        rows.append({
            "normaliser": name,
            "loop_value": mp.nstr(delta, 15),
            "MeV_per_strand": mp.nstr(per_strand, 12),
            "MeV_per_nucleon_at_3_strands": mp.nstr(per_nucleon, 12),
        })
    lo, hi = min(per_nucleon_vals), max(per_nucleon_vals)

    # ---- assertion 2: no member reaches the plateau -------------------------
    none_reaches = hi < B_OVER_A_PLATEAU
    w.add_assertion(
        "no_convention_member_reaches_B_over_A_plateau_AT_THE_m_e_SCALE",
        computed="1" if none_reaches else "0",
        expected="1",
        source=f"max over the family is {mp.nstr(hi, 8)} MeV/nucleon AT m_e; the empirical "
               f"B/A plateau is {B_OVER_A_PLATEAU} MeV/nucleon (independent: nuclear data). "
               f"⚠ The scale qualifier is not cosmetic: at the corpus's own E_0 the same "
               f"family gives {mp.nstr(hi * (_qbeta_e0.order_zero_scaled(1, Q_NUM)), 8)} MeV/nucleon at "
               f"its maximum and every member CLEARS the plateau, which is why this "
               f"probe's verdict is withdrawn.",
    )

    w.add_parameter("q0", mp.nstr(q, 30))
    w.add_parameter("strands_per_nucleon", STRANDS_PER_NUCLEON)
    w.add_data("family", rows)
    w.add_data("span", {
        "min_MeV_per_nucleon": mp.nstr(lo, 12),
        "max_MeV_per_nucleon": mp.nstr(hi, 12),
        "span_ratio": mp.nstr(hi / lo, 8),
        "deficit_vs_plateau": f"{mp.nstr(B_OVER_A_PLATEAU / hi, 6)}x .. {mp.nstr(B_OVER_A_PLATEAU / lo, 6)}x",
        "deficit_vs_a_V": f"{mp.nstr(SEMF_A_V / hi, 6)}x .. {mp.nstr(SEMF_A_V / lo, 6)}x",
        "verdict": "span (1.33x) is two orders of magnitude smaller than the deficit (6-15x)",
    })

    # what closure would require — neither quantity is a convention
    req_loop = mp.e ** (B_OVER_A_PLATEAU / (STRANDS_PER_NUCLEON * M_E_MEV))
    req_strands = B_OVER_A_PLATEAU / (mp.log(1 + q ** 2) * M_E_MEV)
    w.add_data("what_closure_would_require", {
        "loop_value_at_3_strands": mp.nstr(req_loop, 8),
        "family_offers": f"{mp.nstr(min(family.values()), 6)} .. {mp.nstr(max(family.values()), 6)}",
        "strands_per_nucleon_at_corpus_normaliser": mp.nstr(req_strands, 8),
        "corpus_fixes": STRANDS_PER_NUCLEON,
    })
    # ---- the scale correction, and the withdrawal it forces -----------------
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(M_E_MEV, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    lo_e0, hi_e0 = lo * e0 / M_E_MEV, hi * e0 / M_E_MEV
    w.add_data("SCALE_CORRECTION_2026_08_31_VERDICT_WITHDRAWN", {
        "what_is_wrong": "Every MeV figure here uses m_e as the energy scale, unjustified. "
                         "The corpus's binding machinery uses E_0 = m_e/(q_0(q_0-1)).",
        "E_0_MeV": mp.nstr(e0, 20),
        "scale_ratio": mp.nstr(e0 / M_E_MEV, 20),
        "corrected_family_MeV_per_nucleon":
            f"{mp.nstr(lo_e0, 8)} .. {mp.nstr(hi_e0, 8)}",
        "corrected_vs_plateau":
            f"{mp.nstr(lo_e0 / B_OVER_A_PLATEAU, 6)}x .. "
            f"{mp.nstr(hi_e0 / B_OVER_A_PLATEAU, 6)}x OVER (every member clears 8.5)",
        "corrected_vs_a_V":
            f"{mp.nstr(SEMF_A_V / hi_e0, 6)}x .. {mp.nstr(SEMF_A_V / lo_e0, 6)}x short",
        "span_unchanged": mp.nstr(hi / lo, 6),
        "why_the_verdict_falls": (
            "The refutation was 'span 1.33x vs deficit 6-15x, two orders of magnitude too "
            "small'. Corrected, the deficit against a_V is 1.36-1.81x and the span is "
            "1.33x -- the SAME SIZE. That is precisely the condition under which picking a "
            "member is a fit, i.e. the ROAST's original charge. A1 REVERTS to "
            "'unfalsifiable as written'; pinning the convention from the axioms is again "
            "the actual work."
        ),
        "see": "computations/probes/extensive_term_energy_scale_reconciliation_probe.py",
    })
    w.add_data("unreconciled_RESOLVED_2026_08_31", {
        "roast_claim_MeV_per_strand": "2.91",
        "resolution": ("E_0-scaled, not m_e-scaled. 2.91/E_0 = "
                       + mp.nstr(mp.mpf("2.91") / e0, 8) + ", which is ln 2 = "
                       + mp.nstr(mp.log(2), 8) + " to 0.3% -- the ROAST's own stated "
                       "construction 'the extensive coefficient is E_0 log N' at N = 2. "
                       "At m_e the figure is UNREACHABLE: it would need a normaliser with "
                       "log = " + mp.nstr(mp.mpf("2.91") / M_E_MEV, 6) + ", against a family "
                       "whose logs span 0.694-0.923. Failing to reproduce it was the tell; "
                       "I logged it as open instead of chasing it."),
    })
    w.add_data("unreconciled_ORIGINAL_TEXT_kept_for_the_record", {
        "roast_claim_MeV_per_strand": "2.91",
        "this_probe_range_MeV_per_strand":
            f"{mp.nstr(min(mp.log(d) * M_E_MEV for d in family.values()), 6)} .. "
            f"{mp.nstr(max(mp.log(d) * M_E_MEV for d in family.values()), 6)}",
        "note": "6-8x apart; the ROAST does not show its construction and this probe does "
                "not reconstruct it. The span argument is a ratio and is unaffected either way.",
    })
    w.add_data("verdict", (
        "[WITHDRAWN 2026-08-31 -- see SCALE_CORRECTION block. Kept verbatim so the "
        "retraction has something to point at.] A1 REFUTED, not unfitted. The ROAST called the option unfalsifiable because "
        "'do not normalise' is a convention family and choosing the member that lands on "
        "a_V would be a fit. Measured, the family is DISCRETE (the two leading members "
        "differ by exactly one factor of q) and spans 1.33x, while the deficit is 6-15x. "
        "No member lands on a_V, so there is no fit available -- the option fails uniformly "
        "over the family. Pinning the convention from the axioms, which the ROAST called "
        "'the actual work', is therefore not needed to dispose of A1."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  framing factor (1+q^2)/(q+1/q) == q   : {abs(framing - q) < mp.mpf('1e-35')}")
    print(f"  family span (3 strands/nucleon)       : {mp.nstr(lo, 6)} .. {mp.nstr(hi, 6)} MeV/nucleon "
          f"({mp.nstr(hi / lo, 4)}x)")
    print(f"  deficit vs B/A plateau                : {mp.nstr(B_OVER_A_PLATEAU / hi, 4)}x .. "
          f"{mp.nstr(B_OVER_A_PLATEAU / lo, 4)}x")
    print(f"  required loop value to close          : {mp.nstr(req_loop, 6)} (family offers ~2.0-2.5)")
    print(f"  required strands/nucleon to close     : {mp.nstr(req_strands, 6)} (corpus fixes 3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
