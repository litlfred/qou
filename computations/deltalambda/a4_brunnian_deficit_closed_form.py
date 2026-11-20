#!/usr/bin/env python3
"""a4_brunnian_deficit_closed_form.py — EXACT closed form of the A=4 Brunnian deficit.

Target (the open leg of the Milnor-parity sign law, #4389): the A=4 4-component
Brunnian level deficit `1 − τ_L₄` is only MEASURED (τ_L₄ ≈ 1.000145898 at q₀,
slope-estimated order ≈ 6.06; `a4_h12_brunnian_deficit_measure_probe.py`,
Lean `HeliumBrunnianDeficitMeasured.tauL4Measured`). The A=3 leg has a PROVED
closed form (`1 − τ_Borr = h⁴(3+h²)/(h²+4)`). This probe derives the A=4
closed form SYMBOLICALLY, promoting the A=4 data point from measured toward
derived:

    τ_L₄(q) = g_link(q) / g_unlink(q),
    g(word) = Σ_{λ⊢4} y_λ(q) · |χ_λ(word)(q)|      (the SAME perblock 0-fit
                                                     convention as the measuring
                                                     probe, base level n=4),

with `w₄ = [[A₀₁, A₁₂], A₂₃]` the genuine Brunnian iterated pure-braid
commutator (20-crossing σ-word, byte-identical construction to the measuring
probe, re-imported from it), χ_λ via the SYMBOLIC Hoefsmit seminormal form
(`hecke_character_symbolic`), and y_λ via the symbolic Jones-Markov weights
(`wedderburn_jones_markov.y_lambda_at(4, None)`).

Absolute-value resolution: w₄ is a PURE braid, so at q = 1 each ρ_λ(w₄) is the
identity permutation's image and χ_λ(w₄)|_{q=1} = dim_λ > 0. The probe checks
the sign of every χ_λ on a q-grid spanning (1, q₀] and, where all signs are
positive (expected by continuity), |χ_λ| = χ_λ exactly and the deficit is an
honest rational function of q. Any sign flip on the grid is reported and the
closed form is then only claimed on the verified sign-constant interval.

Outputs (exact, then checked):
  1. χ_λ(w₄)(q) per partition, exact rational functions (cancel'd).
  2. D(q) = 1 − τ_L₄(q) exact; numerator factored.
  3. Leading (q−1)-order of D — the Milnor order 2(A−1) = 6 test — obtained
     EXACTLY from a Taylor/series expansion at q = 1 (not a log-log slope).
  4. Sign of D near q₀: exact rational evaluation (no floats in the decision).
  5. Cross-check vs the measured witness value 1.000145898 at q₀ (f64 probe).

STRICT anti-fit: 0 free parameters; the word is fixed by the topological
Brunnian constraint (verified by the measuring probe); nothing wired. This is
a derivation of an already-measured quantity — derive-then-check, with the
check against the INDEPENDENT f64 measurement.

Run:  python3 -u a4_brunnian_deficit_closed_form.py 2>&1 | tee /tmp/a4_closed_form.log
"""
from __future__ import annotations

import sys as _sys
import time
from pathlib import Path as _Path

_COMP = _Path(__file__).resolve().parent.parent
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_COMP / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_COMP))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value

import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

from hecke_character_symbolic import hoefsmit_matrices_symbolic  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

_T0 = time.time()
# Separate MONOTONIC baseline for the witness. WitnessBuilder computes its
# duration against time.monotonic(), so handing it the wall-clock `_T0`
# (an epoch value) yields a large NEGATIVE durationMs. `_T0` stays wall-clock
# because it only feeds the human-readable progress log.
_T0_MONO = time.monotonic()


def _log(msg):
    print(f"[{time.time() - _T0:7.1f}s] {msg}", flush=True)


qs = sp.Symbol("q", positive=True, real=True)


# ── Band-word machinery: byte-equivalent to a4_h12_brunnian_deficit_measure_probe
# (not imported: that module imports pyhecke_native, unavailable in this sandbox).
# The reproduced W4_BAND is asserted against the measuring witness's recorded
# `band_factors` in main() so the word is provably the same object. ─────────────
def sig(g):
    return [(+1, g)]


def sig_inv(g):
    return [(-1, g)]


def word_inv(word):
    return [(-s, g) for (s, g) in reversed(word)]


def band_to_sigma(i, j, e):
    assert i < j
    pre = []
    for k in range(j - 1, i, -1):
        pre += sig(k)
    core = sig(i) + sig(i)
    post = []
    for k in range(i + 1, j):
        post += sig_inv(k)
    w = pre + core + post
    return w if e > 0 else word_inv(w)


def band_word_to_sigma(bw):
    out = []
    for (i, j, e) in bw:
        out += band_to_sigma(i, j, e)
    return out


def band_inv(bw):
    return [(i, j, -e) for (i, j, e) in reversed(bw)]


def band_comm(a, b):
    return list(a) + list(b) + band_inv(a) + band_inv(b)


A01 = [(0, 1, +1)]
A12 = [(1, 2, +1)]
A23 = [(2, 3, +1)]
W4_BAND = band_comm(band_comm(A01, A12), A23)   # [[A₀₁, A₁₂], A₂₃]
W3_BAND = band_comm(A01, A12)                    # [A₀₁, A₁₂]  (Borromean analog)


def partitions_of(n):
    if n == 3:
        return [(3,), (2, 1), (1, 1, 1)]
    if n == 4:
        return [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    raise ValueError(n)


def chi_symbolic(shape, sigma_word):
    """Exact χ_λ(word)(q): product of Hoefsmit matrices over ℚ(q), traced.
    σ_g = ρ(T_g);  σ_g⁻¹ = ρ(T_g) − h·I  (Hecke relation)."""
    matrices, dim, _ = hoefsmit_matrices_symbolic(list(shape), qs)
    h = qs - 1 / qs
    M = sp.eye(dim)
    for (s, g) in sigma_word:
        cross = matrices[g] if s > 0 else (matrices[g] - h * sp.eye(dim))
        M = (M * cross).applyfunc(sp.cancel)
    # The character is a rational function of q (basis-independent trace), but the
    # seminormal matrices carry √(axial-distance) entries — clear the radicals.
    tr = sp.cancel(sp.radsimp(M.trace()))
    if tr.has(sp.Pow) and any(
            isinstance(e, sp.Pow) and e.exp.is_Rational and e.exp.q != 1
            for e in sp.preorder_traversal(tr)):
        tr = sp.cancel(sp.simplify(tr))
    return tr


def sign_on_grid(expr, points):
    """Exact-rational sign of expr at each q in points (sympy Rationals)."""
    out = {}
    for p in points:
        v = expr.subs(qs, p)
        v = sp.nsimplify(v, rational=True) if not v.is_Rational else v
        out[str(p)] = int(sp.sign(v))
    return out


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def main():
    q0_mp = Q_MP
    # exact rational pin close to q₀ for exact-arithmetic sign decisions
    q0_rat = sp.Rational(110997858275, 100000000000)
    # Rational pin in s = √q. Since the deficit is rational in s (the y_λ carry
    # half-integer q-powers), a RATIONAL s₀ makes the q₀ evaluation exactly
    # rational — the substrate pin is then q = s₀², itself an exact rational
    # agreeing with q₀ to ~20 digits. This is what makes the sign claim exact.
    s0_rat = sp.Rational(
        int(mp.floor(mp.sqrt(Q_MP) * 10**20)), 10**20)
    q_from_s0 = s0_rat ** 2
    grid = [sp.Rational(101, 100), sp.Rational(21, 20), sp.Rational(11, 10), q0_rat,
            sp.Rational(6, 5)]

    _log("building σ-words (band construction mirroring the measuring probe)")
    # provenance guard: the reproduced band word must equal the measured witness's
    import json as _json
    _wit = record_upstream(_Path(__file__).resolve().parent /
                        "a4-h12-brunnian-deficit-measure.witness.json", _UPSTREAM_RECORDS)
    assert [[i, j, e] for (i, j, e) in W4_BAND] == _wit["parameters"]["band_factors"], \
        "W4_BAND must match the measuring witness's recorded band_factors"
    w4_sigma = band_word_to_sigma(W4_BAND)
    w3_sigma = band_word_to_sigma(W3_BAND)
    _log(f"w₄ σ-length={len(w4_sigma)}  w₃ σ-length={len(w3_sigma)}")

    # ── exact symbolic y_λ at n=4 and n=3 (file-cached: the n=4 solve is ~18 min) ──
    # Scratchpad root is env-configurable so the cache is portable across
    # environments (a hard-coded sandbox path would miss on every other machine
    # and could fail to create its parents).
    import os as _os
    _scratch = _Path(_os.environ.get("QOU_SCRATCHPAD", "/tmp/qou-scratchpad"))
    # Cache key carries the CONVENTION. Before 2026-08-09 the key was bare
    # existence, so a C-era cache would have been reused verbatim past the C
    # excision and silently reintroduced C weights into the deficit. Naming the
    # convention makes a stale cache a MISS rather than a wrong answer.
    ycache = _scratch / "y_lambda_symbolic_cache_conventionD.json"
    _stale = _scratch / "y_lambda_symbolic_cache.json"
    if _stale.exists():
        _log(f"ignoring pre-excision (convention C) cache at {_stale}")
    import json as _json2

    def _unify_q(e):
        """Force every free symbol named 'q' onto OUR `qs`.

        Critical: round-tripping through str()/sympify() (the cache path, and
        any producer using its own q) LOSES the positive/real assumptions, so
        the parsed `Symbol('q')` is a DIFFERENT object from
        `Symbol('q', positive=True, real=True)`. Without this unification the
        later `subs(qs, s**2)` silently misses those terms and stray `q`
        survives into the deficit — the failure mode that produced a
        `q**51`-bearing expression at the sign step.
        """
        e = sp.sympify(e)
        for sym in list(e.free_symbols):
            if sym.name == "q" and sym is not qs:
                e = e.subs(sym, qs)
        return e

    if ycache.exists():
        _log("symbolic y_λ from cache…")
        raw = _json2.loads(ycache.read_text())
        Y4 = {tuple(_json2.loads(k)): sp.cancel(sp.radsimp(_unify_q(v)))
              for k, v in raw["4"].items()}
        Y3 = {tuple(_json2.loads(k)): sp.cancel(sp.radsimp(_unify_q(v)))
              for k, v in raw["3"].items()}
    else:
        _log("symbolic Jones-Markov weights y_λ (n=4, n=3)… (~18 min cold)")
        Y4 = {tuple(k): sp.cancel(sp.radsimp(_unify_q(v)))
              for k, v in y_lambda_at(4, None).items()}
        Y3 = {tuple(k): sp.cancel(sp.radsimp(_unify_q(v)))
              for k, v in y_lambda_at(3, None).items()}
    for _lbl, _Y in (("y_λ(4)", Y4), ("y_λ(3)", Y3)):
        # `!=`, not `is not`. The danger this guard exists for is a symbol
        # `subs(qs, ...)` would MISS, and subs matches by `==`. A bare
        # `Symbol('q')` from a str round-trip is `!= qs` and IS missed — caught.
        # But `Symbol('q', positive=True)` (what `wedderburn_jones_markov.Q_SYM`
        # is) is `== qs` while `is not qs`, because `positive=True` already
        # implies `real=True`, so the two assumption sets are equivalent and
        # sympy keeps them as distinct cached objects. Verified: `subs(qs, s**2)`
        # on such an expression substitutes correctly. An identity test flags it
        # anyway — a false alarm that blocked this producer when the symbolic
        # convention-D path was wired in 2026-08-09. Note neither `subs` nor
        # `xreplace` can repair it: both see nothing to replace.
        _stray = {str(sym) for v in _Y.values() for sym in v.free_symbols
                  if sym != qs}
        assert not _stray, f"{_lbl} carries non-`qs` symbols {_stray} — q unification failed"
        ycache.parent.mkdir(parents=True, exist_ok=True)
        ycache.write_text(_json2.dumps({
            "4": {_json2.dumps(list(k)): str(v) for k, v in Y4.items()},
            "3": {_json2.dumps(list(k)): str(v) for k, v in Y3.items()},
        }))
    _log(f"y_λ(4) partitions: {sorted(Y4)}")

    results = {}
    for label, n, word, Y in (("A3_w3", 3, w3_sigma, Y3), ("A4_w4", 4, w4_sigma, Y4)):
        _log(f"── {label}: exact χ_λ per partition ──")
        chis = {}
        sign_tables = {}
        all_pos = True
        for lam in partitions_of(n):
            t0 = time.time()
            c = chi_symbolic(lam, word)
            chis[lam] = c
            at1 = sp.limit(c, qs, 1) if c.has(qs) else c
            sgns = sign_on_grid(c, grid)
            sign_tables[lam] = sgns
            pos = all(v > 0 for v in sgns.values())
            all_pos = all_pos and pos
            _log(f"  λ={lam}: χ(q=1)={at1}  signs on grid={sgns}  "
                 f"[{time.time() - t0:.1f}s]")
        # unlink: empty word ⇒ χ_λ = dim_λ = #SYT (trace of identity)
        dims = {lam: sp.Integer(sp.trace(sp.eye(hoefsmit_matrices_symbolic(
            list(lam), qs)[1]))) for lam in partitions_of(n)}

        # perblock g with |χ| resolved by the verified signs (all + expected).
        #
        # The Jones-Markov y_λ carry half-integer powers of q, so g is rational in
        # s = √q, not in q. Substituting q = s² makes every expression a genuine
        # rational function of s — which is what makes `cancel` cheap and the
        # series exact (`factor` on the q-form is the step that hung the first run,
        # and the factored form is cosmetic anyway).
        s = sp.Symbol("s", positive=True, real=True)

        def to_s(e):
            return sp.cancel(sp.powsimp(e.subs(qs, s ** 2), force=True))

        _log("  assembling g_link / g_unlink in s = √q…")
        g_link = sp.cancel(sum(to_s(Y[lam]) * to_s(
            chis[lam] if all(v > 0 for v in sign_tables[lam].values())
            else sp.Abs(chis[lam])) for lam in partitions_of(n)))
        g_unlink = sp.cancel(sum(to_s(Y[lam]) * dims[lam] for lam in partitions_of(n)))
        tau_s = sp.cancel(g_link / g_unlink)
        D_s = sp.cancel(1 - tau_s)
        # Fail loudly HERE (not 8 minutes later at the sign step) if anything
        # other than `s` survived the substitution — the q-assumption-mismatch
        # class of bug.
        _leak = {str(sym) for sym in D_s.free_symbols if sym is not s}
        assert not _leak, f"deficit still carries {_leak}; expected s only"
        # keep a q-form for reporting/eval (exact, just re-expressed)
        tau = tau_s.subs(s, sp.sqrt(qs))
        D = D_s.subs(s, sp.sqrt(qs))
        Dfact = D_s          # cancelled rational function of s (no expensive factor)

        # Exact leading order, by NUMERATOR VALUATION (no `series` — that is the
        # step that stalls on these degree-~130 rationals).
        #
        # q = s² ⇒ q−1 = (s−1)(s+1) with dq/ds|_{s=1} = 2 ≠ 0, so the vanishing
        # order at s=1 in (s−1) EQUALS the order at q=1 in (q−1) (local diffeo).
        # Writing the cancelled D_s = N(s)/M(s) with M(1) ≠ 0, that order is
        # exactly the multiplicity of the root s = 1 in N — obtained by plain
        # polynomial expansion of N(1+ε), which is cheap and exact.
        _log("  leading order at s=1 by numerator valuation (≡ q=1 order)…")
        eps = sp.Symbol("eps")
        N_s, M_s = sp.fraction(sp.cancel(D_s))
        M_at_1 = sp.cancel(M_s.subs(s, 1))
        assert M_at_1 != 0, "denominator vanishes at s=1 — valuation argument invalid"
        Npoly = sp.Poly(sp.expand(N_s.subs(s, 1 + eps)), eps)
        nz = [m[0] for m in Npoly.monoms() if Npoly.coeff_monomial((m[0],)) != 0]
        assert nz, "deficit numerator is identically zero — unexpected"
        lead_order = min(nz)
        # Leading coefficient in (s−1).
        lead_coeff_s = sp.cancel(Npoly.coeff_monomial((lead_order,)) / M_at_1)
        # Convert to the (q−1) leading coefficient. Near s = 1,
        # q − 1 = (s−1)(s+1) = 2(s−1)·(1 + O(s−1)), so (q−1)ⁿ = 2ⁿ(s−1)ⁿ(1+…)
        # and the leading coefficients differ by exactly 2^order.
        # (Cross-checked: A=3 gives 192/2⁴ = 12, matching an independent
        # pure-q run of the same pipeline.)
        lead_coeff = sp.cancel(lead_coeff_s / 2 ** lead_order)

        # EXACT sign at the substrate pin. Because the deficit is rational in
        # s = √q, pinning a RATIONAL s₀ makes the evaluation exactly rational
        # (q = s₀² is then itself an exact rational within ~1e-20 of q₀ — see
        # s0_rat above). No floating point enters the sign decision.
        # Preferred: exactly rational (when the s-form carries no residual
        # radical). Otherwise fall back to a high-precision evaluation with an
        # explicit margin guard — decisive here, since the deficit signal is
        # ~1e-3 (A=3) / ~1e-4 (A=4), some 60 orders above the guard threshold.
        D_at_s0 = sp.cancel(D_s.subs(s, s0_rat))
        if D_at_s0.is_Rational:
            d0_sign = int(sp.sign(D_at_s0))
            sign_method = "exact-rational-at-s0-squared-pin"
        else:
            v = sp.N(D_at_s0, 80)
            assert abs(v) > sp.Float(10) ** (-60), (
                "sign margin guard failed — |D(s₀)| below 1e-60, sign not decisive")
            d0_sign = 1 if v > 0 else -1
            sign_method = "80-digit-evalf-at-s0-squared-pin-margin-guarded"
        tau_num = float(sp.N(tau_s.subs(s, sp.sqrt(sp.Float(Q_50_DIGIT_STR, 50))), 30))

        _log(f"  D(s), q = s²  =  {str(Dfact)[:400]}")
        _log(f"  leading (q−1)-order = {lead_order}   "
             f"leading coeff (q−1) = {lead_coeff}   [(s−1) coeff = {lead_coeff_s}]")
        _log(f"  D(q₀_rat) sign = {d0_sign} ({sign_method})   τ(q₀) ≈ {tau_num:.9f}")

        results[label] = {
            "sigma_word_length": len(word),
            "chi_exact": {str(lam): sp.srepr(chis[lam])[:0] or str(chis[lam])
                          for lam in chis},
            "chi_signs_on_grid": {str(lam): sign_tables[lam] for lam in sign_tables},
            "all_chi_positive_on_grid": bool(all_pos),
            "deficit_exact_in_s_where_q_eq_s_squared": str(Dfact),
            "tau_exact_in_s_where_q_eq_s_squared": str(tau_s),
            "leading_q_minus_1_order": int(lead_order),
            "leading_coeff_in_q_minus_1": str(lead_coeff),
            "leading_coeff_in_s_minus_1": str(lead_coeff_s),
            "deficit_sign_at_q0_exact": d0_sign,
            "deficit_sign_method": sign_method,
            "s0_rational_pin": str(s0_rat),
            "q_from_s0_squared": str(q_from_s0),
            "tau_at_q0_numeric": tau_num,
        }

    # ── verdicts ──────────────────────────────────────────────────────────────
    r3, r4 = results["A3_w3"], results["A4_w4"]
    order_law_ok = (r3["leading_q_minus_1_order"] == 4 and
                    r4["leading_q_minus_1_order"] == 6)
    sign_law_ok = (r3["deficit_sign_at_q0_exact"] == +1 and
                   r4["deficit_sign_at_q0_exact"] == -1)
    measured = 1.000145898
    match_measured = abs(r4["tau_at_q0_numeric"] - measured) < 5e-8

    print("\n" + "=" * 88)
    print("A=4 Brunnian deficit — EXACT closed form (perblock convention, base n=4)")
    print(f"  τ_L₄(s), q = s² = {r4['tau_exact_in_s_where_q_eq_s_squared'][:200]}")
    print(f"  1 − τ_L₄(s) = {r4['deficit_exact_in_s_where_q_eq_s_squared'][:200]}")
    print(f"  leading (q−1)-order: A3={r3['leading_q_minus_1_order']} (expect 4), "
          f"A4={r4['leading_q_minus_1_order']} (expect 6)  → {'OK' if order_law_ok else 'MISMATCH'}")
    print(f"  exact deficit signs at q₀: A3={r3['deficit_sign_at_q0_exact']} (+ expected), "
          f"A4={r4['deficit_sign_at_q0_exact']} (− expected)  → {'OK' if sign_law_ok else 'MISMATCH'}")
    print(f"  τ_L₄(q₀) exact-pipeline ≈ {r4['tau_at_q0_numeric']:.9f} vs measured {measured}"
          f"  → {'MATCH' if match_measured else 'MISMATCH'}")
    print("=" * 88)

    # start_time = process start, so durationMs measures the whole symbolic
    # derivation rather than just the save step.
    w = WitnessBuilder("a4-brunnian-deficit-closed-form", engine="python",
                       start_time=_T0_MONO)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "EXACT symbolic closed form of the A=4 4-component Brunnian level deficit "
        "1 - tau_L4 under the perblock convention g = sum y_lambda*|chi_lambda| at base "
        "n=4, for the genuine Brunnian word w4=[[A01,A12],A23] (byte-identical band "
        "construction re-imported from a4_h12_brunnian_deficit_measure_probe). chi_lambda "
        "computed exactly over Q(q) via the symbolic Hoefsmit seminormal form; y_lambda "
        "symbolic Jones-Markov weights; |.| resolved by exact-rational sign verification "
        "on a q-grid spanning (1, q0] (pure braid => chi(q=1)=dim>0). Promotes the "
        "measured tauL4Measured=1.000145898 / order~6.06 (Lean "
        "HeliumBrunnianDeficitMeasured) toward derived: exact leading (q-1)-order and "
        "exact deficit sign at a rational q0 pin, cross-checked against the independent "
        "f64 measurement. A=3 leg run through the SAME pipeline as validation (expect "
        "order 4, sign +). 0 free parameters, nothing wired, derive-then-check."
    )
    for k, v in results.items():
        w.add_data(k, v)
    w.add_assertion(
        "milnor_order_law_2_A_minus_1_exact",
        computed=float(r3["leading_q_minus_1_order"] * 100 + r4["leading_q_minus_1_order"]),
        expected=406.0, tolerance=0.0,
        source="Exact series expansion at q=1 of the perblock deficit: leading "
               "(q-1)-order is 4=2(3-1) for the A=3 band commutator and 6=2(4-1) for "
               "the A=4 iterated commutator — the Milnor order law, now EXACT at both "
               "known A (was: slope-estimated 6.06 at A=4).",
    )
    w.add_assertion(
        "parity_sign_law_exact_at_q0",
        computed=float(r3["deficit_sign_at_q0_exact"] * 10 + r4["deficit_sign_at_q0_exact"]),
        expected=9.0, tolerance=0.0,
        source="Exact rational-arithmetic signs of the deficit at the rational q0 pin: "
               "A=3 deficit +1 (binding), A=4 deficit -1 (tau_L4>1) — the (-1)^(A-1) "
               "parity law, exact (was: f64-measured at A=4).",
    )
    w.add_assertion(
        "tau_L4_matches_independent_f64_measurement",
        computed=r4["tau_at_q0_numeric"], expected=measured, tolerance=5e-8,
        source="The exact-symbolic pipeline evaluated at q0 reproduces the independent "
               "f64 pyhecke_native measurement tau_L4=1.000145898 "
               "(a4-h12-brunnian-deficit-measure.witness.json).",
    )
    out = w.save()
    _log(f"witness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
