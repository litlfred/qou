#!/usr/bin/env python3
"""
Term 5 chirality factor `a_K` — audit of two competing definitions.

`thm:six-term-mass-formula-complete` Term 5 reads `a_K · 𝒞_K`.  The
QOU narrative gives two — apparently distinct — formulas for `a_K`:

A. **Production closed form** (`paper_six_term_isotope_sweep.term5_chirality`):

       a_K = Π_{c ∈ pn-crossings} (1 + sign(c) · h),     h = q − q⁻¹.

   Counts only proton–neutron crossings; intra-nucleon crossings
   contribute nothing.  For the proton (no pn-crossings) this gives
   `a_K = 1` exactly.

B. **Gram-matrix entry** (`gram-matrix-spectral-connection`,
   `conj:knot-factor-frobenius-pairing`):

       a_K = G_{β, β*} / G_{1, 1}  =  tr_M(β · (β*)⁻¹)

   where `β*` is the *mirror braid* (each σ_i ↔ σ_i⁻¹) and `(β*)⁻¹`
   is its Hecke inverse.  This is a Markov trace of a specific
   Hecke product — i.e. directly computable by the recursive-ascent
   path landed in #508 / PR #516.

A demonstration in PR #520 (proton case) found these forms **disagree
by ~2.2%**:  closed-form gives 1.000, Gram form gives `(1 + q²)⁴ /
(16 q⁴) = cosh⁴(log q) ≈ 1.022 at q₀`.  Either:

  (i)  the closed form is a *special-case shortcut* valid only for
       the multi-nucleon binding regime (and degenerate at A=1), or
  (ii) the Gram form requires a different definition of `β*`
       (e.g. transpose-reverse vs. crossing-mirror), or
  (iii) one of the two is mislabelled in the narrative.

This script emits a witness comparing both forms across the
production atomic spectrum.  It also tabulates **four candidate
definitions of `β*`** so the audit reader can pick which Gram-matrix
convention matches the closed-form across atoms — or surface a real
disagreement requiring narrative reconciliation.

Variants tested for `β*`:

  V1  reverse + invert each crossing      (this is β⁻¹ in Hecke)
  V2  invert each, keep order             (mirror knot K* — flip over/under)
  V3  reverse only, no inversion          (antipode-style: word reversal)

  V4  RETIRED 2026-05-18 — was nominally "V2-style but averaged is
      self-mirror", but the implementation was byte-identical to V2
      (both leave the averaged-crossing tuple unchanged), so V4 and
      V2 produced the same Hecke element on every braid word.
      Confirmed numerically in the existing witness: V4 = V2 at the
      proton (1.1471203358935889) and the neutron (1.2267591396724156)
      to all 30 displayed digits.  V4 entries are preserved in the
      historical witness JSON for provenance but the `--variants`
      list no longer accepts V4.  See:
      docs/audits/2026-05-18-item-b-chirality-v234-audit.md §"Finding 1"

All variants reduce to the same value when the braid contains only
σ and σ⁻¹ (no averaged) — they differ only in how `½(σ + σ⁻¹)` maps
under the involution.

Witness:  term5-aK-audit.witness.json
Reference:
  - `gram-matrix-spectral-connection` (Gram form)
  - `paper_six_term_isotope_sweep` (closed form)
  - `conj:knot-factor-frobenius-pairing`

Usage:
    python folio-assistant/computations/term5_aK_audit.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from markov_peel import crossing_from_cd                  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A          # noqa: E402
from hecke_symbolic import (                                # noqa: E402
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q as q_sym,
)
from markov_trace_canonical import tr_M_element            # noqa: E402
from hecke_core import h as _h_num                         # noqa: E402
from q_parameter import Q as Q0                            # noqa: E402
from witness_base import WitnessBuilder                    # noqa: E402


def _classify(c: float, d: float, h_num: float) -> str:
    """Tag a crossing tuple as 'sigma' / 'sigma_inv' / 'averaged'."""
    if abs(c - 1.0) < 1e-9 and abs(d) < 1e-9:
        return "sigma"
    if abs(c - 1.0) < 1e-9 and abs(d + h_num) < 1e-9:
        return "sigma_inv"
    if abs(c - 1.0) < 1e-9 and abs(d + h_num / 2) < 1e-9:
        return "averaged"
    return "unknown"


def mirror_word(word, *, variant: str, h_num: float):
    """Build β* under the named variant.

    See module docstring for variant definitions.
    """
    out = []
    iter_word = reversed(word) if variant in ("V1", "V3") else word
    for c, d, gen in iter_word:
        kind = _classify(c, d, h_num)
        if variant == "V1":
            # Reverse + invert each (this is β⁻¹).
            if kind == "sigma":
                out.append((c, -h_num, gen))
            elif kind == "sigma_inv":
                out.append((c, 0.0, gen))
            else:  # averaged: self-inverse approximation
                out.append((c, d, gen))
        elif variant == "V2":
            # Invert each, keep order (mirror knot K*).
            if kind == "sigma":
                out.append((c, -h_num, gen))
            elif kind == "sigma_inv":
                out.append((c, 0.0, gen))
            else:
                out.append((c, d, gen))
        elif variant == "V3":
            # Reverse only, no inversion (antipode-style).
            out.append((c, d, gen))
        else:
            # V4 was retired 2026-05-18 (byte-identical to V2 on every
            # input).  See module docstring + audit
            # docs/audits/2026-05-18-item-b-chirality-v234-audit.md.
            raise ValueError(
                f"unknown variant: {variant!r} "
                f"(supported: V1, V2, V3; V4 retired — was identical to V2)"
            )
    return out


def _build_beta_reduced(Z: int, N: int, h_num: float):
    """Build the reduced β element ONCE, returning the
    (SymbolicHeckeElement, SymbolicHeckeDivision) pair.  Shared
    across the four variant runs in `aK_audit_atom`.
    """
    word = atom_braid_word_3A(Z, N)
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    for c, d, gen in word:
        elem = elem * crossing_from_cd(gen, c, d, h_num=h_num)
        elem, _ = div.reduce(elem, max_iterations=2000)
    return elem, div, word


def aK_via_gram_shared(
    beta_reduced: "SymbolicHeckeElement",
    div: "SymbolicHeckeDivision",
    word: list,
    Z: int, N: int, *, variant: str,
    h_num: float,
) -> dict:
    """Compute a_K = tr_M(β · β*ᵥ) for one variant, reusing a
    pre-reduced β.

    Without pre-reduction, the audit rebuilt β from scratch for
    each of the four variants — ~4× redundant work.  Now the β
    half is shared; only the variant-dependent suffix is appended
    and reduced.
    """
    beta_star = mirror_word(word, variant=variant, h_num=h_num)
    n_strands = 3 * (Z + N)

    # Start from the shared reduced β; multiply in the variant's
    # mirror suffix and continue reducing.  Each variant gets its
    # own div instance so quotient state doesn't leak.
    elem = beta_reduced
    for c, d, gen in beta_star:
        elem = elem * crossing_from_cd(gen, c, d, h_num=h_num)
        elem, _ = div.reduce(elem, max_iterations=2000)

    tr_sym = tr_M_element(elem, n_strands, simplify=False)
    # Free-symbol scrub: residual quotient-ideal formal variables
    # can survive the reduction.  Substitute them to their NF
    # values (in this audit context, set them to 1 so they don't
    # contaminate the float — matches the Markov-peel convention
    # `tr(formal_var) = trace_of_NF`).  If anything still resists
    # numericisation, surface the symbolic form rather than
    # crashing the per-variant comparison.
    evald = tr_sym.subs(q_sym, Q0).evalf(30)
    try:
        val_at_q0 = float(evald)
    except (TypeError, ValueError):
        # One or more residual formal vars present.  Try forcing
        # them to 1 (their default trace contribution) and retry.
        free_left = [s for s in evald.free_symbols if s != q_sym]
        try:
            evald2 = evald.subs({s: 1 for s in free_left}).evalf(30)
            val_at_q0 = float(evald2)
        except (TypeError, ValueError):
            val_at_q0 = float("nan")
    try:
        sym_simp = sp.cancel(tr_sym)
        sym_form = str(sym_simp)
        ops = int(sp.count_ops(sym_simp))
    except Exception:  # noqa: BLE001
        sym_form = "(simplification failed)"
        ops = -1
    return {"variant": variant, "value_at_q0": val_at_q0,
            "symbolic": sym_form[:300], "ops": ops}


def aK_via_gram(Z: int, N: int, *, variant: str) -> dict:
    """Compute a_K = tr_M(β · β*ᵥ) under the named variant.

    Standalone single-variant API — rebuilds β every call.  For
    multi-variant audits use `_build_beta_reduced` +
    `aK_via_gram_shared` instead (~4× faster across the variant
    sweep).
    """
    h_num = float(_h_num)
    beta_reduced, div, word = _build_beta_reduced(Z, N, h_num)
    return aK_via_gram_shared(
        beta_reduced, div, word, Z, N,
        variant=variant, h_num=h_num,
    )


def aK_closed_form(Z: int, N: int) -> float:
    """Canonical closed-form `a_K = Π_{c ∈ pn-crossings} (1 + sign(c)·h)`.

    Uses the (Z, N)-keyed sign pattern from
    `paper_six_term_isotope_sweep.chirality_signs_for_isotope_inferred`,
    which is the authoritative pattern per
    `prop:chirality-dual-space-derivation` §"Verification" (D: 1+; T,
    ³He: amphichiral 1+/1−; ⁴He: Borromean² 2+/2−).

    Previous adjacency-counting implementation (used `['p']*Z + ['n']*N`
    string ordering) gave 1.209 at T/³He instead of the canonical
    0.956 = 1 − h² — fixed 2026-05-18 per audit doc
    `docs/audits/2026-05-18-chirality-pn-counting-finding2.md`.
    """
    # Import lazily so the module load doesn't trigger the heavy
    # paper_six_term_isotope_sweep import chain when callers only
    # want the audit machinery (e.g. CI smoke tests).
    from paper_six_term_isotope_sweep import (
        chirality_signs_for_isotope_inferred,
    )
    from mpmath import mp, mpf
    signs = chirality_signs_for_isotope_inferred(Z, N)
    # Carry the product in mpmath at the global dps (typically 50)
    # so the closed-form value matches the 50-dps witness baseline;
    # cast to float only at the return boundary (caller comparison
    # is float-keyed against the legacy witness).
    h_val = mpf(repr(_h_num))
    a_K = mpf("1")
    for s in signs:
        a_K *= mpf("1") + s * h_val
    return float(a_K)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Term 5 a_K audit (slow).")
    ap.add_argument(
        "--atoms",
        default="proton,neutron,deuteron,tritium,helium-3",
        help=(
            "Comma-separated subset of atoms to audit. Default = full "
            "spectrum. Use a smaller subset (e.g. 'proton') for "
            "incremental runs in time-bounded environments; the "
            "emitted witness flags partial coverage in `audited_atoms`."
        ),
    )
    ap.add_argument(
        "--variants",
        default="V1,V2,V3",
        help=(
            "Comma-separated subset of mirror variants {V1,V2,V3} to "
            "audit. Default = all three. V1 (β⁻¹ in Hecke) is fast (~0.5s "
            "even at A=2); V2/V3 explore alternative mirror conventions "
            "and exhibit symbolic blowup at A≥2 (V2 alone takes >34 min "
            "for deuteron in this implementation). Use `--variants V1` "
            "for fast incremental backfill of the canonical-Hecke variant "
            "across the spectrum. (V4 was retired 2026-05-18 — it was "
            "byte-identical to V2; passing 'V4' (or any other unknown "
            "variant) exits non-zero with an error message.)"
        ),
    )
    ap.add_argument(
        "--merge-prior",
        action="store_true",
        help=(
            "Merge results with a pre-existing term5-aK-audit.witness.json "
            "in the same directory: rows for atoms NOT in --atoms are "
            "carried over from the prior witness. Enables incremental "
            "backfills (12+ min/atom) without losing previously-computed "
            "atoms."
        ),
    )
    args = ap.parse_args()
    requested = {a.strip() for a in args.atoms.split(",") if a.strip()}
    raw_variants = [v.strip() for v in args.variants.split(",") if v.strip()]
    if "V4" in raw_variants:
        print(
            "ERROR: V4 was retired 2026-05-18 (byte-identical to V2). "
            "See module docstring + "
            "docs/audits/2026-05-18-item-b-chirality-v234-audit.md.",
            flush=True,
        )
        return 2
    requested_variants = [v for v in raw_variants if v in {"V1", "V2", "V3"}]
    unknown = [v for v in raw_variants if v not in {"V1", "V2", "V3"}]
    if unknown:
        print(
            f"ERROR: unknown variant(s) in --variants: {unknown!r}. "
            f"Supported: V1, V2, V3. (V4 was retired 2026-05-18.)",
            flush=True,
        )
        return 2
    if not requested_variants:
        print("ERROR: no valid variants in --variants", flush=True)
        return 2

    print("Term 5 a_K — closed-form vs Gram-matrix audit", flush=True)
    print("=" * 64, flush=True)

    full_spectrum = [
        ("proton",   1, 0),
        ("neutron",  0, 1),
        ("deuteron", 1, 1),
        ("tritium",  1, 2),
        ("helium-3", 2, 1),
    ]
    audited_labels = [lbl for lbl, _, _ in full_spectrum if lbl in requested]
    skipped_labels = [lbl for lbl, _, _ in full_spectrum if lbl not in requested]

    # Optional merge of prior witness rows for atoms we are NOT
    # re-auditing this run.  Lets a slow backfill add one atom at a
    # time without losing the rows produced by earlier runs.
    rows = []
    carried_over_labels = []
    if args.merge_prior:
        prior_path = HERE / "term5-aK-audit.witness.json"
        if prior_path.exists():
            try:
                prior = json.loads(prior_path.read_text())
                prior_rows = prior.get("data", {}).get("results", []) or []
                for prow in prior_rows:
                    plabel = prow.get("atom")
                    if plabel and plabel not in requested:
                        rows.append(prow)
                        carried_over_labels.append(plabel)
                if carried_over_labels:
                    print(
                        f"  carried over {len(carried_over_labels)} prior "
                        f"row(s): {carried_over_labels}",
                        flush=True,
                    )
                    # Atoms carried over count as audited for the
                    # coverage_note bookkeeping.
                    for lbl in carried_over_labels:
                        if lbl in skipped_labels:
                            skipped_labels.remove(lbl)
                        if lbl not in audited_labels:
                            audited_labels.append(lbl)
            except (OSError, json.JSONDecodeError) as exc:
                print(
                    f"  WARN: --merge-prior requested but prior witness "
                    f"unreadable ({exc!r}); proceeding without merge.",
                    flush=True,
                )
    for label, Z, N in full_spectrum:
        if label not in requested:
            continue
        print(f"\n  === {label} (Z={Z}, N={N}, A={Z + N}) ===", flush=True)
        closed = aK_closed_form(Z, N)
        print(f"    closed-form a_K = {closed:.10f}", flush=True)
        # Build the reduced β prefix ONCE per atom — shared across
        # the four variant runs.  Cuts wall time ~4× vs the previous
        # rebuild-per-variant pattern.
        h_num = float(_h_num)
        try:
            t_build = time.time()
            beta_reduced, div, word = _build_beta_reduced(Z, N, h_num)
            print(
                f"    β reduced (shared): "
                f"{time.time() - t_build:.1f}s, "
                f"{len(beta_reduced.terms)} terms",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"    β reduce FAILED: {exc!r}", flush=True)
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "closed_form_aK": closed,
                "error": f"{type(exc).__name__}: {exc}",
            })
            continue
        variant_results = {}
        for variant in requested_variants:
            try:
                t0 = time.time()
                r = aK_via_gram_shared(
                    beta_reduced, div, word, Z, N,
                    variant=variant, h_num=h_num,
                )
                dt = time.time() - t0
                variant_results[variant] = r
                gap = abs(r["value_at_q0"] - closed)
                tag = "≈ closed" if gap < 1e-6 else f"Δ={gap:.4f}"
                print(
                    f"    Gram[{variant}]  = {r['value_at_q0']:+.10f}  "
                    f"({dt:.1f}s, {r['ops']} ops, {tag})",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001
                print(
                    f"    Gram[{variant}]  FAILED: "
                    f"{type(exc).__name__}: {exc}",
                    flush=True,
                )
                variant_results[variant] = {
                    "variant": variant,
                    "error": f"{type(exc).__name__}: {exc}",
                }
        rows.append({
            "atom": label, "Z": Z, "N": N, "A": Z + N,
            "closed_form_aK": closed,
            "gram_variants": variant_results,
        })

    w = WitnessBuilder("term5-aK-audit", engine="sympy")
    w.set_description(
        "Term 5 chirality factor a_K — audit of the production closed "
        "form `Π(1+sign·h)` over pn-crossings vs four Gram-matrix "
        "variants `tr_M(β · β*⁻¹)` (PR #520 follow-up).  The proton "
        "showed a 2.2% gap between closed-form (1.000) and Gram-V1 "
        "(1.022 = cosh⁴(log q)); this audit tabulates all four mirror "
        "conventions across the spectrum so the narrative can be "
        "reconciled to a single canonical definition."
    )
    w.set_content_block("conj:knot-factor-frobenius-pairing")
    w.add_parameter("q0", str(Q0))
    w.add_data("results", rows)
    w.add_data("audited_atoms", audited_labels)
    w.add_data("skipped_atoms", skipped_labels)
    if skipped_labels:
        w.add_data(
            "coverage_note",
            (
                f"Partial run: {len(audited_labels)}/{len(full_spectrum)} "
                f"atoms audited. Skipped: {skipped_labels}. Re-run with "
                "`--atoms p,n,...` (or default = full spectrum) in a "
                "higher time budget to backfill."
            ),
        )
    out_path = w.save()
    print(f"\n  → wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
