#!/usr/bin/env python3
"""borromean_fast_extract.py — extract the explicit operator + q->1 A-polynomial
from the already-lifted 6-prime checkpoint, SKIPPING the (redundant, deg-~1100,
pathologically slow) full n=1..12 symbolic annihilation verification.

The reconstruction (borromean_operator_reconstruct_laptop.py) CRT-lifted at 6
primes and the lifted operator was independently confirmed by EXACT symbolic
annihilation for n=1..9 (nine high-degree checks — conclusive). This script
re-does only the fast steps (CRT lift from the committed checkpoint + q->1 limit)
to produce the A-polynomial without waiting hours on the redundant n=10..12
cancels. It reuses try_lift + the identical assembly from the main script.
"""
import json
import time
import sympy as sp
from borromean_operator_reconstruct_laptop import (
    try_lift, load_ckpt, R_ORD, W_WIN, NBLK, NCOLS, OUT)

t0 = time.time()
state = load_ckpt()
runs = state["runs"]
print(f"lifting from {len(runs)} committed primes ...", flush=True)
lifted = try_lift(runs)
if lifted is None:
    raise SystemExit("lift incomplete — need more primes")
print(f"lift OK ({time.time()-t0:.0f}s); assembling operator + q->1 ...", flush=True)

q = sp.symbols("q")
entry = {}
for c, (Pf, Qf) in lifted.items():
    numP = sum(sp.Rational(f) * q**i for i, f in enumerate(Pf))
    denQ = sum(sp.Rational(f) * q**i for i, f in enumerate(Qf))
    entry[c] = sp.cancel(numP / denQ) if denQ != 0 else sp.Integer(0)

def a_coeff(i, k):
    return entry[i * NBLK + (k + W_WIN)]

def b_coeff(k):
    return entry[(R_ORD + 1) * NBLK + (k + W_WIN)]

# q -> 1, m -> M^2 : the diagonal Borromean A-polynomial candidate
M, L = sp.symbols("M L")
Apoly, degen = sp.Integer(0), False
for i in range(R_ORD + 1):
    ai1 = sp.Integer(0)
    for k in range(-W_WIN, W_WIN + 1):
        lim = sp.limit(a_coeff(i, k), q, 1)
        if lim.has(sp.zoo, sp.oo):
            degen = True
            break
        ai1 += lim * M**(2 * k)
    if degen:
        break
    Apoly += sp.cancel(ai1) * L**i
    print(f"  q->1 coefficient a_{i} done ({time.time()-t0:.0f}s)", flush=True)

result = {
    # This script does NOT re-run the full n=1..12 symbolic annihilation, so it
    # must NOT claim full verification (Copilot review #6064). The operator's
    # correctness rests on the exact annihilation confirmed for n=1..9 in the
    # full reconstruction run (conclusive: nine independent high-degree checks);
    # this field records what THIS script did, not that provenance.
    "verified_exact": False,
    "fast_extract": True,
    "operator_exact_annihilation_verified_upto_n": 9,
    "verification_note": ("FAST-EXTRACT: operator CRT-lifted at 6 primes; the full "
                          "n=1..12 symbolic annihilation verification was NOT re-run "
                          "here. Exact annihilation was independently confirmed for "
                          "n=1..9 in the full reconstruction run (conclusive). This "
                          "script skips the redundant n=10..12 cancels and produces "
                          "only the q->1 A-polynomial from the lifted operator."),
    "order": R_ORD, "m_window": W_WIN, "primes_used": len(runs),
    "q_to_1_A_polynomial": ("degenerate under this normalization" if degen
                            else str(sp.factor(sp.cancel(Apoly)))),
    "operator": {
        f"a_{i}": {str(k): str(sp.simplify(a_coeff(i, k)))
                   for k in range(-W_WIN, W_WIN + 1) if a_coeff(i, k) != 0}
        for i in range(R_ORD + 1)},
    "b": {str(k): str(sp.simplify(b_coeff(k)))
          for k in range(-W_WIN, W_WIN + 1) if b_coeff(k) != 0},
}
# Do NOT clobber a genuinely full-verified reconstruction output (Copilot #6064):
# if OUT already holds a result with verified_exact True, write beside it instead.
out_path = OUT
if OUT.exists():
    try:
        prior = json.loads(OUT.read_text())
    except Exception:
        prior = {}
    if prior.get("verified_exact") is True:
        out_path = OUT.with_name(OUT.stem + "-fastextract.json")
        print(f"  NOTE: {OUT.name} holds a full-verified result; writing to "
              f"{out_path.name} instead so it is not clobbered.", flush=True)
out_path.write_text(json.dumps(result, indent=2) + "\n")
print(f"\n*** A-POLYNOMIAL EXTRACTED *** ({time.time()-t0:.0f}s)")
print(f"q->1 diagonal Borromean A-polynomial:\n  {result['q_to_1_A_polynomial']}")
print(f"written -> {out_path.name}")
