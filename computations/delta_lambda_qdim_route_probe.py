#!/usr/bin/env python3
"""Δ_λ route-(i) probe — is a QUANTUM-DIMENSION reweighting of |Δ_λ| a
*constrained* magnitude fix, or a hidden degree of freedom?

The ℓ¹-ceiling prune (`delta_lambda_l1_ceiling_sign_prune.py`) shows a
*magnitude-adding* ingredient is necessary and names three routes:
  (i)  re-derive the block magnitude |Δ_λ| ≠ dim_λ,
  (ii) re-weight y_λ,
  (iii) add a term beyond the single Σ_λ sum (T2–T6 / A=4 interface).

This probes route (i): replace the proven classical magnitude
|Δ_λ| = dim_λ (Wedderburn) by a **quantum dimension** at the canonical
substrate q_0, and recompute the ℓ¹ ceiling ‖c_q‖₁ = Σ_λ |y_λ χ^λ dim_q,λ|.
Three natural conventions of dim_q are tested:

  - balanced     : [n]_q!/∏[h]_q with [k]_q = (q^k − q^{−k})/(q − q^{−1});
  - unbalanced   : same, with [k]_q = (1 − q^k)/(1 − q);
  - fake-degree  : q^{n(λ)} · (unbalanced),  n(λ) = Σ_i (i−1)λ_i
                   (the principal-specialization / generic-degree weight).

RESULT (this script): the ceiling ‖c_q‖₁/|target| is **wildly
convention-dependent** —

      iso   classic  balanced  unbalanced  fake-degree
      D      0.52     0.55       0.68        0.85
      T      0.36     0.47       0.86        1.35
      ³He    0.59     0.77       1.41        2.18
      ⁴He    0.41     0.80       2.54        5.62

The balanced convention *undershoots* (< 1) for every isotope, but the
unbalanced and fake-degree conventions *overshoot* (> 1) for the heavier
isotopes (⁴He spans 0.41 → 5.62 across conventions).

INTERPRETATION (scope (a), corrected). Route (i) does NOT "fail" — it
**escapes the sign-only prune** (which holds the magnitude fixed at
classical dim) and is **under-constrained**: the q-dimension convention is
a **hidden degree of freedom** (Rule 14 / production-vs-exploratory
discipline) spanning ≈ 0.4×–5.6× of target. Therefore matching the binding
*magnitude* by choosing a q-dim convention is NOT evidence of a derivation
— almost any target ℓ¹ can be dialled in by the convention.

What this tells the magnitude-side levers (z2bn/thb7/PROBE-2): the binding
ℓ¹ magnitude is a weak discriminator for route (i). The real constraints
are (1) an *independent* principle that FIXES the q-dimension convention
(not chosen to fit), and (2) the SIGN / cancellation structure — the actual
signed sum (net) undershoots at −82.9 % while the fake-degree ℓ¹ overshoots
at +462 % (⁴He), so the missing object must reproduce a *near-total
cancellation* of large q-deformed magnitudes, which the magnitude size
alone does not test.

This is NOT a (b) structural exclusion (no invariant forbids a q-dim
magnitude); it is the scope-(a) observation that route (i) is convention-
under-determined.

Inputs READ from canonical pinned witnesses (mpmath 50 dps on stored y_λ,
χ^λ) — env-skew-immune.

Producer for: computations/delta-lambda-qdim-route-probe.witness.json
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


def n_lambda(part):
    return sum(i * part[i] for i in range(len(part)))


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


def dim_balanced(part, q):
    return _dim_from(part, q, qbal)


def dim_unbalanced(part, q):
    return _dim_from(part, q, qunbal)


def dim_fake(part, q):
    return q**n_lambda(part) * dim_unbalanced(part, q)


CONVENTIONS = {
    "balanced": dim_balanced,
    "unbalanced": dim_unbalanced,
    "fake_degree": dim_fake,
}

M_E_MEV = mpf("0.51099895069")
ISOTOPES = {
    "D":   ("atom-chi-rust-d.witness.json",   "6",  2.224566),
    "T":   ("atom-chi-rust-t.witness.json",   "9",  8.481798),
    "3He": ("atom-chi-rust-3he.witness.json", "9",  7.718043),
    "4He": ("atom-chi-rust-4he.witness.json", "12", 28.295673),
}


def main():
    ywit = os.path.join(HERE, "y-lambda-at-q0.witness.json")
    ydat = json.load(open(ywit))["data"]["by_n"]
    q0 = mpf(json.load(open(ywit))["parameters"]["q_0"])

    rows = []
    span_min = None
    span_max = None
    for name, (chif, nkey, B) in ISOTOPES.items():
        chi = json.load(open(os.path.join(HERE, chif)))["data"]["atom"]["by_partition"]
        yl = {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in ydat[nkey]}
        target = mpf(B) / M_E_MEV
        l1 = {"classic": mpf(0)}
        for conv in CONVENTIONS:
            l1[conv] = mpf(0)
        for e in chi:
            p = tuple(e["partition"]); base = abs(yl[p] * mpf(e["chi_lambda"]))
            l1["classic"] += base * dim_classic(list(p))
            for conv, fn in CONVENTIONS.items():
                l1[conv] += base * abs(fn(list(p), q0))
        ratios = {k: float(v / abs(target)) for k, v in l1.items()}
        for v in ratios.values():
            span_min = v if span_min is None else min(span_min, v)
            span_max = v if span_max is None else max(span_max, v)
        rows.append({"atom": name, "B_AME_MeV": B,
                     "target_units_m_e": float(target),
                     "ceiling_over_target": ratios})

    any_overshoot = any(r["ceiling_over_target"][c] >= 1.0
                        for r in rows for c in CONVENTIONS)
    witness = {
        "engine": "mpmath",
        "engineVersion": "mpmath 50dps on canonical witnesses",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "delta-lambda-qdim-route-probe",
        "scriptFile": "delta_lambda_qdim_route_probe.py",
        "scriptHash": hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12],
        "description": (
            "Route-(i) probe across 3 q-dimension conventions (balanced / "
            "unbalanced / fake-degree). The ℓ¹ ceiling ‖c_q‖₁/|target| is "
            "wildly convention-dependent (⁴He spans 0.41→5.62): balanced "
            "undershoots all isotopes, unbalanced/fake-degree overshoot the "
            "heavy ones. ⟹ route (i) ESCAPES the sign-only prune and is "
            "UNDER-CONSTRAINED — the q-dim convention is a hidden DOF (Rule "
            "14), so magnitude-matching via q-dim is not evidence of a "
            "derivation. The real discriminators: an independent principle "
            "fixing the convention + the sign/cancellation structure (net "
            "−82.9% vs fake-degree ℓ¹ +462% on ⁴He). Scope (a), NOT a (b) "
            "exclusion (no invariant)."
        ),
        "scope": "(a) scope-limited — route (i) is convention-under-determined; q-dim convention is a hidden DOF",
        "conventions": {
            "balanced": "[n]_q!/∏[h]_q, [k]=(q^k-q^-k)/(q-q^-1)",
            "unbalanced": "[n]_q!/∏[h]_q, [k]=(1-q^k)/(1-q)",
            "fake_degree": "q^{n(λ)}·unbalanced, n(λ)=Σ(i-1)λ_i (principal specialization)",
        },
        "parameters": {"q_0": float(q0), "m_e_MeV": float(M_E_MEV)},
        "data": {
            "rows": rows,
            "ceiling_span_across_conventions": [span_min, span_max],
            "some_convention_overshoots_target": any_overshoot,
        },
    }
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "delta-lambda-qdim-route-probe", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
    ).save()

    cols = ["classic"] + list(CONVENTIONS)
    print(f"q_0={float(q0):.5f}   ‖c‖₁(conv)/|target|")
    print(f"{'iso':>4}" + "".join(f"{c:>12}" for c in cols))
    for r in rows:
        print(f"{r['atom']:>4}" + "".join(f"{r['ceiling_over_target'][c]:>12.3f}" for c in cols))
    print(f"\nconvention span {span_min:.2f}–{span_max:.2f}×target; "
          f"some convention overshoots: {any_overshoot} ⟹ route (i) under-constrained (hidden DOF)")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
