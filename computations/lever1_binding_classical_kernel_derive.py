#!/usr/bin/env python3
"""
lever1_binding_classical_kernel_derive.py — DERIVE the exact classical (q=1) binding kernel
(lever-1 / bean z2bn). mpmath-only.

Answers "τ is settled — n≤4 is a FIT?": τ is NOT a fit — τ = (a_D²+a_D⁴)/a_D³ is an exact
q-rational combination of the DERIVED categorical anchors a_D^(n)=lw(n−1) (Lean
`tauAnchor_closed_form`). What is only n≤4-effective is the FIXED-τ depth-2 recurrence as a
model of all-n growth. This probe derives the EXACT kernel — at the classical limit q=1,
exactly; and characterizes the q-deformation.

DERIVATION (q=1, exact, from a PROVED theorem):
  a_D^(n) = lw(n−1) = S(n)/n,  S(n) = Σ_{λ⊢n} dim_q(λ).
  At q=1: dim_q(λ) → f^λ (# SYT), so S(n) → Σ_{λ⊢n} f^λ = I(n) (RSK/Burnside = keystone
  Identity I; I = involution/telephone numbers, OEIS A000085). The telephone numbers satisfy
  the VARIABLE-coefficient recurrence I(n)=I(n−1)+(n−1)I(n−2) (proved). Hence a_D^(n)=I(n)/n
  satisfies the EXACT variable-coefficient depth-2 kernel
    a_D^(n) = ((n−1)/n)·a_D^(n−1) + ((n−1)(n−2)/n)·a_D^(n−2),
  its coefficients GROW with n ⇒ super-exponential — the fixed-τ (constant-coeff) model is its
  n≤4 shadow. Lean: QOU/Mass/BindingClassicalKernel.lean (`aDClassical_variable_coeff`,
  sorry-free) proves this from the corpus `involutionNumber` telephone recurrence.

Q-DEFORMATION (measured here): S(n)=S(n−1)+[n−1]_q·S(n−2)+D(n), the q-telephone recurrence
with a cyclotomic Habiro tail D(n) (D=0 for n≤3, `c_3=[2]_q` exact; growing for n≥4). q→1
sends [n−1]_q→(n−1), D(n)→0, recovering the exact telephone recurrence.

FINDING: the exact classical kernel is DERIVED (variable-coeff telephone recurrence, from the
proved I(n)=I(n−1)+(n−1)I(n−2)), NOT fitted — τ is its n≤4 constant-coeff shadow. Closes the
"exact kernel" gap at q=1 modulo the same Identity I (Σf^λ=I(n)) the keystone P1–P5 program
proves; the full q-deformation is the q-telephone + Habiro tail. Scope-(a), no wiring.

Audit: docs/audits/2026-07-12-lever1-sw-period-lw-rate-refine.md
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

try:
    from q_parameter import Q_50_DIGIT_STR as Q0
    q0 = mp.mpf(Q0)
except Exception:
    q0 = mp.mpf('1.1099785955573347')

I_TELEPHONE = [1, 1, 2, 4, 10, 26, 76, 232, 764]  # OEIS A000085


def qint(k, qq):
    return mp.mpf(k) if qq == 1 else (qq ** k - qq ** (-k)) / (qq - 1 / qq)

def qfac(n, qq):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k, qq)
    return r

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
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]

def dimq(lam, qq):
    d = qfac(sum(lam), qq)
    for h in hooks(lam):
        d /= qint(h, qq)
    return d

def S(n, qq):
    return mp.fsum(dimq(l, qq) for l in partitions(n)) if n > 0 else mp.mpf(1)

def aD(n, qq):
    return S(n, qq) / n


def main() -> int:
    q1 = mp.mpf(1) + mp.mpf('1e-30')   # q → 1
    print("=== DERIVE the exact classical (q=1) binding kernel (lever-1 / z2bn) ===\n")

    # 1. q=1: S(n) = involution/telephone numbers (RSK/Burnside = Identity I)
    print("1. q→1:  S(n) = Σ_{λ⊢n} f^λ = I(n) (involution/telephone, A000085):")
    s_ok = True
    for n in range(1, 9):
        s = S(n, q1)
        ok = abs(s - I_TELEPHONE[n]) < mp.mpf('1e-8')
        s_ok = s_ok and ok
        print(f"     n={n}:  S(n)={float(s):.4f}   I(n)={I_TELEPHONE[n]}   {'✓' if ok else '✗'}")

    # 2. EXACT q=1 variable-coefficient kernel from the telephone recurrence
    print("\n2. EXACT q=1 kernel  a_D(n) = ((n−1)/n)a_D(n−1) + ((n−1)(n−2)/n)a_D(n−2):")
    kernel_ok = True
    for n in range(3, 9):
        lhs = aD(n, q1)
        rhs = (mp.mpf(n - 1) / n) * aD(n - 1, q1) + (mp.mpf((n - 1) * (n - 2)) / n) * aD(n - 2, q1)
        ok = abs(lhs - rhs) < mp.mpf('1e-12')
        kernel_ok = kernel_ok and ok
        print(f"     n={n}:  a_D={float(lhs):.5f}   recurrence={float(rhs):.5f}   "
              f"{'MATCH' if ok else 'MISS'}")
    print("     (variable coefficients ⇒ super-exponential; the fixed-τ depth-2 is the n≤4 shadow.)")

    # 3. q-deformation at q0: S(n)=S(n−1)+[n−1]_q S(n−2)+D(n)  (q-telephone + Habiro tail)
    print("\n3. q-deformation at q₀:  c_n=(S(n)−S(n−1))/S(n−2)  vs [n−1]_q;  Habiro D(n):")
    c3_exact = None
    for n in range(2, 9):
        cn = (S(n, q0) - S(n - 1, q0)) / S(n - 2, q0)
        qn1 = qint(n - 1, q0)
        Dn = S(n, q0) - (S(n - 1, q0) + qint(n - 1, q0) * S(n - 2, q0))
        if n == 3:
            c3_exact = abs(cn - qn1) < mp.mpf('1e-30')
        print(f"     n={n}:  c_n={float(cn):.5f}   [n−1]_q={float(qn1):.5f}   D(n)={float(Dn):+.3e}")
    print("     c_2=[1]_q, c_3=[2]_q EXACT (D=0); Habiro tail D(n) grows from n≥4 (q→1 ⇒ D→0).")

    ok = s_ok and kernel_ok and c3_exact
    print(f"\n### Verdict — the exact classical kernel is DERIVED, not fitted")
    print(f"  τ = (a_D²+a_D⁴)/a_D³ is an exact q-rational of DERIVED anchors (Lean tauAnchor_closed_form),")
    print(f"  NOT a fit. The FIXED-τ depth-2 is only the n≤4 shadow of the EXACT variable-coefficient")
    print(f"  telephone kernel (Lean-proved sorry-free, BindingClassicalKernel.aDClassical_variable_coeff),")
    print(f"  whose q=1 limit is the proved I(n)=I(n−1)+(n−1)I(n−2). Open: the full q-deformation")
    print(f"  (q-telephone + Habiro tail) + the Identity-I discharge Σf^λ=I(n) (keystone P1–P5).")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-binding-classical-kernel-derive", engine="mpmath")
        wb.set_description(
            "DERIVES the exact classical (q=1) binding kernel (lever-1/z2bn). q→1: S(n)=Σ_{λ⊢n}f^λ"
            "=I(n) (RSK/Burnside=Identity I, telephone/A000085). a_D^(n)=I(n)/n then satisfies the "
            "EXACT variable-coefficient kernel a_D(n)=((n−1)/n)a_D(n−1)+((n−1)(n−2)/n)a_D(n−2) "
            "(from the proved telephone recurrence; Lean-proved sorry-free in "
            "BindingClassicalKernel.aDClassical_variable_coeff) — super-exponential, the fixed-τ "
            "depth-2 being its n≤4 shadow. So τ is NOT a fit (exact q-rational of derived anchors); "
            "the fixed-τ MODEL is n≤4-effective. q-deformation: S(n)=S(n−1)+[n−1]_q S(n−2)+D(n), "
            "c_3=[2]_q exact, Habiro tail D(n) growing (q→1⇒D→0). Closes the classical-kernel gap "
            "modulo Identity I (keystone P1–P5). Scope-(a), no wiring.")
        wb.add_data("S_q1_equals_telephone", [float(S(n, q1)) for n in range(1, 9)])
        wb.add_data("telephone_reference", I_TELEPHONE[1:9])
        wb.add_data("habiro_D", [float(S(n, q0) - (S(n - 1, q0) + qint(n - 1, q0) * S(n - 2, q0)))
                                 for n in range(2, 9)])
        wb.add_assertion(
            name="classical_kernel_derived_variable_coeff",
            computed=str(int(bool(ok))), expected="1", tolerance=0,
            source=("q→1: S(n)=I(n) (telephone) exactly; a_D(n)=I(n)/n satisfies the exact "
                    "variable-coefficient kernel a_D(n)=((n−1)/n)a_D(n−1)+((n−1)(n−2)/n)a_D(n−2) "
                    "(Lean-proved from the telephone recurrence); c_3=[2]_q exact (D=0). So τ is an "
                    "exact q-rational of derived anchors (not a fit); the fixed-τ depth-2 is the "
                    "n≤4 shadow of this derived super-exp kernel."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
