"""d_frame_closed_form_law_probe.py — the D(u) closed-form law in convention D.

Bean `qou-cxon`; adjudicates `qou-iayk`. Audit:
`docs/audits/2026-08-23-d-u-closed-form-is-convention-c.md`.

RESULT (all four atoms, exact — not fitted):

    C-frame :   2^(2A+1) * u^(18Z+21N+1) * (1+u^2)^(3A-1)
    D-frame : 6*2^(2A+1) * u^(20A-8Z+14) * (1+u^4)^(A+2Z-1)

The C law is convention-C BY CONSTRUCTION: its `(1+u^2)` is the cleared
denominator of `z_C = u/(1+u^2)` (see `d_u_closed_form_proof.py:18`, which
writes z as `1/(q^(1/2) + q^(-1/2))` = `sqrt(q)/(q+1)`). Under D,
`z_D = u^6/(1+u^4)`, so the base must become `(1+u^4)` — and the exponent
moves too, which clearing z alone does NOT predict.

THE INTERESTING PART. Under C the cyclotomic exponent is `3A-1`: protons and
neutrons contribute equally. Under D it is `A + 2Z - 1` — a proton contributes
3, a neutron 1. The law becomes p/n asymmetric.

STATUS OF EACH CLAIM. The per-atom denominators are EXACT: `tr_M_atomic` is an
integer-coefficient rational function of q with no anchor in it, so its
denominator IS D(u). The `(Z,N)` closed forms are fits — three parameters
against four atoms, i.e. ONE degree of validation each, both held-out tests
exact. They are not derivations: the counting rule behind `A + 2Z - 1` is
open, as is why the prefactor picks up a uniform 6.

The D(u) law across atoms, from the EXACT symbolic trace.

The C-frame law is  2^(2A+1) * u^(18Z+21N+1) * (1+u^2)^(3A-1)  and is
convention-C by construction (its (1+u^2) is the cleared denominator of
z_C = u/(1+u^2)). markov_peel.tr_M_atomic is exact in q with no anchor, so
its denominator IS the D-frame D(u). Compute it per atom and read off the
three factors, rather than fitting them.
"""
import sys, time
from pathlib import Path
HERE = Path("/home/user/qou/computations").resolve()
for p in (HERE, HERE/"substrate", HERE/"hecke", HERE/"markov",
          Path("/home/user/qou/tools/pyhecke/python")):
    sys.path.insert(0, str(p))
import sympy as sp
from markov_peel import tr_M_atomic

q, u = sp.symbols('q u', positive=True)
ATOMS = [("D",1,1), ("T",1,2), ("3He",2,1), ("4He",2,2)]

print(f"{'atom':5s} {'Z':>2s} {'N':>2s} {'A':>2s} | {'pref':>7s} {'u-exp':>6s} {'(1+u^4)^k':>10s} | C-law pref/exp/k")
print("-"*86)
rows=[]
for name, Z, N in ATOMS:
    A = Z+N
    t0=time.time()
    try:
        expr = sp.cancel(sp.together(tr_M_atomic(Z, N)))
    except Exception as e:
        print(f"{name:5s} FAILED: {type(e).__name__}: {e}"); continue
    num, den = sp.fraction(expr)
    den_u = sp.factor(sp.expand(sp.simplify(den.subs(q, u**2))))
    # read off: integer prefactor, power of u, power of (1+u^4)
    pref = sp.Integer(1); upow = 0; cyc = 0; other=[]
    for base, e in (den_u.as_powers_dict().items() if den_u.is_Mul or den_u.is_Pow else [(den_u,1)]):
        if base.is_Integer: pref *= base**e
        elif base == u: upow = int(e)
        elif sp.simplify(base - (1+u**4)) == 0: cyc = int(e)
        else: other.append((base,e))
    cpref, cexp, ck = 2**(2*A+1), 18*Z+21*N+1, 3*A-1
    print(f"{name:5s} {Z:2d} {N:2d} {A:2d} | {int(pref):7d} {upow:6d} {cyc:10d} | {cpref} / {cexp} / {ck}"
          + (f"   OTHER {other}" if other else "") + f"   ({time.time()-t0:.1f}s)", flush=True)
    rows.append((name,Z,N,A,int(pref),upow,cyc))

if len(rows) >= 3:
    print("\nfit each factor as a*Z + b*N + c on the first three, TEST on the fourth:")
    from fractions import Fraction as F
    def solve3(A3,b3):
        M=[[F(x) for x in r]+[F(v)] for r,v in zip(A3,b3)]
        for i in range(3):
            p=next(r for r in range(i,3) if M[r][i]!=0); M[i],M[p]=M[p],M[i]
            M[i]=[x/M[i][i] for x in M[i]]
            for r in range(3):
                if r!=i and M[r][i]!=0:
                    f=M[r][i]; M[r]=[x-f*y for x,y in zip(M[r],M[i])]
        return [M[i][3] for i in range(3)]
    A3=[[r[1],r[2],1] for r in rows[:3]]
    for idx,label in ((5,"u-exponent"),(6,"(1+u^4) exponent")):
        try:
            a,b,c = solve3(A3,[r[idx] for r in rows[:3]])
            pred = a*rows[3][1]+b*rows[3][2]+c if len(rows)>3 else None
            ok = (pred == rows[3][idx]) if len(rows)>3 else None
            print(f"  {label:20s} = {a}*Z + {b}*N + {c}"
                  + (f"   held-out {rows[3][0]}: pred {pred}, actual {rows[3][idx]} -> {'EXACT' if ok else 'FAILS'}" if pred is not None else ""))
        except Exception as e:
            print(f"  {label}: no linear fit ({e})")
    print("\n  prefactors:", [(r[0], r[4]) for r in rows], " vs C 2^(2A+1):", [(r[0], 2**(2*r[3]+1)) for r in rows])
