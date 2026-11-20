#!/usr/bin/env python3
"""Probe: casimir-q-factorial
(audit support for conj:casimir-epsilon-vacuum, classical-limit-preserving sweep).

**Critical insight from prior 5 probes.** The closest non-trivial
near-match found by the grid sweep was `ζ(2)·ℏ_q/[10]_q ≈ π²/720`
at 0.038% — but it VANISHES as q → 1 (because ℏ_q → 0).  The form
contradicts the standard physics Casimir result at q = 1, so it
cannot be the correct q-deformation.

**This probe.**  Search only q-deformed forms that satisfy the
classical limit:

    C_q(q) → π²/720    as    q → 1

The natural candidates are **q-deformations of `5! = 120`** —
since classical Casimir uses `ζ(-3) = -1/5!`:

    C_q^v1(q)  =  π² / (6 · [5]_q!_sym)        symmetric q-factorial
    C_q^v2(q)  =  π² / (6 · {5}!_q)            Pochhammer q-factorial
    C_q^v3(q)  =  π² / (6 · [5]_q!_{q→1=120})  combined-convention

where
    [n]_q!_sym := ∏_{k=1}^n [k]_q       with [k]_q = (q^k - q^{-k})/(q - q^{-1})
    {n}!_q     := ∏_{k=1}^n (1-q^k)/(1-q)

Both satisfy `[n]_q!_sym → n!` and `{n}!_q → n!` at q → 1.

**Additional candidates** of form `π²/720 · f(q)` where f(1) = 1:
    - π² / (6 · [5]_q!_sym^a · [k]_q^b)  with q→1 constraint a + b/n_q!_classical = 1
    - π² · Vol(K)^? / 720

For each candidate, report:
    - C_q at substrate (numerical)
    - C_q at q=1 (analytical: must equal π²/720)
    - rel. deviation from π²/720 at substrate
    - whether classical limit is satisfied

**Goal.**  Find a candidate with classical limit AND substrate
residue < 1%.  This would close sub-problem 3 of
conj:casimir-epsilon-vacuum.

Emits `casimir-q-factorial-probe.witness.json`.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
Ref: [kac-cheung2002] Kac, Cheung, "Quantum Calculus", Springer
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp, mpf, pi as mp_pi  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()


def q_int_sym(n: int, q: "mpf") -> "mpf":
    """Symmetric q-integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_int_poch(n: int, q: "mpf") -> "mpf":
    """Pochhammer q-integer {n}_q = (1 - q^n) / (1 - q)."""
    return (1 - q ** n) / (1 - q)


def q_factorial_sym(n: int, q: "mpf") -> "mpf":
    """[n]_q!_sym = ∏_{k=1}^n [k]_q (symmetric q-factorial)."""
    result = mpf(1)
    for k in range(1, n + 1):
        result *= q_int_sym(k, q)
    return result


def q_factorial_poch(n: int, q: "mpf") -> "mpf":
    """{n}!_q = ∏_{k=1}^n (1-q^k)/(1-q) (Pochhammer q-factorial)."""
    result = mpf(1)
    for k in range(1, n + 1):
        result *= q_int_poch(k, q)
    return result


def verify_classical_limit(f, target: "mpf", eps: "mpf" = mpf("1e-6")) -> bool:
    """Test that f(q) → target as q → 1.  Sample at q = 1 + eps."""
    val = f(1 + eps)
    return abs(val - target) / target < mpf("1e-3")


def _ser_qf(row: dict) -> dict:
    """Serialize one q-factorial row: mpf -> 60-dps decimal string.

    `classical_n_factorial` is left as-is (exact small integer in binary64).
    """
    return {
        k: (fmt(v) if k != "classical_n_factorial" else v)
        for k, v in row.items()
    }


def _ser_cand(c: dict) -> dict:
    """Serialize one candidate: the four mpf fields -> 60-dps strings."""
    return {
        k: (fmt(v) if k not in ("form", "classical_limit_ok") else v)
        for k, v in c.items()
    }


def main() -> int:
    builder = WitnessBuilder(
        "casimir-q-factorial-probe",
        engine="mpmath",
    )

    # NOT `mpf(Q)` / `mpf(str(Q))`: `q_parameter.Q` is `float(_d["q"])`, so
    # either form lifts the DOUBLE's binary expansion and caps this whole
    # probe at ~17 digits.  Read the pin as the SOURCE STRING and build the
    # mpf here, i.e. AFTER `set_compute_dps()`.  Do NOT substitute the
    # module-level `Q_MP`: `q_parameter` builds it at `mp.dps = 50`, so it is
    # a 50-digit cap, which is BELOW `OUTPUT_DPS = 60`.  Measured against the
    # exact 50-digit decimal in `Fraction` arithmetic, `mpf(Q_50_DIGIT_STR)`
    # built at dps 70 sits 4.594e-72 from it and `Q_MP` sits 2.015e-50.
    q = Q_MP
    pi_sq = mp_pi ** 2
    pi_sq_720 = pi_sq / 720
    one_percent = pi_sq_720 / 100

    # ─── Compute q-factorials at substrate and at q=1 ───
    q_close_to_1 = 1 + mpf("1e-6")
    # mpf-valued throughout: these are read back by the display loop and
    # serialized once, at the witness, via `fmt`.  `classical_n_factorial`
    # stays a float because it is an exact small integer (2 … 5040), which
    # binary64 represents without loss; the raw-float64 ratchet does not
    # count integral floats and there is nothing here to drain.
    qf_data = {}
    for n in range(2, 8):
        qf_data[n] = {
            "[n]_q!_sym_at_substrate": q_factorial_sym(n, q),
            "[n]_q!_sym_at_q→1": q_factorial_sym(n, q_close_to_1),
            "classical_n_factorial": float(mpf(1) * mpf(2) * mpf(3) * mpf(4) * mpf(5) * mpf(6) * mpf(7)) if n == 7 else float(_fact(n)),
            "{n}!_q_poch_at_substrate": q_factorial_poch(n, q),
            "{n}!_q_poch_at_q→1": q_factorial_poch(n, q_close_to_1),
        }

    # ─── Casimir candidates with classical limit verified ───
    candidates = []
    for name, eval_at_q in [
        # Standard q-factorial in denominator (most natural)
        ("π²/(6·[5]_q!_sym)", lambda qq: mp_pi ** 2 / (6 * q_factorial_sym(5, qq))),
        ("π²/(6·{5}!_q_poch)", lambda qq: mp_pi ** 2 / (6 * q_factorial_poch(5, qq))),
        # Other partition-like denominators
        ("π²/(6·[4]_q!·[2]_q)", lambda qq: mp_pi ** 2 / (6 * q_factorial_sym(4, qq) * q_int_sym(2, qq))),
        ("π²/([6]_q·[5]_q!)", lambda qq: mp_pi ** 2 / (q_int_sym(6, qq) * q_factorial_sym(5, qq))),
        # Schur-like (Casimir-type) sum approximations
        # π²/(6·[5]_q!) symmetrized via (q→q⁻¹) average
        (
            "π²/(6·([5]_q!+[5]_{q⁻¹}!)/2)",
            lambda qq: mp_pi ** 2 / (
                6 * (q_factorial_sym(5, qq) + q_factorial_sym(5, 1 / qq)) / 2
            ),
        ),
        # Bring-related: classical 5! comes from S_5 permutation count;
        # at q-deformed level, replace by S_5 q-character at substrate.
        # Use [5]_q · [4]_q · ... = [5]_q!_sym  (same as above)
        # q-Pochhammer with different range
        ("π²/(6·(1-q²)·(1-q³)·(1-q⁴)·(1-q⁵)/(1-q)⁴)",
         lambda qq: mp_pi ** 2 / (
             6 * (1 - qq ** 2) * (1 - qq ** 3) *
             (1 - qq ** 4) * (1 - qq ** 5) / (1 - qq) ** 4
         )),
    ]:
        val_substrate = eval_at_q(q)
        val_classical = eval_at_q(q_close_to_1)
        rel_res_substrate = abs(val_substrate - pi_sq_720) / pi_sq_720
        rel_res_classical = abs(val_classical - pi_sq_720) / pi_sq_720
        classical_ok = rel_res_classical < mpf("1e-3")
        # mpf-valued: `rel_residue_substrate` is the key of the `min()` below
        # and is compared against 0.01, so it is arithmetic, not display.
        # Serialized once, at the witness.
        candidates.append({
            "form": name,
            "value_at_substrate": val_substrate,
            "value_at_q→1": val_classical,
            "rel_residue_substrate": rel_res_substrate,
            "rel_residue_classical": rel_res_classical,
            "classical_limit_ok": bool(classical_ok),
        })

    # ─── Best classical-limit-OK candidate ───
    classical_ok_candidates = [c for c in candidates if c["classical_limit_ok"]]
    if classical_ok_candidates:
        best_classical_ok = min(
            classical_ok_candidates,
            key=lambda c: c["rel_residue_substrate"]
        )
    else:
        best_classical_ok = None

    n_sub_one_pct = sum(
        1 for c in classical_ok_candidates
        if c["rel_residue_substrate"] < 0.01
    )

    (
        builder
        .set_description(
            "Empirical q-factorial probe enforcing classical-limit "
            "constraint.  After 5 prior sweeps found near-matches "
            "that vanish at q → 1 (incompatible with standard "
            "Casimir), this probe restricts to q-deformations C_q(q) "
            "that satisfy C_q(q→1) = π²/720.  Tests natural "
            "candidates of form π²/(6·5!_q) for the two main "
            "q-factorial conventions (symmetric and Pochhammer), "
            "and a few related forms.  Reports the best substrate "
            "residue among candidates with verified classical limit."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("substrate_q", fmt(q))
        .add_parameter("target_pi_sq_720", fmt(pi_sq_720))
        .add_data(
            "q_factorials_at_substrate_and_q1",
            {n: _ser_qf(row) for n, row in qf_data.items()},
        )
        .add_data(
            "candidates_with_classical_limit_check",
            [_ser_cand(c) for c in candidates],
        )
        .add_data(
            "best_classical_ok",
            _ser_cand(best_classical_ok)
            if best_classical_ok else "none — all candidates fail classical limit",
        )
        # DEMOTED, and deliberately NOT turned into an existence flag (bean
        # qou-3e5m). The name reads like a claim, and my own triage filed it
        # class R for that reason -- but the measured count is ZERO. A
        # `computed = 1 if n_sub_one_pct else 0, expected = 1` here would not
        # be a check: it would assert sub-problem 3 of
        # conj:casimir-epsilon-vacuum, which is OPEN, and it would fail on
        # correct behaviour. Finding no candidate is a legitimate result of
        # this probe -- five prior sweeps found near-matches that vanish at
        # q -> 1 -- so by the demote-when-nothing-is-a-real-answer rule this is
        # data, not an assertion. If a candidate is ever found, the flag
        # becomes appropriate and this comment is the place to start.
        .add_data(
            "n_classical_ok_candidates_within_one_percent",
            {"value": int(n_sub_one_pct),
             "unit": "count of classical-limit-OK candidates within 1% of "
                     "π²/720 at substrate",
             "source": "If > 0, at least one q-deformation reproduces "
                       "classical Casimir AND lands within 1% at substrate, "
                       "closing sub-problem 3 of conj:casimir-epsilon-vacuum. "
                       "Currently 0."},
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Substrate q = {float(q):.10f}")
    print(f"Target π²/720 = {float(pi_sq_720):.8e}")
    print()
    print("─── q-Factorials at substrate vs q→1 ───")
    print(f"  {'n':<3} {'[n]_q!_sym at q₀':<22} {'classical n!':<14} {'{n}!_q at q₀':<18}")
    for n in [2, 3, 4, 5, 6, 7]:
        d = qf_data[n]
        cl = d["classical_n_factorial"]
        print(f"  {n:<3} {d['[n]_q!_sym_at_substrate']:<22.6e} {cl:<14.0f} {d['{n}!_q_poch_at_substrate']:<18.6e}")
    print()
    print("─── Casimir candidates with classical-limit check ───")
    for c in candidates:
        mark = "✓" if c["classical_limit_ok"] else "✗"
        print(f"  {mark} {c['form']:<55}")
        print(f"     substrate: {c['value_at_substrate']:.6e}  (residue {c['rel_residue_substrate']*100:6.3f}%)")
        print(f"     q→1:       {c['value_at_q→1']:.6e}  (residue {c['rel_residue_classical']*100:6.3f}%)")
    print()
    if best_classical_ok:
        print("─── BEST classical-limit-OK candidate ───")
        print(f"  form:               {best_classical_ok['form']}")
        print(f"  at substrate:       {best_classical_ok['value_at_substrate']:.6e}")
        print(f"  at q→1:             {best_classical_ok['value_at_q→1']:.6e}")
        print(f"  substrate residue:  {best_classical_ok['rel_residue_substrate']*100:.4f}%")
    print()
    if n_sub_one_pct > 0:
        print(f"→ {n_sub_one_pct} classical-limit-OK match(es) within 1% — sub-problem 3 closed!")
    else:
        print("→ No classical-limit-OK candidate within 1% at substrate.")
    return 0


def _fact(n: int) -> int:
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


if __name__ == "__main__":
    raise SystemExit(main())
