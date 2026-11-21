#!/usr/bin/env python3
"""
canonical_braid_crossings.py — bridge `atom_braid_word_3A` →
`(gen_idx, ctype)` format for `chi_lambda_symbolic` consumers.

Generalises the `deuteron_canonical_crossings` helper from PR #564's
`rho_k_h3a_refinement.py` to arbitrary `(Z, N)`.  Replaces all
calls to the **legacy** `hecke_character_symbolic.atomic_braid_to_crossings`
(which uses a non-canonical disjoint-product convention; per the
P3' canonical word fix on PR #564 commit c068550c, the canonical
convention is `mass_at_3A_proper.atom_braid_word_3A` with the
operator-valued interface `I = σ_{n_1} − h/2 · 1`).

The conversion classifies each `(c, d, gen_idx)` triple by `d`:

    d = 0        →  ctype = "sigma"     (positive crossing σ_g)
    d = −h       →  ctype = "sigma_inv" (negative crossing σ_g⁻¹;
                                         from σ² = h·σ + 1 ⇒ σ⁻¹ = σ − h)
    d = −h/2     →  ctype = "averaged"  (interface σ_g − h/2 · 1)

All three are the canonical Hecke-algebra building blocks consumed
by `hoefsmit_symbolic.chi_lambda_symbolic` and
`hecke_character_symbolic.q_character_on_braid_word`.

References:
- PR #546 (`hoefsmit_symbolic.py`) — closed-form symbolic χ^λ
- PR #564 commit c068550c — canonical-word fix on rho_k_h3a_refinement.py
- prop:hecke-branching-trace-decomposition (operator-valued interface)
- prop:q-hecke-seminormal-character-closure (this PR's closure)

@module computations/canonical_braid_crossings
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


_AVG_COLOR_DELTA = None  # cached δ = flavor_split_leading(q₀)


def _avg_color_delta():
    """Substrate flavor split δ = (m_n − m_p)/M_N at q₀ as an **mp.mpf**
    (full precision), for the color-weighted averaged p-n crossing
    `−h·(1/2 − δ/4)`. Lazy + cached; the **single source of δ** for the whole
    braid pipeline (mass_at_3A_proper, chi_lambda_numerical, marshalling).
    Float-context callers wrap with `float()`; mpmath callers use it directly
    so the high-dps paths keep full precision.

    ⚠ q₀-PIN (read before 1ppQ use). δ is evaluated at `q_parameter.Q`, which
    is **anchor-adaptive**: PROTON-pinned by default, but MUON-pinned under
    `QOU_Q0_ANCHOR=ideal` (or when the producer stem is in
    `q0_anchor_manifest.json` `ideal_muon`). So a muon-q₀ compute is correct
    ONLY IF it sets that anchor — otherwise δ silently reverts to proton and a
    color-weighted muon-q₀ trace is off by ~5.86e-11 (fine at scope-(a), WRONG
    at 1ppQ). Two rules: (1) muon-q₀ callers must set `QOU_Q0_ANCHOR=ideal`;
    (2) for **deep**-1ppQ, this accessor only reaches ~5e-16 (it reads the f64
    `q_parameter.Q`, not the 50-dps string) — call
    `flavor_split_leading(local_q0_50dps)` directly (the closed form takes q as
    an argument; = `markov_peel._color_delta`). Do NOT change this default —
    the muon/proton split is owner-gated (AGENTS.md §"q₀ anchor convention";
    bean `tnjb`). Full analysis:
    docs/audits/2026-07-18-avg-color-delta-q0-pin-mismatch.md."""
    global _AVG_COLOR_DELTA
    if _AVG_COLOR_DELTA is None:
        import mpmath as _mp
        # DE-WIRED 2026-06-29: proven leading δ, not posited subleading
        from _li_2_q_util import flavor_split_leading
        # 50-dps source, NOT the float64 `q_parameter.Q`.
        #
        # This read `Q` and laundered it through `mpf(str(...))`, so δ was
        # evaluated at ~17 good digits and this accessor reached only ~5e-16 —
        # the cap the docstring above warns about. With 16 live consumers that
        # was the single widest f64 leak in the braid pipeline: δ enters the
        # colour-weighted crossing as −h·(½ − δ/4), and a 1e-16 error in δ
        # lands at ~7e-20 on a χ result that is otherwise exact to ~1e-50.
        #
        # `flavor_split_leading` takes q as an argument and is exact at
        # whatever precision it is handed, so the fix is to hand it the right
        # thing. Built at >= 60 dps because an mpf keeps the precision it was
        # CREATED at, and this cache is populated on first call — under
        # whatever ambient dps that caller happens to have.
        from q_parameter import Q_50_DIGIT_STR as _Q50
        with _mp.workdps(max(_mp.mp.dps, 60)):
            _AVG_COLOR_DELTA = flavor_split_leading(_mp.mpf(str(_Q50)))
    return _AVG_COLOR_DELTA


def classify_crossing(
    c: float, d: float, h_val: float, *, context: str | None = None,
) -> str:
    """Classify a `(c, d)` Hecke-algebra crossing pair into a ctype
    `{sigma, sigma_inv, averaged}` against the substrate `h = q - q⁻¹`.

    Shared utility for downstream consumers (canonical braid crossings,
    Wenzl LR convention adapter, Rust binary wrappers). Centralises
    the tolerance constants so any future refinement is reflected
    everywhere.

    `context` is an optional string appended to error messages so
    call-site debugging (e.g. "atom (Z, N) = (2, 2) gen 5") survives
    the wrapping. The helper itself does no parsing of the context.
    """
    suffix = f" [{context}]" if context else ""
    if abs(c - 1.0) > 1e-12:
        raise ValueError(
            f"Unexpected coefficient c={c} (expected 1){suffix}"
        )
    if abs(d) < 1e-12:
        return "sigma"
    if abs(d - (-h_val)) < 1e-9:
        return "sigma_inv"
    # "averaged" p-n interface: color-blind −h/2, OR color-weighted
    # −h·(1/2 − δ/4) (bring_color_weighted default, mass_at_3A_proper).
    delta = float(_avg_color_delta())                # float-context comparison
    if abs(d - (-h_val / 2.0)) < 1e-9:
        return "averaged"
    if abs(d - (-h_val * (0.5 - delta / 4.0))) < 1e-9:
        # DISTINCT from "averaged". Both used to return it, and every consumer
        # maps that label to -h/2, so the colour-weighted p-n interface was
        # silently replaced by the colour-blind one: 6.879e-4 on the crossing,
        # 7e-5..3.9e-4 per chi^lambda, and the whole residual Schur-Weyl
        # failure in rho_k_h3a_refinement after the convention-D migration.
        # This is the proton-neutron colour asymmetry (bring_color_weighted);
        # collapsing it into "averaged" de-asymmetrises the nucleus.
        return "averaged_weighted"
    raise ValueError(
        f"Unrecognised crossing (c, d)=({c}, {d}); expected d ∈ "
        f"{{0, -h, -h/2, -h·(1/2-δ/4)}} with h≈{h_val:.6f}, "
        f"δ≈{delta:.6e}{suffix}"
    )


def atom_canonical_crossings(
    Z: int, N: int,
    *,
    include_inter: bool = True,
    m_pp: int = 1, m_pn: int = 1, m_nn: int = 1,
    intra_order: str = "borromean",
    ordering: list | None = None,
) -> list[tuple[int, str]]:
    """Canonical (gen_idx, ctype) crossings for atomic braid β(Z, N).

    Source of truth: `mass_at_3A_proper.atom_braid_word_3A(Z, N)`.

    Returns a list of `(gen_idx, ctype)` pairs consumable by
    `hoefsmit_symbolic.chi_lambda_symbolic` and
    `hecke_character_symbolic.q_character_on_braid_word`.

    Replaces the legacy `hecke_character_symbolic.atomic_braid_to_crossings`,
    which used a disjoint-product convention not matching the
    canonical Markov-axiom reducer.

    `intra_order` is forwarded verbatim; see `atom_braid_word_3A`. Since
    2026-09-05 the default is `"borromean"`, so each nucleon's confinement core
    is the alternating `(σ₀σ₁⁻¹)³`. Pass `"grouped"` for the pre-2026-09-05
    word — which is what any caller asserting the PER-GENERATOR factorisation
    `tr_M = ∏_gen tr₂` must do, since that identity needs each generator's
    letters contiguous and the Borromean word interleaves them (bean
    `qou-hu1f`). Log-RATIO consumers need no change: the ratio is invariant.
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_core import h as h_val  # numeric h = q_0 − q_0⁻¹

    triples = atom_braid_word_3A(
        Z, N,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=include_inter,
        intra_order=intra_order,
        ordering=ordering,
    )
    out: list[tuple[int, str]] = []
    for run_idx, (c, d, g) in enumerate(triples):
        ctx = f"atom_canonical_crossings(Z={Z}, N={N}) gen={int(g)} run={run_idx}"
        out.append((int(g), classify_crossing(
            float(c), float(d), h_val, context=ctx,
        )))
    return out


def d_for_ctype(ctype: str, h_val, *, delta=None):
    """The Hecke shift `d` a ctype denotes, in the caller's numeric type.

    Consumers used to hardcode `{"sigma": 0, "sigma_inv": -h, "averaged": -h/2}`
    inline. That is how the colour-weighted interface got lost: a private
    lookup cannot know about a label it predates, and there were at least two
    such lookups plus two validators with their own `{0, -h, -h/2}` vocabulary.
    Centralised here so a new crossing type is a one-line change with one
    place to audit.

    `h_val` is passed in rather than recomputed so the caller's precision
    (mpmath mpf, sympy expression, float) carries through unchanged -- do not
    coerce it.

    `delta` overrides the substrate flavour split used by
    `averaged_weighted`. It exists for **q-symbolic callers**, and skipping it
    there is a layer straddle: the default `_avg_color_delta()` is evaluated
    at the numeric `q_parameter.Q`, so passing a sympy `h_val` and taking the
    default silently bakes a q0-pinned constant into an otherwise
    q-symbolic expression -- an ideal/experimental mix inside one quantity,
    which AGENTS.md rules out regardless of its size. δ has a closed form, so
    symbolic callers have no excuse:

        from _li_2_q_util import flavor_split_leading
        d_for_ctype(ctype, h_sym, delta=flavor_split_leading(q_sym))

    Numeric callers should leave it None and get the cached q0 value.
    """
    if ctype == "sigma":
        return 0 * h_val
    if ctype == "sigma_inv":
        return -h_val
    if ctype == "averaged":
        return -h_val / 2
    if ctype == "averaged_weighted":
        # -h(1/2 - delta/4), written so h_val's type drives the arithmetic.
        d = _avg_color_delta() if delta is None else delta
        # Honour the "caller's type carries through" contract above. The other
        # three ctypes return whatever `h_val` is; this one used to return an
        # `mpf` REGARDLESS, because the cached δ is an mpf and mpmath wins the
        # promotion. So the single ctype this whole arc is about was the one
        # that broke the function's own documented contract.
        #
        # It was not free. Downstream numpy code builds `sigma + d*eye` in a
        # float64 array; one mpf promotes the array to dtype=object and the
        # per-matmul cost jumps, measured on tritium where the first
        # averaged_weighted crossing lands at index 11 of 35. Three call sites
        # now carry a `float(d_for_ctype(...))` workaround for this
        # (hoefsmit_numpy, and the two numpy dtype audits), and
        # numpy_mpmath_dtype_leak_audit exists partly to police it.
        #
        # Downcast ONLY for a plain-float caller, who has already declared
        # float precision by passing one. mpf and sympy callers are untouched,
        # so nothing that wanted 50 dps loses a digit.
        if isinstance(h_val, float):
            d = float(d)
        return -h_val * (1 - d / 2) / 2
    raise ValueError(f"unknown ctype {ctype!r}")


#: Every ctype `classify_crossing` can return. The one place to read when
#: asking "have I covered them all?" — see `sign_for_ctype` and
#: `test_ctype_consumer_coverage.py`.
CTYPES: tuple[str, ...] = (
    "sigma", "sigma_inv", "averaged", "averaged_weighted",
)


def sign_for_ctype(ctype: str) -> int:
    """The `sign ∈ {-1, 0, +1}` wire encoding of a ctype.

    ⚠ **Lossy for `averaged_weighted`, by construction.** A sign cannot
    carry a magnitude, so both averaged interfaces collapse onto `0` — the
    colour-blind projection. The p-n colour weighting `-h(1/2 - δ/4)` is
    *not* representable in this format at all; consumers that need it must
    take `d_for_ctype` instead, which is exact.

    This is not a new loss: every sign-format consumer already behaved this
    way, because before `averaged_weighted` existed `classify_crossing`
    returned `averaged` for both. Centralising it here makes the projection
    explicit and auditable rather than an omission in four private tables.
    The representational gap itself stays open under bean `qou-fv0s`.
    (Retargeted 2026-08-30: this line said `qou-gdtb`, which is COMPLETED
    and correctly so. `qou-gdtb` closed the *pair* form `(gen_idx, ctype)`,
    which round-trips `d` exactly through `d_for_ctype` — measured at
    2.66e-16, float64 epsilon. The gap this docstring describes is the
    *sign* wire, a different encoding, and it is `qou-fv0s`. Pointing a
    live gap at a closed bean invites reopening a bean that is right.)
    """
    if ctype == "sigma":
        return 1
    if ctype == "sigma_inv":
        return -1
    if ctype in ("averaged", "averaged_weighted"):
        return 0
    raise ValueError(f"unknown ctype {ctype!r}")


def convention_fingerprint(crossings) -> str:
    """A stable label for the crossing convention a WORD ACTUALLY USES.

    `"sigma:11+sigma_inv:7+averaged:4+averaged_weighted:1"` — the ctype
    multiset, in `CTYPES` order, from the word itself rather than from a
    hand-written tag.

    This exists because the symbolic-χ caches keyed on nothing but the file's
    existence. `per_irrep_pole_deuteron_h6` is literally
    `if CHI_CACHE.exists(): return d`, and `per_irrep_pole_atom` resumes on
    partition coverage alone. Neither has any notion of which word produced
    the cached entries, so when the colour-weighted p-n interface landed, the
    caches written before it kept being served — and nine committed witnesses
    with a p-n bond still carry colour-BLIND χ while their producers build the
    weighted word. The producers were never wrong; the caches simply could not
    tell that the question had changed.

    A convention tag hand-set by an auditing pass cannot close that: it
    records what someone concluded about the stored data, not what the current
    builder would emit. Deriving the fingerprint from `crossings` makes the
    two directly comparable, which is the whole point — see
    `convention_label` for the human-facing name.
    """
    from collections import Counter
    counts = Counter(ct for _, ct in crossings)
    unknown = set(counts) - set(CTYPES)
    if unknown:
        raise ValueError(f"unknown ctype(s) in word: {sorted(unknown)}")
    return "+".join(f"{ct}:{counts[ct]}" for ct in CTYPES if counts.get(ct))


def word_fingerprint(crossings) -> str:
    """A stable hash of the ORDERED word: every (generator, ctype) in sequence.

    `convention_fingerprint` is a ctype multiset, so it cannot see a
    reordering of the same letters. The 2026-09-05 intra-ordering ruling
    (grouped -> alternating, bean qou-hu1f) is exactly such a reordering, and
    it left the multiset unchanged: measured 2026-11-20, chi-neutron-h3 and
    chi-deuteron-h6 matched their multiset fingerprint while serving
    characters of the superseded word (bean qou-4383). A cache guard keyed on
    the word itself has to hash the order.

    Returns the first 16 hex digits of SHA-256 over "gen:ctype" joined by ",".
    """
    import hashlib
    for _, ct in crossings:
        if ct not in CTYPES:
            raise ValueError(f"unknown ctype {ct!r}")
    s = ",".join(f"{int(g)}:{ct}" for g, ct in crossings)
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def convention_label(crossings) -> str:
    """The human-facing convention name for a word, derived not declared.

    Matches the strings already in the corpus' `convention` witness field, so
    a regenerated witness stays comparable with the ones already tagged:

      `colour-weighted-averaged-crossing`  the word carries the colour-weighted
                                           p-n interface (every canonical
                                           Z>=1,N>=1 word has exactly one)
      `averaged-crossings`                 averaged crossings, none weighted —
                                           correct for a free word
                                           (`include_inter=False`), a
                                           dineutron/diproton, or a single
                                           nucleon, all of which have no p-n
                                           bond to weight
      `sign-only-crossings`                no averaged crossing of either kind

    Note the corpus also contains `bring_color_weighted-averaged-crossings`,
    a second spelling of the first. Do not add a third: read this function.
    """
    counts = {ct: 0 for ct in CTYPES}
    for _, ct in crossings:
        if ct not in counts:
            raise ValueError(f"unknown ctype {ct!r}")
        counts[ct] += 1
    if counts["averaged_weighted"]:
        return "colour-weighted-averaged-crossing"
    if counts["averaged"]:
        return "averaged-crossings"
    return "sign-only-crossings"


__all__ = [
    "atom_canonical_crossings", "classify_crossing", "d_for_ctype",
    "sign_for_ctype", "CTYPES",
    "convention_fingerprint", "convention_label",
]
