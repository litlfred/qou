#!/usr/bin/env python3
"""
theta_wn_jetfilt_linkvolume.py — closure OPTION 1 (refined) for the θ_λ weight w_n(K).

Option 2 (theta_wn_kernel_derive_or_refute.py) refuted a universal scalar kernel:
the ³H/³He mirror split (13%) means w_n(K) must be isospin-aware. The hyperbolic
link-volume IS isospin-aware (³H=8_11 vol 8.286 ≠ ³He=L6a4 vol 7.328), so option 1
sets w_n(K) ∝ the n-body sub-link volume. BUT a prior RAW single-term attempt
(binding-link-volumes.witness.json) undershoots ~60% at A=3 and hits the deuteron
Hopf-vol=0 wall.

The UNTRIED refinement is the JET-FILTRATION combination: multiply the volume by the
SUPER-EXPONENTIAL SW period a_D^(n)=lw(n−1) (the extensive channel of PR #3270) and
sum over body orders. This probe tests, with NO per-isotope fit, whether that
combination closes the gap — comparing:

  (raw)   B = m_e · Vol_A(K)                       [prior single-term, ~−60%]
  (jet)   B = m_e · a_D^(A) · Vol_A(K)             [super-exp × top-order volume]
  (magic) B = 2 · m_e · A · Vol_A(K)               [magic-A anchor, prop:magic-A-binding]

Honest expectation flagged in the audit: the ⁴He magic-shell wants a 2·A=8
multiplicity, while a_D^(4)=2.53 — so a_D^(n) and the magic multiplicity are
DIFFERENT objects. This probe measures whether the super-exp helps and by how much.

EXPLORATORY — asserts the finding, no production wiring, no fitted constant.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
)
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q = mp.mpf(str(Q0))
M_E = mp.mpf(str(M_E_MEV))


def qint(k): return (q ** k - q ** (-k)) / (q - 1 / q)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1): p *= qint(k)
    return p
def partitions(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k): yield (k,) + r
def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i]-j-1)+(conj[j]-i-1)+1 for i in range(len(lam)) for j in range(lam[i])]
def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam): d /= qint(h)
    return d
def lw(c): return mp.fsum(dimq(l) for l in partitions(c + 1)) / (c + 1)
def a_D(n): return lw(n - 1)


# ── whole-atom hyperbolic link volumes (binding-link-volumes.witness.json) ─────
#   isospin-aware: ³H (pnn) = 8_11 ≠ ³He (ppn) = L6a4; deuteron = Hopf (Vol 0);
#   ⁴He magic shell uses Vol(L6a4) (prop:magic-A-binding-formula).
VOL = {"D": mp.mpf("0.0"),                 # Hopf L2a1 — Seifert-fibred, Vol=0
       "T": mp.mpf("8.286316817806593"),   # 8_11
       "3He": mp.mpf("7.327724753417752"), # L6a4 (= Borromean)
       "4He": mp.mpf("7.327724753417752")} # Vol(L6a4), magic-shell base
AME = {"D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
       "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
       "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
       "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION))}
A = {"D": 2, "T": 3, "3He": 3, "4He": 4}


def report(name, model):
    print(f"  {name}")
    worst = mp.mpf(0)
    for K in AME:
        Bp = model(K)
        err = (Bp - AME[K]) / AME[K] if AME[K] else mp.mpf(0)
        worst = max(worst, abs(err))
        print(f"     {K:<4} B={float(Bp):8.4f}  AME={float(AME[K]):8.4f}  err={float(err)*100:+8.1f}%")
    print(f"     worst |err| = {float(worst)*100:.1f}%\n")
    return float(worst)


def main() -> int:
    print(f"  q₀={float(q):.6f}  m_e={float(M_E):.6f}  "
          f"a_D^(2,3,4)=({float(a_D(2)):.3f},{float(a_D(3)):.3f},{float(a_D(4)):.3f})")
    print(f"  Vol: D(Hopf)={float(VOL['D'])}  ³H(8_11)={float(VOL['T']):.3f}  "
          f"³He(L6a4)={float(VOL['3He']):.3f}\n")

    w_raw   = report("(raw)   B = m_e·Vol_A",
                     lambda K: M_E * VOL[K])
    w_jet   = report("(jet)   B = m_e·a_D^(A)·Vol_A",
                     lambda K: M_E * a_D(A[K]) * VOL[K])
    w_magic = report("(magic) B = 2·m_e·A·Vol_A",
                     lambda K: 2 * M_E * A[K] * VOL[K])

    print("### Verdict — closure option 1 (jet-filtration × link-volume)")
    print(f"  • raw single-term worst |err| = {w_raw*100:.0f}%  (deuteron Vol=0 ⇒ B=0; A=3 ~−60%)")
    print(f"  • super-exp × volume worst    = {w_jet*100:.0f}%  "
          f"({'HELPS' if w_jet < w_raw else 'no better'} vs raw)")
    print(f"  • magic-shell 2·A·Vol worst   = {w_magic*100:.0f}%")
    print("  • Structural reading: the volume supplies the ISOSPIN-awareness (³H>³He,")
    print("    matching the binding order), but the ⁴He magic shell wants the 2·A=8")
    print("    multiplicity, NOT a_D^(4)=2.53 — so the super-exp a_D^(n) and the")
    print("    magic-shell multiplicity are DIFFERENT objects. The deuteron Hopf Vol=0")
    print("    remains a structural wall (2-body sub-link is non-hyperbolic).")
    print("  • ⇒ option 1 (link-volume) is the right ISOSPIN carrier but does NOT close")
    print("    the MAGNITUDE via a single a_D^(n)·Vol product; closure needs the volume")
    print("    (isospin) × a body-order MULTIPLICITY (magic/cluster count), with the")
    print("    Hopf-Vol=0 deuteron handled separately. Narrows the open weight to")
    print("    w_n(K) = (n-body multiplicity) × Vol_n(K), not a_D^(n)·Vol.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("theta-wn-jetfilt-linkvolume", engine="mpmath")
            wb.set_description(
                "Closure option 1 refined: jet-filtration × hyperbolic link-volume. The "
                "volume is the correct isospin carrier (³H>³He), but a_D^(n)·Vol does not "
                "close the magnitude — ⁴He magic shell wants 2·A multiplicity ≠ a_D^(4); "
                "deuteron Hopf Vol=0 is a structural wall. Narrows w_n(K) to "
                "(multiplicity)×Vol_n(K). No fit.")
            wb.add_data("worst_err", {"raw": w_raw, "jet_super_exp": w_jet, "magic_2A": w_magic})
            wb.add_data("volumes", {k: float(VOL[k]) for k in VOL})
            wb.add_assertion(
                name="aDn_times_volume_does_not_close_magnitude",
                computed=str(int(w_jet > 0.05)), expected="1", tolerance=0,
                source=(f"super-exp a_D^(n)·Vol worst |err| = {w_jet*100:.0f}% (>5%): volume is "
                        "the isospin carrier but a_D^(n) ≠ the magic-shell 2·A multiplicity; "
                        "closure needs (multiplicity)×Vol_n(K), Hopf-Vol=0 deuteron separate."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
