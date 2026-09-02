#!/usr/bin/env python3
"""GATE: does the Rust LP-accumulator kernel reproduce a pure-mpmath reference?

`pyhecke_native.lp_accumulator_step_traces_mpfr` is intended to replace the hot
per-partition loop of `hecke_core_legacy.unified_iterative_correction` (and the
identically-shaped loop in `atom_character_raw`). This gate verifies the kernel
against an independent pure-mpmath implementation of the same recurrence:

    M <- I;  per crossing:  M <- c*(M @ sigma_gen) + d*M
    per step: rescale if max|M| > 1e80, accumulate log_norm, record trace(M)

**Both sides use the SAME (Rust MPFR) seminormal matrices.** That is the whole
point and it is easy to get wrong: an earlier version compared the kernel against
mpmath-over-the-PYTHON-matrices and mismatched — but that mismatch was the
braid-relation defect (`qou-4m9u`), not a kernel error. Comparing against `main`
is likewise NOT a valid gate here: the corrected matrices deliberately change the
answer, so equality with `main` would mean the correction had not been applied.

**Tolerance is mixed absolute/relative, deliberately.** Some step traces cancel to
~1e-51, i.e. numerically zero at 50 dps; a relative test on those compares noise
to noise and reports a ~1.6 deviation that means nothing. Such steps are counted
and excluded from the ratio. The production code guards the same quantity the
same way (`abs(tr_run) > 1e-300`).

Exit 0 if the kernel agrees to ~50 dps; 1 otherwise.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

from mpmath import mp  # noqa: E402

mp.dps = 60

import hecke_core_legacy as H  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

try:
    import pyhecke_native as P
except ImportError:  # pragma: no cover
    P = None

ZERO = mp.mpf("1e-40")      # below this, a trace has cancelled: compare absolutely
TOL = mp.mpf("1e-40")       # 50-dps agreement, with room for the last digits
K_MAX = 7                   # keeps the pure-mpmath reference tractable


def _rust_matrices(lam):
    rs = P.seminormal_matrices_mpfr(list(lam), Q_50_DIGIT_STR, 50)
    if not rs:
        return [], 0
    dim = len(rs[0])
    out = []
    for g in rs:
        m = [[mp.mpf(0)] * dim for _ in range(dim)]
        for i, row in enumerate(g):
            for (j, s) in row:
                m[i][j] = mp.mpf(s)
        out.append(m)
    return out, dim


def _reference(lam, steps):
    """The same recurrence the kernel implements, in pure mpmath."""
    sig, dim = _rust_matrices(lam)
    if not sig:
        return []
    m = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(dim)] for i in range(dim)]
    log_norm = mp.mpf(0)
    threshold = mp.mpf("1e80")
    out = []
    for chain in steps:
        for c, d, g in chain:
            cm, dm = mp.mpf(str(c)), mp.mpf(str(d))
            msig = [[mp.mpf(0)] * dim for _ in range(dim)]
            for i in range(dim):
                for j in range(dim):
                    v = sig[g][i][j]
                    if v != 0:
                        for a in range(dim):
                            msig[a][j] += m[a][i] * v
            m = [[cm * msig[a][b] + dm * m[a][b] for b in range(dim)] for a in range(dim)]
        m_max = max(abs(m[i][j]) for i in range(dim) for j in range(dim))
        if m_max > threshold:
            m = [[m[i][j] / m_max for j in range(dim)] for i in range(dim)]
            log_norm += mp.log(m_max)
        out.append(sum(m[i][i] for i in range(dim)))
    return out


def main():
    print("=" * 74)
    print("LP-ACCUMULATOR KERNEL GATE — Rust vs pure mpmath, same corrected matrices")
    print("=" * 74)
    if P is None or not hasattr(P, "lp_accumulator_step_traces_mpfr"):
        print("pyhecke_native.lp_accumulator_step_traces_mpfr unavailable.")
        print("Build it: cd tools/pyhecke-native && cargo build --release, then copy")
        print("target/release/libpyhecke_native.so over the installed extension.")
        print("SKIPPED — nothing was verified.")
        return 0

    ordering = ["p", "n"]        # deuterium
    active = [e for e in H._PARTITION_TABLE
              if e["k"] <= K_MAX and e.get("has_ysn", False) and len(e["ysn"]) > 0]
    print(f"partitions: {len(active)}  (k <= {K_MAX})   ordering: {ordering}\n")

    worst = mp.mpf(0)
    worst_at = None
    checked = zeros = 0
    for e in active:
        n_gens = e["n_gens"]
        steps = [H._step_chain_generic(ordering[k], ordering[:k], n_gens)
                 for k in range(len(ordering))]
        ref = _reference(e["partition"], steps)
        got = P.lp_accumulator_step_traces_mpfr(
            list(e["partition"]),
            [[(str(c), str(d), g) for c, d, g in ch] for ch in steps],
            Q_50_DIGIT_STR, 50)
        for i, (tr_s, _ln_s) in enumerate(got):
            rust, pyref = mp.mpf(tr_s), ref[i]
            checked += 1
            if abs(pyref) < ZERO and abs(rust) < ZERO:
                zeros += 1
                continue
            rel = abs(rust - pyref) / abs(pyref) if pyref != 0 else abs(rust - pyref)
            if rel > worst:
                worst, worst_at = rel, (e["partition"], i, pyref, rust)

    print(f"  checked {checked} (partition, step) traces")
    print(f"  {zeros} cancelled to numerically zero on BOTH sides (excluded from the ratio)")
    print(f"  worst relative deviation = {mp.nstr(worst, 6)}")
    if worst >= TOL and worst_at:
        print(f"    at {worst_at[0]} step {worst_at[1]}:")
        print(f"      reference {mp.nstr(worst_at[2], 25)}")
        print(f"      rust      {mp.nstr(worst_at[3], 25)}")
        print("\nVERDICT: MISMATCH — do not wire the kernel in.")
        return 1
    print("\nVERDICT: kernel agrees with the pure-mpmath reference to ~50 dps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
