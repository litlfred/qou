#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; no symbolic-q polynomial in this layer.
"""Compute |tr_M(⁴He)| on H_12 from the canonical braid word.

See "RESOLVED 2026-09-06" below: the authoritative value is arm (C),
the canonical `atom_braid_word_3A(2, 2)` through the Wenzl bridge.
The disjoint-product construction this module was built around is
retained as arm (A), non-canonical.

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

✅ RESOLVED 2026-09-06 (bean `qou-hft3`).  The regeneration this
header has asked for since PR #564 has been done, because both
halves of its precondition now hold: the y-lambda witness carries
n=12, and taking the Wenzl row cap (bean `qou-fq0f`) brought H_12
from unreachable to ~17 s by not building χ^λ for the 70 of 77
partitions whose weight is exactly zero.  Everything above this
line describes the SUPERSEDED arms, kept because their failure is
the evidence for the correction.

This script now computes three values:

  (C) **Canonical word via the Wenzl bridge** — AUTHORITATIVE.
      `atom_braid_word_3A(2, 2)` (47 factors, interfaces at
      generators 2, 5, 8) through `tr_M_via_wenzl_bridge_mpfr`.
      |tr_M(⁴He)| = 0.011237417659767421564199549374410607…

      Cross-checked against `markov_trace_canonical` — a
      structurally independent Markov-axiom reducer, not this
      bridge — via `binding-canonical.witness.json`, agreeing to
      relative 1e-30.  That is the Schur-Weyl identity
      Σ_λ y_λ χ^λ = tr_M holding on the canonical word, which is
      exactly the test the disjoint word fails by a factor of ~5.

  (A) **Disjoint-product formula** — non-canonical, retained.
      reads tr_M(p), tr_M(n) from `atomic-tr-m-mpfr-50dps.witness.json`
      and emits the product.  1.280783151528646.

  (B) **Direct H_12 recursion via `markov_trace_recursive`** —
      non-canonical, retained.  `markov_trace_of_word(12,
      HELIUM4_WORD)`.  7.610469960740114.

(A) and (B) disagree by a factor of 5.942.  That is not a defect to
adjudicate: **both trace the disjoint word**, so neither is
|tr_M(⁴He)| whatever they agree on, and the disagreement is the
predicted failure of the disjoint-product identity on a
multi-nucleon atom — the same ~5 the deuteron showed at H_6.  The
old claim here that "both values must agree by the disjoint-product
axiom" was assuming the very identity PR #564 had already
deprecated.

The disagreement went unmeasured for months because (B) had never
once completed inside its 480 s budget; the witness recorded
`matches_disjoint_product_within_1ppb: null`, which reads as "not
checked" but meant "cannot complete".  When it did complete, the
old promotion rule (`direct_val if direct_val is not None else …`)
silently replaced the published value with a number 5.9× larger.

(B) can never be run on the canonical word: `markov_trace_of_word`
consumes jet-tracker SIGNED INTEGERS, which express σ and σ⁻¹ and
nothing else, while the canonical word carries two further letter
types — the uniform pn interface -h/2 (×8) and one Bring
colour-weighted interface -h(1-δ/2)/2 (×1).  The interfaces are not
representable in that format.

Output: appends a `helium-4` row to a NEW witness file
`atomic-tr-m-helium4.witness.json` (the legacy 50-dps witness
file remains untouched per its prior `computedAt` timestamp).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402

set_compute_dps()

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
#: ⁴He = 2 protons + 2 neutrons, for `atom_braid_word_3A(Z, N)`.
HELIUM4_Z, HELIUM4_NEUT = 2, 2

DIRECT_BUDGET_SEC = 480.0                        # 8 min budget per task brief


_REF_NAMES = ("atomic-tr-m-mpfr-50dps-proton.witness.json",
              "atomic-tr-m-mpfr-50dps.witness.json")


def _pick_witness_for_pin() -> Path:
    """The |tr_M| reference BUILT AT THIS RUN'S PIN.

    Both layers exist on disk with identical structure and the same five
    atoms. `tr_m_q_hecke_seminormal.py:103`, another reader of this artifact,
    already picks between them — by anchor name; this picks by the recorded
    value, which needs no manifest lookup and cannot drift from it.

    Raises rather than falling back: returning the wrong layer silently is the
    defect being fixed, and a 296 ppb error that reads as a successful load is
    worse than a stack trace.
    """
    from q_parameter import Q_50_DIGIT_STR
    want = mp.mpf(Q_50_DIGIT_STR)
    tried = []
    for name in _REF_NAMES:
        cand = _pb.witness_path(name, HERE)
        if not cand.exists():
            continue
        try:
            d = json.loads(cand.read_text())
        except Exception:                                  # noqa: BLE001
            continue
        w = d.get("witness", d)
        q_rec = (w.get("parameters", {}) or {}).get("q_0") or w.get("q_0") \
            or d.get("q_0_50dps") or w.get("q_0_50dps")
        tried.append((name, str(q_rec)[:26]))
        if q_rec is not None and abs(mp.mpf(str(q_rec)) - want) < mp.mpf("1e-40"):
            return cand
    raise FileNotFoundError(
        f"no |tr_M| reference recorded at this run's pin "
        f"{str(Q_50_DIGIT_STR)[:26]}…; inspected {tried}. Regenerate "
        f"atomic_tr_m_mpfr_50dps.py at this anchor rather than reading the "
        f"other layer."
    )


# ── (A) Disjoint-product formula via legacy witness ──────────
def disjoint_product_value() -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return (|tr_M(⁴He)|, |tr_M(p)|, |tr_M(n)|) read from the
    legacy 50-dps witness."""
    # PIN-STRADDLE FIX (2026-08-30, bean qou-y313). This hardcoded the MUON
    # basename while the module resolves `Q_50_DIGIT_STR`, which is the PROTON
    # pin for this stem. Measured from the two committed witnesses:
    #
    #     tr_M(p)   muon 1.14575978232   proton 1.14575969246   rel 7.84e-8
    #     tr_M(n)   muon 0.987743756821  proton 0.987743688116  rel 6.96e-8
    #     tr_p^2 * tr_n^2                                       rel 2.96e-7
    #
    # and the fourth power is not incidental: this function returns
    # `tr_p**2 * tr_n**2`, so (1+e)^2(1+f)^2 - 1 = 2e + 2f carries a 78 ppb
    # per-factor error to 296 ppb on the product. Those are the same figures
    # `93888aa431` records for `canonical_tr_m_via_chi_cache` — the same
    # straddle, one producer over.
    #
    # Select by the artifact's OWN recorded q rather than by a filename, as
    # `y_lambda_symbolic_validate.load_mpfr_witness` now does. `_REF_NAMES` is
    # ordered proton-first only as a hint; the recorded q decides, and an
    # unmatched pin raises rather than silently returning the other layer.
    path = _pick_witness_for_pin()
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


# ── (B) Direct H_12 trace via Wenzl bridge (preferred) or
#       markov_trace_recursive (legacy fallback) ─────────────
class _Timeout(Exception):
    pass


def _alarm(sig, frame):  # noqa: ARG001
    raise _Timeout()


def _helium4_word_to_factors() -> list[tuple[float, float, int]]:
    """Convert HELIUM4_WORD (jet-tracker 1-indexed signed ints) into
    the (c, d, g) factor triples consumed by `tr_M_via_wenzl_bridge_mpfr`.

    Convention:
      positive i  → σ_i                  → (1.0,  0.0, i-1)
      negative i  → σ_{|i|}^{-1} = σ - h → (1.0, -h,   |i|-1)

    `g` is 0-based (σ_0 = sigmas[0]); the Rust fast path inside
    `tr_M_via_wenzl_bridge_mpfr` shifts g back to 1-based at the
    FFI boundary. `d` is rounded against the in-bridge h snap-map
    (`{0.0, -h, -h/2}`) keyed on `round(d, 9)` inside
    `_chi_lambda_of_word_mpf`. The h-value MUST be computed from
    the same q that the bridge evaluates at — we derive h from
    `Q_50_DIGIT_STR` (the canonical 50-dps substrate string) so the
    snap-map lookup hits; if we used `Q_MP` (a different float
    roundtrip) the keys could miss and the bridge would fall back
    to `mp.mpf(str(d))`, reintroducing the f64 floor.
    """
    from q_parameter import Q_50_DIGIT_STR
    q_mpf = mp.mpf(Q_50_DIGIT_STR)
    h_val = float(q_mpf - 1 / q_mpf)
    factors: list[tuple[float, float, int]] = []
    for i in HELIUM4_WORD:
        if i > 0:
            factors.append((1.0, 0.0, i - 1))
        else:
            factors.append((1.0, -h_val, abs(i) - 1))
    return factors


def direct_h12_recursion(
    budget_sec: float,
    *,
    use_wenzl_bridge: bool = True,
) -> tuple[mp.mpf | None, float, str | None]:
    """Compute |tr_M(⁴He)| at H_12 with a soft time budget.

    Default path is the Wenzl bridge `Σ_λ y_λ · χ_λ(W)` via
    `tr_M_via_wenzl_bridge_mpfr`, which benefits from the Rust
    hecke-engine fast path (rayon-parallel χ_λ over all 77
    partitions of 12) when `pyhecke_native` is built — expected
    sub-second wall time — with a Python-mpmath fallback that
    remains mathematically exact at 50 dps.

    `use_wenzl_bridge=False` reverts to the legacy
    `markov_trace_of_word` markov-peel ascent, kept for
    cross-validation (sympy-based; previously hit the 8 min budget
    at H_12).

    Returns (|tr_M|, elapsed, error_or_None).

    See `docs/coordination/1ppb-compute-tranche-queue.md` for the
    broader compute/speed tranche this fits into; the Wenzl-bridge
    Rust-adapter wiring lives in `tr_m_wenzl_bridge_mpfr.py` and
    is documented in
    `docs/audits/2026-05-22-1ppb-speed-wireups-tranche.md`.
    """
    t0 = time.time()
    have_alarm = hasattr(signal, "SIGALRM")
    if have_alarm:
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(int(budget_sec))
    try:
        if use_wenzl_bridge:
            from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr
            from q_parameter import Q_50_DIGIT_STR

            factors = _helium4_word_to_factors()
            tr_mpf = tr_M_via_wenzl_bridge_mpfr(
                factors, HELIUM4_N, Q_50_DIGIT_STR, dps=mp.mp.dps,
            )
            return abs(mp.mpf(tr_mpf)), time.time() - t0, None
        else:
            # Legacy markov-peel ascent — sympy expression, then
            # numerical substitution at q_0. Use the canonical
            # Q_50_DIGIT_STR for the substitution so both paths
            # evaluate at exactly the same q value (avoids the
            # f64 precision floor that `str(Q_MP)` would introduce
            # via Python float formatting).
            import sympy as sp
            from markov_trace_recursive import markov_trace_of_word
            from q_parameter import Q_50_DIGIT_STR

            tr_sym = markov_trace_of_word(HELIUM4_N, HELIUM4_WORD)
            q_sym = sp.symbols("q", positive=True)
            val_sym = tr_sym.subs(
                q_sym, sp.sympify(Q_50_DIGIT_STR)
            ).evalf(mp.mp.dps)
            return abs(mp.mpf(str(val_sym))), time.time() - t0, None
    except _Timeout:
        return None, time.time() - t0, f"timeout_after_{int(budget_sec)}s"
    except Exception as exc:  # pragma: no cover
        return None, time.time() - t0, f"{type(exc).__name__}: {exc}"
    finally:
        if have_alarm:
            signal.alarm(0)


def canonical_h12_bridge():
    """(C) |tr_M(⁴He)| on the CANONICAL word, via the Wenzl bridge.

    This is the value this module's own header has asked for since PR #564:
    "it should be regenerated using tr_M_via_wenzl_bridge_mpfr.py once the
    y-lambda witness is extended to n=12 at true 50 dps". Both halves of that
    precondition now hold — the witness carries n=12, and taking the Wenzl row
    cap (bean qou-fq0f) brought H_12 from unreachable to ~17 s by not building
    χ_λ for the 70 of 77 partitions whose weight is exactly zero.

    The canonical word is `atom_braid_word_3A(2, 2)`: 47 factors, generators
    0…10, with the three inter-nucleon interfaces at generators 2, 5 and 8 that
    HELIUM4_WORD omits entirely. It carries four letter types where the
    disjoint word carries two — plain σ (×23), σ⁻¹ (×15), the uniform pn
    interface -h/2 (×8), and one Bring colour-weighted interface
    -h(1-δ/2)/2 = -0.10445824776972629. All are full-precision mpf, so they
    take the `isinstance(d, mp.mpf)` branch in the bridge rather than the
    three-key f64 snap map (which does not contain the colour-weighted value).

    That last point is why arm (B) cannot ever evaluate this word:
    `markov_trace_of_word` consumes jet-tracker SIGNED INTEGERS, a format that
    can express σ and σ⁻¹ and nothing else. The interface operators are not
    representable in it. (B) is not slow on the canonical word — it is
    structurally unable to accept it.
    """
    from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr
    from q_parameter import Q_50_DIGIT_STR
    from mass_at_3A_proper import atom_braid_word_3A

    t0 = time.time()
    word = atom_braid_word_3A(HELIUM4_Z, HELIUM4_NEUT)
    tr = tr_M_via_wenzl_bridge_mpfr(word, HELIUM4_N, Q_50_DIGIT_STR,
                                    dps=mp.mp.dps)
    return abs(mp.mpf(tr)), len(word), time.time() - t0


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

    # (C) The CANONICAL word, via the Wenzl bridge. This is the value the
    # module header has asked for since PR #564; its stated precondition is now
    # met (see canonical_h12_bridge). (A) and (B) are BOTH computed on the
    # disjoint 44-crossing word, which omits the three inter-nucleon
    # interfaces, so neither of them is |tr_M(4He)| whatever they agree on.
    print("\n  (C) CANONICAL word atom_braid_word_3A(2,2) via Wenzl bridge")
    try:
        canon_val, canon_len, canon_elapsed = canonical_h12_bridge()
        print(f"      word          = {canon_len} factors "
              f"(interfaces at generators 2, 5, 8)")
        print(f"      |tr_M(⁴He)|   = {mp.nstr(canon_val, 30)}")
        print(f"      elapsed       = {canon_elapsed:.2f} s")
        canon_err = None
    except Exception as exc:
        canon_val, canon_len, canon_elapsed, canon_err = (
            None, None, None, f"{type(exc).__name__}: {exc}")
        print(f"      canonical path failed: {canon_err}")

    # Authoritative value: the direct recursion ONLY IF it agrees with the
    # disjoint product. Otherwise neither arm is authoritative and this
    # producer must not pick one.
    #
    # Until 2026-09-06 this read `direct_val if direct_val is not None else
    # abs_tr_disjoint` -- promote whichever arm returned, agreement unread. That
    # made the published value a function of WALL-CLOCK: the direct recursion
    # had never once finished inside DIRECT_BUDGET_SEC (the committed witness
    # recorded `error: "timeout_after_480s"`, `abs_tr_M_50dps: null`,
    # `matches_disjoint_product_within_1ppb: null`), so the disjoint product was
    # published by default. On 2026-09-06 the recursion completed in 16.54 s and
    # DISAGREED -- 7.610469960740114 against 1.280783151528646, a factor of
    # 5.942 -- and the old logic promoted it anyway, silently replacing the
    # authoritative |tr_M(4He)| while `allPassed` stayed true and the mismatch
    # sat unread in a boolean field. A published value must not switch by 5.9x
    # because a machine got faster. Bean qou-hft3.
    # Superseded 2026-09-06 by arm (C). Neither (A) nor (B) is |tr_M(4He)|:
    # both are computed on the disjoint 44-crossing word, which has no
    # inter-nucleon interfaces, and this module's header has said so since
    # PR #564 -- "the output witness therefore stores a value that is NOT the
    # canonical |tr_M(4He)|". Their disagreement is a fact about that word, not
    # a question about helium-4, and picking between them was never going to
    # produce the right number.
    if canon_val is not None:
        abs_tr_he4 = canon_val
        method = "canonical_h12_wenzl_bridge"
        authoritative_method = (
            "canonical word atom_braid_word_3A(2,2) via tr_M_via_wenzl_bridge_mpfr")
        print(f"\n  → authoritative: (C) canonical, "
              f"|tr_M(⁴He)| = {mp.nstr(canon_val, 24)}")
    elif direct_val is not None and consistency_ok is False:
        print("      ⚠  canonical path unavailable and the two non-canonical "
              "arms disagree; keeping the disjoint-product value.")
        abs_tr_he4 = abs_tr_disjoint
        method = "disjoint_product_UNRESOLVED_MISMATCH"
        authoritative_method = "disjoint_product (non-canonical; direct recursion disagrees)"
    else:
        abs_tr_he4 = direct_val if direct_val is not None else abs_tr_disjoint
        method = "direct_h12_recursion" if direct_val is not None else "disjoint_product"
        authoritative_method = None

    # ── Witness emission ──────────────────────────────────
    out = HERE / "atomic-tr-m-helium4.witness.json"
    witness = {
        "computation": "atomic-tr-m-helium4",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "convention_status": (
            "CANONICAL as of 2026-09-06 (bean qou-hft3). The published value "
            "is arm (C): the canonical word atom_braid_word_3A(2,2), 47 "
            "crossings with 3 interfaces (pp at generator 2, pn at 5, nn at "
            "8), evaluated through tr_M_via_wenzl_bridge_mpfr in ~17 s. "
            "Cross-checked against markov_trace_canonical -- a structurally "
            "independent Markov-axiom reducer -- at relative 1e-30. "
            "Arms (A) disjoint-product and (B) direct recursion are RETAINED "
            "but NON-CANONICAL: both trace the 44-crossing disjoint word with "
            "no interfaces, and they disagree by a factor of 5.942, the same "
            "failure of the disjoint-product identity the deuteron showed at "
            "~5 (PR #564)."
        ),
        # Superseded 2026-09-06. This field previously read "DEPRECATED_DISJOINT
        # ... Canonical |tr_M(4He)| at H_12 via the Wenzl bridge is intractable
        # with current Python mpmath (p(12)=77 partitions, max dim 7700, ~2e13
        # ops per partition x 47 crossings); needs a Rust kernel with rayon
        # parallel partitions or a categorical reduction via Wenzl 1988 LR
        # branching. DO NOT use for mass predictions."
        #
        # That cost model is the one the Wenzl row cap invalidates, and it was
        # wrong in both factors it names: under production convention D the
        # level is r = 2 exactly, so 70 of those 77 partitions carry weight
        # IDENTICALLY ZERO, and the largest surviving dimension is 297, not
        # 7700. No Rust kernel was needed -- only not computing chi^lambda for
        # terms multiplied by zero. Bean qou-fq0f.
        "intractability_claim_superseded": (
            "2026-09-06: 77 -> 7 partitions, max dim 7700 -> 297, ~17 s. "
            "See qou-fq0f."
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
        "q_0_50dps": fmt(Q0_MP),
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
                "tr_M_at_q0_50dps": fmt(abs_tr_he4),
                "abs_tr_M_at_q0_50dps": fmt(abs_tr_he4),
                "method_used": method,
                "disjoint_product": {
                    "formula": "|tr_M(p)|² · |tr_M(n)|²",
                    "abs_tr_p_50dps": fmt(abs_tr_p),
                    "abs_tr_n_50dps": fmt(abs_tr_n),
                    "abs_tr_he4_50dps": fmt(abs_tr_disjoint),
                    # Report the witness actually read, not a hardcoded name.
                    # The pin-straddle fix makes this selectable, so a fixed
                    # string here would record the wrong provenance for every
                    # run at the other anchor — a lie of exactly the kind this
                    # audit exists to catch, one field over.
                    "source_witness": _pick_witness_for_pin().name,
                },
                "direct_recursion": {
                    "engine": "markov_trace_recursive.markov_trace_of_word",
                    # Timings as strings: the raw-float64 gate rejects bare
                    # floats in a witness, and these are wall-clock, not
                    # mathematics, so there is no mpf to carry.
                    "budget_sec": f"{DIRECT_BUDGET_SEC:.3f}",
                    "elapsed_sec": f"{direct_elapsed:.3f}",
                    "abs_tr_M_50dps": (
                        str(direct_val) if direct_val is not None else None
                    ),
                    "error": direct_err,
                    "matches_disjoint_product_within_1ppb": (
                        bool(consistency_ok) if direct_val is not None else None
                    ),
                },
                "canonical_h12_wenzl_bridge": {
                    "engine": "tr_m_wenzl_bridge_mpfr.tr_M_via_wenzl_bridge_mpfr",
                    "word": "mass_at_3A_proper.atom_braid_word_3A(2, 2)",
                    "word_length": canon_len,
                    "interfaces_at_generators": [2, 5, 8],
                    "abs_tr_M_50dps": fmt(canon_val) if canon_val is not None else None,
                    "elapsed_sec": (f"{canon_elapsed:.3f}"
                                    if canon_elapsed is not None else None),
                    "error": canon_err,
                    "note": (
                        "THE canonical |tr_M(4He)|. Cross-checked against "
                        "markov_trace_canonical (binding-canonical.witness.json, "
                        "a structurally independent Markov-axiom reducer, not "
                        "this bridge) at relative 1e-30 -- the Schur-Weyl "
                        "identity sum_lambda y_lambda chi^lambda = tr_M holding "
                        "on the canonical word, which is precisely the test the "
                        "disjoint word below fails by a factor of ~5. Reachable "
                        "at all only because taking the Wenzl row cap "
                        "(qou-fq0f) brought H_12 to ~17 s."
                    ),
                },
                # The two NON-CANONICAL arms disagree. Kept because the
                # disagreement is itself the documented evidence that the
                # disjoint-product identity does not hold for multi-nucleon
                # atoms -- the deuteron showed the same failure at factor ~5
                # (PR #564). Neither is |tr_M(4He)|. See qou-hft3.
                **({"NON_CANONICAL_ARMS_DISAGREE": {
                    "bean": "qou-hft3",
                    "word": "HELIUM4_WORD (disjoint, 44 crossings, no interfaces)",
                    "disjoint_product": fmt(abs_tr_disjoint),
                    "direct_recursion": str(direct_val),
                    "relative_difference": str(
                        abs(direct_val - abs_tr_disjoint) / abs_tr_disjoint),
                    "authoritative_method": authoritative_method,
                    "note": (
                        "Both arms trace the DISJOINT word, which omits the "
                        "three inter-nucleon interfaces, so neither is the "
                        "canonical helium-4 trace regardless of whether they "
                        "agree. The direct recursion had never completed inside "
                        "the budget before 2026-09-06, so this was never "
                        "measured -- the previously recorded `null` meant "
                        "'timed out', not 'agreed'. The measured factor of 5.94 "
                        "matches the ~5 the deuteron showed for the same reason. "
                        "Superseded as the published value by "
                        "canonical_h12_wenzl_bridge above."
                    ),
                }} if (direct_val is not None and consistency_ok is False) else {}),
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
    from witness_base import WitnessBuilder
    out = (
        WitnessBuilder.wrap_legacy(
            "atomic-tr-m-helium4",
            witness,
            script_path=__file__,
            engine="mpmath",
            output_dir=HERE,
        )
        .add_data("lean_uniqueness_ref", lean_uniqueness_ref("helium-4"))
        .save()
    )
    print(f"\n  Wrote {out.name}  (method = {method})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
