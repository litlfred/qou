#!/usr/bin/env python3
"""
theta_wn_kernel_derive_or_refute.py — closure OPTION 2 for the θ_λ magnitude gate
(follow-up to the merged binding_manybody_jet_filtration.py / PR #3270).

The jet-filtration binding B(K) = Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K) has the extensive
mechanism established (a_D^(n) = lw(n−1) super-exp, Lean-proved monotone). The open
piece is the residue weight w_n(K). The conjecture says its growth is a q-difference
recursion OUTPUT (`G(qx;q)=R(q,x)G(x;q)`), NOT a fit — so the decisive test is:

  DERIVE  : the anchors fix a UNIVERSAL (K-independent) per-body-order weight w_n
            that follows one recursion ⇒ w_n(K) = (structure) is derivable.
  REFUTE  : the anchors need PER-ISOTOPE weights (w_n(K) depends on Z,N not just A)
            ⇒ no universal scalar kernel; the weight carries isospin structure.

The sharp discriminant is the **mirror pair** T (³H, Z=1,N=2) vs ³He (Z=2,N=1):
same A=3, same body orders {2,3}, but different binding. Under a universal w_n the
extracted w_3 MUST agree between them; a split refutes the universal-scalar kernel
and points at the isospin (T₃) weight — exactly the IMME degree-2 structure already
on main (2026-06-29-delta-lambda-imme-askey).

EXPLORATORY — asserts the finding, no production wiring, no fitted production constant.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None  # explicit fallback
    _HAVE_WB = False

set_compute_dps()
q = mp.mpf(str(Q0))
M_E = mp.mpf(str(M_E_MEV))


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
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]

def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d

def lw(c):
    return mp.fsum(dimq(l) for l in partitions(c + 1)) / (c + 1)

def a_D(n):
    return lw(n - 1)


B = {"D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
     "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
     "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
     "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION))}


def main() -> int:
    print(f"  q₀={float(q):.6f}  m_e={float(M_E):.6f} MeV")
    aD = {n: a_D(n) for n in range(2, 5)}
    print(f"  a_D^(n): " + "  ".join(f"a_D^({n})={float(aD[n]):.4f}" for n in aD) + "\n")

    # ── Extract UNIVERSAL (K-independent) weights from the anchors ─────────────
    #   D  (A=2): B_D = m_e·a_D^(2)·w2                       ⇒ w2
    #   T  (A=3): B_T = m_e·(a_D^(2)·w2 + a_D^(3)·w3T)       ⇒ w3 from ³H
    #   ³He(A=3): B_He3 = m_e·(a_D^(2)·w2 + a_D^(3)·w3He)    ⇒ w3 from ³He
    #   ⁴He(A=4): B_He4 = m_e·(...+ a_D^(4)·w4)              ⇒ w4
    w2 = B["D"] / (M_E * aD[2])
    w3_T = (B["T"] / M_E - aD[2] * w2) / aD[3]
    w3_He = (B["3He"] / M_E - aD[2] * w2) / aD[3]
    # ⁴He (T₃=0) uses the isospin-SYMMETRIC mirror average of w3 (not one branch),
    # so the w4 extraction carries no ³H-vs-³He bias.
    w3_avg = (w3_T + w3_He) / 2
    w4 = (B["4He"] / M_E - aD[2] * w2 - aD[3] * w3_avg) / aD[4]

    print("  Universal-weight extraction (hypothesis: w_n is K-independent):")
    print(f"     w2 (from D)          = {float(w2):8.4f}")
    print(f"     w3 (from ³H)         = {float(w3_T):8.4f}")
    print(f"     w3 (from ³He)        = {float(w3_He):8.4f}   ← MIRROR PARTNER")
    print(f"     w4 (⁴He, sym-avg w3) = {float(w4):8.4f}   ← CONDITIONAL "
          f"(universality already refuted at A=3; shown for completeness)\n")

    # ── The decisive discriminant: the mirror split ───────────────────────────
    split = abs(w3_T - w3_He) / ((w3_T + w3_He) / 2)
    print(f"  MIRROR SPLIT  |w3(³H) − w3(³He)| / mean = {float(split)*100:.1f}%")
    universal = split < mp.mpf("0.02")
    print(f"     universal-scalar w_n holds (split < 2%)?  {bool(universal)}\n")

    # ── Do the (nominal) weights follow a clean single recursion? ─────────────
    print("  Weight ratios (single-kernel test, mirror-symmetric w3):")
    r32 = w3_avg / w2
    r43 = w4 / w3_avg
    print(f"     w3/w2 = {float(r32):.3f}   w4/w3 = {float(r43):.3f}")
    print(f"     (a q-Bessel/geometric kernel would give a smooth ratio law;")
    print(f"      the isospin split above already breaks a single scalar kernel)\n")

    print("### Verdict — closure option 2")
    if not universal:
        print("  • UNIVERSAL SCALAR KERNEL R(q,x) is REFUTED by the mirror pair:")
        print(f"    ³H and ³He (same A=3, same body orders) need DIFFERENT w3 ")
        print(f"    ({float(w3_T):.2f} vs {float(w3_He):.2f}, {float(split)*100:.1f}% split).")
        print("    ⇒ w_n(K) carries ISOSPIN (Z−N / T₃) structure, not just body order.")
        print("  • This is CONSISTENT with the IMME degree-2 T₃ form found on main")
        print("    (2026-06-29-delta-lambda-imme-askey): the weight is w_n(A,T₃),")
        print("    a(A)+b(A)T₃+c(A)T₃², not a single scalar recursion output.")
        print("  • So closure needs the OPTION-1 route (per-sub-link hyperbolic")
        print("    VOLUME, which is intrinsically Z,N-aware via the link topology),")
        print("    NOT a universal q-difference scalar kernel. Refutes a fit shortcut.")
    else:
        print("  • Universal w_n holds — test the q-difference recursion next.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("theta-wn-kernel-derive-or-refute", engine="mpmath")
            wb.set_description(
                "Closure option 2: extract per-body-order weights w_n from the AME "
                "anchors; the ³H/³He mirror split refutes a universal scalar q-difference "
                "kernel R(q,x) and shows w_n(K) carries isospin (T₃) structure (IMME "
                "degree-2). Points closure to option 1 (per-sub-link hyperbolic volume). "
                "No fit, no production wiring.")
            wb.add_data("a_D", {str(n): float(aD[n]) for n in aD})
            wb.add_data("weights", {"w2": float(w2), "w3_T": float(w3_T),
                                    "w3_He": float(w3_He), "w4": float(w4)})
            wb.add_data("mirror_split_frac", float(split))
            wb.add_assertion(
                name="universal_scalar_wn_kernel_refuted_by_mirror_split",
                computed=str(int(not universal)), expected="1", tolerance=0,
                source=(f"³H/³He mirror split in extracted w3 = {float(split)*100:.1f}% "
                        "(> 2%) ⇒ no universal scalar kernel; w_n(K) is isospin-dependent "
                        "(IMME T₃), closure ⇒ option 1 (per-sub-link hyperbolic volume)."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
