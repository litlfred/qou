#!/usr/bin/env python3
"""Gate: every y_λ table must satisfy the convention-D two-row cap.

Convention D is Wenzl level r = 2, and
`QOU.MassTheory.TwoRowCapDerived.massWeight_eq_zero_of_three_rows_of_wenzl`
(sorry-free) proves `y_λ = 0` whenever `ℓ(λ) > 2`. A table that carries
appreciable weight on a three-or-more-row partition is therefore **not** a
D-frame table, whatever its filename or its `q0` field says.

WHY THIS EXISTS.  `block-swap-binding.witness.json` sat on `main` from
2026-06-22 carrying a value produced by a table that failed this test:

    June-15 table   max|y| over ℓ>2 = 1.98e-4
                    min|y| over ℓ≤2 = 8.77e-5      ratio 2.26
    D-frame table   max|y| over ℓ>2 = 1.03e-73
                    min|y| over ℓ≤2 = 2.29e-4      ratio 4.5e-70

Those ℓ>2 shapes were LARGER than the smallest surviving two-row weight and
carried 7.05 % of `tr_M` (0.8856 against 0.8232 restricted). Nothing caught
it, because nothing looked: the value was only re-derivable once the
producer became runnable at all, two months later (bean `qou-lr57`).

WHAT MAKES IT CHEAP.  The test needs no producer, no braid word, no anchor
and no character evaluation — only the table. It is O(#partitions), runs in
well under a second, and is a pure function of the file. That is the whole
point: the defect it catches is upstream of every consumer, so checking it
at the table costs one test instead of one per consumer.

Exit 0 clean, 1 on any violation.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

import _path_bridge  # noqa: F401, E402  -- substrate modules live in substrate/
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _Y_LAMBDA_BY_ANCHOR, _load_y_lambda  # noqa: E402

# Raise the working precision BEFORE any module-scope `mpf` is built.
# `mp.mpf("1e-30")` below is string-sourced, which is necessary but not
# sufficient: at mpmath's default dps of 15 the constant is still rounded
# to ~53 bits (measured: 8.3e-17 relative against the same literal at 65
# dps). Neither this gate's verdicts nor its 40-orders-of-headroom framing
# turn on that, but the import-time-dps ratchet is a ratchet and this file
# was the one entry taking it red.
set_compute_dps()

#: Convention D forces the ratio to ~1e-70 (pure solver residue against an
#: exact zero). The June table that motivated this gate scored 2.26. Anything
#: between those is not a near-miss to be argued about — it is a different
#: weight family. 1e-30 sits 40 orders clear of compliant and 30 clear of the
#: known-bad case, so the verdict never turns on where the line is drawn.
CAP_RATIO_MAX = mp.mpf("1e-30")

#: n values to test. H_12 is the ⁴He atom width and the case qou-lr57 was
#: found at; H_6 and H_9 are the deuteron/triton widths below it.
N_VALUES = (6, 9, 12)


def check_table(anchor: str, path: Path) -> list[str]:
    """Return a list of violation strings for one table (empty = clean)."""
    out: list[str] = []
    for n in N_VALUES:
        try:
            y = _load_y_lambda(n, path)
        except Exception as exc:                       # noqa: BLE001
            out.append(f"{anchor} n={n}: LOAD FAILED {type(exc).__name__}: {exc}")
            continue
        if not y:
            out.append(f"{anchor} n={n}: table is empty")
            continue
        tall = [s for s in y if len(s) > 2]
        flat = [s for s in y if len(s) <= 2]
        if not flat:
            out.append(f"{anchor} n={n}: no two-row entries at all")
            continue
        if not tall:
            continue                                   # nothing to violate
        hi = max(abs(mp.mpf(str(y[s]))) for s in tall)
        lo = min(abs(mp.mpf(str(y[s]))) for s in flat)
        if lo == 0:
            out.append(f"{anchor} n={n}: a two-row weight is exactly 0")
            continue
        ratio = hi / lo
        status = "ok " if ratio <= CAP_RATIO_MAX else "BAD"
        print(f"  {status} {anchor:<7} n={n:<3} "
              f"max|y| ℓ>2 = {mp.nstr(hi, 6):<14} "
              f"min|y| ℓ≤2 = {mp.nstr(lo, 6):<14} ratio = {mp.nstr(ratio, 4)}")
        if ratio > CAP_RATIO_MAX:
            out.append(
                f"{anchor} n={n}: two-row cap VIOLATED — ratio {mp.nstr(ratio, 6)} "
                f"exceeds {mp.nstr(CAP_RATIO_MAX, 3)}. The ℓ(λ)>2 weights are not "
                f"zero, so this is not a convention-D table.")
    return out


#: The known-bad table, by the revision that predates its regeneration.
#: `acfc4fb2b8` ("regenerate y-lambda-mpfr-witness at muon q0", 2026-06-30)
#: replaced it; `79c484df7f` (2026-06-15) is the version that was live when
#: block-swap-binding's witness was computed on 2026-06-22.
SELFTEST_REV = "79c484df7f"
SELFTEST_PATH = "computations/y-lambda-mpfr-witness.json"


def selftest() -> int:
    """Prove the gate can FAIL. A gate that has never rejected anything is
    not evidence — it is a green light with no bulb behind it.

    Extracts the June-15 table out of git and asserts the gate rejects it.
    If git cannot reach that revision (a shallow clone that does not carry
    it), SKIP loudly rather than passing: an unrunnable self-test must not
    read as a passing one."""
    import subprocess
    import tempfile
    print("SELF-TEST — the gate must REJECT the June-15 table")
    try:
        blob = subprocess.check_output(
            ["git", "show", f"{SELFTEST_REV}:{SELFTEST_PATH}"],
            cwd=str(_HERE.parent.parent), stderr=subprocess.DEVNULL)
    except Exception as exc:                           # noqa: BLE001
        print(f"  SKIP — cannot reach {SELFTEST_REV} ({type(exc).__name__}). "
              f"This is NOT a pass; the gate is unverified in this clone.")
        return 2
    with tempfile.NamedTemporaryFile("wb", suffix=".json", delete=False) as fh:
        fh.write(blob)
        tmp = Path(fh.name)
    bad = check_table("june-15", tmp)
    tmp.unlink(missing_ok=True)
    if bad:
        print(f"  PASS — rejected it, {len(bad)} violation(s):")
        for b in bad:
            print(f"    {b}")
        return 0
    print("  FAIL — the gate ACCEPTED a table known to violate the cap by "
          "ratio 2.26. The check is not doing what it claims.")
    return 1


def main() -> int:
    mp.mp.dps = 60
    if "--selftest" in sys.argv:
        return selftest()
    print("y_λ two-row cap gate — convention D (Wenzl r=2) forces y_λ=0 for ℓ(λ)>2")
    print(f"  threshold: max|y| over ℓ>2  /  min|y| over ℓ≤2  ≤  {mp.nstr(CAP_RATIO_MAX, 3)}")
    violations: list[str] = []
    for anchor, path in sorted(_Y_LAMBDA_BY_ANCHOR.items()):
        if not Path(path).exists():
            violations.append(f"{anchor}: table missing at {path}")
            continue
        violations.extend(check_table(anchor, Path(path)))
    print()
    if violations:
        print(f"FAIL — {len(violations)} violation(s):")
        for v in violations:
            print(f"  {v}")
        return 1
    print("PASS — every y_λ table satisfies the two-row cap.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
