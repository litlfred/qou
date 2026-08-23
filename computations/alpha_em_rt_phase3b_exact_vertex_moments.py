#!/usr/bin/env python3
"""alpha_em_rt_phase3b_exact_vertex_moments.py — make the RT phase-3 vertex
bookkeeping EXACT (the deferred "rigorous coefficient match"), and read off the
same-prescription O(α²) slot.

Context (1ppQ flagship): α_EM at the proton pin with the phase-3 Schwinger
(1−h²α) sits at +0.313 ppb ≈ 2.1σ; the missing 2-loop slot needs
C₂ ≈ −8.1e-4 (known to ~1 significant figure; entropy-blocked from numerical
identification — the only route is structural). Phase 3 established the SHAPE
of (1−h²α) but its own docstring records the coefficient match as OPEN
("requires care with the choice of generator powers vs trace normalization";
its leading-order bookkeeping gives 1−h·q⁻¹ = 1−h+O(h²), not 1−h², before
appealing to a cross-vertex commutator). This probe replaces the hand
bookkeeping with the exact fundamental-representation computation:

  * A = ℂ² (U_q(sl2) fundamental), Hecke-normalized braiding R̂ with
    eigenvalues {q, −q⁻¹} (σ² = hσ + 1, h = q−q⁻¹), pivotal μ = diag(q, q⁻¹),
    quantum trace qTr(x) = Tr(μ^{⊗n}·x).
  * e₋ = (q·1 − R̂)/(q+q⁻¹): the singlet idempotent of the EM projection
    block (validated: qTr(e₋) = 1, dim_q A = [2]_q, braid + Hecke relations).
  * Photon pair = strands (1,2), matter = strand 3 (H₃ rep, 8×8) or strands
    (3,4) (H₄ rep, 16×16). Vertex = σ₂ (photon–matter coupling); matter
    internal braiding = σ₃.
  * Singlet-channel moments  m[w] := qTr(E·w·E)/qTr(E),  E = e₋⊗1.

Every canonical vertex word up to 4 letters is reported with its EXACT value
in ℚ(q) and its exact (q−1)-expansion — no topology is selected post hoc, no
coefficient is fitted. The phase-3 prescription (subtract the bare constant;
the excess at each vertex order fills the ladder slot) is then applied
uniformly, and the O(α²) slot value it implies is compared, single-shot,
against the required C₂ ≈ −8.1e-4 window.

Discipline: scope-(a); nothing wired; the required C₂ enters ONLY as the
falsification window (1 sig fig), never as an input. auditOnly.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

q = sp.Symbol("q", positive=True)
h = q - 1 / q
Q_PROTON = "1.109978582751380808"
C2_REQUIRED = -8.1e-4          # falsification window only (1 sig fig)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def build_reps():
    I2 = sp.eye(2)
    # Hecke-normalized braiding on A⊗A (basis 11, 12, 21, 22)
    R = sp.Matrix([[q, 0, 0, 0],
                   [0, q - 1 / q, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, q]])
    mu = sp.diag(q, 1 / q)
    em = (q * sp.eye(4) - R) / (q + 1 / q)      # singlet idempotent e_-
    reps = {}
    # H3 rep (8x8): sigma1 = R⊗I, sigma2 = I⊗R
    reps[3] = {"sig": {1: kron(R, I2), 2: kron(I2, R)},
               "E": kron(em, I2), "mu": kron(mu, mu, mu)}
    # H4 rep (16x16)
    reps[4] = {"sig": {1: kron(R, I2, I2), 2: kron(I2, R, I2), 3: kron(I2, I2, R)},
               "E": kron(em, I2, I2), "mu": kron(mu, mu, mu, mu)}
    return R, em, mu, reps


def qtr(rep, x):
    return sp.cancel(sp.expand((rep["mu"] * x).trace()))


def moment(rep, word):
    """m[word] = qTr(E·w·E)/qTr(E), word = list of generator indices."""
    w = sp.eye(rep["E"].shape[0])
    for g in word:
        w = w * rep["sig"][g]
    num = qtr(rep, rep["E"] * w * rep["E"])
    den = qtr(rep, rep["E"])
    return sp.cancel(num / den)


def sexp(expr, order=5):
    """(q-1)-expansion, exact rational coefficients."""
    s = sp.Symbol("s")
    ser = sp.series(expr.subs(q, 1 + s), s, 0, order).removeO()
    return [sp.nsimplify(sp.expand(ser).coeff(s, i)) for i in range(order)]


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    print("=" * 78)
    print(" RT phase-3b: EXACT singlet-channel vertex moments (fundamental rep)")
    print("=" * 78)

    R, em, mu, reps = build_reps()

    # ── 0. validations ──
    hecke = sp.simplify(R * R - (q - 1 / q) * R - sp.eye(4))
    r3 = reps[3]["sig"]
    braid = sp.simplify(r3[1] * r3[2] * r3[1] - r3[2] * r3[1] * r3[2])
    dimq = sp.cancel((mu).trace())
    qtr_em = sp.cancel((kron(mu, mu) * em).trace())
    idem = sp.simplify(em * em - em)
    ok0 = (hecke.is_zero_matrix and braid.is_zero_matrix and idem.is_zero_matrix
           and sp.simplify(dimq - (q + 1 / q)) == 0 and sp.simplify(qtr_em - 1) == 0)
    print(f"\n[0] validations (Hecke, braid, e_- idempotent, dim_q=[2]_q, qTr(e_-)=1): {ok0}")
    assert ok0

    # ── 1. exact moments, H3 (matter = strand 3; vertex = sigma_2) ──
    words3 = {"m1 <s2>": [2], "m2 <s2^2>": [2, 2], "m3 <s2^3>": [2, 2, 2],
              "m4 <s2^4>": [2, 2, 2, 2]}
    print("\n[1] H3 singlet-channel moments (exact, with (q−1)-expansion):")
    vals = {}
    for name, w in words3.items():
        v = moment(reps[3], w)
        vals[name] = v
        print(f"    {name:12s} = {sp.nsimplify(sp.simplify(v))}   s-exp: {sexp(v)}")

    m1 = vals["m1 <s2>"]
    # Hecke consistency: m2 = h*m1 + 1 exactly
    ok_hecke_m = sp.simplify(vals["m2 <s2^2>"] - (h * m1 + 1)) == 0
    print(f"    Hecke recursion m2 = h·m1 + 1 exact: {ok_hecke_m}")

    # ── 2. H4 cross-position words (vertex s2, matter-internal s3) ──
    words4 = {"<s2 s3 s2 s3>": [2, 3, 2, 3], "<s2 s3^2 s2>": [2, 3, 3, 2],
              "<(s2 s3)^2 rev>": [3, 2, 3, 2], "<s2^2 s3^2>": [2, 2, 3, 3]}
    print("\n[2] H4 cross-position 4-letter words (exact + s-exp):")
    for name, w in words4.items():
        v = moment(reps[4], w)
        vals[name] = v
        print(f"    {name:16s} = {sp.nsimplify(sp.simplify(v))}   s-exp: {sexp(v)}")

    # ── 3. the phase-3 prescription made exact ──
    #     vertex order k → ladder: excess_k := m_k − (bare), each vertex carries α.
    #     Phase-3 claim: 2-vertex excess = −h²·(1 + O(h)) so that the 1-loop
    #     dressing is (1 − h²α). Exact test:
    ex2 = sp.cancel(vals["m2 <s2^2>"] - 1)
    ex2_series = sexp(ex2)
    print("\n[3] phase-3 prescription, exact:")
    print(f"    2-vertex excess m2 − 1 = h·m1 = {sp.nsimplify(sp.simplify(ex2))}")
    print(f"      s-exp: {ex2_series}")
    lead_order = next(i for i, c in enumerate(ex2_series) if c != 0)
    print(f"      leading (q−1)-order: {lead_order}  (phase-3 SHAPE claim needs 2)")
    # the exact h-content: is ex2 = −h² × (unit + O(h))?
    ratio_h2 = sp.cancel(ex2 / h**2)
    ratio_series = sexp(ratio_h2)
    print(f"      (m2 − 1)/h² = {sp.nsimplify(sp.simplify(ratio_h2))}   s-exp: {ratio_series}")

    # 4-vertex same-position excess beyond the 2-vertex ladder (the O(α²) slot
    # under the SAME prescription): connected part m4 − m2²
    conn4 = sp.cancel(vals["m4 <s2^4>"] - vals["m2 <s2^2>"] ** 2)
    conn4_series = sexp(conn4)
    print(f"\n    4-vertex connected excess m4 − m2² = {sp.nsimplify(sp.simplify(conn4))}")
    print(f"      s-exp: {conn4_series}")
    # cross-position connected: <s2 s3 s2 s3> − <s2^2><s3-loop bare=1>… report raw
    conn_cross = sp.cancel(vals["<s2 s3 s2 s3>"] - vals["m2 <s2^2>"])
    print(f"    cross-position <s2s3s2s3> − m2 = {sp.nsimplify(sp.simplify(conn_cross))}")
    print(f"      s-exp: {sexp(conn_cross)}")

    # ── 4. numeric at the proton pin; single-shot vs the C2 window ──
    qn = mp.mpf(Q_PROTON)
    def at_q0(e):
        return mp.mpf(str(sp.N(e.subs(q, sp.Rational(sp.nsimplify(Q_PROTON))), 30)))
    hn = qn - 1 / qn
    print(f"\n[4] numeric at proton q0 (h² = {mp.nstr(hn**2, 8)}):")
    report = {}
    for name in ["m1 <s2>", "m2 <s2^2>", "m4 <s2^4>"] + list(words4):
        report[name] = at_q0(vals[name])
    ex2_n = report["m2 <s2^2>"] - 1
    print(f"    2-vertex excess (m2−1)      = {mp.nstr(ex2_n, 8)}   vs −h² = {mp.nstr(-hn**2, 8)}"
          f"   ratio = {mp.nstr(ex2_n / (-hn**2), 8)}")
    conn4_n = report["m4 <s2^4>"] - report["m2 <s2^2>"] ** 2
    cross_n = report["<s2 s3 s2 s3>"] - report["m2 <s2^2>"]
    print(f"    4-vertex connected (m4−m2²) = {mp.nstr(conn4_n, 8)}")
    print(f"    cross-position connected    = {mp.nstr(cross_n, 8)}")
    print(f"    required C2 window (falsification only): {C2_REQUIRED} ± 50%")
    in_window = {k: bool(abs(v) > 0 and (abs(abs(v) / abs(C2_REQUIRED) - 1) < 0.5)
                         and (v < 0) == (C2_REQUIRED < 0))
                 for k, v in {"conn4": conn4_n, "cross": cross_n}.items()}
    print(f"    single-shot window hits: {in_window}")

    wb = WitnessBuilder("alpha-em-rt-phase3b-exact-vertex-moments", engine="sympy+mpmath")
    wb.set_description(
        "Exact fundamental-rep computation of the RT phase-3 singlet-channel "
        "vertex moments (the deferred 'rigorous coefficient match' under the "
        "+0.313 ppb alpha_EM headline): e_- validated (qTr=1, dim_q=[2]_q), all "
        "1..4-vertex canonical words computed exactly in Q(q) with (q-1)-"
        "expansions; the phase-3 prescription (bare-subtracted excess fills the "
        "ladder slot) applied uniformly; the implied O(alpha^2) slot values "
        "(connected 4-vertex, cross-position) tested single-shot against the "
        "required C2 ~ -8.1e-4 window (1 sig fig; falsification only, never an "
        "input). auditOnly; no fit; nothing wired."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_data("validations", {"all": bool(ok0)})
    wb.add_data("exact_moments", {k: str(sp.nsimplify(sp.simplify(v))) for k, v in vals.items()})
    wb.add_data("s_expansions", {k: [str(c) for c in sexp(v)] for k, v in vals.items()})
    wb.add_data("phase3_exact_check", {
        "two_vertex_excess": str(sp.nsimplify(sp.simplify(ex2))),
        "leading_q_minus_1_order": int(lead_order),
        "excess_over_h2_series": [str(c) for c in ratio_series],
        "hecke_recursion_exact": bool(ok_hecke_m)})
    wb.add_data("order_alpha2_slot", {
        "connected_4vertex_at_q0": mp.nstr(conn4_n, 12),
        "cross_position_at_q0": mp.nstr(cross_n, 12),
        "required_C2_window": f"{C2_REQUIRED} +/- 50% (falsification only)",
        "window_hits": {k: bool(v) for k, v in in_window.items()}})
    wb.add_assertion("representation_validations", computed=1.0 if ok0 else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="Hecke + braid relations, e_- idempotent, dim_q=[2]_q, qTr(e_-)=1 — all exact")
    wb.add_assertion("hecke_moment_recursion_exact", computed=1.0 if ok_hecke_m else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="m2 = h*m1 + 1 exactly (algebra-level consistency of the moment map)")
    wb.save()
    print(f"\n  ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
