"""qou-0whz: can any braid word be the W? Exact structural checks (sympy, no floats).

The corpus gives the W two different braids:
  * def:beta-decay-skein inserts T(3,5) = (s1 s2)^5 at the converting d quark
    and reduces to  N(Z+1,N-1) ⊔ T(2,3) ⊔ unknot;
  * conj weak-spectral-completeness / thm:hoefsmit-ew-cell-content assign
    W <-> s1^4 = T(2,4).

Level 2 here means convention D read through gl_2 Schur–Weyl duality: H_n(q)
acts on (C^2)^{⊗n} via the Jimbo R-matrix (s^2 = h s + 1, eigenvalue q on the
symmetric part), and the Markov trace is the quantum trace with K = diag(q^{±1}).

Checks
  C1  K orientation: only one orientation of K gives a Markov trace
      (partial quantum trace of R a scalar), and its z is exactly
      z_D = q^3/(q^2+1). So D forces K = q on the highest-weight vector of R,
      i.e. T^3 = +1/2. Which QUARK sits there is not decided here.
  C2  Schur–Weyl: on (C^2)^{⊗3}, every braid letter, hence T(3,5) and s1^4,
      commutes with Delta^{(3)}(K), Delta^{(3)}(E), Delta^{(3)}(F). So a braid
      word preserves each weight (flavour) space and cannot change u into d;
      the flavour-changing maps are E and F.
  C3  Component count: a 3-strand braid closure has at most 3 components.
      The right-hand side of def:beta-decay-skein for the free neutron,
      p ⊔ T(2,3) ⊔ unknot, has at least 3 + 1 + 1 = 5 components (the corpus
      proton is the Borromean B_3, 3 components). So no braid insertion on the
      nucleon's strands can produce it as a link equality; lepton emission
      needs new strands (a creation/coevaluation morphism), not a braid.
  C4  Over/under transmission (qou-0whz, owner card "Probe C4 + Lean"): with the
      corpus convention that in s_i the lower strand i passes OVER
      (intro-particles-as-knots, Lean QOU/Knot/BraidClosure stepOver_lo; for
      s_i^{-1} strand i+1 is over), and with K fixed by C1, a crossing is a pure
      transposition (no h label-exchange term) iff its over strand carries the
      K = q weight vector. Checked for both R conventions and both signs.
      With def:down-quark ("u passes over d at every crossing") this reads
      u = the K = q vector, T^3 = +1/2. Lean twin:
      QOU/QuarkState/OverStrandWeight.lean (over_e1_iff_pure, ptr_markov).
"""
from __future__ import annotations

import itertools
import json
import pathlib

import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
ZD = q**3 / (q**2 + 1)


def R(h_slot: str) -> sp.Matrix:
    """Jimbo R-check on C2⊗C2, basis e1e1,e1e2,e2e1,e2e2; h on e2e1 ('std') or e1e2."""
    M = sp.zeros(4)
    M[0, 0] = q
    M[3, 3] = q
    M[1, 2] = 1
    M[2, 1] = 1
    if h_slot == "std":
        M[2, 2] = h
    else:
        M[1, 1] = h
    return M


def is_zero(M) -> bool:
    return sp.simplify(M) == sp.zeros(*M.shape)


def c1_k_orientation():
    rows = []
    for slot in ("std", "swp"):
        S = R(slot)
        assert is_zero(S * S - h * S - sp.eye(4)), "Hecke relation"
        for a in (1, -1):
            K = sp.diag(q**a, q**-a)
            P = sp.kronecker_product(sp.eye(2), K) * S
            part = sp.Matrix(2, 2, lambda i, j: sum(P[2 * i + k, 2 * j + k] for k in range(2)))
            part = sp.simplify(part)
            scalar = is_zero(part - part[0, 0] * sp.eye(2))
            z = sp.simplify(part[0, 0] / K.trace()) if scalar else None
            rows.append({
                "h_slot": slot, "K_on_e1": f"q^{a:+d}", "markov": scalar,
                "z": str(z) if z is not None else None,
                "z_is_zD": bool(z is not None and sp.simplify(z - ZD) == 0),
                "partial_trace": [[str(x) for x in r] for r in part.tolist()],
            })
    # exactly one Markov orientation per R, and it is z_D
    ok = all(sum(r["markov"] for r in rows if r["h_slot"] == s) == 1 for s in ("std", "swp")) \
        and all(r["z_is_zD"] for r in rows if r["markov"])
    return ok, rows


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


def c2_schur_weyl():
    S = R("std")
    I2 = sp.eye(2)
    K = sp.diag(q, 1 / q)
    E = sp.Matrix([[0, 1], [0, 0]])
    F = sp.Matrix([[0, 0], [1, 0]])
    Ki = K.inv()
    # try the two standard coproducts; keep the one R commutes with on n=2
    cops = {
        "E⊗K+1⊗E": (lambda: kron(E, K) + kron(I2, E), lambda: kron(F, I2) + kron(Ki, F)),
        "E⊗1+K⊗E": (lambda: kron(E, I2) + kron(K, E), lambda: kron(F, Ki) + kron(I2, F)),
    }
    chosen = None
    for name, (dE, dF) in cops.items():
        if is_zero(S * dE() - dE() * S) and is_zero(S * dF() - dF() * S):
            chosen = name
            break
    assert chosen is not None, "no coproduct commutes with R"
    # n = 3 coproducts
    if chosen == "E⊗K+1⊗E":
        E3 = kron(E, K, K) + kron(I2, E, K) + kron(I2, I2, E)
        F3 = kron(F, I2, I2) + kron(Ki, F, I2) + kron(Ki, Ki, F)
    else:
        E3 = kron(E, I2, I2) + kron(K, E, I2) + kron(K, K, E)
        F3 = kron(F, Ki, Ki) + kron(I2, F, Ki) + kron(I2, I2, F)
    K3 = kron(K, K, K)
    s1 = kron(S, I2)
    s2 = kron(I2, S)
    T35 = (s1 * s2) ** 5
    T24 = s1 ** 4
    out = {"coproduct": chosen}
    for nm, X in (("s1", s1), ("s2", s2), ("T(3,5)", T35), ("s1^4", T24)):
        out[nm] = {g: is_zero(X * G - G * X) for g, G in (("K", K3), ("E", E3), ("F", F3))}
    ok = all(all(v.values()) for k, v in out.items() if k != "coproduct")
    return ok, out


def perm_of_word(word, n):
    p = list(range(n))
    for g in word:  # g = i means s_i (1-based), swaps i-1,i
        i = abs(g) - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def cycles(p):
    seen, c = set(), 0
    for i in range(len(p)):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def c3_components():
    n = 3
    t35 = [1, 2] * 5
    # maximum components over every 3-strand word: closure components = cycles of
    # the permutation, so max over S_3 is 3 (identity)
    max_c = max(cycles(list(p)) for p in itertools.permutations(range(n)))
    t35_alone = cycles(perm_of_word(t35, n))
    rhs_min = 3 + 1 + 1  # Borromean proton + trefoil (1 comp) + unknot
    return max_c < rhs_min, {"max_components_3_strand_closure": max_c,
                             "components_T35_closure": t35_alone,
                             "rhs_min_components_p_trefoil_unknot": rhs_min}


def _basis(i, j):
    v = sp.zeros(4, 1)
    v[2 * i + j] = 1
    return v


def c4_over_under():
    rows = []
    ok = True
    for slot in ("std", "swp"):
        S = R(slot)
        Sinv = sp.simplify(S - h * sp.eye(4))
        assert is_zero(S * Sinv - sp.eye(4))
        # K orientation forced by C1 for this R: weight index carrying K = q
        kq = None
        for a in (1, -1):
            K = sp.diag(q**a, q**-a)
            P = sp.kronecker_product(sp.eye(2), K) * S
            part = sp.simplify(sp.Matrix(2, 2, lambda i, j: sum(P[2 * i + k, 2 * j + k] for k in range(2))))
            if is_zero(part - part[0, 0] * sp.eye(2)):
                kq = 0 if a == 1 else 1
        for sign, M, over_pos in (("+", S, 0), ("-", Sinv, 1)):
            for over_lab in (0, 1):
                under_lab = 1 - over_lab
                lab = [None, None]
                lab[over_pos] = over_lab
                lab[1 - over_pos] = under_lab
                v = _basis(*lab)
                out = sp.simplify(M * v)
                swapped = _basis(lab[1], lab[0])
                exch = sp.simplify(out - swapped)
                pure = is_zero(exch)
                predicted = (over_lab == kq)
                ok = ok and (pure == predicted)
                rows.append({"h_slot": slot, "sign": sign,
                             "over_strand_carries": f"e{over_lab + 1}",
                             "K_on_over_strand": "q" if over_lab == kq else "q^-1",
                             "pure_transposition": pure,
                             "exchange_term": [str(x) for x in exch]})
    return ok, rows


def main():
    res = {}
    ok1, res["C1_K_orientation"] = c1_k_orientation()
    ok2, res["C2_schur_weyl_weight_preservation"] = c2_schur_weyl()
    ok3, res["C3_component_count"] = c3_components()
    ok4, res["C4_over_under_transmission"] = c4_over_under()
    res["checks"] = {"C1": ok1, "C2": ok2, "C3": ok3, "C4": ok4}
    for k, v in res["checks"].items():
        print(k, "PASS" if v else "FAIL")
    print(json.dumps(res, indent=1, ensure_ascii=False))
    out = pathlib.Path(__file__).with_name("w-braid-reconcile.witness.json")
    out.write_text(json.dumps({
        "producer": "computations/probes/w_braid_reconcile_probe.py",
        "bean": "qou-0whz",
        "arithmetic": "exact (sympy over Q(q)); no floats",
        "q0_anchor": "none (symbolic in q)",
        "q0Anchor": "independent",
        "q0AnchorReason": ("probe never reads q0: every quantity is exact over Q(q) (sympy), "
                           "q a free symbol; imports only sympy and the standard library"),
        **res,
    }, indent=1, ensure_ascii=False) + "\n")
    assert all(res["checks"].values())


if __name__ == "__main__":
    main()
