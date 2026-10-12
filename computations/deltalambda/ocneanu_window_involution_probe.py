"""Which involution acts on the Markov parameter as z -> h - z?  (bean qou-wktw)

Exact sympy over Q(q, z).  No floats anywhere.

Ocneanu closed form (QOU.SchurWeyl.ocneanuWeight):
    w_mu(q, z) = prod_cells (q^{2i}(q^2-1-qz) + q^{2j+1} z) / prod_cells (q^{2 hook} - 1),
    h = q - q^{-1}.

Checked for every mu |- n, 1 <= n <= 7:

  (T) sign-transpose:  w_{mu'}(q, h - z) == w_mu(q, z)
      (the automorphism sigma -> -sigma^{-1} of H_n(q): tr(-sigma^{-1}) = h - z,
       and it carries V_lambda to V_lambda')
  (B) bar:             w_mu(q^{-1}, z - h(q)) == w_mu(q, z)
      (sigma -> sigma^{-1}, q -> q^{-1}; the bar-conjugate of the trace with
       parameter z(q) has parameter z(q^{-1}) + h(q))

and, on the z-line:
  * (T) fixes exactly z = h/2 (n = 2: w_(2) = w_(1,1) <=> z = h/2);
  * the bar condition z(q) - z(q^{-1}) = h holds for h/2 AND for the whole
    Ocneanu rank family z_k = h q^{2k}/(q^{2k}-1) (z_1 = q, z_2 = q^3/(q^2+1) =
    convention D) and their mirrors h - z_k.  So bar-invariance does NOT single
    out h/2 (scope (a): a statement about this condition, not about any other).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

q, z = sp.symbols("q z")
h = q - 1 / q
NMAX = 7


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(mu):
    return [(i, j) for i, r in enumerate(mu) for j in range(r)]


def transpose(mu):
    return tuple(sum(1 for r in mu if r > j) for j in range(mu[0])) if mu else ()


def hook(mu, i, j):
    mt = transpose(mu)
    return (mu[i] - j) + (mt[j] - i) - 1


def weight(mu, qq, zz):
    num = sp.Integer(1)
    den = sp.Integer(1)
    for (i, j) in cells(mu):
        num *= qq ** (2 * i) * (qq ** 2 - 1 - qq * zz) + qq ** (2 * j + 1) * zz
        den *= qq ** (2 * hook(mu, i, j)) - 1
    return num / den


def is_zero(e):
    return sp.cancel(sp.together(e)) == 0


def main() -> int:
    t_ok = b_ok = True
    rows = []
    for n in range(1, NMAX + 1):
        cnt = 0
        for mu in partitions(n):
            w = weight(mu, q, z)
            t = is_zero(weight(transpose(mu), q, h - z) - w)
            b = is_zero(weight(mu, 1 / q, z - h) - w)
            t_ok &= t
            b_ok &= b
            cnt += 1
        rows.append({"n": n, "partitions": cnt, "T_holds": t_ok, "B_holds": b_ok})
        print(f"n={n}: {cnt} partitions, T={t_ok}, B={b_ok}")

    # (T) fixed points at n = 2
    sol = sp.solve(sp.cancel(weight((2,), q, z) - weight((1, 1), q, z)), z)
    t_fix = [sp.simplify(s - h / 2) for s in sol]
    t_forces_half = (len(sol) == 1 and t_fix[0] == 0)
    print("n=2 transpose-symmetric z:", sol, "forces h/2:", t_forces_half)

    # bar condition z(q) - z(1/q) == h
    def bar_ok(expr):
        return is_zero(expr - expr.subs(q, 1 / q) - h)

    cands = {"h/2": h / 2}
    for k in range(1, 6):
        zk = h * q ** (2 * k) / (q ** (2 * k) - 1)
        cands[f"z_{k}"] = zk
        cands[f"h - z_{k}"] = h - zk
    cands["zD = q^3/(q^2+1)"] = q ** 3 / (q ** 2 + 1)
    cands["z = 0 (control)"] = sp.Integer(0)
    bar = {k: bar_ok(v) for k, v in cands.items()}
    for k, v in bar.items():
        print(f"  bar-invariant {k}: {v}")
    zD_is_z2 = is_zero(cands["z_2"] - q ** 3 / (q ** 2 + 1))

    # an in-window bar-invariant parameter other than h/2: z = h/2 + u,
    # u = h^2/(1+h^2) bar-even; window margins are explicit squares for q > 1:
    #   z - 0 = h/2 + u  (both terms >= 0 for h >= 0)
    #   h - z = h/2 - u = h (1 - h)^2 / (2 (1 + h^2))  >= 0
    u = h ** 2 / (1 + h ** 2)
    u_even = is_zero(u - u.subs(q, 1 / q))
    z_alt = h / 2 + u
    alt_bar = bar_ok(z_alt)
    upper_margin = is_zero((h - z_alt) - h * (1 - h) ** 2 / (2 * (1 + h ** 2)))
    alt_in_window = u_even and alt_bar and upper_margin
    print("in-window bar-invariant z = h/2 + h^2/(1+h^2):", alt_in_window)
    many_bar = sum(1 for k, v in bar.items() if v and k != "h/2") >= 3

    w = WitnessBuilder("ocneanu-window-involution", engine="sympy",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("transpose_identity_all_mu_n_le_7", 1 if t_ok else 0, 1)
    w.add_assertion("bar_identity_all_mu_n_le_7", 1 if b_ok else 0, 1)
    w.add_assertion("transpose_symmetry_n2_forces_h_half", 1 if t_forces_half else 0, 1)
    w.add_assertion("bar_invariance_does_not_single_out_h_half", 1 if many_bar else 0, 1)
    w.add_assertion("bar_invariant_in_window_param_other_than_h_half", 1 if alt_in_window else 0, 1)
    w.add_assertion("zD_equals_rank2_parameter", 1 if zD_is_z2 else 0, 1)
    w.add_assertion("control_z0_not_bar_invariant", 0 if bar["z = 0 (control)"] else 1, 1)
    w.add_parameter("n_max", str(NMAX))
    w.add_data("by_n", rows)
    w.add_data("bar_invariant", {k: bool(v) for k, v in bar.items()})
    w.save()
    ok = alt_in_window and t_ok and b_ok and t_forces_half and many_bar and zD_is_z2 and not bar["z = 0 (control)"]
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
