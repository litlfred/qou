#!/usr/bin/env python3
"""
wlambda_q0_continuation.py — the archimedean q₀-continuation of the W_λ value map is
polynomial evaluation of the Chebyshev quantum integers `qi` at `t = q₀ + q₀⁻¹`.

The W_λ keystone value map `d_q(λ) = [mark λ]_q` (KeystoneMcKayValueMap, proved at
generic q) is a global Laurent polynomial — equivalently a polynomial in the fold
parameter `t = q + q⁻¹`. So the passage from the root-of-unity fibre (t = φ =
2cos(π/5)) to the real substrate (t = q₀ + q₀⁻¹) is EVALUATION OF ONE FIXED
POLYNOMIAL at two points, NOT an analytic continuation of transcendental data.

This probe exhibits that for the four physical n=5 blocks and records the numeric
q₀ table. The Lean certificate is
`content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneWLambdaContinuation.lean`
(muon_folds_at_root / muon_unfolds_generic / block_dims_explicit, sorry-free).

Scope-(a): this certifies the VALUE-MAP continuation is polynomial evaluation; it
does NOT derive loc_matches (the gauge = categorical identification). No fit;
nothing wired; L2 unchanged (2/7).
"""
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# Substrate modulus q₀ (muon-pinned; computations/ layer canonical, from
# q-pinning-50-digit.witness.json). High-precision decimal string, evaluated as float
# for the numeric table (the structural facts below are exact integers/rationals).
Q0_STR = Q_50_DIGIT_STR
q0 = float(Q0_STR)
t0 = q0 + 1.0 / q0  # fold parameter t = q + q⁻¹


def qi_poly(n):
    """Chebyshev quantum integer [n] as an integer-coefficient polynomial in t,
    returned as a dict {power: coeff}.  [0]=0, [1]=1, [n+2] = t·[n+1] − [n]."""
    a, b = {0: 0}, {0: 1}
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(n - 1):
        tb = {p + 1: c for p, c in b.items()}  # t · b
        nxt = dict(tb)
        for p, c in a.items():
            nxt[p] = nxt.get(p, 0) - c
        a, b = b, {p: c for p, c in nxt.items() if c != 0}
    return b


def evalp(poly, t):
    return sum(c * t ** p for p, c in poly.items())


# The four physical n=5 block quantum dimensions as qi-polynomials in t.
blocks = {
    "(5)   [1]": qi_poly(1),
    "(4,1) [4]": qi_poly(4),
    "(3,2) [5] (muon)": qi_poly(5),
    "(3,1,1) [5]+1 (electron)": {**qi_poly(5), 0: qi_poly(5).get(0, 0) + 1},
}

# golden root t = φ = (1+√5)/2 (exact via Fraction is impossible for √5; use the
# defining relation φ² = φ+1 to get qi(φ) exactly as a+bφ — but for the numeric
# root table we use the float φ).
phi = (1.0 + 5.0 ** 0.5) / 2.0

assertions = []

# --- Structural (exact) assertions ---------------------------------------------
# muon block folds to 0 at the root: [5]_φ = 0  (φ² = φ+1 ⇒ φ⁴−3φ²+1 = 0).
# Verified exactly in ℤ[φ]/(φ²−φ−1): reduce t⁴−3t²+1 mod φ²=φ+1.
def reduce_golden(poly):
    """Reduce a poly in t modulo φ² = φ+1 to a+bφ (exact integer a,b)."""
    a, b = 0, 0  # a + bφ
    # powers of φ mod (φ²=φ+1): φ⁰=1, φ¹=φ, φ²=1+φ, φ³=1+2φ, φⁿ = F(n-1)+F(n)φ
    def phi_pow(k):
        # returns (a,b) with φ^k = a + bφ
        if k == 0:
            return (1, 0)
        if k == 1:
            return (0, 1)
        pa, pb = 1, 0
        ca, cb = 0, 1
        for _ in range(k - 1):
            # multiply (ca+cbφ) by φ = caφ + cbφ² = caφ + cb(1+φ) = cb + (ca+cb)φ
            ca, cb = cb, ca + cb
        return (ca, cb)
    for p, c in poly.items():
        pa, pb = phi_pow(p)
        a += c * pa
        b += c * pb
    return (a, b)

muon_root = reduce_golden(qi_poly(5))  # should be (0,0)
assertions.append({
    "name": "muon_block_folds_to_zero_at_root",
    "computed": f"{muon_root[0]}+{muon_root[1]}φ",
    "expected": "0+0φ",
    "passed": muon_root == (0, 0),
    "tolerance": 0,
    "source": "d((3,2))(φ) = [5]_φ = 0 exactly in ℤ[φ]/(φ²−φ−1); Lean muon_folds_at_root.",
})

# electron − muon split = +1 exactly (identity of polynomials).
split = {p: c for p, c in blocks["(3,1,1) [5]+1 (electron)"].items()}
for p, c in qi_poly(5).items():
    split[p] = split.get(p, 0) - c
split = {p: c for p, c in split.items() if c != 0}
assertions.append({
    "name": "electron_muon_split_is_plus_one",
    "computed": json.dumps(split),
    "expected": '{"0": 1}',
    "passed": split == {0: 1},
    "tolerance": 0,
    "source": "d((3,1,1)) − d((3,2)) = 1 (identity of qi-polynomials); Lean electron_muon_split.",
})

# muon generic polynomial is t⁴−3t²+1 (the unfold).
muon_poly = qi_poly(5)
expected_muon = {4: 1, 2: -3, 0: 1}
assertions.append({
    "name": "muon_block_unfolds_to_quartic",
    "computed": json.dumps({str(k): v for k, v in sorted(muon_poly.items())}),
    "expected": json.dumps({str(k): v for k, v in sorted(expected_muon.items())}),
    "passed": muon_poly == expected_muon,
    "tolerance": 0,
    "source": "d((3,2))(t) = t⁴−3t²+1 (qi_five); Lean muon_unfolds_generic.",
})

# --- Numeric q₀ continuation table (the 'shown' continuation) -------------------
dq0 = {name: evalp(poly, t0) for name, poly in blocks.items()}
D2 = sum(v * v for v in dq0.values())
table = {}
for name, poly in blocks.items():
    root_val = evalp(poly, phi)
    q0_val = dq0[name]
    table[name] = {
        "root_d_q(phi)": round(root_val, 6),
        "q0_d_q(t0)": round(q0_val, 6),
        "W_lambda(q0)": round(q0_val * q0_val / D2, 8),
    }

# Sanity: the growing 4-class ratios ≈ (1, 4.11, 5.22, 6.22).
growing = [dq0[k] for k in blocks]
assertions.append({
    "name": "q0_continuation_gives_growing_4class",
    "computed": ", ".join(f"{v:.3f}" for v in growing),
    "expected": "1.000, 4.110, 5.220, 6.220 (approx)",
    "passed": (abs(growing[0] - 1) < 1e-6 and abs(growing[1] - 4.110) < 1e-2
               and abs(growing[2] - 5.220) < 1e-2 and abs(growing[3] - 6.220) < 1e-2),
    "tolerance": 1e-2,
    "source": "value-map qi polynomials evaluated at t₀=q₀+q₀⁻¹; unfolds the bounded root (1,φ,0,1).",
})

all_passed = all(a["passed"] for a in assertions)

# --- Witness emission ----------------------------------------------------------
script_path = Path(__file__)
script_bytes = script_path.read_bytes()
script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]


def git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=script_path.parent,
                                       stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "unknown"


witness = {
    "engine": "python",
    "engineVersion": "python 3.11",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "commitSha": git("rev-parse", "HEAD"),
    "assertions": assertions,
    "allPassed": all_passed,
    "durationMs": 0,
    "computation": "wlambda-q0-continuation",
    "scriptFile": "computations/probes/wlambda_q0_continuation.py",
    "scriptHash": script_hash,
    "scriptCommitSha": git("log", "-1", "--format=%H", "--", "computations/probes/wlambda_q0_continuation.py"),
    "precisionMetadata": {"note": "structural facts exact (ℤ[φ] / ℤ[t]); numeric table float64"},
    "environment": {"python": "3.11"},
    "description": (
        "The archimedean q₀-continuation of the W_λ value map is polynomial evaluation of the "
        "Chebyshev quantum integers at t = q₀+q₀⁻¹. Exhibits the muon-block fold (0 at the root) / "
        "unfold (t⁴−3t²+1 generically) and the growing 4-class (1,[4],[5],[5]+1). Lean certificate: "
        "KeystoneWLambdaContinuation.lean. Scope-(a); does NOT derive loc_matches; no fit; nothing wired."
    ),
    "data": {"q0": Q0_STR, "t0": t0, "D2_q0": D2, "table": table},
}

out = script_path.parent / "wlambda-q0-continuation.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out}  (allPassed={all_passed}, {len(assertions)} assertions)")
for name, row in table.items():
    print(f"  {name:28} root={row['root_d_q(phi)']:>9}  q0={row['q0_d_q(t0)']:>9}  W={row['W_lambda(q0)']}")
