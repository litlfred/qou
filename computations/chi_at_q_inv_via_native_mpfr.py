"""Per-block χ^λ at q = q_0^{-1} (the Hecke/KL bar-image of the substrate
anchor) — Rust-engine driver for the bar-pairing observable.

Companion to PR #1742 (`derive_binding_bar_pairing.py`).

#1742's audit
[`docs/audits/2026-06-03-bar-pairing-does-not-improve-binding.md`]
established that:

  - the CATEGORICAL/fibre realization is the Hecke bar `q ↦ q^{-1}`
    (legitimate over any base ring; the Kazhdan-Lusztig involution),
  - the ARCHIMEDEAN observation at the substrate anchor stays
    `|χ(q_0)|` because Im(q_0) = 0 collapses the conjugation bar to
    the modulus,
  - the *mirror pairing* `χ(q_0)·χ(q_0^{-1})` is a TWO-point
    archimedean construction (q_0 and q_0^{-1} are BOTH real
    positive ≠ 1; both legitimate archimedean evaluations on ℝ_{>0}
    — `q-usage` discipline is satisfied at both points).

The #1742 deuteron result (B_bar = −70.3% vs B_arch = +3.6%) needs
extension to T, ³He, ⁴He to confirm the "mirror-pairing underbinds
across the light series" finding.  #1742's note explicitly said
"a Rust per-partition χ kernel would make T/³He/⁴He cheap" — PR
#1748 ships exactly that kernel.

This driver runs `pyhecke_native.chi_lambda_all_partitions_mpfr`
at q = q_0^{-1} and persists to a witness JSON with the `at-qinv`
tag (parallel filename to `chi-{atom}-h{n}-at-q0-50dps.witness.json`),
so the downstream bar-pairing observable can be assembled by a
post-processor that consumes both witnesses.

q-usage discipline (per AGENTS.md §7c):

| q-value                | type        | role                              |
|------------------------|-------------|-----------------------------------|
| q_0 ≈ 1.1098           | real > 1    | substrate anchor (archimedean)    |
| q_0^{-1} ≈ 0.9009      | real, ∈(0,1)| mirror image (also archimedean!)  |
| both                   | Im = 0      | each is its own ℝ-archimedean place |

The bar-pairing `χ(q_0)·χ(q_0^{-1})` is a product of two REAL-
archimedean evaluations, NOT a unit-circle / root-of-unity
construction.  Both points are gap-separated from `|q| = 1` and
respect `lusztig_q_0_imaginary_part_zero`.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401, E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def _q_inv_str(dps: int) -> str:
    """50+ dps decimal-string of q_0^{-1}."""
    with mp.workdps(dps + 5):
        q = mp.mpf(Q_50_DIGIT_STR)
        return mp.nstr(1 / q, dps, strip_zeros=False)


def _word_to_signed(word, *, dps: int = 50):
    """Translate Python `(c, d, g0)` Hecke-factor word to Rust's
    `(sign, g1)` enum, matching chi_at_q0_via_hoefsmit_mpfr.

    The word was CONSTRUCTED at the substrate anchor q_0 — its `d`
    values are in {0, -h_0, -h_0/2} where h_0 = q_0 - q_0^{-1} ≈
    0.2089.  Decoding therefore uses h_0, NOT h(q) for the
    target evaluation point.  The Rust kernel takes the abstract
    sign and substitutes h(q) internally per its q_str argument.

    Comparisons stay in `mp.mpf` at the active dps so upstream
    `mp.mpf` `d_` values are not silently truncated to float64
    before the inter-class gap check (Copilot review PR #1748).
    Tolerance is `mp.mpf("1e-10")` — bounded below by float64 ulp
    noise (~1e-15) on the current upstream `atom_braid_word_3A`
    (which produces float `d_`) and bounded above by the ~0.1
    inter-class gap at substrate q_0.  Future upstream changes to
    return `mp.mpf` `d_` at higher precision will continue to
    decode correctly since the mpf compare avoids the float
    truncation step.
    """
    with mp.workdps(max(dps, mp.mp.dps)):
        q0 = mp.mpf(Q_50_DIGIT_STR)
        h0 = q0 - 1 / q0
        tol = mp.mpf("1e-10")
        out = []
        for c_, d_, g_ in word:
            c_mpf = mp.mpf(str(c_)) if not isinstance(c_, mp.mpf) else c_
            d_mpf = mp.mpf(str(d_)) if not isinstance(d_, mp.mpf) else d_
            if abs(c_mpf - 1) > tol:
                raise ValueError(
                    f"native chi path requires c==1.0, got c={c_}")
            if abs(d_mpf) < tol:
                sgn = 1
            elif abs(d_mpf + h0) < tol:
                sgn = -1
            elif abs(d_mpf + h0 / 2) < tol:
                sgn = 0
            else:
                raise ValueError(
                    f"unrecognised d={d_} (expected 0, -h0, or -h0/2)")
            g1 = int(g_) + 1
            out.append((sgn, g1))
    return out


def run_atom(atom: str, Z: int, N: int, dps: int = 50) -> Path:
    """χ_λ over all partitions of 3A at q = q_0^{-1}, persisted to
    `chi-{atom}-h{n}-at-qinv-50dps.witness.json` (where n = 3·A)."""
    import pyhecke_native as pn

    A = Z + N
    n = 3 * A
    q_inv = _q_inv_str(dps)
    q_inv_f = float(mp.mpf(q_inv))
    word = atom_braid_word_3A(Z, N)
    ws = _word_to_signed(word)
    out_path = HERE / f"chi-{atom}-h{n}-at-qinv-50dps.witness.json"

    print(f"[{atom}] n={n} word={len(ws)}fac dps={dps}  "
          f"q_inv={q_inv[:14]}…  output={out_path.name}", flush=True)
    t0 = time.time()
    rust_out = pn.chi_lambda_all_partitions_mpfr(n, ws, q_inv, dps)
    elapsed = time.time() - t0
    print(f"[{atom}] DONE: {len(rust_out)} partitions in {elapsed:.2f}s",
          flush=True)

    by_partition = []
    for lam, chi_s in rust_out:
        by_partition.append({"partition": list(lam), "chi_lambda": chi_s})
    payload = {
        "computation": f"chi-{atom}-h{n}-at-qinv-50dps",
        "description": (
            f"Numerical χ^λ_q(β_atomic({Z}, {N})) = {atom} per partition "
            f"λ ⊢ {n}, evaluated at q = q_0^{{-1}} ≈ {q_inv_f:.6f} at "
            f"{dps} dps via the pyhecke-native MPFR kernel (PR #1748).  "
            f"Bar-image cache for PR #1742's mirror pairing "
            f"χ(q_0)·χ(q_0^{{-1}}).  Same partition order as the "
            f"sibling `chi-{atom}-h{n}-at-q0-50dps.witness.json`."
        ),
        "q_inv_50dps_str": q_inv,
        "dps": dps,
        "n_strands": n,
        "atom": atom,
        "Z": Z, "N": N,
        "n_partitions": len(by_partition),
        "n_partitions_total": len(by_partition),
        "compute_time_sec": round(elapsed, 2),
        "by_partition": by_partition,
        "_provenance": {
            "engine": "pyhecke_native",
            "rust_fn": "chi_lambda_all_partitions_mpfr",
            "pr_landing_kernel": 1748,
            "pr_consumer": 1742,
        },
    }
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"[{atom}] wrote {out_path.name} ({out_path.stat().st_size} B)",
          flush=True)
    return out_path


def main(argv: list[str]) -> int:
    set_compute_dps()
    ISOTOPES = {
        "deuteron": (1, 1),
        "tritium": (1, 2),
        "helium-3": (2, 1),
        "helium-4": (2, 2),
    }
    if not argv:
        which = list(ISOTOPES)
    else:
        which = argv
    for atom in which:
        if atom not in ISOTOPES:
            print(f"!! unknown atom {atom!r}; valid: {list(ISOTOPES)}",
                  flush=True)
            return 2
        Z, N = ISOTOPES[atom]
        run_atom(atom, Z, N)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
