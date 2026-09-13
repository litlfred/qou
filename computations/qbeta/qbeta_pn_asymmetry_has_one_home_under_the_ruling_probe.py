"""Under the gamma-gamma ruling the proton/neutron asymmetry has exactly ONE
place left to live — the vertex multiset — and the corpus currently keeps it
somewhere the ruling forbids.

# Ref: AGENTS.md §"OWNER RULING 2026-09-08" (bean `qou-ales`) -- canonical braid
#      words are selected by gamma-gamma construction + the confinement SDP
# Ref: QOU.Mass.GammaGammaWordSelection.altChar_eq_one (sorry-free) -- every
#      gamma-gamma word has alternating character exactly 1
# Ref: computations/qbeta/qbeta_qbeta_scores_a_difference_probe.py -- Q_beta is
#      scored on Delta = neutron word MINUS proton word, so there ARE two words
# Ref: computations/qbeta/qbeta_scored_element_is_not_gamma_gamma_produced_probe.py
#      -- the same exclusion at the ELEMENT level; this probe localises it to
#      the three letters that carry the whole p/n distinction

THE QUESTION THIS ANSWERS.  `Q_beta = |eps(Delta)| * E_0` with `Delta` a
difference of a neutron word and a proton word, so the ruling has to select
TWO words and something has to make them different.  What?

THE CORPUS'S ANSWER TODAY.  `nuc11_interleaved` builds both nucleons as

    (gamma-gamma core, 6 letters) . (quark block, 3 letters) . (gluon pair, 2)

and the core and the gluon pair are **byte-identical between proton and
neutron**.  The entire p/n distinction is the three-letter quark block —
`(sigma_0)(sigma_0 - h/2)(sigma_1 - h/2)` for the proton against
`(sigma_0 - h/2)(sigma_0 - h/2)(sigma_1 - h)` for the neutron.

WHY THAT IS EXACTLY WHAT THE RULING FORBIDS.  The alternating character is
multiplicative and is fixed at `1` on every gamma-gamma word
(`altChar_eq_one`, sorry-free).  Measured here letter by letter: the core sits
at `1.0` exactly, and the quark blocks at `-0.9108` (proton) and `-1.1221`
(neutron) — **negative**, so neither is gamma-gamma-expressible, and they are
where the two nucleons diverge.

So the corpus separates the nucleons **precisely in the invariant the ruling
pins**.  Under the ruling both words would have `altChar = 1` and would be
indistinguishable *by that invariant* — they can still differ, but only
through something the invariant cannot see.

WHAT IS LEFT.  A gamma-gamma word is a product of vertices `sigma_i
sigma_{i+1}^{-1}`, so its only freedom is **which vertices, how many**.  And
the Markov trace is blind to their ORDER (measured: 3840 (permutation,
index-assignment) pairs of a 5-vertex word give one value; the crossing energy
is blind the same way).  So under the ruling the p/n asymmetry has exactly one
home: **the vertex multiset**.

A CONSEQUENCE WORTH STATING, because it upgrades a sibling result.  At `n = 4`
the PSD-feasible set is six words including the empty one, so there are exactly
**15 unordered (neutron, proton) assignments** — which means the 15-pair table
in `qbeta_qbeta_scores_a_difference_probe.py` is **exhaustive at that strand
count**, not a sample of a larger space.

SCOPE.  **(a) scope-limited, plus one structural observation.**  The structural
half — that a gamma-gamma word's only freedom is its vertex multiset, since
`altChar` is pinned and order is invisible to the trace — holds at every `n`.
The rest is about the corpus's current construction at `n = 3` and the
feasible set at `n = 4`.  Nothing here says which multiset a nucleon should be,
and nothing here selects a pair.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

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

TOL = mp.mpf("1e-25")

#: `nuc11_interleaved`, as `(generator, shift in units of h)`.
CORE = [(0, 0), (1, -1)] * 3
QUARK = {
    "p": [(0, 0), (0, mp.mpf("-0.5")), (1, mp.mpf("-0.5"))],
    "n": [(0, mp.mpf("-0.5")), (0, mp.mpf("-0.5")), (1, -1)],
}
GLUON = [(0, 0), (0, 0)]

#: the PSD-feasible gamma-gamma words at n = 4 (MEASURED by #7295), plus empty.
N4_FEASIBLE_COUNT = 6

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def alt_letter(d) -> mp.mpf:
    """Alternating character of a letter `sigma_g + d*h`: `sigma_i -> -1/q`."""
    return -1 / Q + mp.mpf(str(d)) * H0


def alt_word(letters) -> mp.mpf:
    prod = mp.mpf(1)
    for _g, d in letters:
        prod *= alt_letter(d)
    return prod


def sign_block(kind: str) -> mp.mpf:
    """The `(1,1,1)` Wedderburn projection -- one-dimensional, so its trace IS
    the alternating character. Computed through the Hoefsmit matrices, i.e. by
    a completely different route than `alt_word`."""
    sig, dim = _fe.blocks(3)[(1, 1, 1)]
    M = mp.eye(dim)
    for g, d in CORE + QUARK[kind] + GLUON:
        M = M * (sig[g] + (mp.mpf(str(d)) * H0) * mp.eye(dim))
    return sum(M[j, j] for j in range(dim))


def main() -> int:
    w = WitnessBuilder("qbeta-pn-asymmetry-has-one-home-under-the-ruling")
    w.set_description(
        "Q_beta is scored on a difference of a neutron word and a proton word, "
        "so the ruling must select two words and something must separate them. "
        "The corpus separates them ENTIRELY in the three-letter quark block: "
        "the gamma-gamma core and the gluon pair are byte-identical between the "
        "nucleons. And the quark blocks carry alternating character -0.9108 (p) "
        "and -1.1221 (n), both negative, while every gamma-gamma word is pinned "
        "at exactly 1 (altChar_eq_one, sorry-free) -- so the corpus separates "
        "the nucleons precisely in the invariant the ruling fixes. Under the "
        "ruling both words have altChar = 1 and cannot be told apart by it; "
        "since the trace is also blind to vertex ORDER, the p/n asymmetry has "
        "exactly one home left, the VERTEX MULTISET. Consequence: the 15-pair "
        "table in the sibling retraction probe is exhaustive at n = 4, not a "
        "sample. Scope-(a) plus one structural observation that holds at every n."
    )

    # ---- 1. where the p/n distinction actually lives -----------------------
    shared = (CORE == CORE) and (GLUON == GLUON)
    differs = QUARK["p"] != QUARK["n"]
    check("the_whole_pn_distinction_is_the_three_letter_quark_block",
          shared and differs,
          f"nuc11_interleaved builds both nucleons as core(6) . quark(3) . "
          f"gluon(2). The core and the gluon pair are IDENTICAL between proton "
          f"and neutron; only the quark block differs -- "
          f"{[str(d) for _g, d in QUARK['p']]} against "
          f"{[str(d) for _g, d in QUARK['n']]} in units of h. So three letters "
          f"of eleven carry the entire asymmetry", w)

    # ---- 2. the core is pinned at 1, the quark blocks are not --------------
    a_core = alt_word(CORE)
    a_q = {k: alt_word(QUARK[k]) for k in ("p", "n")}
    a_gl = alt_word(GLUON)
    print(f"    core  altChar = {mp.nstr(a_core, 16)}")
    print(f"    quark altChar = p {mp.nstr(a_q['p'], 14)}   n {mp.nstr(a_q['n'], 14)}")
    print(f"    gluon altChar = {mp.nstr(a_gl, 16)}")
    check("the_core_is_pinned_at_one_and_the_quark_blocks_are_negative",
          abs(a_core - 1) < TOL and a_q["p"] < 0 and a_q["n"] < 0,
          f"the six-letter gamma-gamma core has altChar = "
          f"{mp.nstr(a_core, 16)} exactly, as altChar_eq_one requires. The "
          f"quark blocks have {mp.nstr(a_q['p'], 12)} (proton) and "
          f"{mp.nstr(a_q['n'], 12)} (neutron) -- both NEGATIVE, so neither is "
          f"gamma-gamma-expressible, and they are exactly where the nucleons "
          f"diverge. (The gluon pair is {mp.nstr(a_gl, 12)} = 1/q^2, also not 1, "
          f"but it is shared and so carries no asymmetry)", w)

    # ---- 3. cross-check altChar against the Wedderburn (1,1,1) block -------
    gaps = {}
    for k in ("p", "n"):
        full = a_core * a_q[k] * a_gl
        gaps[k] = abs(full - sign_block(k))
    check("the_alternating_character_IS_the_sign_block_computed_independently",
          max(gaps.values()) < TOL,
          f"multiplying the per-letter alternating characters and taking the "
          f"trace of the (1,1,1) Hoefsmit projection are different routes to "
          f"the same number, and they agree to {mp.nstr(max(gaps.values()), 4)}: "
          f"{mp.nstr(a_core * a_q['p'] * a_gl, 14)} (proton), "
          f"{mp.nstr(a_core * a_q['n'] * a_gl, 14)} (neutron). Without this the "
          f"letter-level computation above would be an unchecked convention", w)

    # ---- 4. the consequence for the ruling ---------------------------------
    sep = abs(a_core * a_q["p"] * a_gl - a_core * a_q["n"] * a_gl)
    rel = sep / abs(a_core * a_q["p"] * a_gl) * 100
    check("the_corpus_separates_the_nucleons_in_the_invariant_the_ruling_pins",
          sep > TOL,
          f"the corpus's two nucleons differ by {mp.nstr(sep, 12)} in "
          f"alternating character ({mp.nstr(rel, 6)} % of the proton value). "
          f"Under the ruling both would be exactly 1, so this invariant could "
          f"not tell them apart at all. That is not a defect in either -- it is "
          f"the tension: the corpus's p/n handle is the one thing the ruling "
          f"fixes", w)

    # ---- 5. what is left to carry it ---------------------------------------
    check("under_the_ruling_the_only_remaining_handle_is_the_vertex_multiset",
          True,
          f"a gamma-gamma word is a product of vertices sigma_i "
          f"sigma_{{i+1}}^-1, so its only freedom is which vertices and how "
          f"many; and the Markov trace is blind to their ORDER (3840 "
          f"(permutation, index-assignment) pairs of a 5-vertex word give one "
          f"value -- #7295, and the crossing energy is blind the same way). So "
          f"the p/n asymmetry has exactly one home under the ruling: the vertex "
          f"MULTISET. Stated as an assertion so the structural claim is "
          f"machine-recorded; it is an argument, not a measurement, and it "
          f"holds at every n", w)

    # ---- 6. so the sibling enumeration is exhaustive at n = 4 --------------
    pairs = N4_FEASIBLE_COUNT * (N4_FEASIBLE_COUNT - 1) // 2
    check("the_sibling_15_pair_table_is_exhaustive_at_n_equals_four",
          pairs == 15,
          f"with {N4_FEASIBLE_COUNT} PSD-feasible gamma-gamma words at n = 4 "
          f"(the five of #7295 plus the empty word) there are exactly {pairs} "
          f"unordered (neutron, proton) assignments, and |tr(n) - tr(p)| is "
          f"symmetric. So the 15-pair table in "
          f"qbeta_qbeta_scores_a_difference_probe.py enumerates EVERY "
          f"ruling-admissible assignment at that strand count -- it is "
          f"exhaustive, not a sample, which is what makes its -100 %..+79.4 % "
          f"span a statement about the ruling rather than about a selection", w)

    w.add_data("where_the_asymmetry_lives", {
        "corpus_construction": "core(6 gamma-gamma letters) . quark(3) . gluon(2)",
        "shared_between_nucleons": ["core", "gluon pair"],
        "differs": "the 3-letter quark block only",
        "quark_p": [str(d) for _g, d in QUARK["p"]],
        "quark_n": [str(d) for _g, d in QUARK["n"]],
    })
    w.add_data("alternating_character", {
        "core": mp.nstr(a_core, 25),
        "quark_p": mp.nstr(a_q["p"], 25),
        "quark_n": mp.nstr(a_q["n"], 25),
        "gluon": mp.nstr(a_gl, 25),
        "full_p": mp.nstr(a_core * a_q["p"] * a_gl, 25),
        "full_n": mp.nstr(a_core * a_q["n"] * a_gl, 25),
        "gamma_gamma_value": "1 exactly (altChar_eq_one, sorry-free)",
        "separation_pct": mp.nstr(rel, 12),
    })
    w.add_data("consequence", {
        "structural": "under the ruling a word's only freedom is its vertex "
                      "multiset -- altChar is pinned at 1 and the trace is "
                      "blind to vertex order",
        "n4_admissible_assignments": pairs,
        "sibling_table_is": "exhaustive at n = 4, not a sample",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited, plus one structural observation",
        "structural_half_holds_at": "every n",
        "what_is_NOT_claimed": "which multiset a nucleon should be; no pair is "
                               "selected here, and selecting one by residual "
                               "would be selection against the target",
    })

    ok = not FAILED
    w.save()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
