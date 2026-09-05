#!/usr/bin/env python3
"""PROBE A part 2 (bean `qou-jcmw`) — does the outer derivation of H_5(zeta_5)
act NON-TRIVIALLY on the cocenter HH_0 = A/[A,A]?

Part 1 (`hh1_hecke_h5_bring_root.py`) found dim HH^1(H_5(zeta_5)) = 1: an outer
derivation exists at the Bring root, so the route survives that prune. This is
the gate the 2026-08-08 Q_beta assessment actually named:

    "Degree mismatch needs care: c_3 arrives via tr_M, i.e. it lives in HH_0
     (the cocenter). Derivations are HH^1. The link would be the action of HH^1
     on HH_0, which is exactly what bean qou-dilv proposes and which nobody has
     run."

WHY THE COCENTER IS THE RIGHT TARGET
    c_3 arrives through the Markov trace tr_M, and every trace factors through
    the cocenter (`QOU/Information/CocenterTraceFactor.lean`). So a derivation
    can move trace data ONLY through its induced action on HH_0. Inner
    derivations act as ZERO there (ad_x(y) = [x,y] in [A,A]), so the induced
    action is canonically attached to the HH^1 class with no inner ambiguity --
    this is a well-posed yes/no question about the class itself.

THE TEST
    D_0 = 0  on HH_0   <=>   D(A) is contained in [A,A].
    If D(A) <= [A,A], the unique outer class is trace-blind: it cannot move
    tr_M, hence cannot carry the c_3 swing, and the HH^1 route dies -- without
    ever needing the bar-parity sub-test.

RIGOUR DIRECTION
    Entries lie in Z[zeta]; reduction mod a prime above p is a ring hom, so
    rank_p <= rank_0. Therefore
        D(A) NOT contained in [A,A]  mod p   =>  same in characteristic 0
    (a containment failure witnessed by a nonzero minor persists upward). The
    "contained" direction is the one that needs multi-prime corroboration, and
    is reported with that caveat.

No fit, no free parameter, nothing wired. Exact modular arithmetic only.
"""
import json
import os
from itertools import permutations

import numpy as np

from hh1_hecke_h5_bring_root import (
    find_prime_and_root, hecke_matrices, length, rank_mod,
)


def nullspace_mod(M, p):
    """Basis (as rows) of the nullspace of M over F_p."""
    A = np.array(M, dtype=np.int64) % p
    rows, cols = A.shape
    pivots, r = [], 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]:
                piv = i
                break
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
    free = [c for c in range(cols) if c not in set(pivots)]
    basis = []
    for f in free:
        v = np.zeros(cols, dtype=np.int64)
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-A[i, f]) % p
        basis.append(v % p)
    return np.array(basis, dtype=np.int64) if basis else np.zeros((0, cols), np.int64)


def reduced_word(w):
    """A reduced word for w as a list of generator indices (bubble sort)."""
    v, word = list(w), []
    n = len(v)
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                word.append(i)
                changed = True
    # `word` sorts w to the identity by RIGHT multiplications; reverse it to
    # express w itself as a product of generators.
    return word[::-1]


def analyse(n, p, qv, label):
    a = (qv - pow(qv, p - 2, p)) % p
    basis, index, L, R = hecke_matrices(n, a, p)
    N = len(basis)
    g = n - 1
    I = np.eye(N, dtype=np.int64)

    # ---- rebuild the derivation system (same as part 1) -------------------
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
    Dsys = np.vstack(blocks) % p
    Der = nullspace_mod(Dsys, p)          # rows: concatenated (D(T_1),...,D(T_g))

    # ---- inner derivations, expressed in the same coordinates -------------
    # ad_x(T_i) = T_i x - x T_i  ->  coordinates (R_i - L_i) x
    Inn = []
    for k in range(N):
        x = np.zeros(N, dtype=np.int64)
        x[k] = 1
        Inn.append(np.concatenate([((R[i] - L[i]) @ x) % p for i in range(g)]))
    Inn = np.array(Inn, dtype=np.int64) % p

    rank_inn = rank_mod(Inn, p)
    rank_all = rank_mod(np.vstack([Inn, Der]) % p, p)
    hh1 = rank_all - rank_inn
    assert rank_all == Der.shape[0], (rank_all, Der.shape)

    # ---- pick a derivation OUTSIDE the inner span -------------------------
    outer = None
    for row in Der:
        if rank_mod(np.vstack([Inn, row[None, :]]) % p, p) > rank_inn:
            outer = row % p
            break
    if outer is None:
        return None

    # ---- extend D from generators to all of A by Leibniz ------------------
    Dgen = [outer[i * N:(i + 1) * N] % p for i in range(g)]
    Dfull = np.zeros((N, N), dtype=np.int64)      # column c = D(T_{basis[c]})
    for c, w in enumerate(basis):
        word = reduced_word(w)
        if not word:
            continue                              # D(1) = 0
        acc = np.zeros(N, dtype=np.int64)
        for pos, gi in enumerate(word):
            # T_{prefix} . D(T_gi) . T_{suffix}
            v = Dgen[gi].copy()
            for h in reversed(word[:pos]):        # left-multiply by prefix
                v = (L[h] @ v) % p
            for h in word[pos + 1:]:              # right-multiply by suffix
                v = (R[h] @ v) % p
            acc = (acc + v) % p
        Dfull[:, c] = acc % p

    # sanity: the extension reproduces the generator values it was built from
    for i in range(g):
        s_i = tuple(j + 1 if j == i else (j - 1 if j == i + 1 else j)
                    for j in range(n))
        assert np.array_equal(Dfull[:, index[s_i]] % p, Dgen[i] % p)

    # ---- commutator subspace [A,A] ----------------------------------------
    # Left-multiplication matrix for each basis element, via its reduced word.
    Lbasis = []
    for w in basis:
        M = np.eye(N, dtype=np.int64)
        for h in reversed(reduced_word(w)):
            M = (L[h] @ M) % p
        Lbasis.append(M)
    comms = []
    for u in range(N):
        for v in range(N):
            # [B_u, B_v] = B_u B_v - B_v B_u, read off as columns
            comms.append((Lbasis[u][:, v] - Lbasis[v][:, u]) % p)
    Comm = np.array(comms, dtype=np.int64) % p
    rank_comm = rank_mod(Comm, p)
    dim_cocenter = N - rank_comm

    # ---- the decisive test:  is  D(A)  inside  [A,A] ? --------------------
    both = np.vstack([Comm, Dfull.T % p]) % p
    rank_both = rank_mod(both, p)
    acts_trivially = (rank_both == rank_comm)
    induced_rank = rank_both - rank_comm

    print(f"  {label}")
    print(f"    dim A = {N}   dim [A,A] = {rank_comm}   dim HH_0 = {dim_cocenter}")
    print(f"    dim HH^1 = {hh1}   (outer derivation found: "
          f"{'yes' if outer is not None else 'no'})")
    print(f"    rank of D(A) modulo [A,A] = {induced_rank}")
    print(f"    => outer class acts on the cocenter: "
          f"{'TRIVIALLY (D_0 = 0)' if acts_trivially else 'NON-TRIVIALLY'}")
    return {
        "dim_A": int(N), "dim_commutator": int(rank_comm),
        "dim_cocenter": int(dim_cocenter), "dim_HH1": int(hh1),
        "induced_rank_on_cocenter": int(induced_rank),
        "acts_trivially_on_cocenter": bool(acts_trivially),
    }


def main():
    print("PROBE A part 2 — action of the outer derivation on the cocenter\n")
    out = {}
    primes = [find_prime_and_root(20, 5000)[0], find_prime_and_root(20, 60000)[0]]
    for p in primes:
        g = next(gg for gg in range(2, 500)
                 if pow(gg, (p - 1) // 20, p) != 1
                 and all(pow(pow(gg, (p - 1) // 20, p), 20 // l, p) != 1
                         for l in (2, 5)))
        z20 = pow(g, (p - 1) // 20, p)
        z5 = pow(z20, 4, p)
        print(f"--- F_{p} ---")
        r = analyse(5, p, z5, "H_5 at q = zeta_5 (Bring root)")
        out[str(p)] = r
        print()

    trivial = {v["acts_trivially_on_cocenter"] for v in out.values()}
    print("=" * 72)
    if trivial == {True}:
        print("VERDICT: the unique outer class of H_5(zeta_5) is TRACE-BLIND.")
        print("D(A) lies inside [A,A], so the induced action on HH_0 vanishes.")
        print("Every trace factors through HH_0 (CocenterTraceFactor.lean), so")
        print("this class cannot move tr_M and cannot carry the c_3 swing.")
        print("The HH^1 -> HH_0 route to c_3 is CLOSED -- and the bar-parity")
        print("sub-test is moot: a zero map has no parity to measure.")
    else:
        print("VERDICT: the outer class acts NON-TRIVIALLY on the cocenter.")
        print("It can move trace data. The route survives; bar-parity of the")
        print("induced map is now the decisive gate.")
    print("=" * 72)

    witness = {
        "schema": "qou-probe/v1",
        "probe": "PROBE-A part 2: action of HH^1(H_5(zeta_5)) on the cocenter HH_0",
        "bean": "qou-jcmw",
        "description": (
            "Tests whether the unique outer derivation of H_5 at the Bring root "
            "of unity induces a nonzero map on HH_0 = A/[A,A]. Inner derivations "
            "act as zero on HH_0, so the induced action is canonically attached "
            "to the HH^1 class. Since every trace factors through HH_0, a zero "
            "induced action means the class is trace-blind and cannot carry c_3."),
        "method": (
            "D(A) computed by Leibniz extension along reduced words from the "
            "outer generator of the derivation nullspace; [A,A] spanned by all "
            "[T_u, T_v]; test is rank([A,A] + D(A)) == rank([A,A])."),
        "rigour_note": (
            "Reduction mod a prime above p is a ring hom so rank_p <= rank_0; a "
            "NON-trivial action found mod p therefore persists to characteristic "
            "0. The trivial direction is corroborated across two unrelated primes "
            "but is not by itself a characteristic-0 proof."),
        "results": out,
        "wired_to_production": False,
        "fit_performed": False,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "hh1-h5-cocenter-action.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {path}")


if __name__ == "__main__":
    main()
