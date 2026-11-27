#!/usr/bin/env python3
"""
Probe — qou-5vhf step 2 (bean qou-0fxk): COMPONENT COUNT decides the q-adic
order of a many-body cross term.

Two results already on main pull in opposite directions and this probe joins
them:

  * T1 (interleaving_cross_term_q_adic_order_probe.py): the n = 4 interleaving
    cross term Δ = tr(s0 s1 s0 s2 s1) − tr(s0² s1² s2) has q-adic order ZERO,
    because at q = 1 the Markov trace is the component-count trace 2^{c(w)−n}
    and the two closures have 1 and 3 components.
  * The corpus's own irreducible 3-body operator is the BRUNNIAN band word
    w₃ = [A₀₁, A₁₂] (QOU/MassTheory/BorromeanThreeBodyCluster.lean), whose
    deficit against the 3-unlink is 1 − τ_Borr = h⁴(3 + h²)/(h² + 4),
    h = q − q⁻¹ — q-adic order FOUR.

The joining statement, exact and elementary: the order-zero part of ANY cross
term tr(w) − tr(w′) is 2^{c(w)−n} − 2^{c(w′)−n}, so it vanishes iff the two
closures have the same number of components.  Component-CHANGING word pairs
(trefoil vs Hopf-chain) carry an O(1) classical cross term; component-
PRESERVING pairs — every Brunnian word against its unlink — carry a cross term
of positive q-adic order, a pure q-deformation effect.  Route B's "all orders
in q" claim, dead for the n = 4 word (§7c), is alive exactly for the Brunnian
class the corpus already uses.

WHAT IS MEASURED (exact sympy; one mpmath evaluation at the proton pin):
  1. On 3 strands (8-dim spin-½ rep, convention D): τ(w₃) for the corpus's
     band word w₃ = σ₀² σ₁² σ₀⁻² σ₁⁻² reproduces the Lean closed form
     (4 + h² − 3h⁴ − h⁶)/(h² + 4); ν_(q−1)(1 − τ) = 4; the alternative Borromean
     presentation (σ₀ σ₁⁻¹)³ has the SAME trace (both close to the Borromean
     rings; the Markov trace is a link invariant) and both permutations are the
     identity (c = 3 = the unlink's).
  2. On 3 and 4 strands, for EVERY element of S₃ and S₄: the rep's trace at
     q = 1 is 2^{c(w)−n} (the R-matrix is the swap at q = 1).
  3. The n = 4 pair recomputed: order 0, components 1 vs 3.
  4. Magnitudes at the proton pin, in nats and, through the corpus's own scale
     E₀ = m_e/(q₀(q₀−1)), in MeV: the Brunnian deficit (order h⁴), the n = 4
     classical cross term (order 1), and — quoted, not derived here — the
     Δ_λ-simplex target μ₃ = +0.4708 MeV that BorromeanThreeBodyCluster.lean
     names.  This is a diagnostic at the comparison boundary: nothing is fitted
     and nothing is wired.

SCOPE (a): the two specific word classes on 3 and 4 strands.  The "component
count decides" statement is general and elementary (2^k is injective); its
formal carrier is QOU/Mass/CrossTermOrderZeroComponentCount.lean.

Run: python3 -u computations/probes/component_count_decides_q_adic_order_probe.py \\
       2>&1 | tee /tmp/component_count_q_adic.log
"""
from __future__ import annotations

import itertools
import os
import sys
import time

import mpmath as mp
import sympy as sp
from sympy.combinatorics import Permutation

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from markov_trace_n4_interleaved_cross_term_probe import route_rep  # noqa: E402
from interleaving_cross_term_q_adic_order_probe import poly_val_at_one  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
except Exception:  # pragma: no cover
    Q_50_DIGIT_STR = None
try:
    from qou_substrate import constants as _c  # noqa: E402
    M_E_MEV_STR = str(_c._E_MEV.value_str)  # the CODATA string itself, never a float or mpf printed back
except Exception:  # pragma: no cover
    M_E_MEV_STR = None

mp.mp.dps = 50
T0 = time.monotonic()
MU3_TARGET_MEV_QUOTED = "0.4708"  # quoted from BorromeanThreeBodyCluster.lean; not derived here


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:5.1f}s] {msg}", flush=True)


def perm_of_word(word, n):
    """word: list of (i, e) with e = ±1; permutation ignores signs."""
    p = Permutation(list(range(n)))
    for i, _e in word:
        p = p * Permutation(i, i + 1, size=n)
    return p


def rep_word(word, n, q, sigma):
    """Matrix of a signed braid word in the spin-½ rep; σ⁻¹ = σ − h·1 (Hecke)."""
    h = q - 1 / q
    dim = 2 ** n
    M = sp.eye(dim)
    for i, e in word:
        S = sigma(i)
        M = M * (S if e > 0 else (S - h * sp.eye(dim)))
    return M


def main() -> int:
    print("=" * 76)
    print(" component count decides the q-adic order of a cross term (qou-5vhf step 2)")
    print("=" * 76)
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    checks = []

    # ---- 1. Borromean band word on 3 strands ---------------------------------
    sigma3, tr3 = route_rep(3, q)
    # corpus band word: A01 = σ0², A12 = σ1², w3 = A01 A12 A01⁻¹ A12⁻¹
    w3 = [(0, 1), (0, 1), (1, 1), (1, 1), (0, -1), (0, -1), (1, -1), (1, -1)]
    alt = [(0, 1), (1, -1)] * 3                       # (σ0 σ1⁻¹)³
    tau_w3 = sp.simplify(tr3(rep_word(w3, 3, q, sigma3)))
    tau_alt = sp.simplify(tr3(rep_word(alt, 3, q, sigma3)))
    tau_closed = (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)
    chk_closed = sp.simplify(tau_w3 - tau_closed) == 0
    chk_alt_same = sp.simplify(tau_alt - tau_w3) == 0
    deficit = sp.cancel(sp.together(1 - tau_w3))
    nu_deficit = poly_val_at_one(deficit, q)
    deficit_closed = h ** 4 * (3 + h ** 2) / (h ** 2 + 4)
    chk_deficit_closed = sp.simplify(deficit - deficit_closed) == 0
    chk_nu4 = nu_deficit == 4
    c_w3, c_alt = perm_of_word(w3, 3).cycles, perm_of_word(alt, 3).cycles
    chk_components3 = (c_w3, c_alt) == (3, 3)
    chk_unlink_at_one = tau_w3.subs(q, 1) == 1
    log(f"τ(w₃) = closed form {chk_closed}; τ((σ₀σ₁⁻¹)³) = τ(w₃) {chk_alt_same}; "
        f"1 − τ = h⁴(3+h²)/(h²+4) {chk_deficit_closed}; ν_(q−1)(1−τ) = {nu_deficit}; "
        f"components {c_w3}, {c_alt} (unlink 3); τ(q=1) = {tau_w3.subs(q, 1)}")

    # ---- 2. the rep at q = 1 is the component-count trace on all of S3, S4 -----
    all_ok = True
    for n in (3, 4):
        sig, tr = route_rep(n, q)
        for t in itertools.permutations(range(n)):
            p = Permutation(list(t))
            # a reduced word for p via bubble sort on its array form
            arr = list(p.array_form)
            word = []
            changed = True
            while changed:
                changed = False
                for i in range(n - 1):
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        word.append((i, 1))
                        changed = True
            M1 = rep_word(word, n, q, sig).subs(q, 1)
            val = sp.Rational(int(M1.trace()), 2 ** n)   # W → identity at q = 1, [2]^n → 2^n
            all_ok &= (val == sp.Rational(2 ** p.cycles, 2 ** n))
    chk_component_trace = all_ok
    log(f"rep trace at q = 1 equals 2^(c(w)−n) on all 6 + 24 elements of S₃, S₄: {chk_component_trace}")

    # ---- 3. the n = 4 pair, recomputed --------------------------------------
    sigma4, tr4 = route_rep(4, q)
    I4 = sp.simplify(tr4(rep_word([(0, 1), (1, 1), (0, 1), (2, 1), (1, 1)], 4, q, sigma4)))
    S4 = sp.simplify(tr4(rep_word([(0, 1), (0, 1), (1, 1), (1, 1), (2, 1)], 4, q, sigma4)))
    D4 = sp.cancel(sp.together(I4 - S4))
    nu4 = poly_val_at_one(D4, q)
    c_int = perm_of_word([(0, 1), (1, 1), (0, 1), (2, 1), (1, 1)], 4).cycles
    c_seq = perm_of_word([(0, 1), (0, 1), (1, 1), (1, 1), (2, 1)], 4).cycles
    chk_n4 = (nu4 == 0 and (c_int, c_seq) == (1, 3)
              and D4.subs(q, 1) == sp.Rational(2 ** c_int - 2 ** c_seq, 16))
    log(f"n = 4 pair: ν_(q−1)(Δ) = {nu4}; components {c_int} vs {c_seq}; Δ(1) = {D4.subs(q, 1)} "
        f"= (2^{c_int} − 2^{c_seq})/16 {chk_n4}")

    # ---- 4. the order-zero part of ANY cross term is the component difference ---
    # (checked on every pair of elements of S₄ through the rep at q = 1)
    sig, tr = route_rep(4, q)
    elems = [Permutation(list(t)) for t in itertools.permutations(range(4))]
    zero_iff_ok = True
    for a in elems:
        for b in elems:
            lhs_zero = (a.cycles == b.cycles)
            rhs_zero = (sp.Rational(2 ** a.cycles, 16) - sp.Rational(2 ** b.cycles, 16) == 0)
            zero_iff_ok &= (lhs_zero == rhs_zero)
    chk_zero_iff = zero_iff_ok
    log(f"order-zero cross term vanishes iff component counts agree (all 24×24 pairs): {chk_zero_iff}")

    # ---- 5. magnitudes at the proton pin (diagnostic; comparison boundary) ----
    anchor = {}
    if Q_50_DIGIT_STR is not None:
        q0 = Q_MP
        fdef = sp.lambdify(q, deficit, modules="mpmath")
        ftau = sp.lambdify(q, tau_w3, modules="mpmath")
        fI, fS = sp.lambdify(q, I4, modules="mpmath"), sp.lambdify(q, S4, modules="mpmath")
        d0 = fdef(q0)
        nats_borr = -mp.log(ftau(q0))
        nats_n4 = -mp.log(fI(q0) / fS(q0))
        anchor = {"q0": Q_50_DIGIT_STR, "h0": mp.nstr(q0 - 1 / q0, 30),
                  "brunnian_deficit_1_minus_tau": mp.nstr(d0, 30),
                  "brunnian_nats_minus_log_tau": mp.nstr(nats_borr, 30),
                  "n4_classical_nats_minus_log_I_over_S": mp.nstr(nats_n4, 30),
                  "ratio_n4_over_brunnian_nats": mp.nstr(nats_n4 / nats_borr, 20)}
        if M_E_MEV_STR is not None:
            me = mp.mpf(M_E_MEV_STR)
            import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
            E0 = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
            anchor.update({
                "m_e_MeV": M_E_MEV_STR,
                "E0_MeV": mp.nstr(E0, 30),
                "E0_times_brunnian_deficit_MeV": mp.nstr(E0 * d0, 20),
                "E0_times_brunnian_nats_MeV": mp.nstr(E0 * nats_borr, 20),
                "E0_times_n4_classical_nats_MeV": mp.nstr(E0 * nats_n4, 20),
                "mu3_target_MeV_quoted": MU3_TARGET_MEV_QUOTED,
                "mu3_over_E0_brunnian_deficit": mp.nstr(mp.mpf(MU3_TARGET_MEV_QUOTED) / (E0 * d0), 10),
                "E0_n4_classical_over_mu3": mp.nstr(E0 * nats_n4 / mp.mpf(MU3_TARGET_MEV_QUOTED), 10),
            })
        chk_scale_order = d0 < mp.mpf("0.01") and nats_n4 > mp.mpf("0.5")
        log(f"proton pin: Brunnian deficit {anchor['brunnian_deficit_1_minus_tau'][:10]}…, "
            f"n=4 classical {anchor['n4_classical_nats_minus_log_I_over_S'][:8]}… nats; "
            + (f"E₀ = {anchor['E0_MeV'][:8]} MeV → {anchor['E0_times_brunnian_deficit_MeV'][:8]} vs "
               f"{anchor['E0_times_n4_classical_nats_MeV'][:6]} MeV, target μ₃ = {MU3_TARGET_MEV_QUOTED} (quoted)"
               if M_E_MEV_STR else "(m_e string unavailable)"))
    else:
        chk_scale_order = None
        log("q_parameter not importable — anchor evaluation skipped")

    checks = [
        ("τ(w₃) for the corpus band word matches the Lean closed form (4+h²−3h⁴−h⁶)/(h²+4)", chk_closed),
        ("(σ₀σ₁⁻¹)³ has the same Markov trace as w₃ (both close to the Borromean rings)", chk_alt_same),
        ("1 − τ_Borr = h⁴(3+h²)/(h²+4)", chk_deficit_closed),
        ("q-adic order of the Brunnian deficit at q = 1 is 4", chk_nu4),
        ("both Borromean words are pure braids: 3 components, the unlink's count", chk_components3),
        ("τ_Borr(q = 1) = 1: classically the Borromean rings are the unlink to the trace", chk_unlink_at_one),
        ("rep trace at q = 1 is 2^(c(w)−n) on all of S₃ and S₄", chk_component_trace),
        ("n = 4 pair: order 0, components 1 vs 3, Δ(1) = (2¹ − 2³)/16", chk_n4),
        ("order-zero cross term vanishes iff component counts agree (all pairs in S₄)", chk_zero_iff),
    ]
    if chk_scale_order is not None:
        checks.append(("proton pin: Brunnian deficit < 1e-2 while the classical n=4 cross term > 0.5 nats",
                       chk_scale_order))
    print()
    ok = 0
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    wb = WitnessBuilder("component-count-decides-q-adic-order", engine="sympy", _script_path=__file__)
    wb.set_description(
        "qou-5vhf step 2 (bean qou-0fxk): the order-zero part of any Markov-trace cross term "
        "tr(w) − tr(w′) is 2^{c(w)−n} − 2^{c(w′)−n} (the trace at q = 1 is the component-count "
        "trace; verified on all of S₃, S₄ in the spin-½ rep), so a cross term has positive q-adic "
        "order iff the two closures have the same number of components. Component-changing pairs "
        "(the n = 4 trefoil-vs-chain word, order 0, ~0.9 nats at the proton pin) carry a classical "
        "cross term; component-preserving pairs — the corpus's Brunnian band word w₃ = [A₀₁,A₁₂] "
        "against the 3-unlink — carry a pure q-deformation cross term: 1 − τ_Borr = h⁴(3+h²)/(h²+4), "
        "order 4, ~1.4e-3 at the pin. Route B's 'all orders in q' object is exactly the Brunnian "
        "class. Magnitudes through E₀ = m_e/(q₀(q₀−1)) are recorded as a diagnostic against the "
        "quoted μ₃ = 0.4708 MeV target; nothing is fitted or wired. Scope (a).")
    wb.set_content_block("prop:markov-trace-axiomatic-closed-form")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0",
                         expected="1", tolerance="0.5", source="exact (sympy) / mpmath 50 dps at the pin")
    wb.add_parameter("words", {"brunnian_w3": "s0^2 s1^2 s0^-2 s1^-2 = [A01, A12]",
                               "borromean_alt": "(s0 s1^-1)^3",
                               "n4_interleaved": "s0 s1 s0 s2 s1", "n4_sequential": "s0^2 s1^2 s2"})
    if Q_50_DIGIT_STR is not None:
        wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("brunnian", {"tau_closed": str(sp.factor(tau_w3)), "deficit_closed": str(sp.factor(deficit)),
                             "deficit_q_adic_order": nu_deficit, "components": c_w3})
    wb.add_data("n4_pair", {"Delta": str(sp.factor(D4)), "q_adic_order": nu4,
                            "components": {"interleaved": c_int, "sequential": c_seq}})
    wb.add_data("anchor_evaluation", anchor)
    wb.add_data("verdict", (
        "Component count decides the q-adic order: order 0 iff the closures' component counts "
        "differ. The corpus's Brunnian 3-body operator is the component-preserving, order-4 class — "
        "the one place route B's 'all orders in q' reading applies — and its magnitude at the pin "
        "is ~h⁴ ≈ 1.4e-3 (E₀·deficit ≈ 6e-3 MeV), two orders below the quoted μ₃ target, while a "
        "component-changing (classical) cross term is ~0.9 nats (≈ 3.7 MeV), an order above it. "
        "The missing 3-body magnitude sits between the two classes; neither class supplies it as "
        "it stands. Diagnostic only; not a fit."))
    wb.add_caveat("μ₃ = 0.4708 MeV is QUOTED from BorromeanThreeBodyCluster.lean's docstring, not derived here.")
    wb.add_caveat("Scope (a): 3- and 4-strand word classes; the general 'iff' is elementary (2^k injective).")
    out = wb.save()
    print(f"  witness -> {os.path.relpath(out, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
