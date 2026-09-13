#!/usr/bin/env python3
"""The Cauchy-Schwarz step for `M_1 > 0` is being taken on the WRONG EDGE SET, and fixing it
is free.  Plus an exact identity, and an integrality bound I expect to be cosmetic.

Gap `qou-k5r5`, epic `qou-x631`.  Sequel to PR #6651 (`..._edge_cauchy_schwarz.py`) and
PR #6825 (`..._pq_pointwise_census.py`).  Reuses their edge enumeration; no new chain code.

===============================================================================
THE SETUP, as the corpus has it
===============================================================================

Fulman's exchangeable-pair identity writes both halves of `M_1` over the up-down chain's
edges with one non-negative weight `dmu = pi(lam) J(lam,lam*) (|u|+|v|)`:

    g     = |u| - |v|            = Delta(A),   A = Sum |c|
    2d-2  = 2(d_u - d_v) - 2     = Delta(D),   D = Sum_u d_u^2
    k     = g + 2d - 2           = Delta(Sum h),  since  Sum h = D + A

    P = Sum dmu g^2      N = Sum dmu g(2 - 2d)      Q = Sum dmu (2 - 2d)^2
    M_1 = P - N = Sum dmu g k

Cauchy-Schwarz on that measure gives `N <= sqrt(P Q)`, hence the recorded sufficient
condition **`Q < P  =>  M_1 > 0`**, measured to hold at every `n` in 4..20 with
`P/Q` in [2.231, 2.266].

===============================================================================
FINDING 1 -- the CS step is taken on the wrong edge set, and the fix is free
===============================================================================

**At a `g = 0` edge, `M_1`'s integrand and `P`'s integrand are BOTH identically zero,
while `Q`'s is not.**  `g = 0` means `|u| = |v|` with `u != v`, i.e. `v = -u`: the added
and removed boxes sit on opposite diagonals.  There

    M_1 integrand = g k = 0,    P integrand = g^2 = 0,    Q integrand = (2-2d)^2 >= 0

so those edges load `Q` and nothing else.  Cauchy-Schwarz only ever needed the support of
`g`, and restricting to it is legitimate for exactly that reason:

    M_1 = Sum_{g != 0} dmu g k = P + Sum_{g != 0} dmu g (2-2d)
        >= P - sqrt( P * Q' ),    Q' := Sum_{g != 0} dmu (2-2d)^2  <=  Q

So the live sufficient condition should be **`Q' < P`**, which is strictly weaker than
`Q < P`, and `supp(g)` is the OPTIMAL restriction in this family (CS is insensitive to
any edge where `g = 0`, and no other edge can be dropped without changing `M_1`).

The corpus noticed the family but did not take the restriction.  PR #6825 records:
*"At `g = 0` the `P-Q` integrand is `-(2-2delta)^2 <= 0` for EVERY such edge, while
`M_1`'s `g*k` vanishes identically there. The `|u| = |v|` edges contribute nothing to
`M_1` and carry **11.55 %** of `P-Q`'s negative mass at `n = 20`. Cut out by
`g = 0, delta != 1` -- no inequality to solve."*  That is the same observation, priced
against `P-Q`'s census; the recorded sufficient condition is still stated with the full
`Q`.  This probe measures what the restriction buys.

**MEASURED, and it is FREE but SMALL -- do not read the 11.55 % as this number.**  At
`n = 20` the restriction gives `Q'/Q = 0.9943`, raising `P/Q` from `2.2615` to `2.2743`
(**+0.57 %**) and the CS-certified share of the true margin from `0.8615` to `0.8663`
(+0.0048).  The two figures have DIFFERENT DENOMINATORS and both are right: the `g = 0`
edges are 11.55 % of `P-Q`'s *negative* mass and 0.57 % of `Q`.  So the correct statement
of the live sufficient condition is `Q' < P`, and adopting it costs nothing -- but it
improves headroom by half a percent, not by an order.  It does not change the difficulty
of the open problem, which is still the joint law of `(g, delta)` under Plancherel.

===============================================================================
FINDING 2 -- an exact identity, one line from what is already recorded
===============================================================================

PR #6825 records the factorisation `g^2 - (2-2d)^2 = k(2g - k)`, i.e.
`P - Q = Sum dmu (2 g k - k^2)`.  With `M_1 = Sum dmu g k` that rearranges to

    **2 M_1  =  E_k + (P - Q),      E_k := Sum dmu k^2  =  Sum dmu (Delta Sum h)^2**

an exact identity over the same edge set.  Two readings:

  * `E_k >= 0` trivially, so **`M_1 >= (P - Q)/2` with NO Cauchy-Schwarz at all**.  (The
    CS bound `P - sqrt(PQ)` is the sharper of the two at the measured `P/Q ~ 2.24`:
    `0.332 P` against `0.277 P`.  Reported so the weaker one is not mistaken for a gain.)
  * `E_k` is the exact slack.  It is the Dirichlet energy of `Sum h` under `dmu`.

**It gives no new SUFFICIENT CONDITION by itself** -- substituting
`E_k = P + 2 Sum dmu (Delta A)(Delta D) + Q` turns `E_k > Q - P` back into `M_1 > 0`,
which is circular.  Recorded as an identity, not as a route.

===============================================================================
FINDING 3 -- an integrality bound, and I EXPECT IT TO BE COSMETIC
===============================================================================

`k = g + 2(d_u - d_v) - 2` is an INTEGER, so `k^2 >= 1` wherever `k != 0`:

    E_k >= mu({k != 0}),   hence   2 M_1 >= mu({k != 0}) + (P - Q)

-- so `M_1 > 0` whenever `Q - P < mu({k != 0})`, strictly weaker than `Q < P`.

**Stated prediction, before the measurement, so the reading is not motivated:** I expected
this to be COSMETIC.  Contents run to `O(sqrt n)`, so `|k|` should be typically `O(sqrt n)`
and `E_k` should exceed `mu({k != 0})` by a factor growing like `n` -- making the
relaxation a lower-order correction to an `O(n^{5/2})` quantity.

**🛑 THE PREDICTION IS WRONG, and the measurement is left in place rather than the
prediction quietly deleted.**  `E_k / mu({k != 0})` runs `1.80` at `n = 5` to `4.10` at
`n = 20` -- a global log-log slope of **0.594**, not 1.  The dmu-weighted mean of `k^2`
stays around 4, i.e. `|k| ~ 2`: the increment of `Sum h` along an up-down edge does NOT
inherit the `O(sqrt n)` scale of the contents, because `Delta A` and `Delta D` largely
cancel in `k = Delta A + Delta D`.  So the integrality bound gives away a SUB-LINEAR
factor, and is milder than I claimed.

**But the exponent is NOT pinned and must not be quoted as `sqrt n`.**  The last six local
log-log slopes span `[0.315, 0.788]` -- a factor of 2.5 -- over a window that ends at
`n = 20`.  `0.594` is a measured global slope on a short window, not an asymptotic.

**And it still yields no new route.**  A factor that grows at all means the bound weakens
with `n`, and the condition it buys (`Q - P < mu({k != 0})`) is only useful where `Q > P`,
which is not the measured regime.  Recorded as a corrected measurement, not as a door.

===============================================================================
FINDING 4 -- the DEPTH reading, and it localises the whole difficulty
===============================================================================

In cell coordinates write `b = i + j` (anti-diagonal) and `c = j - i` (content).  Then
`Sum h = Sum_cells b + n`, so `k = Delta b` exactly, and

    **b = |c| + 2 m,   m := min(i, j) >= 0**

-- the cell's DEPTH along its diagonal.  (The corpus already has both halves: `d = m + 1`
in `..._edge_ratio_monotonicity.py:158` and `..._kappa_large_n_sampler.py:100`, and
"a cell on diagonal c at depth k is (k, k+c), so i+j+1 = 2k+c+1" in
`..._kappa_derivation.py:26`.)  Hence `k = g + 2 Delta_m`, and

    **M_1 = Sum dmu g (g + 2 Delta_m) = P + 2 Sum dmu g Delta_m**

Two things follow.  If every cell sat at depth 0 (a hook), `k = g` and `M_1 = P > 0`
TERMWISE -- the entire obstruction is the depth.  And more usefully, on any edge with
`Delta_m = 0` the integrand is `g k = g^2 >= 0` with no inequality to solve, so

    **M_1 = [Sum_{Delta_m = 0} dmu g^2]  +  [Sum_{Delta_m != 0} dmu g k]**

with the first bracket unconditionally non-negative and all negative edges confined to the
second.  `Delta_m = 0` is `delta = 1`, the value PR #6825 already singles out; its
recorded integer criterion independently implies no `delta = 1` edge is negative, so this
is a derivation of a known fact plus its price.

**MEASURED, and it prices the family OUT as a route.**  The unconditional part is
`12.33 %` of `M_1` at `n = 20`, and its share is **DECLINING**: `0.356` (n=8), `0.271`
(n=10), `0.225` (n=12), `0.173` (n=15), `0.123` (n=20).  So the free family shrinks as `n`
grows and cannot carry a large-`n` proof; `87.67 %` of `M_1` sits on depth-changing edges
and is not controlled here.  Reported because a 12 % family whose share is falling is a
decomposition, not a foothold -- and quoting the 12.33 % without the trend would suggest
otherwise.

===============================================================================
SCOPE -- read before citing
===============================================================================

Sufficient is never necessary: a failure of `Q' < P` would say nothing about `M_1 > 0`.
Window `n <= 20` against a requirement of `n >= 79`; **nothing here is a bound over all
`n`**, and none of the three findings closes the gap.  Finding 1 improves the HEADROOM of
the live route; it does not remove the need for the joint law of `(g, delta)` under
Plancherel, which is what both routes still want.  `qou-k5r5` stays OPEN.

NO FLOAT64: exact `Fraction`/`int` throughout; mpmath only for square roots and display.
"""
import importlib.util
import pathlib
import sys
from fractions import Fraction as F

import mpmath as mp

mp.mp.dps = 40
NMAX = 20


def _load_reach():
    """Chain helpers from the sibling reach probe, by explicit file path (the `_path_bridge`
    bootstrap trap: this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_eigenfunction_reach.py"
    spec = importlib.util.spec_from_file_location("_m1_reach", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cells(lam):
    return {(i, j) for i, part in enumerate(lam) for j in range(part)}


def diag_lengths(lam):
    d = {}
    for i, part in enumerate(lam):
        for j in range(part):
            d[j - i] = d.get(j - i, 0) + 1
    return d


def show(fr, digits=6):
    return mp.nstr(mp.mpf(fr.numerator) / mp.mpf(fr.denominator), digits)


def main():
    reach = _load_reach()
    cl = reach._load_cl()

    ctrl_identity = True        # 2 M_1 == E_k + P - Q, exactly
    ctrl_m1 = True              # edge M_1 == Cov(A,W) + Cov(D,W), independent yardstick
    ctrl_P = True               # edge P == Cov(A,W)
    ctrl_integrality = True     # E_k >= mu(k != 0)
    ctrl_g0 = True              # g = 0 edges contribute 0 to both M_1 and P
    ctrl_depth = True           # Delta_m = 0 family is termwise >= 0 and the split is exact

    rows = []
    for n in range(4, NMAX + 1):
        nfact = cl.fact(n)
        parts = [tuple(p) for p in cl.partitions(n)]
        dim = {p: reach.dim_partition(p, nfact) for p in parts}
        st = {p: reach.stats_of(p, n) for p in parts}
        pi = {p: F(dim[p] * dim[p], nfact) for p in parts}
        dl = {p: diag_lengths(p) for p in parts}
        cs_ = {p: cells(p) for p in parts}

        cover = {}
        for p in parts:
            for mu in reach.addable(p):
                cover.setdefault(mu, []).append(p)
        J = {p: {} for p in parts}
        for mu, below in cover.items():
            for a in below:
                for b in below:
                    J[a][b] = J[a].get(b, F(0)) + F(dim[b], (n + 1) * dim[a])

        # --- independent Plancherel yardstick (no edges) ---
        EA = sum(pi[p] * st[p][0] for p in parts)
        ED = sum(pi[p] * st[p][1] for p in parts)
        EW = sum(pi[p] * st[p][2] for p in parts)
        cov_AW = sum(pi[p] * st[p][0] * st[p][2] for p in parts) - EA * EW
        cov_DW = sum(pi[p] * st[p][1] * st[p][2] for p in parts) - ED * EW
        m1_direct = cov_AW + cov_DW

        sum_P = sum_Q = sum_M1 = sum_Ek = F(0)
        sum_Q_supp = F(0)          # Q restricted to supp(g)
        mass_k_nonzero = F(0)      # mu({k != 0})
        g0_M1 = g0_P = F(0)        # control: the g = 0 edges' contribution to M_1 and P
        # FINDING 4: the DEPTH decomposition.  With b = i+j the anti-diagonal coordinate,
        # Sum h = Sum_cells b + n, so k = Delta b; and b = |c| + 2m with m = min(i,j) >= 0 the
        # cell's depth along its diagonal (the corpus already has d = m + 1 and
        # "a cell on diagonal c at depth k is (k, k+c)").  Hence k = g + 2*Delta_m, and on an
        # edge with Delta_m = 0 the M_1 integrand is g*k = g^2 >= 0 TERMWISE.
        m1_dm0 = m1_dmne = F(0)
        dm0_all_nonneg = True

        for a in parts:
            for b, jab in J[a].items():
                if a == b:
                    continue
                only_a = cs_[a] - cs_[b]
                only_b = cs_[b] - cs_[a]
                if len(only_a) != 1 or len(only_b) != 1:
                    continue
                (ia, ja), = only_a
                (ib, jb), = only_b
                u = ja - ia
                v = jb - ib
                d_u = dl[a].get(u, 0)
                d_v = dl[a].get(v, 0)
                g = abs(u) - abs(v)
                delta = d_u - d_v
                m = 2 - 2 * delta                 # = -Delta(D)
                k = g + 2 * delta - 2             # = Delta(Sum h);  note k = g - m

                dmu = pi[a] * jab * (abs(u) + abs(v))

                sum_P += dmu * g * g
                sum_Q += dmu * m * m
                sum_M1 += dmu * g * k
                sum_Ek += dmu * k * k
                if g != 0:
                    sum_Q_supp += dmu * m * m
                else:
                    g0_M1 += dmu * g * k
                    g0_P += dmu * g * g
                if k != 0:
                    mass_k_nonzero += dmu
                # depth decomposition: Delta_m = delta - 1 (since d = m + 1 on both cells,
                # with d_v read before v is added -- see the sign-convention note in the report)
                if delta - 1 == 0:
                    m1_dm0 += dmu * g * k
                    if g * k < 0:
                        dm0_all_nonneg = False      # would falsify k = g on this family
                else:
                    m1_dmne += dmu * g * k

        # The identity's divisor, common to BOTH halves: 2(1 - beta_3) = 6/(n+1).  Taken from
        # the reference probe `..._edge_cauchy_schwarz.py`.  It multiplies P, Q, M_1, E_k and
        # the mass IDENTICALLY, so every ratio below is unaffected by it -- but the equality
        # controls against the Plancherel yardstick are not, and omitting it fails them.
        scale = F(n + 1, 6)
        sum_P *= scale
        sum_Q *= scale
        sum_Q_supp *= scale
        sum_M1 *= scale
        sum_Ek *= scale
        mass_k_nonzero *= scale
        g0_M1 *= scale
        g0_P *= scale
        m1_dm0 *= scale
        m1_dmne *= scale

        # --- controls ---
        if 2 * sum_M1 != sum_Ek + sum_P - sum_Q:
            ctrl_identity = False
        if sum_M1 != m1_direct:
            ctrl_m1 = False
        if sum_P != cov_AW:
            ctrl_P = False
        if sum_Ek < mass_k_nonzero:
            ctrl_integrality = False
        if g0_M1 != 0 or g0_P != 0:
            ctrl_g0 = False
        if m1_dm0 + m1_dmne != sum_M1 or not dm0_all_nonneg or m1_dm0 < 0:
            ctrl_depth = False

        rows.append((n, sum_P, sum_Q, sum_Q_supp, sum_M1, sum_Ek, mass_k_nonzero,
                     m1_dm0, m1_dmne))

    # ---------------- report ----------------
    print("M_1 > 0: the Cauchy-Schwarz step restricted to supp(g), plus an exact identity")
    print("#   dmu = pi(lam) J(lam,lam*) (|u|+|v|) >= 0 ;  g = Delta(A) ;  k = Delta(Sum h)")
    print("#   M_1 = Sum dmu g k ;  P = Sum dmu g^2 ;  Q = Sum dmu (2-2delta)^2")
    print("#   Q' = Q restricted to {g != 0}.  CS on supp(g):  M_1 >= P - sqrt(P Q')")
    print()
    print(f"  {'n':>3} {'P/Q':>8} {'P/Q(supp)':>10} {'Q(supp)/Q':>10} "
          f"{'CS_full':>9} {'CS_supp':>9} {'gain':>7} {'E_k/mu(k!=0)':>13}")
    for (n, P, Q, Qs, M1, Ek, mk, _dm0, _dmne) in rows:
        pq = mp.mpf(P.numerator) / P.denominator / (mp.mpf(Q.numerator) / Q.denominator)
        pqs = mp.mpf(P.numerator) / P.denominator / (mp.mpf(Qs.numerator) / Qs.denominator)
        qratio = mp.mpf(Qs.numerator) / Qs.denominator / (mp.mpf(Q.numerator) / Q.denominator)
        Pf = mp.mpf(P.numerator) / P.denominator
        M1f = mp.mpf(M1.numerator) / M1.denominator
        Qf = mp.mpf(Q.numerator) / Q.denominator
        Qsf = mp.mpf(Qs.numerator) / Qs.denominator
        cs_full = (Pf - mp.sqrt(Pf * Qf)) / M1f          # fraction of M_1 the CS bound keeps
        cs_supp = (Pf - mp.sqrt(Pf * Qsf)) / M1f
        ekr = (mp.mpf(Ek.numerator) / Ek.denominator) / (mp.mpf(mk.numerator) / mk.denominator)
        print(f"  {n:>3} {mp.nstr(pq, 6):>8} {mp.nstr(pqs, 6):>10} {mp.nstr(qratio, 6):>10} "
              f"{mp.nstr(cs_full, 5):>9} {mp.nstr(cs_supp, 5):>9} "
              f"{mp.nstr(cs_supp - cs_full, 4):>7} {mp.nstr(ekr, 5):>13}")

    n_last, P, Q, Qs, M1, Ek, mk, dm0, dmne = rows[-1]
    checks = []

    checks.append(("CONTROL 1: the identity  2 M_1 = E_k + (P - Q)  holds EXACTLY at every n",
                   ctrl_identity,
                   "exact Fraction equality, n = 4..20, no tolerance"))
    checks.append(("CONTROL 2: edge M_1 == Cov(A,W) + Cov(D,W) from the Plancherel measure",
                   ctrl_m1,
                   "independent yardstick computed with no edges at all"))
    checks.append(("CONTROL 3: edge P == Cov(A,W) exactly", ctrl_P,
                   "the second independent yardstick; Q has none and this probe does not fake one"))
    checks.append(("CONTROL 4: g = 0 edges contribute EXACTLY 0 to both M_1 and P", ctrl_g0,
                   "this is what licenses restricting the CS step to supp(g)"))
    checks.append(("CONTROL 5: integrality  E_k >= mu({k != 0})", ctrl_integrality,
                   "k is an integer, so k^2 >= 1 off {k = 0}"))
    checks.append(("CONTROL 6: depth split is exact AND the Delta_m = 0 family is termwise >= 0",
                   ctrl_depth,
                   "b = |c| + 2m with m = min(i,j) >= 0, so k = g + 2 Delta_m; at Delta_m = 0 the "
                   "M_1 integrand is g*k = g^2. Checked per edge, not in aggregate."))

    pq = mp.mpf(P.numerator) / P.denominator / (mp.mpf(Q.numerator) / Q.denominator)
    pqs = mp.mpf(P.numerator) / P.denominator / (mp.mpf(Qs.numerator) / Qs.denominator)
    checks.append((f"FINDING 1: restricting CS to supp(g) raises P/Q from {mp.nstr(pq, 6)} "
                   f"to {mp.nstr(pqs, 6)} at n = {n_last}",
                   pqs > pq,
                   "free: the dropped edges contribute 0 to M_1 and 0 to P, and only load Q. "
                   "The live sufficient condition should be Q' < P, not Q < P."))

    # FINDING 2: the growth EXPONENT of E_k / mu(k != 0), measured rather than eyeballed.
    # This is the factor the integrality bound gives away.  My docstring predicted ~n; the
    # measurement decides, and the local log-log slope is reported over the last third of the
    # window so a short-window artefact is visible as instability rather than hidden in endpoints.
    def _ekr(row):
        Ekr, mkr = row[5], row[6]
        return (mp.mpf(Ekr.numerator) / Ekr.denominator) / \
               (mp.mpf(mkr.numerator) / mkr.denominator)

    ekr = _ekr(rows[-1])
    slopes = []
    for i in range(1, len(rows)):
        n0, n1 = rows[i - 1][0], rows[i][0]
        r0, r1 = _ekr(rows[i - 1]), _ekr(rows[i])
        slopes.append(mp.log(r1 / r0) / mp.log(mp.mpf(n1) / n0))
    tail = slopes[-6:]
    slope_lo, slope_hi = min(tail), max(tail)
    # global slope from n=5 (n=4 is an outlier: the chain is too small for the ratio to mean much)
    i5 = next(i for i, r in enumerate(rows) if r[0] == 5)
    slope_global = mp.log(_ekr(rows[-1]) / _ekr(rows[i5])) / mp.log(mp.mpf(n_last) / 5)

    checks.append((f"FINDING 2: my docstring prediction was WRONG -- E_k/mu(k!=0) grows like "
                   f"n^{mp.nstr(slope_global, 3)}, not n^1",
                   slope_global < mp.mpf("0.8"),
                   f"E_k/mu(k!=0) = {mp.nstr(_ekr(rows[i5]), 5)} at n=5 -> {mp.nstr(ekr, 5)} at "
                   f"n={n_last}; global log-log slope {mp.nstr(slope_global, 4)}, last-6 local "
                   f"slopes in [{mp.nstr(slope_lo, 3)}, {mp.nstr(slope_hi, 3)}]. I predicted the "
                   f"factor would grow like n (making the integrality bound cosmetic). It does "
                   f"NOT: |k| stays O(1)-ish, weighted mean k^2 ~ {mp.nstr(ekr, 4)} at n={n_last}. "
                   f"So the bound gives away a sub-linear factor, and is weaker than the exact "
                   f"E_k but NOT by the order I claimed. Window n<=20 is short -- this is a "
                   f"measured local slope, not an asymptotic."))

    d0 = mp.mpf(dm0.numerator) / dm0.denominator
    dn = mp.mpf(dmne.numerator) / dmne.denominator
    M1f = mp.mpf(M1.numerator) / M1.denominator
    checks.append((f"FINDING 3: the Delta_m = 0 family alone is {mp.nstr(100*d0/M1f, 4)} % of M_1 "
                   f"at n = {n_last}, and it is UNCONDITIONALLY non-negative",
                   d0 > 0,
                   f"M_1 = {mp.nstr(M1f, 6)} splits as {mp.nstr(d0, 6)} (Delta_m = 0, termwise "
                   f"g^2 >= 0, needs NO inequality) + {mp.nstr(dn, 6)} (Delta_m != 0, the only "
                   f"place negative edges can live). So the whole difficulty sits on "
                   f"depth-CHANGING edges. This is a decomposition, not a bound: the second term "
                   f"is {mp.nstr(100*dn/M1f, 4)} % of M_1 and is not controlled here."))

    print()
    print(f"  depth split of M_1 (b = |c| + 2m, k = g + 2*Delta_m):")
    print(f"    {'n':>3} {'M_1':>14} {'Delta_m=0 (>=0)':>16} {'Delta_m!=0':>14} {'share':>8}")
    for r in rows:
        nn, _, _, _, mm, _, _, a0, an = r
        mf = mp.mpf(mm.numerator) / mm.denominator
        af = mp.mpf(a0.numerator) / a0.denominator
        anf = mp.mpf(an.numerator) / an.denominator
        print(f"    {nn:>3} {mp.nstr(mf, 6):>14} {mp.nstr(af, 6):>16} {mp.nstr(anf, 6):>14} "
              f"{mp.nstr(af/mf, 5):>8}")

    print()
    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"        {detail}")
    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{npass}/{len(checks)} checks pass")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
