#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; no symbolic-q polynomial in this layer.
"""Compute |tr_M(⁴He)| via the disjoint-product extension on H_12.

⚠ CONVENTION CORRECTION (PR #564, 2026-05-08).  This script uses the
*disjoint* multi-atom word inherited from
`markov_trace_axiomatic_multi_atom.py`.  Per the convention audit
(see `hecke-branching-trace-decomposition.md`), the disjoint-product
identity tr_M(α⊗β) = tr_M(α)·tr_M(β) is **only valid for genuine
disjoint-cluster braids** (e.g. an unknot operator on a disjoint
strand bundle), NOT for multi-nucleon atoms whose canonical word
(from `mass_at_3A_proper.atom_braid_word_3A`) includes operator-
valued σ_{3k} interfaces between adjacent nucleons.

Empirical evidence (deuteron, P3' from rho_k_h3a_refinement.py):
the disjoint 22-crossing word σ₁⁷σ₂⁴σ₄⁶σ₅⁴σ₄⁻¹ fails the
Schur-Weyl identity Σ_λ y_λ χ^λ = tr_M by factor ~5; the canonical
23-crossing word with σ_3 interface matches at machine precision.

For ⁴He, the canonical word atom_braid_word_3A(2, 2) has 47
crossings with 3 interfaces (pp at gen 2, pn at gen 5, nn at gen 8),
not the 44 crossings used here.  The output witness
`atomic-tr-m-helium4.witness.json` therefore stores a value that
is NOT the canonical |tr_M(⁴He)|; it should be regenerated using
tr_M_via_wenzl_bridge_mpfr.py once the y-lambda witness is extended
to n=12 at true 50 dps.

Per the AUDIT-DEEP-2026-05.md §3.3a resolution, ⁴He was originally
identified as the disjoint product

    ⁴He = proton ⊗ proton ⊗ neutron ⊗ neutron

on H_12 with the four 3-strand clusters placed on strand sets
{1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}.  The braid word follows
the established multi-atom pattern from
`markov_trace_axiomatic_multi_atom.py`:

    proton-on-{i,i+1,i+2}  : σ_i⁷ σ_{i+1}⁴
    neutron-on-{i,i+1,i+2} : σ_i⁶ σ_{i+1}⁴ σ_i⁻¹

For ⁴He on strand sets {1,2,3}/{4,5,6}/{7,8,9}/{10,11,12} the word is

    σ₁⁷ σ₂⁴  ·  σ₄⁷ σ₅⁴  ·  σ₇⁶ σ₈⁴ σ₇⁻¹  ·  σ₁₀⁶ σ₁₁⁴ σ₁₀⁻¹

which has 7+4 + 7+4 + 6+4+1 + 6+4+1 = 44 crossings on 12 strands.

Under the (deprecated) disjoint-product convention
  tr_M(α ⊗ β) = tr_M(α) · tr_M(β),
the helium-4 trace would factor as

    tr_M(⁴He) = tr_M(p)² · tr_M(n)²,

so |tr_M(⁴He)| = |tr_M(p)|² · |tr_M(n)|².

⚠ The convention audit on PR #564 *removed* the deuteron disjoint-
product check from `markov-trace-axiomatic-multi-atom.witness.json`
(it was tautological for the disjoint word but did not validate the
deuteron physics; see `convention_status: DEPRECATED_NON_CANONICAL`
in that witness). The disjoint-product identity therefore is **not
empirically verified** for multi-nucleon atoms; this script's value
is retained only as a placeholder pending the Rust-kernel canonical
recompute described in `atomic-tr-m-helium4.witness.json`'s
`convention_status` field.

This script computes both values in parallel:

  (A) **Disjoint-product formula** (fast, exact):
      reads tr_M(p), tr_M(n) from `atomic-tr-m-mpfr-50dps.witness.json`
      and emits the product.

  (B) **Direct H_12 recursion via `markov_trace_recursive`** (slow,
      authoritative): runs `markov_trace_of_word(12, helium4_word)`
      with a runtime budget; emits the value if it returns within
      budget, otherwise records a stub and the elapsed time so the
      next session can pick up.

Both values must agree by the disjoint-product axiom.  We commit
the disjoint-product value as authoritative whenever (B) does not
return in budget; this is consistent with the deuteron pattern
(disjoint-product matches direct recursion to 1e-30 in the
deuteron witness).

Output: appends a `helium-4` row to a NEW witness file
`atomic-tr-m-helium4.witness.json` (the legacy 50-dps witness
file remains untouched per its prior `computedAt` timestamp).
"""
from __future__ import annotations

import json
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from q_parameter import Q_MP  # noqa: E402

Q0_MP = mp.mpf(str(Q_MP))


# ── ⁴He braid word on H_12 ───────────────────────────────────
# Convention: positive ints = σ_i (1-indexed, jet-tracker style),
# negative = σ_i^{-1}.
# Four disjoint 3-strand clusters at strand offsets 0, 3, 6, 9:
HELIUM4_WORD = (
    [1] * 7 + [2] * 4                            # proton on {1,2,3}
    + [4] * 7 + [5] * 4                          # proton on {4,5,6}
    + [7] * 6 + [8] * 4 + [-7]                   # neutron on {7,8,9}
    + [10] * 6 + [11] * 4 + [-10]                # neutron on {10,11,12}
)
HELIUM4_WORD_LEN = len(HELIUM4_WORD)             # 44 crossings
HELIUM4_N = 12

DIRECT_BUDGET_SEC = 480.0                        # 8 min budget per task brief


# ── (A) Disjoint-product formula via legacy witness ──────────
def disjoint_product_value() -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return (|tr_M(⁴He)|, |tr_M(p)|, |tr_M(n)|) read from the
    legacy 50-dps witness."""
    path = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
    if not path.exists():
        raise FileNotFoundError(
            f"Required legacy |tr_M| witness not found at {path}; "
            "run atomic_tr_m_mpfr_50dps.py first."
        )
    d = json.loads(path.read_text())
    rows = {r["atom"]: r for r in d.get("results", [])}
    tr_p = abs(mp.mpf(rows["proton"]["tr_M_at_q0_50dps"]))
    tr_n = abs(mp.mpf(rows["neutron"]["tr_M_at_q0_50dps"]))
    return tr_p ** 2 * tr_n ** 2, tr_p, tr_n


# ── (B) Direct H_12 recursion via markov_trace_recursive ─────
class _Timeout(Exception):
    pass


def _alarm(sig, frame):  # noqa: ARG001
    raise _Timeout()


def direct_h12_recursion(budget_sec: float) -> tuple[mp.mpf | None, float, str | None]:
    """Try `markov_trace_of_word(12, helium4_word)` with a soft
    time budget.  Returns (|tr_M|, elapsed, error_or_None)."""
    import sympy as sp  # noqa: F401  (used inside the import)

    from markov_trace_recursive import markov_trace_of_word

    t0 = time.time()
    # Use SIGALRM as a soft watchdog (POSIX only; safe on Linux deploy).
    have_alarm = hasattr(signal, "SIGALRM")
    if have_alarm:
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(int(budget_sec))
    try:
        tr_sym = markov_trace_of_word(HELIUM4_N, HELIUM4_WORD)
    except _Timeout:
        return None, time.time() - t0, f"timeout_after_{int(budget_sec)}s"
    except Exception as exc:  # pragma: no cover
        return None, time.time() - t0, f"{type(exc).__name__}: {exc}"
    finally:
        if have_alarm:
            signal.alarm(0)

    # Evaluate at q_0 to 50 dps.
    import sympy as sp
    q_sym = sp.symbols("q", positive=True)
    val_sym = tr_sym.subs(q_sym, sp.sympify(str(Q_MP))).evalf(mp.mp.dps)
    return abs(mp.mpf(str(val_sym))), time.time() - t0, None


# ── Main ─────────────────────────────────────────────────────
def main() -> int:
    print("=" * 96)
    print("  ⁴He |tr_M| via H_12 disjoint product  (PR #564, foreground task)")
    print("    Word: σ₁⁷σ₂⁴ · σ₄⁷σ₅⁴ · σ₇⁶σ₈⁴σ₇⁻¹ · σ₁₀⁶σ₁₁⁴σ₁₀⁻¹  (44 crossings on H_12)")
    print("=" * 96)

    # (A) Disjoint-product value (always cheap).
    print("\n  (A) Disjoint-product formula |tr_M(⁴He)| = |tr_M(p)|² · |tr_M(n)|²")
    abs_tr_disjoint, abs_tr_p, abs_tr_n = disjoint_product_value()
    print(f"      |tr_M(p)|     = {mp.nstr(abs_tr_p, 16)}")
    print(f"      |tr_M(n)|     = {mp.nstr(abs_tr_n, 16)}")
    print(f"      |tr_M(⁴He)|   = {mp.nstr(abs_tr_disjoint, 16)}")

    # (B) Direct H_12 recursion (budgeted).
    print(f"\n  (B) Direct recursion: markov_trace_of_word(12, word)  (budget {int(DIRECT_BUDGET_SEC)} s)")
    direct_val, direct_elapsed, direct_err = direct_h12_recursion(DIRECT_BUDGET_SEC)
    if direct_val is not None:
        print(f"      |tr_M(⁴He)|   = {mp.nstr(direct_val, 16)}")
        print(f"      elapsed       = {direct_elapsed:.2f} s")
        rel_diff = abs(direct_val - abs_tr_disjoint) / abs_tr_disjoint
        print(f"      Δ vs (A)      = {mp.nstr(rel_diff, 6)}")
        consistency_ok = rel_diff < mp.mpf("1e-30")
        if consistency_ok:
            print("      ✅ direct H_12 recursion matches disjoint product to mpmath-exact precision")
        elif rel_diff < mp.mpf("1e-9"):
            print("      ✓  direct H_12 recursion matches disjoint product within 1 ppb")
            consistency_ok = True
        else:
            print("      ✗  MISMATCH — investigate disjoint-product application on H_12")
    else:
        print(f"      direct-path skipped: {direct_err}  (elapsed {direct_elapsed:.2f}s)")
        consistency_ok = None  # not exercised this run

    # Authoritative value: prefer direct if it returned, else disjoint-product.
    abs_tr_he4 = direct_val if direct_val is not None else abs_tr_disjoint
    method = "direct_h12_recursion" if direct_val is not None else "disjoint_product"

    # ── Witness emission ──────────────────────────────────
    out = HERE / "atomic-tr-m-helium4.witness.json"
    witness = {
        "computation": "atomic-tr-m-helium4",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "convention_status": (
            "DEPRECATED_DISJOINT — value below uses the disjoint-product "
            "convention (44 crossings, no interface) which is empirically "
            "wrong per PR #564 audit. Canonical word atom_braid_word_3A(2,2) "
            "has 47 crossings with 3 interfaces (pp, pn, nn). Canonical "
            "|tr_M(⁴He)| at H_12 via the Wenzl bridge is intractable with "
            "current Python mpmath (p(12)=77 partitions, max dim 7700, "
            "~2×10¹³ ops per partition × 47 crossings); needs a Rust kernel "
            "with rayon parallel partitions or a categorical reduction via "
            "Wenzl 1988 LR branching. DO NOT use for mass predictions."
        ),
        "auditOnly": "AUDIT-DEEP-2026-05.md",
        "description": (
            "⁴He |tr_M| extension to H_12: disjoint product of two protons and "
            "two neutrons on strand sets {1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}. "
            "Companion to atomic-tr-m-mpfr-50dps.witness.json (which covers "
            "p, n, D, T, ³He at H_3/H_6/H_9 with the canonical convention). "
            "The disjoint-product identity tr_M(α⊗β)=tr_M(α)·tr_M(β) is only "
            "valid for genuine disjoint-cluster braids (e.g. unknot operators), "
            "NOT for multi-nucleon atoms whose canonical word includes "
            "operator-valued σ_{3k} interfaces. The deuteron 'disjoint check' "
            "previously cited here was REMOVED from "
            "markov-trace-axiomatic-multi-atom.witness.json on PR #564 "
            "(tautological for the disjoint word; did not validate physics)."
        ),
        "audit_reference": "AUDIT-DEEP-2026-05.md §3.3a (P4″) + convention audit PR #564",
        "pr": "#564",
        "precision": "mpfr_50dps_disjoint_only",
        "method": method,
        "q_0_50dps": str(Q0_MP),
        "results": [
            {
                "atom": "helium-4",
                "Z": 2,
                "N": 2,
                "A": 4,
                "n_strands_3A": HELIUM4_N,
                "rho_factor": 2,
                "word_length_3A": HELIUM4_WORD_LEN,
                "braid_word_jet_tracker": HELIUM4_WORD,
                "braid_word_str": (
                    "σ₁⁷σ₂⁴ · σ₄⁷σ₅⁴ · σ₇⁶σ₈⁴σ₇⁻¹ · σ₁₀⁶σ₁₁⁴σ₁₀⁻¹"
                ),
                "tr_M_at_q0_50dps": str(abs_tr_he4),
                "abs_tr_M_at_q0_50dps": str(abs_tr_he4),
                "method_used": method,
                "disjoint_product": {
                    "formula": "|tr_M(p)|² · |tr_M(n)|²",
                    "abs_tr_p_50dps": str(abs_tr_p),
                    "abs_tr_n_50dps": str(abs_tr_n),
                    "abs_tr_he4_50dps": str(abs_tr_disjoint),
                    "source_witness": "atomic-tr-m-mpfr-50dps.witness.json",
                },
                "direct_recursion": {
                    "engine": "markov_trace_recursive.markov_trace_of_word",
                    "budget_sec": DIRECT_BUDGET_SEC,
                    "elapsed_sec": direct_elapsed,
                    "abs_tr_M_50dps": (
                        str(direct_val) if direct_val is not None else None
                    ),
                    "error": direct_err,
                    "matches_disjoint_product_within_1ppb": (
                        bool(consistency_ok) if direct_val is not None else None
                    ),
                },
                "historical_K_comparison": {
                    "registry_status": (
                        "REGISTRY_PHASE_3B in joint_tower_sdp_solver_v2.py "
                        "covers p, n, D, T, ³He but NOT ⁴He.  The literature "
                        "identification (Borromean / B_3² in B_3) is recorded "
                        "for future cross-checks but is not used here — the "
                        "disjoint-product extension on H_12 is sufficient for "
                        "the leading-order ρ_K ansatz of P4″."
                    ),
                    "literature_candidate": "Borromean (B_3² in B_3)",
                },
            }
        ],
    }
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  Wrote {out.name}  (method = {method})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
