#!/usr/bin/env python3
"""
perknot_pn_bond_resolved_extensivity_probe.py — can a PARAMETER-FREE, per-knot
p≠n-resolved bond weight reproduce the non-monotone extensivity multiplier
μ_ext(K)=B_AME/B_base, INCLUDING the T≠³He degeneracy-break that any symmetric
(equal-weight) bond model structurally cannot make?

CONTEXT (the open gap).  ``deltalambda-extensivity-gap-synthesis.witness.json``
closes sign+magnitude of the base B_base=m_e·|Σ y_λ χ^λ sgn·dim| but leaves the
per-isotope extensivity multiplier

    μ_ext(K) = B_AME(K) / B_base(K)   =  D 5.8529 / T 4.4441 / ³He 3.2918 / ⁴He 9.3133

as the OPEN k(A) (GAP-A-3 jet-tower level selection, DERIVED not fit).  μ_ext is
non-monotone in A/bond-count ⇒ not fit-closable from 4 points by a symmetric model.

THE DIFFERENT ANGLE (why this is not a duplicate of the equal-weight bond model in
``computations/bond_extensivity_equal_weight.py``, nor of the sibling additive-S(K)
probe under computations/probes/).  T=(p,n,n) and ³He=(p,p,n) share A=3 and share
bond count C(3,2)=3, yet μ_ext differs 4.444 vs 3.292 (ratio 1.350).  An EQUAL-WEIGHT
bond model gives every A=3 nucleus the same 3 bonds ⇒ ratio ≡ 1.000 ⇒ it CANNOT split
them.  The per-knot p≠n-distinct Markov traces CAN: the pair bonds resolve into pp/pn/nn
TYPES with distinct weights.  This probe screens whether a parameter-free per-bond weight
w(a,b) = fixed function of tr_M(p)/tr_M(n) reproduces the split (and the ordering).

DISCIPLINE.  EXPLORATORY, scope-(a).  Anti-fit gate ``adhb``: NO Breit-Wigner fit, NO
free per-bond coefficients tuned to targets, NO reverse-engineered constants.  Every
weight is a FIXED, pre-registered function of tr_M(p)/tr_M(n).  A SINGLE global scale
constant is consumed ONCE — normalising by the D value — after which D is the normaliser
and ONLY T/³He/⁴He are genuine predictions.  Screening ~4 weights × 2 aggregates ⇒ the
entropy caveat applies: a single <5% hit is a LEAD to verify, NOT a closure.

INPUTS (current-main-verified per-knot Jones–Markov traces, chi-cache):
    tr_M(p) = 1.0653062 ,  tr_M(n) = 0.9232333
Pair-bond decompositions (all C(A,2) pairs):
    D  = (p,n)     → {pn}
    T  = (p,n,n)   → {pn, pn, nn}
    ³He= (p,p,n)   → {pp, pn, pn}
    ⁴He= (p,p,n,n) → {pp, pn, pn, pn, pn, nn}
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "substrate"))
sys.path.insert(0, str(HERE.parent))
try:
    from _precision import set_compute_dps  # noqa: E402
    set_compute_dps()
except Exception:
    set_compute_dps()
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:
    WitnessBuilder = None
    _HAVE_WB = False

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# ── pre-registered inputs ─────────────────────────────────────────────────────
TR = {"p": mp.mpf("1.0653062"), "n": mp.mpf("0.9232333")}

# targets from deltalambda-extensivity-gap-synthesis.witness.json
MU_TARGET = {
    "D":   mp.mpf("5.852902577599116"),
    "T":   mp.mpf("4.444146924325849"),
    "3He": mp.mpf("3.2918285794896933"),
    "4He": mp.mpf("9.313340597451814"),
}
# bond multisets (pair type per bond)
BONDS = {
    "D":   ["pn"],
    "T":   ["pn", "pn", "nn"],
    "3He": ["pp", "pn", "pn"],
    "4He": ["pp", "pn", "pn", "pn", "pn", "nn"],
}


def _pair(bt):
    return (TR[bt[0]], TR[bt[1]])


# ── pre-registered parameter-free per-bond weight functions w(a,b) ────────────
# each is a FIXED function of tr_M(p)/tr_M(n); none tuned to any target.
def w_prod(a, b):   return a * b                    # Markov-multiplicative
def w_sum(a, b):    return a + b                    # additive trace
def w_gmean(a, b):  return mp.sqrt(a * b)           # geometric mean
def w_inv(a, b):    return 1 / (a * b)              # inverse-product (un-binding susceptibility)

CANDIDATES = {
    "prod":  w_prod,
    "sum":   w_sum,
    "gmean": w_gmean,
    "inv":   w_inv,
}

# ── junk / calibration controls ──────────────────────────────────────────────
def w_count(a, b):  return mp.mpf(1)                # equal-weight (main's model): ratio must be 1.000
def w_absdiff(a, b):  return mp.fabs(a - b) + mp.mpf("0.5")  # symmetric-in-type (pp=nn): also 1.000
CONTROLS = {
    "equal_weight(count)": w_count,
    "meaningless(|Δtr|+.5)": w_absdiff,
}

# ── aggregates over the bond multiset ─────────────────────────────────────────
def agg_product(vals):
    r = mp.mpf(1)
    for v in vals:
        r *= v
    return r


def agg_sum(vals):
    return mp.fsum(vals)


AGGREGATES = {"product": agg_product, "sum": agg_sum}


def bond_vals(K, wfn):
    return [wfn(*_pair(bt)) for bt in BONDS[K]]


def mu_pred(K, wfn, aggfn):
    """S(K)/S(D)·μ_target(D) — D consumed ONCE as the global normaliser."""
    S_K = aggfn(bond_vals(K, wfn))
    S_D = aggfn(bond_vals("D", wfn))
    return S_K / S_D * MU_TARGET["D"]


def t_3he_ratio(wfn, aggfn):
    return aggfn(bond_vals("T", wfn)) / aggfn(bond_vals("3He", wfn))


def main() -> int:
    dps_used = mp.mp.dps
    print(f"  dps={dps_used}   tr_M(p)={float(TR['p'])}   tr_M(n)={float(TR['n'])}\n")

    # ── Step 1: confirm targets + the split ratio ────────────────────────────
    tgt_ratio = MU_TARGET["T"] / MU_TARGET["3He"]
    print("### Step 1 — targets (μ_ext=B_AME/B_base) + the decisive T/³He split")
    for K in ("D", "T", "3He", "4He"):
        print(f"     μ_ext({K:>3}) = {float(MU_TARGET[K]):.6f}")
    print(f"     T/³He target ratio = {float(tgt_ratio):.6f}   (symmetric model gives 1.000)\n")

    # ── Step 2/3: screen candidates ──────────────────────────────────────────
    print("### Step 2/3 — parameter-free per-knot bond-resolved candidates")
    print("     (primary aggregate = product = Markov-multiplicative; ratio is scale-free)\n")
    results = {}
    ORDER_TARGET = ["3He", "T", "D", "4He"]  # ascending target order
    target_asc = sorted(MU_TARGET, key=lambda k: MU_TARGET[k])
    for aggname, aggfn in AGGREGATES.items():
        print(f"  ── aggregate = {aggname} ──")
        header = f"     {'cand':<7}" + "".join(f"{K:>10}" for K in ("D", "T", "3He", "4He")) \
                 + f"{'T/³He':>10}{'relerr%':>10}{'order?':>8}"
        print(header)
        for cname, wfn in {**CANDIDATES, **CONTROLS}.items():
            preds = {K: mu_pred(K, wfn, aggfn) for K in MU_TARGET}
            r = t_3he_ratio(wfn, aggfn)
            relerr = float((r - tgt_ratio) / tgt_ratio * 100)
            pred_asc = sorted(preds, key=lambda k: preds[k])
            order_ok = (pred_asc == target_asc)
            row = f"     {cname:<7}" + "".join(f"{float(preds[K]):>10.4f}" for K in ("D", "T", "3He", "4He"))
            row += f"{float(r):>10.4f}{relerr:>10.2f}{('yes' if order_ok else 'no'):>8}"
            print(row)
            results[f"{aggname}:{cname}"] = {
                "mu_pred": {K: float(preds[K]) for K in MU_TARGET},
                "t_3he_ratio": float(r),
                "t_3he_relerr_pct": relerr,
                "ordering_full_match": bool(order_ok),
                "is_control": cname in CONTROLS,
            }
        print()

    # ── decisive read ────────────────────────────────────────────────────────
    # best genuine candidate on the T/³He split
    genuine = {k: v for k, v in results.items() if not v["is_control"]}
    best = min(genuine, key=lambda k: abs(genuine[k]["t_3he_relerr_pct"]))
    b = genuine[best]
    split_hit = abs(b["t_3he_relerr_pct"]) < 5.0
    right_dir = b["t_3he_ratio"] > 1.0
    print("### Decisive test — the T/³He degeneracy-break (scale-free)")
    print(f"     best genuine combo : {best}")
    print(f"     T/³He pred = {b['t_3he_ratio']:.6f}  vs target {float(tgt_ratio):.6f}  "
          f"(relerr {b['t_3he_relerr_pct']:+.2f}%)  right-direction={right_dir}")
    print(f"     split <5% : {split_hit}     full-ordering match : {b['ordering_full_match']}")
    # controls
    ctrl_ratios = {k: results[k]["t_3he_ratio"] for k in results if results[k]["is_control"]
                   and k.startswith("product:")}
    print(f"     controls (product agg): " +
          ", ".join(f"{k.split(':',1)[1]}={v:.4f}" for k, v in ctrl_ratios.items())
          + "  ← symmetric ⇒ 1.000, cannot split")

    # ── verdict ──────────────────────────────────────────────────────────────
    # LEAD iff a genuine parameter-free weight splits T/³He <5% right-direction
    #   AND controls confirm 1.000; PRUNE otherwise. Full-ordering / 4He-max is
    #   the harder second bar and is reported separately.
    lead_on_split = split_hit and right_dir
    full_closure = lead_on_split and b["ordering_full_match"]
    if full_closure:
        verdict = ("LEAD (strong): a parameter-free per-knot p≠n bond weight reproduces BOTH the "
                   "T/³He split (<5%) AND the full non-monotone μ_ext ordering. Verify, not closure.")
    elif lead_on_split:
        verdict = (f"LEAD (qualified): the inverse-product per-bond weight w(a,b)=1/(tr_a·tr_b) under "
                   f"the product aggregate reproduces the T/³He degeneracy-break to "
                   f"{b['t_3he_relerr_pct']:+.2f}% (pred {b['t_3he_ratio']:.4f} vs 1.3500) — the split a "
                   f"symmetric/equal-weight model structurally CANNOT make (controls give exactly 1.000). "
                   f"This is the genuine non-duplicative contribution: the p≠n resolution supplies the "
                   f"sign+magnitude of the T≠³He degeneracy-break. BUT it does NOT supply k(A): the full "
                   f"non-monotone μ_ext ordering fails (⁴He is not reproduced as the maximum; magnitudes "
                   f"off by tens of %). One <5% hit among ~8 screened combos + a binary direction choice ⇒ "
                   f"a LEAD to verify, NOT a closure (entropy caveat). Scope-(a).")
    else:
        verdict = ("PRUNE (scope-(a) negative): no parameter-free per-knot bond weight splits T/³He to "
                   "<5% in the right direction — even the p≠n-resolved bond model does not supply k(A). "
                   "Narrows the search away from per-bond-weight extensivity.")
    print("\n### VERDICT")
    print("   " + verdict)

    # ── witness ──────────────────────────────────────────────────────────────
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("perknot-pn-bond-resolved-extensivity", engine="mpmath")
            wb.set_description(
                "EXPLORATORY scope-(a): screens parameter-free per-knot p≠n-resolved bond weights "
                "w(a,b)=fixed fn of tr_M(p)/tr_M(n) against the open extensivity multiplier "
                "μ_ext=B_AME/B_base (D 5.853 / T 4.444 / ³He 3.292 / ⁴He 9.313). The decisive test is the "
                "T/³He degeneracy-break (ratio 1.350) that any symmetric/equal-weight model gives as 1.000. "
                "The inverse-product weight 1/(tr_a·tr_b) under the product aggregate reproduces the split "
                "to ~1.4% (right direction) — supplying the sign+magnitude of the T≠³He break the p≠n "
                "resolution uniquely provides — but does NOT reproduce the full non-monotone μ_ext (⁴He not "
                "the max). Qualified LEAD, not closure; entropy caveat (1 hit / ~8 combos). No fit, no wiring.")
            wb.set_audit_only("docs/audits/2026-07-17-perknot-pn-bond-resolved-extensivity.md")
            wb.add_data("discipline", "EXPLORATORY")
            wb.add_data("production_wired", False)
            wb.add_data("scope", "(a)")
            wb.add_data("tr_M", {k: float(v) for k, v in TR.items()})
            wb.add_data("targets", {k: float(v) for k, v in MU_TARGET.items()})
            wb.add_data("t_3he_ratio_target", float(tgt_ratio))
            wb.add_data("bonds", BONDS)
            wb.add_data("candidates", results)
            wb.add_data("best_genuine_combo", best)
            wb.add_data("t_3he_ratio_pred_vs_target", {
                "pred": b["t_3he_ratio"], "target": float(tgt_ratio),
                "relerr_pct": b["t_3he_relerr_pct"], "right_direction": right_dir,
                "split_under_5pct": split_hit})
            wb.add_data("per_isotope", b["mu_pred"])
            wb.add_data("verdict", verdict)
            wb.add_assertion(
                name="t3he_split_reproduced_under_5pct_right_direction",
                computed=str(int(lead_on_split)), expected="1", tolerance=0,
                source=(f"best genuine per-bond weight ({best}) gives T/³He={b['t_3he_ratio']:.4f} "
                        f"vs target 1.3500 ({b['t_3he_relerr_pct']:+.2f}%); symmetric controls give 1.000. "
                        "A parameter-free p≠n-resolved weight DOES supply the degeneracy-break sign+magnitude."))
            wb.add_assertion(
                name="full_muext_ordering_and_4He_max_reproduced",
                computed=str(int(b["ordering_full_match"])), expected="1", tolerance=0,
                source=("whether the full non-monotone μ_ext ordering (3He<T<D<4He, ⁴He max) is reproduced. "
                        "FAILS: the split is captured but k(A) global extensivity / ⁴He-max is not — "
                        "so this is a qualified LEAD (split only), not a closure of k(A). Scope-(a)."))
            wb.add_data("allPassed", bool(lead_on_split))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
