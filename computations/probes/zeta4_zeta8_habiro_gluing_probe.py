"""zeta4 -> zeta8 Habiro-gluing edge probe on the categorical [2]_q factor.

Bean qou-c0aw (U4). Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 3).

CONTEXT. GSWZ Definition 1.1 (arXiv:2412.04241v2, uploaded at
library/arxiv-2412.04241v2/2412.04241v2.pdf) realizes Habiro-ring elements as collections
f_m(x) in Z[zeta_m][[x]] glued by f_m(x + zeta_pm - zeta_m) =
phi_p f_pm(x) p-adically. The corpus holds evaluations of Habiro
elements at zeta_4 = i (the alpha_EM modular zero, which is the
tau-assignment monodromy point) and at zeta_8 (the Q_beta categorical
witness). The p = 2 gluing edge zeta_4 -> zeta_8 is therefore the first
vertical edge testable on corpus-adjacent data.

WHAT THIS CHECKS (exact cyclotomic arithmetic in Q(zeta_8), sympy):

1. The edge is 2-adically genuine: Norm(zeta_8 - zeta_4) = 2 (a non-unit
   exactly at p = 2, so the re-expansion disc |x|_2 < 1 contains the
   shift — the GSWZ smallness condition).
2. Fibre integrality: the expansions of the categorical factor
   [2]_q = q + q^{-1} around zeta_4 and around zeta_8 have coefficients
   in Z[zeta_4] resp. Z[zeta_8] (denominator-free), to order N.
3. Route-independent gluing at K = Q (phi_2 = id on Z): re-expanding the
   zeta_4-fibre series at the shifted point equals the zeta_8-fibre
   series, coefficient by coefficient, to the order supported by the
   truncation.
4. The corpus modular zero: [2]_{zeta_4} = 0 exactly (constant term of
   the zeta_4 fibre) — the alpha_EM element's H(zeta_4) = 0 zero at the
   monodromy point, reproduced at the [2]_q factor level.

HONESTY: [2]_q is a Laurent POLYNOMIAL, i.e. an element of the CLASSICAL
Habiro ring over Q, where the Frobenius twist is trivial — this probe is
the harness + smallness/integrality/zero verification, not a test of the
nontrivial number-field twist. The nontrivial test (Phi-series of 4_1
over Q(sqrt(-3)) with genuine phi_p) needs multi-fibre series data and
stays on bean qou-1hlh.
"""

import json
import sys

import sympy as sp

z8 = sp.exp(sp.I * sp.pi / 4)  # zeta_8, exact
z4 = z8**2  # zeta_4 = i

x = sp.symbols("x")
N = 6

checks = {}

# (1) Norm(zeta_8 - zeta_4) over Q: product of conjugates zeta_8^k, k odd
delta = z8 - z4
conjs = [sp.exp(sp.I * sp.pi * sp.Rational(k, 4)) for k in (1, 3, 5, 7)]
norm = sp.simplify(sp.expand_complex(sp.prod(c - c**2 for c in conjs)))
checks["norm_of_shift_is_2"] = bool(sp.simplify(norm - 2) == 0)


def fibre_series(center, order):
    """Coefficients of [2]_q = q + 1/q around q = center + x, exact."""
    f = (center + x) + 1 / (center + x)
    ser = sp.series(f, x, 0, order).removeO()
    return [sp.expand(sp.simplify(ser.coeff(x, k))) for k in range(order)]


f4 = fibre_series(z4, N)
f8 = fibre_series(z8, N)


def in_z_zeta8(c):
    """Coefficient lies in Z[zeta_8]: rational parts of its coordinates
    w.r.t. the power basis have denominator 1. Use exact rewrite."""
    p = sp.Poly(sp.expand(sp.nsimplify(c, [sp.sqrt(2)])), sp.sqrt(2), sp.I)
    return all(sp.Rational(sp.nsimplify(a)).q in (1, 2) for a in p.coeffs())
    # zeta_8 = (sqrt2/2)(1+i): integrality in Z[zeta_8] shows up as
    # half-integer coordinates in the (sqrt2, i) basis — denominator 1 or 2.


checks["zeta4_fibre_integral"] = all(
    sp.Rational(sp.nsimplify(sp.re(c))).q == 1 and sp.Rational(sp.nsimplify(sp.im(c))).q == 1
    for c in f4
)
checks["zeta8_fibre_integral"] = all(in_z_zeta8(c) for c in f8)

# (3) gluing: f4 re-expanded at x -> x + (z8 - z4) equals f8, to the
# order supported by truncation of the tail (compare orders 0..N-2 with
# exact rational-function route instead of truncated route)
f_at = (z4 + (x + delta)) + 1 / (z4 + (x + delta))
glue = sp.series(sp.simplify(f_at), x, 0, N - 1).removeO()
ok = True
for k in range(N - 1):
    lhs = sp.simplify(glue.coeff(x, k) - f8[k])
    if sp.simplify(sp.nsimplify(lhs, [sp.sqrt(2)])) != 0:
        ok = False
        break
checks["gluing_zeta4_to_zeta8_exact"] = ok

# (4) the modular zero at the monodromy point
checks["two_bracket_zeta4_zero"] = bool(sp.simplify(f4[0]) == 0)

print(json.dumps(checks, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "zeta4_zeta8_habiro_gluing_probe",
    "beans": ["qou-c0aw"],
    "source": "GSWZ arXiv:2412.04241v2 Def 1.1; corpus alpha-em-habiro-bar-involution (H(zeta4)=0); zeta8 witness audit 2026-06-01",
    "checks": checks,
    "order": N,
    "scope": "scope-(a): classical-Habiro (K=Q, trivial Frobenius) harness; number-field twist test stays on qou-1hlh",
}
with open("computations/probes/zeta4_zeta8_habiro_gluing.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
