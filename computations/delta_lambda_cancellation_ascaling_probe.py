#!/usr/bin/env python3
"""Δ_λ cancellation / A-scaling probe — the SIGNED net under each q-dim
convention, the real closure test behind the ℓ¹-ceiling prune.

The ℓ¹-ceiling prune bounds *sign-only* fixes; the route-(i) q-dim probe
(`delta_lambda_qdim_route_probe.py`) showed the *ℓ¹* ceiling is convention-
dependent (a hidden DOF). But ℓ¹ is only the ceiling — the quantity that
must actually equal the target is the SIGNED net

    net(K) = Σ_λ y_λ(q_0) · χ^λ(β_K) · sgn(w₀^{S_{λ'}}) · dim_q,λ ,

with the proven chirality sign (PR #2416) on the magnitude dim_q,λ. This
script computes net/target (normalised so a closure reads +1) for the four
light isotopes under the classic dimension and three q-dim conventions
(balanced / unbalanced / fake-degree = principal specialization).

RESULT (this script): net/target —

      iso   classic  balanced  unbalanced  fake-degree
      D      0.171    0.180      0.219       0.277
      T      0.225    0.295      0.568       0.908
      ³He    0.304    0.402      0.783       1.270
      ⁴He    0.107    0.206      0.653       1.313

As the convention "grows" (classic → fake-degree) the net grows — but
**non-uniformly in A**: the heavy isotopes (³He, ⁴He) shoot past target
while the light ones (D, T) stay well below. NO single convention lands all
four near +1: at fake-degree D is 0.28 while ⁴He is 1.31 (a 4.7× spread that
*straddles* the target). The per-convention isotope spread never collapses.

INTERPRETATION (scope (a)). This sharpens the route-(i) finding: a q-dim
magnitude re-derivation is not merely an ℓ¹ hidden DOF — when the actual
chirality signs are imposed, **no single q-dimension convention reproduces
the A-scaling of nuclear binding** (D wants a steep convention, ⁴He a shallow
one; they conflict). So a convention-only route (i) cannot close the family;
the correct object must carry an **A- or λ-dependent** structure (route
(ii)/(iii), or a structured generating kernel whose effective dim_q bends
the A-scaling — e.g. the z2bn q-Gaussian/Habiro EGF, #2899). NOT a (b)
exclusion — no invariant forbids such a structured object; it is the
scope-(a) statement that the three flat conventions fail the A-scaling test.

Inputs READ from canonical pinned witnesses (mpmath 50 dps) — env-skew-immune.

Producer for: computations/delta-lambda-cancellation-ascaling-probe.witness.json
"""
from __future__ import annotations
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json, math, os, hashlib, datetime
from mpmath import mp, mpf
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = os.path.dirname(os.path.abspath(__file__))


def hook_lengths(part):
    maxc = part[0]; col = [0] * maxc
    for r in part:
        for j in range(r):
            col[j] += 1
    out = []
    for i, r in enumerate(part):
        for j in range(r):
            out.append((r - j - 1) + (col[j] - i - 1) + 1)
    return out


def dim_classic(part):
    n = sum(part); h = 1
    for x in hook_lengths(part):
        h *= x
    return math.factorial(n) // h


def conj(part):
    return [sum(1 for r in part if r > j) for j in range(part[0])]


def n_lambda(part):
    return sum(i * part[i] for i in range(len(part)))


def sgn_w0_young(part):
    s = 1
    for m in part:
        if (m * (m - 1) // 2) % 2 == 1:
            s = -s
    return s


def qbal(k, q):
    return (q**k - q**(-k)) / (q - q**(-1))


def qunbal(k, q):
    return (1 - q**k) / (1 - q)


def _dim_from(part, q, qint):
    n = sum(part)
    num = mpf(1)
    for k in range(1, n + 1):
        num *= qint(k, q)
    den = mpf(1)
    for x in hook_lengths(part):
        den *= qint(x, q)
    return num / den


CONVENTIONS = {
    "classic": lambda p, q: mpf(dim_classic(p)),
    "balanced": lambda p, q: _dim_from(p, q, qbal),
    "unbalanced": lambda p, q: _dim_from(p, q, qunbal),
    "fake_degree": lambda p, q: q**n_lambda(p) * _dim_from(p, q, qunbal),
}

M_E_MEV = mpf("0.51099895069")
ISOTOPES = {
    "D":   ("atom-chi-rust-d.witness.json",   "6",  2.224566, 2),
    "T":   ("atom-chi-rust-t.witness.json",   "9",  8.481798, 3),
    "3He": ("atom-chi-rust-3he.witness.json", "9",  7.718043, 3),
    "4He": ("atom-chi-rust-4he.witness.json", "12", 28.295673, 4),
}


def main():
    ywit = os.path.join(HERE, "y-lambda-at-q0.witness.json")
    ydat = json.load(open(ywit))["data"]["by_n"]
    q0 = mpf(json.load(open(ywit))["parameters"]["q_0"])

    rows = []
    for name, (chif, nkey, B, A) in ISOTOPES.items():
        chi = json.load(open(os.path.join(HERE, chif)))["data"]["atom"]["by_partition"]
        yl = {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in ydat[nkey]}
        target = -mpf(B) / M_E_MEV   # binding is a negative energy contribution; closure ⇒ net/target = +1
        netrat = {}
        for cname, fn in CONVENTIONS.items():
            net = mpf(0)
            for e in chi:
                p = tuple(e["partition"])
                net += yl[p] * mpf(e["chi_lambda"]) * sgn_w0_young(conj(list(p))) * fn(list(p), q0)
            netrat[cname] = float(net / target)
        rows.append({"atom": name, "A": A, "B_AME_MeV": B,
                     "net_over_target": netrat})

    # per-convention isotope spread (max/min of net/target across the 4 isotopes)
    spreads = {}
    closes = {}
    for c in CONVENTIONS:
        vals = [r["net_over_target"][c] for r in rows]
        spreads[c] = {"min": min(vals), "max": max(vals), "ratio": max(vals) / min(vals) if min(vals) else None}
        closes[c] = all(0.9 <= v <= 1.1 for v in vals)
    any_closes = any(closes.values())

    witness = {
        "engine": "mpmath",
        "engineVersion": "mpmath 50dps on canonical witnesses",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "delta-lambda-cancellation-ascaling-probe",
        "scriptFile": "delta_lambda_cancellation_ascaling_probe.py",
        "scriptHash": hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12],
        "description": (
            "SIGNED net/target = Σ_λ y_λ χ^λ sgn(w₀^{S_λ'}) dim_q,λ (closure ⇒ "
            "+1) for D/T/³He/⁴He under classic + 3 q-dim conventions. As the "
            "convention grows the net grows NON-UNIFORMLY in A: heavy isotopes "
            "(³He 1.27, ⁴He 1.31 at fake-degree) overshoot while light ones "
            "(D 0.28, T 0.91) undershoot. NO single convention lands all four "
            "near +1 ⟹ no flat q-dim convention reproduces binding's A-scaling; "
            "the closure object must be A-/λ-structured (route (ii)/(iii) or a "
            "structured kernel, e.g. z2bn q-Gaussian/Habiro EGF #2899). Scope "
            "(a), not a (b) exclusion. Sign on transpose λ' (proven form PR "
            "#2416)."
        ),
        "scope": "(a) scope-limited — the 3 flat q-dim conventions fail the A-scaling closure test",
        "parameters": {"q_0": float(q0), "m_e_MeV": float(M_E_MEV)},
        "data": {
            "rows": rows,
            "per_convention_isotope_spread": spreads,
            "any_convention_closes_all_four": any_closes,
        },
        "allPassed": True,
    }
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "delta-lambda-cancellation-ascaling-probe", witness,
        script_path=__file__, engine="python", start_time=_T0,
    ).save()

    cols = list(CONVENTIONS)
    print("net/target (closure ⇒ +1.000)")
    print(f"{'iso':>4}" + "".join(f"{c:>13}" for c in cols))
    for r in rows:
        print(f"{r['atom']:>4}" + "".join(f"{r['net_over_target'][c]:>13.3f}" for c in cols))
    print(f"\nany single convention closes all four (0.9–1.1): {any_closes}")
    print("per-convention isotope spread (max/min):",
          {c: round(spreads[c]['ratio'], 2) for c in cols})
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
