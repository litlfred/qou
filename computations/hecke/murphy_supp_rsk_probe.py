#!/usr/bin/env python3
"""Is the Murphy basis triangular against the T_w basis, with RSK as the leading map?

Exact integer arithmetic throughout (permutations are tuples, Hecke coefficients are
Laurent polynomials in q held as dict{exponent: int}).  No floats appear anywhere, so
the NO-FLOAT64 discipline is satisfied by construction rather than by tolerance.

Background.  `QOU.BraidKnot.SpechtStandardBasis.Triangular` is the corpus's linear-
independence lever: a family `v : ι -> (alpha ->_0 R)` with an injective leading map
`lead`, a unit diagonal coefficient, and support bounded above by `lead`.  Applying it
to the Murphy basis `m_{st} = T_{d(s)}^* x_lambda T_{d(t)}` against the `T_w` basis needs

    lead_inj   -- FREE: RSK is a bijection MurphyIndex n <-> S_n (already Lean-proved)
    diag_unit  -- needs  RSK^{-1}(s,t)  to lie in  supp(m_{st})  at all
    supp_le    -- needs a linear order on S_n with  supp(m_{st}) <= RSK^{-1}(s,t)

`diag_unit` is the cheap necessary condition and is what this probe tests first: if
`RSK^{-1}(s,t)` is not even in the support then `supp_le` is unreachable for that lead.

The probe also reports, for a candidate lead map, whether ANY linear order could work:
that holds iff the digraph  {a -> lead(i) : a in supp(v_i)}  is acyclic.
"""

from itertools import permutations
import sys

# ---------------------------------------------------------------- permutations

def compose(u, v):
    """(u o v)(i) = u(v(i))."""
    return tuple(u[v[i]] for i in range(len(v)))

def inverse(w):
    n = len(w)
    out = [0] * n
    for i, wi in enumerate(w):
        out[wi] = i
    return tuple(out)

def length(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])

def reduced_word(w):
    """A reduced word in the adjacent transpositions, by bubble sort on positions."""
    w = list(w)
    word = []
    n = len(w)
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if w[i] > w[i + 1]:
                w[i], w[i + 1] = w[i + 1], w[i]
                word.append(i)
                changed = True
    # `word` sorts w to the identity by right multiplications; reverse to build w.
    return list(reversed(word))

def right_mul_s(w, i):
    """w * s_i  (swap the values at positions i, i+1)."""
    l = list(w)
    l[i], l[i + 1] = l[i + 1], l[i]
    return tuple(l)

# ------------------------------------------------- Laurent polynomials in q

def poly_add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
        if out[e] == 0:
            del out[e]
    return out

def poly_scale(a, factor):
    out = {}
    for e, c in a.items():
        for fe, fc in factor.items():
            k = e + fe
            out[k] = out.get(k, 0) + c * fc
            if out[k] == 0:
                del out[k]
    return out

ONE = {0: 1}
Q_MINUS_QINV = {1: 1, -1: -1}      # q - q^{-1}

# ------------------------------------------------------------- Hecke algebra
# Corpus convention: sigma_i^2 = (q - q^{-1}) sigma_i + 1, so
#   T_w T_{s_i} = T_{w s_i}                          if l(w s_i) > l(w)
#   T_w T_{s_i} = T_{w s_i} + (q - q^{-1}) T_w       otherwise.

def elt_right_mul_s(elt, i):
    out = {}
    for w, coef in elt.items():
        ws = right_mul_s(w, i)
        if w[i] < w[i + 1]:                       # length goes up
            out[ws] = poly_add(out.get(ws, {}), coef)
        else:
            out[ws] = poly_add(out.get(ws, {}), coef)
            out[w] = poly_add(out.get(w, {}), poly_scale(coef, Q_MINUS_QINV))
    return {w: c for w, c in out.items() if c}

def elt_right_mul_Tw(elt, v):
    for i in reduced_word(v):
        elt = elt_right_mul_s(elt, i)
    return elt

def elt_left_mul_Tw(elt, u):
    """T_u * elt, computed as (elt^* * T_{u^{-1}})^* using the anti-automorphism
    T_w -> T_{w^{-1}}, which is exact on the T-basis and preserves coefficients."""
    star = {inverse(w): c for w, c in elt.items()}
    prod = elt_right_mul_Tw(star, inverse(u))
    return {inverse(w): c for w, c in prod.items()}

# ------------------------------------------------------------------ tableaux

def partitions(n):
    def rec(n, cap):
        if n == 0:
            yield ()
            return
        for k in range(min(n, cap), 0, -1):
            for rest in rec(n - k, k):
                yield (k,) + rest
    return list(rec(n, n))

def row_superstandard(lam):
    """t^lambda: rows filled 1,2,3,... left to right."""
    rows, e = [], 1
    for r in lam:
        rows.append(tuple(range(e, e + r)))
        e += r
    return tuple(rows)

def standard_tableaux(lam):
    n = sum(lam)
    rows = [[] for _ in lam]
    out = []

    def rec(k):
        if k > n:
            out.append(tuple(tuple(r) for r in rows))
            return
        for i in range(len(lam)):
            if len(rows[i]) < lam[i] and (i == 0 or len(rows[i - 1]) > len(rows[i])):
                rows[i].append(k)
                rec(k + 1)
                rows[i].pop()

    rec(1)
    return out

def d_of(t, tlam):
    """The permutation d with t = t^lambda . d, i.e. d(t^lambda(c)) = t(c).
    Returned 0-indexed."""
    n = sum(len(r) for r in tlam)
    p = [0] * n
    for r_lam, r_t in zip(tlam, t):
        for a, b in zip(r_lam, r_t):
            p[a - 1] = b - 1
    return tuple(p)

def row_stabiliser(tlam):
    """S_lambda: the permutations preserving each row's entry set (0-indexed)."""
    blocks = [[e - 1 for e in r] for r in tlam]
    n = sum(len(b) for b in blocks)
    out = []

    def rec(idx, partial):
        if idx == len(blocks):
            out.append(tuple(partial))
            return
        blk = blocks[idx]
        for perm in permutations(blk):
            nxt = list(partial)
            for src, dst in zip(blk, perm):
                nxt[src] = dst
            rec(idx + 1, nxt)

    rec(0, [0] * n)
    return out

# ----------------------------------------------------------------------- RSK

def rsk(w):
    """Row-insert the one-line word w (1-based values); return (P, Q)."""
    P, Q = [], []
    for pos, x in enumerate(w, start=1):
        cur = x
        r = 0
        while True:
            if r == len(P):
                P.append([cur])
                Q.append([pos])
                break
            row = P[r]
            j = None
            for idx, y in enumerate(row):
                if y > cur:
                    j = idx
                    break
            if j is None:
                row.append(cur)
                Q[r].append(pos)
                break
            row[j], cur = cur, row[j]
            r += 1
    return (tuple(tuple(r) for r in P), tuple(tuple(r) for r in Q))

def rsk_inverse_table(n):
    """word (0-indexed perm tuple) keyed by (P, Q)."""
    table = {}
    for w in permutations(range(1, n + 1)):
        P, Q = rsk(w)
        table[(P, Q)] = tuple(x - 1 for x in w)
    return table

# -------------------------------------------------------------------- driver

def murphy_support(lam, s, t):
    tlam = row_superstandard(lam)
    ds, dt = d_of(s, tlam), d_of(t, tlam)
    x_lam = {w: dict(ONE) for w in row_stabiliser(tlam)}
    elt = elt_left_mul_Tw(x_lam, inverse(ds))
    elt = elt_right_mul_Tw(elt, dt)
    return elt, ds, dt

def has_cycle(edges, nodes):
    """edges: dict node -> set of successors.  True iff a directed cycle exists."""
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {v: WHITE for v in nodes}
    for root in nodes:
        if colour[root] != WHITE:
            continue
        stack = [(root, iter(edges.get(root, ())))]
        colour[root] = GREY
        while stack:
            v, it = stack[-1]
            advanced = False
            for u in it:
                if colour[u] == GREY:
                    return True
                if colour[u] == WHITE:
                    colour[u] = GREY
                    stack.append((u, iter(edges.get(u, ()))))
                    advanced = True
                    break
            if not advanced:
                colour[v] = BLACK
                stack.pop()
    return False

def run(n):
    inv = rsk_inverse_table(n)
    total = 0
    diag_ok_PQ = 0
    diag_ok_QP = 0
    first_failure = None
    supports = {}
    for lam in partitions(n):
        syts = standard_tableaux(lam)
        for s in syts:
            for t in syts:
                total += 1
                elt, ds, dt = murphy_support(lam, s, t)
                supp = set(elt.keys())
                supports[(lam, s, t)] = (supp, elt)
                u_pq = inv[(s, t)]
                u_qp = inv[(t, s)]
                if u_pq in supp:
                    diag_ok_PQ += 1
                elif first_failure is None:
                    first_failure = (lam, s, t, u_pq, sorted(supp))
                if u_qp in supp:
                    diag_ok_QP += 1

    print(f"n = {n}:  {total} Murphy indices  ({total} = {n}! ? "
          f"{'yes' if total == __import__('math').factorial(n) else 'NO'})")
    print(f"    RSK^-1(P=s,Q=t) in supp(m_st):  {diag_ok_PQ}/{total}")
    print(f"    RSK^-1(P=t,Q=s) in supp(m_st):  {diag_ok_QP}/{total}")

    for tag, pick in (("P=s,Q=t", lambda s, t: inv[(s, t)]),
                      ("P=t,Q=s", lambda s, t: inv[(t, s)])):
        leads = {}
        bad = False
        for (lam, s, t), (supp, _elt) in supports.items():
            lead = pick(s, t)
            if lead in leads:
                bad = True
            leads[lead] = (lam, s, t)
        if bad:
            print(f"    lead ({tag}) is NOT injective -- skipping order test")
            continue
        edges = {}
        for (lam, s, t), (supp, _elt) in supports.items():
            lead = pick(s, t)
            for a in supp:
                if a != lead:
                    edges.setdefault(a, set()).add(lead)
        nodes = set(permutations(range(n)))
        cyc = has_cycle(edges, nodes)
        print(f"    lead ({tag}) injective; a compatible linear order "
              f"{'CANNOT' if cyc else 'CAN'} exist (digraph "
              f"{'has' if cyc else 'has no'} cycle)")

    if first_failure is not None:
        lam, s, t, u, supp = first_failure
        print(f"    first diag_unit failure (P=s,Q=t): lambda={lam} s={s} t={t}")
        print(f"        RSK^-1 = {u}   supp = {supp}")

    # support sizes, and whether the Bruhat-maximum candidate is unique
    sizes = sorted({len(sp) for sp, _ in supports.values()})
    print(f"    support sizes observed: {sizes}")
    return supports




# ------------------------------------------------- can ANY bijective lead work?
#
# Suppose a linear order `<=` on S_n and a bijection `lead` satisfy the Triangular
# axioms.  Let M be the order's maximum.  For every index j, supp(m_j) <= lead(j), so
# M in supp(m_j) forces lead(j) = M, and `lead` is injective, so M lies in EXACTLY ONE
# support.  Deleting that index and M leaves the same problem one size smaller.  The
# recursion is therefore forced: a valid (order, lead) pair exists iff this peeling
# always finds a permutation lying in exactly one surviving support.

def peel_test(supports, n):
    live = {k: set(sp) for k, (sp, _e) in supports.items()}
    order_from_top = []
    while live:
        counts = {}
        for k, sp in live.items():
            for a in sp:
                counts.setdefault(a, []).append(k)
        singles = [a for a, ks in counts.items() if len(ks) == 1]
        if not singles:
            return False, order_from_top, live, counts
        a = singles[0]
        owner = counts[a][0]
        order_from_top.append((a, owner))
        del live[owner]
    return True, order_from_top, {}, {}


def run_peel(n):
    supports = {}
    for lam in partitions(n):
        syts = standard_tableaux(lam)
        for s in syts:
            for t in syts:
                elt, _ds, _dt = murphy_support(lam, s, t)
                supports[(lam, s, t)] = (set(elt.keys()), elt)
    ok, order_from_top, live, counts = peel_test(supports, n)
    print(f"n = {n}: a bijective Triangular lead (ANY linear order) "
          f"{'EXISTS' if ok else 'DOES NOT EXIST'}")
    if not ok:
        print(f"    peeled {len(order_from_top)} of {len(supports)} indices, then stuck")
        print(f"    {len(live)} indices remain; every surviving permutation lies in "
              f">= 2 of their supports")
        mult = sorted({len(ks) for ks in counts.values()})
        print(f"    surviving multiplicities: {mult}")
        for k in list(live)[:3]:
            print(f"    e.g. index lambda={k[0]} s={k[1]} t={k[2]}  "
                  f"|supp|={len(live[k])}")
    return ok


if __name__ == "__main__":
    for n in (3, 4, 5):
        run(n)
        run_peel(n)
        print()
