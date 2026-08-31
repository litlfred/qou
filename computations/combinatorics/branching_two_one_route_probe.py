"""`branching_two_one` is NOT blocked on RSK -- the route, checked.

WHAT THIS DECIDES
-----------------
`QOU.BraidKnot.YoungTableauStandard.RSKIdentitiesContext.branching_two_one` is the class's
one remaining open field.  Its docstrings say it is "discharged by the RSK correspondence",
which Mathlib lacks.  This probe tests whether that is actually required, by checking the
identity the differential-poset route would give:

    G(mu, k) := sum_{|lam| = k} f^lam * f^{lam/mu}  =  (k! / |mu|!) * f^mu.

At mu = (2,1) -- f^mu = 2, |mu|! = 6 -- that reads sum = k!/3, i.e. 3*sum = k!, which is
`branching_two_one` verbatim.

THE ROUTE (why the identity follows from what the corpus already has)
--------------------------------------------------------------------
Induction on k, with base G(mu, |mu|) = f^mu (the only lam of size |mu| containing mu is mu):

    G(mu, k+1) = sum_{|lam|=k+1}  f^lam * f^{lam/mu}
               = sum_{|lam|=k+1}  f^lam * sum_{nu <. lam, nu >= mu} f^{nu/mu}   [skew branching]
               = sum_{|nu|=k}     f^{nu/mu} * sum_{lam .> nu} f^lam             [transpose]
               = sum_{|nu|=k}     f^{nu/mu} * (k+1) * f^nu                      [upSum_eq]
               = (k+1) * G(mu, k).

The third step is QOU.Mathlib.upSum_eq, PROVED (PR #6164, sorry-free).  The transposition is
the same Finset.sum_comm manoeuvre `pairTerm` handles there.  So the ONE remaining obligation
is the skew branching rule -- f^{lam/mu} = sum over corners of lam outside mu of
f^{(lam - c)/mu}, i.e. "remove the largest entry of a skew SYT" -- the direct analogue of the
already-proved straight case QOU.Mathlib.numStandardYoungTableaux_branching.

WHAT THIS PROBE DOES AND DOES NOT ESTABLISH
-------------------------------------------
DOES: the identity holds exactly for k = 3..11, so the route's conclusion is not wrong.
DOES NOT: prove the skew branching rule.  `fskew` below is COMPUTED BY that recursion, so
the probe assumes it rather than checking it.  Read this as "the arithmetic of the route is
sound", not as a verification of its one open input.

Exact integer arithmetic throughout; no float is ever constructed (AGENTS.md NO-FLOAT64 --
probes are not exempt).  Nothing here is fitted: every number is a count.
"""
from functools import lru_cache
from math import factorial

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxp), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

@lru_cache(maxsize=None)
def fdim(lam):
    """#SYT of shape lam, by the branching recursion (remove a corner)."""
    if sum(lam) == 0: return 1
    tot = 0
    for i in range(len(lam)):
        if i + 1 == len(lam) or lam[i] > lam[i+1]:
            new = list(lam); new[i] -= 1
            new = tuple(x for x in new if x > 0)
            tot += fdim(new)
    return tot

def contains(lam, mu):
    if len(mu) > len(lam): return False
    return all(mu[i] <= lam[i] for i in range(len(mu)))

@lru_cache(maxsize=None)
def fskew(lam, mu):
    """#skew-SYT of shape lam/mu, by removing the maximal entry (a corner of lam not in mu)."""
    if not contains(lam, mu): return 0
    if sum(lam) == sum(mu): return 1
    tot = 0
    for i in range(len(lam)):
        if i + 1 == len(lam) or lam[i] > lam[i+1]:
            if i < len(mu) and lam[i] == mu[i]:   # that corner is inside mu
                continue
            new = list(lam); new[i] -= 1
            new = tuple(x for x in new if x > 0)
            tot += fskew(new, mu)
    return tot

mu = (2, 1)
m = sum(mu)
print(f"mu = {mu},  f^mu = {fdim(mu)},  |mu|! = {factorial(m)}")
print(f"{'k':>3} {'LHS = sum f^lam f^{lam/mu}':>28} {'RHS = (k!/m!) f^mu':>22}  {'3*LHS':>12} {'k!':>12}  ok")
allok = True
for k in range(3, 12):
    lhs = sum(fdim(lam) * fskew(lam, mu) for lam in partitions(k))
    rhs = factorial(k) // factorial(m) * fdim(mu)
    ok = (lhs == rhs) and (3 * lhs == factorial(k))
    allok &= ok
    print(f"{k:>3} {lhs:>28} {rhs:>22}  {3*lhs:>12} {factorial(k):>12}  {ok}")
print()
print("ALL EXACT MATCHES:", allok)
if not allok:
    raise SystemExit("route REFUTED -- the identity does not hold; do not pursue it")
print()
print("Scope: this confirms the route's arithmetic. The open input is the SKEW branching")
print("rule; upSum_eq (its other input) is already proved sorry-free.")
