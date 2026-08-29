#!/usr/bin/env python3
"""PROBE A part 3 (bean `qou-jcmw`) — parity of the outer class's cocenter
action under the sign-twisted bar involution of H_5(zeta_5).

Parts 1-2 established: dim HH^1(H_5(zeta_5)) = 1, and the unique outer class
acts with rank 1 on the 7-dimensional cocenter HH_0 -- it is trace-visible, so
it CAN move tr_M. The remaining gate named by
`docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md` §5 is bar
parity: the c_3 carrier S is bar-ODD, and a bar-EVEN object cannot supply it.

WHAT IS AND IS NOT COMPUTED HERE -- READ BEFORE CITING
    The corpus's bar involution is SEMILINEAR: it sends q -> q^{-1} together
    with T_i -> T_i^{-1} = T_i - a. Over a finite field with q specialized to a
    fixed root z, "q -> q^{-1}" is not available (F_p has no automorphism moving
    z to z^{-1}), so bar itself does not act on H_z; it maps H_z -> H_{z^{-1}}.

    What IS available over F_p is the composite with the sign twist
    sigma_-: T_i -> -T_i  (an isomorphism H_{z^{-1}} -> H_z), giving

        Theta := sigma_- . bar :  H_z -> H_z,     Theta(T_i) = a - T_i,

    which is verified below to be an involutive F_p-ALGEBRA automorphism -- the
    linear shadow of bar. This script measures the parity of the cocenter action
    under Theta, NOT under bar itself.

    Consequently: a Theta-parity result transfers to a bar-parity statement only
    after the sign twist's own contribution is accounted for. That last step
    needs the semilinear computation over Q(zeta_5) and is NOT done here. This
    file reports a Theta-parity fact and names the residual gap; it does not
    claim to have settled bar parity. (AGENTS.md "Before declaring refuted":
    everything below is scope-(a).)

No fit, no free parameter, nothing wired. Exact modular arithmetic only.
"""
import json
import os

import numpy as np

from hh1_hecke_h5_bring_root import find_prime_and_root, hecke_matrices, rank_mod
from hh1_h5_cocenter_action import nullspace_mod, reduced_word


def rref_mod(M, p):
    """Reduced row echelon form and pivot columns."""
    A = np.array(M, dtype=np.int64) % p
    rows, cols = A.shape
    pivots, r = [], 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c]), None)
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        nz = np.nonzero(A[:, c])[0]
        nz = nz[nz != r]
        if nz.size:
            A[nz] = (A[nz] - np.outer(A[nz, c], A[r])) % p
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return A[:r], pivots


def build(n, p, qv):
    a = (qv - pow(qv, p - 2, p)) % p
    basis, index, L, R = hecke_matrices(n, a, p)
    N, g = len(basis), n - 1
    I = np.eye(N, dtype=np.int64)

    def row_block(assign):
        row = np.zeros((N, g * N), dtype=np.int64)
        for i, M in assign.items():
            row[:, i * N:(i + 1) * N] = M % p
        return row

    blocks = [row_block({i: (L[i] + R[i] - a * I) % p}) for i in range(g)]
    for i in range(g - 1):
        j = i + 1
        blocks.append(row_block({
            i: (R[i] @ R[j] + L[i] @ L[j] - L[j] @ R[j]) % p,
            j: (L[i] @ R[i] - R[j] @ R[i] - L[j] @ L[i]) % p}))
    for i in range(g):
        for j in range(i + 2, g):
            blocks.append(row_block({i: (R[j] - L[j]) % p,
                                     j: (L[i] - R[i]) % p}))
    Der = nullspace_mod(np.vstack(blocks) % p, p)
    Inn = np.array([np.concatenate(
        [((R[i] - L[i])[:, k]) % p for i in range(g)]) for k in range(N)],
        dtype=np.int64) % p
    rank_inn = rank_mod(Inn, p)
    outer = next(row % p for row in Der
                 if rank_mod(np.vstack([Inn, row[None, :]]) % p, p) > rank_inn)

    # left-multiplication matrix per basis element
    Lbasis = []
    for w in basis:
        M = np.eye(N, dtype=np.int64)
        for h in reversed(reduced_word(w)):
            M = (L[h] @ M) % p
        Lbasis.append(M)

    # D on all of A
    Dgen = [outer[i * N:(i + 1) * N] % p for i in range(g)]
    Dfull = np.zeros((N, N), dtype=np.int64)
    for c, w in enumerate(basis):
        word = reduced_word(w)
        acc = np.zeros(N, dtype=np.int64)
        for pos, gi in enumerate(word):
            v = Dgen[gi].copy()
            for h in reversed(word[:pos]):
                v = (L[h] @ v) % p
            for h in word[pos + 1:]:
                v = (R[h] @ v) % p
            acc = (acc + v) % p
        Dfull[:, c] = acc % p

    # Theta: algebra automorphism  T_i -> a - T_i,  extended along words
    Theta_gen = [(a * np.eye(N, dtype=np.int64)[:, 0] * 0) for _ in range(g)]
    Theta = np.zeros((N, N), dtype=np.int64)
    for c, w in enumerate(basis):
        word = reduced_word(w)
        vec = np.zeros(N, dtype=np.int64)
        vec[0] = 1                                   # start from T_e = 1
        # identity must be basis index 0 (basis sorted by length)
        assert basis[0] == tuple(range(n))
        for gi in word:
            # multiply on the right by Theta(T_gi) = a*1 - T_gi
            vec = (a * vec - (R[gi] @ vec)) % p
        Theta[:, c] = vec % p
    # Theta is an involution
    assert np.array_equal((Theta @ Theta) % p, np.eye(N, dtype=np.int64))

    # commutator subspace
    comms = [(Lbasis[u][:, v] - Lbasis[v][:, u]) % p
             for u in range(N) for v in range(N)]
    Comm = np.array(comms, dtype=np.int64) % p
    Crref, Cpiv = rref_mod(Comm, p)
    free = [c for c in range(N) if c not in set(Cpiv)]

    def to_cocenter(vec):
        """Coordinates of vec in A/[A,A], using `free` columns as the basis."""
        v = np.array(vec, dtype=np.int64) % p
        for i, c in enumerate(Cpiv):
            if v[c]:
                v = (v - v[c] * Crref[i]) % p
        return v[free] % p

    d = len(free)
    D0 = np.array([to_cocenter(Dfull[:, 0] * 0 + Dfull @ np.eye(N, dtype=np.int64)[:, free[k]])
                   for k in range(d)], dtype=np.int64).T % p
    T0 = np.array([to_cocenter(Theta @ np.eye(N, dtype=np.int64)[:, free[k]])
                   for k in range(d)], dtype=np.int64).T % p
    return dict(a=a, N=N, dim_cocenter=d, D0=D0, T0=T0, p=p)


def main():
    print("PROBE A part 3 — Theta-parity of the outer class on the cocenter")
    print("(Theta = sign-twisted bar, the F_p-linear shadow; see docstring)\n")
    out = {}
    primes = [find_prime_and_root(20, 5000)[0], find_prime_and_root(20, 60000)[0]]
    for p in primes:
        gg = next(x for x in range(2, 500)
                  if pow(x, (p - 1) // 20, p) != 1
                  and all(pow(pow(x, (p - 1) // 20, p), 20 // l, p) != 1
                          for l in (2, 5)))
        z5 = pow(pow(gg, (p - 1) // 20, p), 4, p)
        r = build(5, p, z5)
        D0, T0, d = r["D0"], r["T0"], r["dim_cocenter"]
        conj = (T0 @ D0 @ T0) % p                 # T0 is an involution: T0^{-1} = T0
        even = np.array_equal(conj, D0 % p)
        odd = np.array_equal(conj, (-D0) % p)
        verdict = ("Theta-EVEN" if even else
                   "Theta-ODD" if odd else "neither (mixed)")
        print(f"--- F_{p} ---")
        print(f"    dim HH_0 = {d}   rank D_0 = {rank_mod(D0, p)}   "
              f"rank(Theta_0) = {rank_mod(T0, p)}")
        print(f"    Theta_0 . D_0 . Theta_0  vs  D_0  ->  {verdict}")
        out[str(p)] = {"dim_cocenter": int(d),
                       "rank_D0": int(rank_mod(D0, p)),
                       "theta_parity": verdict}
    print()
    verdicts = {v["theta_parity"] for v in out.values()}
    print("=" * 72)
    print(f"Theta-parity across primes: {verdicts}")
    if verdicts == {"Theta-ODD"}:
        print("The outer class's cocenter action is ODD under the sign-twisted")
        print("bar. This is the parity the c_3 carrier S needs -- the route is")
        print("NOT pruned here. Remaining step: convert Theta-parity to true bar")
        print("parity by accounting for the sign twist, over Q(zeta_5).")
    elif verdicts == {"Theta-EVEN"}:
        print("The outer class's cocenter action is EVEN under the sign-twisted")
        print("bar. Whether that makes it bar-EVEN (and so unable to carry the")
        print("bar-odd S) depends on the sign twist's own parity -- NOT settled")
        print("here. Do not record this as a refutation without that step.")
    else:
        print("Mixed / inconsistent: the action is not a Theta-eigenvector.")
        print("No parity claim can be made; report as inconclusive.")
    print("=" * 72)

    witness = {
        "schema": "qou-probe/v1",
        "probe": "PROBE-A part 3: Theta-parity of the HH^1 class action on HH_0",
        "bean": "qou-jcmw",
        "description": (
            "Parity of the outer class's cocenter action under Theta = "
            "sigma_- . bar (T_i -> a - T_i), the F_p-linear shadow of the "
            "semilinear bar involution."),
        "scope_caveat": (
            "scope-(a). This measures Theta-parity, NOT bar-parity. The bar "
            "involution is semilinear (q -> q^{-1}) and does not act on a "
            "single finite-field specialization; converting a Theta-parity "
            "result into a bar-parity claim requires accounting for the sign "
            "twist and is NOT performed here."),
        "results": out,
        "wired_to_production": False,
        "fit_performed": False,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "hh1-h5-bar-parity.witness.json")
    with open(path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {path}")


if __name__ == "__main__":
    main()
