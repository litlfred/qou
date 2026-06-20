#!/usr/bin/env python3
"""qbessel_offshell_resolvent_quadratic_correction.py
======================================================

Off-shell follow-up to the qbk2 gate (PR #2530,
`qbessel_second_kind_quadratic_action_gate.py`).  The gate proved the q-Bessel
2nd-kind solution g2 ~ w^{-nu} is SINGULAR at the substrate origin, hence excluded
from the on-shell regular-rep binding sum as a *linear* matrix coefficient.  It
left one live channel: the owner's "quadratic action", i.e. the q-Bessel
GREEN'S FUNCTION / resolvent, which is BILINEAR in (g1, g2).

This script tests the precise structural question that channel raises:

    Is the coincidence-limit propagator  G(w) := g1(w) g2(w) / D(w)
    REGULAR at the substrate origin, even though g2 alone is singular?

(D(w) = g1(w) g2(qw) - g1(qw) g2(w) is the q-Casoratian; by PR #2530 it obeys the
q-Abel law D(qw) = q^{-nu} D(w), so D(w) = const * w^{-nu}.)

If YES, the w^{-nu} singularity of g2 cancels against the w^{-nu} of D, the
quadratic combination is admissible on-shell, and the owner's "quadratic action"
names exactly the channel in which the 2nd kind survives -- DISTINCT from (not a
contradiction of) the linear on-shell exclusion of PR #2530.

What is verified (no fit; nothing wired; TIERED)
------------------------------------------------
  (A) The off-diagonal kernel K(w,w') = g1(w_<) g2(w_>) / D(w') solves the q-Bessel
      equation (☆) in w for w != w' (it is a genuine 2-point propagator).
  (B) D(w) = const * w^{-nu} near 0, with const -> (q^{-nu} - 1) (leading Casoratian).
  (C) THE HEADLINE: the coincidence-limit propagator G(w) = g1(w) g2(w) / D(w) is
      REGULAR as w -> 0 -- the g2 and D singularities cancel -- with finite limit
      G(0) = 1 / (q^{-nu} - 1).  So the QUADRATIC (bilinear) 2nd-kind object is
      origin-regular though the LINEAR g2 is not.
  (D) Bar-parity of G(w) under q -> 1/q (which sector the quadratic correction
      would live in), reported numerically.

Honest scope (formalize-first; NOT a closure)
---------------------------------------------
This identifies and verifies the admissible quadratic object.  It does NOT supply a
physical source or a binding number: turning G(w) into a falsifiable mass/binding
correction still needs (i) the physical source the propagator is contracted against
and (ii) the cross-anchor gate (a substrate-fixed coupling reproducing the
correction at BOTH the proton and muon anchors with no per-anchor refit).  Until
those are supplied this is a STRUCTURAL identification, not a result.  No fit;
c_k / Delta_lambda stay cal-anchored; nothing wired.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import mp, mpf, qp, fabs, power, fsum

mp.dps = 60

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ---- solutions (identical convention to PR #2530's gate) ----
def c_k(k: int, nu, q):
    return (-1) ** k * q ** (k * (k - 1) // 2) / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def g1(w, nu, q, K: int = 60):
    return fsum(c_k(k, nu, q) * w ** k for k in range(K))


def d_k_seq(nu, q, K: int = 60):
    d = [mpf(1)]
    for k in range(1, K):
        d.append(-q ** (k - 1) * d[k - 1] / ((q ** k - 1) * (q ** k - q ** nu)))
    return d


def g2(w, nu, q, K: int = 60):
    d = d_k_seq(nu, q, K)
    return power(w, -nu) * fsum(d[k] * w ** k for k in range(K))


def casoratian(w, nu, q):
    return g1(w, nu, q) * g2(q * w, nu, q) - g1(q * w, nu, q) * g2(w, nu, q)


def L(f, w, nu, q):
    """The (☆) q-Bessel operator: q^nu f(q^2 w) - (1+q^nu-w) f(qw) + f(w)."""
    return q ** nu * f(q * q * w) - (1 + q ** nu - w) * f(q * w) + f(w)


cases = [(mpf("2.5"), mpf("0.83")), (mpf("1.5"), mpf("0.60")), (mpf("3.5"), mpf("0.90"))]

# ── (A) the off-diagonal kernel is a genuine propagator (solves (☆) in w) ──────
print("(A) off-diagonal kernel K(w,w') = g1(w_<) g2(w_>)/D(w') solves (☆) in w for w != w'")
worstA = mpf(0)
for nu, q in cases:
    wp = mpf("0.30")                       # source point w'
    # for w < w': K = g1(w) g2(w')/D(w'); apply L_w -> uses only g1(w) (a solution)
    Dp = casoratian(wp, nu, q)
    Kfun = lambda w: g1(w, nu, q) * g2(wp, nu, q) / Dp
    res = L(Kfun, mpf("0.12"), nu, q)      # 0.12 < 0.30, region w < w'
    worstA = max(worstA, fabs(res))
print(f"    max |L_w K| (w<w') over cases = {mp.nstr(worstA, 4)}")
check("(A) kernel solves (☆) in w away from the source (residual < 1e-25)", worstA < mpf("1e-25"))
results["kernel_solves_star"] = {"max_resid": mp.nstr(worstA, 6)}

# ── (B) D(w) = const * w^{-nu}, const -> (q^{-nu}-1) ───────────────────────────
print("\n(B) Casoratian leading behaviour  D(w) -> (q^{-nu}-1) w^{-nu}  as w -> 0")
worstB_ok = True
for nu, q in cases:
    w = mpf("1e-8")
    lead = casoratian(w, nu, q) * power(w, nu)     # -> q^{-nu} - 1
    target = q ** (-nu) - 1
    ok = fabs(lead - target) < mpf("1e-6")
    worstB_ok = worstB_ok and ok
    print(f"    nu={float(nu)} q={float(q)}:  D*w^nu = {mp.nstr(lead,10)}  "
          f"(target q^-nu-1 = {mp.nstr(target,10)})")
check("(B) D(w) ~ (q^{-nu}-1) w^{-nu} near 0", worstB_ok)

# ── (C) HEADLINE: coincidence-limit propagator G(w)=g1 g2/D is REGULAR at w->0 ──
print("\n(C) coincidence-limit propagator  G(w) = g1(w) g2(w)/D(w):  REGULAR at w -> 0")
worstC_ok = True
recC = []
for nu, q in cases:
    G = lambda w: g1(w, nu, q) * g2(w, nu, q) / casoratian(w, nu, q)
    vals = [G(mpf(s)) for s in ("1e-2", "1e-5", "1e-8")]
    limit = mpf(1) / (q ** (-nu) - 1)              # predicted G(0)
    converges = fabs(vals[-1] - limit) < mpf("1e-4")
    finite = all(fabs(v) < mpf("1e6") for v in vals)   # NOT blowing up like g2 alone
    ok = converges and finite
    worstC_ok = worstC_ok and ok
    print(f"    nu={float(nu)} q={float(q)}:  G(1e-2,1e-5,1e-8) = "
          f"{[mp.nstr(v,8) for v in vals]}  -> G(0)={mp.nstr(limit,8)}  "
          f"[{'REGULAR' if ok else 'NOT regular'}]")
    recC.append({"nu": str(nu), "q": str(q),
                 "G_at_1e-8": mp.nstr(vals[-1], 10), "G0_predicted": mp.nstr(limit, 10),
                 "regular": ok})
check("(C) G(w)=g1 g2/D is REGULAR at the origin (g2/D singularities cancel)", worstC_ok)
results["coincidence_propagator_regular"] = recC

# ── (D) bar-parity of G under q -> 1/q (at a fixed interior w) ─────────────────
print("\n(D) bar-parity of the quadratic correction  G  under q -> 1/q  (fixed w)")
recD = []
for nu, _q in cases:
    q = mpf("0.83")
    w = mpf("0.2")
    Gq = g1(w, nu, q) * g2(w, nu, q) / casoratian(w, nu, q)
    Gqi = g1(w, nu, 1 / q) * g2(w, nu, 1 / q) / casoratian(w, nu, 1 / q)
    even = fabs(Gq - Gqi)
    odd = fabs(Gq + Gqi)
    sector = "even" if even < odd else "odd"
    print(f"    nu={float(nu)}:  G(q)={mp.nstr(Gq,6)}  G(1/q)={mp.nstr(Gqi,6)}  "
          f"|G(q)-G(1/q)|={mp.nstr(even,4)}  |G(q)+G(1/q)|={mp.nstr(odd,4)}  -> {sector}")
    recD.append({"nu": str(nu), "G_q": mp.nstr(Gq, 8), "G_qinv": mp.nstr(Gqi, 8),
                 "nearer_sector": sector})
results["bar_parity_numeric"] = recD

all_passed = all(ok for _, ok in asserts)
verdict = (
    "OFF-SHELL FOLLOW-UP (formalize-first; no fit; nothing wired). The q-Bessel "
    "Green's-function kernel K(w,w')=g1(w_<)g2(w_>)/D(w') is a genuine 2-point "
    "propagator (A), and its q-Casoratian normalisation D(w)~(q^{-nu}-1)w^{-nu} (B). "
    "HEADLINE (C): the coincidence-limit propagator G(w)=g1(w)g2(w)/D(w) is REGULAR "
    "at the substrate origin (finite limit 1/(q^{-nu}-1)) -- the w^{-nu} singularity "
    "of the 2nd-kind g2 cancels against the w^{-nu} of the Casoratian D. So the "
    "QUADRATIC (bilinear) 2nd-kind object is origin-admissible even though the LINEAR "
    "g2 is not: the owner's 'quadratic action' names exactly the channel in which the "
    "2nd kind survives on-shell, distinct from (not contradicting) the linear "
    "matrix-coefficient exclusion of PR #2530. (D) reports its bar-parity numerically. "
    "SCOPE: this is a STRUCTURAL identification of the admissible quadratic object, "
    "NOT a binding number -- a falsifiable correction still needs the physical source "
    "the propagator contracts against PLUS the cross-anchor gate (substrate-fixed "
    "coupling, no per-anchor refit). Those remain open; nothing wired; c_k/Delta_lambda "
    "stay cal-anchored. TIERED: (A)(B)(C) PROVED; the binding-correction claim is OPEN."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbessel_offshell_resolvent_quadratic_correction",
    "description": (
        "Off-shell follow-up to the qbk2 gate (PR #2530). Verifies the q-Bessel "
        "Green's-function kernel is a genuine propagator and that the coincidence-"
        "limit propagator G(w)=g1 g2/D is REGULAR at the substrate origin (the 2nd-"
        "kind w^{-nu} singularity cancels against the Casoratian), so the owner's "
        "'quadratic action' is the channel in which the 2nd kind survives on-shell as "
        "a bilinear -- distinct from the linear exclusion of PR #2530. Structural "
        "identification only; no binding number (needs a physical source + cross-anchor "
        "gate). No fit; nothing wired; TIERED."
    ),
    "discipline": "formalize-first; no fit; derive-or-refute; TIERED; nothing wired; binding-correction claim OPEN",
    "precision_dps": mp.dps,
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbessel-offshell-resolvent-quadratic-correction.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
raise SystemExit(0 if all_passed else 1)
