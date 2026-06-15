#!/usr/bin/env python3
# polynomial_q_not_applicable: all identities are EXACT in the fraction field
# Q(q) of the generic Hecke parameter (sympy symbolic, pre-archimedean); the
# only archimedean step is the sign evaluation -h/q < 0 at the substrate q_0.
"""
RT 2-loop plan sub-claim C2.3 — the Schwinger-sign core (no pi).

Scope: PR #1495 `docs/coordination/2026-05-30-alpha-em-4pi-rt-2loop-derivation-
plan.md`, Identity 2 (F_2 = -h^2 alpha_EM), sub-claim:

  (C2.3) Sign of -h^2 alpha follows from the Hecke quadratic identity in the
         antisymmetric (singlet) channel.

WHAT THIS PROBE VERIFIES (exact, in H_2(q) = R[sigma]/(sigma^2 - h sigma - 1),
Hecke-Skein convention CLAUDE.md section 7a: eigenvalues q and -q^{-1}).

  1. The Bezout singlet projector e_- = (q - sigma)/(q + q^{-1}) is idempotent
     and sigma e_- = -q^{-1} e_-  (the singlet channel carries the UNIQUE
     NEGATIVE braiding eigenvalue; thm:em-spectral-completeness statement 3).
  2. Skein: sigma - sigma^{-1} = h holds identically in H_2(q) — each
     vertex-pair "interaction insertion" carries one factor h, two carry h^2
     (the C2.1 h^2 bookkeeping is channel-independent).
  3. The connected double-crossing insertion (sigma^2 - 1) acts on the singlet
     channel as
            (sigma^2 - 1) e_-  =  -(h/q) e_-,
     i.e. the interaction part of the 2-vertex insertion is NEGATIVE-definite
     on e_- for real q > 1 (archimedean leg at q_0): the minus sign of the
     Schwinger term is forced by the singlet eigenvalue, not chosen.
  4. Contrast: on the symmetric channel (sigma^2 - 1) e_+ = +(h q) e_+ —
     positive.  The sign asymmetry IS the e_+/e_- split.

WHAT REMAINS OPEN (not claimed).
  The full Identity-2 normalisation -h^2 alpha_EM multiplying [2]_q/(8 pi)
  requires the RT shadow-world measure on the zero-mode subspace (C1.3) and
  the two charge insertions (alpha each); those stay on PR #1495's track.
  This probe closes only the SIGN+h-power bookkeeping core (C2.3 + the h^2 of
  C2.1 at the channel-algebra level).

Refs: thm:em-spectral-completeness (e_+/e_- split, negative singlet
eigenvalue); cor:gauge-coupling-uniqueness (e_- is THE coupling channel);
prop:alpha-em-habiro-bar-involution (H = [2]_q (1 - h^2 alpha));
PR #2114 (Identity-1 denominator 8 pi = pi b_1 grounded on b_1 = 8).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import sympy as sp

try:
    import mpmath as mp
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785827513808075916690956107688798744991218736"


def reduce_word(poly: sp.Poly, q: sp.Symbol, s: sp.Symbol) -> sp.Expr:
    """Reduce an element of R[s] modulo the Hecke quadratic s^2 = h s + 1."""
    h = q - 1 / q
    expr = poly.as_expr()
    # iterate: replace s**k for k >= 2 until degree <= 1
    while sp.degree(sp.Poly(sp.expand(expr), s)) >= 2:
        p = sp.Poly(sp.expand(expr), s)
        terms = []
        for (k,), c in p.terms():
            if k >= 2:
                terms.append(sp.expand(c * s ** (k - 2) * (h * s + 1)))
            else:
                terms.append(c * s ** k)
        expr = sp.expand(sum(terms))
    return sp.simplify(expr)


def main() -> None:
    w = WitnessBuilder("rt-c23-singlet-sign-core", engine="python")
    q, s = sp.symbols("q s", positive=True)  # s = sigma (abstract generator)
    h = q - 1 / q

    # Singlet / symmetric Bezout projectors (eigenvalues q, -q^{-1}; section 7a)
    e_minus = (q - s) / (q + 1 / q)
    e_plus = 1 - e_minus

    def hecke_eq(a, b) -> bool:
        """a == b in H_2(q) (reduce mod quadratic, then simplify over Q(q))."""
        diff = sp.together(a - b)
        num, _den = sp.fraction(diff)
        red = reduce_word(sp.Poly(sp.expand(num), s), q, s)
        return sp.simplify(red) == 0

    # 1. idempotency + eigenvalue on the singlet channel
    idem_ok = hecke_eq(sp.expand(e_minus * e_minus), e_minus)
    eig_ok = hecke_eq(sp.expand(s * e_minus), sp.expand(-(1 / q) * e_minus))

    # 2. Skein sigma - sigma^{-1} = h  (sigma^{-1} = sigma - h from the quadratic)
    s_inv = s - h
    skein_ok = hecke_eq(sp.expand(s * s_inv), sp.Integer(1)) and hecke_eq(
        sp.expand(s - s_inv), h
    )

    # 3. connected double-crossing insertion on each channel
    minus_ok = hecke_eq(sp.expand((s * s - 1) * e_minus),
                        sp.expand(-(h / q) * e_minus))
    plus_ok = hecke_eq(sp.expand((s * s - 1) * e_plus),
                       sp.expand((h * q) * e_plus))

    # 4. archimedean sign leg at q_0
    q0 = mp.mpf(Q0) if HAVE_MP else float(Q0)
    h0 = q0 - 1 / q0
    singlet_coeff = -(h0 / q0)
    sign_ok = singlet_coeff < 0

    print("=" * 74)
    print("RT 2-loop C2.3 — Schwinger-sign core on the singlet channel (exact)")
    print("=" * 74)
    print(f"  H_2(q) convention (7a): sigma^2 = h sigma + 1, eigenvalues q, -1/q")
    print(f"  e_- idempotent:                      {idem_ok}")
    print(f"  sigma e_- = -q^-1 e_- (neg. root):   {eig_ok}")
    print(f"  Skein sigma - sigma^-1 = h:          {skein_ok}")
    print(f"  (sigma^2 - 1) e_- = -(h/q) e_-:      {minus_ok}   <-- the C2.3 sign")
    print(f"  (sigma^2 - 1) e_+ = +(h q) e_+:      {plus_ok}")
    print(f"  at q0: -(h/q) = "
          f"{mp.nstr(mp.mpf(singlet_coeff), 12) if HAVE_MP else singlet_coeff}"
          f"  (< 0: {sign_ok})")
    print()
    print("  Open (PR #1495 track): the RT zero-mode measure (C1.3) + the two")
    print("  charge insertions that normalise this core to -h^2 alpha [2]_q/(8 pi).")

    w.set_description(
        "RT 2-loop derivation plan (PR #1495) sub-claim C2.3: the minus sign of "
        "the Schwinger term -h^2 alpha is FORCED by the Hecke quadratic in the "
        "antisymmetric/singlet channel.  Exact identities in H_2(q) = "
        "R[sigma]/(sigma^2 - h sigma - 1) (section 7a convention, eigenvalues "
        "q and -q^{-1}): the Bezout singlet projector e_- = (q - sigma)/(q + "
        "q^{-1}) is idempotent with sigma e_- = -q^{-1} e_- (the unique "
        "NEGATIVE braiding root, thm:em-spectral-completeness); Skein sigma - "
        "sigma^{-1} = h gives one h per vertex-pair (C2.1 bookkeeping); the "
        "connected double-crossing insertion acts as (sigma^2 - 1) e_- = "
        "-(h/q) e_- (negative for real q > 1) vs +(h q) on e_+.  The sign "
        "asymmetry IS the e_+/e_- split; no choice is made.  The full "
        "-h^2 alpha [2]_q/(8 pi) normalisation (RT zero-mode measure C1.3 + "
        "two charge insertions) remains open on PR #1495's track."
    )
    w.set_content_block("thm:em-spectral-completeness")
    w.add_data("q0", str(q0))
    w.add_data("singlet_double_crossing_coeff_at_q0", str(singlet_coeff))
    w.add_data("symbolic", {
        "e_minus": "(q - sigma)/(q + q^{-1})",
        "singlet_eigenvalue": "-q^{-1}",
        "double_crossing_on_e_minus": "-(h/q)",
        "double_crossing_on_e_plus": "+(h q)",
        "skein": "sigma - sigma^{-1} = h",
    })
    w.add_assertion(
        "e_- is idempotent in H_2(q) (exact, generic q)",
        computed=bool(idem_ok), expected=True,
        source="Bezout split of the Hecke quadratic (thm:em-spectral-completeness)",
    )
    w.add_assertion(
        "sigma e_- = -q^{-1} e_- — singlet channel carries the unique negative root",
        computed=bool(eig_ok), expected=True,
        source="section 7a eigenvalues (q, -q^{-1})",
    )
    w.add_assertion(
        "Skein sigma - sigma^{-1} = h (one h per vertex-pair; C2.1 bookkeeping)",
        computed=bool(skein_ok), expected=True,
        source="Hecke quadratic, exact",
    )
    w.add_assertion(
        "C2.3 sign core: (sigma^2 - 1) e_- = -(h/q) e_- (exact)",
        computed=bool(minus_ok), expected=True,
        source="reduction mod sigma^2 = h sigma + 1",
    )
    w.add_assertion(
        "symmetric contrast: (sigma^2 - 1) e_+ = +(h q) e_+ (exact)",
        computed=bool(plus_ok), expected=True,
        source="reduction mod sigma^2 = h sigma + 1",
    )
    w.add_assertion(
        "archimedean leg: -(h/q) < 0 at substrate q_0",
        computed=bool(sign_ok), expected=True,
        source="q_0 > 1 real",
    )
    w.add_data(
        "finding",
        "C2.3 closed at the channel-algebra level: the Schwinger minus sign is "
        "the singlet channel's negative braiding root -q^{-1}; the connected "
        "2-vertex insertion is -(h/q) on e_- vs +(h q) on e_+, and Skein gives "
        "the h-per-vertex-pair bookkeeping of C2.1.  Remaining for Identity 2: "
        "the RT zero-mode measure (C1.3) and the two alpha charge insertions."
    )
    w.save()
    print("\nDone. Witness saved (rt-c23-singlet-sign-core).")


if __name__ == "__main__":
    main()
