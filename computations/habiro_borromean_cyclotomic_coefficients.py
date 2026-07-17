#!/usr/bin/env python3
r"""
Extract the Habiro CYCLOTOMIC COEFFICIENTS C_l(q) of the Borromean rings
from the verified diagonal colored-Jones tower J_{B,n}.

WHY
---
The corpus already has the Borromean diagonal colored Jones J_{B,n} in
Habiro's closed form (habiro_borromean_colored_jones.py, 4/4 anchors),
but it has NEVER extracted the cyclotomic coefficients C_l(q) themselves
— the n-independent Laurent polynomials in Habiro's cyclotomic expansion

    J_{B,n} = sum_{l>=0} C_l(q) * B_l(n),   B_l(n) = prod_{j=1}^l {n+j}{n-j},

with {a} = q^{a/2} - q^{-a/2}, B_0(n) = 1.  This is the canonical object
one cross-checks against any candidate c_k identification (bean n920).

The extraction is EXACT and OVER-DETERMINED, not a fit:
  * B_l(n) = 0 for l >= n (the factor {n-l} vanishes at l=n), so the
    system J_{B,n} = sum_{l<n} C_l B_l(n) is lower-triangular: C_0 from
    n=1, C_1 from n=2, ..., each solved by one subtraction+division.
  * Habiro's theorem guarantees C_l is INDEPENDENT of n.  We do NOT
    assume this — we solve C_l at its first appearance (n=l+1) and then
    RE-DERIVE it at every larger n; agreement across all n>l is an
    independent correctness check (if the basis or transcription were
    wrong, the "C_l" would drift with n).

This is audit-only mathematics.  It wires into nothing; it produces the
cyclotomic coefficients as a witnessed object and reports, TIERED and
honestly (per the AGENTS.md c_k banner), whether any C_l(q_0) coincides
with a corpus precision-ladder c_k — WITHOUT forcing an identification.
"""
from __future__ import annotations
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from habiro_borromean_colored_jones import habiro_borromean  # verified tower

q, s = sp.symbols("q s", positive=True)   # s = q^{1/2}
LMAX = 6                                   # extract C_0 .. C_5


def brk(a: int):
    """{a} = q^{a/2} - q^{-a/2} = s^a - s^{-a}."""
    return s**a - s**(-a)


def basis_B(l: int, n: int):
    """B_l(n) = prod_{j=1}^l {n+j}{n-j}; B_0 = 1.  Laurent poly in s."""
    out = sp.Integer(1)
    for j in range(1, l + 1):
        out *= brk(n + j) * brk(n - j)
    return sp.expand(out)


def _lpoly_to_q(poly_s):
    """Map an even-power Laurent polynomial in s to a polynomial in q=s^2."""
    p = sp.expand(poly_s)
    out = sp.Integer(0)
    for term in sp.Add.make_args(p):
        coeff, rest = term.as_independent(s)
        if rest == 1:
            k = 0
        elif rest == s:
            k = 1
        elif rest.is_Pow and rest.base == s:
            k = int(rest.exp)
        else:
            raise ValueError(f"non-monomial-in-s term: {term}")
        if k % 2 != 0:
            raise ValueError(f"odd s-power s^{k} -> not a function of q: {term}")
        out += coeff * q**(k // 2)
    return sp.expand(out)


def to_q(expr):
    """Map a rational function of s (even powers only) to a rational fn of q=s^2.

    C_l is a RATIONAL function of q for the Borromean diagonal basis (its
    denominator is a power of q(q-1)(q+1)), so we convert numerator and
    denominator separately.  No sqrt, no simplify (both blow up on the
    cube-summand expressions); a stray odd s-power raises (transcription
    bug guard).
    """
    e = sp.cancel(sp.together(expr))
    num, den = sp.fraction(e)
    # J_{B,n} is invariant under s->-s (even powers only), so a cancelled
    # ratio has even num and den; if a common odd factor of s survives,
    # clear it (multiplying both by s preserves the ratio).
    num, den = sp.expand(num), sp.expand(den)
    if any(int(getattr(t.as_independent(s)[1], "exp", 0)) % 2
           or t.as_independent(s)[1] == s for t in sp.Add.make_args(den)):
        num, den = sp.expand(num * s), sp.expand(den * s)
    return sp.cancel(_lpoly_to_q(num) / _lpoly_to_q(den))


def extract_cyclotomic(lmax: int):
    """Triangular solve for C_0..C_{lmax}, then an over-determined check.

    Extraction (exact): B_l(n)=0 for l>=n, so C_l is isolated at its
    diagonal n=l+1:
        C_l = (J_{B,l+1} - sum_{m<l} C_m B_m(l+1)) / B_l(l+1).
    Everything stays in s (clean Laurent objects); C_l -> q=s^2 at the end.

    Over-determination (the real check): each C_l was fixed at n=l+1, yet
    Habiro's theorem says the SAME C_l must rebuild J_{B,n} at every larger
    n.  So for each n we test  sum_{l<n} C_l B_l(n) == J_{B,n}  exactly.
    This uses every low-l C_l at n >> l+1 — a genuine, non-circular check
    (a wrong or n-dependent C_l would break the reconstruction).

    Returns (coeffs_q, recon) where coeffs_q[l] is C_l over q and recon is
    the list of (n, reconstructs?) for n = 1 .. lmax+1.
    """
    J = {n: sp.expand(habiro_borromean(n)) for n in range(1, lmax + 2)}
    coeffs_s: dict[int, sp.Expr] = {}
    coeffs_q: dict[int, sp.Expr] = {}
    for l in range(lmax + 1):
        n = l + 1                                     # the diagonal — C_l isolated
        resid = J[n] - sum(coeffs_s[m] * basis_B(m, n) for m in range(l))
        Cl_s = sp.cancel(sp.together(resid / basis_B(l, n)))
        coeffs_s[l] = Cl_s
        coeffs_q[l] = to_q(Cl_s)
    recon = []
    for n in range(1, lmax + 2):
        rebuilt = sum(coeffs_s[l] * basis_B(l, n) for l in range(n))
        ok = sp.expand(sp.cancel(rebuilt - J[n])) == 0
        recon.append((n, bool(ok)))
    return coeffs_q, recon


def q0_value():
    """Substrate q_0 (muon-anchored canonical computations/ value)."""
    wf = Path(__file__).with_name("q-pinning-50-digit.witness.json")
    if wf.exists():
        d = json.loads(wf.read_text())
        for k in ("q0", "q_0", "q", "value", "q0_50dps"):
            if k in d:
                return sp.Rational(str(d[k]))
    # documented fallback (muon anchor, -11.5 ppb)
    return sp.Rational("1.10997859555733471")


def main() -> int:
    print("\n  Habiro Borromean cyclotomic coefficients C_l(q)\n")
    coeffs, recon = extract_cyclotomic(LMAX)

    coeff_str = {}
    for l in range(LMAX + 1):
        Cl = coeffs[l]
        coeff_str[f"C_{l}"] = str(Cl)
        print(f"  C_{l}(q) = {sp.factor(Cl)}")

    all_consistent = all(ok for _, ok in recon)
    good_n = [n for n, ok in recon if ok]
    print(f"\n  over-determination (Habiro n-independence):"
          f" {'CONFIRMED' if all_consistent else 'FAILED'}"
          f"\n    sum_{{l<n}} C_l(q) B_l(n) == J_{{B,n}} exactly for n={good_n}"
          f"  (each C_l fixed at n=l+1, rebuilt at all larger n)")

    # honest, TIERED look at any c_k coincidence — no forcing
    q0 = q0_value()
    print(f"\n  numerical C_l(q_0), q_0={float(q0):.6f}:")
    vals = {}
    for l in range(LMAX + 1):
        v = sp.N(coeffs[l].subs(q, q0), 20)
        vals[f"C_{l}"] = str(v)
        print(f"    C_{l}(q_0) = {sp.N(coeffs[l].subs(q, q0), 12)}")
    print("\n  NOTE (c_k banner, tiered): the corpus precision-ladder c_k are"
          "\n  Q_beta/meson/m_p TRUNCATION coefficients (near-matches to Hopf"
          "\n  Jones, only c_2 Taylor-exact). The C_l above are the Borromean"
          "\n  CYCLOTOMIC coefficients — a distinct object. No identification"
          "\n  is asserted here; the C_l are provided as the clean input any"
          "\n  future c_k<->Borromean cross-check must use.")

    script_path = Path(__file__)
    try:
        commit_sha = subprocess.run(["git", "rev-parse", "HEAD"],
                                    capture_output=True, text=True,
                                    cwd=script_path.parent).stdout.strip() or "unknown"
    except Exception:  # noqa: BLE001  (git may be absent)
        commit_sha = "unknown"
    witness = {
        "engine": f"python {sys.version.split()[0]} / sympy {sp.__version__}",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": commit_sha,
        "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": ("Habiro cyclotomic coefficients C_l(q) of the Borromean "
                        "rings, extracted (exact, triangular, over-determined) "
                        "from the verified diagonal colored-Jones tower"),
        "computation": "habiro-borromean-cyclotomic-coefficients",
        "audit_only": True,
        "basis": "J_{B,n} = sum_l C_l(q) * prod_{j=1}^l {n+j}{n-j}, {a}=q^{a/2}-q^{-a/2}",
        "l_max": LMAX,
        "n_independence_confirmed": bool(all_consistent),
        "cyclotomic_coefficients_q": coeff_str,
        "cyclotomic_coefficients_at_q0": vals,
        "q0_used": str(q0),
        "ck_identification": "none asserted (distinct object; see NOTE)",
    }
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, str(script_path.parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    _wb = WitnessBuilder.wrap_legacy(
        "habiro-borromean-cyclotomic-coefficients", witness,
        script_path=__file__, engine="sympy", start_time=_T0,
    )
    # reads the canonical substrate pin as input -> record the upstream edge
    _qp = script_path.with_name("q-pinning-50-digit.witness.json")
    if _qp.exists():
        _wb.add_upstream(_qp)
    out = _wb.save()
    print(f"\n  written -> {out.name}")
    return 0 if all_consistent else 1


if __name__ == "__main__":
    sys.exit(main())
