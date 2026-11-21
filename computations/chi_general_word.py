#!/usr/bin/env python3
"""chi_general_word — `{λ ⊢ n: χ^λ(word)}` for an ARBITRARY braid word.

The fine-Bratteli transfer (`chi_monotone_transfer.chi_all_lambda` and its
accelerator `reduced_block_kernel.chi_all_lambda_reduced_block`) is fast because
it is `d_λ`-free, and it is `d_λ`-free because it assumes the word's generator
sequence is **monotone non-decreasing**: each `O_g` is applied once, acts only on
level `g+1` of the Bratteli chain, and the trace closure therefore factorises
over Bratteli *edges*. Revisit a generator after a higher one and that argument
fails — the level it acts on has already been advanced past.

Both transfer entry points refuse a non-monotone word, and **that refusal is
correct**: composing one through the per-generator `α/β` reduction would give a
silently wrong answer rather than an error. What was missing is a route for the
words that are not monotone. This module is that route.

Why it is needed now (bean `qou-wdij`). Commit `7db032fb48` (2026-09-05, owner
ruling, bean `qou-hu1f`) made `mass_at_3A_proper.atom_braid_word_3A` emit the
INTERLEAVED Borromean intra-nucleon word by default, because the previous
grouped assembly was a different element of `H_3(q)`. That fix is correct. But
interleaving `σ_0` and `σ_1` is exactly what non-monotone means:

    grouped    (1,0)  gens [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]      monotone
    borromean  (1,0)  gens [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]  NOT monotone

so every atom word now refuses, and `tr_m_atom_via_transfer.tr_m_atom_zn` — the
canonical atom trace producer — raised for every atom.

## What this dispatches to, and what that costs

`pyhecke_native.chi_lambda_all_partitions_mpfr` — the general-word Rust mpfr
kernel. It is correct for any word, and it is **not** `d_λ`-free: it builds the
seminormal representation per partition, so its cost grows with `d_λ` exactly as
the transfer was designed to avoid.

Measured on this container (50 dps, canonical `q₀`, atom words):

| A | n | partitions | general-word kernel | monotone transfer |
|---|---|---|---|---|
| 1 | 3 | 3 | < 0.01 s | 0.001 s |
| 2 | 6 | 11 | < 0.01 s | 0.002 s |
| 3 | 9 | 30 | 0.69 s | 0.015 s |

So the dispatcher is cheap where it is currently needed and gets expensive fast.
`_WARN_N` below emits a stderr note rather than silently spending minutes; it
does not refuse, because a slow correct answer beats a fast wrong one and the
caller may genuinely want it.

**This module is a REPAIR, not the destination.** The atom word is not merely
non-monotone — it is *block*-monotone: non-monotone only within each 3-strand
nucleon, while the nucleons themselves are in increasing generator order. A
transfer carrying the three-level window state `(s_{3k}, s_{3k+1}, s_{3k+2})`
instead of a single edge would compose the interleaved intra word and keep the
`O(A)`, `d_λ`-free scaling. That is the real fix and it is real work; tracked as
bean `qou-wdij`.

NO float64: the kernel returns decimal strings, loaded into `mpf`; every
comparison and every returned value is `mpmath` at the requested dps.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from chi_window_transfer import chi_all_lambda_window  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()
# Template-classification tolerance, matching `chi_monotone_transfer`'s.
_TEMPLATE_TOL = mp.mpf("1e-30")

# Above this `n` the general-word kernel is slow enough to be worth saying so.
# n = 12 is ⁴He; n = 9 already costs ~0.7 s against the transfer's 0.015 s.
_WARN_N = 12

_warned: set[int] = set()


def word_is_monotone(word) -> bool:
    """True iff the word's generator sequence is non-decreasing.

    This is the exact precondition of the fine-Bratteli transfer. Checked
    explicitly rather than by catching the transfer's `ValueError`, so a caller
    can branch on the word's shape without provoking an exception — and so a
    genuine `ValueError` from inside the transfer is never mistaken for a
    monotonicity refusal.
    """
    last = -1
    for _c, _d, g in word:
        if g < last:
            return False
        last = g
    return True


def _is_symbolic(q) -> bool:
    return q is not None and not isinstance(q, (int, float, mp.mpf, mp.mpc))


def _encode(word, h):
    """`(c, d, g)` triples -> the kernel's `(sign, g+1)` plus per-position
    `avg_shifts`.

    The kernel takes each crossing as a SIGN (`+1` for `σ`, `-1` for `σ⁻¹`, `0`
    for an averaged/shifted letter) with the shift supplied separately as a
    decimal string. Every atom-word crossing has `c = 1`; only `d`
    distinguishes the templates, so `d` is classified against `0`, `−h` and
    `−h/2` and anything else is carried through as an explicit shift — which is
    what the colour-weighted p–n letter is.

    Encoding validated against the monotone transfer in
    `probes/nonmonotone_atom_trace_kernel_route_probe.py` (max |Δχ| = 6.1e-50 at
    50 dps, i.e. the serialization floor).
    """
    signed, shifts = [], []
    for c, d, g in word:
        cm = c if isinstance(c, mp.mpf) else mp.mpf(str(c))
        if abs(cm - 1) > mp.mpf("1e-9"):
            raise ValueError(
                f"general-word kernel: crossing c={c} at gen={g} is not 1; the "
                "sign encoding cannot represent it")
        dm = d if isinstance(d, mp.mpf) else mp.mpf(str(d))
        g1 = int(g) + 1
        if abs(dm) < _TEMPLATE_TOL:
            signed.append((1, g1))
            shifts.append("")
        elif abs(dm + h) < _TEMPLATE_TOL:
            signed.append((-1, g1))
            shifts.append("")
        elif abs(dm + h / 2) < _TEMPLATE_TOL:
            signed.append((0, g1))
            shifts.append("")
        else:  # colour-weighted p-n letter, or any other explicit shift
            signed.append((0, g1))
            shifts.append(mp.nstr(-dm, 60))
    return signed, shifts


def chi_all_lambda_general(word, n: int, *, dps: int = 50, q=None):
    """`{λ ⊢ n: χ^λ(word)}` for an arbitrary word, via the general-word kernel.

    Correct for monotone and non-monotone words alike; use
    `chi_all_lambda_any` unless you specifically want to bypass the fast path.
    """
    import pyhecke_native as pn

    if mp.mp.dps < dps:
        mp.mp.dps = dps
    if _is_symbolic(q):
        raise ValueError(
            "general-word kernel is numeric only; a symbolic q needs the "
            "monotone transfer, which requires a monotone word")
    qv = mp.mpf(Q_50_DIGIT_STR) if q is None else mp.mpf(str(q))
    q_str = Q_50_DIGIT_STR if q is None else mp.nstr(qv, dps)
    h = qv - 1 / qv

    if n > _WARN_N and n not in _warned:
        _warned.add(n)
        print(
            f"chi_general_word: n={n} on the general-word kernel — this route "
            f"is not d_lambda-free and gets expensive above n={_WARN_N}. "
            "It is correct; it is the O(A) scaling that is lost. See bean "
            "qou-wdij.",
            file=sys.stderr, flush=True)

    signed, shifts = _encode(word, h)
    out = pn.chi_lambda_all_partitions_mpfr(n, signed, q_str, dps, shifts)
    return {tuple(lam): mp.mpf(s) for lam, s in out}


def chi_all_lambda_any(word, n: int, *, dps: int = 50, q=None, fast: bool = True):
    """`{λ ⊢ n: χ^λ(word)}` for ANY word — the transfer when it applies, the
    general-word kernel when it does not.

    `fast=True` (default) uses `reduced_block_kernel`'s O(A) block composition
    on a monotone word; `fast=False` uses the plain `chi_monotone_transfer`
    sweep, which is the same value by a different route and is what the
    cross-checks compare against.

    The dispatch is on the word's own generator sequence, never on a caught
    exception — see `word_is_monotone`.

    **Non-monotone words now take the WINDOW TRANSFER, not the kernel** (bean
    `qou-wdij`). `chi_window_transfer.chi_all_lambda_window` is `d_λ`-free and
    validated against the kernel on the interleaved word at A ≤ 4 (max |Δχ| =
    2.9e-49 at ⁴He) and against the monotone transfer at A = 4/6/7. Measured
    head-to-head at ⁴He: kernel 401.41 s, window 0.42 s — **963×**, and ⁶Li/⁷Li
    (5.0 s / 15.9 s) become reachable at all.

    The kernel remains the fallback, because the window transfer is efficient
    only while the word's live level-window stays bounded; a word that revisits
    a low generator after a high one raises `ValueError` from `MAX_LIVE` rather
    than exhausting memory, and the kernel is correct for any word at all. So
    the fallback is on that *specific* guard, not a bare `except`.

    Monotone words keep the existing transfer, which is **~10× faster than the
    window transfer on them** (0.18 s vs 1.82 s at ⁷Li) because it needs no
    (init, cur) level pair. That measurement is why this is a dispatch and not a
    replacement.
    """
    if word_is_monotone(word):
        if fast:
            return chi_all_lambda_reduced_block(word, n, dps=dps, q=q)
        return chi_all_lambda(word, n, dps=dps, q=q)
    try:
        return chi_all_lambda_window(word, n, dps=dps, q=q)
    except ValueError as exc:
        if "MAX_LIVE" not in str(exc):
            raise
        print(
            f"chi_general_word: window transfer declined (n={n}: {exc}); "
            "falling back to the general-word kernel, which is correct for any "
            "word but not d_lambda-free.",
            file=sys.stderr, flush=True)
        return chi_all_lambda_general(word, n, dps=dps, q=q)
