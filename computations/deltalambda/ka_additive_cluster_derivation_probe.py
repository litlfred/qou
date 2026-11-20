#!/usr/bin/env python3
"""
ka_additive_cluster_derivation_probe.py — a DIFFERENT-CONTEXT (per-knot-trace
side) attack on the open GAP-A-3 k(A) extensivity gap (bean qou-7uxa), executing
the formalize-first plan in
``docs/scope/2026-07-18-ka-additive-cluster-derivation.md``.

TARGET.  ``deltalambda-extensivity-gap-synthesis.witness.json`` closes sign +
magnitude of the parameter-free base B_base = m_e·|Σ y_λ χ^λ sgn·dim| but leaves
the per-isotope extensivity multiplier

    μ_ext(K) = B_AME/B_base = D 5.8529 / T 4.4441 / ³He 3.2918 / ⁴He 9.3133

as the OPEN k(A).  μ_ext is non-monotone (⁴He, doubly magic, is the maximum).

THE DERIVATION (parameter-free, formalize-first, scope-(a/b); NO fit, NO BW, NO
reverse-engineering μ_ext).

  Step 0 — cast the miss additively: (μ_ext − μ_base) = C₂(A) + C₃(A) [+C₄].
           μ_base = 1 (the base contributes multiplier 1 by definition; the
           cluster channels supply the remaining μ_ext − 1).

  Step 1 — FREEZE the pairwise channel to the merged, Lean-grounded Mayer-b₂
           object   w(a,b) = 1/(tr_M(a)·tr_M(b))   (PR #3841, bond-weight
           isospin split proved).  Aggregate = bond SUM Σ_bonds w  (additive,
           per the Ursell B/m_e = Σ_k b_k structure — NOT a product; a product
           would not be additive over bonds).  ONE a-priori global scale κ₂ is
           consumed ONCE, fixed by the DEUTERON — the unique pure-2-body anchor
           (1 bond, 0 triples ⇒ C₃(D)=0 exactly), so κ₂ = (μ_ext(D)−1)/w(pn).
           After that, C₂(T/³He/⁴He) are predictions with NO freedom.

  Step 2 — residual C₃(A) = (μ_ext−1) − C₂(A), then test the THREE gates:
           * I-conn — genuinely connected (coordinator's FULL 3-body cumulant,
             subtracting BOTH the 2+1 and the 1+1+1 disconnected partitions):
               tr_conn(abc) = tr(abc) − Σ_{2+1} tr(xy)tr(z) + 2 tr(a)tr(b)tr(c).
             The NAIVE per-knot triple 1/(tr_a tr_b tr_c) is a product of 1-body
             traces ⇒ its connected cumulant ≡ 0 ⇒ fully DISCONNECTED ⇒ already
             inside the 1-body/pairwise ceiling ⇒ fails I-conn.  The genuinely-
             connected object is the joint-trace cumulant b₃ (from the real
             multi-nucleon Markov traces, incl. the here-computed diproton /
             dineutron joint pair traces).
           * I-par — is the connected object bar-EVEN (q ↦ q⁻¹)?  The absolute
             scale is bar-even; a bar-odd residual is the p−n channel (wrong
             object).
           * A-locality — C₃(D) must be ≈ 0 (deuteron has no triple).

  Step 3 — verdict, scope-(a/b), with a JUNK control (meaningless triple-count).

INPUTS — all Jones–Markov joint traces at q₀ (50 dps), colour-weighted
averaged-crossing convention; per-nucleon and multi-nucleon caches on main, the
diproton/dineutron joint pair traces computed here via the same Hoefsmit
producer (GATE-A check: the (1,1) path reproduces the cached deuteron trace).

DISCIPLINE.  EXPLORATORY, scope-(a).  No fit, no wiring, adhb anti-BW gate.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "substrate"))
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from chi_at_q0_via_hoefsmit_mpfr import build_chi_cache_at_q0  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:
    WitnessBuilder = None
    _HAVE_WB = False

# ── targets (μ_ext = B_AME/B_base) ────────────────────────────────────────────
MU = {
    "D": mp.mpf("5.852902577599116"),
    "T": mp.mpf("4.444146924325849"),
    "3He": mp.mpf("3.2918285794896933"),
    "4He": mp.mpf("9.313340597451814"),
}
# Cached deuteron joint pair trace — the GATE-A reference for the producer
# path. This is a REGRESSION GUARD, not a recorded result: its only use is
# GATE A below, asserting that the producer still reproduces it. A guard must
# therefore track the producer.
#
# REFRESHED 2026-08-23 (bean `qou-8chw`). Was
# 0.38835720735922143663882816968153229794820994065468, and GATE A was FAILING
# ON MAIN at rel = 4.81e-01 (the probe exited 1). The old value is CONVENTION
# C: recombining the transfer's chi with the live convention-C weights
# (schur_principal_mpmath.y_lambda_at_q0_mpmath_convention_C_HISTORICAL) gives
# 0.3883571411977910 at the proton pin, matching it to ~7 digits. The corpus
# moved to convention D on 2026-08-09, so the producer moved and the guard did
# not.
#
# Refreshing is right HERE and would be wrong for the gap_a3 pair. Those two
# files carry C-frame constants as *recorded inputs to a conclusion*, so they
# get scoped (see the label in gap_a3_deuteron_A_D_overshoot.py). This one is
# a gate on a live producer, so it gets the live value.
#
# The new figure is agreed by four independent paths at the proton pin: this
# chi-cache/Hoefsmit route, the fine-Bratteli transfer, the markov-peel
# arbiter, and (since qou-zck8 regenerated its extract off float64) the
# operator-valued branching combiner.
TR_D_CACHED = mp.mpf("0.5751722439177718708265353439858617251768310907401")

# bond multisets (all C(A,2) pairs, by nucleon type)
BONDS = {
    "D": ["pn"],
    "T": ["pn", "pn", "nn"],
    "3He": ["pp", "pn", "pn"],
    "4He": ["pp", "pn", "pn", "pn", "pn", "nn"],
}
# triple multisets (all C(A,3) triples, by nucleon type)
TRIPLES = {
    "D": [],
    "T": ["pnn"],
    "3He": ["ppn"],
    "4He": ["ppn", "ppn", "pnn", "pnn"],
}


def _tr(name, Z, N, qval, qstr):
    """Joint Markov trace tr_M(β_atomic(Z,N)) at q via Σ_λ y_λ·χ^λ."""
    n = 3 * (Z + N)
    rec = build_chi_cache_at_q0(name, Z, N, qstr, dps=50)
    yl = y_lambda_at(n, qval)
    s = mp.mpf(0)
    for e in rec["by_partition"]:
        lam = tuple(e["partition"])
        if lam in yl:
            s += mp.mpf(str(yl[lam])) * mp.mpf(e["chi_lambda"])
    return s


def joint_traces(qval, qstr):
    return {
        "p": _tr("proton", 1, 0, qval, qstr),
        "n": _tr("neutron", 0, 1, qval, qstr),
        "pp": _tr("diproton", 2, 0, qval, qstr),
        "nn": _tr("dineutron", 0, 2, qval, qstr),
        "pn": _tr("deuteron", 1, 1, qval, qstr),
        "T": _tr("tritium", 1, 2, qval, qstr),
        "3He": _tr("helium-3", 2, 1, qval, qstr),
        "4He": _tr("helium-4", 2, 2, qval, qstr),
    }


def connected_cumulants(tr):
    """Coordinator's FULL Ursell cumulants from joint traces."""
    p, n, pp, nn, pn = tr["p"], tr["n"], tr["pp"], tr["nn"], tr["pn"]
    T, He3, He4 = tr["T"], tr["3He"], tr["4He"]
    # connected 2-body cumulants c2 = tr(ab) − tr(a)tr(b)
    c2 = {"pp": pp - p * p, "pn": pn - p * n, "nn": nn - n * n}
    # connected 3-body: tr(abc) − Σ_{2+1} tr(xy)tr(z) + 2 tr a tr b tr c
    b3_T = T - (2 * pn * n + nn * p) + 2 * p * n * n
    b3_He3 = He3 - (pp * n + 2 * pn * p) + 2 * p * p * n
    # connected 4-body (4He = p,p,n,n):
    #   tr(abcd) − Σ_{3+1} tr(abc)tr(d) − Σ_{2+2} tr(ab)tr(cd)
    #             + 2 Σ_{2+1+1} tr(ab)tr(c)tr(d) − 6 tr a tr b tr c tr d
    b4 = (He4
          - (2 * He3 * n + 2 * T * p)
          - (pp * nn + 2 * pn * pn)
          + 2 * (pp * n * n + nn * p * p + 4 * pn * p * n)
          - 6 * p * p * n * n)
    return c2, {"T": b3_T, "3He": b3_He3, "4He": b4}


def main() -> int:
    q0 = Q_MP
    qinv = 1 / q0
    print(f"dps={mp.mp.dps}  q0={float(q0):.10f}  q0^-1={float(qinv):.10f}\n")

    tr0 = joint_traces(q0, Q_50_DIGIT_STR)

    # GATE A — producer (1,1) path reproduces the cached deuteron trace
    gateA = abs(tr0["pn"] - TR_D_CACHED) / TR_D_CACHED
    print(f"### GATE A  producer tr(pn) vs cached deuteron: rel={float(gateA):.2e} "
          f"(pass={float(gateA) < 1e-30})")
    print("### joint Markov traces at q0 (incl. computed diproton/dineutron):")
    for k in ("p", "n", "pp", "pn", "nn", "T", "3He", "4He"):
        print(f"     tr({k:>3}) = {float(tr0[k]):+.9f}")

    c2cum, bconn = connected_cumulants(tr0)
    print("\n### connected cumulants (from JOINT traces — genuinely connected):")
    print(f"     c2: pp={float(c2cum['pp']):+.5f}  pn={float(c2cum['pn']):+.5f}  "
          f"nn={float(c2cum['nn']):+.5f}   (all nonzero ⇒ joint traces do NOT factorize)")
    print(f"     b3(T)  ={float(bconn['T']):+.6f}")
    print(f"     b3(3He)={float(bconn['3He']):+.6f}")
    print(f"     b4(4He)={float(bconn['4He']):+.6f}")

    # ── Step 0/1 — additive decomposition, C₂ frozen + deuteron-anchored ──────
    w = {"pp": 1 / (tr0["p"] * tr0["p"]),
         "pn": 1 / (tr0["p"] * tr0["n"]),
         "nn": 1 / (tr0["n"] * tr0["n"])}

    def c2raw(K):
        return mp.fsum(w[b] for b in BONDS[K])

    miss = {K: MU[K] - 1 for K in MU}
    kap2 = miss["D"] / c2raw("D")  # deuteron = pure 2-body anchor, consumed ONCE
    print(f"\n### Step 0/1 — additive decomposition (μ_base=1, C₂ frozen b₂ bond-sum)")
    print(f"     κ₂ (deuteron-anchored, a-priori) = {float(kap2):.5f}")
    hdr = (f"     {'iso':>4}{'μ_ext':>9}{'miss':>9}{'C2raw':>9}{'C2':>10}"
           f"{'C3resid':>10}")
    print(hdr)
    C2 = {}
    C3 = {}
    for K in ("D", "T", "3He", "4He"):
        C2[K] = kap2 * c2raw(K)
        C3[K] = miss[K] - C2[K]
        print(f"     {K:>4}{float(MU[K]):>9.4f}{float(miss[K]):>9.4f}"
              f"{float(c2raw(K)):>9.4f}{float(C2[K]):>10.4f}{float(C3[K]):>10.4f}")

    # ── A-locality: C₃(D) must be ≈ 0 ────────────────────────────────────────
    a_local_ok = abs(C3["D"]) < mp.mpf("1e-40")
    print(f"\n### A-locality  C₃(D) = {float(C3['D']):.2e}  (deuteron has no triple; "
          f"pass={a_local_ok})")

    # ── Step 2 — does residual C₃ track the genuinely-connected cumulant? ─────
    print("\n### I-conn / magnitude — residual C₃ vs connected cumulant b:")
    print("     naive triple 1/(tr_a tr_b tr_c) is a PRODUCT of 1-body traces ⇒ "
          "connected cumulant ≡ 0 ⇒ DISCONNECTED ⇒ fails I-conn (mean-field, "
          "inside ceiling).")
    ratios = {}
    for K in ("T", "3He", "4He"):
        ratios[K] = C3[K] / bconn[K]
        print(f"     {K:>4}: C₃={float(C3[K]):+.4f}  b_conn={float(bconn[K]):+.5f}  "
              f"C₃/b={float(ratios[K]):+.4f}")
    # single-scale test: do the three C₃/b ratios agree?
    rvals = [ratios[K] for K in ("T", "3He", "4He")]
    rmean = mp.fsum(rvals) / 3
    rspread = max(abs(r - rmean) for r in rvals) / abs(rmean)
    single_scale = float(rspread) < 0.10 and all((r > 0) == (rvals[0] > 0) for r in rvals)
    print(f"     single-scale (one κ₃ fits all): spread={float(rspread):.2f}, "
          f"sign-consistent={all((r > 0) == (rvals[0] > 0) for r in rvals)} "
          f"⇒ {single_scale}")

    # ── I-par — bar parity of the connected object ───────────────────────────
    tri = joint_traces(qinv, mp.nstr(qinv, 50))
    _, bconn_inv = connected_cumulants(tri)
    print("\n### I-par — bar parity of the connected cumulant (q ↦ q⁻¹):")
    par = {}
    for K in ("T", "3He", "4He"):
        rel = (bconn_inv[K] - bconn[K]) / bconn[K]
        par[K] = float(rel)
        print(f"     b_conn({K:>4}): q0={float(bconn[K]):+.5f}  qinv="
              f"{float(bconn_inv[K]):+.5f}  rel={float(rel):+.3e}  "
              f"bar_even={abs(float(rel)) < 1e-6}")
    bar_even = all(abs(par[K]) < 1e-6 for K in par)
    # raw nucleon-trace parity too (root cause)
    relp = float((tri["p"] - tr0["p"]) / tr0["p"])
    reln = float((tri["n"] - tr0["n"]) / tr0["n"])
    print(f"     (root cause) raw tr(p) rel={relp:+.3e}, tr(n) rel={reln:+.3e} "
          f"⇒ single-nucleon trace itself is NOT bar-even")

    # ── 4He-max test ─────────────────────────────────────────────────────────
    # would a positive-additive connected-triple make ⁴He the max?  b₃(T/³He)>0
    # but b₄(⁴He)<0 (sign flip) ⇒ NO.
    he4_max_ok = (bconn["4He"] > 0) and (bconn["4He"] > bconn["T"]) and (bconn["4He"] > bconn["3He"])
    print(f"\n### 4He-max — connected object makes ⁴He the max? {he4_max_ok}  "
          f"(b₃(T)={float(bconn['T']):+.3f}, b₃(³He)={float(bconn['3He']):+.3f} >0 but "
          f"b₄(⁴He)={float(bconn['4He']):+.3f} <0 — sign flip)")

    # ── junk control — meaningless triple-count C(A,3) ───────────────────────
    junk = {"T": mp.mpf(1), "3He": mp.mpf(1), "4He": mp.mpf(4)}  # #triples
    print("\n### junk control — C₃_junk = #triples C(A,3) = T 1 / ³He 1 / ⁴He 4:")
    jr = {K: C3[K] / junk[K] for K in junk}
    jvals = [jr[K] for K in ("T", "3He", "4He")]
    jmean = mp.fsum(jvals) / 3
    jspread = max(abs(r - jmean) for r in jvals) / abs(jmean)
    print(f"     C₃/junk = T {float(jr['T']):+.3f} / ³He {float(jr['3He']):+.3f} / "
          f"⁴He {float(jr['4He']):+.3f}   spread={float(jspread):.2f}")
    print(f"     connected-cumulant spread {float(rspread):.2f} vs junk spread "
          f"{float(jspread):.2f} ⇒ connected cumulant "
          f"{'BEATS' if float(rspread) < float(jspread) else 'does NOT beat'} junk")

    # ── verdict ──────────────────────────────────────────────────────────────
    lead = (single_scale and bar_even and he4_max_ok
            and float(rspread) < float(jspread))
    if lead:
        verdict = ("LEAD: a parameter-free connected-triple cumulant reproduces the "
                   "residual (single scale, bar-even, ⁴He-max), beating junk. VERIFY.")
    else:
        verdict = (
            "scope-(a) NEGATIVE — the connected 3-cluster channel is CONSTRAINED, "
            "not closed, on four independent grounds: "
            "(1) MAGNITUDE — the frozen Mayer-b₂ bond-sum, forced to absolute μ_ext "
            "scale by the only a-priori anchor (the pure-2-body deuteron), OVERSHOOTS "
            "T/³He/⁴He by 4–5× because μ_ext−1 is strongly SUB-extensive in bond count "
            "(D 4.85/1 bond vs ⁴He 8.31/6 bonds); the residual C₃ is dominated by this "
            "overshoot. "
            "(2) I-conn — the naive per-knot triple 1/(tr_a tr_b tr_c) is a product of "
            "1-body traces ⇒ connected cumulant ≡ 0 ⇒ fully disconnected (mean-field, "
            "already inside the ceiling). The genuinely-connected joint-trace cumulant is "
            "well-defined (b₃(T)=+0.939, b₃(³He)=+0.951 — nearly isospin-blind; "
            "b₄(⁴He)=−2.210) but the residual does NOT track it (C₃/b = −12.6/−12.2/+9.5; "
            "no single scale, sign flips). "
            "(3) I-par — the connected cumulant is NOT bar-even (b₃ shifts ~−19%, b₄ "
            "−24% under q↦q⁻¹; the single-nucleon trace itself shifts +12–13%), so the "
            "object carries bar-odd (p−n) content — wrong channel for the bar-even scale. "
            "(4) 4He-max — b₄(⁴He) is NEGATIVE, opposite in sign to the positive b₃(T/³He), "
            "so no parameter-free connected-triple makes ⁴He the maximum; the junk "
            "triple-count is more self-consistent than the connected cumulant. "
            "A-locality C₃(D)=0 holds trivially (the one gate that passes). Reported to "
            "#3808: freeze nothing new; the per-knot-trace side does not supply k(A). "
            "No fit, no wiring.")
    print("\n### VERDICT\n   " + verdict)

    # ── witness ──────────────────────────────────────────────────────────────
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("ka-additive-cluster-derivation", engine="mpmath")
            wb.set_description(
                "EXPLORATORY scope-(a): different-context (per-knot-trace side) attack on "
                "the open GAP-A-3 k(A) extensivity gap (bean qou-7uxa). Casts μ_ext−1 = "
                "C₂+C₃, freezes C₂ to the merged Lean-grounded Mayer-b₂ bond object "
                "1/(tr_a·tr_b) (deuteron-anchored, one a-priori scale), and tests whether "
                "the residual C₃ is a clean genuinely-connected 3-body cumulant (coordinator's "
                "full Ursell formula, from real joint traces incl. here-computed "
                "diproton/dineutron). NEGATIVE on 4 grounds: b₂ bond-sum overshoots (μ_ext "
                "sub-extensive in bonds); naive triple 1/(tr³) is disconnected; the residual "
                "does not track the genuine connected cumulant (b₃(T)≈b₃(³He)≈+0.94, "
                "b₄(⁴He)=−2.21, sign flip); the connected cumulant is NOT bar-even (I-par "
                "fail). No parameter-free connected-triple makes ⁴He the max. Constrains, does "
                "not close. No fit, no BW, no wiring.")
            wb.set_audit_only("docs/scope/2026-07-18-ka-additive-cluster-derivation.md")
            wb.add_data("discipline", "EXPLORATORY")
            wb.add_data("production_wired", False)
            wb.add_data("scope", "(a)")
            wb.add_data("mu_base", 1.0)
            wb.add_data("mu_ext_target", {K: float(MU[K]) for K in MU})
            wb.add_data("joint_traces_q0", {k: str(v) for k, v in tr0.items()})
            wb.add_data("gateA_producer_vs_cached_deuteron_rel", str(gateA))
            wb.add_data("kappa2_deuteron_anchored", float(kap2))
            wb.add_data("C2_per_isotope", {K: float(C2[K]) for K in C2})
            wb.add_data("C3_residual", {K: float(C3[K]) for K in C3})
            wb.add_data("connected_cumulant_c2", {k: float(v) for k, v in c2cum.items()})
            wb.add_data("connected_cumulant_b", {K: float(bconn[K]) for K in bconn})
            wb.add_data("connected_cumulant_b_qinv", {K: float(bconn_inv[K]) for K in bconn_inv})
            wb.add_data("C3_over_bconn_ratio", {K: float(ratios[K]) for K in ratios})
            wb.add_data("single_scale_fit", bool(single_scale))
            wb.add_data("parity_rel_diff", par)
            wb.add_data("parity_verdict", "NOT bar-even (I-par FAIL)" if not bar_even else "bar-even")
            wb.add_data("conn_verdict",
                        "naive 1/(tr^3) disconnected (cumulant=0); genuine joint-trace "
                        "cumulant well-defined but residual does not track it")
            wb.add_data("A_locality_C3_D", float(C3["D"]))
            wb.add_data("he4_max_reproduced", bool(he4_max_ok))
            wb.add_data("junk_control",
                        {"C3_over_triplecount": {K: float(jr[K]) for K in jr},
                         "junk_spread": float(jspread),
                         "cumulant_spread": float(rspread),
                         "cumulant_beats_junk": bool(float(rspread) < float(jspread))})
            wb.add_data("final_verdict", verdict)
            wb.add_assertion(
                name="residual_is_clean_connected_triple",
                computed=str(int(bool(lead))), expected="1", tolerance=0,
                source="LEAD iff residual C₃ tracks a single-scale, bar-even, ⁴He-max, "
                       "junk-beating connected cumulant. It does NOT (see final_verdict).")
            wb.add_assertion(
                name="A_locality_C3_D_zero",
                computed=str(float(C3["D"])), expected="0", tolerance=1e-30,
                source="deuteron has no triple ⇒ C₃(D)=0 exactly (the one gate that passes).")
            wb.add_data("allPassed", bool(lead))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
