#!/usr/bin/env python3
"""
Plan F advance — extends the mpmath @ 50 dps tr_M evaluation from
proton (proton_mass_mpfr_50dps.py) to neutron, deuteron, and now
tritium / ³He (previously timed out) plus the symbolic comparison
test for ²H / ³H / ³He against published Jones polynomials.

For each atom 𝔥 ∈ {proton, neutron, deuteron, tritium, helium-3}:
  1. Build the 3A-strand Hecke factor word via atom_braid_word_3A
     (no GB-NF needed — Wenzl bridge consumes raw Hecke factors).
  2. Compute tr_M(W) via the Hoefsmit + Wenzl bridge:
        tr_M(W) = Σ_{λ ⊢ 3A} y_λ(q) · χ_λ(W)
     using y-lambda-mpfr-witness.json for y_λ and per-partition
     seminormal matrices in mpmath at 50 dps.
  3. (Optional, gated on `--symbolic`) Cross-check against the
     legacy sympy tr_M_element path for proton / neutron / deuteron
     where it terminates in reasonable time.
  4. Report Term-1 contribution m_e · ρ · |tr_M(q_0)| and the
     residual against B_AME for diagnostic.

For atoms in {²H, ³H, ³He} flagged `manual-historical-volume-match`
in joint-tower-sdp-rust.witness.json, also report whether the
numeric tr_M(q_0) matches the published Jones polynomial of the
historical knot up to writhe normalisation (q^k factor).

Output: `atomic-tr-m-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from mpmath import mp, mpf

from _precision import set_compute_dps, fmt
set_compute_dps()  # mp.mp.dps via QOU_COMPUTE_DPS (default 50)
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import atom_nf_symbolic_D as M
from mass_at_3A_proper import atom_braid_word_3A
from markov_trace_canonical import tr_M_element, Z_SYMB, H_SYMB
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr
from canonical_tr_m_via_rust import compute_tr_m as _canonical_rust_compute_tr_m
# Re-assert our working precision after the canonical_tr_m_via_rust
# import — historically that module set `mp.mp.dps = 30` at import
# time (since fixed, but this guard makes the script robust if the
# upstream regression returns).  Copilot PR #895 review.
set_compute_dps()

Q0 = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
OUT = HERE / "atomic-tr-m-mpfr-50dps.witness.json"

OUT_BY_ANCHOR = {
    "ideal": OUT,
    "proton": HERE / "atomic-tr-m-mpfr-50dps-proton.witness.json",
}


def q0_for(anchor: str) -> str:
    """50-dps q₀ for one layer. `ideal` from the q-pinning witness (the
    canonical muon source `q_parameter` itself reads), `proton` from
    `q_parameter.Q_50_DIGIT_STR`. No fallback between them.

    `--anchor proton` alone is NOT enough and this refuses rather than let it
    look like it worked. `q_parameter` resolves its pin at IMPORT time, from
    the running script's stem — and this script's stem is in
    `q0_anchor_manifest.json` `ideal_muon`, so `Q_50_DIGIT_STR` is bound to the
    MUON value here unless the environment overrides the manifest. argparse
    runs long after that import, so the flag cannot change it.

    Without this check the run "succeeds" and writes muon numbers into the
    proton-named witness — a mislabelled layer, which is worse than the
    straddle it was meant to fix, because the filename then lies about which
    pin the contents carry.
    """
    if anchor == "ideal":
        return json.load(open(Q0))["derived_50_digit"]["q"]
    if anchor != "proton":
        raise SystemExit(f"unknown anchor {anchor!r}: expected 'ideal' or 'proton'")
    from q_parameter import Q_50_DIGIT_STR
    q = str(Q_50_DIGIT_STR)
    if not q.startswith("1.10997858275"):
        raise SystemExit(
            "--anchor proton, but q_parameter resolved to the MUON pin "
            f"({q[:24]}…). This script's stem is in q0_anchor_manifest.json "
            "`ideal_muon`, and that binding happens at import, before "
            "argparse. Re-run as:\n"
            "    QOU_Q0_ANCHOR=proton python3 "
            "computations/atomic_tr_m_mpfr_50dps.py --anchor proton\n"
            "Refusing to write muon values into the proton-named witness.")
    return q

from codata_constants import M_E_MEV  # CODATA 2022 — centralised

# Published Jones polynomials (from Kawauchi tables / KnotInfo).
# Variable conventions: in our pipeline σ_i² = (q − q⁻¹)σ_i + 1, so
# J_K is the Markov-trace value for the trefoil-like normalization.
J_PUBLISHED = {
    # 6_2: from Kawauchi Theorem 2.2.4 / KnotInfo.
    "6_2": "q - 1 + 2/q - 2/q**2 + 2/q**3 - 2/q**4 + 1/q**5",
    # 8_11: KnotInfo / Murasugi (Knot Theory and its Applications).
    "8_11": "-q**6 + 2*q**5 - 4*q**4 + 5*q**3 - 5*q**2 + 5*q - 4 + 3/q - 1/q**2",
    # L_6a4 (Borromean): standard formula.
    "L_6a4": "q**3 - 3*q**2 + 6*q - 7 + 6/q - 3/q**2 + 1/q**3",
}

ATOMS = [
    ("proton",    1, 0, 1, "p (B_3 Borromean)",   None),
    ("neutron",   0, 1, 1, "n (B_3 Borromean)",   None),
    ("deuteron",  1, 1, 1, "²H (B_6 atom-3A)",    "6_2"),
    ("tritium",   1, 2, 1, "³H (B_9 atom-3A)",    None),
    ("helium-3",  2, 1, 1, "³He (B_9 atom-3A)",   None),
    # ⁴He intentionally OMITTED here.  Canonical |tr_M(⁴He)| at H_12
    # via the Wenzl bridge is intractable at 50 dps with current
    # Python mpmath: p(12)=77 partitions and the largest partition
    # (5,3,2,1,1) has dim 7700, requiring ~2×10¹³ mp.mpf ops per
    # partition × 47 crossings.  bu64reus1 (PR #564) hit the 30-min
    # timeout.  See atomic-tr-m-helium4.witness.json for the
    # disjoint-product placeholder (flagged DEPRECATED_DISJOINT) and
    # AUDIT-DEEP-2026-05.md §7 for the deferral rationale.  Tractable
    # canonical ⁴He requires either (a) Rust kernel with rayon
    # parallel partitions + block-sparse Hoefsmit MPFR, or (b) a
    # categorical reduction (e.g. via the Wenzl 1988 LR branching
    # decomposition in `hecke-branching-trace-decomposition.md`)
    # that avoids the full p(12)=77 sum.
]


def _bridge_tr_M(Z: int, N: int, q_str: str, dps: int = 50):
    """Compute tr_M(W_atom) via the Hoefsmit + Wenzl bridge.

    Builds the 3A-strand Hecke-factor word and evaluates Σ_λ y_λ · χ_λ
    at mpf precision.  Returns (tr_mpf, breakdown_dict, n_strands,
    word_length).
    """
    word = atom_braid_word_3A(Z, N)
    n_strands = 3 * (Z + N)
    t0 = time.time()
    tr = tr_M_via_wenzl_bridge_mpfr(
        word, n_strands, q_str, dps=dps, return_breakdown=False)
    dt = time.time() - t0
    return tr, n_strands, len(word), dt


def _rust_canonical_tr_M(Z: int, N: int, label: str):
    """Compute tr_M(W_canonical(Z, N)) via the Rust LR convention adapter
    + Phase-2 `canonical_tr_m_via_rust.compute_tr_m`.

    Cheat sheet §5 fix #3 (2026-05-22): wires the Rust binary
    `hecke-canonical-chi` (release build, f64 Hoefsmit seminormal
    with averaged-crossing expansion + per-partition mpmath
    combiner) into this consumer.  Expected speedup: ~500× at ⁴He
    (n=12), ~10⁶× at ¹⁰B vs the Python `tr_M_via_wenzl_bridge_mpfr`
    kernel.

    The Rust binary uses its own pinned q value (loaded by
    `canonical_tr_m_via_rust.compute_tr_m` from the same
    `q-pinning-50-digit.witness.json` source as this script — see
    that module for the q-pin chain), so the caller does NOT pass q.

    Returns `(tr_mpf_50dps, n_strands, n_crossings_canonical, dt)`:
        tr_mpf_50dps      — SIGNED Markov trace at 50 dps mpmath
                            (per Copilot review on PR #895: do not
                            collapse to abs; sign is algebraic).
        n_strands         — 3·(Z+N).
        n_crossings_canonical — canonical-word crossing count
                            (NOT the Hecke-factor word length used
                            by the Python bridge — call sites that
                            need the latter must still go through
                            `_bridge_tr_M`).
        dt                — wall-clock seconds.

    Returns `(None, None, None, dt)` if the Rust binary is unavailable
    (graceful fallback).
    """
    t0 = time.time()
    r = _canonical_rust_compute_tr_m(Z, N, label)
    dt = time.time() - t0
    if "tr_M_q0_unavail_reason" in r:
        return None, None, None, dt
    # Prefer the new 50-dps signed field (PR #895 review fix); fall
    # back to the 30-dps signed alias if older Rust output is in
    # play.  Never silently swap in `abs_*` — sign loss is a real
    # algebraic regression (Gemini PR #895 review).
    tr_str = r.get("tr_M_q0_mp50dps") or r.get("tr_M_q0_mp30dps")
    if tr_str is None:
        return None, None, None, dt
    return (mpf(tr_str),
            r.get("n_strands"),
            r.get("n_crossings"),
            dt)


def main(also_symbolic: bool = False, method: str = "canonical-rust",
         anchor: str = "ideal") -> int:
    # One witness per q0 LAYER, never one shared. This producer's stem is in
    # `q0_anchor_manifest.json` `ideal_muon`, so its q0 comes from the
    # q-pinning witness and `ideal` stays the default here — the 2026-08-07
    # "default to proton" directive governs NEW compute, and explicitly does
    # not redefine the ideal CAL-2 layer this producer belongs to.
    #
    # The proton counterpart exists because the experimental layer needs its
    # own bridge: `markov_peel_atomic_witness` is NOT in the manifest, so it
    # re-anchors to proton on its own, and then cross-checks itself against
    # THIS witness. With only the muon bridge available that comparison
    # straddles the layers, and its `abs_diff_vs_bridge` blew up to 6.73e-04.
    global OUT
    OUT = OUT_BY_ANCHOR[anchor]
    q_str = q0_for(anchor)
    q_0 = mpf(q_str)
    q_sym = sp.Symbol("q")  # match sympify default
    print(f"  q_0 (50 dps) = {q_str}")
    if method == "hoefsmit-python":
        print(f"  primary path: Hoefsmit+Wenzl bridge (mpf @ 50 dps)")
    elif method == "canonical-rust":
        print(f"  primary path: Rust hecke-canonical-chi "
              f"(cheat sheet §5 fix #3 wiring)")
    else:
        print(f"  primary path: Rust hecke-canonical-chi "
              f"WITH Python Hoefsmit+Wenzl cross-check at each atom")
    if also_symbolic:
        print(f"  symbolic cross-check: enabled (--symbolic) "
              f"— may be slow at A>=2")

    results = []
    for label, Z, N, rho, descr, historical_K in ATOMS:
        print(f"\n  === {label} (Z={Z}, N={N}, ρ={rho}) ===")

        # Primary path: kernel selector per `--method`.
        bridge_t_python = None
        bridge_t_rust = None
        rust_crosscheck = None
        n_crossings_canonical = None  # canonical-word crossing count
                                      # — distinct from Hecke-factor word length
        effective_method = method     # tracks fallback (PR #895 review)
        if method in ("canonical-rust", "rust-with-python-crosscheck"):
            tr_at_q0_mpf, n_strands_rust, n_crossings_rust, bridge_t_rust = (
                _rust_canonical_tr_M(Z, N, label)
            )
            if tr_at_q0_mpf is None:
                print(f"    [rust] hecke-canonical-chi unavailable; "
                      f"falling back to Hoefsmit+Wenzl bridge")
                effective_method = "hoefsmit-python-fallback"
                tr_at_q0_mpf, n_strands, word_len, bridge_t_python = \
                    _bridge_tr_M(Z, N, q_str, dps=50)
            else:
                n_strands = n_strands_rust
                # The Hecke-factor word length isn't known on the Rust
                # path (the Rust kernel marshalls a canonical-crossings
                # word, not the H_{3A} Hecke-factor word).  Compute it
                # separately so the witness can carry both consistently
                # (Copilot PR #895 review fix).
                word_len = len(atom_braid_word_3A(Z, N))
                n_crossings_canonical = n_crossings_rust
                print(f"    n_strands = {n_strands},  "
                      f"word_length_3A = {word_len},  "
                      f"n_crossings_canonical = {n_crossings_canonical}")
                print(f"    [rust]   tr_M(q_0) = {tr_at_q0_mpf}  "
                      f"({bridge_t_rust:.3f}s)")
                if method == "rust-with-python-crosscheck":
                    # Independent Hoefsmit+Wenzl bridge for cross-check.
                    # Sign-preserving (no `abs` collapse) per Gemini fix.
                    tr_python, _, _, bridge_t_python = _bridge_tr_M(
                        Z, N, q_str, dps=50)
                    delta = abs(tr_at_q0_mpf - tr_python)
                    rel = (delta / max(abs(tr_python), mpf("1e-30")))
                    agree_25 = bool(rel < mpf("1e-25"))
                    rust_crosscheck = {
                        "tr_M_python_50dps": fmt(tr_python),
                        "abs_delta": fmt(delta),
                        "rel_diff": fmt(rel),
                        "agree_at_25dps": agree_25,
                        # Wall-clock timings, not measurements. Written as
                        # fixed-precision STRINGS: it keeps raw float64 out of
                        # the witness, and it stops a timing jitter in the 16th
                        # digit from rewriting the file on every run.
                        "python_wall_sec": f"{bridge_t_python:.4f}",
                        "speedup_vs_python":
                            f"{bridge_t_python / bridge_t_rust:.1f}"
                            if bridge_t_rust > 0 else None,
                    }
                    print(f"    [crosscheck] python = {tr_python}  "
                          f"({bridge_t_python:.2f}s)")
                    print(f"    [crosscheck] |Δ| = {fmt(delta)}  "
                          f"rel = {fmt(rel)}  "
                          f"speedup = {rust_crosscheck['speedup_vs_python']}×")
                    # Enforce the gate (Copilot PR #895 review fix):
                    # cross-check mode is a verification mode, so a
                    # failing agreement must surface as a hard error.
                    if not agree_25:
                        raise RuntimeError(
                            f"rust-with-python-crosscheck failed for "
                            f"{label} (Z={Z}, N={N}): rel.diff = "
                            f"{fmt(rel)} exceeds 25-dps acceptance gate "
                            f"(1e-25).  This indicates a real divergence "
                            f"between the Rust and Python kernels, not "
                            f"numerical noise."
                        )
        else:
            tr_at_q0_mpf, n_strands, word_len, bridge_t_python = _bridge_tr_M(
                Z, N, q_str, dps=50)
            print(f"    n_strands = {n_strands},  word_length = {word_len}")
            print(f"    [bridge] tr_M(q_0) = {tr_at_q0_mpf}  "
                  f"({bridge_t_python:.2f}s)")
        # `bridge_elapsed_sec` reflects the PRIMARY kernel's wall time —
        # rust when canonical-rust path is the one that produced
        # `tr_at_q0_mpf`, python otherwise.  Cross-check overhead is
        # separately recorded in `rust_crosscheck.python_wall_sec`
        # (Copilot PR #895 review fix — dashboards must not see the
        # cross-check Python time as the production primary).
        if effective_method == "canonical-rust" and bridge_t_rust is not None:
            bridge_t = bridge_t_rust
        elif bridge_t_python is not None:
            bridge_t = bridge_t_python
        else:
            bridge_t = bridge_t_rust
        b_term1 = M_E_MEV * rho * abs(tr_at_q0_mpf)
        print(f"    Term-1 contribution: m_e · ρ · |tr_M| = {b_term1} MeV")

        # Optional symbolic cross-check (legacy path, slow at A>=2).
        symbolic_check = None
        if also_symbolic:
            try:
                t_sym = time.time()
                elem, stats = M.build_atom_nf_symbolic(Z, N, verbose=False)
                tr_q = tr_M_element(elem, n_strands, Z_SYMB, H_SYMB,
                                      simplify=False)
                free = list(tr_q.free_symbols)
                q60 = sp.Float(q_str, 60)
                tr_at_q0_sym = sp.N(tr_q.subs({s: q60 for s in free}), 50)
                tr_sym_mpf = mpf(str(tr_at_q0_sym))
                dt_sym = time.time() - t_sym
                diff = abs(tr_sym_mpf - tr_at_q0_mpf)
                print(f"    [sympy] tr_M(q_0) = {tr_sym_mpf}  ({dt_sym:.2f}s)")
                print(f"    |bridge - sympy|   = {diff}")
                # `abs_diff_vs_bridge` USED TO BE RECORDED WITHOUT A THRESHOLD.
                # It was computed, printed, stored as a field, and compared to
                # nothing — so `recomputed-low-isotope-mass-table.md`'s claim
                # that three production paths "agree to machine epsilon" rested
                # on a check that could not fail. Worse, this path sits behind
                # `also_symbolic` and had never been enabled: the committed
                # witness carries no `abs_diff_vs_bridge` for any of the five
                # atoms. Had it run before the `_D_HECKE_TOL` fix it would have
                # reported 8.14e-05 on the deuteron and still passed. Bean
                # `qou-4e5k`.
                sym_tol = mpf("1e-40")
                sym_ok = diff < sym_tol
                symbolic_check = {
                    "nf_terms": stats["n_terms_nf"],
                    "elapsed_sec": f"{dt_sym:.4f}",
                    "tr_M_at_q0_50dps": fmt(tr_sym_mpf),
                    "abs_diff_vs_bridge": fmt(diff),
                    "tolerance": fmt(sym_tol),
                    "passed": bool(sym_ok),
                }
                if not sym_ok:
                    print(f"    [sympy] MISMATCH: |bridge - sympy| = {diff} "
                          f"exceeds {sym_tol}")
            except Exception as exc:
                print(f"    [sympy] FAILED ({type(exc).__name__}: {exc})")
                symbolic_check = {"error": f"{type(exc).__name__}: {exc}"}

        # Markov-axiom recursive ascent (#508) — third independent path.
        # Build via `markov_peel.tr_M_atomic`, evaluate at 50 dps to
        # cross-check both the bridge and the symbolic legacy path.
        peel_check = None
        try:
            from markov_peel import tr_M_atomic
            from hecke_symbolic import q as q_peel_sym
            t_peel = time.time()
            tr_peel_sym = tr_M_atomic(Z, N)
            q60 = sp.Float(q_str, 60)
            free = list(tr_peel_sym.free_symbols) if hasattr(
                tr_peel_sym, "free_symbols") else [q_peel_sym]
            tr_peel_at_q0 = sp.N(
                tr_peel_sym.subs(
                    {s: q60 for s in free} if free else
                    {q_peel_sym: q60}),
                50)
            tr_peel_mpf = mpf(str(tr_peel_at_q0))
            dt_peel = time.time() - t_peel
            diff_peel = abs(tr_peel_mpf - tr_at_q0_mpf)
            print(f"    [peel]  tr_M(q_0) = {tr_peel_mpf}  ({dt_peel:.2f}s)")
            print(f"    |bridge - peel|    = {diff_peel}")
            peel_check = {
                "elapsed_sec": f"{dt_peel:.4f}",
                "tr_M_at_q0_50dps": fmt(tr_peel_mpf),
                "abs_diff_vs_bridge": fmt(diff_peel),
            }
        except Exception as exc:
            print(f"    [peel]  FAILED ({type(exc).__name__}: {exc})")
            peel_check = {"error": f"{type(exc).__name__}: {exc}"}

        # If a historical knot ID is available, compare numerically at q_0.
        comparison = None
        if historical_K and historical_K in J_PUBLISHED:
            J_sym = sp.sympify(J_PUBLISHED[historical_K])
            q60 = sp.Float(q_str, 60)
            J_at_q0 = sp.N(J_sym.subs({s: q60 for s in J_sym.free_symbols}), 50)
            J_at_q0_mpf = mpf(str(J_at_q0))
            ratio_q0 = tr_at_q0_mpf / J_at_q0_mpf if J_at_q0_mpf != 0 else None
            comparison = {
                "historical_K": historical_K,
                "J_K_published": fmt(J_sym),
                "J_K_at_q0_50dps": fmt(J_at_q0_mpf),
                "tr_M_over_J_K_at_q0_50dps": fmt(ratio_q0),
                "note":
                    "If the ratio is a power of q_0, then tr_M = q_0^k · J_K, "
                    "i.e. they agree up to writhe normalisation. "
                    "q_0 = " + q_str[:30] + "..., so log(ratio)/log(q_0) "
                    "should be close to an integer.",
            }
            print(f"    historical K = {historical_K}")
            print(f"    J_K(q_0)   = {J_at_q0_mpf}")
            print(f"    tr_M / J_K = {ratio_q0}")
            if ratio_q0 is not None and ratio_q0 != 0:
                from mpmath import log as mp_log
                k_estimate = mp_log(abs(ratio_q0)) / mp_log(mpf(q_str))
                print(f"    log(|ratio|)/log(q_0) = {k_estimate}  (integer ⇒ writhe match)")

        results.append({
            "atom": label,
            "Z": Z, "N": N, "A": Z + N,
            "n_strands_3A": n_strands,
            "rho_factor": rho,
            "word_length_3A": word_len,
            "n_crossings_canonical": n_crossings_canonical,
            "tr_M_at_q0_50dps": fmt(tr_at_q0_mpf),
            "term1_b_pred_mev_50dps": fmt(b_term1),
            "bridge_elapsed_sec": f"{bridge_t:.4f}",
            # `method` is the user-requested kernel; `effective_method`
            # reflects what actually produced `tr_M_at_q0_50dps` after
            # any fallback (Copilot PR #895 review).
            "method": method,
            "effective_method": effective_method,
            "rust_canonical_chi_elapsed_sec":
                None if bridge_t_rust is None else f"{bridge_t_rust:.6f}",
            "python_hoefsmit_elapsed_sec":
                None if bridge_t_python is None else f"{bridge_t_python:.4f}",
            "rust_crosscheck": rust_crosscheck,
            "symbolic_cross_check": symbolic_check,
            "peel_cross_check": peel_check,
            "historical_K_comparison": comparison,
        })

    stem = ("atomic-tr-m-mpfr-50dps" if anchor == "ideal"
            else "atomic-tr-m-mpfr-50dps-proton")
    out = {
        "computation": stem,
        # Self-declared layer, so a reader never has to infer the pin by
        # string-matching q0 — that inference is what let the two layers be
        # mistaken for one another.
        "q0Anchor": "muon" if anchor == "ideal" else "proton",
        "description":
            "Plan F advance — tr_M(T_w, q_0) via the 3A-strand atom-braid "
            "convention for proton, neutron, deuteron, tritium, ³He, "
            "evaluated at q_0 to 50 dps via the Hoefsmit + Wenzl bridge "
            "(Σ_λ y_λ · χ_λ) and (where applicable) compared against the "
            "published Jones polynomial of the historical knot ID. "
            "Companion to proton-mass-mpfr-50dps.witness.json.  "
            "Tritium / ³He at H_9 unblocked vs. legacy sympy path "
            "(>4-min timeout).",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "method": (
            "hoefsmit_wenzl_bridge: tr_M(W) = Σ_{λ ⊢ n} y_λ(q) · χ_λ(W); "
            "y_λ from y-lambda-mpfr-witness.json; χ_λ via per-partition "
            "Young-seminormal matrices in mpmath (sparse COO) at 50 dps; "
            "W is the atom_braid_word_3A Hecke-factor word"
        ),
        "structural_reference":
            "prop:full-pole-structure-mass-trace — tr_M(T_w, q) is "
            "meromorphic in q with simple poles at every primitive root "
            "of unity ζ_n^(j) (gcd(j,n)=1, n>=2); this witness reports "
            "tr_M evaluated at q = q_0 ≈ 1.11, the regular point used "
            "throughout the paper.  The prop's Mittag-Leffler / Habiro "
            "cyclotomic expansion expresses the same function as a sum "
            "over these poles; Habiro's convergence theorem guarantees "
            "the order-m Habiro truncation neglects only the ζ_1, …, "
            "ζ_m residues, so the values reported here are the LHS of "
            "the prop's equations (Mittag-Leffler eq. and Habiro eq.) "
            "at q = q_0.",
        "y_lambda_witness": "y-lambda-mpfr-witness.json",
        "q_0_50dps": q_str,
        # Same value under the key `q0_anchor_consistency_audit` actually
        # reads. Without it the audit cannot check the pin against the
        # anchor declared above and files the witness Q0_VALUE_MISSING —
        # which is exactly how a genuine flip stayed invisible here for
        # four days: the muon-labelled witness carried the PROTON value
        # (read from the pin file while 9a9c6b31c7 had it corrupted) and
        # the audit could not see it to say so. `q_0_50dps` is kept for
        # existing consumers.
        "q0Value": q_str,
        "symbolic_cross_check_enabled": also_symbolic,
        "precision_caveat": (
            "y-lambda-mpfr-witness.json was computed with q at f64 "
            "precision (its 'q' field stores str(float(Q0))); the y_λ "
            "values inherit f64-limited input. Bridge results agree "
            "with the prop-table canonical values to ~1e-15. To upgrade "
            "to full 50-dps precision, regenerate that witness with "
            "q_str at 50 dps (see y_lambda_mpfr_witness.py)."
        ),
        "results": results,
    }
    sys.path.insert(0, str(HERE))
    from witness_base import WitnessBuilder  # noqa: E402
    out_path = (
        WitnessBuilder.wrap_legacy(
            stem, out,
            script_path=__file__, engine="mpmath",
        )
        .set_audit_only(
            "docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
        .save()
    )
    print(f"\n  Output: {out_path}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--symbolic", action="store_true",
        help="Also run the legacy sympy tr_M_element path as a "
             "cross-check (slow at A>=2; will likely time out at A=3).")
    parser.add_argument(
        "--method", choices=("hoefsmit-python", "canonical-rust",
                             "rust-with-python-crosscheck"),
        default="canonical-rust",
        help="tr_M kernel selector (cheat sheet §5 fix #3 — Rust "
             "now default per 2026-05-23).  "
             "`canonical-rust` (default): the Rust `hecke-canonical-chi` "
             "binary via `canonical_tr_m_via_rust.compute_tr_m` — "
             "~500× faster at ⁴He, ~10⁶× at ¹⁰B vs the Python kernel.  "
             "Falls back to `hoefsmit-python` automatically if the "
             "Rust binary is not built (graceful, no error).  "
             "`hoefsmit-python` (legacy back-compat): the Hoefsmit + "
             "Wenzl-bridge mpf @ 50 dps kernel.  Useful for cross-check "
             "or when the Rust kernel is unavailable.  "
             "`rust-with-python-crosscheck`: run both kernels and "
             "assert agreement at 25 dps (uses Python wall time + "
             "Rust speedup gain).")
    parser.add_argument(
        "--anchor", choices=("ideal", "proton"), default="ideal",
        help="q0 layer. Default `ideal` (muon): this producer's stem is in "
             "q0_anchor_manifest.json `ideal_muon`. `proton` writes the "
             "separate experimental-layer witness the proton markov-peel "
             "cross-checks against; neither anchor ever rewrites the other's "
             "file.")
    args = parser.parse_args()
    sys.exit(main(also_symbolic=args.symbolic, method=args.method,
                  anchor=args.anchor))
