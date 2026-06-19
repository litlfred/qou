#!/usr/bin/env python3
"""⁵He Wedderburn-block saturation profile — which λ⊢15 blocks carry tr_M.

Follow-on to the A=5 combiner cross-check (#2459). The scalar fine-Bratteli
transfer gives `tr_M = Σ_λ y_λ χ^λ` but discards *which* Wedderburn blocks the
bound state saturates — the structural content the A-operator combiner preserves
(cost-wall doc "Honest framing"). This probe makes that structure explicit for
⁵He: it ranks the H₁₅ irreducible blocks λ⊢15 by their signed share of `tr_M`.

The per-λ characters are taken from the **exact** (50-dps) transfer
(`reduced_block_kernel.chi_all_lambda_reduced_block`) — the same object the
combiner was shown (#2459) to reproduce to machine precision — so the profile is
exact and fast (no ρ_ξ build needed). The Wedderburn weights are the canonical
`y_λ` (`wedderburn_jones_markov.y_lambda_at`, the production Jones–Markov weight).

No production value changes; descriptive structural audit. No fit.

Run: `python3 -u aoperator_a5_block_profile.py 2>&1 | tee /tmp/a5prof.log`
"""
from __future__ import annotations

import datetime
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parents[1]               # computations/
for p in (str(HERE), str(HERE / "a_operator"), str(HERE / "substrate")):
    sys.path.insert(0, p)

import a_operator_categorical as aoa            # noqa: E402
from lr_coefficients import partitions_of       # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0                 # noqa: E402

DPS = 50
mp.mp.dps = 60


def main() -> int:
    q = aoa.q0_mp(DPS)
    print(f"q₀={mp.nstr(q, 12)}  dps={DPS}\n", flush=True)

    w5 = atom_braid_word_3A(2, 3)               # ⁵He: 5 nucleons (2 p, 3 n)
    chi = {tuple(k): mp.mpf(str(v)) if not isinstance(v, mp.mpf) else v
           for k, v in chi_all_lambda_reduced_block(w5, 15, q=None).items()}
    y = {tuple(k): (v if isinstance(v, mp.mpf) else mp.mpf(str(v)))
         for k, v in y_lambda_at(15, Q0).items()}
    pdim = aoa.partition_dim

    contrib = {lam: y[lam] * chi[lam] for lam in chi}
    trM = mp.fsum(contrib.values())
    absT = mp.fsum(abs(c) for c in contrib.values())   # L1 mass (for spread)

    ranked = sorted(contrib, key=lambda l: -abs(contrib[l]))
    print(f"tr_M(⁵He) = {mp.nstr(trM, 12)}   "
          f"Σ|y_λ χ^λ| = {mp.nstr(absT, 12)}  (signed/L1 = {mp.nstr(trM/absT, 4)})")
    print(f"#blocks λ⊢15 = {len(chi)}\n")
    print(f"{'rank':>4} {'λ':<26} {'d_λ':>6} {'y_λ':>12} {'χ^λ':>12} "
          f"{'y_λχ^λ':>13} {'share%':>8} {'cum%':>7}")
    cum = mp.mpf(0)
    rows = []
    for i, lam in enumerate(ranked):
        c = contrib[lam]
        share = c / trM * 100
        cum += share
        if i < 20 or abs(share) > mp.mpf("0.5"):
            print(f"{i+1:>4} {str(lam):<26} {pdim(lam):>6} "
                  f"{mp.nstr(y[lam],5):>12} {mp.nstr(chi[lam],5):>12} "
                  f"{mp.nstr(c,6):>13} {mp.nstr(share,4):>8} {mp.nstr(cum,4):>7}")
        rows.append({"lambda": list(lam), "d_lambda": int(pdim(lam)),
                     "y": float(y[lam]), "chi": float(chi[lam]),
                     "contrib": float(c), "share_pct": float(share)})

    # how many top blocks make up 90% / 99% of the signed tr_M
    cum = mp.mpf(0)
    n90 = n99 = None
    for i, lam in enumerate(ranked):
        cum += contrib[lam] / trM
        if n90 is None and abs(cum) >= mp.mpf("0.90"):
            n90 = i + 1
        if n99 is None and abs(cum) >= mp.mpf("0.99"):
            n99 = i + 1
            break
    top = ranked[0]
    print(f"\nDominant block: λ={top} (d_λ={pdim(top)}), "
          f"{mp.nstr(contrib[top]/trM*100,4)}% of tr_M")
    print(f"Blocks for 90% of tr_M: {n90}/{len(chi)};  for 99%: {n99}/{len(chi)}")

    # Row-count aggregation — the connection to #2406 (a finite colour-SU(N)
    # arena = partitions with ≤ N rows; #2406: colour-ℂ³ (≤3-row) misses 3.4%
    # @⁴He). Reports how much of tr_M each row-count shell carries.
    from collections import defaultdict
    byrows: dict = defaultdict(lambda: mp.mpf(0))
    for lam in contrib:
        byrows[len(lam)] += contrib[lam]
    print("\ntr_M share by #rows of λ (finite colour-SU(N) arena = ≤N rows):")
    cumr = mp.mpf(0)
    rowshare = {}
    for r in sorted(byrows):
        sh = byrows[r] / trM * 100
        cumr += sh
        rowshare[r] = float(sh)
        print(f"  {r}-row: {mp.nstr(sh,4):>9}%   (≤{r}-row cum {mp.nstr(cumr,6)}%)")
    le2 = sum(rowshare.get(r, 0.0) for r in (1, 2))
    le3 = le2 + rowshare.get(3, 0.0)
    print(f"  ⇒ ≤2-row (SU(2)/TL shadow): {le2:.3f}%;  ≤3-row (colour ℂ³): "
          f"{le3:.3f}%;  ≥4-row (beyond ℂ³): {100 - le3:.3f}%")

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _sha(),
        "description": "⁵He Wedderburn-block saturation profile: λ⊢15 ranked by "
                       "signed share of tr_M = Σ_λ y_λ χ^λ (exact transfer χ^λ).",
        "q0": mp.nstr(q, DPS),
        "trM": float(trM),
        "L1_mass": float(absT),
        "n_blocks": len(chi),
        "dominant_lambda": list(top),
        "dominant_share_pct": float(contrib[top] / trM * 100),
        "blocks_for_90pct": n90,
        "blocks_for_99pct": n99,
        "share_by_rowcount_pct": {int(r): rowshare[r] for r in rowshare},
        "le2row_pct": float(le2),
        "le3row_pct": float(le3),
        "ge4row_pct": float(100 - le3),
        "ranking": rows,
        "auditOnly": True,
    }
    wpath = Path(__file__).with_suffix("").as_posix() + ".witness.json"
    Path(wpath).write_text(json.dumps(witness, indent=2))
    print(f"\nwitness → {wpath}", flush=True)
    return 0


def _sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE)).decode().strip()
    except Exception:
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
