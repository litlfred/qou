#!/usr/bin/env python3
"""molien_wenzl_weight_identity_probe.py — the FULL n=4 Jones-Markov weight
identity: the Molien-predicted weights equal the INDEPENDENT Wenzl Schur-principal
weights as rational functions of (q,z). (bean qou-3quc / qou-idwf.)

Closes the scope gap flagged in MolienJonesMarkovN4.lean: the n=4 structural Lean
(normalisation + D-cap) did not by itself prove y_lambda^Molien = y_lambda^JM as
rational functions; that needs an INDEPENDENT general-z H_4 weight. This probe
supplies it via Wenzl's closed form and checks equality symbolically.

## The two independently-computed weight families (share no inputs)

1. Molien:  y_lambda = M_nu(u=q^2, t=qz/(q^2-qz-1)) * (1+qz-q^2)^(n-1)   [companion probe]
2. Wenzl (Schur-principal specialization), NO reference to the Molien series:
     Q=q^2, R=Q^r=qz/(1-q^2+qz),
     s_lambda = Q^{n(lambda)} * prod_{x}(1 - R Q^{c(x)}) / prod_{x}(1 - Q^{h(x)}),
     Z = sum_mu f^mu s_mu,   y_lambda = s_lambda / Z.

Verified EQUAL as rational functions of (q,z) at n=3 AND n=4 (exact sympy).
This is exactly the independent H_4 weight the Lean full-identity theorem
(n4_full_identity in MolienJonesMarkovN4.lean) certifies via ratio identities.

Exact ℚ(q,z); no float. Nothing wired.

-- Ref: [webster-williamson-2014-markov] arXiv:0911.4494
-- Ref: computations/markov/markov_weights_symbolic.py (Wenzl schur_principal machinery)
-- Ref: content/.../QOU/QBeta/MolienJonesMarkovN4.lean (n4_full_identity)
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

q, z, u, t = sp.symbols("q z u t")


def partitions_of(n):
    def h(n, mx):
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for r in h(n - k, k):
                yield (k,) + r
    return list(h(n, n))


def hooks_contents(lam):
    hs, cs = [], []
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def n_stat(lam):
    return sum(i * l for i, l in enumerate(lam))


def f_lambda(lam, n):
    hs, _ = hooks_contents(lam)
    p = 1
    for hh in hs:
        p *= hh
    return sp.factorial(n) // p


def wenzl_weights(n):
    """Independent Wenzl Schur-principal weights y_lambda(q,z), general z."""
    Q = q ** 2
    R = q * z / (1 - Q + q * z)                      # Q^r symbolic in (q,z)
    shapes = partitions_of(n)
    s = {}
    for lam in shapes:
        hs, cs = hooks_contents(lam)
        num = sp.Integer(1)
        den = sp.Integer(1)
        for hh, c in zip(hs, cs):
            num *= (1 - R * Q ** c)
            den *= (1 - Q ** hh)
        s[lam] = sp.cancel(Q ** n_stat(lam) * num / den)
    Z = sp.cancel(sum(s[lam] * f_lambda(lam, n) for lam in shapes))
    return {lam: sp.cancel(s[lam] / Z) for lam in shapes}


def s3_molien():
    classes = [(1, 1, 1, 2, (1 + t) ** 2, (1 - u) ** 2),
               (3, 1, -1, 0, (1 + t) * (1 - t), (1 - u) * (1 + u)),
               (2, 1, 1, -1, 1 - t + t ** 2, 1 + u + u ** 2)]

    def M(idx):
        return sp.simplify(sum(c[0] * c[1 + idx] * c[4] / c[5] for c in classes) / 6)
    return {(3,): M(0), (1, 1, 1): M(1), (2, 1): M(2)}


def s4_molien():
    # REAL determinant forms (no omega/i) -> clean symbolic subs.
    cls = [(1, (1 + t) ** 3, (1 - u) ** 3),
           (6, (1 + t) ** 2 * (1 - t), (1 - u) ** 2 * (1 + u)),
           (3, (1 + t) * (1 - t) ** 2, (1 - u) * (1 + u) ** 2),
           (8, (1 + t) * (1 - t + t ** 2), (1 - u) * (1 + u + u ** 2)),
           (6, (1 - t) * (1 + t ** 2), (1 + u) * (1 + u ** 2))]
    chars = {(4,): [1, 1, 1, 1, 1], (3, 1): [3, 1, -1, 0, -1],
             (2, 2): [2, 0, 2, -1, 0], (2, 1, 1): [3, -1, -1, 0, 1],
             (1, 1, 1, 1): [1, -1, 1, 1, -1]}

    def M(lam):
        return sp.simplify(sum(cls[k][0] * chars[lam][k] * cls[k][1] / cls[k][2]
                               for k in range(len(cls))) / 24)
    return {lam: M(lam) for lam in chars}


def molien_weights(n, Ms):
    W = q ** 2 - q * z - 1
    Zn = (1 + q * z - q ** 2) ** (n - 1)
    return {lam: sp.cancel(sp.simplify(Ms[lam].subs({u: q ** 2, t: q * z / W}) * Zn))
            for lam in Ms}


def main() -> int:
    ok_all = True
    results = {}
    for n, Msf in [(3, s3_molien), (4, s4_molien)]:
        yw = wenzl_weights(n)
        ym = molien_weights(n, Msf())
        n_ok = True
        for lam in yw:
            eq = sp.simplify(yw[lam] - ym[lam]) == 0
            n_ok = n_ok and eq
            print(f"  n={n} {str(lam):>12}: Wenzl == Molien ? {'YES' if eq else 'NO'}")
        norm = sp.simplify(sum(f_lambda(lam, n) * yw[lam] for lam in yw))
        norm_ok = (sp.simplify(norm - 1) == 0)
        print(f"  n={n} Wenzl normalisation Sum f^lam y_lam = {norm}  [{'PASS' if norm_ok else 'FAIL'}]")
        results[n] = n_ok and norm_ok
        ok_all = ok_all and results[n]
    print(f"\nVERDICT: Molien weights == independent Wenzl weights as rational "
          f"functions of (q,z): {'CONFIRMED at n=3 AND n=4' if ok_all else 'FAILED'}. "
          f"This is the independent H_n weight the Lean n4_full_identity certifies.")

    try:
        from witness_base import WitnessBuilder
    except Exception:
        return 0 if ok_all else 1
    w = WitnessBuilder("molien-wenzl-weight-identity", engine="sympy")
    w.set_description(
        "bean qou-3quc/qou-idwf: the Molien-predicted Jones-Markov weights EQUAL the "
        "INDEPENDENT Wenzl Schur-principal weights y_lambda = s_lambda/Z as rational "
        "functions of (q,z), verified exact at n=3 and n=4. Supplies the independent "
        "general-z H_4 weight the n=4 full-identity Lean (n4_full_identity) needed; "
        "the two families share no inputs. Nothing wired."
    )
    w.set_audit_only("docs/audits/2026-08-29-molien-jones-markov-n3-identification.md")
    w.add_data("wenzl_formula", "y_lambda = s_lambda/Z, s_lambda = Q^n(lam) prod(1-R Q^c)/prod(1-Q^h), R=qz/(1-q^2+qz)")
    w.add_data("free_parameters", 0)
    w.add_assertion("n3_wenzl_eq_molien", 1 if results[3] else 0, 1,
                    source="Wenzl weights == Molien weights, exact Q(q,z), n=3")
    w.add_assertion("n4_wenzl_eq_molien", 1 if results[4] else 0, 1,
                    source="Wenzl weights == Molien weights, exact Q(q,z), n=4")
    # q0Anchor DECLARED, not defaulted. `resolve_q0_anchor` returns "proton" for
    # any stem absent from the manifest -- the runtime DEFAULT, not evidence -- so
    # an undeclared witness goes out asserting a pin it never used, and
    # `q0_anchor_ratchet --strict` counts it as unstamped. Declared 2026-08-29,
    # bean `qou-6u53`, on an import-cone trace plus the absence of any q_0 value
    # in the payload.
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-independent: q_0 is unreachable from this producer's entire import "
            "cone. The Wenzl weight identity is an algebraic identity in the formal "
            "parameter, not a substrate evaluation."
        ),
    })
    print(f"witness -> {out}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
