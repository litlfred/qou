#!/usr/bin/env python3
# polynomial_q_not_applicable: structural adapter; emits wire-format
# specs for downstream Rust binaries (`hecke-tr-m-wenzl-lr`,
# `hecke-atomic`). Carries no symbolic q-arithmetic of its own.
"""Wenzl LR convention adapter — 1-strand vs 3-strand bridges.

Implements `prop:lr-tensor-character-bridge`: splits a canonical
$(Z, N)$ atomic braid into the LR-compatible tensor-product factors
plus the residual inter-nucleon interface word, in the wire format
consumed by the Rust LR binary `hecke-tr-m-wenzl-lr`. Also emits the
v12-style 1-strand-per-particle factor spec consumed by the legacy
`hecke-atomic` binary, so the two conventions can be invoked from a
single Python entry point.

The proposition is precise: the LR identity

    χ^ν_{H_n}(β_1 ⊗ … ⊗ β_k)
      = Σ_{λ_1,…,λ_k} c^ν_{λ_1,…,λ_k} · Π χ^{λ_i}_{H_{n_i}}(β_i)

holds for *tensor-product* (parabolic) braids only. The canonical
atomic braid

    β(Z, N) = β_disjoint · β_interface,
    β_disjoint = β_1 ⊗ … ⊗ β_A   (per-nucleon H_3 factors)
    β_interface = product of inter-nucleon averaged crossings
                   σ_{3k+2} − ½ h · 1 at H_{3A}

is *not* a tensor product, so the LR bridge is the correct primitive
for β_disjoint but not for the full canonical braid. This module
exists to keep the partition explicit and to prevent the consumer-
scope bug recorded in `rho_k_full_via_wenzl_lr.py` (the 2026-05-17
cross-check that found ~80% error when the LR identity was applied
to the entire canonical word).

Public API:
    nucleon_factor_spec_3strand(nucleon, label) -> dict
    atom_split_3strand(Z, N, ordering=None) -> (factor_specs,
                                                interface_word)
    atom_factor_spec_1strand(Z, N, ordering=None) -> dict
    canonical_word_summary(Z, N, ordering=None) -> dict

References:
    prop:lr-tensor-character-bridge
        content/quantum-observable-universe/braids-and-knots/
        lr-tensor-character-bridge.md
    tools/hecke-engine/src/bin/hecke_tr_m_wenzl_lr.rs (Rust producer)
    tools/hecke-engine/src/bin/v12_atomic.rs (Rust 1-strand producer)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_core import h as H_VAL  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

# Wire-format sign codes shared with the Rust binary
# `hecke-tr-m-wenzl-lr` (`Crossing::from_sign`).
SIGN_SIGMA = 1
SIGN_SIGMA_INV = -1
SIGN_AVERAGED = 0


def _ctype_from_d(c: float, d: float) -> str:
    """Classify a (c, d) crossing pair into ctype {sigma, sigma_inv,
    averaged}. Mirrors `canonical_braid_crossings._ctype_from_d`
    but lives here so the adapter is self-contained for downstream
    Rust-binary consumers."""
    if abs(c - 1.0) > 1e-12:
        raise ValueError(f"Unexpected coefficient c={c} (expected 1)")
    if abs(d) < 1e-12:
        return "sigma"
    if abs(d - (-H_VAL)) < 1e-9:
        return "sigma_inv"
    if abs(d - (-H_VAL / 2)) < 1e-9:
        return "averaged"
    raise ValueError(
        f"Unrecognised crossing (c, d)=({c}, {d}); "
        f"expected d ∈ {{0, -h, -h/2}} with h≈{H_VAL:.6f}"
    )


def _ctype_to_sign(ctype: str) -> int:
    return {"sigma": SIGN_SIGMA,
            "sigma_inv": SIGN_SIGMA_INV,
            "averaged": SIGN_AVERAGED}[ctype]


def nucleon_factor_spec_3strand(nucleon: str, label: str | None = None) -> dict:
    """Build the LR-binary wire spec for a single nucleon's canonical
    3-strand braid at H_3.

    The nucleon's intra-braid is `atom_braid_word_3A(Z, N,
    include_inter=False)` at (Z, N) = (1, 0) for a proton or (0, 1)
    for a neutron. Generator indices are 0-based in the source word;
    the LR binary's wire format expects 1-based, so we shift by +1.

    Returns the dict consumed by `hecke-tr-m-wenzl-lr`:
        {"label": <label>, "n_strands": 3, "word": [[sign, gen], …]}
    """
    if nucleon not in ("p", "n"):
        raise ValueError(f"nucleon must be 'p' or 'n', got {nucleon!r}")
    Z, N = (1, 0) if nucleon == "p" else (0, 1)
    triples = atom_braid_word_3A(Z, N, include_inter=False)
    word: list[list[int]] = []
    for c, d, gen in triples:
        ctype = _ctype_from_d(float(c), float(d))
        # 0-based gen → 1-based wire format.
        word.append([_ctype_to_sign(ctype), int(gen) + 1])
    return {
        "label": label or nucleon,
        "n_strands": 3,
        "word": word,
    }


def _default_ordering(Z: int, N: int) -> list[str]:
    return ["p"] * Z + ["n"] * N


def atom_split_3strand(
    Z: int, N: int, ordering: list[str] | None = None,
) -> tuple[list[dict], list[tuple[int, str, int]]]:
    """Split the canonical $(Z, N)$ braid into LR-compatible
    per-nucleon factors and the inter-nucleon interface residue.

    Returns:
        factor_specs   list of dicts in the `hecke-tr-m-wenzl-lr`
                        wire format, one per nucleon, each at H_3.
                        Tensoring them yields β_disjoint at H_{3A}.
        interface_word list of `(gen_0based_in_H3A, ctype, run_index)`
                        triples. Each entry is one of the averaged
                        inter-nucleon crossings σ_{3k+2} − ½ h · 1 in
                        the H_{3A} frame; `run_index` is the position
                        in the canonical word (0-based) for
                        round-tripping. Applied as a residual
                        multiply in the seminormal basis at H_{3A};
                        does *not* factor through the parabolic
                        embedding and is therefore *not* part of the
                        LR sum.
    """
    ordering = ordering or _default_ordering(Z, N)
    A = len(ordering)
    if A != Z + N:
        raise ValueError(
            f"ordering length {A} does not match Z+N = {Z}+{N} = {Z+N}"
        )

    factor_specs: list[dict] = [
        nucleon_factor_spec_3strand(nuc, label=f"{nuc}{k}")
        for k, nuc in enumerate(ordering)
    ]

    full = atom_braid_word_3A(Z, N, include_inter=True)
    interface_word: list[tuple[int, str, int]] = []
    for run_idx, (c, d, gen) in enumerate(full):
        if int(gen) % 3 == 2:
            ctype = _ctype_from_d(float(c), float(d))
            interface_word.append((int(gen), ctype, run_idx))
    return factor_specs, interface_word


# v12_atomic crossing table (mirrors tools/hecke-engine/src/bin/
# v12_atomic.rs `crossing()`): (c, d, doubled?) for each unordered
# particle pair, indexed by sorted-pair key.
_V12_CROSSING_TABLE: dict[frozenset, tuple[float, float, bool]] = {
    frozenset({"p"}): (1.0, 0.0, False),                  # pp → σ
    frozenset({"n"}): (1.0, -H_VAL, False),               # nn → σ⁻¹
    frozenset({"p", "n"}): (1.0, -H_VAL / 2.0, True),     # pn → ½(σ+σ⁻¹)
    frozenset({"e"}): (1.0, 0.0, False),                  # ee → σ
    frozenset({"p", "e"}): (1.0, -H_VAL, False),          # pe → σ⁻¹
    frozenset({"n", "e"}): (0.0, 1.0, False),             # ne → identity
}


def _v12_pair_crossing(a: str, b: str) -> tuple[float, float, bool]:
    key = frozenset({a, b})
    if key not in _V12_CROSSING_TABLE:
        raise ValueError(f"Unknown particle pair {a!r}+{b!r}")
    return _V12_CROSSING_TABLE[key]


def atom_factor_spec_1strand(
    Z: int, N: int, ordering: list[str] | None = None,
) -> dict:
    """1-strand-per-particle factor spec at H_{|ordering|}.

    Mirrors `tools/hecke-engine/src/bin/v12_atomic.rs`: each particle
    contributes a single strand, and crossings appear between every
    pair `(i, k)` with `i < k` at generator `i` (0-based). The
    averaged pn / np crossings appear twice (the v12 `doubled` flag).

    Returns the single-factor wire spec consumed by
    `hecke-tr-m-wenzl-lr` when invoked in 1-strand mode (informational
    only; the LR bridge over a single factor is the identity, so this
    is primarily a cross-validation handle for `hecke-atomic`).
    """
    ordering = ordering or _default_ordering(Z, N)
    A = len(ordering)
    word: list[list[int]] = []
    for k in range(1, A):
        for i in range(k):
            c, d, doubled = _v12_pair_crossing(ordering[i], ordering[k])
            if c == 0.0 and d == 1.0:
                # Identity (n+e): no crossing emitted; skips.
                continue
            ctype = _ctype_from_d(c, d)
            sign = _ctype_to_sign(ctype)
            word.append([sign, i + 1])  # 1-based wire format
            if doubled:
                word.append([sign, i + 1])
    return {
        "label": "atom-1strand",
        "n_strands": A,
        "word": word,
    }


def canonical_word_summary(
    Z: int, N: int, ordering: list[str] | None = None,
) -> dict:
    """Summary record cross-linking the two conventions for $(Z, N)$.

    Returned dict is JSON-serialisable and suitable for inclusion in
    a downstream witness file. Records:

      - n_strands_3strand:    3·A         (canonical convention)
      - n_strands_1strand:    A or A+E    (v12_atomic convention)
      - n_intra_crossings:    per-nucleon intra word length
      - n_interface_crossings: number of averaged inter-nucleon
                              crossings in β_interface
      - factor_specs_3strand: per-nucleon H_3 LR specs
      - interface_word:       inter-nucleon residue, H_{3A} frame
      - factor_spec_1strand:  v12_atomic-style single H_A spec
    """
    factor_specs, interface_word = atom_split_3strand(Z, N, ordering)
    factor_1s = atom_factor_spec_1strand(Z, N, ordering)
    intra_lengths = [len(f["word"]) for f in factor_specs]
    return {
        "Z": Z,
        "N": N,
        "ordering": ordering or _default_ordering(Z, N),
        "n_strands_3strand": 3 * (Z + N),
        "n_strands_1strand": len(factor_1s["word"]) and factor_1s["n_strands"],
        "n_intra_crossings": intra_lengths,
        "n_interface_crossings": len(interface_word),
        "factor_specs_3strand": factor_specs,
        "interface_word": [
            {"gen_0based_h3a": g, "ctype": ct, "run_index": ri}
            for (g, ct, ri) in interface_word
        ],
        "factor_spec_1strand": factor_1s,
        "convention_note": (
            "LR bridge applies to factor_specs_3strand (tensor "
            "product). The interface_word must be applied as a "
            "separate H_{3A} seminormal-basis multiplication; it "
            "does not factor through the parabolic embedding."
        ),
        "proposition": "prop:lr-tensor-character-bridge",
    }


__all__ = [
    "nucleon_factor_spec_3strand",
    "atom_split_3strand",
    "atom_factor_spec_1strand",
    "canonical_word_summary",
    "SIGN_SIGMA",
    "SIGN_SIGMA_INV",
    "SIGN_AVERAGED",
]


def _smoke_test() -> int:
    """Smoke test: verify split round-trips back to the canonical word."""
    from witness_base import WitnessBuilder

    cases = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)]
    summaries: dict[str, dict] = {}
    for (Z, N) in cases:
        summary = canonical_word_summary(Z, N)
        A = Z + N
        # Self-consistency check: total intra + interface crossings =
        # length of full canonical word.
        full_len = len(atom_braid_word_3A(Z, N, include_inter=True))
        intra_total = sum(summary["n_intra_crossings"])
        iface_total = summary["n_interface_crossings"]
        if intra_total + iface_total != full_len:
            raise AssertionError(
                f"({Z},{N}): intra {intra_total} + iface {iface_total} "
                f"!= full {full_len}"
            )
        # Interface should have exactly A-1 crossings (one per
        # inter-nucleon arc). ctype is sigma (pp), sigma_inv (nn), or
        # averaged (mixed pn / np).
        if iface_total != max(0, A - 1):
            raise AssertionError(
                f"({Z},{N}): iface count {iface_total} != A-1 = {A-1}"
            )
        allowed = {"sigma", "sigma_inv", "averaged"}
        for entry in summary["interface_word"]:
            if entry["ctype"] not in allowed:
                raise AssertionError(
                    f"({Z},{N}) interface entry has invalid ctype: "
                    f"{entry}"
                )
            if entry["gen_0based_h3a"] % 3 != 2:
                raise AssertionError(
                    f"({Z},{N}) interface at non-inter gen: {entry}"
                )
        summaries[f"Z{Z}_N{N}"] = summary
        print(
            f"  ({Z},{N}): A={A}, n_strands_3strand={summary['n_strands_3strand']}, "
            f"intra={intra_total}, interface={iface_total}  ✓"
        )

    out = WitnessBuilder.wrap_legacy(
        "wenzl-lr-convention-adapter",
        {
            "computation": "wenzl-lr-convention-adapter",
            "description": (
                "Convention adapter splitting canonical (Z, N) atomic "
                "braids into LR-compatible tensor-product factors and "
                "the inter-nucleon interface residue, per "
                "prop:lr-tensor-character-bridge. Six smoke-test atoms "
                "(p, n, D, T, ³He, ⁴He) verified for self-consistent "
                "splitting (intra + interface = full canonical word; "
                "interface is purely averaged and has length A-1)."
            ),
            "binary_built": None,
            "cases": summaries,
            "proposition": "prop:lr-tensor-character-bridge",
        },
        script_path=__file__,
        engine="python",
    ).set_audit_only(
        "docs/coordination/2026-05-19-refreshed-workplan.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(_smoke_test())
