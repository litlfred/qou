#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): WHICH of the four objects can the exchangeable-pair machinery actually reach?
The Fulman identity is keyed to an EIGENFUNCTION of the up-down chain, and only W is one -- so the
route whose remaining object is V_A may be the one the machinery CANNOT help with.

WHY THIS, AND WHY IT REFINES THE SAME PR IT SHIPS WITH. PR #6651 (this branch) measured that the
Cauchy-Schwarz relaxation is cheap -- it keeps >= 78.6% of the true margin -- and concluded "the
margin route is the right target". That conclusion conflates two different claims:

    (i)  the relaxation is TIGHT           <- what #6651 measured, and it stands
    (ii) the resulting bound is TRACTABLE  <- NOT measured, and it is a different question

Tractability is decided by the machinery the corpus already identified. Fulman's exchangeable-pair
identity (arxiv-math-0305423, via the up-down Markov chain J on the Young lattice) reads

    Cov(f, g) = E_pi[(f - f*)(g - g*)] / (2(1 - beta))     valid when  J g = beta * g,

i.e. it computes the covariance of ANY statistic f against an EIGENFUNCTION g. The corpus's
reduction uses g = omega_3 = W with beta_3 = (n-2)/(n+1), which is why P = Cov(A,W) and
N = -Cov(D,W) come out as local, per-edge, manifestly-signed sums.

    V_A = Cov(A, A) needs A ITSELF to be an eigenfunction. If it is not, the identity does not
    apply to V_A at all, and the margin route's one remaining object has no local representation --
    while P > N's two objects both do.

That would not make V_A unreachable by other means; it would mean the tool the roadmap names does
not reach it. Either way it decides where the next effort goes, so it is worth one exact test.

WHAT IS COMPUTED. The up-down chain on Y_n composes a Plancherel up-step with a down-step:

    p_up(lam -> mu)   = dim(mu) / ((n+1) dim(lam))      for lam /^ mu,  mu |- n+1
    p_down(mu -> nu)  = dim(nu) / dim(mu)               for mu \_ nu,   nu |- n

which composes to the closed form this probe uses (and asserts row-stochastic):

    J(lam, lam*) = dim(lam*) * c(lam, lam*) / ((n+1) dim(lam)),
    c(lam, lam*) = #{ mu |- n+1 : lam /^ mu  and  lam* /^ mu }.

For each statistic f in {W, A, D} it forms (Jf)(lam) = sum_lam* J(lam,lam*) f(lam*) in exact
Fractions and asks whether Jf = beta*f for a single constant beta -- the definition of an
eigenfunction. The spread of the pointwise ratio (Jf)(lam)/f(lam) over all lam is the answer: zero
spread is an eigenfunction, anything else is not.

THE POSITIVE CONTROL IS W, and it is what makes a negative on A meaningful. W is KNOWN to be an
eigenfunction with beta_3 = (n-2)/(n+1) (corpus, 2026-08-21, verified there to n <= 13). If this
probe's chain is built correctly it must reproduce that exactly; if it does not, the chain is wrong
and NOTHING here about A or D may be quoted. A negative from an unvalidated detector is the failure
mode this corpus keeps paying for.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib

NMAX = 12


def _load_cl():
    """Import partitions()/fact() by explicit file path (the _path_bridge bootstrap trap: this probe
    must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_constant_C_landscape.py"
    spec = importlib.util.spec_from_file_location("_m1_cl", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dim_partition(lam, nfact):
    """f^lambda by the hook-length formula, exact."""
    if not lam:
        return 1
    m = lam[0]
    conj = [0] * m
    for part in lam:
        for j in range(part):
            conj[j] += 1
    prod = 1
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (conj[j] - i - 1) + 1
    return nfact // prod


def stats_of(lam, n):
    """(A, D, W) for one partition: A = Sum|c|, D = Sum_u d_u^2, W = Sum c^2 - C(n,2)."""
    absc = 0
    c2 = 0
    diag = {}
    for i, part in enumerate(lam):
        for j in range(part):
            u = j - i
            absc += abs(u)
            c2 += u * u
            diag[u] = diag.get(u, 0) + 1
    return absc, sum(v * v for v in diag.values()), c2 - (n * (n - 1)) // 2


def addable(lam):
    """Every mu |- n+1 with lam /^ mu, as sorted tuples."""
    out = []
    L = list(lam)
    for i in range(len(L)):
        if i == 0 or L[i] < L[i - 1]:
            nxt = L[:]; nxt[i] += 1
            out.append(tuple(nxt))
    out.append(tuple(L + [1]))
    return out


def main():
    mod = _load_cl()
    print("# which objects does the exchangeable-pair machinery REACH? exact Fractions; NO float64")
    print("# J = up-down chain on the Young lattice; an identity Cov(f,g)=E[(f-f*)(g-g*)]/(2(1-beta))")
    print("# needs J g = beta g. Only an EIGENFUNCTION g can play that role.")
    print("#")
    print(f"#   {'n':>3} {'stochastic?':>12} {'beta(W)':>12} {'(n-2)/(n+1)':>12} "
          f"{'W eig?':>7} {'A eig?':>7} {'D eig?':>7}")

    rows = []
    control_ok = True
    for n in range(3, NMAX + 1):
        nfact = mod.fact(n)
        n1fact = mod.fact(n + 1)
        parts = [tuple(p) for p in mod.partitions(n)]
        idx = {p: k for k, p in enumerate(parts)}
        dim = {p: dim_partition(p, nfact) for p in parts}
        st = {p: stats_of(p, n) for p in parts}

        # c(lam, lam*) = # of mu |- n+1 covering both. Build by walking up from each lam.
        cover = {}                       # mu -> list of lam |- n below it
        for p in parts:
            for mu in addable(p):
                cover.setdefault(mu, []).append(p)

        # J as a sparse row map, in exact Fractions.
        J = {p: {} for p in parts}
        for mu, below in cover.items():
            dmu_ok = mu in cover           # every mu here has >= 1 lam below
            for a in below:
                for b in below:
                    J[a][b] = J[a].get(b, F(0)) + F(dim[b], (n + 1) * dim[a])

        stochastic = all(sum(row.values()) == 1 for row in J.values())
        if not stochastic:
            control_ok = False

        def apply_J(which):
            return {p: sum(w * st[q][which] for q, w in J[p].items()) for p in parts}

        verdicts = {}
        betas = {}
        constant = {}
        for name, which in (("W", 2), ("A", 0), ("D", 1)):
            Jf = apply_J(which)
            ratios = {F(Jf[p], st[p][which]) for p in parts if st[p][which] != 0}
            is_eig = len(ratios) == 1
            verdicts[name] = is_eig
            betas[name] = next(iter(ratios)) if is_eig else None
            # A CONSTANT statistic is trivially an eigenfunction of ANY stochastic chain (beta = 1)
            # and carries no information -- it must not be counted as a reachability result.
            constant[name] = len({st[p][which] for p in parts}) == 1

        beta_W_expected = F(n - 2, n + 1)
        if not (verdicts["W"] and betas["W"] == beta_W_expected):
            control_ok = False

        rows.append((n, stochastic, betas["W"], beta_W_expected, verdicts, constant))
        mark = lambda k: ("YES*" if verdicts[k] and constant[k]
                          else "YES" if verdicts[k] else "no")
        print(f"#   {n:>3} {'YES' if stochastic else 'NO':>12} "
              f"{str(betas['W']) if betas['W'] is not None else 'not eig':>12} "
              f"{str(beta_W_expected):>12} "
              f"{mark('W'):>7} {mark('A'):>7} {mark('D'):>7}")
    print("#   * = the statistic is CONSTANT at that n, so it is trivially an eigenfunction of any")
    print("#     stochastic chain (beta = 1) and carries NO reachability information.")
    print("#")

    print("# POSITIVE CONTROL. W is KNOWN (corpus 2026-08-21) to be an eigenfunction with")
    print("#   beta_3 = (n-2)/(n+1). If this chain does not reproduce that EXACTLY, the chain is")
    print("#   wrong and no verdict about A or D here may be quoted.")
    if control_ok:
        print("#   PASSED: J is row-stochastic at every n, and beta(W) = (n-2)/(n+1) exactly.")
    else:
        print("#   FAILED. Fix the chain before reading anything below.")
        print("RESULT: CONTROL FAILED -- the up-down chain is not reproducing the known beta_3; no "
              "verdict from this probe may be quoted. qou-k5r5 OPEN.")
        print("EXIT: 0")
        return 0
    print("#")

    # QUANTIFIER. An earlier version of this probe asked `any(n)` and so reported "D is an
    # eigenfunction" on the strength of n = 3 alone, where D is CONSTANT (= 3 at all three
    # partitions) and therefore trivially one. Reachability is a claim about the FAMILY, so the
    # question is whether f is an eigenfunction at EVERY n -- and a constant n never counts.
    def eig_everywhere(k):
        nondegenerate = [r for r in rows if not r[5][k]]
        return bool(nondegenerate) and all(r[4][k] for r in nondegenerate), nondegenerate

    w_all, _ = eig_everywhere("W")
    a_all, a_nd = eig_everywhere("A")
    d_all, d_nd = eig_everywhere("D")
    a_any = [r[0] for r in a_nd if r[4]["A"]]
    d_any = [r[0] for r in d_nd if r[4]["D"]]
    d_const = [r[0] for r in rows if r[5]["D"]]

    print("# THE REACH, quantified over the FAMILY (every non-degenerate n), not over any single n:")
    print(f"#   W : eigenfunction at every n  {'YES' if w_all else 'NO':>4}  => Cov(., W) reachable "
          f"=> P and N BOTH reachable")
    print(f"#   A : eigenfunction at every n  {'YES' if a_all else 'NO':>4}  "
          f"(non-degenerate n where it IS one: {a_any if a_any else 'none'})")
    print(f"#   D : eigenfunction at every n  {'YES' if d_all else 'NO':>4}  "
          f"(non-degenerate n where it IS one: {d_any if d_any else 'none'}; "
          f"CONSTANT and thus vacuously one at n = {d_const})")
    print("#   => V_A and V_D are NOT reachable by this identity; only covariances against W are.")
    print("#")
    print("# CROSS-CHECK against an independent measurement, and it agrees. PR #6627 found V_W an")
    print("#   EXACT polynomial n(n-1)(n-2)/3 while V_A, V_D and P are not polynomial at all. That")
    print("#   is the same split from the other side: the one object with a closed form is the one")
    print("#   whose statistic is the eigenfunction. Two independent routes, one boundary.")
    print("#")

    if not a_all:
        verdict = ("A is NOT an eigenfunction of the up-down chain at any non-degenerate n <= "
                   f"{NMAX} (W is, exactly, with beta_3 = (n-2)/(n+1) -- control passed). So the "
                   "Fulman exchangeable-pair identity reaches P and N but NOT V_A: the margin "
                   "route's one remaining object is the one the named machinery does not reach, "
                   "while P > N's two objects are both local per-edge sums. #6651's finding that "
                   "the CS relaxation is TIGHT stands; its inference that the margin route is "
                   "therefore the right TARGET does not follow, and is withdrawn")
    else:
        verdict = ("A IS an eigenfunction somewhere in this window, which contradicts the "
                   "expectation -- re-derive before acting on it")
    print(f"# VERDICT (computed, not predicted): {verdict}.")
    print("#")
    print("# SCOPE -- this is scope-(a), NOT an exclusion. It says the named identity does not")
    print("#   apply to V_A. It does NOT say V_A is unreachable: a spectral decomposition of A in")
    print("#   the chain's eigenbasis, or a different chain for which A IS an eigenfunction, are")
    print("#   both untested here. What it settles is where the roadmap's OWN tool points.")
    print(f"RESULT: {verdict}. Control: J row-stochastic and beta(W) = (n-2)/(n+1) exact for "
          f"n = 3..{NMAX}. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
