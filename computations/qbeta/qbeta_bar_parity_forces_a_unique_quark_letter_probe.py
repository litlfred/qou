"""The corpus's own bar-odd property, imposed on the ruled `z_D` base, FORCES a
unique Q_beta from the letters the gamma-gamma ruling cannot reach — and the
census assignment does not satisfy it.

# Ref: AGENTS.md line 2182 -- "Q_beta ... the bar-odd `sinh` partner of the
#      bar-even `cosh` meson scale m_pi". That is the hypothesis tested here,
#      and it is the CORPUS'S, not this probe's.
# Ref: bean qou-99qc, 2026-09-12 PARITY BOUND -- the ruling reaches 6 of 11
#      letters provably; exactly 5 lie outside it
# Ref: computations/qbeta/qbeta_pn_asymmetry_has_one_home_under_the_ruling_probe.py
#      -- of those 5, the two bar-fixed ones are shared, so the whole p/n
#      asymmetry sits in the remaining quark letter
# Ref: computations/qbeta/qbeta_quark_block_is_the_bar_fixed_letters_probe.py
#      -- `-h/2` is the unique bar-fixed shift; bar swaps `0` and `-h`
# Ref: AGENTS.md §"NO FITTING" -- accuracy is not evidence; a less accurate
#      DERIVED route outranks a more accurate selected one

WHAT IS OPEN, STATED SHARPLY.  The parity bound proves no 11-crossing word is
gamma-gamma-produced, so exactly 5 of the 11 letters lie outside the ruling:
the 3-letter quark block and the 2-letter gluon pair.  Of those 5, two are
bar-fixed (`-h/2`) and IDENTICAL between the nucleons, and the gluon pair is
shared — so the entire proton/neutron asymmetry is carried by **one** letter,
which the ruling provably cannot select.  What does select it?

THE HYPOTHESIS, AND IT IS THE CORPUS'S OWN.  AGENTS.md records Q_beta as the
**bar-odd** partner of the bar-even meson scale.  That property is attached to
the *published closed form* — the `z = 1` cell retired as a base by the
2026-09-08 ruling — so whether it survives the move to `z_D = q^3/(q^2+1)` is
exactly the open question.  Impose it and see.

THE FREEDOM, MEASURED.  The odd letter can sit in any of the three quark slots
and be either member of the bar-pair (`sigma`, shift `0`; or `sigma^-1`, shift
`-h`).  That is 6 configurations per nucleon — but slots 0 and 1 are both
generator 0 and give **exactly** the same trace, so there are only **4 distinct
elements**.  Of the 30 ordered (proton, neutron) pairs with p != n, four have
`Delta = 0` (the slot-0/slot-1 duplicates), leaving **26** with something to
say.

THE RESULT.  Requiring `tr^{z_D}(Delta)` to be bar-odd, `f(1/q) = -f(q)`,
selects **8 of those 26**, and the census assignment is **not one of them**
— every bar-odd pair gives the two nucleons the SAME member of the bar-pair and
differs only in generator, while the census gives them OPPOSITE members, which
is precisely what destroys the parity.

AND THE 8 DO NOT NEED CHOOSING BETWEEN, because they collapse.  Symbolically,

    Delta(sigma, sigma)  =  - Delta(sigma^-1, sigma^-1)

*exactly*, so `|tr(Delta)|` is the same for all eight:

    |tr(Delta)| = (q^6 - 1)(q^4 + 1)(q^12 - 4q^10 + 6q^8 - 7q^6 + 6q^4
                   - 4q^2 + 1) / (4 q^9 (q^2 + 1)^2)

giving **Q_beta = 0.353415698 MeV, -54.825 %** against CODATA.

🛑 NO SELECTION WAS MADE, and that is the point.  The constraint is structural
(a parity in `q`), never proximity to the measured value; it narrows 26 -> 8;
and the 8 collapse to one number by an exact identity.  There is nothing left
to pick.  The answer is WORSE than the census assignment's -16.678 %, which is
what AGENTS.md asks for: implement the specification and report what it gives
even when that is worse, and rank by derivational cleanliness rather than by
residual.

🛑 AND UNDER THE RULED SCOPE IT IS EXCLUDED, NOT MERELY UNCLOSED.  The SDP
scope question — does the confinement SDP of `qou-ales` constrain only the 6
gamma-gamma core letters, or the whole 11-letter word? — was put to the owner
on 2026-09-13 and answered **"(B) whole element"**: every Wedderburn projection
of the full word must be `PosSemidef`.  Measured here, ALL SIX (slot, kind)
configurations fail it, so under (B) the ruling rejects this entire one-letter
family — the bar-odd survivors above AND the census assignment alike.

So the bar-parity result is a derivation whose answer the SDP half then
excludes.  Both halves stand: the parity narrowing is real and forced, and the
element it forces is inadmissible.  That is a stronger negative than "does not
close", and it is what makes the open problem sharp — the un-ruled letters need
a principle that is bar-consistent AND whole-element PSD-admissible, and no
member of this family is.

HISTORY, because the scoping moved twice and both moves were mine.  A first
draft called the PSD failure a rejection by the ruling with no scope stated; a
correction (`04edd8b5d75`) demoted it to "a measurement under reading (B), not
selected", on the strength of the bean's then-recorded "(A) core only".  The
owner has now selected (B), so the first draft's verdict is reinstated — but it
is reinstated by a ruling, not by the argument that originally produced it.

SCOPE.  **(a) scope-limited** for the parity half: one hypothesis, one family,
`n = 3`, and its force is conditional on the bar-odd property transferring from
the retired `z = 1` cell to the ruled `z_D` base, which is assumed here, not
established.  **The PSD half is unconditional** given (B): the six
configurations are measured infeasible, independent of the bar-odd assumption.
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
Q0 = mp.mpf(str(_oc.Q0))

#: the census witness's recorded value for the scored element, verbatim.
RECORDED_TR_CONV_D = "-0.1541948850472397056592555"

#: the census assignment, in this probe's (slot, kind) coordinates.
CENSUS_P = (0, "sigma")
CENSUS_N = (2, "inv")

GENS = (0, 0, 1)              # the quark block's generators, shared by p and n
SLOTS = (0, 1, 2)
KINDS = ("sigma", "inv")      # the two members of the bar-pair: shift 0, -h

TOL = mp.mpf("1e-25")

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


# ---- numeric side, at the proton pin ------------------------------------
NUM_SHIFT = {"sigma": mp.mpf(0), "fixed": mp.mpf("-0.5"), "inv": mp.mpf(-1)}
NUM_CORE = [(0, 0), (1, -1)] * 3
NUM_GLUON = [(0, 0), (0, 0)]


def num_letters(slot: int, kind: str):
    quark = [(GENS[i], NUM_SHIFT[kind] if i == slot else NUM_SHIFT["fixed"])
             for i in SLOTS]
    return NUM_CORE + quark + NUM_GLUON


def qint(m: int):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - 1 / Q0)


def y_lambda(lam) -> mp.mpf:
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(3 - 2 * k + 1) / qint(2) ** 3


def _blocks_of(slot: int, kind: str):
    out = {}
    for shape, (sig, dim) in _fe.blocks(3).items():
        M = mp.eye(dim)
        for g, d in num_letters(slot, kind):
            M = M * (sig[g] + (mp.mpf(str(d)) * H0) * mp.eye(dim))
        out[shape] = (M, dim)
    return out


def num_trace(slot: int, kind: str) -> mp.mpf:
    return sum(y_lambda(s) * sum(M[j, j] for j in range(dim))
               for s, (M, dim) in _blocks_of(slot, kind).items())


def psd_feasible(slot: int, kind: str) -> bool:
    return all(_fe.is_psd(M, dim) for M, dim in _blocks_of(slot, kind).values())


# ---- symbolic side, in q -------------------------------------------------
qs = sp.symbols("q", positive=True)
hs = qs - 1 / qs
zDs = qs ** 3 / (qs ** 2 + 1)
SYM_SHIFT = {"sigma": sp.Integer(0), "fixed": -hs / 2, "inv": -hs}
SYM_CORE = [(0, sp.Integer(0)), (1, -hs)] * 3
SYM_GLUON = [(0, sp.Integer(0)), (0, sp.Integer(0))]


def sym_trace(slot: int, kind: str):
    quark = [(GENS[i], SYM_SHIFT[kind] if i == slot else SYM_SHIFT["fixed"])
             for i in SLOTS]
    lets = SYM_CORE + quark + SYM_GLUON
    return sp.simplify(_oc.tr(_oc.word_to_vec(lets, 3, {}, hs), 3, hs, zDs))


def main() -> int:
    w = WitnessBuilder("qbeta-bar-parity-forces-a-unique-quark-letter")
    w.set_description(
        "The gamma-gamma ruling provably cannot reach 5 of the 11 letters, and "
        "of those the whole p/n asymmetry sits in ONE quark letter. Imposing "
        "the corpus's own bar-odd property for Q_beta (AGENTS.md line 2182) on "
        "the ruled z_D base narrows the 26 non-degenerate ordered (p, n) pairs to 8, "
        "and the CENSUS ASSIGNMENT IS NOT AMONG THEM -- every bar-odd pair "
        "gives both nucleons the same member of the bar-pair, the census gives "
        "them opposite members. The 8 then COLLAPSE: Delta(sigma,sigma) = "
        "-Delta(inv,inv) exactly, so |tr(Delta)| is one number and no selection "
        "is possible or needed. It gives Q_beta = 0.353415698 MeV, -54.825 % -- "
        "WORSE than the census -16.678 %, which is the point: derived beats "
        "selected. It does NOT close Q_beta: all four distinct elements fail "
        "PSD, so the SDP half rejects the whole family. Scope-(a); conditional "
        "on the bar-odd property transferring from the retired z = 1 cell."
    )

    E0 = qbeta_e0.canonical()
    qb = mp.mpf(str(Q_BETA_MEV))

    # ---- 1. calibration: reproduce the census cell from this parametrisation
    tp = num_trace(*CENSUS_P)
    tn = num_trace(*CENSUS_N)
    rec = mp.mpf(RECORDED_TR_CONV_D)
    print(f"  census p {CENSUS_P}: tr = {mp.nstr(tp, 20)}")
    print(f"  census n {CENSUS_N}: tr = {mp.nstr(tn, 20)}")
    print(f"  tr(n) - tr(p)      = {mp.nstr(tn - tp, 20)}")
    print(f"  recorded           = {RECORDED_TR_CONV_D}")
    print()
    check("the_parametrisation_reproduces_the_census_cell",
          abs((tn - tp) - rec) < mp.mpf("1e-24"),
          f"the (slot, kind) coordinates used here reproduce the census "
          f"witness's tr_conv_D to {mp.nstr(abs((tn - tp) - rec), 4)}: the "
          f"census assignment is p = {CENSUS_P}, n = {CENSUS_N}. Without this "
          f"the whole enumeration would be about a different object -- the "
          f"check whose absence caused this branch's earlier retraction", w)

    # ---- 2. the freedom is 4 distinct elements, not 6 ---------------------
    vals = {(sl, k): num_trace(sl, k) for sl in SLOTS for k in KINDS}
    same01 = all(abs(vals[(0, k)] - vals[(1, k)]) < TOL for k in KINDS)
    distinct = {mp.nstr(v, 25) for v in vals.values()}
    distinct_short = sorted({mp.nstr(mp.mpf(x), 12) for x in distinct})
    check("the_one_letter_freedom_is_four_distinct_elements",
          same01 and len(distinct) == 4,
          f"slots 0 and 1 are both generator 0 and give exactly the same trace "
          f"(agreement < {mp.nstr(TOL, 2)}), so the 6 (slot, kind) "
          f"configurations realise only {len(distinct)} distinct traces: "
          f"{sorted(distinct_short)}. Only the "
          f"GENERATOR of the odd letter matters, not its slot within a "
          f"generator", w)

    # ---- 3. bar parity narrows 30 -> 8, and excludes the census -----------
    sym = {(sl, k): sym_trace(sl, k) for sl in SLOTS for k in KINDS}
    cfgs = [(sl, k) for sl in SLOTS for k in KINDS]
    bar_odd = []
    for a, b in itertools.permutations(cfgs, 2):
        D = sp.simplify(sym[b] - sym[a])
        if D == 0:
            continue
        if sp.simplify(D.subs(qs, 1 / qs) + D) == 0:
            bar_odd.append((a, b))
    census_odd = (CENSUS_P, CENSUS_N) in bar_odd
    ordered = len([1 for a, b in itertools.permutations(cfgs, 2)
                   if sp.simplify(sym[b] - sym[a]) != 0])
    check("bar_parity_narrows_the_freedom_and_EXCLUDES_the_census_assignment",
          len(bar_odd) == 8 and not census_odd,
          f"requiring tr^{{z_D}}(Delta)(1/q) = -tr^{{z_D}}(Delta)(q) leaves "
          f"{len(bar_odd)} of the {ordered} ordered (p, n) pairs with p != n, "
          f"and the census assignment p = {CENSUS_P}, n = {CENSUS_N} is "
          f"{'among' if census_odd else 'NOT among'} them. Every surviving pair "
          f"gives both nucleons the SAME member of the bar-pair and differs "
          f"only in generator; the census gives them OPPOSITE members, which is "
          f"exactly what breaks the parity", w)

    # ---- 4. the 8 collapse, exactly ----------------------------------------
    Ds = sp.simplify(sym[(2, "sigma")] - sym[(0, "sigma")])
    Di = sp.simplify(sym[(2, "inv")] - sym[(0, "inv")])
    collapse = sp.simplify(Ds + Di) == 0
    mags = {mp.nstr(abs(num_trace(*b) - num_trace(*a)), 22) for a, b in bar_odd}
    check("the_eight_survivors_collapse_to_ONE_magnitude_by_an_exact_identity",
          collapse and len(mags) == 1,
          f"Delta(sigma, sigma) = -Delta(inv, inv) EXACTLY (symbolic: "
          f"simplify(Ds + Di) == 0), so all {len(bar_odd)} bar-odd pairs share "
          f"one |tr(Delta)| -- measured, {len(mags)} distinct magnitude. There "
          f"is therefore NOTHING to select among the survivors, which is what "
          f"keeps this a derivation rather than a choice", w)

    # ---- 5. the value it forces --------------------------------------------
    mag = abs(num_trace(*bar_odd[0][1]) - num_trace(*bar_odd[0][0]))
    pred = mag * E0
    pct = (pred - qb) / qb * 100
    census_pred = abs(tn - tp) * E0
    census_pct = (census_pred - qb) / qb * 100
    closed = sp.factor(Ds)
    print(f"  |tr(Delta)| forced = {mp.nstr(mag, 20)}")
    print(f"  Q_beta             = {mp.nstr(pred, 12)} MeV   {mp.nstr(pct, 8)} %")
    print(f"  census, for contrast = {mp.nstr(census_pred, 12)} MeV   "
          f"{mp.nstr(census_pct, 8)} %")
    print()
    check("the_forced_value_is_WORSE_than_the_census_and_that_is_the_point",
          abs(pct) > abs(census_pct),
          f"the bar-odd constraint forces Q_beta = {mp.nstr(pred, 12)} MeV, "
          f"{mp.nstr(pct, 8)} %, against the census assignment's "
          f"{mp.nstr(census_pct, 8)} %. The derived answer is the less accurate "
          f"one. AGENTS.md: implement the specification and report what it "
          f"gives even when that is worse; rank by derivational cleanliness, "
          f"never by residual. No configuration was chosen for its value -- the "
          f"constraint is a parity in q and the survivors collapse", w)

    # ---- 6. it narrows; it does not close ----------------------------------
    feas = {(sl, k): psd_feasible(sl, k) for sl in SLOTS for k in KINDS}
    check("no_configuration_is_whole_element_PSD_feasible_so_reading_B_rejects_them_all",
          not any(feas.values()),
          f"all {len(feas)} (slot, kind) configurations FAIL Matrix.PosSemidef "
          f"on at least one Wedderburn block -- the census assignment and every "
          f"bar-odd alternative alike. Under the OWNER-SELECTED scope "
          f"'(B) whole element' (2026-09-13, bean qou-99qc), the confinement "
          f"SDP of qou-ales applies to every Wedderburn projection of the full "
          f"11-letter word, so the ruling REJECTS this entire one-letter "
          f"family. The bar-parity derivation above therefore forces an element "
          f"the SDP half then excludes: both halves stand, and the open problem "
          f"is a principle that is bar-consistent AND whole-element "
          f"PSD-admissible. (Reading (A) core-only would have excluded nothing "
          f"here; it was not selected)", w)

    w.add_data("the_open_problem", {
        "parity_bound": "no 11-crossing word is gamma-gamma-produced, so 5 of "
                        "11 letters lie outside the ruling (bean qou-99qc, "
                        "2026-09-12)",
        "of_those_five": "2 are bar-fixed (-h/2) and identical between the "
                         "nucleons; the gluon pair is shared; so ONE quark "
                         "letter carries the whole p/n asymmetry",
        "question": "what selects that letter, given the ruling cannot",
    })
    w.add_data("hypothesis", {
        "statement": "tr^{z_D}(Delta) is bar-odd: f(1/q) = -f(q)",
        "provenance": "AGENTS.md line 2182 -- Q_beta is 'the bar-odd sinh "
                      "partner of the bar-even cosh meson scale m_pi'",
        "caveat": "that property is recorded for the PUBLISHED closed form, "
                  "the z = 1 cell retired as a base by the 2026-09-08 ruling; "
                  "whether it transfers to z_D is assumed here, not established",
    })
    w.add_data("freedom", {
        "configurations_per_nucleon": len(cfgs),
        "distinct_elements": len(distinct),
        "why_fewer": "slots 0 and 1 are both generator 0 and give exactly the "
                     "same trace; only the generator matters",
        "traces": {f"slot{sl}_{k}": mp.nstr(vals[(sl, k)], 25)
                   for sl in SLOTS for k in KINDS},
    })
    w.add_data("bar_parity_result", {
        "ordered_pairs_tested": ordered,
        "bar_odd_survivors": len(bar_odd),
        "census_assignment": {"p": list(CENSUS_P), "n": list(CENSUS_N)},
        "census_is_bar_odd": bool(census_odd),
        "survivor_pattern": "both nucleons take the SAME member of the "
                            "bar-pair and differ only in generator",
        "survivors": [{"p": list(a), "n": list(b)} for a, b in bar_odd],
    })
    w.add_data("forced_value", {
        "collapse_identity": "Delta(sigma, sigma) = -Delta(inv, inv), exact",
        "closed_form_of_Delta": sp.srepr(closed)[:0] or str(closed),
        "abs_tr_Delta": mp.nstr(mag, 25),
        "E0_MeV": mp.nstr(E0, 25),
        "E0_form": "tower_summed (canonical, qbeta_e0.canonical)",
        "Q_beta_MeV": mp.nstr(pred, 20),
        "err_pct": mp.nstr(pct, 12),
        "census_Q_beta_MeV": mp.nstr(census_pred, 20),
        "census_err_pct": mp.nstr(census_pct, 12),
    })
    w.add_data("ruled_out_by_the_sdp_half", {
        "psd_feasible": {f"slot{sl}_{k}": bool(feas[(sl, k)])
                         for sl in SLOTS for k in KINDS},
        "reading": "a REJECTION by the ruling. The owner selected scope "
                   "'(B) whole element' on 2026-09-13 (bean qou-99qc), so the "
                   "confinement SDP of qou-ales applies to every Wedderburn "
                   "projection of the full 11-letter word. All 6 configurations "
                   "fail it, so the whole one-letter family is inadmissible -- "
                   "the bar-odd survivors and the census assignment alike",
        "scope_answer": "(B) whole element -- owner ruling 2026-09-13, "
                        "answering the fork this bean had carried as "
                        "'(A) core only, SELECTED-with-ambiguity'",
        "consequence": "the bar-parity derivation forces an element the SDP "
                       "half excludes; the open problem is a principle that is "
                       "bar-consistent AND whole-element PSD-admissible",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited",
        "unconditional": ["the census assignment is not bar-odd",
                          "the bar-odd family collapses to one magnitude",
                          "no member is whole-element PSD-feasible -- which "
                          "under the selected scope (B) is a rejection by the "
                          "ruling, and does not depend on the bar-odd premise"],
        "conditional_on": "the bar-odd property transferring from the retired "
                          "z = 1 cell to the ruled z_D base",
        "no_selection_was_made": "the constraint is a parity in q, never "
                                 "proximity to the measured value, and the "
                                 "survivors collapse to a single number",
    })

    ok = not FAILED
    w.save()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
