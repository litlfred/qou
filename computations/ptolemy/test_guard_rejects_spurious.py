"""REGRESSION: the round-trip guard must REJECT the known-spurious L6a4 point.

Accepting good points is the easy half -- 4_1 did that under the BROKEN reduction too.
The half that matters is rejecting a point that satisfies the reduced system but is not
on the original variety. This replays the exact point that caused the retraction: root 0
of the degree-18 RUR from the UNSATURATED reduction, which satisfies the 12-variable
reduced system to 39 digits and yet drives x0 to ~1e471 when lifted.

Exit 0 iff the guard rejects it.
"""
import ast, json, re, sys, mpmath as mp, sympy as sp
import pathlib

# qou-47nf: the fixture this guard replays has never existed in git history
# (`git log --all` finds no `L6a4_c1_q_sl5_P.res`); it was a scratch file in the
# author's working directory. Until the author says which degree-18 RUR from the
# UNSATURATED reduction it was, the guard cannot run. Skip with that reason
# rather than fail at collection, so nobody reads a green suite as "guard passed".
_RES = pathlib.Path(__file__).resolve().parent / 'L6a4_c1_q_sl5_P.res'
if not _RES.exists():
    _REASON = ("qou-47nf: fixture L6a4_c1_q_sl5_P.res has never existed in git; "
               "regression guard NOT run (unrecoverable data, owner decision 2026-11-15 option 2a)")
    if __name__ == "__main__":
        sys.exit("SKIPPED -- " + _REASON)
    import pytest
    pytest.skip(_REASON, allow_module_level=True)
mp.mp.dps = 50
core = ast.literal_eval(open('L6a4_c1_q_sl5_P.res').read().strip().rstrip(':'))[1]
vnames, linform = core[3], core[4]; blk = core[5][1]
w, den, nums = blk[0][1], blk[1][1], blk[2]
param = vnames[linform.index(1)]; others = [v for v in vnames if v != param]
def ev(c, t):
    r = mp.mpf(0)
    for x in reversed(c): r = r*t + x
    return r
t = mp.polyroots([mp.mpf(c) for c in reversed(w)], maxsteps=300, extraprec=300)[0]
d = ev(den, t)
pt = {param: t}
for vn, (nc, m) in zip(others, [(e[0][1], mp.mpf(e[1])) for e in nums]):
    pt[vn] = -ev(nc, t) / (m * d)

sub = json.load(open('L6a4_c1_subs.json'))          # the UNSATURATED substitutions
full = {sp.Symbol(k): v for k, v in pt.items()}
verdict, why = "ACCEPTED", ""
for v, expr in reversed(sub['subs_order']):
    e = sp.sympify(expr); fs = sorted(e.free_symbols, key=str)
    dd = sp.denom(sp.together(e))
    dv = sp.lambdify(fs, dd, 'mpmath')(*[full[x] for x in fs]) if dd.free_symbols else complex(dd)
    if abs(mp.mpc(dv)) < mp.mpf(10)**-20:
        verdict, why = "REJECTED", f"denominator of {v} vanishes ({mp.nstr(abs(mp.mpc(dv)),3)})"
        break
    val = sp.lambdify(fs, e, 'mpmath')(*[full[x] for x in fs])
    if abs(mp.mpc(val)) > mp.mpf(10)**20:
        verdict, why = "REJECTED", f"{v} blows up to {mp.nstr(abs(mp.mpc(val)),3)}"
        break
    full[sp.Symbol(v)] = val
print(f"known-spurious point (RUR root 0, unsaturated reduction): {verdict}")
if why: print(f"  reason: {why}")
print("\nregression PASSES -- the guard catches the exact failure that caused the retraction"
      if verdict == "REJECTED" else
      "\nregression FAILS -- the guard would NOT have caught it")
sys.exit(0 if verdict == "REJECTED" else 1)
