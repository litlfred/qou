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



def _pn_delta():
    """Colour-weighting delta for the p-n interface (qou-gdtb)."""
    from canonical_braid_crossings import _avg_color_delta
    return _avg_color_delta()

def _q_inv_str(dps: int) -> str:
    """50+ dps decimal-string of q_0^{-1}."""
    with mp.workdps(dps + 5):
        q = mp.mpf(Q_50_DIGIT_STR)
        return mp.nstr(1 / q, dps, strip_zeros=False)


# ── Reproducibility envelope of this producer's chi values (measured, qou-1oxx)
#
# Diffing a regenerated witness against a committed one shows LAST-DIGIT
# movement. Measured, so a future reader does not re-derive it or mistake it
# for a regression:
#
#   within one process   three consecutive kernel calls are BIT-IDENTICAL
#   4-arg vs 5-arg-None  BIT-IDENTICAL (deuteron 11/11, helium-3 30/30), so
#                        the avg_shifts argument added here is NOT a cause
#   across processes     the 50th (last serialised) digit CAN move: tritium
#                        (3,3,2,1) matched main on one run and differed by
#                        1.42e-50 on the next -- same code, same container
#   vs origin/main       the environment also differs. main's committed
#                        witnesses record mpmath 1.3.0 / pyhecke_native_build
#                        c7ea7ebb0d76c4e2; this container is mpmath 1.4.1 /
#                        c85ef99ee89ce1c3. A systematic contributor on top of
#                        the run-to-run effect above, not instead of it.
#
# Largest observed: 4.34e-50 relative (helium-4, 4 of 77 partitions). That is
# ~35 orders below the L1 target of 1e-15, so it bears on nothing -- but do
# NOT claim "byte-identical" as a property of this producer. It has held on
# some runs and not others, and that is luck, not a guarantee.


def _h_at(q):
    """Substrate h(q) = q - 1/q. Sign-FLIPS under the bar: h(1/q) = -h(q)."""
    return q - 1 / q


def _classify_word(word, *, dps: int = 50):
    """Classify each Hecke factor of the q_0-BUILT word as `(sign, gen, kind)`.

    `kind` is `""` for `sign = +-1`, `"blind"` for the colour-symmetric
    average `d = -h_0/2`, and `"weighted"` for the canonical colour-weighted
    p-n interface `d = -h_0*(1/2 - delta(q_0)/4)` (convention R3).

    Classification uses `h_0` because the word's `d` values are pinned at the
    SUBSTRATE anchor -- but the shift handed to the kernel must be REBUILT at
    the target evaluation point (`_avg_shifts_at`).  Carrying `d` across the
    bar is wrong rather than conservative: `h(1/q_0) = -h(q_0)`, so `-h_0/2`
    is not the averaged coefficient at `1/q_0` -- there it is `+h_0/2`.
    Bean `qou-1oxx`; this is why the sign/type representation is NECESSARY
    and not itself the defect.

    The two averaged variants are separated by
    `h_0*delta(q_0)/4 ~ 7.2e-05`, four orders above the 1e-10 tolerance, so
    they are cleanly distinguishable.  The previous version tested them in a
    single `or` and returned one `sign = 0` channel for both, which is what
    made the colour weighting unrecoverable downstream.
    """
    with mp.workdps(max(dps, mp.mp.dps)):
        q0 = mp.mpf(Q_50_DIGIT_STR)
        h0 = _h_at(q0)
        w_pn = mp.mpf(1) / 2 - _pn_delta() / 4
        tol = mp.mpf("1e-10")
        out = []
        for c_, d_, g_ in word:
            c_mpf = mp.mpf(str(c_)) if not isinstance(c_, mp.mpf) else c_
            d_mpf = mp.mpf(str(d_)) if not isinstance(d_, mp.mpf) else d_
            if abs(c_mpf - 1) > tol:
                raise ValueError(
                    f"native chi path requires c==1.0, got c={c_}")
            if abs(d_mpf) < tol:
                sgn, kind = 1, ""
            elif abs(d_mpf + h0) < tol:
                sgn, kind = -1, ""
            elif abs(d_mpf + h0 / 2) < tol:
                sgn, kind = 0, "blind"
            elif abs(d_mpf + h0 * w_pn) < tol:
                sgn, kind = 0, "weighted"
            else:
                raise ValueError(
                    f"unrecognised d={d_} (expected 0, -h0, -h0/2, "
                    f"or -h0*(1/2 - delta/4))")
            out.append((sgn, int(g_) + 1, kind))
    return out


def _avg_shifts_at(classified, q_str: str, *, dps: int = 50,
                   colour_weighted: bool = True):
    """Per-crossing shift strings for the kernel's 5th argument, rebuilt at `q`.

    The kernel evaluates `sigma_g - shift*I` for `sign == 0` and defaults to
    `h(q)/2`.  So `"blind"` reproduces that default exactly, and `"weighted"`
    is `h(q)*(1/2 - delta(q)/4)` with **delta evaluated at q**, never at q_0 --
    `flavor_split_leading` takes q as an argument and is exact at whatever
    precision it is handed.

    Returns `None` when nothing is colour-weighted, which makes the call
    bit-identical to the four-argument form the kernel already defaults to.
    Serialised from the mpf at `dps + 10`, never via float: the shift carries
    delta, and an f64 round-trip would cap chi near 1e-16 however high `dps`
    is set (the same trap `chi_at_q0_via_hoefsmit_mpfr` documents).
    """
    from _li_2_q_util import flavor_split_leading
    with mp.workdps(dps + 15):
        q = mp.mpf(q_str)
        h = _h_at(q)
        blind = h / 2
        weighted = h * (mp.mpf(1) / 2 - flavor_split_leading(q) / 4)
        shifts, any_weighted = [], False
        for sgn, _g, kind in classified:
            if sgn != 0:
                shifts.append("")
            elif kind == "weighted" and colour_weighted:
                any_weighted = True
                shifts.append(mp.nstr(weighted, dps + 10, strip_zeros=False))
            else:
                shifts.append(mp.nstr(blind, dps + 10, strip_zeros=False))
    return shifts if any_weighted else None


def _word_to_signed(word, *, dps: int = 50):
    """Back-compat shim: `(sign, gen)` pairs only, colour weighting DISCARDED.

    Kept so any existing caller keeps working, but new code should use
    `_classify_word` + `_avg_shifts_at`, which preserve the p-n weighting.
    """
    return [(s, g) for s, g, _k in _classify_word(word, dps=dps)]


def run_atom(atom: str, Z: int, N: int, dps: int = 50, *,
             colour_weighted: bool = True) -> Path:
    """chi_lambda over all partitions of 3A at q = q_0^{-1}, persisted to a
    witness JSON.

    Two frames, because a bar-parity probe pairs this against the `at-q0`
    sibling and the two questions it can be asking are different objects
    (bean `qou-1oxx`, owner decision 2026-08-26):

    * `colour_weighted=True` -> `chi-{atom}-h{n}-at-qinv-50dps-colour-weighted`
      the canonical p-n convention (R3), matching what the `at-q0` sibling
      carries.  Pairing the two measures the canonical form's bar DEFECT,
      which is nonzero by construction:
      `bar(f) - f = (q-1)^5 (q+1)^3 (q^2+1) / (12 q^5)`.
    * `colour_weighted=False` -> `chi-{atom}-h{n}-at-qinv-50dps`
      the colour-blind average, which IS the bar-symmetriser and IS
      bar-invariant.  Unchanged computation-id and unchanged values, so every
      existing consumer keeps its current behaviour until it opts in.

    Neither is "the stale one".  The colour-blind frame is a coherent object
    and is arguably the right one for a bar-parity question; what was wrong
    was pairing it against a colour-weighted `at-q0` without saying so.
    """
    import pyhecke_native as pn
    from witness_base import WitnessBuilder

    A = Z + N
    n = 3 * A
    q_inv = _q_inv_str(dps)
    q_inv_f = float(mp.mpf(q_inv))
    word = atom_braid_word_3A(Z, N)
    classified = _classify_word(word, dps=dps)
    ws = [(s, g) for s, g, _k in classified]
    avg_shifts = _avg_shifts_at(classified, q_inv, dps=dps,
                                colour_weighted=colour_weighted)

    # Derive the label from the word, never assert it. The committed witnesses
    # carried `convention_inferred_by: chi_convention_audit.py --fix` with a
    # FILENAME REGEX -- a label about the path, not about the numbers. It
    # happened to be right; nothing in the witness established that.
    n_weighted = sum(1 for _s, _g, k in classified if k == "weighted")
    applied_weighting = bool(avg_shifts) and n_weighted > 0
    convention = ("colour-weighted-averaged-crossing" if applied_weighting
                  else "averaged-crossings")
    suffix = "-colour-weighted" if applied_weighting else ""
    comp_id = f"chi-{atom}-h{n}-at-qinv-50dps{suffix}"
    out_path = HERE / f"{comp_id}.witness.json"

    print(f"[{atom}] n={n} word={len(ws)}fac dps={dps}  "
          f"q_inv={q_inv[:14]}...  convention={convention}  "
          f"weighted_crossings={n_weighted if applied_weighting else 0}  "
          f"output={out_path.name}", flush=True)
    t0 = time.time()
    # `avg_shifts=None` is the kernel's own `h(q)/2` default, so the
    # colour-blind branch stays bit-identical to the four-argument call.
    rust_out = pn.chi_lambda_all_partitions_mpfr(n, ws, q_inv, dps, avg_shifts)
    elapsed = time.time() - t0
    print(f"[{atom}] DONE: {len(rust_out)} partitions in {elapsed:.2f}s",
          flush=True)

    by_partition = [{"partition": list(lam), "chi_lambda": chi_s}
                    for lam, chi_s in rust_out]
    payload = {
        "computation": comp_id,
        "description": (
            f"Numerical chi^lambda_q(beta_atomic({Z}, {N})) = {atom} per "
            f"partition lambda |- {n}, evaluated at q = q_0^-1 ~ "
            f"{q_inv_f:.6f} at {dps} dps via the pyhecke-native MPFR kernel "
            f"(PR #1748).  p-n convention: {convention}.  Bar-image cache "
            f"for the mirror pairing chi(q_0)*chi(q_0^-1).  Same partition "
            f"order as the sibling chi-{atom}-h{n}-at-q0-50dps.witness.json."
        ),
        "convention": convention,
        "convention_derived_from": (
            "the classified braid word, by counting crossings whose d matches "
            "-h_0*(1/2 - delta/4); NOT inferred from the filename"
        ),
        "n_colour_weighted_crossings": n_weighted if applied_weighting else 0,
        "q_inv_50dps_str": q_inv,
        "q_0_50dps": Q_50_DIGIT_STR,
        "dps": dps,
        "n_strands": n,
        "atom": atom,
        "Z": Z, "N": N,
        "n_partitions": len(by_partition),
        "n_partitions_total": len(by_partition),
        "producer": Path(__file__).name,
        # STRING, not a raw float: the raw-float64 ratchet flags this
        # field, and `compute_time_sec` matches neither "dur" nor
        # "elapsed", so the duration carve-out does not and must not
        # cover it -- widening that mask is what the audit's own
        # comment warns against. The `at-q0` sibling has emitted a
        # string here all along; this producer simply never drained it.
        "compute_time_sec": f"{elapsed:.2f}",
        "by_partition": by_partition,
        "_provenance": {
            "engine": "pyhecke_native",
            "rust_fn": "chi_lambda_all_partitions_mpfr",
            "avg_shifts_passed": bool(avg_shifts),
            "pr_landing_kernel": 1748,
            "pr_consumer": 1742,
            "bean": "qou-1oxx",
        },
    }
    # The shift is rebuilt at the TARGET q, so record both what was used and
    # why: `h(1/q_0) = -h(q_0)`, and delta is bar-MIXED
    # (`bar(delta) = -q^2 delta`), so neither factor survives the bar unchanged.
    if avg_shifts:
        payload["_provenance"]["avg_shift_values"] = sorted(
            set(s for s in avg_shifts if s))
    # Stamp scriptHash / scriptCommitSha / q0Anchor rather than hand-rolling.
    # The committed witnesses carried `scriptCommitSha: "unknown"` and
    # `q0Anchor: "ambiguous"` because this producer never called it.
    WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="pyhecke_native")
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
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
        # BOTH frames, every run (owner decision 2026-08-26, bean qou-1oxx).
        # Emitting only one is what created the mismatch this fixes: a
        # consumer then has exactly one object available and pairs it with
        # whatever the `at-q0` side happens to carry, with nothing in either
        # witness saying the two frames differ.
        run_atom(atom, Z, N, colour_weighted=False)
        run_atom(atom, Z, N, colour_weighted=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
