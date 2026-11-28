"""Subprocess bridge to `crates/gs-basis` (`gs-peel` binary).

Provides zero-float64 exact dyadic Laurent (`Z[1/2][q, q^{-1}]`) normal-form walks,
Temperley-Lieb loop-closure trace walks, homogeneous Annex-B Markov tower peeling,
and monotone two-row Bratteli character sweeps backed by `crates/gs-basis`.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any

_FAST_COPRIME_FRACTION = getattr(Fraction, "_from_coprime_ints", None)


def decode_dyadic_term(mantissa_str: str, exp2: int) -> Fraction:
    """Convert `(odd_mantissa_decimal, exp2)` into an exact `Fraction` with zero `math.gcd`."""
    mant = int(mantissa_str)
    if mant == 0:
        return Fraction(0)
    if exp2 >= 0:
        num = mant << exp2
        return _FAST_COPRIME_FRACTION(num, 1) if _FAST_COPRIME_FRACTION is not None else Fraction(num, 1)
    den = 1 << (-exp2)
    return _FAST_COPRIME_FRACTION(mant, den) if _FAST_COPRIME_FRACTION is not None else Fraction(mant, den)


def decode_dyadic_laurent(raw_terms: list[list[Any] | tuple[Any, ...]]) -> dict[int, Fraction]:
    """Decode `[[q_exp, odd_mantissa_str, exp2], ...]` into `{q_exp: Fraction}`."""
    return {int(exp): decode_dyadic_term(str(m_str), int(e2)) for exp, m_str, e2 in raw_terms}


def gs_peel_binary_path() -> Path | None:
    """Locate compiled `gs-peel` release binary following workspace `CARGO_TARGET_DIR` order."""
    explicit = os.environ.get("GS_PEEL_BIN")
    if explicit:
        p = Path(explicit)
        if p.is_file() and os.access(p, os.X_OK):
            return p

    candidates: list[Path] = []
    cargo_target = os.environ.get("CARGO_TARGET_DIR")
    if cargo_target:
        candidates.append(Path(cargo_target) / "release" / "gs-peel")
    candidates.append(Path("/tmp/qou-shared-cargo-target/release/gs-peel"))

    here = Path(__file__).resolve()
    for anc in here.parents:
        if (anc / "crates" / "gs-basis" / "Cargo.toml").is_file():
            candidates.append(anc / "target" / "release" / "gs-peel")
            candidates.append(anc / "crates" / "gs-basis" / "target" / "release" / "gs-peel")
            break

    for cand in candidates:
        if cand.is_file() and os.access(cand, os.X_OK):
            return cand

    which = shutil.which("gs-peel")
    return Path(which) if which else None


def invoke_gs_peel(payload: dict[str, Any], timeout: int | None = None) -> dict[str, Any]:
    """Send a JSON request to `gs-peel` over stdin and parse its JSON stdout."""
    bin_path = gs_peel_binary_path()
    if bin_path is None:
        raise FileNotFoundError(
            "gs-peel binary not found. Build with: "
            "CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target cargo build --release -p gs-basis --bin gs-peel"
        )
    proc = subprocess.run(
        [str(bin_path)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gs-peel failed ({proc.returncode}): {proc.stderr[:500]}")
    return json.loads(proc.stdout)


def eval_dyadic_laurent_mpmath(raw_terms: list[list[Any] | tuple[Any, ...]], q_mp: Any) -> Any:
    """Evaluate `[[q_exp, odd_mantissa_str, exp2], ...]` at an `mpmath.mpf` `q_mp` at full `mp.dps`."""
    import mpmath as mp

    if not raw_terms:
        return mp.mpf(0)
    terms_out = []
    for exp_raw, m_str, e2_raw in raw_terms:
        exp = int(exp_raw)
        e2 = int(e2_raw)
        coeff = mp.ldexp(mp.mpf(int(m_str)), e2)
        terms_out.append(coeff * (q_mp ** exp))
    return mp.fsum(terms_out)
