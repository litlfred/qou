#!/usr/bin/env python3
"""Which weight family does the Magnus Ω₂ pairing OBEY a stabilisation law under?
Derived first, then measured. (bean qou-gba1 — option E; parent qou-za3q dec. 1)

THE QUESTION THIS ANSWERS, AND WHY IT IS NOT A MATTER OF TASTE
--------------------------------------------------------------
`qou-za3q` decision 1 asks which partition weight the pairing

    P_w(β) = Σ_λ w(λ) · tr( ρ(β)_λ · Ω₂(β)_λ )

should use. Two candidates are in play and they DISAGREE ON THE ANSWER, not
merely on a number: the quantum Plancherel measure d_q(λ)²/[n]_q! gives
−, +, + over A = 2, 3, 4 (one sign change) and the production Wenzl weight
gives −, −, − (none), so the programme's target A-dependent sign change exists
under one and not the other. Options A–D each PICK one and defend it. Option E
is supposed to DERIVE it. This probe is E's first bounded deliverable.

The derivation does not appeal to convention. A nucleus is a LINK; a braid word
is only a presentation of it, and two words related by a Markov move present the
same link. So a functional that is to be a property of the nucleus must respect
those moves. The Markov trace on ⋃_n H_n(q) is *characterised* (Jones–Ocneanu)
by exactly three axioms —

    (1) tr_n(1) = 1
    (2) tr_n(xy) = tr_n(yx)
    (3) tr_{n+1}(x·σ_{n-1}) = z · tr_n(x)    for x ∈ H_n      ← STABILISATION

— and the Wenzl y_λ are the weights that realise them, with z = q³/(q²+1)
under convention D (`closed_form_tau_M.markov_z`, owner ruling 2026-08-09).
The Plancherel measure satisfies NEITHER (1) — its tr(1) is 11.1 / 184.2 /
6751.5 at n = 6 / 9 / 12 — NOR (3), because it has no z at all.

Axiom (3) is the one that matters here, because stabilisation is precisely the
move that changes n, and n = 3A. A cross-A statement is a statement across
stabilisations.

WHAT THE ALGEBRA PREDICTS BEFORE ANY ARITHMETIC RUNS
----------------------------------------------------
Take β ∈ B_n on generators σ_0..σ_{n-2} and its positive stabilisation
β' = β·σ_{n-1} ∈ B_{n+1}. Then ρ' = ρ·σ_{n-1}, and

    Ω₂(β') = Ω₂(β) + ½ Σ_{i} [A_{g_i}, A_{n-1}]

over the crossings i of β. Far-commutativity ([A_a,A_b] = 0 for |a−b| ≥ 2)
kills every term except those with g_i = n−2, so the increment is exactly

    ΔΩ₂ = ½ · m · [A_{n-2}, A_{n-1}],     m = multiplicity of σ_{n-2} in β.

Now split the pairing. Ω₂(β)·ρ lies in H_n, so by cyclicity and axiom (3)

    tr_{n+1}( ρ σ_{n-1} · Ω₂(β) ) = tr_{n+1}( Ω₂(β) ρ · σ_{n-1} )
                                  = z · tr_n( Ω₂(β) ρ )
                                  = z · tr_n( ρ Ω₂(β) ).

So the pairing does NOT satisfy a clean Markov law — the new crossing
contributes a genuine new term — but it satisfies an EXACT one:

    ┌──────────────────────────────────────────────────────────────┐
    │  P_y(β σ_{n-1})  =  z · P_y(β)  +  (m/2) · Σ_λ y_λ           │
    │                          tr( ρ'_λ · [A_{n-2}, A_{n-1}]_λ )   │
    └──────────────────────────────────────────────────────────────┘

with z = q³/(q²+1) FIXED, not fitted. Every quantity on the right is
independently computable, so this is a prediction with no free parameter.

Under Plancherel there is no z, so there is no such identity to state. That
asymmetry is the derivation: **the Ω₂ pairing has an exact stabilisation law
under the Wenzl weight and none under Plancherel.**

WHAT IS MEASURED HERE
---------------------
  CONTROL (must pass, or the harness is wrong and nothing else may be read):
    * tr(1) = 1 exactly under Wenzl at every n; ≠ 1 under Plancherel.
    * The RAW trace obeys axiom (3): T_y(βσ) = z·T_y(β) exactly. This is a
      known fact, used here as a positive control on the implementation.
    * The raw trace does NOT obey it under Plancherel — negative control. A
      "no z works" claim is worth nothing unless z is searched for, so the
      best-fit ratio is reported and shown to move between words.
  THE QUESTION:
    * Does the boxed identity hold, numerically, at the working precision?

HONESTY (STRICT). scope-(a): a structural identity about the pairing, checked
numerically at the proton q₀ on the canonical deuteron word and its
stabilisations. It does NOT choose the pairing by which answer it yields — the
sign never enters the test. It does NOT reproduce any MeV. It does not by
itself close qou-za3q decision 1: axiom (3) is a NECESSARY condition for a
link functional, and this shows the Wenzl arm meets it while Plancherel has no
analogue, which is an argument from principle rather than a proof that the
binding functional must be a link invariant. That last premise is stated, not
derived, and is where the remaining work sits. NO-FLOAT64: mpmath end to end.
"""
from __future__ import annotations

import os
import sys
from math import prod

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

set_compute_dps()
mp.mp.dps = 140

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0 = mp.mpf(_Q0_RESOLVED)
H = Q0 - 1 / Q0
EPS = mp.mpf(10) ** -50
_EXACT = mp.mpf(10) ** -30


def markov_z(q):
    """z(q) = q³/(q²+1) — registry convention D. Mirrors closed_form_tau_M."""
    return q ** 3 / (q ** 2 + 1)


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def q_int(k, q):
    if q == 1:
        return mp.mpf(k)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def w_planch(shape, q):
    """**quantum Plancherel** measure d_q(λ)²/[n]_q!.

    NOT the Wenzl y_λ — the two are distinct at q ≠ 1 and AGENTS.md forbids
    conflating them. Named for the family it computes, per
    `computations/audits/y_lambda_conflation_audit.py`.
    """
    n = sum(shape)
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            hooks.append((ri - j - 1) + (cols[j] - i - 1) + 1)
    nfact = prod(q_int(k, q) for k in range(1, n + 1))
    dq = nfact / prod(q_int(hh, q) for hh in hooks)
    return (dq * dq) / nfact


def germ_matrices(shape):
    """(sig, A, dim) at q₀. A_g = q(∂_q σ_g)σ_g⁻¹, central finite difference.

    Validates the differentiated Hecke identity per generator, as the sibling
    Magnus probes do — the germ is the one object here that is not exact
    arithmetic, so it is checked rather than trusted.
    """
    sig, dim, _ = build_seminormal_matrices_mp(shape, Q0)
    if dim == 1:
        return sig, {}, dim
    sig_p, _, _ = build_seminormal_matrices_mp(shape, Q0 + EPS)
    sig_m, _, _ = build_seminormal_matrices_mp(shape, Q0 - EPS)
    hp = 1 + 1 / Q0 ** 2
    A = {}
    for g in range(len(sig)):
        dsig = (sig_p[g] - sig_m[g]) / (2 * EPS)
        A[g] = Q0 * dsig * mp.inverse(sig[g])
        lhs = sig[g] * dsig + dsig * sig[g]
        rhs = hp * sig[g] + H * dsig
        resid = sum(abs(lhs[r, c] - rhs[r, c]) for r in range(dim) for c in range(dim))
        assert resid < mp.mpf(10) ** -60, f"germ Hecke check failed: {shape} g={g}"
    return sig, A, dim


def _net_pairs(gens):
    """Folded Ω₂ pair table: {(a<b): net coefficient}, far-commutativity applied."""
    net: dict[tuple[int, int], int] = {}
    for i in range(len(gens)):
        for j in range(i + 1, len(gens)):
            a, b = gens[i], gens[j]
            if a == b or abs(a - b) >= 2:
                continue
            key = (a, b) if a < b else (b, a)
            net[key] = net.get(key, 0) + (1 if a < b else -1)
    return {k: v for k, v in net.items() if v}


def evaluate(gens, n, extra_comm=None):
    """Both arms of the pairing for a word, plus the raw trace and tr(1).

    `extra_comm` = (a, b): also accumulate Σ_λ w(λ) tr(ρ_λ [A_a,A_b]_λ), the
    correction term the boxed stabilisation identity predicts.
    """
    net = _net_pairs(gens)
    out = {k: mp.mpf(0) for k in
           ("P_y", "P_w", "T_y", "T_w", "one_y", "one_w", "C_y", "C_w")}
    for shape in partitions(n):
        # dps=mp.mp.dps, NOT a literal. `y_lambda_wenzl_bridge_numeric`
        # assigns `mp.mp.dps = dps` GLOBALLY and never restores it, so a
        # literal 50 here silently drops the working precision to 50 and
        # destroys the EPS=1e-50 finite-difference germ computed below.
        # Caught, not guessed: the germ's differentiated-Hecke check
        # asserted on shape (5,1) the first time this was written that way.
        yl = y_lambda_wenzl_bridge_numeric(shape, Q0, dps=mp.mp.dps)
        wl = w_planch(shape, Q0)
        sig, A, dim = germ_matrices(shape)
        out["one_y"] += yl * dim
        out["one_w"] += wl * dim

        rho = mp.eye(dim)
        for g in gens:
            rho = rho * sig[g]
        tr_rho = sum(rho[i, i] for i in range(dim))
        out["T_y"] += yl * tr_rho
        out["T_w"] += wl * tr_rho

        if dim == 1:
            continue                      # every commutator vanishes on a 1×1

        Om2 = mp.zeros(dim, dim)
        for (a, b), c in net.items():
            Om2 += mp.mpf(c) / 2 * (A[a] * A[b] - A[b] * A[a])
        M = rho * Om2
        tr_M = sum(M[i, i] for i in range(dim))
        out["P_y"] += yl * tr_M
        out["P_w"] += wl * tr_M

        if extra_comm is not None:
            a, b = extra_comm
            if a in A and b in A:
                K = rho * (A[a] * A[b] - A[b] * A[a])
                tr_K = sum(K[i, i] for i in range(dim))
                out["C_y"] += yl * tr_K
                out["C_w"] += wl * tr_K
    return out


def main() -> int:
    from mass_at_3A_proper import atom_braid_word_3A
    from witness_base import WitnessBuilder

    z = markov_z(Q0)
    gens = [int(t[2]) for t in atom_braid_word_3A(1, 1)]     # deuteron, σ₀..σ₄
    n0 = max(gens) + 2                                        # 6 strands

    print(f"  q₀ = {mp.nstr(Q0, 17)}   z = q³/(q²+1) = {mp.nstr(z, 20)}")
    print(f"  deuteron word: {len(gens)} crossings on σ₀..σ{max(gens)}, "
          f"n = {n0}\n")

    steps = []
    prev = evaluate(gens, n0)
    print(f"  n={n0:2d}  tr(1): Wenzl {mp.nstr(prev['one_y'], 12):>16}   "
          f"Plancherel {mp.nstr(prev['one_w'], 12):>16}")

    cur_gens, cur_n = list(gens), n0
    for _ in range(2):                       # two successive stabilisations
        new_g = cur_n - 1                    # σ_{n-1} adds a strand
        m = sum(1 for g in cur_gens if g == new_g - 1)   # far-comm survivors
        nxt_gens = cur_gens + [new_g]
        nxt = evaluate(nxt_gens, cur_n + 1, extra_comm=(new_g - 1, new_g))

        # AXIOM (3) on the raw trace — the positive/negative control.
        raw_y = nxt["T_y"] - z * prev["T_y"]
        raw_w = nxt["T_w"] - z * prev["T_w"]
        # What z WOULD Plancherel need? Reported so "no z works" is a
        # measurement rather than an assertion: a family with a stabilisation
        # law has ONE z, so a ratio that moves between words has none.
        z_w_needed = (nxt["T_w"] / prev["T_w"]) if prev["T_w"] != 0 else mp.nan
        z_y_needed = (nxt["T_y"] / prev["T_y"]) if prev["T_y"] != 0 else mp.nan

        # THE QUESTION — the boxed identity.
        pred_y = z * prev["P_y"] + mp.mpf(m) / 2 * nxt["C_y"]
        pred_w = z * prev["P_w"] + mp.mpf(m) / 2 * nxt["C_w"]
        res_y = nxt["P_y"] - pred_y
        res_w = nxt["P_w"] - pred_w

        # FALSIFICATION CONTROL — could the identity have failed?
        #
        # An identity that holds is worth nothing if it holds for any input.
        # Both terms are already known to be load-bearing (the correction is
        # 40% and 15% of P at the two steps), but z itself must also be pinned.
        # Re-evaluate the same formula at the two wrong values that a reader
        # might reasonably substitute:
        #   z = q       the competing Markov root, degenerate (y_(2,1) = 0, not
        #               faithful on TL_3) and named in markov_z's own docstring;
        #   z = 1       no stabilisation scaling at all.
        # If either reproduced P, the test would be bookkeeping rather than a
        # measurement of z.
        wrong = {}
        for label, zz in (("z_eq_q", Q0), ("z_eq_1", mp.mpf(1))):
            pw = zz * prev["P_y"] + mp.mpf(m) / 2 * nxt["C_y"]
            wrong[label] = abs(nxt["P_y"] - pw) / abs(nxt["P_y"])

        def rel(r, ref):
            return abs(r) / abs(ref) if ref != 0 else abs(r)

        print(f"\n  ── stabilise: append σ{new_g}   n {cur_n} → {cur_n + 1}   "
              f"m(σ{new_g - 1}) = {m}")
        print(f"     tr(1)        Wenzl {mp.nstr(nxt['one_y'], 12):>16}   "
              f"Plancherel {mp.nstr(nxt['one_w'], 12):>16}")
        print(f"     raw trace    T_y  {mp.nstr(nxt['T_y'], 12):>16}   "
              f"z·T_y(prev) {mp.nstr(z * prev['T_y'], 12):>16}   "
              f"resid {mp.nstr(rel(raw_y, nxt['T_y']), 6)}")
        print(f"                  T_w  {mp.nstr(nxt['T_w'], 12):>16}   "
              f"z·T_w(prev) {mp.nstr(z * prev['T_w'], 12):>16}   "
              f"resid {mp.nstr(rel(raw_w, nxt['T_w']), 6)}")
        print(f"     z implied by the raw trace:  Wenzl "
              f"{mp.nstr(z_y_needed, 20)}   Plancherel {mp.nstr(z_w_needed, 20)}")
        print(f"     PAIRING      P_y  {mp.nstr(nxt['P_y'], 12):>16}   "
              f"predicted {mp.nstr(pred_y, 12):>16}   "
              f"rel resid {mp.nstr(rel(res_y, nxt['P_y']), 6)}")
        print(f"     falsification: same law at z=q "
              f"{mp.nstr(wrong['z_eq_q'], 6)}   at z=1 "
              f"{mp.nstr(wrong['z_eq_1'], 6)}   (both must be large)")
        print(f"                  P_w  {mp.nstr(nxt['P_w'], 12):>16}   "
              f"predicted {mp.nstr(pred_w, 12):>16}   "
              f"rel resid {mp.nstr(rel(res_w, nxt['P_w']), 6)}")

        steps.append({
            "n_from": cur_n, "n_to": cur_n + 1, "appended_generator": new_g,
            "m_far_comm_survivors": m,
            "tr_one_wenzl": fmt(nxt["one_y"]), "tr_one_plancherel": fmt(nxt["one_w"]),
            "raw_trace_wenzl": fmt(nxt["T_y"]),
            "raw_trace_plancherel": fmt(nxt["T_w"]),
            "raw_markov_residual_rel_wenzl": fmt(rel(raw_y, nxt["T_y"])),
            "raw_markov_residual_rel_plancherel": fmt(rel(raw_w, nxt["T_w"])),
            "z_implied_wenzl": fmt(z_y_needed),
            "z_implied_plancherel": fmt(z_w_needed),
            "P_wenzl": fmt(nxt["P_y"]), "P_wenzl_predicted": fmt(pred_y),
            "P_wenzl_residual_rel": fmt(rel(res_y, nxt["P_y"])),
            "P_plancherel": fmt(nxt["P_w"]), "P_plancherel_predicted": fmt(pred_w),
            "P_plancherel_residual_rel": fmt(rel(res_w, nxt["P_w"])),
            "correction_term_wenzl": fmt(mp.mpf(m) / 2 * nxt["C_y"]),
            "falsification_rel_resid_at_z_eq_q": fmt(wrong["z_eq_q"]),
            "falsification_rel_resid_at_z_eq_1": fmt(wrong["z_eq_1"]),
        })
        prev, cur_gens, cur_n = nxt, nxt_gens, cur_n + 1

    tol = mp.mpf(10) ** -25
    one_ok = abs(prev["one_y"] - 1) < _EXACT
    raw_ok = all(mp.mpf(s["raw_markov_residual_rel_wenzl"]) < tol for s in steps)
    raw_planch_fails = all(mp.mpf(s["raw_markov_residual_rel_plancherel"]) > tol
                           for s in steps)
    z_planch_moves = (abs(mp.mpf(steps[0]["z_implied_plancherel"])
                          - mp.mpf(steps[1]["z_implied_plancherel"])) > tol)
    pair_ok = all(mp.mpf(s["P_wenzl_residual_rel"]) < tol for s in steps)
    falsifiable = all(mp.mpf(s["falsification_rel_resid_at_z_eq_q"]) > tol
                      and mp.mpf(s["falsification_rel_resid_at_z_eq_1"]) > tol
                      for s in steps)

    print(f"\n  tr(1) = 1 under Wenzl                       : {one_ok}")
    print(f"  raw trace obeys axiom (3) under Wenzl       : {raw_ok}   (control)")
    print(f"  raw trace FAILS axiom (3) under Plancherel  : {raw_planch_fails}   (control)")
    print(f"  the z Plancherel would need MOVES word→word : {z_planch_moves}   (control)")
    print(f"  PAIRING obeys the derived law under Wenzl   : {pair_ok}   ← the question")
    print(f"  ...and FAILS it at z=q and at z=1           : {falsifiable}   (falsification)")

    wb = WitnessBuilder("magnus-omega2-markov-stabilisation", engine="mpmath")
    wb.set_description(
        "Tests whether the Magnus Omega2 pairing obeys a stabilisation law "
        "under each candidate partition weight. Derived first: because "
        "Omega2(beta).rho lies in H_n, cyclicity plus the Markov axiom "
        "tr_{n+1}(x sigma_{n-1}) = z tr_n(x) forces "
        "P(beta sigma) = z P(beta) + (m/2) Sum_lambda w(lambda) "
        "tr(rho' [A_{n-2},A_{n-1}]) with z = q^3/(q^2+1) FIXED. Plancherel has "
        "no z, so no such identity exists to state for it. Bean qou-gba1, "
        "option E of qou-za3q decision 1."
    )
    wb.add_data("z_convention_D", fmt(z))
    wb.add_data("base_word", {"atom": "deuteron", "crossings": len(gens),
                              "n": n0, "source": "atom_braid_word_3A(1,1)"})
    wb.add_data("stabilisations", steps)
    wb.add_caveat(
        "The identity is a NECESSARY condition for the pairing to be a "
        "function of the link rather than of the braid word, not a proof that "
        "the binding functional must be a link invariant. That premise is "
        "stated, not derived, and is the remaining work in qou-gba1."
    )
    wb.add_caveat(
        "The sign of P never enters this test. The two weight families "
        "disagree on the sign at A=3 and A=4 (bean qou-za3q), so a criterion "
        "that used the sign would be selection against the target "
        "(AGENTS.md). Stabilisation covariance is independent of it."
    )
    wb.add_caveat(
        "Positive stabilisation only. The other Markov move, conjugation "
        "beta -> alpha beta alpha^-1, needs negative crossings, which this "
        "germ machinery does not build; it is untested here."
    )
    wb.add_assertion(name="tr_one_equals_one_under_wenzl",
                     computed=str(int(one_ok)), expected="1")
    wb.add_assertion(name="raw_trace_obeys_markov_axiom_under_wenzl",
                     computed=str(int(raw_ok)), expected="1")
    wb.add_assertion(name="raw_trace_fails_markov_axiom_under_plancherel",
                     computed=str(int(raw_planch_fails)), expected="1")
    wb.add_assertion(name="plancherel_has_no_fixed_z",
                     computed=str(int(z_planch_moves)), expected="1")
    wb.add_assertion(name="pairing_obeys_derived_stabilisation_law_under_wenzl",
                     computed=str(int(pair_ok)), expected="1")
    wb.add_assertion(name="law_fails_at_the_wrong_z_so_the_test_pins_z",
                     computed=str(int(falsifiable)), expected="1")
    print(f"  Witness: {wb.save()}")
    return 0 if (one_ok and raw_ok and raw_planch_fails and z_planch_moves
                 and pair_ok and falsifiable) else 1


if __name__ == "__main__":
    raise SystemExit(main())
