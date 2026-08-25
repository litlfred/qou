#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical χ^λ at q = q_0, not symbolic.
"""Numerical per-irrep χ^λ_q(β_atomic) cache at q_0 (50 dps).

Optimization of the symbolic chi cache emitted by
`per_irrep_pole_atom.py` for callers that only need the canonical
|tr_M| at q_0 (e.g. `canonical_tr_m_via_chi_cache.py`,
`cross_check_trM_1ppb.py`'s third path). The symbolic cache
remains the source of truth for pole-order analysis
(`prop:per-nucleon-shift-additive-linearity` via q → u²
substitution); this script provides the **numerical-only**
counterpart, built **~100× faster** by skipping the symbolic poly
arithmetic.

The per-λ χ^λ values are extracted from the existing
[`tr_M_via_wenzl_bridge_mpfr`](./tr_m_wenzl_bridge_mpfr.py) call
with `return_breakdown=True`. That function already computes
χ^λ(β; q_0) in the Hoefsmit seminormal basis at 50 dps for every
λ ⊢ n; we just expose the per-λ table.

Per-atom timing (single-thread, mpmath @ 50 dps):
  - proton/neutron (H_3, 3 partitions): seconds
  - deuteron (H_6, 11 partitions): seconds
  - tritium / ³He (H_9, 30 partitions): minutes
  - ⁴He (H_12, 77 partitions): tens of minutes — feasible

Output: `chi-{atom}-h{n}-at-q0-50dps.witness.json` — separate from
the symbolic `chi-{atom}-h{n}.witness.json`. The `canonical_tr_m_via_chi_cache.py`
combiner prefers the numerical cache when present.
"""
from __future__ import annotations

import hashlib

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from per_irrep_pole_atom import ATOMS, ATOM_ALIASES, parts_of  # noqa: E402
from q_parameter import Q as Q_0_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    anchor_of_q0,
    _build_seminormal_matrices_mpf,
    _chi_lambda_of_word_mpf,
    _load_y_lambda,
    load_y_lambda_for_q0,
    tr_M_via_wenzl_bridge_mpfr,
)
from witness_base import WitnessBuilder  # noqa: E402


def _save_partial(out_path: Path, payload: dict) -> None:
    """Atomic incremental save — write to a temp file, then rename
    so an interrupt mid-write can't leave the witness corrupted.
    """
    tmp = out_path.with_suffix(out_path.suffix + ".partial")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    tmp.replace(out_path)


def build_chi_cache_at_q0(
    atom_name: str, Z: int, N: int, q_str: str, *, dps: int = 50,
    incremental: bool = True, fresh: bool = False,
) -> dict:
    """Return per-λ χ^λ(β_atomic(Z, N); q_0) at 50 dps.

    When ``incremental=True`` (default), loops over partitions of n
    one at a time, building Hoefsmit seminormal matrices at q = q_0
    numerically and computing the per-partition χ. Each completed
    partition is **persisted to disk immediately** via
    `chi-{atom}-h{n}-at-q0-50dps.witness.json`, so a SIGTERM /
    timeout / OOM mid-loop preserves the work done so far.
    Re-running picks up where it left off.

    When ``incremental=False``, falls through to a single call to
    `tr_M_via_wenzl_bridge_mpfr(return_breakdown=True)` — faster for
    small atoms (no per-iteration JSON write overhead) but loses all
    work on interrupt. Used by tests and the cheap-atom default.
    """
    n = 3 * (Z + N)
    word = atom_braid_word_3A(Z, N)
    # Upgrade the color-weighted p-n crossing's δ from the word's f64 value
    # to full mpf precision. atom_braid_word_3A casts δ=_avg_color_delta()
    # to float (mass_at_3A_proper L300); the seminormal χ slow path would
    # then carry only ~f64 precision in the δ term, capping inter-method
    # agreement with markov_peel at ~1.5e-15·(#crossings). markov_peel
    # re-derives δ symbolically (exact), so we restore the exact mpf
    # d = −h·(½ − δ/4) here to match it. Distinct from the color-blind
    # −h/2 by ~7e-5, so a 1e-9 match window is unambiguous. A=1 atoms have
    # no inter-nucleon crossing → no match → word unchanged.
    n_colour_weighted = 0
    try:
        # δ from the closed form at THIS q₀, not from `_avg_color_delta()`.
        #
        # That accessor evaluates δ at the float64 `q_parameter.Q`, so it
        # reaches only ~5e-16 relative — its own docstring says so, and
        # AGENTS.md §"q₀ anchor convention" directs deep-1ppQ callers to
        # `flavor_split_leading(local_q0_50dps)` instead, the same closed form
        # taking q as an argument.
        #
        # It is a small term and it still dominated the floor: δ enters as
        # −h·(½ − δ/4), so the δ/4 piece is ~6.9e-4 of the offset and a 1e-16
        # error in δ lands at ~7e-20 on the result. Measured — with exact
        # crossings but this accessor still in place, deuteron, tritium and
        # helium-3 all sat at exactly 3.476e-20, the same value for three
        # different atoms, which is the signature of a shared input rather
        # than anything atom-specific. A=1 atoms have no p-n crossing, never
        # touch δ, and reached ~1e-50 in the same run.
        from _li_2_q_util import flavor_split_leading
        _qm = mp.mpf(q_str)
        _hm = _qm - mp.mpf(1) / _qm
        _cw_d = -_hm * (mp.mpf(1) / 2 - flavor_split_leading(_qm) / 4)
        _cw_f64 = float(_cw_d)
        n_colour_weighted = sum(1 for (_, d, _) in word
                                if abs(float(d) - _cw_f64) < 1e-9)

        # Upgrade EVERY crossing offset to exact mpf, not just the
        # colour-weighted one.
        #
        # `atom_braid_word_3A` returns `d` as a Python float, so each offset
        # carries ~17 good digits into a 50-dps computation. This block used to
        # replace only the colour-weighted p-n crossing, leaving the plain
        # averaged (-h/2) and inverse (-h) crossings at float64 — and A=1 atoms,
        # which have no p-n crossing at all, kept a wholly float64 word.
        #
        # That is the ~1e-16 floor (bean qou-gpwk). Measured on the proton:
        # the word carries d = -0.10453014939781968 where -h/2 is
        # -0.10453014939781965771542310656…, and the stored χ then sat
        # 4.976e-17 off a native recompute that passes exact crossing codes.
        # The dual-path cross-check bottomed out at ~1e-16 for every atom
        # instead of the ~1e-19 the muon layer reached.
        #
        # Matched by nearest float64 rather than by index: the word's own
        # values are the only statement of which crossing is which, and the
        # three exact candidates are ~7e-5 apart, so a 1e-9 window is
        # unambiguous. Anything unrecognised is left alone rather than snapped
        # to a guess.
        _exact = [(mp.mpf(0), 0.0), (-_hm, float(-_hm)),
                  (-_hm / 2, float(-_hm / 2)), (_cw_d, _cw_f64)]

        def _upgrade(d):
            for exact, approx in _exact:
                if abs(float(d) - approx) < 1e-9:
                    return exact
            return d

        word = [(c, _upgrade(d), g) for (c, d, g) in word]
    except Exception:
        pass  # import miss / unexpected shape → leave word as-is
    # Derive the convention label from the word instead of asserting it. Both
    # payloads below used to hardcode "averaged-crossings" while this block
    # installs the colour-weighted p-n crossing — so every A>=2 cache shipped a
    # label contradicting its own numbers, which
    # `chi_convention_from_values_audit` then had to detect by recomputation
    # (deuteron, tritium, helium-3 all MISLABELLED). Repairing the witnesses
    # without repairing this would have been undone by the next rebuild; this
    # run regressed helium-4's one correct label exactly that way.
    #
    # A=1 atoms have no inter-nucleon crossing, so nothing is substituted and
    # colour-blind is the honest label for them — which is why this is counted
    # rather than assumed from the atom.
    convention = ("colour-weighted-averaged-crossing" if n_colour_weighted
                  else "averaged-crossings")
    t0 = time.time()

    if not incremental:
        result = tr_M_via_wenzl_bridge_mpfr(
            word, n, q_str, dps=dps, return_breakdown=True,
        )
        elapsed = time.time() - t0
        return {
            "atom": atom_name,
            "Z": Z, "N": N,
            "n_strands": n,
            "n_partitions": result["n_partitions_used"],
            "n_partitions_total": len(list(parts_of(n))),
            "partial": result["n_partitions_used"] < len(list(parts_of(n))),
            "convention": convention,
            # wall clock, not a measurement: string keeps raw float64 out of
            # the witness and stops per-run jitter rewriting the file
            "compute_time_sec": f"{elapsed:.2f}",
            "tr_M_at_q0": result["tr_M"],
            "by_partition": result["by_partition"],
        }

    # Incremental path — partition-by-partition with per-step save.
    #
    # OFF-ANCHOR q GETS ITS OWN FILE (2026-08-23, bean `qou-8chw`). The cache
    # path used to be `…-at-q0-50dps.witness.json` for EVERY q, so whatever q
    # was evaluated last owned a file whose name says q₀. The "q0 CHANGED"
    # branch below discards and recomputes — correct for the returned value —
    # and then writes the new q's χ into the q₀-named file.
    #
    # That was survivable while the only two reachable q were the muon and
    # proton pins, both arguably "q₀". It stopped being survivable the moment
    # the BAR IMAGE became reachable: `tr_m_wenzl_bridge_mpfr` used to raise on
    # 1/q₀, and now computes it, so an ordinary probe evaluating at 1/q₀
    # rewrote `chi-deuteron-h6-at-q0-50dps.witness.json` to hold
    # q_0_50dps = 0.90091828… — observed, on eight caches at once, in the run
    # that prompted this. A later consumer reading a file named `at-q0` would
    # have got bar-image χ with nothing in the filename to say so.
    #
    # An unblock that converts a loud crash into silent cache poisoning is a
    # net loss, so the path now carries the q whenever it is off-anchor. The
    # two anchors keep their existing filenames untouched — no migration, no
    # change for any current consumer.
    #
    # WHY A HASH AND NOT THE EXISTING `-at-qinv-` NAME. The corpus already has
    # a bar-image convention, `chi-{atom}-h{n}-at-qinv-50dps.witness.json`,
    # written by `chi_at_q_inv_via_native_mpfr.py` with 8 tracked files and
    # several consumers. Reusing it here looked tidier and would have been the
    # same defect again: that producer's schema is NOT this one's — it keys the
    # modulus as `q_inv_50dps_str` and carries a full `_provenance` / `engine` /
    # `scriptHash` block, where this incremental cache writes `q_0_50dps`,
    # `partial` and `tr_M_at_q0`. Writing this shape into those filenames would
    # hand every `at-qinv` consumer a file missing the field it reads. Checked
    # before choosing, not after.
    _anchor = anchor_of_q0(q_str)
    if _anchor is None:
        _tag = hashlib.sha256(str(q_str).strip().encode()).hexdigest()[:8]
        out_path = HERE / f"chi-{atom_name}-h{n}-at-q{_tag}-50dps.witness.json"
    else:
        out_path = HERE / f"chi-{atom_name}-h{n}-at-q0-50dps.witness.json"
    already: dict[tuple, dict] = {}
    if out_path.exists():
        existing = json.loads(out_path.read_text())
        # Resume ONLY from a cache computed at this same q₀.
        #
        # This used to resume unconditionally, so re-running at a different
        # anchor kept the PREVIOUS anchor's χ values and stamped the new q₀
        # over them — a witness whose label and contents disagree, which is
        # the defect the whole `q0Anchor` apparatus exists to prevent.
        #
        # Measured: migrating tritium / helium-3 / neutron to proton
        # "completed" in 0.25s, 0.12s and 0.00s, and the dual-path audit then
        # read 2.14e-07 / 2.83e-07 / 8.15e-08 against a proton peel — versus
        # 1e-16 for the two atoms genuinely recomputed. A stale cache wearing
        # a fresh label is indistinguishable by inspection; only the
        # cross-check caught it.
        prev_q = str(existing.get("q_0_50dps", "")).strip()
        # `--fresh` is the repair path for a cache ALREADY relabelled. The q0
        # check above compares against the stored q0, so a witness that was
        # wrongly stamped with the new anchor looks consistent and resumes
        # its stale values forever. Nothing in the file can reveal that; only
        # recomputation can.
        if fresh:
            print(f"    --fresh: discarding "
                  f"{len(existing.get('by_partition', []))} cached "
                  f"partition(s) and recomputing from scratch")
        elif prev_q and prev_q != str(q_str).strip():
            print(f"    q0 CHANGED ({prev_q[:22]}… -> {str(q_str)[:22]}…): "
                  f"discarding {len(existing.get('by_partition', []))} cached "
                  f"partition(s) and recomputing")
        else:
            for entry in existing.get("by_partition", []):
                already[tuple(entry["partition"])] = entry
            if already:
                print(f"    resume: {len(already)} partition(s) already cached")

    with mp.workdps(dps):
        q = mp.mpf(q_str)
        # y_λ at the SAME layer as q₀. `_load_y_lambda(n, None)` reads the
        # default cache, which is the ideal (muon) one — pairing it with a
        # proton q₀ is the straddle AGENTS.md forbids, built into the producer.
        y_table = load_y_lambda_for_q0(n, q_str)
        shapes = list(parts_of(n))
        per_partition: list[dict] = []
        running_total = mp.mpf(0)

        # FAST PATH (gap-1 fix, PR-wire-native-chi-incremental):
        # before grinding O(d³) per-partition mpmath matmuls, ask Rust
        # for χ_λ over ALL uncached partitions in one batch call.
        # Falls through to the legacy per-partition loop below if the
        # native path is unavailable or rejects the word.  Pre-FFI
        # validation (gap-3) keeps a panic from aborting the process;
        # a warning on fallback (gap-2) surfaces the bypass instead of
        # silently grinding the slow path.
        rust_chi: dict[tuple, mp.mpf] = {}
        _part_dim = None  # pre-imported partition_dimension when fast path fires
        # Precompute shape tuples once (avoid building tuple(s) twice per shape).
        shape_tuples = [tuple(s) for s in shapes]
        uncached_shapes = [s for s in shape_tuples if s not in already]
        if uncached_shapes:
            try:
                from pyhecke_native import (
                    chi_lambda_all_partitions_mpfr as _rust_chi_all,
                )
                # Translate Python `(c, d, g0)` Hecke-factor word to
                # Rust's `(sign, g1)` enum, matching tr_m_wenzl_bridge.
                # `d_` and h are float64; the three expected values
                # 0, -h ≈ -0.20, -h/2 ≈ -0.10 are gap-separated by
                # ~0.1 at substrate q_0, so a 1e-12 tolerance is
                # comfortably above float64 ulp noise (~1e-15) and
                # well below the inter-class gap.  Replaces the prior
                # `round(_, 9)`-as-dict-key pattern, which would have
                # collided in the q → 1 limit where h → 0.
                h_f64 = float(q - mp.mpf(1) / q)
                tol = 1e-12
                word_signed: list[tuple[int, int]] = []
                # `sign == 0` carries a SHIFT, not just a class: a crossing
                # is σ_g + d·I and the native path applies σ_g − shift·I. The
                # symmetric average is shift = h/2, but this pipeline also
                # emits the colour-weighted p–n crossing d = −h·(1/2 − δ/4)
                # (installed above from `_avg_color_delta`), and an atomic
                # braid contains BOTH — p–p and n–n crossings are
                # colour-symmetric, p–n ones are not. ⁴He at H_12 carries the
                # two together, which is why a single word-level shift was not
                # enough and the first attempt still fell back. So the shift is
                # per crossing: `avg_shifts[i]` for word position i, empty
                # string meaning "h/2 here".
                avg_shifts: list[str] = []
                for c_, d_, g_ in word:
                    if abs(float(c_) - 1.0) > tol:
                        raise ValueError(
                            f"native chi path requires c==1.0, got c={c_}")
                    d_val = float(d_)
                    if abs(d_val) < tol:
                        sgn = 1
                        avg_shifts.append("")
                    elif abs(d_val + h_f64) < tol:
                        sgn = -1
                        avg_shifts.append("")
                    else:
                        sgn = 0
                        # Serialise from the mpf, never the f64: the shift
                        # carries δ and must reach Rust at working precision,
                        # or χ is capped near 1e-16 however high `dps` is set.
                        avg_shifts.append(
                            mp.nstr(-mp.mpf(d_), dps + 10, strip_zeros=False))
                    g1 = int(g_) + 1
                    # Pre-FFI validation — Rust panics on out-of-range gen,
                    # and pyo3 PanicException is BaseException (not catchable
                    # by `except Exception`).  Reject in Python first.
                    if not (1 <= g1 <= n - 1):
                        raise ValueError(
                            f"gen σ_{g1} out of range 1..{n-1} for H_{n}")
                    word_signed.append((sgn, g1))
                _t0 = time.time()
                # None => the native default h/2, bit-identical to the
                # previous four-argument call.
                # All-empty => the native default h/2 everywhere, which is
                # bit-identical to the previous four-argument call.
                rust_out = _rust_chi_all(
                    n, word_signed, q_str, dps,
                    None if not any(avg_shifts) else avg_shifts,
                )
                rust_chi = {tuple(lam): mp.mpf(chi_s)
                            for lam, chi_s in rust_out}
                # Pre-import partition_dimension once for the per-partition
                # loop below — avoids the hot-path re-import overhead.
                try:
                    from pyhecke.wedderburn import partition_dimension as _pd
                    _part_dim = _pd
                except ImportError:
                    _part_dim = None
                print(f"    native batch: {len(rust_chi)} χ_λ via "
                      f"chi_lambda_all_partitions_mpfr in "
                      f"{time.time() - _t0:.1f}s")
            except BaseException as e:
                # Catch BaseException so pyo3's PanicException (subclass of
                # BaseException, not Exception) falls through to the
                # warning + slow-path fallback instead of aborting the
                # process.  KeyboardInterrupt / SystemExit must still
                # propagate (otherwise Ctrl-C and `sys.exit()` would be
                # silently absorbed).
                if isinstance(e, (KeyboardInterrupt, SystemExit)):
                    raise
                import warnings
                warnings.warn(
                    f"native chi path bypassed "
                    f"({type(e).__name__}: {e}); falling back to O(d^3) "
                    f"pure-mpmath per-partition loop — n={n} will be "
                    f"SLOW.  Build the pyhecke-native wheel or check "
                    f"the word encoding.",
                    RuntimeWarning,
                    stacklevel=2,
                )
                rust_chi = {}

        for shape_t in shape_tuples:
            if shape_t in already:
                per_partition.append(already[shape_t])
                running_total += mp.mpf(already[shape_t]["contribution"])
                continue
            t_part = time.time()
            chi: mp.mpf | None = rust_chi.get(shape_t)
            if chi is None:
                sigmas, dim_built = _build_seminormal_matrices_mpf(shape_t, q)
                if dim_built == 0:
                    continue
                chi = _chi_lambda_of_word_mpf(sigmas, dim_built, word, q=q)
                dim = dim_built
            else:
                # Need dim_λ for the entry payload; use pre-imported
                # partition_dimension (hook-length formula) when the fast
                # path was active.  Falls through to Hoefsmit build only
                # if the import was unavailable.
                if _part_dim is not None:
                    dim = int(_part_dim(shape_t))
                else:
                    sigmas, dim = _build_seminormal_matrices_mpf(shape_t, q)
                    if dim == 0:
                        continue
            y_lam = y_table.get(shape_t)
            if y_lam is None:
                continue
            contrib = y_lam * chi
            running_total += contrib
            entry = {
                "partition": list(shape_t),
                "dim": dim,
                "y_lambda": str(y_lam),
                "chi_lambda": str(chi),
                "contribution": str(contrib),
                "compute_time_sec": f"{time.time() - t_part:.2f}",
            }
            per_partition.append(entry)
            # Incremental save (atomic rename — interrupt-safe).
            payload = {
                "computation": f"chi-{atom_name}-h{n}-at-q0-50dps",
                "description": (
                    f"Numerical χ^λ_q(β_atomic({Z}, {N})) = {atom_name} per "
                    f"partition λ ⊢ {n}, evaluated at q = q_0 at {dps} dps via "
                    f"the Hoefsmit seminormal basis. Built incrementally — "
                    f"each completed partition is persisted immediately, so "
                    f"a SIGTERM/timeout mid-loop preserves work done so far. "
                    f"Re-running picks up cached partitions and computes the "
                    f"remaining ones."
                ),
                "convention": convention,
                "q_0_50dps": str(q),
                "dps": dps,
                "n_strands": n,
                "atom": atom_name,
                "Z": Z, "N": N,
                "n_partitions": len(per_partition),
                "n_partitions_total": len(shapes),
                "partial": len(per_partition) < len(shapes),
                "compute_time_sec_so_far": f"{time.time() - t0:.2f}",
                "tr_M_at_q0": str(running_total),
                "by_partition": per_partition,
            }
            _save_partial(out_path, payload)
            print(f"    λ={shape_t!s:20} dim={dim:>3}  "
                  f"+{float(entry['compute_time_sec']):>5.1f}s  "
                  f"({len(per_partition)}/{len(shapes)})")

    elapsed = time.time() - t0
    return {
        "atom": atom_name,
        "Z": Z, "N": N,
        "n_strands": n,
        "n_partitions": len(per_partition),
        "n_partitions_total": len(shapes),
        "partial": len(per_partition) < len(shapes),
        "convention": convention,
        "compute_time_sec": f"{elapsed:.2f}",
        "tr_M_at_q0": str(running_total),
        "by_partition": per_partition,
    }


def save_witness(record: dict) -> Path:
    """Persist the per-atom numerical cache as
    `chi-{atom}-h{n}-at-q0-50dps.witness.json`."""
    atom_name = record["atom"]
    n = record["n_strands"]
    out = HERE / f"chi-{atom_name}-h{n}-at-q0-50dps.witness.json"
    payload = {
        "computation": f"chi-{atom_name}-h{n}-at-q0-50dps",
        "description": (
            f"Numerical χ^λ_q(β_atomic({record['Z']}, {record['N']})) "
            f"= {atom_name} per partition λ ⊢ {n}, evaluated at q = q_0 "
            f"at 50 decimal places via the Hoefsmit seminormal basis. "
            f"Companion to the symbolic chi-{atom_name}-h{n}.witness.json "
            f"emitted by per_irrep_pole_atom.py; this numerical cache is "
            f"used by canonical_tr_m_via_chi_cache.py and the 3-way "
            f"1ppb cross-check (cross_check_trM_1ppb.py) when full "
            f"symbolic data is not yet available. ~100× faster to build "
            f"than the symbolic counterpart (no sympy poly arithmetic)."
        ),
        # From the record, not recomputed: `save_witness` is a different
        # scope and must not re-derive a label the build already established.
        "convention": record["convention"],
        # Restored. A rebuild used to DROP these, so regenerating a witness
        # silently shrank it — `n_partitions_total` and `partial` are how a
        # consumer tells a complete cache from a resumed one, and `producer`
        # is what `chi_convention_audit._producer_field` reads first. The
        # classifier surfaced it as `field removed at n_partitions_total`
        # rather than as churn, which is the whole reason a removal is a
        # rejection and an addition is not.
        "producer": Path(__file__).name,
        "n_partitions_total": record["n_partitions_total"],
        "partial": record["partial"],
        "q_0_50dps": Q_50_DIGIT_STR,
        "dps": 50,
        "n_strands": n,
        "atom": atom_name,
        "Z": record["Z"], "N": record["N"],
        "n_partitions": record["n_partitions"],
        "compute_time_sec": record["compute_time_sec"],
        "tr_M_at_q0": record["tr_M_at_q0"],
        "by_partition": record["by_partition"],
    }
    # Stamp provenance rather than hand-rolling it. `WitnessBuilder` was
    # already imported here and never used, so a rebuild wrote no `scriptHash`
    # and no `q0Anchor` at all — the committed file carried
    # `q0Anchor: "ambiguous"` from a one-off audit fix, and regenerating
    # silently DROPPED it. Losing the anchor label is worse than the stale one
    # it replaced, and it is precisely what `witness_regen_classify` refused
    # the rebuild for. `resolve_q0_anchor` reports "proton" for this script,
    # which is both correct and an improvement on "ambiguous".
    WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine="python+mpmath")
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "atoms", nargs="*",
        help="Atoms to build (default: tritium, helium-3 — the ones with "
             "partial symbolic caches). One of: " + ", ".join(ATOMS),
    )
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument(
        "--fresh", action="store_true",
        help="Ignore any cached partitions and recompute from scratch. Use "
             "when a cache may already have been stamped with the CURRENT q0 "
             "while holding values computed at a different one — the resume "
             "check compares stored-vs-current q0, so it cannot see that.")
    args = parser.parse_args()

    if not args.atoms:
        atoms = ["tritium", "helium-3"]
    else:
        atoms = [ATOM_ALIASES.get(a, a) for a in args.atoms]

    mp.mp.dps = args.dps
    # Per Q6 audit: use the canonical 50-dps decimal string, not the
    # f64-quantised `repr(Q_FLOAT)` (which truncates to ~16 digits).
    q_str = Q_50_DIGIT_STR
    print("=" * 80)
    print(f" Building numerical χ^λ caches at q_0 (50 dps)")
    print(f" q_0 = {Q_50_DIGIT_STR}")
    print("=" * 80)
    print(f"  {'atom':>9}  {'n':>3}  {'n_partitions':>14}  {'tr_M(q_0)':>22}  {'time':>10}")
    print("  " + "-" * 70)

    for atom_name in atoms:
        if atom_name not in ATOMS:
            print(f"  {atom_name}: not in ATOMS, skip")
            continue
        Z, N = ATOMS[atom_name]
        try:
            record = build_chi_cache_at_q0(atom_name, Z, N, q_str,
                                           dps=args.dps, fresh=args.fresh)
        except Exception as exc:  # noqa: BLE001
            print(f"  {atom_name:>9}  ERROR  {type(exc).__name__}: {exc}")
            continue
        out_path = save_witness(record)
        n_parts = record["n_partitions"]
        tr_m_short = record["tr_M_at_q0"][:22]
        print(f"  {atom_name:>9}  {record['n_strands']:>3}  "
              f"{n_parts:>14}  {tr_m_short:>22}  "
              f"{float(record['compute_time_sec']):>9.2f}s")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
