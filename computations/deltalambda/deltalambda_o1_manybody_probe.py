#!/usr/bin/env python3
"""
The residual O(1) factor in Δ_λ = O(1)·sgn·dim(λ) is NOT a categorical constant —
it is the missing MANY-BODY (α-saturation) binding term. Formalize-first NEGATIVE
result: it prunes the "single O(1) constant" and "topological O(1)" hypotheses before
any fit, and re-identifies the residual as the known-open Subgoal-1 many-body term
(operator-valued branching combiner). No fit; nothing wired.

Context: #3569 showed the A-stability criterion selects Δ_λ = sgn·dim (classical q=1
dim); the residual target/B(dim) is D 5.9, T 4.4, ³He 3.3, ⁴He 9.3 (spread 2.8x).
The tempting next move is to fit that residual with a per-nucleon / color / interface
O(1). Per the Δ_λ gate ("do not propose a seventh fit-based ansatz") + formalize-first,
this probe instead PRUNES the constant hypothesis and identifies the structure.

Three structural facts (parameter-free; reuse atom-chi-rust + validated y_λ):

  A1. n_strands = 3A EXACTLY (D:6, T:9, ³He:9, ⁴He:12) — the color-triplet ×3 per
      nucleon, already baked into the braid. So "color ×3" is NOT a free residual
      factor; it is already in χ^λ(β_K).

  A2. T and ³He share IDENTICAL braid topology (n_strands=9, n_partitions=30) yet have
      DIFFERENT residuals (4.4 vs 3.3, >20% apart). So the residual is NOT a function
      of braid topology — it cannot be a single topological O(1) constant. (A single
      constant leaves a 2.8x cross-isotope spread — it does not close.)

  A3. B(dim) is SUB-linear in A (|B_dim|: 0.38, 1.91, 2.34, 3.04 MeV) while B_AME is
      SUPER-linear (2.22, 8.48, 7.72, 28.30) — the α-particle enhancement. The residual
      B_AME/|B(dim)| is MAXIMAL (9.3) exactly at the doubly-magic ⁴He, where B_AME/A
      peaks (7.07) but B(dim)/A is flat (~0.76). So the residual tracks the many-body
      α-SATURATION, not an isotope-independent coefficient.

Conclusion (formalize-first, NO fit): the residual "O(1)" is the size of the missing
many-body binding term (AGENTS.md: "a trace object is already many-body; the probe
measures the size of the missing higher term"). A single Jones–Markov trace tr_M(β_K)
is a 2-body-like object; the α enhancement is 4-body saturation. Deriving the residual
= deriving the operator-valued branching combiner (the KNOWN-OPEN Subgoal-1 closure
path in docs/precision-goals.md), NOT fitting a constant. Scope-(a) magnitude-limited;
nothing wired.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
from math import factorial

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (os.path.join(_ROOT, "computations"),
           os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

B_AME_MEV = {"d": "2.22452", "t": "8.48180", "3he": "7.71804", "4he": "28.29567"}
M_E_MEV = "0.51099895000"
A_OF = {"d": 2, "t": 3, "3he": 3, "4he": 4}


def n_lambda(lam):
    return sum(i * p for i, p in enumerate(lam))


def _hooks(lam):
    hs = []
    for r, rl in enumerate(lam):
        for c in range(rl):
            arm = rl - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            hs.append(arm + leg + 1)
    return hs


def dim_ordinary(lam):
    prod = 1
    for h in _hooks(lam):
        prod *= h
    return factorial(sum(lam)) // prod


def main():
    set_compute_dps()
    from wedderburn_jones_markov import y_lambda_at
    try:
        from qou_substrate.constants import q_at
        q0 = mp.mpf(str(q_at(30)))
        q0src = "qou_substrate.q_at(30)"
    except Exception:                                # noqa: BLE001 (substrate optional in sandbox)
        q0 = mp.mpf("1.1099785827513808076")
        q0src = "fallback (q_at proton pin, hardcoded high-precision)"

    me = mp.mpf(M_E_MEV)
    isos = ["d", "t", "3he", "4he"]
    rows = {}
    for iso in isos:
        with open(os.path.join(_ROOT, "computations", f"atom-chi-rust-{iso}.witness.json")) as f:
            atom = json.load(f)["data"]["atom"]
        n = atom["n_strands"]
        npart = atom["n_partitions"]
        yd = y_lambda_at(n, q0)
        B = mp.mpf(0)
        for e in atom["by_partition"]:
            lam = tuple(e["partition"])
            B += mp.mpf(str(yd[lam])) * mp.mpf(e["chi_lambda"]) * \
                ((-1) ** (n_lambda(lam) % 2)) * dim_ordinary(lam)
        Bmev = me * B
        A = A_OF[iso]
        bame = mp.mpf(B_AME_MEV[iso])
        rows[iso] = {
            "A": A, "n_strands": n, "n_partitions": npart,
            "B_dim_MeV": float(Bmev), "B_AME_MeV": float(bame),
            "residual": float(bame / abs(Bmev)),
            "B_AME_per_A": float(bame / A), "B_dim_per_A": float(abs(Bmev) / A),
        }

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # A1: n_strands = 3A exactly (color ×3 per nucleon).
    check("n_strands_is_3A_color_triplet",
          all(rows[iso]["n_strands"] == 3 * rows[iso]["A"] for iso in isos),
          "n_strands = 3A for all four (" +
          ", ".join(f"{iso}:{rows[iso]['n_strands']}=3·{rows[iso]['A']}" for iso in isos) +
          ") — the color triplet is already in the braid, NOT a free residual factor")

    # A2: T and ³He share braid topology but differ in residual => not topological.
    topo_same = (rows["t"]["n_strands"] == rows["3he"]["n_strands"] and
                 rows["t"]["n_partitions"] == rows["3he"]["n_partitions"])
    resid_diff = abs(rows["t"]["residual"] - rows["3he"]["residual"]) / \
        min(rows["t"]["residual"], rows["3he"]["residual"])
    check("residual_not_topological_TvsHe3",
          topo_same and resid_diff > 0.20,
          f"T and ³He share braid topology (n_strands=9, n_partitions=30) but residuals "
          f"differ {rows['t']['residual']:.2f} vs {rows['3he']['residual']:.2f} "
          f"({resid_diff*100:.0f}%) => residual is NOT a topological O(1) constant")

    # A3: residual maximal at doubly-magic ⁴He (α-saturation), where B_AME/A peaks but
    #     B_dim/A does not => residual = missing many-body term, not a constant.
    resid_max_iso = max(isos, key=lambda i: rows[i]["residual"])
    bame_per_A_max = max(isos, key=lambda i: rows[i]["B_AME_per_A"])
    bdim_per_A_max = max(isos, key=lambda i: rows[i]["B_dim_per_A"])
    check("residual_max_at_alpha_manybody",
          resid_max_iso == "4he" and bame_per_A_max == "4he" and bdim_per_A_max != "4he",
          f"residual max at {resid_max_iso} (⁴He, {rows['4he']['residual']:.1f}); "
          f"B_AME/A max at {bame_per_A_max} (α-saturation) but B_dim/A max at {bdim_per_A_max} "
          "(NOT ⁴He) => the residual is the missing many-body α-saturation term, not a constant")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "THE O(1) RESIDUAL IS THE MISSING MANY-BODY TERM, NOT A CONSTANT (formalize-first "
        "NEGATIVE, no fit): (A1) n_strands=3A exactly — color ×3 is already in the braid, not "
        "a free factor; (A2) T and ³He share braid topology but differ in residual (4.4 vs 3.3) "
        "— the residual is NOT topological, so a single constant cannot close it (leaves the "
        "2.8x spread); (A3) B(dim) is sub-linear while B_AME is super-linear, and the residual "
        "is MAXIMAL at the doubly-magic ⁴He (α-saturation) where B_AME/A peaks but B_dim/A does "
        "not. So the residual is the SIZE of the missing many-body binding term — a single "
        "Jones–Markov trace tr_M(β_K) is a 2-body-like object; the α enhancement is 4-body "
        "saturation. Deriving it = deriving the operator-valued branching combiner (the "
        "KNOWN-OPEN Subgoal-1 closure path), NOT fitting a seventh O(1) ansatz. Scope-(a) "
        "magnitude-limited. NOTHING WIRED."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "deltalambda-o1-manybody-residual",
        "description": "The O(1) residual in Δ_λ=O(1)·sgn·dim is the missing many-body "
                       "(α-saturation) term, NOT a categorical constant: n_strands=3A (color "
                       "already in braid), T/³He share topology but differ (not topological), "
                       "residual max at doubly-magic ⁴He (α-saturation). Deriving it = the "
                       "known-open operator-valued branching combiner, not a fit. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-11-deltalambda-o1-manybody-residual.md",
        "tier": "measurement (reuses atom-chi-rust χ + validated y_lambda_at; AME targets)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "q0": mp.nstr(q0, 20), "q0_source": q0src,
        "assertions": assertions, "allPassed": all_passed,
        "result": {"per_isotope": rows, "verdict": verdict},
        "context": {
            "follows": "deltalambda-binding-a-scaling.witness.json (#3569)",
            "prunes": "the 'single O(1) constant' and 'topological O(1)' hypotheses for the residual",
            "reidentifies": "the residual as the coarse per-isotope shadow of the ALREADY-quantified "
                            "connected-cumulant deficit (probes/b4-framework-connected-cumulant-deficit "
                            "b4=6.3%, b3 wrong-signed; probes/pairwise_magnitude_gap_probe ~40% at A=3)",
            "concrete_open": "the [1^4] Slater↔trace dictionary (Λ^A(4) nucleon-flavor) closing the b4 "
                             "deficit — the operator-valued branching combiner (Subgoal-1)",
            "gate": "Δ_λ gate — formalize-first NEGATIVE; no seventh fit-based ansatz; nothing wired",
        },
    }
    out = os.path.join(_HERE, "deltalambda-o1-manybody-residual.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
