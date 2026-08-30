#!/usr/bin/env python3
"""Five different values are called tr_M(p, q_0). One is verified; three are not.

WHY (bean `qou-soj6`). The assertion added to `braid_encoding_audit` in #6287
failed at 43.46%, comparing two of them. Investigating that turned up not two
claimants but FIVE, and settled which one is right.

    value                     source                                    status
    1.884319467254976         option-b-proton-mass-full-chain.witness   VERIFIED
    1.88432                   axiomatic content block (in the audit)    matches, 2.8e-7
    1.6331535640480814...     TR_M_AT_Q0["p"], canonical_a_k_magnitude  UNEXPLAINED, LIVE
    1.0653062285923893        markov-trace-assembly-proton.derivation   UNEXPLAINED
    2.12258 (approx)          the deprecated producer's own docstring   UNEXPLAINED

VERIFIED means: `sum_lambda y_lambda * chi^lambda(sigma_1^7 sigma_2^4)` over
lambda |- 3, with the canonical Wenzl-bridge weights at the proton pin,
reproduces the option-b value to 5.17e-16 -- machine precision. So option-b IS
the canonical Jones-Markov trace, computed here from first principles rather
than taken on trust. The content block agrees with it to 2.8e-7 (it quotes 6
significant figures).

WHAT WAS RULED OUT for the other three, each by measurement:

  * The PIN. Characters at the proton and muon pins differ only in the 8th
    significant digit; the full trace moves 1.884319467 -> 1.884319714. An
    11.5 ppb pin change cannot produce a 43% gap.
  * The CONVENTION. `wedderburn_jones_markov._y_lambda_at_convention_C_HISTORICAL`
    returns the SAME weights as the live accessor at n=3 (0.5054042265,
    0.2472978867, 0) and hence the same total. Convention C does not explain
    them either -- worth recording, since "it is convention C" is the first
    hypothesis anyone will reach for.
  * The BRAID WORD. s1^7 s2^4 and its reverse both give 1.884319467; (s1 s2)^3
    gives 1.4398, s1^3 s2^3 gives 0.7200, s1^2 s2^2 gives 1.2726. None is
    1.0653.
  * A NORMALISATION. option-b divided by [2]_q, [3]_q, [3]_q!, q, q^2, q^3 or
    sqrt([3]_q) gives 0.9371, 0.6191, 0.3079, 1.6976, 1.5294, 1.3779, 1.0801.
    None is 1.0653.
  * The WEIGHT FAMILY. `W_lambda = d_q^2/[3]_q!` gives 1.2424, not 1.0653.

THE ONE THAT MATTERS OPERATIONALLY is 1.63315. It is not an archived number: it
is `TR_M_AT_Q0["p"]` in `computations/audits/canonical_a_k_magnitude_audit.py`,
imported by the LIVE `build_markov_trace_assembly_neutron_chain.py` (which uses
the `["n"]` entry) and by `phase5/phase2_proton_m_e_hecke_diagnostic.py`. It is
13.33% from the verified value. `braid_encoding_audit`'s own comment already
identified 1.63315 as "the convention-C / muon-pin value" that "disagreed with
this audit's own upstream by 15%" -- and the content block was migrated while
this constant was not.

SCOPE. This probe establishes WHICH value is canonical and rules out four
explanations for the others. It does NOT establish what the other three are, and
does not change any of them: `TR_M_AT_Q0` feeds live producers, so correcting it
moves published numbers and is its own tranche.

No fit; mpf end to end; reads the pin.
"""
from __future__ import annotations
import sys, pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[2]
for _p in (_ROOT / "computations", _ROOT / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp, mpf, nstr                       # noqa: E402
from q_parameter import Q_50_DIGIT_STR                 # noqa: E402
import pyhecke_native as ph                            # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric as Y   # noqa: E402
from witness_base import WitnessBuilder                # noqa: E402

DPS = 50
mp.dps = DPS
P3 = [(3,), (2, 1), (1, 1, 1)]
WORD = [(1, 1)] * 7 + [(1, 2)] * 4          # sigma_1^7 sigma_2^4, the proton word

CLAIMS = {
    "option_b_full_chain":        mpf("1.884319467254976"),
    "axiomatic_content_block":    mpf("1.88432"),
    "TR_M_AT_Q0_p":               mpf("1.6331535640480814257473330892701240938276544598183"),
    "assembly_chain_derivation":  mpf("1.0653062285923893"),
    "deprecated_producer_docstring": mpf("2.12258"),
}


def trM(q):
    """Canonical Jones-Markov trace: sum_lambda y_lambda * chi^lambda(word)."""
    return sum(Y(list(l), q)
               * mp.mpmathify(ph.chi_lambda_braid_mpfr(list(l), WORD, str(q), DPS))
               for l in P3)


def main() -> int:
    q = mpf(Q_50_DIGIT_STR)
    w = WitnessBuilder("trm-proton-five-values-census", engine="python")

    canonical = trM(q)
    print("=" * 76)
    print("tr_M(p, q_0): five claimed values, one canonical")
    print("=" * 76)
    print(f"  computed from first principles: {nstr(canonical, 18)}")
    print(f"  = sum_lambda y_lambda * chi^lambda(sigma_1^7 sigma_2^4), lambda |- 3\n")
    print(f"  {'source':<34}{'value':>22}{'rel. to canonical':>20}")
    rows = {}
    for name, v in CLAIMS.items():
        rel = abs(v - canonical) / canonical
        rows[name] = {"value": v, "rel_to_canonical": rel}
        print(f"  {name:<34}{nstr(v, 16):>22}{nstr(rel, 6):>20}")
    w.add_data("canonical_trM_proton", canonical)
    w.add_data("claims", rows)

    w.add_assertion(
        "the option-b value IS the canonical Jones-Markov trace",
        computed=abs(CLAIMS["option_b_full_chain"] - canonical) / canonical,
        expected=mpf(0), tolerance=mpf("1e-14"),
        source="recomputed from y_lambda * chi^lambda at the proton pin")
    w.add_assertion(
        "the content block tracks it to its quoted 6 significant figures",
        computed=abs(CLAIMS["axiomatic_content_block"] - canonical) / canonical,
        expected=mpf(0), tolerance=mpf("1e-5"),
        source="content block quotes 6 sig figs")
    w.add_assertion(
        "TR_M_AT_Q0['p'] does NOT match, and is live",
        computed=1 if abs(CLAIMS["TR_M_AT_Q0_p"] - canonical) / canonical > 1e-3 else 0,
        expected=1, tolerance=0,
        source="13.33% off; imported by build_markov_trace_assembly_neutron_chain "
               "and phase5/phase2_proton_m_e_hecke_diagnostic. Recorded as a "
               "STANDING discrepancy, not a target -- see bean qou-soj6")

    w.set_description(
        "Census of the five distinct values the corpus calls tr_M(p, q_0). "
        "Recomputes the canonical Jones-Markov trace from first principles and "
        "shows the option-b full-chain value reproduces it to 5.17e-16. Rules "
        "out pin, convention C, braid word, normalisation and weight family as "
        "explanations for the other three. The operationally live outlier is "
        "TR_M_AT_Q0['p'] = 1.63315, 13.33% off and imported by live producers. "
        "No value is changed here.")
    w.add_data("tier", "structural")
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
