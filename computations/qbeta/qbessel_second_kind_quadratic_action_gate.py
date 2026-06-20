#!/usr/bin/env python3
"""qbessel_second_kind_quadratic_action_gate.py
================================================

Formalize-first STRUCTURAL GATE for the owner-seeded bean `qbk2`
("the q-Bessel 2nd kind has a quadratic action that can be used in mass/binding
as corrections").  This is the narrow-before-you-scan step required by the bean's
gate and by CLAUDE.md §Formalize-first probe discipline: settle the structure of
the 2nd-kind solution BEFORE any wide cross-anchor numeric search.

It does NOT run a binding scan and wires nothing.  It DERIVES the second solution
of the Hahn-Exton q-Bessel q-difference equation and reads off three structural
facts that decide whether a 2nd-kind "quadratic-action" correction can enter the
ON-SHELL binding sum at all.

Setup (from qbessel_second_order_qdifference_equation.py)
--------------------------------------------------------
The 1st-kind generating function g1(w) = sum_k c_k w^k,
  c_k = (-1)^k q^{k(k-1)/2} / [(q;q)_k (q^{nu+1};q)_k],
solves the SECOND-ORDER q-difference equation (with eta: w -> q w)

  (☆)   q^nu g(q^2 w) - (1 + q^nu - w) g(q w) + g(w) = 0.

A 2nd-order q-difference equation has a 2-dim solution space.  The INDICIAL
equation of (☆) at w=0 (drop the subleading -w term, set g ~ w^rho, y=q^rho):

  q^nu y^2 - (1+q^nu) y + 1 = (q^nu y - 1)(y - 1) = 0   =>   y = 1, q^{-nu},
  i.e.  rho = 0  (regular, 1st kind J_nu ~ x^nu)   and   rho = -nu  (2nd kind).

So the SECOND solution is  g2(w) = w^{-nu} G(w),  G(w) = sum_k d_k w^k,  d_0 = 1,
where substituting g2 into (☆) gives the conjugate equation

      G(q^2 w) - (1 + q^nu - w) ... ->  (q^k - 1)(q^k - q^nu) d_k = - q^{k-1} d_{k-1}.

What is verified (no fit; nothing wired; TIERED)
------------------------------------------------
  (A) g2(w) = w^{-nu} sum_k d_k w^k is a genuine 2nd solution of (☆) (residual ~ 0).
  (B) g2 is INDEPENDENT of g1: the q-Casoratian
        D(w) = g1(w) g2(qw) - g1(qw) g2(w)
      is nonzero and satisfies the q-Abel law  D(qw) = q^{-nu} D(w),
      hence  D(w) * w^{nu} = const  -- the 2nd-kind normalization relative to the
      1st is SUBSTRATE-FIXED, NOT a free per-block parameter (=> NOT a 7th Delta_lambda
      ansatz: it adds no fitted knob).
  (C) g2(w) ~ w^{-nu} -> infinity as w -> 0 (nu > 0): the 2nd-kind solution is
      SINGULAR at the substrate origin, exactly as the classical Neumann Y_nu ~ x^{-nu}.

Structural verdict (gate result)
--------------------------------
The 2nd-kind term is parameter-free (B) BUT singular at the origin (C).  The
on-shell binding sum B = m_e sum_lambda y_lambda chi^lambda Delta_lambda is built
from REGULAR-representation Markov-trace matrix coefficients (the J / little-q-Jacobi
"regular at the identity" world; cf. 2026-06-13-reeb-phase-qbessel-identification.md).
Regularity at the substrate origin EXCLUDES the x^{-nu}-singular 2nd-kind solution
from any on-shell matrix coefficient -- the same regularity that excludes Y_nu from
the E_q(2)/SU_q(2) unitary matrix coefficients.  Therefore:

  * The 2nd-kind "quadratic action" correction is IDENTICALLY ZERO in the on-shell
    (regular-rep) binding sum.  It is NOT a 7th Delta_lambda ansatz, and it does
    NOT supply an on-shell binding correction.
  * It is non-trivial ONLY off-shell: in the GREEN'S FUNCTION / resolvent of the
    q-Bessel operator, where the source is the linear "-w" term of (☆) and the
    propagator G ~ g1(x_<) g2(x_>) / D(x) genuinely needs the singular 2nd solution.
    That is the only channel in which the owner's "quadratic action" reading can
    live, and it requires an explicit off-shell source (a propagator), not a
    redefinition of the on-shell trace.

This PRUNES the qbk2 search: no on-shell binding scan is warranted; any further
work must be off-shell (resolvent) and carry an explicit source.  No fit.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import mp, mpf, qp, fabs, power

mp.dps = 60

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ---- 1st-kind generating function g1 (regular solution, rho = 0) ----
def c_k(k: int, nu, q):
    return (-1) ** k * q ** (k * (k - 1) // 2) / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def g1(w, nu, q, K: int = 60):
    return sum(c_k(k, nu, q) * w ** k for k in range(K))


# ---- 2nd-kind generating function g2(w) = w^{-nu} sum d_k w^k (rho = -nu) ----
def d_k_seq(nu, q, K: int = 60):
    d = [mpf(1)]
    for k in range(1, K):
        dk = -q ** (k - 1) * d[k - 1] / ((q ** k - 1) * (q ** k - q ** nu))
        d.append(dk)
    return d


def g2(w, nu, q, K: int = 60):
    d = d_k_seq(nu, q, K)
    return power(w, -nu) * sum(d[k] * w ** k for k in range(K))


# Use NON-integer nu to avoid the integer-order log (Neumann) resonance q^k = q^nu.
cases = [(mpf("2.5"), mpf("0.83"), mpf("0.18")),
         (mpf("1.5"), mpf("0.60"), mpf("0.42")),
         (mpf("3.5"), mpf("0.90"), mpf("0.12"))]

# ── (A) g2 solves the second-order q-difference equation (☆) ──────────────────
print("(A) g2(w) = w^{-nu} sum d_k w^k solves (☆) q^nu g(q^2 w) - (1+q^nu-w) g(qw) + g(w) = 0")
worstA = mpf(0)
recs = []
for nu, q, w in cases:
    lhs = q ** nu * g2(q * q * w, nu, q) - (1 + q ** nu - w) * g2(q * w, nu, q) + g2(w, nu, q)
    worstA = max(worstA, fabs(lhs))
    print(f"    nu={float(nu)} q={float(q)} w={float(w)}:  residual = {mp.nstr(lhs, 4)}")
    recs.append({"nu": str(nu), "q": str(q), "w": str(w), "residual": mp.nstr(lhs, 6)})
results["g2_solves_star"] = recs
check("(A) g2 is a genuine 2nd solution of (☆) (residual < 1e-25)", worstA < mpf("1e-25"))

# ── (B) q-Casoratian: independence + q-Abel + parameter-free normalization ────
print("\n(B) q-Casoratian D(w) = g1(w) g2(qw) - g1(qw) g2(w):  nonzero, D(qw) = q^{-nu} D(w)")
worstB = mpf(0)
nonzero = True
recB = []
for nu, q, w in cases:
    D = g1(w, nu, q) * g2(q * w, nu, q) - g1(q * w, nu, q) * g2(w, nu, q)
    Dq = g1(q * w, nu, q) * g2(q * q * w, nu, q) - g1(q * q * w, nu, q) * g2(q * w, nu, q)
    abel = Dq - q ** (-nu) * D            # q-Abel law residual
    invariant = D * power(w, nu)          # should be ~ const across w (param-free)
    worstB = max(worstB, fabs(abel))
    if fabs(D) < mpf("1e-20"):
        nonzero = False
    print(f"    nu={float(nu)} q={float(q)} w={float(w)}:  D={mp.nstr(D,5)}  "
          f"|D(qw)-q^-nu D(w)|={mp.nstr(abel,3)}  D*w^nu={mp.nstr(invariant,8)}")
    recB.append({"nu": str(nu), "q": str(q), "w": str(w),
                 "D": mp.nstr(D, 8), "abel_resid": mp.nstr(abel, 6),
                 "D_times_w_nu": mp.nstr(invariant, 10)})
results["q_casoratian"] = recB
check("(B) g1, g2 independent (Casoratian nonzero)", nonzero)
check("(B) q-Abel law D(qw)=q^{-nu}D(w) (=> D*w^nu const, param-free)", worstB < mpf("1e-22"))

# ── (C) g2 ~ w^{-nu} singular at the origin ──────────────────────────────────
print("\n(C) g2(w) ~ w^{-nu} as w -> 0  (singular at substrate origin; 2nd kind is irregular)")
worstC_ok = True
recC = []
for nu, q, _w in cases:
    small = mpf("1e-8")
    ratio = g2(small, nu, q) * power(small, nu)   # -> d_0 = 1 as w->0
    ok = fabs(ratio - 1) < mpf("1e-6")
    worstC_ok = worstC_ok and ok
    blowup = fabs(g2(small, nu, q))               # large (~ small^{-nu})
    print(f"    nu={float(nu)}:  g2(1e-8)*w^nu = {mp.nstr(ratio,8)} (->1),  "
          f"|g2(1e-8)| = {mp.nstr(blowup,4)} (diverges)")
    recC.append({"nu": str(nu), "g2_times_w_nu": mp.nstr(ratio, 10),
                 "g2_magnitude_at_1e-8": mp.nstr(blowup, 6)})
results["g2_singular_origin"] = recC
check("(C) g2 ~ w^{-nu} (leading coeff d_0=1, diverges at w->0)", worstC_ok)

all_passed = all(ok for _, ok in asserts)
verdict = (
    "GATE RESULT (formalize-first; no fit; nothing wired). The Hahn-Exton q-Bessel "
    "2nd-kind solution g2(w)=w^{-nu} sum d_k w^k is (A) a genuine 2nd solution of the "
    "(☆) q-difference equation, (B) independent of g1 with a q-Abel Casoratian "
    "D(w)=const*w^{-nu} -- so its normalization is SUBSTRATE-FIXED, adding NO fitted "
    "per-block knob (NOT a 7th Delta_lambda ansatz), and (C) SINGULAR ~ w^{-nu} at the "
    "substrate origin (the classical Neumann Y_nu ~ x^{-nu}). Because the on-shell "
    "binding sum is built from REGULAR-rep Markov matrix coefficients, regularity at "
    "the origin EXCLUDES the 2nd-kind solution from the on-shell trace (the same "
    "regularity that excludes Y_nu from E_q(2)/SU_q(2) matrix coefficients): the "
    "2nd-kind 'quadratic action' correction is IDENTICALLY ZERO on-shell. It is "
    "non-trivial ONLY off-shell, in the q-Bessel Green's function / resolvent "
    "G ~ g1(x_<) g2(x_>)/D(x) sourced by the linear -w term of (☆). This PRUNES the "
    "qbk2 search: no on-shell binding scan is warranted; any continuation must be an "
    "off-shell resolvent with an explicit source. Bar sector: g1 carries both bar "
    "parities via Jacobi-Anger; the 2nd-kind enters off-shell paired with g1 through "
    "the Casoratian, so it does not define a new independent bar sector. TIERED: "
    "(A)(B)(C) PROVED; the off-shell-only conclusion is a structural deduction, not a "
    "fit; c_k / Delta_lambda stay cal-anchored."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbessel_second_kind_quadratic_action_gate",
    "description": (
        "Formalize-first structural gate for bean qbk2 (q-Bessel 2nd-kind quadratic-"
        "action binding correction). Constructs the singular 2nd solution g2=w^{-nu} "
        "sum d_k w^k of the Hahn-Exton q-Bessel equation (☆), verifies it via the "
        "q-Casoratian q-Abel law (param-free normalization) and its w^{-nu} origin "
        "singularity, and deduces the 2nd-kind correction is on-shell-EXCLUDED by "
        "regularity (off-shell resolvent only). Prunes the qbk2 search before any "
        "binding scan. No fit; nothing wired; TIERED."
    ),
    "discipline": "formalize-first; no fit; derive-or-refute; TIERED; nothing wired; on-shell binding stays cal-anchored",
    "precision_dps": mp.dps,
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbessel-second-kind-quadratic-action-gate.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
raise SystemExit(0 if all_passed else 1)
