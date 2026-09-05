#!/usr/bin/env python3
"""
Hadron-level knot table: NF decomposition in the H₃(q) basis.

Instead of expanding every braid word into individual generators
(which produces 14,067 entries for tritium alone), this computes
the same physics using the 6-element NF basis {γ, σ₀, σ₁, L₊, L₋, e⁻}.

Each atom is 6 coefficients. Total: 84 entries for 14 atoms
(vs 21,694 quark-level entries for 6 atoms).

The Markov trace, net, and Frobenius stability are identical to
the quark-level computation — the H₃(q) NF captures all the
information needed for mass formulas and Q-value predictions.

Usage:
    python3 hadron_knot_table.py

Output:
    hadron-knot-table.witness.json

Content block: rem:hadron-level-knot-table
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path
from mpmath import mp  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))

from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_core import (
    build_nucleon_nf,
    check_frobenius,
)
from hecke_core_legacy import (
    binding_energy,
    classify_nuclear_knot,
)
from pyhecke.gram import (
    build_atom_nf,
    nf_tr,
    nf_net,
    NF_NAMES,
    tr_m_mp,
    gram_matrix_mp,
)
from pyhecke.atom import build_nucleon_nf_mp
from compound_shift_nf import build_atom_nf_mp
from hecke_engine import HeckeEngine, HeckeRational
from witness_base import WitnessBuilder
from _precision import set_compute_dps, fmt  # noqa: E402

# ── q0 canonical per-generator volumes (mpmath, true substrate) ──────────
# Use the TRUE substrate q0, not the legacy 111/100 (~2e-4 off). The
# exact-Fraction HeckeEngine cannot run at q0 (q0^k denominators 10^7k blow
# up the Fractions; the table never terminates), so this mpmath port mirrors
# HeckeRational.V_full at q0 — verified vs the rational engine to ~2e-4 (the
# genuine q-gap). _HE is retained ONLY for the q-independent ground-state
# ordering. See docs/audits/2026-06-16-gram-q-approximation-audit.md.
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
_Q0 = mp.mpf(Q_50_DIGIT_STR)
_QI0 = 1 / _Q0
_HA0 = _Q0 - _QI0
# Markov parameter under convention D: z = q³/(q²+1).
#
# NO FLOAT64 EVER (owner directive). This was computed twice: once here in mpf
# as `_z_q0`, which nothing used, and once ~15 lines above as
# `_z = Q**3 / (Q**2 + 1)` over the FLOAT `Q` — and it was the float one that
# fed `delta_xchan = _Z2 * cross_sum * M_E_MEV` and the witness. An exact value
# sat unread next to the approximate one that did the work.
#
# (The comment on the deleted line described z as `1/(q^{1/2} + q^{-1/2})`,
# which is convention C — excised by owner ruling — while the code was already
# convention D. Both are fixed here.)
_z_q0 = _Q0**3 / (_Q0**2 + 1)
_z = _z_q0
_Z2 = _z * _z
_HE = HeckeEngine(111, 100)  # ground-state ordering only (q-independent)


def _crossing_q0(ti, tj):
    if ti == 1 and tj == 1:
        return mp.mpf(1), mp.mpf(0)
    if ti == 0 and tj == 0:
        return mp.mpf(1), -_HA0
    return mp.mpf(1), -_HA0 / 2


def _traced_volume_q0(gi, ordering):
    M00, M01, M10, M11 = mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(1)
    for j in range(gi + 1, len(ordering)):
        c, d = _crossing_q0(ordering[gi], ordering[j])
        t00 = c * _HA0 + d
        M00, M01, M10, M11 = (M00 * t00 + M01 * c, M00 * c + M01 * d,
                              M10 * t00 + M11 * c, M10 * c + M11 * d)
    return _z_q0 * M10 + M11


def _v_full_all_q0(ordering):
    """Per-generator Wedderburn-weighted V̂_i^full at the true q0 (mpmath)."""
    n2 = _Q0 ** 2 + 2 + _QI0 ** 2
    den = n2 + 2
    w_sym, w_std, w_alt = mp.mpf(1) / den, n2 / den, mp.mpf(1) / den
    out = []
    for i in range(len(ordering) - 1):
        lam_sym = mp.mpf(1)
        lam_alt = mp.mpf(1)
        for j in range(i + 1, len(ordering)):
            c, d = _crossing_q0(ordering[i], ordering[j])
            lam_sym *= c * _Q0 + d
            lam_alt *= -c * _QI0 + d
        out.append(w_sym * lam_sym + w_std * _traced_volume_q0(i, ordering)
                   + w_alt * lam_alt)
    return out


# ── Atoms to compute ─────────────────────────────────────────────

ATOMS = [
    # Nucleons
    ("proton",    1, 0, "uud"),
    ("neutron",   0, 1, "udd"),
    # Light atoms (Z ≤ 8)
    ("protium",   1, 0, None),
    ("deuterium", 1, 1, None),
    ("tritium",   1, 2, None),
    ("he3",       2, 1, None),
    ("he4",       2, 2, None),
    ("li6",       3, 3, None),
    ("li7",       3, 4, None),
    ("be9",       4, 5, None),
    ("b11",       5, 6, None),
    ("c12",       6, 6, None),
    ("c14",       6, 8, None),
    ("n14",       7, 7, None),
    ("o16",       8, 8, None),
    # Medium atoms
    ("ne20",     10, 10, None),
    ("si28",     14, 14, None),
    ("ca40",     20, 20, None),
    ("fe56",     26, 30, None),
]


def compute_per_generator_volumes(Z, N):
    """Per-generator full traced volumes V̂_i^full and cross-channel.

    Uses the CANONICAL paper formula (wedderburn-mass-formula.md):
        V̂_i^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt
    via HeckeRational.V_full (central utility).

    Cross-channel (mass-endomorphism-tower formula sum 3):
        δ_xchan = z² × Σ_{|i-j|=1} ln|V̂_i^full · V̂_j^full| × m_e

    Returns:
        ordering, V_full_list, cross_sum, delta_xchan_MeV
    """
    A = Z + N
    if A < 2:
        return [], [], 0.0, 0.0

    ordering, method = _HE.ground_state_ordering(Z, N)
    # V_full at the true substrate q0 (mpmath), not the legacy 111/100.
    V_list = _v_full_all_q0(ordering)

    cross_sum = 0.0
    for i in range(len(V_list) - 1):
        prod = abs(V_list[i] * V_list[i + 1])
        if prod > 1e-300:
            cross_sum += mp.log(prod)

    delta_xchan = _Z2 * cross_sum * M_E_MEV
    return ordering, V_list, cross_sum, delta_xchan


_MP_DPS = 50

#: Relative Frobenius tolerance (beans `qou-3uvs`, `qou-ejuy`).
#:
#: The f64 `check_frobenius` in `pyhecke.atom` tests `Gx[i] < -1e-10`, a FIXED
#: ABSOLUTE tolerance, against values whose magnitude runs from 1e1 at o16 to
#: 1e31 at fe56. One float64 ulp at fe56's scale is ~2.5e+15 — twenty-five
#: orders ABOVE that threshold — so a `Gx` entry whose true value is 0 could
#: land at -1e+15 from cancellation alone and register as a violation. The
#: verdict was below its own noise floor for ca40 and fe56.
#:
#: 1e-10 RELATIVE reproduces the old test exactly wherever ‖Gx‖∞ ≤ 1, which is
#: the regime where the absolute form was meaningful, and scales with the
#: quantity everywhere it was not. Deliberately NOT tightened to something like
#: 1e-30 just because mpf could carry it: that would be a new scientific
#: threshold smuggled in under a precision change.
_FROB_REL_TOL = mp.mpf("1e-10")

_TR_M_MP = None
_G_MP = None


def _mp_tables():
    """`(tr_m_mp, gram_matrix_mp)` at `_MP_DPS`, built once."""
    global _TR_M_MP, _G_MP
    if _TR_M_MP is None:
        _TR_M_MP = tr_m_mp(_MP_DPS)
        _G_MP = gram_matrix_mp(_MP_DPS)
    return _TR_M_MP, _G_MP


def check_frobenius_mp(nf, G_mp):
    """Frobenius positivity G·x >= 0 in mpf, with a SCALE-AWARE tolerance.

    The mp counterpart of `pyhecke.atom.check_frobenius`, kept HERE rather
    than in the library: that function is on the deliberately bit-stable f64
    path (`gram.py`, bean `qou-jtbo`) and other callers depend on it being
    exactly what it is.
    """
    Gx = [sum(G_mp[i][j] * nf[j] for j in range(6)) for i in range(6)]
    scale = max((abs(v) for v in Gx), default=mp.mpf(0))
    if scale < 1:
        scale = mp.mpf(1)          # never LOOSER than the original absolute test
    tol = -(_FROB_REL_TOL * scale)
    violations = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < tol]
    return len(violations) == 0, Gx, violations


def compute_atom(name, Z, N, quarks=None):
    """Compute hadron-level NF for one atom."""
    # mp path throughout (beans `qou-ejuy`, `qou-3uvs`). This read
    # `build_atom_nf` / `nf_tr` / `nf_net` / `check_frobenius`, all of which
    # are on `pyhecke.gram`'s deliberately bit-stable FLOAT64 path — so the
    # row mixed two precisions, publishing a float64 `tr_M` beside a `B_MeV`
    # that came through the MPFR kernel. The mpf counterparts already existed
    # and the module says to use them.
    #
    # `build_atom_nf_mp` was NOT a drop-in until this session: it used `-h/2`
    # for the inter-nucleon p-n crossing where the canonical builder uses the
    # colour-weighted `D_PN`, a 6.88e-4 difference in convention rather than
    # precision. Fixed under `qou-ejuy`, and the two now agree to 1e-16..1e-15
    # over deuterium..c12 — verified BEFORE this switch, because a silent 7e-4
    # shift would have looked exactly like a clean precision upgrade.
    TRmp, G_mp = _mp_tables()
    if quarks:
        quark_list = list(quarks.replace("u", "u").replace("d", "d"))
        nf = build_nucleon_nf_mp(quark_list, _MP_DPS)
    else:
        nf = build_atom_nf_mp(Z, N, _MP_DPS)

    tr = sum(nf[i] * TRmp[i] for i in range(6))
    net = sum(nf)
    stable, Gx, violations = check_frobenius_mp(nf, G_mp)
    alpha_knot, knot_name, is_hyp = classify_nuclear_knot(Z, N)
    B = binding_energy(Z, N)

    # Compact NF: only non-zero coefficients with basis names
    # `fmt`, not `round(val, 12)` (bean `qou-uiut`, NO-FLOAT64). `round()` on
    # an mpf returns a Python float, so every NF coefficient reached the
    # witness as float64 — 12 decimals of a value the pipeline carried at 50
    # dps. The threshold stays a magnitude test on the mpf; only the
    # SERIALIZATION changes.
    nf_compact = {}
    for i, (bname, val) in enumerate(zip(NF_NAMES, nf)):
        if abs(val) > mp.mpf("1e-15"):
            nf_compact[bname] = fmt(val)

    # Per-generator traced volumes + cross-channel (mass-tower sum 3)
    ordering, V_list, cross_sum, delta_xchan = compute_per_generator_volumes(Z, N)
    # The comment here used to read "compute mpf@q0; serialize float", which
    # is an accurate description of the defect (bean `qou-uiut`): the volumes
    # are computed as mpf at q0 and were then narrowed to float64 on the way
    # out. Serialized at output precision now.
    V_rounded = [fmt(v) for v in V_list]

    return {
        "name": name,
        "Z": Z,
        "N": N,
        "A": Z + N,
        "nf": nf_compact,
        "n_terms": len(nf_compact),
        # `tr` and `net` come out of `pyhecke.gram.nf_tr` / `nf_net` as
        # FLOAT64, not mpf, and `fmt` renders a float via `str()` — so these
        # two carry ~17 significant digits and say so, rather than being padded
        # out to 60. The source of that is `pyhecke.gram`, whose `z`, `h` and
        # `TR_M` are Python floats / a float64 numpy array; excising it is a
        # library change with a wide blast radius and is tracked separately
        # (bean `qou-ejuy`). What changed here is only that the narrowing is no
        # longer done a SECOND time by `round(float(...), 12)` on the way out.
        "tr_M": fmt(tr),
        "net": fmt(net),
        # 17 dps DELIBERATELY, not the default 60 (bean `qou-uiut`). `mp.log`
        # promotes its float64 argument to mpf and will happily return 60 true
        # digits — but they are 60 digits of the logarithm of a value that only
        # HAS ~17, so digits 18-60 describe the binary64 rounding of `tr`, not
        # the physics. Publishing them would be manufactured precision of
        # exactly the kind the float64-padding ratchet exists to catch. When
        # `qou-ejuy` makes `tr` a real mpf, drop the override.
        # Full width again (bean `qou-uiut`): the `dps=17` cap was there
        # because `tr` was a float64 and `mp.log` would have manufactured 43
        # digits describing its binary64 rounding. `tr` is an mpf now, so the
        # digits are real.
        "ln_abs_tr": (fmt(mp.log(abs(tr)))
                      if abs(tr) > mp.mpf("1e-300") else None),
        "frobenius_stable": stable,
        # Record the EVIDENCE, not just the verdict (bean `qou-3uvs`).
        # `check_frobenius` returns `(stable, Gx, violations)` and this
        # function already unpacked all three, then published only the
        # boolean — so a False verdict could not be audited without re-running
        # a 4.6-hour table.
        #
        # It needs auditing here specifically. The test is `Gx[i] < -1e-10`, a
        # FIXED absolute tolerance, on a float64 product whose magnitude runs
        # from 1e1 (o16) to 1e31 (fe56). At fe56's scale one float64 ulp is
        # ~2.5e+15, twenty-five orders ABOVE the threshold, so a `Gx` entry
        # whose true value is 0 can land at -1e+15 from cancellation alone and
        # register as a violation. With these recorded, a reader can see
        # whether a violation is genuinely large or sits in the noise.
        # No `float()` (beans `qou-ejuy`, `qou-uiut`): `Gx` comes from
        # `check_frobenius_mp` as mpf now, and re-narrowing it here would
        # discard the precision the migration exists to gain — and with it the
        # ability to see whether a violation is real or noise, which is the
        # whole reason these are recorded.
        "Gx": [fmt(v) for v in Gx],
        "frobenius_violations": [[nm, fmt(val)] for nm, val in violations],
        "knot_type": knot_name,
        "B_MeV": fmt(B),
        # Per-generator traced volumes (mass-tower formula, sum 1 + 3)
        "ordering": ordering,
        "V_per_gen": V_rounded,
        "cross_channel_sum": fmt(cross_sum),
        "delta_xchan_MeV": fmt(delta_xchan),
    }


# ── Main ─────────────────────────────────────────────────────────

# Per-atom timing + a real start_time (bean qou-c7g8).
#
# Two separate defects, both of which made this producer impossible to reason
# about from its own output:
#
#  (a) `durationMs` was MEANINGLESS. `WitnessBuilder` is constructed below,
#      AFTER this loop, and was passed no `start_time` -- so it reported the
#      time to SERIALISE the witness, not to compute it. The committed witness
#      says `durationMs: 53`, which was read (by me) as "19 atoms in 53 ms" and
#      used to claim a six-orders-of-magnitude regression. It measured neither.
#      `_T0` below is captured before any work and handed to WitnessBuilder.
#
#  (b) NO PROGRESS SIGNAL. stdout here is block-buffered when redirected, while
#      warnings go to stderr unbuffered, so a redirected run shows a few atoms
#      and then nothing -- which reads as "stalled at atom N" whether or not it
#      stalled. Every atom line now carries its own elapsed time and flushes.
import time as _time
_T0 = _time.monotonic()
_atom_secs = {}

# ── Resume across restarts (beans `qou-uiut` / `qou-sv7h`) ────────
#
# This table runs 19 atoms up to fe56 (A = 56) and writes its witness only at
# the very end, so an interrupted run loses everything. That was academic while
# the producer could not finish a single A=2 atom; now that it can (deuterium:
# ~40 days estimated -> 31 s, via the Rust MPFR character kernel) the full
# table is a multi-hour run, and multi-hour runs in an ephemeral container get
# reclaimed part-way.
#
# OFF by default: without `QOU_HKT_CHECKPOINT` this file behaves exactly as
# before. The checkpoint is a CACHE, never an input to the corpus — it is
# written outside the repo and must not be committed.
#
# The cache is keyed on a hash of the sources that determine the numbers plus
# q itself. Any edit to those files discards it. That is deliberately
# conservative — it will throw away a long run for a comment change — because
# the alternative failure is resurrecting stale numbers into a witness, and
# this table has already carried wrong numbers once (the YSN matrices were not
# a representation of H_n(q) until bean `qou-uiut`).
#
# mpf values are stored as their exact `_mpf_` limbs, not as decimal strings.
# A decimal round-trip would quietly reduce their precision on resume, and the
# checkpoint holds INTERMEDIATE values, not just the serialized row. Verified
# exact round-trip for 1/7, -1e-300, 0, log(3)/9 and a rounded mpf.
#
# The example this used to cite -- `round(mp.log(abs(tr)), 12)` in
# `compute_atom` -- is gone: those sites now serialize with `fmt` at output
# precision instead of rounding (bean `qou-uiut`), so the row itself carries
# decimal STRINGS. That does not change the rule for this encoder, which still
# sees mpf anywhere a checkpointed value is an intermediate.
import hashlib as _hashlib
import json as _json
import os as _os

_CKPT_PATH = _os.environ.get("QOU_HKT_CHECKPOINT", "").strip()


def _ckpt_key():
    """Hash of everything that determines the numbers."""
    h = _hashlib.sha256()
    h.update(mp.nstr(_Q0, 50, strip_zeros=False).encode())
    import hecke_core as _hc
    import hecke_core_legacy as _hcl
    for mod in (__file__, _hcl.__file__, _hc.__file__):
        with open(mod, "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()


def _ckpt_enc(o):
    if isinstance(o, mp.mpf):
        return {"__mpf__": [int(t) for t in o._mpf_]}
    if isinstance(o, dict):
        return {k: _ckpt_enc(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_ckpt_enc(v) for v in o]
    return o


def _ckpt_dec(o):
    if isinstance(o, dict):
        if "__mpf__" in o and len(o) == 1:
            return mp.make_mpf(tuple(o["__mpf__"]))
        return {k: _ckpt_dec(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_ckpt_dec(v) for v in o]
    return o


def _ckpt_load():
    if not _CKPT_PATH or not _os.path.exists(_CKPT_PATH):
        return {}
    try:
        # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
        # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
        # dump runs, so any exception in between leaves the committed witness
        # empty or partial -- the shape that emptied 22 witnesses to zero bytes
        # in one `producer_importability_audit` run. `os.replace` is atomic on
        # POSIX within a filesystem, hence a SIBLING temp file.
        _wpath_sidu = _CKPT_PATH
        _wtmp_sidu = str(_wpath_sidu) + ".tmp"
        with open(_wtmp_sidu, encoding="utf-8") as fh:
            blob = _json.load(fh)
        _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    except (OSError, ValueError) as exc:
        print(f"  [checkpoint] unreadable ({exc}); starting fresh", flush=True)
        return {}
    if blob.get("key") != _ckpt_key():
        print("  [checkpoint] KEY MISMATCH — the producer or its inputs "
              "changed since it was written. Discarding it rather than "
              "resuming onto stale numbers.", flush=True)
        return {}
    return {k: _ckpt_dec(v) for k, v in blob.get("atoms", {}).items()}


def _ckpt_save(cache):
    """Atomic write — a crash mid-save must not leave a truncated cache."""
    if not _CKPT_PATH:
        return
    tmp = _CKPT_PATH + ".tmp"
    _os.makedirs(_os.path.dirname(_os.path.abspath(_CKPT_PATH)), exist_ok=True)
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = tmp
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as fh:
        _json.dump({"key": _ckpt_key(),
                    "atoms": {k: _ckpt_enc(v) for k, v in cache.items()}}, fh)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    _os.replace(tmp, _CKPT_PATH)


_ckpt = _ckpt_load()
if _CKPT_PATH:
    print(f"  [checkpoint] {_CKPT_PATH} — {len(_ckpt)} atom(s) already done",
          flush=True)

# Optional chunking: compute only these atoms this pass (comma-separated
# names), resuming the rest from the checkpoint. Lets a table longer than one
# container lifetime be finished across several passes.
#
# The witness is written ONLY when every atom in ATOMS is present. A partial
# witness is the failure this producer already committed once — four rows of
# AssertionError text serialised as `allPassed: true` (bean `qou-qe81`) — so a
# short pass ends by naming what is still missing and writing nothing.
_ONLY = {x.strip() for x in _os.environ.get("QOU_HKT_COMPUTE_ONLY", "").split(",")
         if x.strip()}

results = []
print(f"Hadron-level knot table ({len(ATOMS)} atoms)")
print(f"q = {mp.nstr(_Q0, 12)}, basis = {{γ, σ₀, σ₁, L₊, L₋, e⁻}}")
print()
print(f"{'Atom':>12} {'A':>3} {'tr_M':>14} {'B(MeV)':>10} {'cross_sum':>11} {'δ_xchan':>10} {'Frob':>5} {'wall':>9}")
print("-" * 80)

for name, Z, N, quarks in ATOMS:
    _t_atom = _time.monotonic()
    if name in _ckpt:
        r = _ckpt[name]
        _atom_secs[name] = 0.0      # resumed, not recomputed
    elif _ONLY and name not in _ONLY:
        print(f"{name:>12} {Z + N:>3}   deferred (not in QOU_HKT_COMPUTE_ONLY)",
              flush=True)
        continue
    else:
        r = compute_atom(name, Z, N, quarks)
        _atom_secs[name] = _time.monotonic() - _t_atom
        _ckpt[name] = r
        _ckpt_save(_ckpt)           # after EVERY atom, not at the end
    results.append(r)
    # `float(...)` for the console only (bean `qou-uiut`). The row fields are
    # decimal STRINGS now — serialized at output precision rather than rounded
    # to float64 — and a str has no `:.6f`. Parsing back for a fixed-width
    # column is presentation, not a value: nothing here reaches the witness.
    print(
        f"{name:>12} {r['A']:>3} "
        f"{float(r['tr_M']):>14.6f} "
        f"{float(r['B_MeV']):>10.4f} "
        f"{float(r['cross_channel_sum']):>+11.6f} "
        f"{float(r['delta_xchan_MeV']):>+10.4f} "
        f"{'OK' if r['frobenius_stable'] else 'FAIL':>5}"
        f"{_atom_secs[name]:>9.2f}s",
        flush=True,
    )

_missing = [n for n, _z, _n, _q in ATOMS if n not in {r["name"] for r in results}]
if _missing:
    print(f"\n  {len(results)}/{len(ATOMS)} atoms computed. NOT writing a "
          f"witness — still missing: {', '.join(_missing)}")
    if _CKPT_PATH:
        print(f"  Re-run with QOU_HKT_CHECKPOINT={_CKPT_PATH} to continue.")
    else:
        print("  Set QOU_HKT_CHECKPOINT=<path> so a partial pass is not lost.")
    raise SystemExit(0)

total_terms = sum(r["n_terms"] for r in results)
print(f"\nTotal NF entries: {total_terms} (vs 21,694 quark-level)")

# ── Witness ──────────────────────────────────────────────────────

w = WitnessBuilder("hadron-knot-table", engine="python", start_time=_T0)
w.set_description(
    f"Hadron-level knot decomposition table for {len(ATOMS)} atoms in the "
    f"H₃(q) NF basis. Each atom is 6 coefficients (vs thousands at "
    f"quark level). Now also records per-generator traced volumes V_i "
    f"and cross-channel z²·Σ ln|V_iV_{{i+1}}| for the mass-endomorphism-tower "
    f"formula's third sum."
)
w.set_content_block("rem:hadron-level-knot-table")
w.add_parameter("q", _Q0)      # mpf, not the float64 Q (NO FLOAT64 EVER)
w.add_parameter("basis", NF_NAMES)
w.add_parameter("z_markov", _z)
w.add_parameter("z_squared", _Z2)
w.add_parameter("n_atoms", len(ATOMS))
# Per-atom wall time, as STRINGS (bean qou-c7g8). Strings, not floats, so this
# does not add raw float64 to the witness -- the NO-FLOAT64 directive applies to
# diagnostics too. These exist because this producer's cost profile was pure
# speculation for as long as its only timing signal was a `durationMs` that
# measured witness serialisation.
w.add_parameter("per_atom_wall_seconds",
                {k: f"{v:.3f}" for k, v in _atom_secs.items()})
w.add_parameter("total_nf_entries", total_terms)

# Assertions: check key traces AND LP stability
for r in results:
    # The `tr_M(<atom>)` assertion that stood here read
    # `computed=r["tr_M"], expected=r["tr_M"]` under
    # `source="hecke_core.build_atom_nf -> nf_tr"` — it advertised a check
    # against a named producer while comparing the value to itself, so it
    # passed for any number the producer returned (bean `qou-26f2`).
    #
    # Removed rather than repaired, because there is nothing to repair it TO:
    # each `tr_M` has one derivation route, so no assertion over it can fail,
    # and `w.add_data("atoms", results)` below already records every one of
    # these values with full precision. The assertion was contributing a
    # guaranteed pass to `allPassed` and nothing else; deleting it loses no
    # information and removes a claim that was never made.
    #
    # The LP-stability assertion below is the model: `computed` is the measured
    # predicate and `expected=1` is fixed, so it can fail.
    # LP stability assertion: all atoms must be Frobenius-stable
    # (gluon-dressed nucleons satisfy Gx ≥ 0). Catches missing operators.
    if r["A"] >= 2:
        w.add_assertion(
            f"LP_stable({r['name']})",
            computed=1 if r["frobenius_stable"] else 0,
            expected=1,
            tolerance=0,
            unit="bool",
            source="hecke_core.check_frobenius (Gx ≥ 0)",
        )

w.add_data("atoms", results)
w.save()
