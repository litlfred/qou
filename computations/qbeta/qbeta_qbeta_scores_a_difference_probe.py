"""🛑 RETRACTION. The Q_beta functional eats a DIFFERENCE of two words, so a
lower bound on each word's trace does not bound it — and two probes on this
branch, both mine, inferred exactly that.

# Ref: computations/qbeta/qbeta_option_e_required_level_probe.py::delta_of --
#      "Delta = neutron - proton, coordinatewise in the NF basis"
# Ref: computations/qbeta/qbeta_gamma_gamma_trace_ge_one_probe.py -- the tr >= 1
#      bound, which is CORRECT and whose Q_beta inference is retracted here
# Ref: computations/qbeta/qbeta_gamma_gamma_psd_trace_floor_probe.py -- same
#      defect, one bound earlier
# Ref: AGENTS.md §"Terse != compressed" -- a correction says what else it
#      contaminated, not merely that it happened

WHAT I ASSERTED.  That `tr_M(w) >= 1` for every PSD-feasible gamma-gamma word
means "the gamma-gamma + confinement-SDP route cannot reproduce Q_beta at ANY
strand count", and that "the smallest Q_beta this family can predict is exactly
E_0 = 4.2274834 MeV, +440.369 %".

WHAT IS ACTUALLY TRUE.  `Q_beta = |eps(Delta)| * E_0` where
**`Delta` is the NEUTRON element MINUS the PROTON element** — the source says so
in as many words (`delta_of`'s docstring) and the arithmetic confirms it to 25
digits below.  The Markov trace is **linear**, so

    tr(Delta) = tr(neutron word) - tr(proton word),

and two quantities each bounded below by 1 have a difference bounded by
nothing at all.  The exclusion does not follow, and I withdraw it.

HOW IT WAS CAUGHT — by the calibration step, which is the whole reason that
step exists.  Reconstructing `nuc11_interleaved` letter by letter gave
`tr = 0.6293284022029219` for the proton and `0.4751335171556822` for the
neutron, and neither matched the census witness's recorded
`tr_conv_D = -0.1541948850472397056592555`.  Their **difference** matches it
exactly, to every recorded digit.  Had the probe scored a single word and
skipped the calibration, the mismatch would never have surfaced.

WHAT IS CONTAMINATED, so it can be fixed rather than discovered later:

* `qbeta_gamma_gamma_trace_ge_one_probe.py` — its description and the
  `Q_beta_is_excluded_at_every_strand_count` assertion.
* `qbeta_gamma_gamma_psd_trace_floor_probe.py` — the same inference one bound
  earlier ("no gamma-gamma + SDP word on five strands or fewer can reproduce
  Q_beta").
* `qbeta_gamma_gamma_qbeta_prediction_probe.py` — subtler and still wrong: it
  scored each feasible word ALONE as a Q_beta prediction (+458 % to +620 %).
  That is not the scoring path either.  Those numbers are what you get if a
  single word is the functional's argument, and it is not.
* `QOU/Archimedean/GammaGammaTraceFloor.lean` — the docstring's framing, not
  the theorems, which are about pairings and say nothing about Q_beta.
* Beans `qou-99qc` parts 9 and 10, and the PR body.

WHAT SURVIVES UNTOUCHED, because it was measured rather than inferred:

* `tr_M(w) >= 1` for every individual PSD-feasible gamma-gamma word, tight at
  the empty word.  All four ingredients stand — the det-1 fact (1e-39 over 590
  (word, block) pairs), AM-GM, weight non-negativity, the Markov normalisation.
* The `[n+1]_q/[2]_q^n` floor and its strict decay.
* Every Lean theorem on this branch: they are statements about Frobenius
  pairings and PSD matrices, and none of them mentions Q_beta.
* The crossing-energy results.

WHAT THE DIFFERENCE FUNCTIONAL ACTUALLY GIVES.  Reported in full — all 15
pairs from the six-element feasible set — because reporting only the closest
would be the selection-against-the-target AGENTS.md bans.  The predictions run
from -100 % to +79.4 %; they STRADDLE the target rather than sitting above it,
which is the opposite of what the retracted claim said.  The best is +5.15 %,
against an expected-best-by-chance of **7.73 %** for a grid this coarse — the
same order, so it is not evidence either.

AND ONE MEASUREMENT SURVIVES AND IS NEW: the scored element's proton and
neutron words are **both PSD-INFEASIBLE**, two of three blocks each, and carry
`det != 1` in every block.

🛑 SCOPED 2026-09-13, after the first draft of this file called that "the SDP
half of the ruling excludes the scored element".  It does not.  The SDP scope
question was answered **"(A) core only"** (bean `qou-99qc`, 2026-09-12), under
which reading 3 constrains the 6 gamma-gamma letters and prunes nothing among
the other 5 — and under (A), in that entry's own words, "the census element
stands".  Whole-element PSD is reading (B), which was NOT selected.  So this is
a measurement about the element, not a rejection of it by the ruling.  The
alternating-character exclusion already on record is separate and unaffected.
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import qbeta_e0  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402

_OC = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_ocneanu_trace_general_n_probe.py")
_spec = importlib.util.spec_from_file_location("_oc", _OC)
_oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_oc)

_FE = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_gamma_gamma_sdp_feasibility_probe.py")
_spec2 = importlib.util.spec_from_file_location("_fe", _FE)
_fe = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(_fe)

set_compute_dps(60)
mp.mp.dps = 40

H0 = _oc.H0
Q = mp.mpf(str(_oc.Q0))
HR = sp.Rational(str(H0))
ZR = sp.Rational(str(_oc.ZD))

#: the census witness's recorded value for the scored element, verbatim.
RECORDED_TR_CONV_D = "-0.1541948850472397056592555"

#: `nuc11_interleaved` letter by letter, as `(generator, shift-in-units-of-h)`.
#: `hm(nf, ONE, d, g)` multiplies by `sigma_g + d`, so `-1` is `sigma^-1`.
CORE = [(0, 0), (1, -1)] * 3                    # the gamma-gamma Borromean core
QUARK = {
    "p": [(0, 0), (0, mp.mpf("-0.5")), (1, mp.mpf("-0.5"))],
    "n": [(0, mp.mpf("-0.5")), (0, mp.mpf("-0.5")), (1, -1)],
}
GLUON = [(0, 0), (0, 0)]

#: the PSD-feasible gamma-gamma words at n = 4, MEASURED by #7295.
FEASIBLE = [
    ((), "empty"),
    ((0, 1, 0, 1), "(v0 v1)^2"),
    ((0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^4"),
    ((0, 0, 1, 1, 0, 1, 1, 0, 0, 1), "sporadic A"),
    ((0, 1, 1, 0, 0, 1, 0, 0, 1, 1), "sporadic B"),
    ((0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^6"),
]

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def qint(m: int):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def y_lambda(n: int, lam) -> mp.mpf:
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(n - 2 * k + 1) / qint(2) ** n


def nucleon_blocks(kind: str):
    """`rho_lambda(nuc11_interleaved(kind))` per H_3 block."""
    letters = CORE + QUARK[kind] + GLUON
    out = {}
    for shape, (sig, dim) in _fe.blocks(3).items():
        M = mp.eye(dim)
        for g, d in letters:
            M = M * (sig[g] + (mp.mpf(str(d)) * H0) * mp.eye(dim))
        out[shape] = (M, dim)
    return out


def nucleon_trace(kind: str) -> mp.mpf:
    return sum(y_lambda(3, s) * sum(M[j, j] for j in range(dim))
               for s, (M, dim) in nucleon_blocks(kind).items())


def gg_trace(combo, n: int = 4) -> mp.mpf:
    lets: list = []
    for i in combo:
        lets += [(i, sp.Integer(0)), (i + 1, -HR)]
    return mp.mpf(str(sp.N(
        _oc.tr(_oc.word_to_vec(lets, n, {}, HR), n, HR, ZR), 35)))


def main() -> int:
    w = WitnessBuilder("qbeta-qbeta-scores-a-difference")
    w.set_description(
        "RETRACTION. Q_beta = |eps(Delta)|*E_0 with Delta = NEUTRON word MINUS "
        "PROTON word (delta_of's own docstring, confirmed to 25 digits here), "
        "and the Markov trace is linear -- so the tr_M >= 1 bound on individual "
        "PSD-feasible gamma-gamma words does NOT bound the scored quantity, and "
        "the 'cannot reproduce Q_beta at any strand count' inference drawn from "
        "it on this branch is withdrawn. The bound itself, the floor, and every "
        "Lean theorem stand: they are about pairings and PSD matrices and none "
        "mentions Q_beta. Caught by the calibration step. What the difference "
        "functional actually gives, all 15 pairs reported: -100 % to +79.4 %, "
        "STRADDLING the target rather than sitting above it, best +5.15 % "
        "against 7.73 % expected by chance. Surviving new MEASUREMENT: the "
        "scored element's proton and neutron words are both PSD-INFEASIBLE (2 "
        "of 3 blocks) with det != 1 everywhere -- which is reading (B), NOT a "
        "rejection by the ruling, whose scope answer was '(A) core only'."
    )

    E0 = qbeta_e0.canonical()
    qb = mp.mpf(str(Q_BETA_MEV))
    target = qb / E0

    # ---- 1. the calibration that caught it ---------------------------------
    tp = nucleon_trace("p")
    tn = nucleon_trace("n")
    diff = tn - tp
    rec = mp.mpf(RECORDED_TR_CONV_D)
    print(f"  tr(proton word)  = {mp.nstr(tp, 22)}")
    print(f"  tr(neutron word) = {mp.nstr(tn, 22)}")
    print(f"  tr(n) - tr(p)    = {mp.nstr(diff, 22)}")
    print(f"  recorded         = {RECORDED_TR_CONV_D}")
    print()
    check("the_scored_value_is_a_DIFFERENCE_of_two_word_traces",
          abs(diff - rec) < mp.mpf("1e-24")
          and abs(tp - rec) > mp.mpf("0.1") and abs(tn - rec) > mp.mpf("0.1"),
          f"reconstructing nuc11_interleaved letter by letter gives "
          f"tr(p) = {mp.nstr(tp, 18)} and tr(n) = {mp.nstr(tn, 18)}; NEITHER "
          f"matches the census witness's tr_conv_D = {RECORDED_TR_CONV_D}, and "
          f"their DIFFERENCE matches it to {mp.nstr(abs(diff - rec), 4)}. "
          f"delta_of's docstring says so independently: 'Delta = neutron - "
          f"proton, coordinatewise in the NF basis'", w)

    # ---- 2. so a per-word lower bound does not bound it ---------------------
    check("a_lower_bound_on_each_word_does_NOT_bound_their_difference",
          True,
          f"tr is linear, so tr(Delta) = tr(n) - tr(p). Two quantities each "
          f">= 1 have a difference bounded by nothing. The inference drawn on "
          f"this branch -- that tr_M >= 1 per PSD-feasible gamma-gamma word "
          f"excludes Q_beta at every strand count -- does not follow and is "
          f"WITHDRAWN. Asserted as a check so the retraction is machine-"
          f"recorded rather than living only in prose", w)

    # ---- 3. what the difference functional gives, ALL of it ----------------
    vals = {lab: gg_trace(c) for c, lab in FEASIBLE}
    pairs = []
    for (a, va), (b, vb) in itertools.combinations(vals.items(), 2):
        d = abs(va - vb)
        pairs.append((a, b, d, d * E0, (d * E0 - qb) / qb * 100))
    print("  every pair of the PSD-feasible set, as |tr(n-word) - tr(p-word)|:")
    for a, b, d, pred, pct in pairs:
        print(f"    |{a:11s} - {b:11s}| = {mp.nstr(d, 12):>16s}  "
              f"{mp.nstr(pred, 10):>14s} MeV  {mp.nstr(pct, 7):>11s} %")
    print()
    pcts = [p for *_, p in pairs]
    check("the_difference_predictions_STRADDLE_the_target",
          min(pcts) < 0 < max(pcts),
          f"all {len(pairs)} pairs of the six-element feasible set run from "
          f"{mp.nstr(min(pcts), 7)} % to {mp.nstr(max(pcts), 7)} % -- they "
          f"straddle the measurement rather than sitting above it, which is the "
          f"opposite of what the retracted claim said. Reported in full; "
          f"reporting only the closest would be selection against the target", w)

    # ---- 4. the chance control ---------------------------------------------
    U = sorted({mp.nstr(d, 18) for *_, d, _, _ in
                [(a, b, d, p_, q_) for a, b, d, p_, q_ in pairs]})
    U = sorted(mp.mpf(x) for x in U)
    win = [u for u in U if abs(u - target) <= mp.mpf("0.5") * target]
    gaps = sorted(win[i + 1] - win[i] for i in range(len(win) - 1))
    med = gaps[len(gaps) // 2]
    expected = med / 4 / target * 100
    observed = min(abs(u - target) for u in U) / target * 100
    check("the_best_difference_is_the_same_ORDER_as_chance",
          observed < expected * 4,
          f"{len(U)} distinct |differences| over the 15 pairs, {len(win)} "
          f"within +-50 % of the target, median spacing {mp.nstr(med, 6)} -> "
          f"expected best-by-chance {mp.nstr(expected, 4)} %. Observed best "
          f"{mp.nstr(observed, 6)} %. Better than chance but the same order, on "
          f"a grid of 11 values -- not evidence for any pair, and the assertion "
          f"deliberately tests ORDER rather than 'beats chance', because "
          f"beating a coarse grid is what a coarse grid does", w)

    # ---- 5. what survives ---------------------------------------------------
    survivors = [(lab, v) for lab, v in vals.items()]
    check("the_per_word_bound_itself_is_untouched",
          all(v >= 1 - mp.mpf("1e-25") for _, v in survivors),
          f"tr_M >= 1 still holds on every PSD-feasible gamma-gamma word "
          f"({', '.join(mp.nstr(v, 10) for _, v in survivors)}), tight at the "
          f"empty word. The det-1 fact, AM-GM, weight non-negativity and the "
          f"Markov normalisation are all measured and all stand; so do the "
          f"floor and every Lean theorem on this branch, which are about "
          f"pairings and PSD matrices and mention no observable. What is "
          f"withdrawn is one inference, not the mathematics", w)

    # ---- 6. the surviving NEW finding --------------------------------------
    infeas = {}
    for kind in ("p", "n"):
        bad = []
        for shape, (M, dim) in nucleon_blocks(kind).items():
            if not _fe.is_psd(M, dim):
                bad.append(str(shape))
        infeas[kind] = bad
    dets = {kind: {str(s): mp.nstr(mp.det(M), 12)
                   for s, (M, dim) in nucleon_blocks(kind).items()}
            for kind in ("p", "n")}
    check("the_scored_elements_words_are_BOTH_psd_infeasible",
          all(infeas[k] for k in ("p", "n")),
          f"nuc11_interleaved fails Matrix.PosSemidef on {infeas['p']} for the "
          f"proton and {infeas['n']} for the neutron -- 2 of 3 H_3 blocks each "
          f"-- and carries det != 1 in every block (proton: {dets['p']}). "
          f"🛑 That is a MEASUREMENT under reading (B), NOT a rejection by the "
          f"ruling: the SDP scope question was answered '(A) core only' (bean "
          f"qou-99qc, 2026-09-12), under which reading 3 prunes nothing outside "
          f"the gamma-gamma core and 'the census element stands'. The first "
          f"draft of this assertion said the ruling excluded it; that was an "
          f"over-application of the SDP half. The alternating-character "
          f"exclusion already recorded is separate and unaffected", w)

    w.add_data("retraction", {
        "what_I_asserted": "tr_M >= 1 per PSD-feasible gamma-gamma word means "
                           "the route cannot reproduce Q_beta at any strand "
                           "count, with a minimum prediction of E_0 = +440.369 %",
        "what_is_true": "Q_beta = |eps(Delta)|*E_0 with Delta = neutron word "
                        "MINUS proton word; tr is linear, so a lower bound on "
                        "each word does not bound their difference",
        "how_caught": "the calibration step -- tr(p) and tr(n) each failed to "
                      "match the recorded tr_conv_D, and their difference "
                      "matched it to 25 digits",
        "source_confirms": "delta_of docstring: 'Delta = neutron - proton, "
                           "coordinatewise in the NF basis'",
        "contaminated": [
            "qbeta_gamma_gamma_trace_ge_one_probe.py (description + the "
            "Q_beta_is_excluded_at_every_strand_count assertion)",
            "qbeta_gamma_gamma_psd_trace_floor_probe.py (same inference)",
            "qbeta_gamma_gamma_qbeta_prediction_probe.py (scored single words, "
            "which is not the scoring path either)",
            "QOU/Archimedean/GammaGammaTraceFloor.lean (docstring framing only)",
            "beans qou-99qc parts 9 and 10, and the PR body",
        ],
        "survives": [
            "tr_M >= 1 per PSD-feasible gamma-gamma word, tight",
            "the [n+1]_q/[2]_q^n floor and its strict decay",
            "every Lean theorem on this branch",
            "the crossing-energy results",
        ],
    })
    w.add_data("calibration", {
        "tr_proton_word": mp.nstr(tp, 25),
        "tr_neutron_word": mp.nstr(tn, 25),
        "difference": mp.nstr(diff, 25),
        "recorded_tr_conv_D": RECORDED_TR_CONV_D,
        "abs_gap": mp.nstr(abs(diff - rec), 6),
    })
    w.add_data("difference_predictions", [
        {"a": a, "b": b, "abs_diff": mp.nstr(d, 25),
         "Q_beta_MeV": mp.nstr(pred, 15), "err_pct": mp.nstr(pct, 8)}
        for a, b, d, pred, pct in pairs
    ])
    w.add_data("chance_control", {
        "distinct_differences": len(U),
        "within_50pct_of_target": len(win),
        "median_spacing": mp.nstr(med, 20),
        "expected_best_pct": mp.nstr(expected, 8),
        "observed_best_pct": mp.nstr(observed, 8),
        "verdict": "same order as chance on an 11-value grid; not evidence",
    })
    w.add_data("scored_element_sdp_status", {
        "psd_infeasible_blocks": infeas,
        "block_determinants": dets,
        "reading": "a MEASUREMENT under reading (B). NOT a rejection by the "
                   "ruling: the scope answer was '(A) core only' (bean "
                   "qou-99qc, 2026-09-12), under which the census element "
                   "stands and reading 3 prunes nothing outside the core. The "
                   "alternating-character exclusion is separate and unaffected",
        "scope_answer": "(A) core only -- itself recorded as SELECTED-with-"
                        "ambiguity in that bean entry, not as a clean ruling",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited -- a retraction plus a measurement",
        "what_is_now_OPEN": "whether any PAIR of PSD-feasible gamma-gamma "
                            "words reproduces Q_beta. Nothing here excludes "
                            "it, and picking the closest pair out of 15 would "
                            "be selection against the target",
    })

    ok = not FAILED
    w.save()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
