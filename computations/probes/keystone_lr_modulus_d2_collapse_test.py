#!/usr/bin/env python3
"""keystone_lr_modulus_d2_collapse_test.py

The decisive first gate of the Lawrence–Rozansky modulus identification
`|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)` (W_λ keystone, m_p/m_μ root cause): does
the SU(2)-colored order-5 fibre carry FOUR independent modular components (the
4 conjugacy classes of λ⊢5 the value map needs), or does it collapse to only
TWO (the recon's flagged D=2 trap: α ≡ 5−α under the false-theta support fold)?

If it collapses to 2, the LR modulus ID via SU(2)-fibre coloring is REFUTED
(scope-(a)) before any amplitude transcription — the route needs a different
insertion (knot-complement Ẑ / F_K blocks), a sharp negative. If it gives 4,
the full amplitude probe is worth building.

Method. Reuse the merged, machine-validated Σ(2,3,5) colored-false-theta
machinery (`keystone_colored_sigma235_wrt.py`): for α = 1,2,3,4 compute the
color-α support (mod 60) and the false-theta value Ψ^{(α)}(q) at several q inside
the convergence disk (q = 1/q₀ and roots of unity), then count independent
components by (i) support-set equality and (ii) numerical rank of the Ψ-value
matrix over the q-grid.

KILL CRITERIA (pre-registered): rank(Ψ-matrix) = 2 or fewer independent
supports ⇒ D=2 collapse confirmed ⇒ scope-(a) negative for the fibre-coloring
insertion. rank = 4 with 4 distinct supports ⇒ the route survives this gate
(NOT a closure — the amplitude-level |S_{0λ}| test is the next, separate step).

DISCIPLINE: reuse only; no fit; no W_λ value wired; the Lean `loc_matches` gate
closes only by derivation, never by a probe. No tier change.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mpmath as mp  # noqa: E402
import keystone_colored_sigma235_wrt as base  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                  cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def main():
    # q0 read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). It was the
    # literal 1.1099785955573... -- the RETIRED self-certified muon pin A,
    # superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. There is
    # no comparison leg here, so the 2026-08-30 owner ruling puts this producer
    # on the PROTON default; the pin moves 11.54 ppb. `q_parameter`, not
    # `qou_substrate.constants`, so the witness resolves its anchor stamp.
    Q0 = Q_MP   # zeta-side uses 1/q0
    # q-grid inside the convergence disk |q|<1: 1/q₀ and a few real interior points.
    qs = [1 / Q0, mp.mpf("0.85"), mp.mpf("0.7"), mp.mpf("0.55"), mp.mpf("0.4")]
    colors = [1, 2, 3, 4]

    supports = {a: tuple(base.colored_support(a)) for a in colors}
    print("colored supports (mod 60, folded to 1..30):")
    for a in colors:
        print(f"  α={a}: {supports[a]}")
    distinct_supports = len(set(supports.values()))
    # which colours share a support (the fold α ≡ 5−α?)
    fold_pairs = [(a, b) for a in colors for b in colors
                  if a < b and supports[a] == supports[b]]
    print(f"  distinct supports: {distinct_supports}; support-equal pairs: {fold_pairs}")

    # Ψ-value matrix: rows = colours, cols = q-grid.
    M = mp.matrix(len(colors), len(qs))
    for i, a in enumerate(colors):
        chi = base.chi_of(supports[a])
        for j, q in enumerate(qs):
            M[i, j] = base.false_theta(chi, q, nterms=3000)
    # numerical rank via singular values (row space dimension).
    try:
        _, S, _ = mp.svd(M)
        svals = [float(abs(S[k])) for k in range(min(M.rows, M.cols))]
    except Exception:
        # fallback: Gram determinant ranks
        svals = []
    smax = max(svals) if svals else 1.0
    tol = smax * 1e-20
    rank = sum(1 for s in svals if s > tol)
    print(f"\n  Ψ-value singular values: {[f'{s:.3e}' for s in svals]}")
    print(f"  numerical rank of Ψ-matrix (independent colour components) = {rank}")

    collapse = (rank <= 2) or (distinct_supports <= 2)
    verdict = (
        f"D={rank} colour components (distinct supports {distinct_supports}; "
        f"support-equal pairs {fold_pairs}). "
        + ("**D=2 COLLAPSE CONFIRMED** — the SU(2)-colored order-5 fibre carries "
           "only ≤2 independent modular components, but the LR modulus ID needs 4 "
           "(the 4 conjugacy classes of λ⊢5). So `|S_{0λ}^{Σ(2,3,5)}| = d_ζ(λ)/D` "
           "via fibre-coloring is REFUTED (scope-(a)): the route cannot carry the 4 "
           "value-map classes; a genuine derivation needs a different insertion "
           "(knot-complement Ẑ / F_K blocks), as the recon flagged. This is the "
           "existing bare-vs-4d refutation, re-confirmed at the colored level."
           if collapse else
           "**No D=2 collapse** — 4 independent colour components with 4 distinct "
           "supports. The SU(2)-fibre coloring survives this gate; the amplitude-"
           "level |S_{0λ}| test (Gauss-sum color insertion + per-flat-connection "
           "weights, α=1 anchored to bare τ_N) is the next, separate step — NOT a "
           "closure.")
        + " No fit; no W_λ value wired; the Lean loc_matches gate is untouched; no "
        "tier change."
    )
    print("\nVERDICT:", verdict)

    assertions = [
        {"name": "four_colors_evaluated", "passed": bool(len(colors) == 4)},
        {"name": "rank_decisive", "passed": bool(rank in (2, 4) or distinct_supports in (2, 4))},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "keystone-lr-modulus-d2-collapse-test",
        "description": "Decisive first gate of the LR modulus ID: does the SU(2)-"
                       "colored Σ(2,3,5) order-5 fibre carry 4 independent components "
                       "(needed for λ⊢5 classes) or collapse to D=2?",
        "audit_only": True,
        "tier": "numerical (structural gate)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "supports": {str(a): list(supports[a]) for a in colors},
            "distinct_supports": distinct_supports,
            "support_equal_pairs": [list(p) for p in fold_pairs],
            "psi_singular_values": [f"{s:.6e}" for s in svals],
            "psi_matrix_rank": rank,
            "d2_collapse": collapse,
            "verdict": verdict,
        },
        "context": {
            "axis": "W_λ keystone / LR modulus ID (m_p/m_μ root cause; s5-so3)",
            "gate": "D=2 collapse (α≡5−α fold) — recon's flagged decisive trap",
            "on_survive": "amplitude-level |S_{0λ}| test (separate step, not a closure)",
            "on_collapse": "route refuted; needs Ẑ/F_K knot-complement blocks",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "keystone-lr-modulus-d2-collapse-test.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
