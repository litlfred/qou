"""Which side of a block a traced-out spectator crossing sits on.

Exact symbolic check (sympy over Q(q), no floats) of the local fact proved in
`QOU/QBeta/WeightedTraceSide.lean`, inside the pair-term readout of one block.

The readout weights every strand by K = diag(q, 1/q). Take one spectator strand and a
single crossing between it and the block, and trace the spectator out:

* spectator to the RIGHT of the block, crossing its last strand: the spectator trace
  leaves the scalar q^2 on that strand, so the ratio T_X/T_1 is the same in every charge
  sector of the block (a constant);
* spectator to the LEFT of the block, crossing its first strand: the trace leaves
  diag(q^2 + 1 - q^-2, 1) on that strand, and the ratio depends on the block's charge.

The block is three strands with C = (s0 s1^-1)^3, as in the pair-term readout; charge is
(number of weight +1 strands) - 1. Since C and the sector projector factor over the two
blocks, the same ratio is what the full two-block readout sees for X = that crossing.

Run: python3 computations/probes/np_splitting/np_one_crossing_trace_side_probe.py
"""
import sympy as sp

q = sp.Symbol("q")
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, q - 1 / q, 0], [0, 0, 0, q]])
I2 = sp.eye(2)
K = sp.diag(q, 1 / q)


def kp(*m):
    return m[0] if len(m) == 1 else sp.kronecker_product(m[0], kp(*m[1:]))


def ptrace(Y, site, w):
    """Trace out `site` (0 or 1) of a two-strand operator with weight w."""
    Z = sp.zeros(2, 2)
    for i in range(4):
        for j in range(4):
            bi, bj = [(i >> 1) & 1, i & 1], [(j >> 1) & 1, j & 1]
            if bi[site] != bj[site]:
                continue
            o = 1 - site
            Z[bi[o], bj[o]] += w[bi[site], bi[site]] * Y[i, j]
    return Z.applyfunc(sp.factor)


def main():
    D_left = ptrace(R, 0, K)    # spectator on the left, traced against the block's first strand
    D_right = ptrace(R, 1, K)   # spectator on the right, traced against the block's last strand
    print("left-closed crossing :", D_left.tolist())
    print("right-closed crossing:", D_right.tolist())
    assert D_right == q**2 * sp.eye(2)
    assert sp.simplify(D_left - sp.diag(q**2 + 1 - q**-2, 1)) == sp.zeros(2, 2)

    s0, s1 = kp(R, I2), kp(I2, R)
    C = ((s0 * s1.inv()) ** 3).applyfunc(sp.cancel)
    KK = kp(K, K, K)

    def charge(i):
        return sum(1 for k in range(3) if not (i >> (2 - k)) & 1) - 1

    out = {}
    for name, D in [("left", kp(D_left, I2, I2)), ("right", kp(I2, I2, D_right))]:
        vals = []
        for a in (-1, 0, 1, 2):
            P = sp.diag(*[1 if charge(i) == a else 0 for i in range(8)])
            T = sp.cancel((KK * P * C).trace())
            TD = sp.cancel((KK * P * C * D).trace())
            vals.append(sp.factor(sp.cancel(TD / T)))
        out[name] = vals
        print(f"spectator on the {name}: T_X/T_1 by block charge -1, 0, 1, 2 (before dividing by "
              f"the spectator's own trace q + 1/q):")
        for a, v in zip((-1, 0, 1, 2), vals):
            print(f"   charge {a:2d}: {v}")
    right_const = all(sp.cancel(v - out["right"][0]) == 0 for v in out["right"])
    left_const = all(sp.cancel(v - out["left"][0]) == 0 for v in out["left"])
    print("right: same in every charge sector:", right_const)
    print("left : same in every charge sector:", left_const)
    assert right_const and not left_const
    print("PASS")


if __name__ == "__main__":
    main()
