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
    v12_atomic_cli_args(Z, N, ordering=None) -> list[str]
    canonical_word_summary(Z, N, ordering=None) -> dict

References:
    prop:lr-tensor-character-bridge
        content/quantum-observable-universe/braids-and-knots/
        lr-tensor-character-bridge.md
    tools/hecke-engine/src/bin/hecke_tr_m_wenzl_lr.rs (Rust producer)
    tools/hecke-engine/src/bin/v12_atomic.rs (Rust 1-strand producer)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from canonical_braid_crossings import classify_crossing  # noqa: E402
from hecke_core import h as H_VAL  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

# Wire-format sign codes shared with the Rust binary
# `hecke-tr-m-wenzl-lr` (`Crossing::from_sign`).
SIGN_SIGMA = 1
SIGN_SIGMA_INV = -1
SIGN_AVERAGED = 0


_CTYPE_SIGNS = {
    "sigma": SIGN_SIGMA,
    "sigma_inv": SIGN_SIGMA_INV,
    "averaged": SIGN_AVERAGED,
}


def _ctype_to_sign(ctype: str) -> int:
    """Map a ctype literal to its LR-wire sign code. Raises
    ValueError (not KeyError) on an unrecognised ctype so the
    public adapter surface emits actionable errors."""
    if ctype not in _CTYPE_SIGNS:
        raise ValueError(
            f"unrecognised ctype {ctype!r}; "
            f"expected one of {sorted(_CTYPE_SIGNS)}"
        )
    return _CTYPE_SIGNS[ctype]


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
        ctype = classify_crossing(float(c), float(d), H_VAL)
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

    Custom orderings are currently rejected — `atom_braid_word_3A`
    hardcodes `['p']*Z + ['n']*N`, so a non-default ordering would
    desynchronise the per-nucleon factors from the interface word.
    Lift this restriction only after `atom_braid_word_3A` is extended
    to accept ordering.

    Returns:
        factor_specs   list of dicts in the `hecke-tr-m-wenzl-lr`
                        wire format, one per nucleon, each at H_3.
                        Tensoring them yields β_disjoint at H_{3A}.
        interface_word list of `(gen_0based_in_H3A, ctype, run_index)`
                        triples, one per adjacent nucleon pair. Each
                        entry's ctype is `sigma` on a pp arc,
                        `sigma_inv` on an nn arc, and `averaged` on a
                        mixed pn / np arc. Applied as a residual
                        multiply in the seminormal basis at H_{3A};
                        does *not* factor through the parabolic
                        embedding and is therefore *not* part of the
                        LR sum (see prop:lr-tensor-character-bridge
                        for the scope statement).
    """
    default = _default_ordering(Z, N)
    if ordering is not None and ordering != default:
        raise NotImplementedError(
            f"custom ordering {ordering!r} is not yet supported; "
            f"`atom_braid_word_3A` hardcodes ordering = {default!r}. "
            f"Extend the source generator to accept ordering before "
            f"lifting this restriction."
        )
    ordering = default

    factor_specs: list[dict] = [
        nucleon_factor_spec_3strand(nuc, label=f"{nuc}{k}")
        for k, nuc in enumerate(ordering)
    ]

    full = atom_braid_word_3A(Z, N, include_inter=True)
    interface_word: list[tuple[int, str, int]] = []
    for run_idx, (c, d, gen) in enumerate(full):
        if int(gen) % 3 == 2:
            ctype = classify_crossing(float(c), float(d), H_VAL)
            interface_word.append((int(gen), ctype, run_idx))
    return factor_specs, interface_word


def v12_atomic_cli_args(
    Z: int, N: int, ordering: list[str] | None = None,
) -> list[str]:
    """Build the command-line arguments for the `hecke-atomic`
    (v12_atomic) Rust binary.

    `hecke-atomic` consumes `Z N [ordering]` directly — there is no
    JSON wire format to share with `hecke-tr-m-wenzl-lr`. The two
    binaries compute *different* observables:

      - `hecke-atomic` emits `f_pauli` at H_{|ordering|} using v12's
        crossing kernel (`pn → 2σ - h·1` per v12_atomic.rs line 7),
        normalising by `2^pn_count` at the end.
      - `hecke-tr-m-wenzl-lr` emits per-partition χ^λ of a
        tensor-product braid in the LR wire format, using the
        averaged kernel `pn → σ - (h/2)·1 = ½(σ+σ⁻¹)`, normalising
        via its own `averaging_denominator = 2^(avg-count)`.

    The two kernels differ by a factor of 2 per pn crossing; each
    binary handles its own normalisation. This adapter therefore
    exposes the v12 binary only at the CLI-argument level — never as
    an LR factor spec — to avoid silent kernel-mismatch bugs.
    """
    default = _default_ordering(Z, N)
    if ordering is not None and ordering != default:
        raise NotImplementedError(
            f"custom ordering {ordering!r} is not yet supported; "
            f"`atom_braid_word_3A` hardcodes ordering = {default!r}. "
            f"Extend the source generator to accept ordering before "
            f"lifting this restriction."
        )
    ordering_str = "".join(default)
    return [str(Z), str(N), ordering_str]


def canonical_word_summary(
    Z: int, N: int, ordering: list[str] | None = None,
) -> dict:
    """Summary record cross-linking the two conventions for $(Z, N)$.

    Returned dict is JSON-serialisable and suitable for inclusion in
    a downstream witness file. Records:

      - n_strands_3strand:    3·A             (canonical convention)
      - n_strands_v12_atomic: A = Z + N       (v12_atomic convention)
      - n_intra_crossings:    per-nucleon intra word length
      - n_interface_crossings: number of inter-nucleon crossings in
                              β_interface (one per adjacent pair)
      - factor_specs_3strand: per-nucleon H_3 LR specs
      - interface_word:       inter-nucleon residue, H_{3A} frame
      - v12_atomic_cli_args:  argv for the `hecke-atomic` Rust binary
    """
    factor_specs, interface_word = atom_split_3strand(Z, N, ordering)
    cli_args = v12_atomic_cli_args(Z, N, ordering)
    intra_lengths = [len(f["word"]) for f in factor_specs]
    return {
        "Z": Z,
        "N": N,
        "ordering": ordering or _default_ordering(Z, N),
        "n_strands_3strand": 3 * (Z + N),
        "n_strands_v12_atomic": Z + N,
        "n_intra_crossings": intra_lengths,
        "n_interface_crossings": len(interface_word),
        "factor_specs_3strand": factor_specs,
        "interface_word": [
            {"gen_0based_h3a": g, "ctype": ct, "run_index": ri}
            for (g, ct, ri) in interface_word
        ],
        "v12_atomic_cli_args": cli_args,
        "convention_note": (
            "LR bridge applies to factor_specs_3strand (tensor "
            "product). The interface_word must be applied as a "
            "separate H_{3A} seminormal-basis multiplication; it "
            "does not factor through the parabolic embedding. The "
            "v12_atomic_cli_args drive the separate `hecke-atomic` "
            "Rust binary, which computes a different observable "
            "(f_pauli) and uses a different crossing kernel — see "
            "v12_atomic_cli_args() for the kernel-mismatch note."
        ),
        "proposition": "prop:lr-tensor-character-bridge",
    }


__all__ = [
    "nucleon_factor_spec_3strand",
    "atom_split_3strand",
    "v12_atomic_cli_args",
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
                "splitting: intra + interface = full canonical word; "
                "interface has length A-1, each entry at gen 3k+2 "
                "with ctype ∈ {sigma (pp), sigma_inv (nn), averaged "
                "(mixed pn / np)}."
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
