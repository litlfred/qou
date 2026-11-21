#!/usr/bin/env python3
"""atom_braid_words.py — Hecke→braid conversion and compositional atom braids.

**Why this module exists.** These four helpers used to live in
`probe_he4_jsj_topology.py`. That probe was moved to `_deprecated/probes/`
because its `main()` needs SnapPy, but the helpers themselves are pure
braid-word construction with no SnapPy dependency — and **two live producers
still import them**:

    computations/delta_lambda_jsj_phase3.py       load_atom_braids()
    computations/delta_lambda_alexander_phase4.py load_atom_braids()

`_path_bridge` deliberately skips `_deprecated/`, so those imports raised
`ImportError` at call time from the moment the probe was deprecated. Both
producers were dead on their braid-loading path. This module is the live home
that the deprecation should have created — AGENTS.md, "Move wiring and script
together: when relocating a hook-backed script or a queue, repoint every
reference (docs, hooks, readers) in the same change."

**Extracted verbatim.** The bodies below are byte-for-byte the deprecated
originals apart from imports and docstrings; no convention was changed while
moving them. The deprecated probe keeps its own copies — it is frozen history
and `_path_bridge` cannot reach out of `_deprecated/` to import from here — so
the two definitions are intentionally duplicated. **This module is the live
one**; a change to a convention must land here, and the deprecated copy carries
a pointer saying so.

Read-only: defines helpers, writes no witness, runs no producer.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402 — substrate modules live in substrate/

from q_parameter import HA as H_VAL  # noqa: E402  canonical h = q − q⁻¹ at q_0


def hecke_word_to_braid_word(word: list) -> list[int]:
    """Convert Hecke (c, d, gen) word → braid-group integer word.

    Conventions:
      (1, 0, g):     σ_{g+1}     → +(g+1)
      (1, -h, g):    σ_{g+1}⁻¹  → -(g+1)
      (1, -h/2, g):  averaged   → σ_{g+1} (treat as positive)
                                   per F1 convention

    Returns: list of signed integers (1-indexed braid generators).
    Convention: SnapPy braid_closure uses 1-indexed positive σ_i and
    negative σ_i⁻¹.
    """
    out = []
    for c, d, g in word:
        gen_1indexed = g + 1
        if abs(c - 1) > 1e-12:
            raise ValueError(f"unsupported c = {c}")
        if abs(d) < 1e-12:
            out.append(gen_1indexed)  # σ
        elif abs(d + H_VAL) < 0.01:
            out.append(-gen_1indexed)  # σ⁻¹
        elif abs(d + H_VAL / 2) < 0.01:
            # averaged — convert to σ (positive) per F1 convention
            out.append(gen_1indexed)
        else:
            raise ValueError(f"unsupported d = {d}")
    return out


def _proton_braid_word() -> list[int]:
    """Proton's intra-nucleon braid word as integer braid (1-indexed)."""
    from sublemma_2_1_h9_tritium_verify import _proton_body
    return hecke_word_to_braid_word(_proton_body())


def _neutron_braid_word() -> list[int]:
    from sublemma_2_1_h9_tritium_verify import _neutron_body
    return hecke_word_to_braid_word(_neutron_body())


def shift_word(word: list[int], k: int) -> list[int]:
    """Move a signed braid word ``k`` strands to the right.

    Letters are SIGNED (``-g`` is σ_g⁻¹, the convention of
    ``hecke_word_to_braid_word`` above), so the shift acts on the absolute
    value and keeps the sign: σ_g^{±1} ↦ σ_{g+k}^{±1}.  The bare ``g + k``
    this replaces sent σ_2⁻¹ = -2 to +1 = σ_1 under k = 3 instead of to
    -5 = σ_5⁻¹ (bean qou-yaqm).
    """
    return [g + k if g > 0 else g - k for g in word]


def he4_compositional_braids() -> dict[str, tuple[list[int], int]]:
    """Three compositional ⁴He braid words (1-indexed, n_strands=12).

    Returns: {name: (braid_word, n_strands)}.
    For F1 disjoint composition: just concatenate with strand shift.
    """
    p = _proton_braid_word()
    n = _neutron_braid_word()

    # canonical pppnnn ⁴He at H_12: p · I_pp · p · I_pn · n · I_nn · n
    # I_pp = σ_3 (c=1, d=0 at strand 2 0-indexed = strand 3 1-indexed)
    # I_pn = σ_6 (averaged → +σ)
    # I_nn = σ_9 (c=1, d=-h at strand 8 0-indexed = strand 9 1-indexed)
    canonical = (
        list(p)
        + [3]                                       # I_pp = σ_3
        + shift_word(p, 3)                       # p₂ on strands 4-6
        + [6]                                       # I_pn averaged → σ_6
        + shift_word(n, 6)                       # n₁ on strands 7-9
        + [-9]                                      # I_nn = σ_9⁻¹
        + shift_word(n, 9)                       # n₂ on strands 10-12
    )

    # D⊕D disjoint: β_D = p · I_pn · n on H_6, two copies on disjoint strands
    # First D on strands 1-6 (gens 1..5), Second D on strands 7-12 (gens 7..11)
    deuteron = list(p) + [3] + shift_word(n, 3)  # canonical D
    D_disjoint = list(deuteron) + shift_word(deuteron, 6)

    # T⊕p: T on strands 1-9, p on strands 10-12
    tritium = list(p) + [3] + shift_word(n, 3) + [-6] + shift_word(n, 6)
    T_p_disjoint = list(tritium) + shift_word(p, 9)

    # ³He⊕n: ³He on strands 1-9, n on strands 10-12
    he3 = list(p) + [3] + shift_word(p, 3) + [6] + shift_word(n, 6)
    He3_n_disjoint = list(he3) + shift_word(n, 9)

    return {
        "canonical_pppnnn": (canonical, 12),
        "D_oplus_D":         (D_disjoint, 12),
        "T_oplus_p":         (T_p_disjoint, 12),
        "He3_oplus_n":       (He3_n_disjoint, 12),
    }


def _self_test() -> int:
    """Verify the helpers resolve and produce the documented shapes."""
    fails = 0

    def chk(name: str, ok: bool) -> None:
        nonlocal fails
        if not ok:
            fails += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")

    p, n = _proton_braid_word(), _neutron_braid_word()
    chk("proton braid word is non-empty", len(p) > 0)
    chk("neutron braid word is non-empty", len(n) > 0)
    chk("both are 1-indexed (no zero generator)",
        all(g != 0 for g in p + n))

    br = he4_compositional_braids()
    chk("four compositional ⁴He braids", len(br) == 4)
    for name, (word, ns) in br.items():
        chk(f"{name}: n_strands = 12", ns == 12)
        chk(f"{name}: generators within 1..11",
            all(1 <= abs(g) <= 11 for g in word))

    canon = br["canonical_pppnnn"][0]
    chk("canonical contains I_pp = +3, I_pn = +6, I_nn = -9",
        3 in canon and 6 in canon and -9 in canon)

    # the two producers' own D / T / ³He constructions, reproduced here
    D = list(p) + [3] + shift_word(n, 3)
    chk("deuteron word length = 2·|p| + 1", len(D) == len(p) + len(n) + 1)

    # qou-yaqm: the strand shift must keep each letter's sign.  The proton
    # word carries inverse letters, so a sign-dropping shift changes the
    # count of inverse letters and leaves the top strand untouched.
    neg = lambda w: sum(1 for g in w if g < 0)  # noqa: E731
    chk("shift_word keeps signs: σ_2⁻¹ shifted by 3 is σ_5⁻¹",
        shift_word([-2, 1], 3) == [-5, 4])
    chk("shifted words keep their count of inverse letters",
        all(neg(shift_word(w, k)) == neg(w) for w in (p, n) for k in (3, 6, 9)))
    chk("deuteron word reaches strand 6 (σ_5^{±1} present)",
        max(abs(g) for g in D) == 5)
    chk("canonical ⁴He word reaches strand 12 (σ_11^{±1} present)",
        max(abs(g) for g in canon) == 11)

    print(f"\n{'PASS' if not fails else 'FAIL'} — {fails} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(_self_test())
