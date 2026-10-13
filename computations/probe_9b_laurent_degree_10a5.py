#!/usr/bin/env python3
"""PROBE 1 (step-9b, bean drjk) — Laurent-degree bookkeeping for the
q₀^(10A−5) canonical-binding residual.

EXPLORATORY PROBE — derive-or-refute; NOT wired to production; introduces
NO new constants (Δ_λ gate: no seventh fit ansatz).

Context (docs/audits/2026-06-09-delta-lambda-canonical-residual.md): the
trace-canonical binding residual satisfies

    Δ_λ(K) = B_AME / B_pred ≈ q₀^(10A−5),   B_pred = Q_β·(tr_M(W_free) − tr_M(W_atom))

with D exact to 0.01 q₀-units, T −0.07, ⁴He +0.27, ³He −1.40 (Z-dependent).

HYPOTHESIS UNDER TEST (not assumed): 10A−5 = 5(2A−1) = 5·[A nucleons +
(A−1) interfaces] — i.e. the exponent is a per-block / per-interface q₀⁵
factorization that should fall out of exact Laurent-degree bookkeeping of
the Phase-5q closed form (computations/closed_form_tau_M.py):

    tr_M(𝓑_K) = tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏_i f_i(q),
    f_pp = z,  f_nn = z − h,  f_pn = z − h·(1/2 − δ(q)/4)   [bring_color_weighted]

with z = 1/(√q + 1/√q), h = q − q⁻¹, δ(q) = (q−1)²(1−q⁻⁴)/3 (the PROVEN
leading flavor split, prop:flavor-split-substrate; the posited subleading
was de-wired 2026-06-29).

METHOD (exact, per compute-author §1/§3):
  1. tr_p(q), tr_n(q) computed EXACTLY as symbolic Laurent rationals in
     s = √q via the canonical Jones–Markov trace
     (markov/markov_trace_canonical.tr_M_element) on the canonical H₃
     nucleon words (pyhecke.atom.nucleon_gen_chains templates via
     mass_at_3A_proper.atom_braid_word_3A).
  2. Interface factors symbolic with the EXACT rational δ(q).
  3. Closed-form identity verified (a) EXACTLY in ℚ at rational s-points
     for D and T (full H_{3A} symbolic trace vs closed form), and
     (b) numerically at q₀ vs the independent transfer path
     (tr_m_atom_via_transfer.tr_m_atom_zn) for D/T/³He/⁴He.
  4. Exponent bookkeeping vs 10A−5: exact leading/lowest Laurent degrees
     of every factor and of Δtr = tr_free·(1 − ∏f_i); writhe / exponent-sum
     difference W_atom − W_free; the 50-dps log_{q₀} decomposition
       log_{q₀}Δ_λ = log_{q₀}(B_AME/Q_β) − log_{q₀}tr_free − log_{q₀}(1−∏f)
     with per-nucleon increments; an exponent dictionary of the structural
     constants in q₀-units; and the T-vs-³He mirror decomposition of the
     −1.40 outlier.

Scale note: the MeV multiplier is Q_β(n) = m_n − m_p − m_e ≈ 0.78233 MeV  # noqa: P31 — docstring; Q_beta scale note (experimental_constants.Q_NEUTRON_MEV)
(experimental_constants.Q_NEUTRON_MEV), exactly as in binding_canonical.py
(whose docstring records that this parameter was historically misnamed
E_0; the 10A−5 residual of the 2026-06-09 audit is defined on this scale).

Run:  python3 -u computations/probe_9b_laurent_degree_10a5.py
Witness: probe-9b-laurent-degree-10a5.witness.json (audit-only)

Ref: docs/audits/2026-06-09-delta-lambda-canonical-residual.md
Ref: docs/audits/2026-06-09-binding-trace-convention-split.md
Ref: computations/closed_form_tau_M.py (Phase 5q closed form)
Ref: `constit-factor-tau-M-proton-identity` (Phase 5l)
Ref: prop:interface-knot-markov-z (Phase 5c.1)

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from hecke_symbolic import (  # noqa: E402
    SymbolicHeckeDivision, SymbolicHeckeElement, HA as H_SYMB, q as q_sym,
)
from markov.markov_trace_canonical import tr_M_element  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from closed_form_tau_M import canonical_interface_kinds  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
# 50-dps source. `_H_F64` below is DELIBERATELY f64 (it feeds an f64 kernel),
# but it should be the correctly-rounded f64, and the delta on the next line
# was being evaluated at ~17 digits before the float cast. Alias renamed:
# a name saying F64 over an mpf is the label problem this sweep is about.
from q_parameter import Q_MP as _Q0_MP  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from qou_substrate import Q_50_DIGIT_STR, WitnessBuilder  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS  # noqa: E402

mp.mp.dps = COMPUTE_DPS + 15

_H_F64 = float(_Q0_MP - 1 / _Q0_MP)
_D_PN_F64 = -_H_F64 * (0.5 - float(flavor_split_leading(_Q0_MP)) / 4)

# Exact symbolic building blocks (all rational in q except √q inside z).
S = sp.Symbol("s", positive=True)          # s = √q
DELTA_SYM = (q_sym - 1) ** 2 * (1 - q_sym ** -4) / 3   # proven leading δ(q)
Z_SYM = q_sym**3 / (q_sym**2 + 1)       # Markov z(q)
H_Q = q_sym - 1 / q_sym                                  # Hecke h(q)
F_SYM = {
    "positive": Z_SYM,                                    # p-p interface
    "negative": Z_SYM - H_Q,                              # n-n interface
    "averaged": Z_SYM - H_Q * (sp.Rational(1, 2) - DELTA_SYM / 4),  # p-n (bring)
}

ATOMS = [
    ("D", 1, 1, float(AME_B_DEUTERON_MEV_VALIDATION)),
    ("T", 1, 2, float(AME_B_TRITIUM_MEV_VALIDATION)),
    ("3He", 2, 1, float(AME_B_HE3_MEV_VALIDATION)),
    ("4He", 2, 2, float(AME_B_HE4_MEV_VALIDATION)),
]


def _symbolic_factor(c_f: float, d_f: float, g: int) -> SymbolicHeckeElement:
    """Map an f64 canonical crossing (c, d, gen) to the EXACT symbolic
    Hecke factor. Templates: d ∈ {0, −h, −h(1/2−δ/4), −h/2} with the
    color-weighted p-n checked BEFORE −h/2 (they differ by ≈7e-5 ≫ tol)."""
    if abs(c_f - 1.0) > 1e-12:
        raise ValueError(f"unexpected c={c_f}")
    if abs(d_f) < 1e-12:
        d = sp.Integer(0)
    elif abs(d_f + _H_F64) < 1e-9:
        d = -H_SYMB
    elif abs(d_f - _D_PN_F64) < 1e-9:
        d = -H_SYMB * (sp.Rational(1, 2) - DELTA_SYM / 4)
    elif abs(d_f + _H_F64 / 2) < 1e-9:
        d = -H_SYMB / 2
    else:
        raise ValueError(f"unrecognised d={d_f} at gen {g}")
    return SymbolicHeckeElement({(g,): sp.Integer(1), (): d})


def build_symbolic_element(Z: int, N: int, include_inter: bool
                           ) -> SymbolicHeckeElement:
    """Canonical atom braid (bring_color_weighted) as an exact symbolic
    Hecke element with incremental Gröbner–Shirshov reduction."""
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    cnt = 0
    for (c_f, d_f, g) in word:
        elem = elem * _symbolic_factor(c_f, d_f, g)
        cnt += 1
        if cnt >= 4:
            elem, _ = div.reduce(elem, engine="laurent")
            cnt = 0
    if cnt:
        elem, _ = div.reduce(elem, engine="laurent")
    return elem


def laurent_degree_data(expr_q: sp.Expr) -> dict:
    """Exact Laurent-degree data of a rational function of q and √q,
    as a ratio of polynomials in s = √q (leading = s→∞ growth order,
    lowest = s→0 order; q-units = s-units / 2)."""
    e_s = sp.cancel(sp.together(sp.expand(expr_q.subs(q_sym, S ** 2))))
    num, den = sp.fraction(e_s)
    pnum = sp.Poly(sp.expand(num), S)
    pden = sp.Poly(sp.expand(den), S)
    lead = pnum.degree() - pden.degree()
    low = (min(m[0] for m in pnum.monoms())
           - min(m[0] for m in pden.monoms()))
    return {
        "leading_deg_s": int(lead),
        "lowest_deg_s": int(low),
        "leading_deg_q": lead / 2.0,
        "lowest_deg_q": low / 2.0,
        "bar_symmetric_range": bool(lead == -low),
        "_expr_s": e_s,
    }


def eval_at_q0(expr_q: sp.Expr, s0: mp.mpf) -> mp.mpf:
    """Evaluate a symbolic expression exactly rationalised in s at s0=√q₀."""
    e_s = sp.cancel(sp.together(sp.expand(expr_q.subs(q_sym, S ** 2))))
    return sp.lambdify(S, e_s, "mpmath")(s0)


def word_writhe(word) -> dict:
    """Exponent-sum bookkeeping of a canonical f64 word: σ → +1,
    σ⁻¹ → −1, averaged (either d-template) → 0 (it is (σ+σ⁻¹)/2-like,
    not a group element; counted separately)."""
    wr, n_avg = 0, 0
    for (c_f, d_f, g) in word:
        if abs(d_f) < 1e-12:
            wr += 1
        elif abs(d_f + _H_F64) < 1e-9:
            wr -= 1
        else:
            n_avg += 1
    return {"writhe_signed": wr, "n_averaged": n_avg, "n_crossings": len(word)}


def main() -> int:
    t_start = time.monotonic()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    s0 = mp.sqrt(q0)
    lnq0 = mp.log(q0)
    qb = mp.mpf(str(Q_NEUTRON_MEV))

    def logq(x):
        return mp.log(x) / lnq0

    w = WitnessBuilder("probe-9b-laurent-degree-10a5", engine="sympy+mpmath")
    w.set_audit_only("docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md")
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("Q_beta_n_MeV", float(Q_NEUTRON_MEV))
    w.add_parameter("pn_convention", "bring_color_weighted (proven leading δ)")

    # ── 1. Exact symbolic H₃ nucleon traces ─────────────────────────
    print("── symbolic H₃ nucleon traces (canonical Jones–Markov) ──")
    tr_sym = {}
    for nuc, (Z, N) in [("p", (1, 0)), ("n", (0, 1))]:
        elem = build_symbolic_element(Z, N, include_inter=False)
        tr_sym[nuc] = tr_M_element(elem, 3, simplify=False)
    deg_p = laurent_degree_data(tr_sym["p"])
    deg_n = laurent_degree_data(tr_sym["n"])
    tr_p0 = eval_at_q0(tr_sym["p"], s0)
    tr_n0 = eval_at_q0(tr_sym["n"], s0)
    print(f"  tr_p(q0) = {mp.nstr(tr_p0, 30)}   deg_s [{deg_p['lowest_deg_s']}, "
          f"{deg_p['leading_deg_s']}]  log_q0 = {mp.nstr(logq(tr_p0), 8)}")
    print(f"  tr_n(q0) = {mp.nstr(tr_n0, 30)}   deg_s [{deg_n['lowest_deg_s']}, "
          f"{deg_n['leading_deg_s']}]  log_q0 = {mp.nstr(logq(tr_n0), 8)}")
    w.add_data("nucleon_traces", {
        "tr_p_symbolic_in_s": sp.sstr(deg_p.pop("_expr_s")),
        "tr_n_symbolic_in_s": sp.sstr(deg_n.pop("_expr_s")),
        "tr_p_at_q0": mp.nstr(tr_p0, 50),
        "tr_n_at_q0": mp.nstr(tr_n0, 50),
        "log_q0_tr_p": float(logq(tr_p0)),
        "log_q0_tr_n": float(logq(tr_n0)),
        "degrees_p": deg_p, "degrees_n": deg_n,
    })

    # ── 2. Interface factors: degrees + q₀ values ───────────────────
    print("── interface factors ──")
    iface_data = {}
    f0 = {}
    for kind, label in [("positive", "f_pp = z"),
                        ("negative", "f_nn = z − h"),
                        ("averaged", "f_pn = z − h(1/2 − δ/4)")]:
        dd = laurent_degree_data(F_SYM[kind])
        dd.pop("_expr_s")
        v = eval_at_q0(F_SYM[kind], s0)
        f0[kind] = v
        g = 1 - v
        iface_data[kind] = {
            "form": label, "degrees": dd,
            "value_at_q0": mp.nstr(v, 50),
            "log_q0_f": float(logq(abs(v))),
            "one_minus_f_at_q0": mp.nstr(g, 50),
            "log_q0_one_minus_f": float(logq(abs(g))),
        }
        print(f"  {label:28s} deg_s [{dd['lowest_deg_s']}, {dd['leading_deg_s']}]"
              f"  f(q0)={mp.nstr(v, 12)}  log_q0 f={mp.nstr(logq(abs(v)), 8)}")
    w.add_data("interface_factors", iface_data)

    # ── 3. Closed-form identity verification ────────────────────────
    # (a) EXACT in ℚ at rational s-points, D and T: full symbolic H_{3A}
    #     canonical trace vs tr_p^Z tr_n^N ∏f_i, with the exact δ(q).
    print("── closed-form identity: exact rational verification ──")
    exact_checks = []
    for name, Z, N in [("D", 1, 1), ("T", 1, 2)]:
        t0 = time.time()
        ea = build_symbolic_element(Z, N, include_inter=True)
        ef = build_symbolic_element(Z, N, include_inter=False)
        tra = tr_M_element(ea, 3 * (Z + N), simplify=False)
        trf = tr_M_element(ef, 3 * (Z + N), simplify=False)
        kinds = canonical_interface_kinds(Z, N)
        prod_f = sp.prod([F_SYM[k] for k in kinds])
        closed = tr_sym["p"] ** Z * tr_sym["n"] ** N * prod_f
        free_closed = tr_sym["p"] ** Z * tr_sym["n"] ** N
        diffs = []
        for sv in [sp.Rational(3, 2), sp.Rational(7, 5)]:
            d1 = sp.cancel((tra - closed).subs(q_sym, S ** 2).subs(S, sv))
            d2 = sp.cancel((trf - free_closed).subs(q_sym, S ** 2).subs(S, sv))
            diffs.append((sp.simplify(d1), sp.simplify(d2)))
        ok = all(d1 == 0 and d2 == 0 for d1, d2 in diffs)
        exact_checks.append({
            "atom": name, "exact_identity_holds": bool(ok),
            "s_points": ["3/2", "7/5"], "wall_sec": round(time.time() - t0, 2),
        })
        print(f"  {name}: exact ℚ identity at s∈{{3/2, 7/5}} → {ok} "
              f"[{time.time() - t0:.1f}s]")
        w.add_assertion(
            name=f"closed_form_exact_identity_{name}",
            computed=0.0 if ok else 1.0, expected=0.0, tolerance=0.0,
            source=f"tr_M(W_{name}) − tr_p^{Z}·tr_n^{N}·∏f_i and the free "
                   f"analogue, both EXACTLY 0 in ℚ at s = 3/2 and 7/5 "
                   f"(full H_{3*(Z+N)} symbolic canonical trace vs Phase-5q "
                   f"closed form, exact rational δ(q))",
        )
    w.add_data("exact_identity_checks", exact_checks)

    # (b) numeric at q₀ vs the independent transfer path (all 4 anchors).
    #     KNOWN OFFSET: the q₀-baked canonical word carries δ derived from
    #     the f64 Q (q_parameter.Q) via _avg_color_delta(); this probe uses
    #     δ(q₀) at the full 50-digit pin, giving a uniform ≈9.1e-20 relative
    #     offset in the interface ratio — far below any conclusion drawn
    #     here (the exact-ℚ check above is the strict identity witness).
    print("── closed-form vs transfer path at q₀ ──")
    from tr_m_atom_via_transfer import tr_m_atom_zn
    rows = []
    for name, Z, N, B_ame in ATOMS:
        A = Z + N
        tr_a_tr, tr_f_tr, _chi, wall = tr_m_atom_zn(Z, N, dps=50)
        kinds = canonical_interface_kinds(Z, N)
        prod_f0 = mp.mpf(1)
        for k in kinds:
            prod_f0 *= f0[k]
        tr_f_cf = (tr_p0 ** Z) * (tr_n0 ** N)
        tr_a_cf = tr_f_cf * prod_f0
        rel_a = abs(tr_a_cf - tr_a_tr) / abs(tr_a_tr)
        rel_f = abs(tr_f_cf - tr_f_tr) / abs(tr_f_tr)
        B_pred = qb * (tr_f_cf - tr_a_cf)
        delta_lam = mp.mpf(str(B_ame)) / B_pred
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "interface_kinds": kinds,
            "tr_free_closed": mp.nstr(tr_f_cf, 50),
            "tr_atom_closed": mp.nstr(tr_a_cf, 50),
            "prod_f": mp.nstr(prod_f0, 50),
            "one_minus_prod_f": mp.nstr(1 - prod_f0, 50),
            "rel_diff_vs_transfer_atom": float(rel_a),
            "rel_diff_vs_transfer_free": float(rel_f),
            "B_pred_MeV": mp.nstr(B_pred, 30),
            "B_AME_MeV": B_ame,
            "Delta_lambda": mp.nstr(delta_lam, 30),
            "log_q0_Delta_lambda": float(logq(delta_lam)),
            "law_10A_minus_5": 10 * A - 5,
            "dev_from_law": float(logq(delta_lam)) - (10 * A - 5),
            "_mp": (tr_f_cf, tr_a_cf, prod_f0, B_pred, delta_lam),
        })
        print(f"  {name:>4}: rel(atom)={mp.nstr(rel_a, 3)} rel(free)="
              f"{mp.nstr(rel_f, 3)}  B_pred={mp.nstr(B_pred, 8)} MeV  "
              f"log_q0 Δ_λ={mp.nstr(logq(delta_lam), 6)} (law {10*A-5})")
        w.add_assertion(
            name=f"closed_form_matches_transfer_{name}",
            computed=float(max(rel_a, rel_f)), expected=0.0, tolerance=1e-18,
            source="closed-form tr_atom/tr_free vs independent fine-Bratteli "
                   "transfer path (tr_m_atom_zn, 50 dps); residual ≈9e-20 is "
                   "the f64-q₀-baked δ in the canonical word vs the 50-digit "
                   "δ(q₀) used here",
        )
    # Reproduce the residual-law table (anchor: audit 2026-06-09).
    for r, (dev_expect, tol) in zip(rows, [(-0.01, 0.02), (-0.07, 0.02),
                                            (-1.40, 0.02), (+0.27, 0.02)]):
        w.add_assertion(
            name=f"residual_law_reproduced_{r['atom']}",
            computed=r["dev_from_law"], expected=dev_expect, tolerance=tol,
            source="log_q0(B_AME/B_pred) − (10A−5) vs the 2026-06-09 "
                   "delta-lambda-canonical-residual audit values",
        )

    # ── 4. Exponent bookkeeping vs 10A−5 ────────────────────────────
    # (i) Exact Laurent degrees of Δtr_rel = 1 − ∏f and Δtr = tr_free·(1−∏f).
    print("── exact Laurent degrees of the binding difference ──")
    for r in rows:
        Z, N = r["Z"], r["N"]
        kinds = r["interface_kinds"]
        prod_sym = sp.prod([F_SYM[k] for k in kinds])
        dtr_sym = tr_sym["p"] ** Z * tr_sym["n"] ** N * (1 - prod_sym)
        dd_rel = laurent_degree_data(1 - prod_sym)
        dd_rel.pop("_expr_s")
        dd = laurent_degree_data(dtr_sym)
        dd.pop("_expr_s")
        r["degrees_one_minus_prod_f"] = dd_rel
        r["degrees_delta_tr"] = dd
        print(f"  {r['atom']:>4}: deg_q(1−∏f) = [{dd_rel['lowest_deg_q']}, "
              f"{dd_rel['leading_deg_q']}]  deg_q(Δtr) = [{dd['lowest_deg_q']}, "
              f"{dd['leading_deg_q']}]   vs 10A−5 = {r['law_10A_minus_5']}")

    # (ii) writhe / exponent-sum difference W_atom − W_free.
    print("── writhe / exponent-sum bookkeeping ──")
    for r in rows:
        wa = word_writhe(atom_braid_word_3A(r["Z"], r["N"], include_inter=True))
        wf = word_writhe(atom_braid_word_3A(r["Z"], r["N"], include_inter=False))
        r["writhe_atom"] = wa
        r["writhe_free"] = wf
        r["writhe_diff_atom_minus_free"] = wa["writhe_signed"] - wf["writhe_signed"]
        print(f"  {r['atom']:>4}: e(W_atom)−e(W_free) = "
              f"{r['writhe_diff_atom_minus_free']}  (avg crossings: "
              f"atom {wa['n_averaged']}, free {wf['n_averaged']})   "
              f"vs 10A−5 = {r['law_10A_minus_5']}")

    # (iii) 50-dps log_{q₀} decomposition of the residual exponent.
    print("── log_q0 decomposition: Δ_λ = (B_AME/Q_β) / [tr_free·(1−∏f)] ──")
    print(f"  {'atom':>5} {'log(B_AME/Qβ)':>14} {'−log tr_free':>13} "
          f"{'−log(1−∏f)':>12} {'total':>8} {'10A−5':>6}")
    for r in rows:
        tr_f_cf, tr_a_cf, prod_f0, B_pred, delta_lam = r["_mp"]
        t_ame = logq(mp.mpf(str(r["B_AME_MeV"])) / qb)
        t_free = -logq(tr_f_cf)
        t_iface = -logq(1 - prod_f0)
        r["log_decomposition"] = {
            "log_q0_BAME_over_Qbeta": float(t_ame),
            "minus_log_q0_tr_free": float(t_free),
            "minus_log_q0_one_minus_prod_f": float(t_iface),
            "trace_side_total": float(t_free + t_iface),
            "total": float(t_ame + t_free + t_iface),
        }
        print(f"  {r['atom']:>5} {float(t_ame):>14.3f} {float(t_free):>13.3f} "
              f"{float(t_iface):>12.3f} {float(t_ame+t_free+t_iface):>8.2f} "
              f"{r['law_10A_minus_5']:>6}")

    # Per-nucleon increments of each decomposition term (D→T, D→³He, T/³He→⁴He).
    incr = []
    by_name = {r["atom"]: r for r in rows}
    for a, b, added in [("D", "T", "+n (+nn interface)"),
                        ("D", "3He", "+p (+pp interface)"),
                        ("T", "4He", "+p (pp; census T{pn,nn}→⁴He{pp,pn,nn})"),
                        ("3He", "4He", "+n (nn; census ³He{pp,pn}→⁴He{pp,pn,nn})")]:
        ra, rb = by_name[a], by_name[b]
        da, db = ra["log_decomposition"], rb["log_decomposition"]
        incr.append({
            "step": f"{a}→{b}", "added": added,
            "d_log_Delta_lambda": round(rb["log_q0_Delta_lambda"]
                                        - ra["log_q0_Delta_lambda"], 3),
            "d_BAME_side": round(db["log_q0_BAME_over_Qbeta"]
                                 - da["log_q0_BAME_over_Qbeta"], 3),
            "d_trace_side": round(db["trace_side_total"]
                                  - da["trace_side_total"], 3),
            "law_increment": 10,
        })
    w.add_data("per_nucleon_increments", incr)
    print("── per-nucleon increments (law: +10 each) ──")
    for i in incr:
        print(f"  {i['step']:>9} ({i['added']}): ΔlogΔ_λ = "
              f"{i['d_log_Delta_lambda']:+.2f} = B_AME-side "
              f"{i['d_BAME_side']:+.2f} + trace-side {i['d_trace_side']:+.2f}")

    # (iv) exponent dictionary of structural constants (q₀-units).
    h0 = q0 - 1 / q0
    z0 = q0**3 / (q0**2 + 1)
    dictionary = {
        "log_q0_z": float(logq(z0)),
        "log_q0_h": float(logq(h0)),
        "log_q0_tr_p": float(logq(tr_p0)),
        "log_q0_tr_n": float(logq(tr_n0)),
        "log_q0_tr_n_over_tr_p": float(logq(tr_n0 / tr_p0)),
        "log_q0_f_pp": float(logq(f0["positive"])),
        "log_q0_f_pn": float(logq(f0["averaged"])),
        "log_q0_f_nn": float(logq(f0["negative"])),
        "log_q0_g_pp=1-f_pp": float(logq(1 - f0["positive"])),
        "log_q0_g_pn=1-f_pn": float(logq(1 - f0["averaged"])),
        "log_q0_g_nn=1-f_nn": float(logq(1 - f0["negative"])),
        "log_q0_delta_flavor": float(logq(flavor_split_leading(q0))),
    }
    w.add_data("exponent_dictionary_q0_units", dictionary)
    print("── exponent dictionary (log_q0 of structural constants) ──")
    for k, v in dictionary.items():
        print(f"  {k:28s} = {v:+.4f}")
    # The sharp near-integer anchor: h(q₀) = q₀^(−15.000) to 2e-4 relative.
    w.add_assertion(
        name="h_at_q0_is_q0_to_minus_15_near_match",
        computed=float(logq(h0)), expected=-15.0, tolerance=0.001,
        source="OBSERVATION TIER (near-match, not derived): "
               "log_q0 h(q0) = log_q0(q0 − q0⁻¹); the deuteron residual "
               "exponent 10·2−5 = 15 coincides with −log_q0 h to ≈2e-4 "
               "relative — i.e. Δ_λ(D) ≈ 1/h(q0)",
    )

    # (v) T vs ³He mirror decomposition of the −1.40 outlier.
    rT, r3 = by_name["T"], by_name["3He"]
    dT, d3 = rT["log_decomposition"], r3["log_decomposition"]
    mirror = {
        "observed_exponent_gap_T_minus_3He":
            round(rT["log_q0_Delta_lambda"] - r3["log_q0_Delta_lambda"], 3),
        "nucleon_trace_asymmetry_term (−log tr_n/tr_p)":
            round(-float(logq(tr_n0 / tr_p0)), 3),
        "interface_sign_swap_term (−log (1−f_pn·f_nn)/(1−f_pp·f_pn))":
            round(d3["minus_log_q0_one_minus_prod_f"] * -1
                  + dT["minus_log_q0_one_minus_prod_f"], 3),
        "B_AME_mirror_asymmetry_term (log B_T/B_3He)":
            round(dT["log_q0_BAME_over_Qbeta"] - d3["log_q0_BAME_over_Qbeta"], 3),
        "note": ("The trace side supplies nucleon asymmetry + interface swap; "
                 "their sum plus the AME mirror term reproduces the observed "
                 "gap by construction. The point is the SPLIT: how much of the "
                 "³He −1.40 deviation is generated by interface SIGNS (pp vs "
                 "nn) vs the p/n trace asymmetry."),
    }
    w.add_data("mirror_decomposition_T_vs_3He", mirror)
    print("── T vs ³He mirror decomposition ──")
    for k, v in mirror.items():
        if k != "note":
            print(f"  {k}: {v}")

    # strip mp objects before serialising rows
    for r in rows:
        r.pop("_mp")
    w.add_data("isotope_rows", rows)

    # ── 5. Verdict (tiered per the (a)/(b) refutation discipline) ───
    trace_sides = [r["log_decomposition"]["trace_side_total"] for r in rows]
    verdict = {
        "hypothesis": "10A−5 = 5·[A nucleons] + 5·[(A−1) interfaces]: a "
                      "per-block/per-interface q₀⁵ factorization derivable "
                      "from Laurent-degree bookkeeping of the Phase-5q "
                      "closed form",
        "tier": "REFUTED — scope (a) ONLY",
        "scope_a_statement": (
            "Leading-degree / writhe / interface bookkeeping of the Phase-5q "
            "closed form, ALONE, does not produce 10A−5. The exact trace-side "
            "contribution to log_q0 Δ_λ (−log tr_free − log(1−∏f)) SHRINKS "
            f"with A ({trace_sides[0]:+.2f} at D → {trace_sides[3]:+.2f} at "
            "⁴He) while the law grows by +10 per nucleon; the growth is "
            "carried by the experimental B_AME/Q_β term, which the closed "
            "form does not model. Exact Laurent degrees of Δtr and the "
            "writhe difference are O(1)–O(20) and NOT of the form 10A−5. "
            "This constrains this bookkeeping route only — it does NOT "
            "structurally exclude a per-object q₀⁵ factor arising elsewhere "
            "in the chain (no proved invariant; scope-(b) NOT claimed)."
        ),
        "observation_tier_residues": [
            "log_q0 h(q0) = −15.0002: the deuteron exponent 15 equals "
            "−log_q0 h to 2e-4 relative (Δ_λ(D) ≈ 1/h(q0)) — near-match, "
            "not derived",
            "Deuteron decomposition splits cleanly as ≈10.0 (B_AME side) + "
            "≈4.97 (trace side ≈ −log_q0 Δtr) — the '10+5' at A=2 is real "
            "but the split does NOT persist (trace side → 0.88 at ⁴He)",
            "³He outlier: the mirror gap decomposes into nucleon-trace "
            "asymmetry (tr_n/tr_p = q₀^−1.37) + interface-sign swap "
            "(pp↔nn) + AME mirror asymmetry — the interface SIGNS alone do "
            "not account for −1.40",
        ],
    }
    w.add_data("verdict", verdict)
    w.set_description(
        "PROBE 1 (9b, bean drjk): exact Laurent-degree bookkeeping of the "
        "Phase-5q closed form tr_M(𝓑_K)=tr_p^Z·tr_n^N·∏f_i vs the canonical "
        "binding residual law Δ_λ≈q₀^(10A−5). Closed form verified EXACTLY "
        "in ℚ (D, T; rational s-points, exact rational δ(q)) and vs the "
        "transfer path at q₀ (≤1e-18). VERDICT: hypothesis '10A−5 from "
        "per-block/per-interface degree bookkeeping' REFUTED scope-(a) — "
        "trace-side exponent shrinks with A (4.97→0.88) while the law grows "
        "+10/nucleon (carried by B_AME). Observation tier: h(q₀)=q₀^−15.0002 "
        "(deuteron anchor), and the ³He −1.40 outlier decomposes into "
        "p/n-trace asymmetry + interface-sign swap + AME mirror asymmetry. "
        "Exploratory; NOT wired; no new constants."
    )
    out = w.save()
    print(f"\nVerdict: {verdict['tier']}")
    print(f"Witness: {out}  [{time.monotonic() - t_start:.1f}s total]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
