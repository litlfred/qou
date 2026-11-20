#!/usr/bin/env python3
"""How many digits does the float64 character kernel actually deliver?

`mass_at_3A_proper.chi_lambda_of_word` is a float64 kernel by contract -- its
own docstring says so: *"no caller has ever received more than 53 bits from
here."* Four producers use it as their ONLY route
(`native_5_strand_baryon`, `phase3_deuteron_tritium_h_expansion`,
`rho_k_h3a_gg_trajectory`, `tr_m_q_hecke_seminormal`), and the first three of
those write a witness.

"It is float64, therefore ~1e-16" is the assumption this probe exists to
replace. 1e-16 is the ULP FLOOR, not a measurement: a character is a trace of a
PRODUCT over the whole braid word, so rounding accumulates with word length, and
the word coefficients (c, d) alternate in sign. The question is how far above
the floor the real words land -- and that is not something a source-text reading
can answer, only a run.

MEASURED (proton pin, `mp.dps` >= 50 for the exact side):

    deuteron  A=2, |word| = 23   worst rel gap 5.4e-15   ~24x the ulp floor
    helium-3  A=3, |word| = 35   worst rel gap 8.2e-15   ~37x the ulp floor

So the kernel delivers roughly FOURTEEN good digits, and the loss GROWS with
word length -- 23 ops to 35 ops moved it 24x -> 37x, so A >= 4 is worse again.

WHY THAT NUMBER MATTERS RATHER THAN BEING A CURIOSITY. The L1 precision goal is
internal cross-method agreement <= 1 ppQ = 1e-15 (AGENTS.md, "Precision goals").
Every gap above is LARGER than that. A quantity computed through this kernel
therefore cannot meet L1 -- not as a matter of taste about float64, but
arithmetically. Any producer that reports more than ~14 significant digits from
it, or claims agreement "to 1 ppQ", is reporting its own rounding.

AND ALL FOUR CONSUMERS PUBLISH PAST THAT CEILING. The gap alone does not tell
you whether it matters -- a witness storing SIX significant digits is untouched
by a 14-digit kernel. Measured over the committed witnesses of the four
float64-only producers (`consumer_census()`, run at the end of this probe):

    native-5-strand-baryon        n= 28  max 18 digits    71% carry > 14
    rho-k-h3a-gg-trajectory       n=136  max 17 digits    82% carry > 14
    tr-m-q-hecke-seminormal       n= 70  max 18 digits    87% carry > 14
    phase3-deuteron-tritium-...   n=  6  max 15 digits   100% carry > 14

So all four publish digits their own computation does not determine. That is
what scopes the migration -- not "float64 is bad".

THE FOURTH ONE ALMOST ESCAPED, AND THE WAY IT DID IS THE POINT. A first pass
here walked only BARE FLOATS and reported `phase3` as carrying none, i.e. clean.
It is not: it stores "12.7030229395046" -- fifteen digits AS A STRING, which is
what `_precision.fmt` emits. Worse, the raw-float64 ratchet keys on the same
representation, so `phase3` is the one consumer absent from
`raw-float64-baseline.json`. Two detectors "agreeing" that it is clean was a
SHARED BLIND SPOT, not independent corroboration -- and it very nearly went into
a PR as evidence.

The exact route (`hoefsmit_mpmath.chi_lambda_of_word_sparse_mp`, PR #5648)
carries the same word at full precision; Hoefsmit seminormal matrices hold <= 2
nonzeros per row, so it costs O(dim^2 * |word| * nnz) rather than the dense
O(dim^3 * |word|) that made the exact route "not a drop-in for the A >= 4
producers" in the float64 kernel's own docstring.

Writes no witness: the deliverable is the digit count, and it is in this
docstring and in the run output.

Run:  python3 -u computations/probes/chi_lambda_float64_precision_loss_probe.py
"""
import re as _re
import sys
from pathlib import Path

_R = Path(__file__).resolve().parent.parent
for _p in (_R, _R / "probes", _R / "substrate",
           _R.parent / "tools" / "qou-substrate" / "python"):
    sys.path.insert(0, str(_p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
from mpmath import mp  # noqa: E402

# mpmath does NOT set dps on import of `_precision`; its default is 15, which is
# float64-grade. Benchmarking both routes at dps 15 makes them agree for that
# reason alone -- measured, and the reason this assert is here rather than a
# comment.
assert mp.dps >= 50, f"exact side needs >= 50 dps, got {mp.dps}"

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word  # noqa: E402
from hoefsmit_mpmath import (BlockCacheMP, chi_lambda_of_word_sparse_mp,  # noqa: E402
                             seminormal_matrices_mp)
from pyhecke.syt_prefix_cache import (BlockCache,  # noqa: E402
                                      build_seminormal_matrices_cached)

# The float64 ulp, for expressing each gap as a MULTIPLE of the floor rather
# than as a bare exponent -- "5e-15" reads like the floor; "24x the floor" does
# not.
_ULP = mp.mpf("2.220446049250313e-16")


def _two_row_partitions(n: int, max_rows: int):
    out: list[tuple[int, ...]] = []

    def walk(rem: int, cap: int, pre: tuple[int, ...]) -> None:
        if rem == 0:
            if len(pre) <= max_rows:
                out.append(pre)
            return
        for k in range(min(rem, cap), 0, -1):
            if len(pre) < max_rows:
                walk(rem - k, k, pre + (k,))

    walk(n, n, ())
    return out



# ── what the consumers actually PUBLISH ─────────────────────────────────
#
# The gap above is only half the question. A witness that stores SIX significant
# digits is untouched by a 14-digit kernel; one that stores EIGHTEEN is
# publishing four digits of its own rounding, as data. That distinction is what
# should scope the migration -- not "float64 is bad".
_CONSUMERS = ("native_5_strand_baryon", "phase3_deuteron_tritium_h_expansion",
              "rho_k_h3a_gg_trajectory", "tr_m_q_hecke_seminormal")


def _sig_digits(x: float) -> int:
    """Significant digits in the shortest round-tripping repr of ``x``."""
    m = _re.match(r"-?0*(\d+)\.?(\d*)(?:e[-+]?\d+)?$", repr(float(x)))
    if not m:
        return 0
    return len((m.group(1).lstrip("0") + m.group(2)).rstrip("0")) or 1


_NUMERIC_STR = _re.compile(r"^-?\d+\.\d+(?:[eE][-+]?\d+)?$")


def _published_numbers(obj):
    """Every published numeric value, whether stored as a float OR AS A STRING.

    Counting only bare floats is a blind spot, and a consequential one: a
    producer that serializes through `_precision.fmt` emits STRINGS, so a
    float-only walk reports it as carrying no numbers at all and it reads as
    clean. `phase3_deuteron_tritium_h_expansion` is exactly that case --
    "12.7030229395046" is fifteen significant digits stored as text.

    Worse, the raw-float64 ratchet keys on the same representation, so the two
    detectors agree on such a producer BECAUSE THEY SHARE THE BLIND SPOT, not
    because they independently confirm anything. Two detectors agreeing is not
    corroboration when they key on the same thing.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("durationMs", "computedAt"):   # ephemeral, not results
                continue
            yield from _published_numbers(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _published_numbers(v)
    elif isinstance(obj, float):
        yield obj
    elif isinstance(obj, str) and _NUMERIC_STR.match(obj):
        try:
            yield float(obj)
        except ValueError:  # pragma: no cover
            pass


def consumer_census() -> None:
    """Per consumer: how many published floats carry more than 14 digits?"""
    import json
    print("\nWhat the float64-only consumers PUBLISH "
          "(the kernel determines ~14 digits):")
    for w in sorted(_R.rglob("*.witness.json")):
        try:
            body = json.loads(w.read_text())
        except Exception:  # noqa: BLE001
            continue
        if Path(str(body.get("scriptFile") or "")).stem not in _CONSUMERS:
            continue
        vals = list(_published_numbers(body.get("data", body)))
        if not vals:
            print(f"   {w.name:<50} no published numbers")
            continue
        over = sum(1 for v in vals if _sig_digits(v) > 14)
        print(f"   {w.name:<50} n={len(vals):>4}  "
              f"max_digits={max(_sig_digits(v) for v in vals):>2}  "
              f">14 digits: {over} ({100 * over // len(vals)}%)")
    print("   Digits past the 14th are not determined by the computation.")

def main() -> int:
    q_exact = Q_MP
    q_f64 = float(q_exact)
    h_f64 = q_f64 - 1.0 / q_f64
    print(f"mp.dps = {mp.dps}   q = {mp.nstr(q_exact, 20)} (proton pin)\n")

    cache_mp = BlockCacheMP(q_exact)
    cache64 = BlockCache(q_f64, h_f64)

    for (Z, N, label) in ((1, 1, "deuteron A=2"), (2, 1, "helium-3 A=3")):
        word = atom_braid_word_3A(Z, N, include_inter=True)
        # Three strands per nucleon: the word lives at n = 3A, which is why the
        # H6 probes work at lambda |- 6 for the deuteron.
        n = 3 * (Z + N)
        print(f"{label}: |word| = {len(word)}, n = {n}")
        worst = None
        for lam in _two_row_partitions(n, 3 if n <= 6 else 2):
            sig_mp, dim, _ = seminormal_matrices_mp(lam, cache=cache_mp)
            if dim == 0:
                continue
            exact = chi_lambda_of_word_sparse_mp(sig_mp, dim, word, n - 1)
            sig64, dim64 = build_seminormal_matrices_cached(lam, cache=cache64)[:2]
            approx = mp.mpf(chi_lambda_of_word(sig64, dim64, word, n - 1))
            rel = (abs(approx - exact) / abs(exact) if exact != 0
                   else abs(approx - exact))
            print(f"   lambda={lam!s:12s} dim={dim:3d}  "
                  f"exact={mp.nstr(exact, 18):>24s}  rel_gap={mp.nstr(rel, 4)}")
            if worst is None or rel > worst[1]:
                worst = (lam, rel)
        if worst is not None:
            print(f"   WORST: lambda={worst[0]}  rel_gap={mp.nstr(worst[1], 6)}"
                  f"  = {mp.nstr(worst[1] / _ULP, 4)}x the float64 ulp floor"
                  f"  -> ~{int(-mp.log10(worst[1]))} good digits\n")
    print("L1 target is <= 1e-15 (1 ppQ). Every gap above exceeds it, so a "
          "quantity\ncomputed through this kernel cannot meet L1.")
    consumer_census()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
