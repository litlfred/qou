"""S2/S3/S5 of PREREG.md: colour on an octonion-derived strand, exact over Z[q, q^-1].

S2  Furey strand C^8 = 1 + 3 + 3bar + 1 (minimal left ideal of Cl(6) = C (x) O left mult.),
    Jimbo U_q(gl_8) braiding, colour U_q(sl_3) acting on 3 + 3bar.
S5  Oriented colour strand: V = C^3 (quark) and V* (antiquark = reversed orientation), mixed
    crossing R_{V,V*} = (id (x) t)(R^-1), colour = genuine U_q(gl_3) coproduct.

All arithmetic is exact Laurent polynomials with Fraction coefficients (lalg.py). No floats.
Pass/fail criteria are those of PREREG.md (commits abcdfc76382, 3864c1f5b69).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lalg import M, L, lc, ladd, lmul, lstr, leval, H
from fractions import Fraction as Fr

OUT = {}
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"check": name, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))


def jimbo_R(N):
    """Unflipped Jimbo R on C^N (x) C^N and flipped Rcheck = P R."""
    d = {}
    for i in range(N):
        for j in range(N):
            a = i * N + j
            if i == j:
                d[(a, a)] = lc(1, 1)
            else:
                d[(a, a)] = lc(1)
    for i in range(N):
        for j in range(i + 1, N):
            # (q - q^-1) e_ij (x) e_ji
            d[(i * N + j, j * N + i)] = ladd(d.get((i * N + j, j * N + i), {}), H)
    R = M(N * N, d)
    P = M(N * N, {(j * N + i, i * N + j): lc(1) for i in range(N) for j in range(N)})
    return R, P


def Kdiag(N, wts):
    return M(N, {(i, i): lc(1, wts[i]) for i in range(N) if True})


# ---------------------------------------------------------------- S2: Furey strand
def furey(order):
    """order: list of block names; blocks '1','3','3b','1p' with sizes 1,3,3,1."""
    sizes = {'1': 1, '3': 3, '3b': 3, '1p': 1}
    idx = {}
    k = 0
    for b in order:
        idx[b] = list(range(k, k + sizes[b]))
        k += sizes[b]
    N = k
    I = M.eye(N)
    R, P = jimbo_R(N)
    Rc = P @ R
    res = {"order": order, "N": N}
    # Q2a Hecke + braid
    q_ = lc(1, 1); qi = lc(1, -1)
    hecke = (Rc - M.eye(N * N).scale(q_)) @ (Rc + M.eye(N * N).scale(qi))
    check(f"S2[{order}] Q2a Hecke (R-q)(R+q^-1)=0", hecke.is_zero())
    R1 = Rc.kron(I); R2 = I.kron(Rc)
    check(f"S2[{order}] Q2a braid relation on (C^{N})^3", (R1 @ R2 @ R1) == (R2 @ R1 @ R2))
    # colour U_q(sl3) generators on C^8: 3 block = fundamental, 3b block = fundamental o theta
    # fundamental of sl3: E1 = e01, E2 = e12 ; K1 = diag(q, q^-1, 1), K2 = diag(1, q, q^-1)
    def fund(b, gen):
        i0, i1, i2 = idx[b]
        if gen == 'E1': return M.e(N, i0, i1)
        if gen == 'E2': return M.e(N, i1, i2)
        if gen == 'F1': return M.e(N, i1, i0)
        if gen == 'F2': return M.e(N, i2, i1)
        w = {'K1': (1, -1, 0), 'K2': (0, 1, -1)}[gen]
        return M(N, {(i0, i0): lc(1, w[0]), (i1, i1): lc(1, w[1]), (i2, i2): lc(1, w[2])})
    theta = {'E1': 'E2', 'E2': 'E1', 'F1': 'F2', 'F2': 'F1', 'K1': 'K2', 'K2': 'K1'}
    def ones_on_singlets():
        return M(N, {(i, i): lc(1) for b in ('1', '1p') for i in idx[b]})
    col = {}
    for g in ('E1', 'E2', 'F1', 'F2'):
        col[g] = fund('3', g) + fund('3b', theta[g])
    for g in ('K1', 'K2'):
        col[g] = fund('3', g) + fund('3b', theta[g]) + ones_on_singlets()
    Kinv = {g: M(N, {k: lc(1, -list(v.keys())[0]) for k, v in col[g].d.items()}) for g in ('K1', 'K2')}
    # Q2b U_q(sl3) relations on C^8
    hq = M.eye(N).scale(H)
    ok = True
    A = {('1', '1'): 2, ('2', '2'): 2, ('1', '2'): -1, ('2', '1'): -1}
    for i in ('1', '2'):
        Ki, Ei, Fi = col['K' + i], col['E' + i], col['F' + i]
        # [E,F] (q-q^-1) = K - K^-1
        if not (((Ei @ Fi) - (Fi @ Ei)).scale(H) == (Ki - Kinv['K' + i])):
            ok = False
        for j in ('1', '2'):
            Ej, Fj = col['E' + j], col['F' + j]
            a = A[(i, j)]
            if not ((Ki @ Ej) == (Ej @ Ki).scale(lc(1, a))): ok = False
            if not ((Ki @ Fj) == (Fj @ Ki).scale(lc(1, -a))): ok = False
            if i != j:
                # q-Serre: E_i^2 E_j - [2] E_i E_j E_i + E_j E_i^2 = 0
                two = L({1: 1, -1: 1})
                s = (Ei @ Ei @ Ej) - (Ei @ Ej @ Ei).scale(two) + (Ej @ Ei @ Ei)
                if not s.is_zero(): ok = False
                Fi_ = col['F' + i]
                s = (Fi_ @ Fi_ @ Fj) - (Fi_ @ Fj @ Fi_).scale(two) + (Fj @ Fi_ @ Fi_)
                if not s.is_zero(): ok = False
        if i == '1' and not ((col['E1'] @ col['F2']) == (col['F2'] @ col['E1'])): ok = False
    check(f"S2[{order}] Q2b U_q(sl3) relations on C^8", ok)
    # weights (sl3 Cartan eigen-exponents per basis vector)
    wts = [(list(col['K1'].d[(v, v)].keys())[0], list(col['K2'].d[(v, v)].keys())[0]) for v in range(N)]
    res["weights_(K1,K2)_exponents"] = {b: [wts[v] for v in idx[b]] for b in order}
    # Q2c-Levi: gl8 Levi elements (block-separate) commute with Rc under gl8 coproduct
    # gl_N Chevalley on C^N: E_i = e_{i,i+1}, Kgl_i = q^{e_ii} ; coproduct conventions tested
    def coprods(E, K, Kinv_):
        return {
            "E(x)K+1(x)E": E.kron(K) + I.kron(E),
            "E(x)1+K(x)E": E.kron(I) + K.kron(E),
            "E(x)K^-1+1(x)E": E.kron(Kinv_) + I.kron(E),
            "E(x)1+K^-1(x)E": E.kron(I) + Kinv_.kron(E),
        }
    # find the gl_N coproduct convention under which Jimbo Rc is an intertwiner
    conv_ok = {}
    for i in range(N - 1):
        E = M.e(N, i, i + 1)
        w = [0] * N; w[i] = 1; w[i + 1] = -1
        K = Kdiag(N, w); Ki_ = Kdiag(N, [-x for x in w])
        for name, D in coprods(E, K, Ki_).items():
            conv_ok.setdefault(name, True)
            if not ((Rc @ D) == (D @ Rc)): conv_ok[name] = False
    good = [k for k, v in conv_ok.items() if v]
    check(f"S2[{order}] gl_N coproduct convention for Jimbo Rc identified", len(good) >= 1, str(good))
    conv = good[0] if good else None
    res["glN_coproduct_convention"] = conv
    # Levi control: each colour block's E as a gl_N element, with its own gl K
    lev_ok = True
    for b in ('3', '3b'):
        for g in ('E1', 'E2'):
            E = fund(b, g)
            (r, c), = E.d.keys()
            w = [0] * N; w[r] = 1; w[c] = -1
            K = Kdiag(N, w); Ki_ = Kdiag(N, [-x for x in w])
            D = coprods(E, K, Ki_)[conv]
            if not ((Rc @ D) == (D @ Rc)): lev_ok = False
    check(f"S2[{order}] Q2c-Levi: block-separate gl3 x gl3 colour commutes with Rc", lev_ok)
    # Q2c-diag: one U_q(sl3) through its own coproduct, K acting on both blocks
    diag = {}
    for cname in ("E(x)K+1(x)E", "E(x)1+K(x)E", "E(x)K^-1+1(x)E", "E(x)1+K^-1(x)E"):
        allc = True; entries = set()
        for i in ('1', '2'):
            D = coprods(col['E' + i], col['K' + i], Kinv['K' + i])[cname]
            C = (Rc @ D) - (D @ Rc)
            if not C.is_zero():
                allc = False
                for v in C.nonzero().values():
                    entries.add(lstr(v))
        diag[cname] = {"commutes": allc, "distinct_commutator_entries": sorted(entries)}
    res["Q2c_diag"] = diag
    anyc = any(v["commutes"] for v in diag.values())
    check(f"S2[{order}] Q2c-diag: ONE U_q(sl3) on 3+3bar commutes with Jimbo Rc at generic q", anyc,
          "; ".join(f"{k}: {v['distinct_commutator_entries']}" for k, v in diag.items()))
    # Q2c-diag at q = 1 (classical)
    q1 = all(leval(v, 1) == 0 for cn in diag for e in [] for v in [])
    # evaluate commutator at q=1 directly for the identified convention
    D = coprods(col['E1'], col['K1'], Kinv['K1'])[conv]
    C = (Rc @ D) - (D @ Rc)
    res["Q2c_diag_commutator_vanishes_at_q=1"] = all(leval(v, 1) == 0 for v in C.d.values())
    res["Q2c_diag_commutator_vanishes_at_q=-1"] = all(leval(v, -1) == 0 for v in C.d.values())
    # Q2e Markov twists: support T, d_k = z q^{-(2k-1)}, z = q^r/[r]; verify Ocneanu condition
    # and Levi-colour invariance of the twisted trace on n = 1, 2
    return res, Rc, idx, col, N


def markov_twist_check(Rc, N, support):
    """Return (ok, z) where D on support with d_k = q^{r-2k+1}/[r] (k = 1..r, increasing index),
    ok iff (id (x) Tr_D)(Rc) = z * Id on the support lines. Exact over Q(q): we clear [r] by
    working with D' = [r] D and z' = [r] z = q^r."""
    r = len(support)
    dprime = {s: lc(1, r - 2 * k + 1) for k, s in enumerate(sorted(support), start=1)}
    zprime = lc(1, r)
    ok = True
    for i in support:
        acc = {}
        for j in support:
            v = Rc.d.get((i * N + j, i * N + j), {})
            acc = ladd(acc, lmul(v, dprime[j]))
        if acc != zprime:
            ok = False
    # normalisation: sum dprime = [r]  <=>  tr(1) = 1
    s = {}
    for v in dprime.values():
        s = ladd(s, v)
    rint = L({r - 1 - 2 * k: 1 for k in range(r)})
    return ok and s == rint, dprime


def colour_invariant_trace(Rc, N, support, col, idx, dprime):
    """Ad-invariance of the twisted trace Tr(D^{(x)n} X) under the Levi colour U_q(gl3) of each
    block, for n = 1 and n = 2, with the gl_N coproduct Delta E = E(x)K + 1(x)E,
    Delta F = F(x)1 + K^-1(x)F (the convention found to commute with Jimbo Rc):
       E:  Delta(K^-1) D Delta(E) - Delta(E) Delta(K^-1) D = 0
       F:  D Delta(F) - Delta(K) Delta(F) D Delta(K^-1) = 0
    (from sum S(x2) D x1 = eps(x) D, S(E) = -E K^-1, S(F) = -K F)."""
    D = M(N, {(s, s): v for s, v in dprime.items()})
    I = M.eye(N)
    ok = True
    for b in ('3', '3b'):
        i0, i1, i2 = idx[b]
        for (a, c) in ((i0, i1), (i1, i2)):
            E = M.e(N, a, c); F = M.e(N, c, a)
            w = [0] * N; w[a] = 1; w[c] = -1
            K = Kdiag(N, w); Ki = Kdiag(N, [-x for x in w])
            for n in (1, 2):
                if n == 1:
                    DD, DE, DF, DK, DKi = D, E, F, K, Ki
                else:
                    DD = D.kron(D); DE = E.kron(K) + I.kron(E); DF = F.kron(I) + Ki.kron(F)
                    DK = K.kron(K); DKi = Ki.kron(Ki)
                if not ((DKi @ DD @ DE) == (DE @ DKi @ DD)): ok = False
                if not ((DD @ DF) == (DK @ DF @ DD @ DKi)): ok = False
    return ok


def run_S2():
    allres = {}
    for order in (['1', '3', '3b', '1p'], ['3', '1', '3b', '1p']):
        res, Rc, idx, col, N = furey(order)
        # Q2e: classify twists invariant under Levi colour, among supports = unions of blocks
        blocks = list(idx.keys())
        fam = []
        import itertools
        for rr in range(1, len(blocks) + 1):
            for sub in itertools.combinations(blocks, rr):
                supp = sorted(i for b in sub for i in idx[b])
                ok, dprime = markov_twist_check(Rc, N, supp)
                inv = colour_invariant_trace(Rc, N, supp, col, idx, dprime)
                fam.append({"blocks": list(sub), "rank": len(supp), "markov": ok,
                            "levi_colour_invariant_n1": inv,
                            "z": f"q^{len(supp)}/[{len(supp)}]_q"})
        # partial-block supports are never colour invariant (spot check: one line of the 3 block)
        supp = [idx['3'][0], idx['1'][0]]
        ok, dprime = markov_twist_check(Rc, N, supp)
        inv = colour_invariant_trace(Rc, N, supp, col, idx, dprime)
        res["partial_block_twist_example"] = {"support": supp, "markov": ok, "colour_invariant": inv}
        res["Q2e_block_union_twists"] = fam
        zD = [f["blocks"] for f in fam if f["rank"] == 2 and f["markov"] and f["levi_colour_invariant_n1"]]
        res["Q2e_colour_invariant_twists_with_z_D"] = zD
        check(f"S2[{order}] Q2e all block-union twists Markov", all(f["markov"] for f in fam))
        check(f"S2[{order}] Q2e block-union twists Levi-colour invariant",
              all(f["levi_colour_invariant_n1"] for f in fam))
        check(f"S2[{order}] Q2e partial-block twist NOT colour invariant", not inv)
        allres["/".join(order)] = res
        # Q2f: photon letters on (C^N)^3 commute with Levi colour Delta^(3) (one block, E1)
        if order[0] == '1':
            I = M.eye(N)
            s0 = Rc.kron(I); s1 = I.kron(Rc)
            # s1^-1 = s1 - (q - q^-1)
            s1inv = s1 - M.eye(N ** 3).scale(H)
            w = s0 @ s1inv
            i0, i1, _ = idx['3']
            E = M.e(N, i0, i1)
            wv = [0] * N; wv[i0] = 1; wv[i1] = -1
            K = Kdiag(N, wv)
            conv = res["glN_coproduct_convention"]
            # Delta^(3) for convention
            if conv == "E(x)K+1(x)E":
                D3 = E.kron(K).kron(K) + I.kron(E).kron(K) + I.kron(I).kron(E)
            elif conv == "E(x)1+K(x)E":
                D3 = E.kron(I).kron(I) + K.kron(E).kron(I) + K.kron(K).kron(E)
            else:
                Ki = Kdiag(N, [-x for x in wv])
                if conv == "E(x)K^-1+1(x)E":
                    D3 = E.kron(Ki).kron(Ki) + I.kron(E).kron(Ki) + I.kron(I).kron(E)
                else:
                    D3 = E.kron(I).kron(I) + Ki.kron(E).kron(I) + Ki.kron(Ki).kron(E)
            ok = ((w @ D3) == (D3 @ w)) and ((s0 @ D3) == (D3 @ s0)) and ((s1 @ D3) == (D3 @ s1))
            check("S2 Q2f photon letters s0, s1, s0 s1^-1 commute with colour (Levi E) on (C^8)^3", ok)
            res["Q2f_photon_letters_colour_neutral"] = ok
    OUT["S2"] = allres


# ---------------------------------------------------------------- S5: oriented colour strand
def run_S5():
    N = 3
    R, P = jimbo_R(N)
    I = M.eye(N)
    # R^{-1}: Jimbo R(q)^{-1} = sum q^-1 e_ii(x)e_ii + sum_{i!=j} e_ii (x) e_jj - h sum_{i<j} e_ij (x) e_ji
    d = {}
    for i in range(N):
        for j in range(N):
            a = i * N + j
            d[(a, a)] = lc(1, -1) if i == j else lc(1)
    for i in range(N):
        for j in range(i + 1, N):
            d[(i * N + j, j * N + i)] = ladd(d.get((i * N + j, j * N + i), {}), H, -1)
    Rinv = M(N * N, d)
    check("S5 R R^-1 = 1", (R @ Rinv) == M.eye(N * N))
    # partial transpose in 2nd factor
    def pt2(X):
        dd = {}
        for (r, c), v in X.d.items():
            i, j = divmod(r, N); k, l = divmod(c, N)
            dd[(i * N + l, k * N + j)] = v
        return M(N * N, dd)
    def pt1(X):
        dd = {}
        for (r, c), v in X.d.items():
            i, j = divmod(r, N); k, l = divmod(c, N)
            dd[(k * N + j, i * N + l)] = v
        return M(N * N, dd)
    # identify coproduct convention for Rc on V (x) V
    Rc = P @ R
    convs = {}
    for i in range(N - 1):
        E = M.e(N, i, i + 1); w = [0] * N; w[i] = 1; w[i + 1] = -1
        K = Kdiag(N, w); Ki = Kdiag(N, [-x for x in w])
        F = M.e(N, i + 1, i)
        cands = {"A": (E.kron(K) + I.kron(E), F.kron(I) + Ki.kron(F)),
                 "B": (E.kron(I) + K.kron(E), F.kron(Ki) + I.kron(F))}
        for nm, (DE, DF) in cands.items():
            convs.setdefault(nm, True)
            if not ((Rc @ DE) == (DE @ Rc) and (Rc @ DF) == (DF @ Rc)):
                convs[nm] = False
    good = [k for k, v in convs.items() if v]
    check("S5 U_q(gl3) coproduct convention with Jimbo Rc", len(good) >= 1, str(good))
    cv = good[0]
    # dual rep: pi*(x) = pi(S(x))^T. Convention A: Delta E = E(x)K + 1(x)E => S(E) = -E K^-1;
    # Delta F = F(x)1 + K^-1(x)F => S(F) = -K F. Convention B: Delta E = E(x)1+K(x)E => S(E) = -K^-1 E;
    # Delta F = F (x) K^-1 + 1 (x) F => S(F) = -F K.
    def dual(i):
        E = M.e(N, i, i + 1); F = M.e(N, i + 1, i); w = [0] * N; w[i] = 1; w[i + 1] = -1
        K = Kdiag(N, w); Ki = Kdiag(N, [-x for x in w])
        m1 = lc(-1)
        if cv == "A":
            SE = (E @ Ki).scale(m1); SF = (K @ F).scale(m1)
        else:
            SE = (Ki @ E).scale(m1); SF = (F @ K).scale(m1)
        return (E, F, K, Ki), (SE.T(), SF.T(), Ki.T(), K.T())
    # Mixed crossings. Left dual V* (pi*(x) = pi(S x)^T). The 2-dim intertwiner spaces do not
    # pin them, so they are taken in the standard form and the content is in Q5b/Q5c:
    #   c_{V*,V} = P (t (x) id)(R^-1)                         [(S (x) id) R = R^-1]
    #   c_{V,V*} = (K2r^-1 (x) 1) P (id (x) t)(R^-1) (1 (x) K2r),  K2r = diag(q^2, 1, q^-2)
    # (the second is the right-dual formula moved to the left dual by the S^2-implementer K_{2rho}).
    K2r = Kdiag(N, [2, 0, -2]); K2ri = Kdiag(N, [-2, 0, 2])
    RcVsV = P @ pt1(Rinv)
    RcVVs = (K2ri.kron(I)) @ (P @ pt2(Rinv)) @ (I.kron(K2r))
    # Q5a: intertwining. coproduct on V (x) V*: Delta(x) acts as (pi (x) pi*) Delta(x)
    def Dlt(a, b, i):
        (E, F, K, Ki), (Es, Fs, Ks, Kis) = dual(i)
        reps = {'V': (E, F, K, Ki), 'S': (Es, Fs, Ks, Kis)}
        Ea, Fa, Ka, Kia = reps[a]; Eb, Fb, Kb, Kib = reps[b]
        if cv == "A":
            return Ea.kron(Kb) + I.kron(Eb), Fa.kron(I) + Kia.kron(Fb), Ka.kron(Kb)
        return Ea.kron(I) + Ka.kron(Eb), Fa.kron(Kib) + I.kron(Fb), Ka.kron(Kb)
    ok = True
    for i in range(N - 1):
        DVS = Dlt('V', 'S', i); DSV = Dlt('S', 'V', i); DSS = Dlt('S', 'S', i)
        for X, Y in zip(DVS, DSV):
            if not ((RcVVs @ X) == (Y @ RcVVs)): ok = False
        for X, Y in zip(DSV, DVS):
            if not ((RcVsV @ X) == (Y @ RcVsV)): ok = False
    check("S5 Q5a mixed crossings intertwine the genuine U_q(gl3) coproduct (colour moves with strand)", ok)
    # dual rep relations sanity: [E*,F*](q-q^-1) = K* - K*^-1
    ok2 = True
    for i in range(N - 1):
        _, (Es, Fs, Ks, Kis) = dual(i)
        if not (((Es @ Fs) - (Fs @ Es)).scale(H) == (Ks - Kis)): ok2 = False
    check("S5 dual (antiquark) strand is a U_q(sl3) rep", ok2)
    # Q5b: mixed YBE on V (x) V* (x) V:  (R_{V*V} x 1)(1 x R_{V V})... use the general form
    # on X(x)Y(x)Z: (c_{YZ} x 1)(1 x c_{XZ})(c_{XY} x 1) = (1 x c_{XY})(c_{XZ} x 1)(1 x c_{YZ})
    C = {('V', 'V'): Rc, ('V', 'S'): RcVVs, ('S', 'V'): RcVsV}
    def ybe(X, Y, Z):
        a = C[(Y, Z)].kron(I) @ I.kron(C[(X, Z)]) @ C[(X, Y)].kron(I)
        b = I.kron(C[(X, Y)]) @ C[(X, Z)].kron(I) @ I.kron(C[(Y, Z)])
        return a == b
    ok3 = ybe('V', 'S', 'V') and ybe('S', 'V', 'V') and ybe('V', 'V', 'S')
    check("S5 Q5b mixed Yang-Baxter on VV*V, V*VV, VVV*", ok3)
    # Q5c monodromy on V (x) V*: M = c_{V*,V} c_{V,V*}
    Mono = RcVsV @ RcVVs
    # q-contraction: coev/ev with K_{2rho}; e = coev o ev on V (x) V*. Use the projector found
    # as the 1-dim image of (Mono - lambda_8): find eigenvalues via minimal polynomial test.
    # Candidate eigenvalues from Drinfeld: on 1: q^{-2c(V)}, on 8: q^{c(8)-2c(V)}; we test
    # (Mono - a)(Mono - b) = 0 for a, b among q^k, k in -8..8.
    found = []
    Id = M.eye(N * N)
    cands = [(sg, k) for sg in (1, -1) for k in range(-8, 9)]
    for ia, (sa, ka) in enumerate(cands):
        for (sb, kb) in cands[ia + 1:]:
            X = (Mono - Id.scale(lc(sa, ka))) @ (Mono - Id.scale(lc(sb, kb)))
            if X.is_zero():
                found.append(((sa, ka), (sb, kb)))
    check("S5 Q5c monodromy on V(x)V* has a degree-2 minimal polynomial (q^a, q^b)", len(found) == 1, str(found))
    res = {"coproduct_convention": cv, "monodromy_eigen_exponents": found}
    if found:
        (sa, ka), (sb, kb) = found[0]
        Pa = (Mono - Id.scale(lc(sb, kb)))
        qv = 2
        tr_num = sum(leval(Pa.d.get((i, i), {}), qv) for i in range(N * N))
        den = leval(lc(sa, ka), qv) - leval(lc(sb, kb), qv)
        mult_a = tr_num / den
        res["eigenvalue_a"] = f"{sa}*q^{ka}"; res["mult_a"] = str(mult_a)
        res["eigenvalue_b"] = f"{sb}*q^{kb}"; res["mult_b"] = str(N * N - mult_a)
        res["octet_projector"] = "P8 = (M - lambda_1)/(lambda_8 - lambda_1), lambda_8 the eigenvalue of multiplicity 8"
    # Q5d: Rc (photon letters' building block) is colour-neutral: covered by convention search
    res["Q5d_photon_letters_colour_neutral"] = True
    OUT["S5"] = res


# ---------------------------------------------------------------- S4: Bring handles
def run_S4():
    import itertools
    pts = list(itertools.permutations(range(5)))
    def mul(a, b): return tuple(a[b[i]] for i in range(5))
    def inv(a):
        r = [0] * 5
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    def order(a):
        e = tuple(range(5)); k = 1; x = a
        while x != e: x = mul(x, a); k += 1
        return k
    def ctype(a):
        seen = set(); t = []
        for i in range(5):
            if i in seen: continue
            j = i; L_ = 0
            while j not in seen: seen.add(j); j = a[j]; L_ += 1
            t.append(L_)
        return tuple(sorted(t, reverse=True))
    def sign(a):
        return (-1) ** sum(1 for c in ctype(a) for _ in range(c - 1))
    G = pts
    # signature (2,4,5) generating vector: x transposition, y 4-cycle, x y z = 1, z 5-cycle
    gen = None
    for x in G:
        if ctype(x) != (2, 1, 1, 1): continue
        for y in G:
            if ctype(y) != (4, 1):
                continue
            z = inv(mul(x, y))
            if ctype(z) == (5,):
                # generation check
                S = {tuple(range(5))}; frontier = list(S)
                while frontier:
                    nf = []
                    for s in frontier:
                        for g in (x, y):
                            t = mul(s, g)
                            if t not in S: S.add(t); nf.append(t)
                    frontier = nf
                if len(S) == 120:
                    gen = (x, y, z); break
        if gen: break
    x, y, z = gen
    # Riemann-Hurwitz: 2g-2 = 120(-2 + (1-1/2)+(1-1/4)+(1-1/5)) -> g
    from fractions import Fraction as F
    g = (120 * (-2 + F(1, 2) + F(3, 4) + F(4, 5)) + 2) / 2
    check("S4 Riemann-Hurwitz genus of (2,4,5) S5-cover = 4", g == 4, str(g))
    def cyc(c):
        e = tuple(range(5)); s = [e]; t = c
        while t != e: s.append(t); t = mul(t, c)
        return set(s)
    Hs = [cyc(x), cyc(y), cyc(z)]
    def fix(gel):
        # fixed points of gel: sum over branch types of |C_G(g)| |cl(g) cap H| / |H|
        cent = sum(1 for h in G if mul(h, gel) == mul(gel, h))
        cl = {mul(mul(h, gel), inv(h)) for h in G}
        tot = F(0)
        for Hc in Hs:
            tot += F(cent * len(cl & Hc), len(Hc))
        return tot
    classes = {}
    for a in G:
        classes.setdefault(ctype(a), []).append(a)
    chi = {}
    for ct, els in classes.items():
        a = els[0]
        chi[ct] = 8 if ct == (1, 1, 1, 1, 1) else 2 - fix(a)
    # S5 character table (cycle types order)
    order_ct = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
    sizes = {ct: len(classes[ct]) for ct in order_ct}
    table = {
        "triv":  [1, 1, 1, 1, 1, 1, 1],
        "sgn":   [1, -1, 1, 1, -1, -1, 1],
        "std4":  [4, 2, 0, 1, -1, 0, -1],
        "std4s": [4, -2, 0, 1, 1, 0, -1],
        "5":     [5, 1, 1, -1, 1, -1, 0],
        "5s":    [5, -1, 1, -1, -1, 1, 0],
        "6":     [6, 0, -2, 0, 0, 0, 1],
    }
    mults = {}
    for nm, row in table.items():
        s = sum(F(sizes[ct]) * chi[ct] * row[k] for k, ct in enumerate(order_ct)) / 120
        mults[nm] = str(s)
    # A5 restriction: A5 classes (1), (2,2,1), (3,1,1), (5) split into 5a, 5b
    res = {"genus": str(g), "character_H1_by_cycle_type": {str(k): str(v) for k, v in chi.items()},
           "S5_multiplicities": mults}
    # A5 characters: triv, 3a, 3b, 4, 5 on classes 1, (2,2), (3), 5a, 5b ; we need chi on 5a, 5b
    # 5-cycles: H1 character on 5-cycles splits? compute per element.
    fives = classes[(5,)]
    vals = sorted({str(2 - fix(a)) for a in fives})
    res["H1_character_values_on_5cycles"] = vals
    triv_mult = F(mults["triv"])
    res["trivial_multiplicity_S5"] = str(triv_mult)
    # A5 trivial multiplicity
    A5 = [a for a in G if sign(a) == 1]
    tA = sum((F(8) if a == tuple(range(5)) else 2 - fix(a)) for a in A5) / 60
    res["trivial_multiplicity_A5"] = str(tA)
    # A5 3-dim irreps: 3a = (3,-1,0,phi,1-phi), 3b conj; inner products need sqrt5; use that
    # 3a + 3b has character (6,-2,0,1,1) on (1,(2,2),(3),5a,5b), rational. Multiplicity of 3a+3b
    # pieces: <chi, 3a+3b> = m(3a)+m(3b).
    def a5chi(a):
        return F(8) if a == tuple(range(5)) else 2 - fix(a)
    def c33(a):
        ct = ctype(a)
        return {(1,1,1,1,1): 6, (2,2,1): -2, (3,1,1): 0, (5,): 1}[ct]
    m33 = sum(a5chi(a) * c33(a) for a in A5) / 60
    res["A5_multiplicity_3a_plus_3b"] = str(m33)
    def c4(a):
        return {(1,1,1,1,1): 4, (2,2,1): 0, (3,1,1): 1, (5,): -1}[ctype(a)]
    def c5(a):
        return {(1,1,1,1,1): 5, (2,2,1): 1, (3,1,1): -1, (5,): 0}[ctype(a)]
    res["A5_multiplicity_4"] = str(sum(a5chi(a) * c4(a) for a in A5) / 60)
    res["A5_multiplicity_5"] = str(sum(a5chi(a) * c5(a) for a in A5) / 60)
    check("S4 trivial summand in H1(Bring) (needed for an equivariant unit 1 of O or H)",
          triv_mult > 0 or tA > 0, f"S5: {triv_mult}, A5: {tA}")
    check("S4 3-dim A5 summand in H1(Bring) (needed for an equivariant Im H = (i,j,k))",
          m33 > 0, f"m(3a)+m(3b) = {m33}")
    OUT["S4"] = res


if __name__ == "__main__":
    run_S2()
    run_S5()
    run_S4()
    out = {
        "producer": "computations/probes/qcd_octonion_colour_strand/furey_oriented_probe.py",
        "prereg": "computations/probes/qcd_octonion_colour_strand/PREREG.md",
        "arithmetic": "exact Laurent polynomials over Q (fractions.Fraction); no floats",
        "q0Anchor": "independent",
        "q0AnchorReason": "generic formal q (Laurent polynomials); q0 never read",
        "checks": CHECKS,
        "results": OUT,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "furey-oriented.witness.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"{sum(c['pass'] for c in CHECKS)}/{len(CHECKS)} checks pass (FAIL lines are results, see PREREG)")
