#!/usr/bin/env python3
"""
Probe — the Markov trace is NOT bond-multiplicative at n = 4: the interleaved
word s0 s1 s0 s2 s1 carries an exact, nonzero cross term.

Answers the general-n question left OPEN by
`markov_multiplicativity_interleaved_probe.py` (bean qou-ls86, 2026-08-18):
on H_3 the single interleaved word s0 s1 s0 is a cyclic rotation of a
sequential one, so the per-bond product formula is exact there; that probe
named `s0 s1 s0 s2 s1` as an n = 4 word with no such rotation and said
"nothing here says the product formula survives them."

It does not. Two INDEPENDENT routes agree as rational functions:

  (1) Ocneanu axioms only — tr(1)=1, Markov tr(x g_top)=z tr(x), cyclicity,
      Hecke g^2 = h g + 1, braid g0 g1 g0 = g1 g0 g1 — symbolic in (z, h):

        tr(s0 s1 s0 s2 s1) = z (z^2 + h z + h^2 z^2)
        tr(s0^2 s1^2 s2)   = z (h z + 1)^2            (the per-bond product)
        difference         = z (z^2 - h z - 1)

  (2) the spin-1/2 representation on V^{⊗4} (16-dim, brick-1 R-matrix) with the
      μ-weighted quantum trace normalised by [2]^4 — convention D — computed
      directly, no axioms assumed.

At convention D (z = q^3/(q^2+1), h = q - 1/q):

        difference = - q^3 (q^2 - q + 1)(q^2 + q + 1) / (q^2 + 1)^3  < 0   (q > 0)

The interleaved trace is SMALLER than the product, so an interleaved word class
carries EXTRA log-suppression = extra binding. At the proton anchor the ratio is
0.4085 (0.895 nats per interleaving). Control: the n = 3 identity reproduces as
exactly 0 in the same representation.

SCOPE — scope-(a) POSITIVE EXISTENCE, deliberately narrow. The production atom
word (`atom_braid_word_3A`) is sequential — each inter-nucleon generator is a
single letter and no generator recurs after its neighbour has appeared — so the
production trace's bare-product implementation is EXACT for the production word
class and NO existing number changes. This shows the multi-bond source that
qou-ls86 closed at n = 3 is OPEN at n = 4 for a DIFFERENT word class. Which word
class (if any) a nucleus is remains the carrier blocker (qou-5vhf); nothing is
wired and nothing is fitted.

Arithmetic: sympy exact rational functions; mpmath at 50 dps for the single
anchor evaluation (proton pin, `Q_50_DIGIT_STR`). No float64 anywhere.
"""
from __future__ import annotations

import os
import sys

import mpmath as mp
import sympy as sp

# Path bootstrap FIRST, then the bridge (per _path_bridge's documented USAGE — a script in a
# cluster subdir has sys.path[0] = its own dir, so `import _path_bridge` must follow the insert).
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401  (puts every cluster subdir on sys.path)
try:  # proton pin at 50 digits (owner directive 2026-08-07: proton is the default)
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
except Exception:  # pragma: no cover — bare container without the package path
    Q_50_DIGIT_STR = None

mp.mp.dps = 50


def route_axioms():
    """Ocneanu-axiom algebra, symbolic in (z, h). Returns (inter, seq, diff)."""
    z, h = sp.symbols("z h")
    tr_s0 = z                                   # Markov on 1
    tr_s0s1 = z * tr_s0                         # Markov on s0 ∈ H_2
    tr_s0sq = h * z + 1                         # Hecke: s0^2 = h s0 + 1
    tr_s0sq_s1 = z * tr_s0sq                    # Markov on s0^2 ∈ H_2
    tr_s0s1s0 = tr_s0sq_s1                      # cyclicity: tr((s0 s1) s0) = tr(s0 (s0 s1))
    tr_s1s0s1s0 = h * tr_s0s1s0 + tr_s0s1       # braid → s0 s1 s0 s0, Hecke on s0^2
    inter = z * tr_s1s0s1s0                     # cyclic rotate s1 to front, Markov on s2
    tr_s0sq_s1sq = h * tr_s0sq_s1 + tr_s0sq     # Hecke on s1^2
    seq = z * tr_s0sq_s1sq                      # Markov on s2
    return sp.expand(inter), sp.expand(seq), sp.factor(sp.expand(inter - seq)), (z, h)


def route_rep(n: int, q):
    """Spin-1/2 V^{⊗n} representation, μ-weighted quantum trace / [2]^n."""
    R = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
    I2 = sp.eye(2)

    def kron(*ms):
        out = ms[0]
        for m in ms[1:]:
            out = sp.kronecker_product(out, m)
        return out

    def sigma(i):
        return kron(*([I2] * i + [R] + [I2] * (n - i - 2)))

    W = kron(*([sp.diag(q, 1 / q)] * n))
    br2 = q + 1 / q

    def tr(X):
        return sp.simplify((W * X).trace() / br2 ** n)

    return sigma, tr


def main() -> int:
    checks: list[tuple[str, bool]] = []
    q = sp.symbols("q", positive=True)
    h_q = q - 1 / q
    z_D = q ** 3 / (q ** 2 + 1)

    # ---- (1) axioms ----
    inter_ax, seq_ax, diff_ax, (z, h) = route_axioms()
    target = sp.factor(z * (z ** 2 - h * z - 1))
    checks.append(("axioms: interleaved − product = z(z² − hz − 1)", sp.simplify(diff_ax - target) == 0))
    diff_ax_D = sp.factor(diff_ax.subs({z: z_D, h: h_q}))
    closed_D = -q ** 3 * (q ** 2 - q + 1) * (q ** 2 + q + 1) / (q ** 2 + 1) ** 3
    checks.append(("axioms @ conv D: = −q³(q²−q+1)(q²+q+1)/(q²+1)³", sp.simplify(diff_ax_D - closed_D) == 0))

    # ---- (2) independent 16-dim representation ----
    sigma, tr = route_rep(4, q)
    s0, s1, s2 = sigma(0), sigma(1), sigma(2)
    checks.append(("rep: tr(σ) = z_D (convention D)", sp.simplify(tr(s0) - z_D) == 0))
    checks.append(("rep: Hecke σ² = hσ + 1 holds in the rep",
                   sp.simplify(s0 * s0 - h_q * s0 - sp.eye(16)) == sp.zeros(16)))
    checks.append(("rep: braid σ0σ1σ0 = σ1σ0σ1 holds in the rep",
                   sp.simplify(s0 * s1 * s0 - s1 * s0 * s1) == sp.zeros(16)))
    inter_rep = tr(s0 * s1 * s0 * s2 * s1)
    seq_rep = tr(s0 * s0 * s1 * s1 * s2)
    diff_rep = sp.factor(sp.simplify(inter_rep - seq_rep))
    checks.append(("rep: interleaved − product equals the axiom closed form", sp.simplify(diff_rep - closed_D) == 0))
    checks.append(("rep: interleaved tr = z(z²+hz+h²z²) at conv D",
                   sp.simplify(inter_rep - inter_ax.subs({z: z_D, h: h_q})) == 0))
    checks.append(("rep: product tr = z(hz+1)² at conv D",
                   sp.simplify(seq_rep - seq_ax.subs({z: z_D, h: h_q})) == 0))
    checks.append(("cross term is NOT identically zero", sp.simplify(diff_rep) != 0))

    # ---- control: n = 3 identity is exactly zero in the same rep ----
    sigma3, tr3 = route_rep(3, q)
    a, b = sigma3(0), sigma3(1)
    checks.append(("control n=3: tr(s0 s1 s0) − tr(s0² s1) = 0 (the qou-ls86 identity)",
                   sp.simplify(tr3(a * b * a) - tr3(a * a * b)) == 0))

    # ---- sign and magnitude at the proton anchor (exact mp, 50 dps) ----
    if Q_50_DIGIT_STR is not None:
        q0 = Q_MP
        zz = q0 ** 3 / (q0 ** 2 + 1)
        hh = q0 - 1 / q0
        ratio = (zz ** 2 + hh * zz + hh ** 2 * zz ** 2) / ((hh * zz + 1) ** 2)
        extra_nats = -mp.log(ratio)
        checks.append(("q₀ (proton pin): interleaved/product ratio < 1 (extra binding)", ratio < 1))
        print(f"  q0 = {mp.nstr(q0, 20)}   ratio = {mp.nstr(ratio, 20)}   "
              f"extra log-suppression = {mp.nstr(extra_nats, 20)} nats")
    else:
        print("  (q_parameter not importable — anchor evaluation skipped; symbolic checks unaffected)")

    print("\n  axioms:  interleaved − product =", diff_ax)
    print("  conv D:  interleaved − product =", closed_D)
    print("  rep:     interleaved tr =", sp.factor(inter_rep))
    print("  rep:     product tr     =", sp.factor(seq_rep), "\n")

    ok = 0
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
