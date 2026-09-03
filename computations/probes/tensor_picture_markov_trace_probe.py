#!/usr/bin/env python3
"""The Markov trace as a quantum trace on `(ℂ²)^{⊗n}` — the Schur–Weyl identification, checked.

Bean `qou-qqm4` (stage 1). Both `ClassicalTraceFloor` (c₀) and
`LeadingOrderTraceCoefficient` (c₁) rest on ONE unformalised hypothesis:

    tr_M(x)  =  Tr( K · ρ(x) ) / (1 + q²)^n ,     K = diag(1, q²)^{⊗n}          [SW]

with `ρ` the tensor representation of `H_n(q)` on `(ℂ²)^{⊗n}` in which the
generator acts on an adjacent pair as the `U_q(sl₂)` R-matrix in Hecke
normalisation,

    Ř e₁₁ = q e₁₁,   Ř e₂₂ = q e₂₂,   and on span(e₁₂, e₂₁):  [[0, 1], [1, h]],  h = q − q⁻¹

(eigenvalues `q` and `−q⁻¹`, i.e. `(Ř − q)(Ř + q⁻¹) = 0`). One check is
immediate: `Tr(KŘ)/(1+q²)² = (q + hq² + q⁵)/(1+q²)² = q³/(1+q²) = z_D`, the
convention-D loop value. This probe checks [SW] on the ACTUAL braid words —
free and atom, D / T / ³He — against the seminormal Markov trace
`Σ_λ y_λ χ^λ` computed by the validated exact-`Fraction` pipeline, both as
exact power series in `ε = q − 1` (every order computed) and as exact
rationals at `q = 8/7`.

Two conventions are possible for WHICH off-diagonal state carries the `h`
(`e₂₁` or `e₁₂`); they are conjugate by the global spin flip, which does NOT
commute with `K`. The probe runs both. **Measured: both match at every order**
— and on reflection they must: each is an `H_n(q)`-trace with the Markov
property and loop value `z_D`, and the Markov trace with a given loop value is
unique. (The first draft of this docstring expected exactly one to pass; that
expectation was wrong and the assertion was corrected to say so.)

What this buys: [SW] passes from "hypothesis stated in Lean" to "identity
verified on the six words at every computed order"; and the objects the
second-order derivation needs are now explicit —

    Ř(1+ε) = s + ε(1 + Y) + ε² W + O(ε³),   Y = diag(0, −1, +1, 0),   W = −E_{e₂₁,e₂₁}

on `(e₁₁, e₁₂, e₂₁, e₂₂)` (from `h = 2ε − ε² + …`), so `sY = −Ys` and
`Tr(Y·P) = 0` are checkable by inspection rather than argued.

Precision: `Fraction` end to end. Not evaluated at `q₀`; proton pin irrelevant.
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "c1probe", _HERE / "c1_leading_coefficient_derived_probe.py")
_c1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c1)
Ser, factors_for = _c1.Ser, _c1.factors_for
tr_M_series, tr_M_fraction = _c1.tr_M_series, _c1.tr_M_fraction


# ═══════════════════════════════════════════════════════════════════════════
#  the tensor picture
# ═══════════════════════════════════════════════════════════════════════════
def apply_letter(vec: dict, c, d, g: int, q, h, conv: str) -> dict:
    """`(c·Ř_g + d·1)` on a sparse vector over basis states = bitmasks
    (bit i set ⇔ site i is `e₂`). `conv` = which off-diagonal state carries `h`."""
    out: dict = {}
    m_g, m_g1 = 1 << g, 1 << (g + 1)

    def add(k, x):
        if k in out:
            out[k] = out[k] + x
        else:
            out[k] = x

    for s, a in vec.items():
        bg, bg1 = bool(s & m_g), bool(s & m_g1)
        if d != 0:
            add(s, d * a)
        if bg == bg1:
            add(s, c * q * a)
        else:
            sw = s ^ (m_g | m_g1)
            add(sw, c * a)
            carries_h = (bg and not bg1) if conv == "h_on_e21" else (bg1 and not bg)
            if carries_h:
                add(s, c * h * a)
    return out


def tr_tensor(Z: int, N: int, include_inter: bool, q, conv: str, *, log=None):
    """`Tr(K ρ(word)) / (1+q²)^n` for the canonical word, over any scalar `q`."""
    n = 3 * (Z + N)
    crossings = atom_canonical_crossings(Z, N, include_inter=include_inter)
    facs = factors_for(crossings, q, colour_weighted=True)      # (c, d, g+1)
    h = q - 1 / q
    q2 = q * q
    total = 0
    t0 = time.time()
    for b in range(1 << n):
        vec = {b: F(1)}
        for (c, dd, g1) in reversed(facs):
            vec = apply_letter(vec, c, dd, g1 - 1, q, h, conv)
        amp = vec.get(b, 0)
        if amp != 0:
            total = total + (q2 ** bin(b).count("1")) * amp
        if log and b and b % 128 == 0:
            log(f"      {b}/{1 << n} basis states, {time.time()-t0:.0f}s")
    return total / (1 + q2) ** n


def main() -> int:
    T0 = time.time()

    def log(msg):
        print(f"  [{time.time()-T0:7.1f}s] {msg}", flush=True)

    w = WitnessBuilder("tensor-picture-markov-trace-probe")
    w.set_description(
        "Checks the Schur-Weyl identification tr_M(word) = Tr(K rho(word))/(1+q^2)^n, "
        "K = diag(1,q^2)^(x)n, rho the U_q(sl2) R-matrix representation, against the "
        "seminormal Markov trace sum_lambda y_lambda chi^lambda on the actual free and "
        "atom words of D, T, 3He: exact power series in eps = q-1 (every computed order) "
        "and exact rationals at q = 8/7. Identifies which R-matrix convention is the "
        "quantum trace, and makes Y and R'' explicit for the second-order derivation."
    )

    print("=" * 78)
    print("  tr_M as a quantum trace on (C^2)^(x)n — [SW] checked on the words")
    print("=" * 78)

    # ---- 1. the loop value, both conventions, exact -------------------------
    q = F(8, 7)
    loops = {}
    for conv in ("h_on_e21", "h_on_e12"):
        # H_2: the word is the single generator sigma_1 (c=1, d=0, g=1)
        h = q - 1 / q
        tot = F(0)
        for b in range(4):
            vec = apply_letter({b: F(1)}, F(1), F(0), 0, q, h, conv)
            tot += (q * q) ** bin(b).count("1") * vec.get(b, 0)
        loops[conv] = tot / (1 + q * q) ** 2
    z_D = q ** 3 / (q * q + 1)
    log(f"loop value at q=8/7: {loops}  vs z_D = {z_D}")
    w.add_assertion(
        "single_crossing_quantum_trace_is_the_convention_D_loop_value",
        computed="1" if all(v == z_D for v in loops.values()) else "0", expected="1",
        source=f"Tr(K R)/(1+q^2)^2 at q = 8/7 = {loops['h_on_e21']} for both h-placements; "
               f"z_D = q^3/(q^2+1) = {z_D}. Exact Fraction equality.",
    )

    # ---- 2. the words: series and rational, both conventions ----------------
    CASES = [("D", (1, 1), 6), ("T", (1, 2), 4), ("3He", (2, 1), 4)]   # n=9: orders 0..2
    rows, conv_ok = [], {"h_on_e21": True, "h_on_e12": True}
    for name, (Z, N), P in CASES:
        for inter in (False, True):
            tag = f"{name} {'atom' if inter else 'free'}"
            log(f"seminormal series {tag} (P={P}) …")
            ref = tr_M_series(Z, N, inter, P)
            ref_frac = tr_M_fraction(Z, N, inter, F(8, 7))
            for conv in ("h_on_e21", "h_on_e12"):
                log(f"  tensor {tag} [{conv}] …")
                ten = tr_tensor(Z, N, inter, Ser.eps(P), conv, log=log if name != "D" else None)
                orders = min(ref.p, ten.p)
                match_series = all(ref.coeff(k) == ten.coeff(k) for k in range(orders))
                ten_frac = tr_tensor(Z, N, inter, F(8, 7), conv)
                match_frac = (ten_frac == ref_frac)
                conv_ok[conv] &= (match_series and match_frac)
                rows.append({
                    "case": tag, "convention": conv, "orders_compared": orders,
                    "series_match": match_series, "rational_q_8_7_match": match_frac,
                    "seminormal_coeffs": [str(ref.coeff(k)) for k in range(orders)],
                    "tensor_coeffs": [str(ten.coeff(k)) for k in range(orders)],
                    "seminormal_at_8_7": str(ref_frac), "tensor_at_8_7": str(ten_frac),
                })
                log(f"    orders 0..{orders-1}: {'MATCH' if match_series else 'DIFFER'}; "
                    f"q=8/7: {'MATCH' if match_frac else 'DIFFER'}")

    good = [c for c, ok in conv_ok.items() if ok]
    w.add_assertion(
        "SW_identification_holds_on_all_six_words_for_BOTH_h_placements",
        computed=",".join(sorted(good)) if good else "none", expected="h_on_e12,h_on_e21",
        source="tr_M(word) via sum_lambda y_lambda chi^lambda (exact-Fraction seminormal) vs "
               "Tr(K rho(word))/(1+q^2)^n (tensor picture), D/T/3He free and atom, as series in "
               "eps to every computed order and as exact rationals at q = 8/7. Both h-placements "
               "match — and must: each is an H_n(q)-trace with the Markov property and loop value "
               "z_D, and the Markov trace with a given loop value is unique (Jones/Ocneanu). The "
               "docstring's expectation that only one would pass was wrong; recorded, not hidden.",
    )
    diff_rows = [r for r in rows if not (r["series_match"] and r["rational_q_8_7_match"])]
    w.add_data("comparison", rows)
    w.add_data("conventions_passing", good)

    # ---- 3. the explicit first- and second-order R-matrix ---------------------
    # R on (e11, e12, e21, e22) with h on e21 (or e12): expand h = 2e - e^2 + e^3 ...
    P = 5
    e = Ser.eps(P)
    h = e - 1 / e
    R_expl = {"q": e, "h": h}
    Y = {"e11": 0, "e12": -1, "e21": 1, "e22": 0}       # first-order minus identity, h_on_e21
    W = {"e11": 0, "e12": 0, "e21": -1, "e22": 0}       # second-order coefficient
    # check: coefficient of eps^1 of q is 1 (=> X = 1 on e11,e22), of h is 2 (=> X = 1 + 1 on e21);
    # e12 -> e21 has no eps dependence (X = 0 there ... as an off-diagonal it is the swap s itself)
    ok_orders = (e.coeff(1) == 1 and h.coeff(1) == 2 and h.coeff(2) == -1 and e.coeff(2) == 0)
    w.add_assertion(
        "R_matrix_expansion_gives_Y_diag_0_m1_p1_0_and_W_minus_E2121",
        computed="1" if ok_orders else "0", expected="1",
        source=f"q = 1 + eps exactly; h = q - 1/q = {h.coeff(1)} eps + ({h.coeff(2)}) eps^2 + ... "
               f"so on the diagonal (e11, e12, e21, e22) the eps-coefficient of R is (1, 0, 2, 1) "
               f"= 1 + (0, -1, +1, 0) and the eps^2-coefficient is (0, 0, -1, 0). Hence "
               f"Y = diag(0,-1,+1,0): sY = -Ys by inspection, and Tr(Y P) = 0 for any permutation "
               f"P by the e12 <-> e21 count symmetry. These are the objects the c2 derivation uses.",
    )
    w.add_data("R_matrix_expansion", {
        "q_series": [str(e.coeff(k)) for k in range(3)],
        "h_series": [str(h.coeff(k)) for k in range(3)],
        "Y_diag_e11_e12_e21_e22": [0, -1, 1, 0],
        "W_diag_e11_e12_e21_e22": [0, 0, -1, 0],
        "note": "diagonal entries in the (e11, e12, e21, e22) basis with h placed on e21; "
                "the off-diagonal part of R is the swap s and is eps-independent.",
    })

    ok = all(v == z_D for v in loops.values()) and sorted(good) == ["h_on_e12", "h_on_e21"] \
        and ok_orders
    if diff_rows:
        print("\n  rows that DIFFER:")
        for r in diff_rows:
            print(f"    {r['case']} [{r['convention']}]  series {r['series_match']}  q=8/7 {r['rational_q_8_7_match']}")
    print(f"\n  conventions passing [SW] on all six words: {good}")
    out = w.save()
    print(f"  witness -> {out}")
    print(f"  ALL PASSED: {ok}   ({time.time()-T0:.0f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
