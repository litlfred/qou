#!/usr/bin/env python3
"""Hunt for the FIRST q-difference recurrence of the Borromean rings'
diagonal colored Jones tower J_{B,n} (bean n920 tail; PR #3443).

Input tower: Habiro's cyclotomic formula (verified transcription in
habiro_borromean_colored_jones.py, GL2011 Appendix A):

    J_{B,n} = sum_{l=0}^{n-1} (-1)^l {n}^2
              (prod_{j=1}^l {n+j}{n-j})^3 / (prod_{j=l+1}^{2l+1} {j})^2,
    {j} = s^j - s^{-j},  s = q^{1/2}.

Sought: a nontrivial operator with coefficients Laurent in m := q^n,

    sum_{i=0}^{r} a_i(q, m) J_{B,n+i} = b(q, m)   for all n >= 1,

with a_i, b supported on m^k, k in [-W..W].  q-holonomicity of the
diagonal guarantees SOME (r, W) works (Garoufalidis-Le 2005); the open
question is the minimal window — no Borromean recurrence has ever been
published (link-AJ is formulated-only: Sawabe 2024, Hopf + Whitehead).

Method (mod-p existence certificate, mirroring the corpus's 4_1
construct-verify recipe's mod-p stage):
  1. For several large primes p and several base points s of large
     multiplicative order mod p, evaluate J_{B,n} mod p for n = 1..Nmax
     (exact modular arithmetic, no floats).
  2. For each (r, W) on a grid: build the linear system over F_p in the
     unknown coefficients {c_{i,k}} u {d_k} (inhomogeneous column) with
     FIT rows n = 1..R (R = #unknowns + 20); compute the nullspace.
  3. Existence certificate: nullity >= 1 at EVERY (p, s) sample, and a
     null vector solved on the FIT rows continues to satisfy 30 extra
     CHECK rows (n beyond the fit range) mod p — accidental survival
     probability ~ p^{-30} per sample, so consistent survival across
     samples is decisive *existence* evidence (NOT yet a symbolic
     operator — reconstruction to Z[q^{±1}] coefficients is phase 2).
  4. Report the minimal (r, W) found; scope-(a) negative if the grid
     (r <= R_MAX, W <= W_MAX) has no consistent candidate.

Honesty: this is an existence probe, not a proof; the symbolic
operator + exact symbolic annihilation (the epistemic step the 4_1 /
trefoil transcriptions have) is the follow-up once the window is known.
Audit-only; no wiring.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# three verified primes (2^61-1 Mersenne; largest primes < 2^62, < 2^63)
PRIMES = [2305843009213693951, 4611686018427387847, 9223372036854775783]
SPOINTS = [3, 5, 7]          # small bases; order mod p is astronomically large
R_MAX = 6
W_MAX = 14
CHECK_ROWS = 30


def jones_tower_mod(p: int, s: int, nmax: int) -> list[int]:
    """J_{B,n} mod p for n = 1..nmax (index n-1). Exact modular arithmetic."""
    sinv = pow(s, p - 2, p)
    # brackets {j} = s^j - s^{-j} mod p for j up to 2*nmax
    br = [0] * (2 * nmax + 2)
    sj, sij = 1, 1
    for j in range(1, 2 * nmax + 2):
        sj = sj * s % p
        sij = sij * sinv % p
        br[j] = (sj - sij) % p
        if j <= 2 * nmax and br[j] == 0:
            raise ZeroDivisionError(f"bracket {{{j}}} = 0 mod p (bad s)")
    out = []
    for n in range(1, nmax + 1):
        total = 0
        prod3 = 1          # (prod_{j=1}^{l} {n+j}{n-j})^3, built incrementally
        for l in range(0, n):
            if l > 0:
                f = br[n + l] * br[n - l] % p
                prod3 = prod3 * pow(f, 3, p) % p
            den = 1
            for j in range(l + 1, 2 * l + 2):
                den = den * br[j] % p
            den2inv = pow(den * den % p, p - 2, p)
            term = br[n] * br[n] % p * prod3 % p * den2inv % p
            total = (total - term if l & 1 else total + term) % p
        out.append(total)
    return out


def nullspace_mod(rows: list[list[int]], p: int) -> list[list[int]]:
    """Nullspace basis of the matrix (rows) over F_p, via Gauss-Jordan."""
    if not rows:
        return []
    ncols = len(rows[0])
    m = [r[:] for r in rows]
    pivots = {}
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(m)):
            if m[r][col] % p:
                piv = r
                break
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], p - 2, p)
        m[rank] = [x * inv % p for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col]:
                f = m[r][col]
                m[r] = [(a - f * b) % p for a, b in zip(m[r], m[rank])]
        pivots[col] = rank
        rank += 1
        if rank == len(m):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for c, r in pivots.items():
            v[c] = (-m[r][fc]) % p
        basis.append(v)
    return basis


def build_rows(J: list[int], p: int, s: int, r: int, W: int,
               n_lo: int, n_hi: int) -> list[list[int]]:
    """Rows for n in [n_lo, n_hi]: sum_{i,k} c_{i,k} m^k J_{n+i} - sum_k d_k m^k = 0."""
    rows = []
    q = s * s % p
    for n in range(n_lo, n_hi + 1):
        m = pow(q, n, p)
        minv = pow(m, p - 2, p)
        mk = {0: 1}
        for k in range(1, W + 1):
            mk[k] = mk[k - 1] * m % p
            mk[-k] = mk[-(k - 1)] * minv % p
        row = []
        for i in range(r + 1):
            Jni = J[n + i - 1]
            for k in range(-W, W + 1):
                row.append(mk[k] * Jni % p)
        for k in range(-W, W + 1):        # inhomogeneous column block
            row.append((-mk[k]) % p)
        rows.append(row)
    return rows


def check_vector(v: list[int], J: list[int], p: int, s: int, r: int, W: int,
                 n_lo: int, n_hi: int) -> bool:
    rows = build_rows(J, p, s, r, W, n_lo, n_hi)
    return all(sum(a * b for a, b in zip(row, v)) % p == 0 for row in rows)


def main() -> int:
    t0 = time.time()
    print("\n  Borromean diagonal recurrence hunt (mod-p existence certificate)\n")
    grid_results = {}
    found = None
    for r in range(2, R_MAX + 1):
        for W in range(2, W_MAX + 1):
            nunk = (r + 2) * (2 * W + 1)
            R = nunk + 20
            nmax = R + r + CHECK_ROWS
            ok_all = True
            supports = []
            for p in PRIMES[:2]:
                for s in SPOINTS[:2]:
                    J = jones_tower_mod(p, s, nmax)
                    rows = build_rows(J, p, s, r, W, 1, R)
                    basis = nullspace_mod(rows, p)
                    if not basis:
                        ok_all = False
                        break
                    v = basis[0]
                    if not check_vector(v, J, p, s, r, W, R + 1, R + CHECK_ROWS):
                        ok_all = False
                        break
                    supports.append(frozenset(i for i, x in enumerate(v) if x))
                if not ok_all:
                    break
            grid_results[f"r={r},W={W}"] = {
                "nullity_ge_1_all_samples": ok_all,
                "nullity": len(basis) if ok_all else 0,
            }
            el = time.time() - t0
            print(f"  [grid] r={r} W={W} unknowns={nunk} rows={R} "
                  f"-> {'CANDIDATE' if ok_all else 'empty'}  ({el:.0f}s)")
            if ok_all:
                found = (r, W, len(basis))
                break
        if found:
            break

    verdict: dict
    if found:
        r, W, nullity = found
        # confirm on the remaining (p, s) samples for the found window
        confirms = 0
        nunk = (r + 2) * (2 * W + 1)
        R = nunk + 20
        nmax = R + r + CHECK_ROWS
        for p in PRIMES:
            for s in SPOINTS:
                try:
                    J = jones_tower_mod(p, s, nmax)
                except ZeroDivisionError:
                    continue
                rows = build_rows(J, p, s, r, W, 1, R)
                basis = nullspace_mod(rows, p)
                if basis and check_vector(basis[0], J, p, s, r, W,
                                          R + 1, R + CHECK_ROWS):
                    confirms += 1
        print(f"\n  CANDIDATE: order r={r}, m-window W={W}, nullity={nullity}; "
              f"confirmed on {confirms}/{len(PRIMES)*len(SPOINTS)} (p,s) samples")
        verdict = {
            "found": True,
            "order": r,
            "m_window": W,
            "nullity_at_found_window": nullity,
            "confirmations": f"{confirms}/{len(PRIMES)*len(SPOINTS)}",
            "certificate": (
                f"mod-p nullspace on {R} fit rows survives {CHECK_ROWS} "
                f"check rows beyond the fit range at every sampled (p, s); "
                "accidental-survival probability ~ p^-30 per sample"
            ),
            "scope": (
                "EXISTENCE certificate only — the symbolic operator over "
                "Z[q^{±1}] and its exact symbolic annihilation are phase 2"
            ),
        }
    else:
        print(f"\n  NEGATIVE (scope-a): no operator with r <= {R_MAX}, "
              f"W <= {W_MAX} — the window is insufficient, NOT evidence "
              "against existence (q-holonomicity guarantees a recurrence).")
        verdict = {
            "found": False,
            "scope_a_negative": (
                f"no consistent nullspace for r <= {R_MAX}, W <= {W_MAX}; "
                "constrains the window only — q-holonomicity (garoufalidis-"
                "le-2005) guarantees existence at some larger window"
            ),
        }

    script_path = Path(__file__)
    witness = {
        "engine": f"python {sys.version.split()[0]} (int mod-p, no floats)",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            cwd=script_path.parent).stdout.strip(),
        "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Existence hunt for the first Borromean diagonal colored-Jones "
            "q-difference recurrence, over the verified Habiro tower "
            "(habiro_borromean_colored_jones.py); mod-p nullspace with "
            "beyond-fit-range check rows"
        ),
        "computation": "borromean-diagonal-recurrence-hunt",
        "audit_only": True,
        "search_grid": {"r": f"2..{R_MAX}", "W": f"2..{W_MAX}",
                        "primes": [str(p) for p in PRIMES],
                        "s_points": SPOINTS, "check_rows": CHECK_ROWS},
        "grid_results": grid_results,
        "verdict": verdict,
        "wall_seconds": f"{time.time() - t0:.1f}",
    }
    out = script_path.with_name("borromean-diagonal-recurrence-hunt.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness → {out.name}   wall {witness['wall_seconds']}s\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
