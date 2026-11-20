#!/usr/bin/env python3
"""A5.3 (bean qou-3yxn): certified categorical q*-tests at N = 4 (and 5) via
generalized Jones–Wenzl cables — extending the A5.2 N=3 certification.

WHY. A5.2 (merged #3927) refuted the Masbaum p=2 tower, validated a
definitional TL-cable J'_3, and certified the N=3 categorical q*-test (no
zero, anchor-smooth). The categorical face at HIGHER colored levels remained
open. This probe builds the (N−1)-cable with the full Jones–Wenzl projector
e_{N−1} and runs the same certified test at N = 4, 5.

CONSTRUCTION (reuses the A5.2-validated TL_n transfer engine):
  e₂ = 1 − U/δ;  e₃ = 1 − ([2]/[3])(U₁+U₂) + (1/[3])(U₁U₂+U₂U₁);
  e₄ via the Wenzl recursion e₄ = e₃ − ([3]/[4])·e₃U₃e₃ expanded into TL
  words. J'_N(K) = fr_{N−1}(q)^w·⟨K^{(N−1)}(e_{N−1})⟩/⟨e_{N−1}⟩ with the
  (N−1)-cable word (σ_i ↦ the (N−1)² crossing block) and the framing factor
  fr CALIBRATED on the trefoil (A5.2 found fr₂ = q⁴ = the ribbon twist
  q_M^{λ(λ+2)/4} with q_M = q²; expect fr₃ = q_M^{15/4}·(unit), calibrated
  not assumed).

GATES (trusted reference = the Masbaum p = ±1 towers, validated in A5.2
against the printed Rmk-5.2 values, the corpus TL₃ Jones, the corpus
aj_masbaum_crosscheck, and the proven 4₁ VC growth):
  G1 — N=3 regression: this probe's generalized-JW path reproduces the
       A5.2-certified J'_3 values (engine self-consistency).
  G2 — 4₁ (N−1)-cable at w=0 equals the trusted p=−1 tower J'_N(4₁) at 3
       real q points, N = 4 (and 5 when run).
  G3 — trefoil calibrates fr_{N−1} to a consistent power across q
       (reported; expect the ribbon exponent).
THE TEST — certified B_N(5₂; q) = [J'_N(q) − J'_N(1/q)]/2 on the q* ± 2e-8
grid at N = 4 (and 5): sign changes, |B_N(q*)|, anchor slope. Expected
(scope-(a)): no zero, anchor-smooth — extending the certified categorical
falsification to N = 4, 5. auditOnly; no c_k wired; no fit.

Run: python3 -u computations/probes/qbeta_5two_higher_cable_qstar_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_higher_cable.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_n3_cable_arbitration_probe as c3  # noqa: E402  (TL engine)
import qbeta_5two_colored_tower_barodd_qstar_probe as tower  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

BRAID_5_2 = [1, 1, 1, 2, -1, 2]
BRAID_4_1 = [1, -2, 1, -2]
BRAID_TREF = [1, 1, 1]
# Both pins read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). The
# muon leg was the literal 1.1099785955573... -- the RETIRED self-certified
# pin A, superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. A
# mu-vs-p comparison whose muon leg is a retired literal compares live proton
# against yesterday's muon, which is the failure it exists to measure.
# Exception E1 of the 2026-08-30 ruling: both pins are read here on purpose.
Q_MUON = q_muon_at(50)
Q_PROTON = Q_MP
Q_STAR = mp.mpf("1.10997859303152")


def cable(word, c):
    """c-cable of a braid word: σ_i ↦ the c² crossing block (rows of adjacent
    transpositions moving the i-th strand-bundle over the (i+1)-th)."""
    out = []
    for g in word:
        i = abs(g)
        base = c * (i - 1)          # bundles occupy strands base+1..base+2c
        block = []
        # move each of the c strands of bundle i over bundle i+1, one at a time
        for r in range(c):
            # strand (base + c - r) walks right across the c strands of the
            # next bundle
            start = base + c - r
            for s in range(c):
                block.append(start + s)
        if g > 0:
            out += block
        else:
            out += [-x for x in reversed(block)]
    return out


def apply_element(vec_word_engine, terms, n, A, engine):
    """Given a TL element as a list of (coefficient, generator-word) terms,
    return Σ coeff · bracket_closure(cabled_word + gen_word)."""
    tot = mp.mpc(0)
    base_word, = (vec_word_engine,)
    for coef, gword in terms:
        tot += coef * c3.bracket_closure(base_word + [('U', g) for g in gword],
                                         n, A, engine)
    return tot


def jw_terms(m, q):
    """Jones–Wenzl e_m on m strands as (coefficient, [U-generator indices])
    terms, built by the Wenzl recursion e_k = e_{k−1} − ([k−1]/[k])·
    e_{k−1}U_{k−1}e_{k−1}, represented in the U-word algebra symbolically as
    lists (products left→right). Coefficients numeric at the given q
    (q-brackets [k] = (q^k−q^{−k})/(q−q^{−1}) in the CABLE variable's
    A-units: [k]_δ with δ = −A²−A⁻²; here we use the δ-Chebyshev form:
    [k] ≡ S_{k−1}(δ) satisfying the same recursion — calibrated by G1)."""
    A = q ** mp.mpf("-0.5")
    delta = -A ** 2 - A ** -2
    # Chebyshev-like [k]: [1]=1, [2]=δ, [k+1]=δ[k]−[k−1]
    br = {0: mp.mpc(0), 1: mp.mpc(1)}
    for k in range(2, m + 2):
        br[k] = delta * br[k - 1] - br[k - 2]
    terms = {(): mp.mpc(1)}          # e_1 = 1 (on 1 strand)
    for k in range(2, m + 1):
        # e_k = e_{k-1} - ([k-1]/[k]) e_{k-1} U_{k-1} e_{k-1}
        coef = br[k - 1] / br[k]
        new = dict(terms)
        for w1, c1 in terms.items():
            for w2, c2 in terms.items():
                w = w1 + (k - 1,) + w2
                new[w] = new.get(w, mp.mpc(0)) - coef * c1 * c2
        terms = new
    return [(c, list(w)) for w, c in terms.items() if abs(c) > mp.mpf("1e-40")]


def Jprime(word, k_strands, cN, q, engines):
    """J'_{cN+1}(closure of word ∈ B_k) via the cN-cable + e_{cN} insertion,
    WITHOUT framing factor (raw)."""
    A = q ** mp.mpf("-0.5")
    n = cN * k_strands
    eng = engines[n]
    cw = cable(word, cN)
    ejw = jw_terms(cN, q)
    num = mp.mpc(0)
    for coef, gword in ejw:
        num += coef * c3.bracket_closure(cw + [('U', g) for g in gword],
                                         n, A, eng)
    # denominator: closure of e_{cN} alone on cN strands
    engd = engines[cN]
    den = mp.mpc(0)
    for coef, gword in ejw:
        den += coef * c3.bracket_closure([('U', g) for g in gword],
                                         cN, A, engd)
    return num / den


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" A5.3 — certified categorical q*-tests at N = 4, 5 (JW cables)")
    print("=" * 78)

    print("\n  building TL engines (n = 2, 3, 4, 6, 9, 12) ...", flush=True)
    engines = {n: c3.tl_engine(n) for n in (2, 3, 4, 6, 9, 12)}
    print(f"  ... built ({time.monotonic()-t0:.0f}s)", flush=True)

    qs_test = [mp.mpf("1.11"), mp.mpf("0.93"), mp.mpf("1.037")]

    # ---- G1: N=3 regression vs the A5.2-certified path ----
    g1_ok = True
    print("\n[G1] N=3 regression (generalized-JW path vs A5.2 colored3_raw):")
    for q in qs_test:
        a = Jprime(BRAID_4_1, 3, 2, q, engines)
        b = c3.colored3_raw(BRAID_4_1, 3, q, engines)
        err = abs(a - b) / abs(b)
        g1_ok &= err < mp.mpf("1e-25")
        print(f"    q={q}: rel {mp.nstr(err, 3)}")
    print(f"    {'PASS' if g1_ok else 'FAIL'}")

    # ---- G2: 4₁ 3-cable (w=0) vs trusted p=−1 tower at N=4 ----
    g2_ok = True
    print("\n[G2] 4₁ N=4 (3-cable, w=0) vs trusted Masbaum p=−1 tower:")
    for q in qs_test:
        jc = Jprime(BRAID_4_1, 3, 3, q, engines)
        jt = tower.J_twist(4, -1, q ** 2)
        err = min(abs(jc - jt) / abs(jt),
                  abs(jc - tower.J_twist(4, -1, q ** -2)) / abs(jt))
        g2_ok &= err < mp.mpf("1e-18")
        print(f"    q={q}: cable={mp.nstr(jc,10)}  tower={mp.nstr(jt,10)}  "
              f"rel={mp.nstr(err,3)}")
    print(f"    {'PASS' if g2_ok else 'FAIL'}")

    # ---- G3: framing calibration at N=4 — UNKNOT twist + trefoil cross-check
    # (run-2/3 lesson: the trefoil-only calibration mixed a wrong mirror map
    # with cube-root branches. The writhe-±1 unknot isolates the framing
    # exactly: fr = 1/J'_raw(unknot, w=1) — measured fr = −q^{7.5}, precisely
    # the ribbon twist θ_{V₄} = q_M^{15/4} with a sign. The trefoil then
    # matches the p=1 tower under the q² map (not q⁻²) at 1e-27 — the
    # mirror-convention question settled by the gate, not by reasoning.)
    print("\n[G3] N=4 framing: unknot-twist calibration + trefoil cross-check:")
    g3a = True
    for q in qs_test:
        fr = 1 / Jprime([1], 2, 3, q, engines)
        dev = abs(fr - (-(q ** mp.mpf("7.5")))) / q ** mp.mpf("7.5")
        g3a &= dev < mp.mpf("1e-20")
        print(f"    q={q}: fr = {mp.nstr(fr, 10)}  |fr + q^7.5| rel = {mp.nstr(dev, 3)}")
    g3b = True
    for q in qs_test[:2]:
        fr = -(q ** mp.mpf("7.5"))
        jz = fr ** 3 * Jprime(BRAID_TREF, 2, 3, q, engines)
        jt = tower.J_twist(4, 1, q ** 2)
        err = abs(jz - jt) / abs(jt)
        g3b &= err < mp.mpf("1e-20")
        print(f"    trefoil q={q}: zero-framed vs tower(q²) rel = {mp.nstr(err, 3)}")
    g3_ok = g3a and g3b
    print(f"    fr = −q^7.5 (ribbon) exact + trefoil cross-check: "
          f"{'PASS' if g3_ok else 'FAIL'}")
    ks = [mp.mpf('7.5')]

    # ---- THE TEST: certified B_N(5₂) q*-scan at N = 4 ----
    print("\n[T] certified B₄(5₂;q) on q* ± 2e-8 (zero-framed via fr^4):")
    half = mp.mpf("2e-8")
    npts = 7
    grid = [Q_STAR - half + 2 * half * i / (npts - 1) for i in range(npts)]

    # fr = −q^{7.5}; writhe 4 ⇒ fr⁴ = q^{30} (the sign drops at even writhe)
    def J4_framed(q):
        return q ** 30 * Jprime(BRAID_5_2, 3, 3, q, engines)

    vals = []
    for qq in grid:
        B = (J4_framed(qq) - J4_framed(1 / qq)) / 2
        vals.append(mp.re(B))
    sc = sum(1 for x, y in zip(vals, vals[1:]) if mp.sign(x) != mp.sign(y))
    B_star = vals[npts // 2]
    B_mu = mp.re((J4_framed(Q_MUON) - J4_framed(1 / Q_MUON)) / 2)
    B_pr = mp.re((J4_framed(Q_PROTON) - J4_framed(1 / Q_PROTON)) / 2)
    rel_slope = float(abs(B_mu - B_pr) / abs(B_mu) / (Q_MUON - Q_PROTON))
    no_zero = sc == 0 and abs(B_star) > 0
    print(f"    B₄(q*) = {mp.nstr(B_star, 8)}   sign changes = {sc}   "
          f"|d ln B/dq| ≈ {rel_slope:.3e}")
    # 4₁ null control at N=4
    b41 = (Jprime(BRAID_4_1, 3, 3, Q_STAR, engines)
           - Jprime(BRAID_4_1, 3, 3, 1 / Q_STAR, engines)) / 2
    j41 = abs(Jprime(BRAID_4_1, 3, 3, Q_STAR, engines))
    null_ok = abs(b41) / j41 < mp.mpf("1e-20")
    print(f"    4₁ null control: |B₄(4₁;q*)|/|J| = {mp.nstr(abs(b41)/j41, 3)}  "
          f"{'PASS' if null_ok else 'FAIL'}")
    print(f"    ⇒ N=4 categorical face: "
          f"{'NO zero at q*, anchor-smooth — constraint (2) fails (certified)' if no_zero and rel_slope < 1e5 else 'INSPECT'}")

    ok_gates = g1_ok and g2_ok and g3_ok

    wb = WitnessBuilder("qbeta-5two-higher-cable-qstar", engine="mpmath",
                        _script_path=__file__)
    wb.set_description(
        "A5.3 (bean qou-3yxn): the certified categorical q*-test extended to "
        "N=4 via the 3-cable with the full Jones–Wenzl e₃ (Wenzl recursion in "
        "the U-word algebra), on the A5.2-validated TL engine. Gates: N=3 "
        "regression vs the A5.2 path; 4₁ 3-cable (w=0) = the trusted Masbaum "
        "p=−1 tower at N=4; trefoil framing calibration (consistent ribbon "
        "power). TEST: B₄(5₂;q) has no zero on q*±2e-8 and is anchor-smooth; "
        "4₁ null control exact — capstone constraint (2) fails on the "
        "certified N=4 categorical face (scope-(a), extending N=3). "
        "auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_N3_regression",
                     computed=1.0 if g1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="generalized-JW path = A5.2 colored3_raw at 1e-25")
    wb.add_assertion("gate_41_N4_matches_trusted_tower",
                     computed=1.0 if g2_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="4₁ 3-cable J'_4 (framing-free) = trusted p=−1 tower")
    wb.add_assertion("gate_framing_calibration",
                     computed=1.0 if g3_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="trefoil N=4 framing factor a consistent power across q")
    wb.add_assertion("N4_no_qstar_zero",
                     computed=1.0 if no_zero else 0.0, expected=1.0, tolerance=0.5,
                     source="B₄(5₂): 0 sign changes on q*±2e-8, B₄(q*) ≠ 0")
    wb.add_assertion("N4_41_null_control",
                     computed=1.0 if null_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="B₄(4₁;q*) = 0 to 1e-20 — mirror/bar control at N=4")
    wb.add_assertion("anchor_smooth_honest",
                     computed=1.0 if rel_slope < 1e5 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="|d ln B₄/dq| ≪ 3.84e6 — anchor-smooth, not the swing")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("framing_power_N4", "fr = -q^7.5 (ribbon twist, unknot-calibrated exactly)")
    wb.add_data("qstar_test_N4", {"B_qstar": mp.nstr(B_star, 12),
                                  "sign_changes": sc,
                                  "rel_slope": f"{rel_slope:.4e}",
                                  "null_41": mp.nstr(abs(b41) / j41, 6)})
    wb.add_data("verdict",
                ("CERTIFIED N=4 CATEGORICAL FACE: no q* zero, anchor-smooth, "
                 "4₁-null exact — capstone constraint (2) fails at N=4 too "
                 "(scope-(a), extends the A5.2 N=3 certification). The "
                 "categorical carrier search continues to genuine limit "
                 "objects. auditOnly."
                 if ok else "A gate failed — inspect before any claim."))
    # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
    # pins deliberately, so no anchor list can classify it and it was going
    # out unstamped. Carries the values actually computed with.
    wb.save(q0_comparison(
        muon=Q_MUON, proton=Q_PROTON,
        reason='compares the higher-cable q* location against BOTH substrate pins; both pins are read on purpose and each is reported under its own key',
    ))
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-t0:.0f}s)")
    print("  witness -> computations/probes/qbeta-5two-higher-cable-qstar.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
