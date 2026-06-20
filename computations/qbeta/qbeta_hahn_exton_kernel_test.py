#!/usr/bin/env python3
"""Q_β c_k — Hahn–Exton trivial-kernel identification test (formalize-first).

Stage-C context (bean qkhc; registry docs/coordination/ck-dk-canonical-registry.md):
only c_2=−1 is canonical; c_k live in the FIBRE; the OPEN object is the kernel
R(q,ξ) of the q-difference equation F(qξ)=R(q,ξ)·F(ξ) whose Habiro element F(q)
generates the c_k ladder. The Hahn–Exton q-Bessel coefficients

    c_k^HE(q,ν) = (−1)^k q^{k(k−1)/2} / [(q;q)_k (q^{ν+1};q)_k]

satisfy the EXACT first-order q-holonomic recurrence (QBesselContiguityRecurrence.lean):

    c_{k+1}·(1−q^{k+1})(1−a q^k) = −q^k·c_k,   a = q^{ν+1},
  ⇒ ratio  r_k(q,ν) = c_{k+1}/c_k = −q^k / [(1−q^{k+1})(1−q^{ν+1+k})].

THIS PROBE tests the SIMPLEST kernel hypothesis — that the Q_β multiplicative
ladder c_k IS the Hahn–Exton family for some single order ν (i.e. the kernel R is
the bare Hahn–Exton ratio, no extra structure). It is normalization-free: it
works with the RATIOS r_k = c_{k+1}/c_k, pinning ν from the one trusted ratio and
predicting the next, at two levels:

  Level A — substrate anchor q₀ (real): the Hahn–Exton ratio r_2(q₀,ν) has a
            structurally FORBIDDEN range. r_2 = −q²/[(1−q³)(1−q^{ν+3})]; with
            q₀>1, (1−q³)<0, so as q^{ν+3} ranges over (0,∞) the achievable r_2
            covers (−∞,0) ∪ (q²/(q³−1), ∞) — the interval (0, q²/(q³−1)) is
            UNREACHABLE for any real ν. We check whether r_2^emp = c_3/c_2 lands
            in that gap (⇒ no real ν ⇒ refute trivial kernel at q₀).

  Level B — q=1 shadow (classical Bessel J_ν): c_k^HE → b_k = (−1)^k/(k! (ν+1)_k)
            (the fibre object's classical limit). Shadow ratio
            ρ_k = b_{k+1}/b_k = −1/[(k+1)(ν+k+1)]. Pin ν from ρ at the c_3/c_2
            rung; predict the c_4/c_3 rung; compare to empirical.

Empirical (registry): c_2=−1 (canonical, proved), c_3=−2 (near-match integer),
c_4=−0.97157 (CODATA residual). DISCIPLINE: tests one named kernel hypothesis and
records its refutation as a structural class (C14); proposes NO c_k value, tunes
NO free parameter (ν is pinned by one ratio, then USED to predict, not fitted to
all). EXPLORATORY — no production rewire. Emits
`qbeta-hahn-exton-kernel-test.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"

# Empirical ladder (registry ck-dk-canonical-registry.md §3).
C_EMP = {2: mp.mpf("-1"), 3: mp.mpf("-2"), 4: mp.mpf("-0.97157")}


def he_ratio(q: mp.mpf, nu: mp.mpf, k: int) -> mp.mpf:
    """r_k(q,ν) = −q^k / [(1−q^{k+1})(1−q^{ν+1+k})]."""
    return -q**k / ((1 - q**(k + 1)) * (1 - q**(nu + 1 + k)))


def shadow_ratio(nu: mp.mpf, k: int) -> mp.mpf:
    """q=1 classical-Bessel shadow ratio ρ_k = b_{k+1}/b_k = −1/[(k+1)(ν+k+1)]."""
    return -1 / ((k + 1) * (nu + k + 1))


def main() -> int:
    w = WitnessBuilder("qbeta-hahn-exton-kernel-test", engine="mpmath")
    w.set_audit_only("docs/audits/2026-06-20-qbeta-hahn-exton-kernel-test.md")
    w.set_description(
        "Q_β Stage-C: tests the trivial-kernel hypothesis that the c_k ladder IS "
        "the Hahn–Exton q-Bessel family for some single order ν, normalization-"
        "free via ratios, at the substrate anchor q₀ (forbidden-gap analysis) and "
        "the q=1 classical-Bessel shadow (pin-ν-predict-next). EXPLORATORY; "
        "records the refuted kernel class C14, proposes no c_k value, no fit."
    )

    q = mp.mpf(Q_0_50DPS)
    r2_emp = C_EMP[3] / C_EMP[2]          # = 2
    r3_emp = C_EMP[4] / C_EMP[3]          # ≈ 0.4858

    print("=" * 78)
    print("Q_β c_k — Hahn–Exton trivial-kernel identification test")
    print("=" * 78)
    print(f"  q₀ = {float(q):.10f}")
    print(f"  empirical ratios: r_2 = c_3/c_2 = {float(r2_emp):+.6f}   "
          f"r_3 = c_4/c_3 = {float(r3_emp):+.6f}\n")

    # ── Level A: q₀ forbidden gap for r_2 ──
    gap_hi = q**2 / (q**3 - 1)            # achievable r_2 ∈ (−∞,0) ∪ (gap_hi, ∞)
    in_gap = mp.mpf(0) < r2_emp < gap_hi
    print("Level A — substrate anchor q₀ (real ν):")
    print(f"  Hahn–Exton r_2 achievable range: (−∞, 0) ∪ ({float(gap_hi):.6f}, ∞)")
    print(f"  forbidden gap: (0, {float(gap_hi):.6f})")
    print(f"  r_2^emp = {float(r2_emp):+.6f}  →  "
          f"{'IN forbidden gap ⇒ NO real ν' if in_gap else 'reachable'}")
    # the ν that would be needed (shows q^{ν+3} < 0, impossible)
    # r_2 = −q²/[(1−q³)(1−q^{ν+3})]  ⇒  1−q^{ν+3} = −q²/[r_2 (1−q³)]
    q_nu3_needed = 1 - (-q**2 / (r2_emp * (1 - q**3)))
    print(f"  solving r_2(q₀,ν)=r_2^emp ⇒ q^(ν+3) = {float(q_nu3_needed):+.6f} "
          f"({'NEGATIVE — impossible for real ν' if q_nu3_needed <= 0 else 'ok'})\n")

    # ── Level B: q=1 shadow, pin ν from r_2, predict r_3 ──
    # ρ_2(ν) = −1/[3(ν+3)] = r2_emp  ⇒  ν = −1/(3 r2_emp) − 3
    nu_pin = -1 / (3 * r2_emp) - 3
    r3_shadow_pred = shadow_ratio(nu_pin, 3)   # ρ_3 = −1/[4(ν+4)]
    rel_B = (r3_shadow_pred - r3_emp) / r3_emp
    sign_flip_B = (r3_shadow_pred < 0) != (r3_emp < 0)
    print("Level B — q=1 classical-Bessel shadow (pin ν from r_2, predict r_3):")
    print(f"  ν pinned by ρ_2 = r_2^emp:  ν = {float(nu_pin):+.6f}")
    print(f"  predicted r_3 shadow ρ_3 = {float(r3_shadow_pred):+.6f}  vs  "
          f"r_3^emp = {float(r3_emp):+.6f}")
    print(f"  rel err = {float(rel_B):+.3e}  "
          f"{'(SIGN FLIP)' if sign_flip_B else ''}\n")

    refuted_A = bool(in_gap)
    refuted_B = abs(rel_B) > mp.mpf("5e-2")
    verdict = (
        "REFUTED — trivial-kernel Hahn–Exton identification excluded at BOTH "
        "levels. "
        f"Level A: r_2^emp = {float(r2_emp):+.4f} lies in the structurally "
        f"forbidden gap (0, {float(gap_hi):.4f}) of the Hahn–Exton ratio at q₀ — "
        f"reproducing it would require q^(ν+3) = {float(q_nu3_needed):+.4f} < 0, "
        f"impossible for real ν. "
        f"Level B: pinning ν = {float(nu_pin):.4f} from the q=1 shadow r_2 and "
        f"predicting r_3 gives {float(r3_shadow_pred):+.4f} vs empirical "
        f"{float(r3_emp):+.4f} ({'sign-flipped, ' if sign_flip_B else ''}"
        f"rel err {float(rel_B):.1%}). "
        "CONCLUSION: the bare Hahn–Exton ratio is NOT the Q_β kernel — a "
        "NON-trivial kernel R(q,ξ) is required (consistent with the OPEN-keystone "
        "status in the registry). Recorded as refuted class C14 (trivial-kernel "
        "Hahn–Exton identification). No c_k value proposed, no fit."
    )
    print("VERDICT:")
    for chunk in verdict.split(". "):
        print(f"  {chunk.strip()}")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("r2_emp", str(r2_emp))
    w.add_parameter("r3_emp", str(r3_emp))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("level_A_q0", {
        "forbidden_gap_hi": str(gap_hi),
        "r2_emp_in_forbidden_gap": refuted_A,
        "q_nu_plus_3_needed": str(q_nu3_needed),
        "real_nu_exists": bool(q_nu3_needed > 0),
    })
    w.add_data("level_B_shadow", {
        "nu_pinned_from_r2": str(nu_pin),
        "r3_shadow_predicted": str(r3_shadow_pred),
        "r3_empirical": str(r3_emp),
        "relative_error": str(rel_B),
        "sign_flip": sign_flip_B,
        "refuted": refuted_B,
    })
    w.add_data("refuted_class", "C14 — trivial-kernel Hahn–Exton identification")
    w.add_data("verdict", verdict)

    w.add_assertion(
        "level_A_r2_in_forbidden_gap",
        computed=refuted_A,
        expected=True,
        tolerance=0.0,
        source="r_2^emp = 2 must lie in the Hahn–Exton forbidden gap "
               "(0, q²/(q³−1)) at q₀ (no real ν reproduces it).",
    )
    w.add_assertion(
        "level_B_shadow_prediction_refuted",
        computed=refuted_B,
        expected=True,
        tolerance=0.0,
        source="q=1 shadow: ν pinned from r_2 must mispredict r_3 by > 5% "
               "(single-ν Hahn–Exton shadow excluded).",
    )

    out = w.save()
    try:
        rel = out.relative_to(COMPUTE_DIR.parent)
    except ValueError:
        rel = out
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
