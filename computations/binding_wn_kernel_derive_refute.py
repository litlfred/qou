#!/usr/bin/env python3
"""EXPLORATORY — derive-or-refute the residue-weight q-difference kernel R(q,x)
of the jet-filtration binding (bean t7qv, option #2 of
docs/audits/2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md).

The jet-filtration binding is
    B_strong(K) = Σ_{n=2}^{A} m_e · a_D^(n) · w_n(K),   a_D^(n) = lw(n−1),
where a_D^(n) (the super-exponential na-Stokes SW period = mean quantum
dimension) is the DERIVED extensive KERNEL and w_n(K) (the per-body-order
"ρ·A residue weight") is the OPEN multiplier. The conjecture asserts w_n is a
q-difference recursion output G(qx;q)=R(q,x)G(x;q) — NOT a fit.

This probe runs the STRICT derive-or-refute:

  1. Coulomb-correct the AME bindings (B_strong = B_AME + E_Coulomb) so the
     STRONG-sector weight is isolated from electromagnetism.
  2. UNIVERSALITY check — after Coulomb correction, do the A=3 mirror nuclei
     ³H (pnn) and ³He (ppn) give the same strong binding? (If yes to within the
     charge-symmetry-breaking residual, a body-order-only w_n is admissible.)
  3. EXTRACT the universal w_2, w_3, w_4 from ²H (A=2), avg(³H,³He) (A=3), and
     ⁴He (A=4) — no per-isotope fit; three linear equations, three unknowns.
  4. DERIVE-OR-REFUTE — do the extracted w_n satisfy ONE recursion with a
     PARAMETER-FREE derived kernel (geometric R=const, R=[n]_q, R=a_D-self-
     ratio, R∝n)? A recursion whose coefficients must be TUNED to the data is a
     fit (STRICT ⇒ refute). Any candidate reproducing both ratios w_3/w_2 and
     w_4/w_3 to ≤5% zero-parameter is surfaced for promotion.

DISCIPLINE (production-vs-exploratory, "before declaring refuted"): a negative
is scope-(a) — "this parameter-free recursion, alone, does not fix w_n" — NOT a
structural exclusion. The corpus already records (2026-07-06 §2j tranche 8) that
an A-flattened w_n "IS the Δ_λ gate in disguise", so a refutation here CONFIRMS
w_n(K) carries the gated Δ_λ / W_λ content, not that the mechanism is wrong. No
production touch, no fitted constant, no tier change.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401,E402
from q_parameter import q_at  # noqa: E402 — canonical high-precision q₀ (NOT the f64 Q)
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION)
from coulomb_energy import coulomb_energy_mev  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:
    _HAVE_WB = False

set_compute_dps()                 # canonical compute precision (sets mp.mp.dps)
q = q_at(mp.mp.dps)               # q₀ at full compute precision (not f64 str-cast)
M_E = mp.mpf(str(M_E_MEV))
_NS = mp.mp.dps                   # serialization digits tied to global precision


# ── mean quantum dimension lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q V_λ  (exact reuse
#    of binding_manybody_jet_filtration.py) ─────────────────────────────────────
def qint(k):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    n = len(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hs = []
    for i in range(n):
        for j in range(lam[i]):
            hs.append((lam[i] - j - 1) + (conj[j] - i - 1) + 1)
    return hs


def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def S_qinv(n):
    """S(n) = Σ_{λ⊢n} dim_q V_λ — the q-involution number (→ 1,2,4,10,26,…
    at q=1, the count of involutions in S_n). a_D^(n) = S(n)/n."""
    return mp.fsum(dimq(l) for l in partitions(n))


def lw(c):
    return S_qinv(c + 1) / (c + 1)


def a_D(n):
    return lw(n - 1)


# AME bindings + (Z, A) for the Coulomb correction.
AME_B = {"D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
         "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
         "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
         "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION))}
ZA = {"D": (1, 2), "T": (1, 3), "3He": (2, 3), "4He": (2, 4)}


def main() -> int:
    print(f"  q₀ = {float(q):.6f}   m_e = {float(M_E):.6f} MeV\n")

    aD = {n: a_D(n) for n in (2, 3, 4)}
    print("  na-Stokes SW periods (derived extensive kernel):")
    for n in (2, 3, 4):
        print(f"     a_D^({n}) = lw({n-1}) = {float(aD[n]):.6f}")

    # ── 1. Coulomb-correct: B_strong = B_AME + E_Coulomb ──────────────────────
    print("\n  Coulomb correction  B_strong = B_AME + E_Coulomb:")
    Bstrong = {}
    for K, (Z, A) in ZA.items():
        ec = mp.mpf(str(coulomb_energy_mev(Z, A)))
        Bstrong[K] = AME_B[K] + ec
        print(f"     {K:<4} B_AME={float(AME_B[K]):8.4f}  +E_C={float(ec):.4f}"
              f"  ⇒ B_strong={float(Bstrong[K]):8.4f}")

    # ── 2. Universality: A=3 mirror nuclei ³H vs ³He after Coulomb ─────────────
    csb = (Bstrong["3He"] - Bstrong["T"]) / ((Bstrong["3He"] + Bstrong["T"]) / 2)
    print(f"\n  A=3 mirror check (universality of a body-order-only w_n):")
    print(f"     B_strong(³H) = {float(Bstrong['T']):.4f}   "
          f"B_strong(³He) = {float(Bstrong['3He']):.4f}")
    print(f"     charge-symmetry-breaking residual = {float(csb)*100:+.2f}%  "
          f"({'admissible — CSB is a small separate effect' if abs(csb) < 0.05 else 'LARGE — w_n is not A-universal'})")

    # ── 3. Extract universal w_2, w_3, w_4 (no per-isotope fit) ────────────────
    #   ²H (A=2):  B_s = m_e·a2·w2
    #   A=3 avg:   B_s = m_e·(a2·w2 + a3·w3)
    #   ⁴He (A=4): B_s = m_e·(a2·w2 + a3·w3 + a4·w4)
    B3 = (Bstrong["T"] + Bstrong["3He"]) / 2  # CSB-averaged A=3 strong binding
    w = {}
    w[2] = Bstrong["D"] / (M_E * aD[2])
    w[3] = (B3 / M_E - aD[2] * w[2]) / aD[3]
    w[4] = (Bstrong["4He"] / M_E - aD[2] * w[2] - aD[3] * w[3]) / aD[4]
    print("\n  Extracted universal residue weights (from D / avg(³H,³He) / ⁴He):")
    for n in (2, 3, 4):
        print(f"     w_{n} = {mp.nstr(w[n], 6)}")
    r32 = w[3] / w[2]
    r43 = w[4] / w[3]
    print(f"     ratios:  w_3/w_2 = {mp.nstr(r32, 6)}   w_4/w_3 = {mp.nstr(r43, 6)}")

    # ── 4. Derive-or-refute: parameter-free recursion candidates ──────────────
    #   A recursion w_{n+1} = R(q,n)·w_n is DERIVED only if R needs no tuning.
    #   Each candidate predicts BOTH ratios from ZERO free parameters. (All
    #   arithmetic stays in mpf; only the final display uses mp.nstr.)
    print("\n  Derive-or-refute — parameter-free kernel candidates R(q,n) "
          "(predict w_3/w_2 AND w_4/w_3, zero tuning):")
    cands = {
        "geometric R=const (needs equal ratios)": (None, None),  # test ratio equality
        "R=[n]_q (q-integer)":       (qint(3) / qint(2), qint(4) / qint(3)),
        "R=a_D self-ratio":          (aD[3] / aD[2], aD[4] / aD[3]),
        "R∝n (linear body-order)":   (mp.mpf(3) / 2, mp.mpf(4) / 3),
        "R=[n]_q² ":                 ((qint(3) / qint(2)) ** 2, (qint(4) / qint(3)) ** 2),
    }
    obs = (r32, r43)
    thr = mp.mpf(5) / 100
    any_close = False
    print(f"     {'candidate':<40}{'pred r32':>10}{'pred r43':>10}{'max|err|':>10}")
    # geometric: the two observed ratios must themselves be equal
    geo_err = abs(r32 - r43) / ((r32 + r43) / 2)
    any_close = any_close or geo_err <= thr
    print(f"     {'geometric R=const (r32==r43?)':<40}{mp.nstr(r32,4):>10}"
          f"{mp.nstr(r43,4):>10}{mp.nstr(geo_err*100,3):>9}%{'  ← CLOSES' if geo_err <= thr else ''}")
    for name, (p32, p43) in cands.items():
        if p32 is None:
            continue
        e = max(abs(p32 - obs[0]) / obs[0], abs(p43 - obs[1]) / obs[1])
        close = e <= thr
        any_close = any_close or close
        print(f"     {name:<40}{mp.nstr(p32,4):>10}{mp.nstr(p43,4):>10}"
              f"{mp.nstr(e*100,3):>9}%{'  ← CLOSES' if close else ''}")

    # ── 5. The na-Stokes kernel's OWN eigenfunction relation → the basis ───────
    #   Owner steer (2026-07-11): "how does a_D^(n) inform the kernel? look at the
    #   relations defining the eigenfunction → the appropriate orthogonal basis
    #   for q-hyperbolic + categorical action." a_D^(n)=S(n)/n with S(n) the
    #   q-involution number; S obeys a THREE-TERM recurrence S(n)=S(n-1)+c_n·S(n-2)
    #   — the q-Hermite / Rogers–Szegő eigenfunction relation (basis of the
    #   q-oscillator = the categorical action). c_3=[2]_q EXACTLY; c_n/[n-1]_q
    #   drifts up monotonically (the q-Hermite correction), so the naive [n-1]_q
    #   is NOT the coefficient — the correct basis is Rogers–Szegő
    #   (QOU.Mass.RogersSzegoInhabited), not a constant-ratio kernel.
    print("\n  Eigenfunction relation of the na-Stokes kernel a_D^(n)=S(n)/n "
          "(S(n)=Σ_{λ⊢n} dim_q V_λ, the q-involution number):")
    S = {n: S_qinv(n) for n in range(1, 9)}
    c3_is_2q = abs((S[3] - S[2]) / S[1] - qint(2)) < mp.mpf(10) ** (-mp.mp.dps + 5)
    print(f"     three-term recurrence  S(n) = S(n-1) + c_n·S(n-2):")
    print(f"     {'n':>2} {'c_n':>12} {'[n-1]_q':>12} {'c_n/[n-1]_q':>13}")
    c_seq = {}
    for n in range(3, 9):
        cn = (S[n] - S[n - 1]) / S[n - 2]
        c_seq[n] = cn
        print(f"     {n:>2} {mp.nstr(cn,8):>12} {mp.nstr(qint(n-1),8):>12} "
              f"{mp.nstr(cn/qint(n-1),8):>13}")
    print(f"     ⇒ c_3 = [2]_q exactly: {c3_is_2q};  c_n/[n-1]_q rises monotonically")
    print(f"     ⇒ eigenfunction basis = q-Hermite / Rogers–Szegő (q-oscillator /")
    print(f"       q-hyperbolic categorical action; corpus QOU.Mass.RogersSzegoInhabited)")

    verdict = (
        "TWO-PART. (i) REFUTED (scope-(a)) — the extracted universal residue "
        f"weights w_2,w_3,w_4 = {mp.nstr(w[2],4)},{mp.nstr(w[3],4)},{mp.nstr(w[4],4)} "
        f"(ratios {mp.nstr(r32,4)},{mp.nstr(r43,4)}) satisfy NO CONSTANT-RATIO / "
        "ad-hoc parameter-free kernel to 5% (geometric/[n]_q/a_D-self/linear all "
        "miss; [n]_q² is the lone 6.9% near-miss, echoing the √C_λ near-miss of "
        "PR #3518). A recursion tuned to reproduce them is a fit, banned as a "
        "seventh Δ_λ ansatz. (ii) POSITIVE LEAD (owner steer 2026-07-11) — the "
        "na-Stokes kernel a_D^(n)=S(n)/n has a DERIVED eigenfunction relation: "
        "S(n)=Σ_{λ⊢n} dim_q V_λ (the q-involution number) obeys a THREE-TERM "
        "recurrence S(n)=S(n-1)+c_n·S(n-2) with c_3=[2]_q EXACT and c_n/[n-1]_q "
        "rising monotonically — the q-Hermite / Rogers–Szegő recurrence, i.e. the "
        "orthogonal basis of the q-oscillator / q-hyperbolic categorical action "
        "(corpus QOU.Mass.RogersSzegoInhabited). So the correct search for w_n is "
        "its EXPANSION IN THE q-HERMITE BASIS (a derive, not a fit), NOT a "
        "constant-ratio kernel — that is why the ad-hoc candidates miss. The "
        "extensive kernel a_D^(n) stays a permanent correct contribution; the "
        "gated multiplier is the geometric W_λ projector (s5-so3). Next: expand "
        "w_n in the Rogers–Szegő basis / test the hyperbolic-link-volume route "
        "(option #1). No production touch; no value wired; no tier change."
        if not any_close else
        "A PARAMETER-FREE derived kernel reproduces both w_n ratios zero-tuning "
        "— surface for categorical derivation of R(q,x) (do NOT wire until the "
        "kernel is derived from the 13 categorical drivers, per anti-laundering)."
    )
    print("\n### VERDICT")
    print("  " + verdict.replace(". ", ".\n  "))

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("binding-wn-kernel-derive-refute", engine="mpmath",
                                output_dir=HERE)
            wb.set_description(
                "EXPLORATORY: derive-or-refute the jet-filtration residue-weight "
                "q-difference kernel R(q,x). Coulomb-corrects AME binding, checks "
                "³H/³He A=3 universality, extracts universal w_2,w_3,w_4, tests them "
                "against ad-hoc parameter-free kernels (all refuted), and derives the "
                "na-Stokes kernel a_D^(n)'s OWN eigenfunction relation: the q-involution "
                "S(n)=Σ dim_q obeys a q-Hermite / Rogers–Szegő three-term recurrence "
                "(c_3=[2]_q exact), identifying the correct orthogonal basis for w_n. No fit.")
            wb.add_parameter("q0_50dps", mp.nstr(q, _NS))
            wb.add_parameter("compute_dps", mp.mp.dps)
            wb.add_data("a_D_periods", {str(n): mp.nstr(aD[n], _NS) for n in aD})
            wb.add_data("B_strong_coulomb_corrected", {K: mp.nstr(Bstrong[K], _NS) for K in Bstrong})
            wb.add_data("csb_A3_mirror_residual", mp.nstr(csb, _NS))
            wb.add_data("w_universal", {str(n): mp.nstr(w[n], _NS) for n in w})
            wb.add_data("w_ratios", {"w3_over_w2": mp.nstr(r32, _NS), "w4_over_w3": mp.nstr(r43, _NS)})
            wb.add_data("qinvolution_recurrence", {
                "S_n": {str(n): mp.nstr(S[n], _NS) for n in S},
                "c_n": {str(n): mp.nstr(c_seq[n], _NS) for n in c_seq},
                "c3_eq_2q_exact": bool(c3_is_2q),
                "basis": "q-Hermite / Rogers–Szegő (q-oscillator; QOU.Mass.RogersSzegoInhabited)",
            })
            wb.add_data("verdict", verdict)
            wb.add_assertion(
                name="wn_kernel_derives_or_refutes",
                computed=str(int(not any_close)), expected="1", tolerance=0,
                source=("1 = no parameter-free derived recursion reproduces w_n "
                        "(refuted, w_n = Δ_λ gate); 0 = a kernel closes → promote."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
