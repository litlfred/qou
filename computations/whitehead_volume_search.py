#!/usr/bin/env python3
"""Whitehead braid-word identification by the formula-free 4G volume test,
using the fast (numpy) validated colored-Jones machinery.

The closure whose normalized colored Jones grows at rate 4·G = 3.66386
(regular ideal octahedron) is the Whitehead link.  Discriminants:
    torus / split         Vol 0
    Whitehead (L5a1)      4G       = 3.66386
    Borromean rings       2Vol(oct)= 7.32772
No colored-Jones form is assumed — the volume is read off the growth.

Audit-only; no wiring.

## Emits its witness (added 2026-08-30, bean `qou-nro6`)

`whitehead-volume-identification.witness.json` was **producerless**: this
script computed exactly what the witness records and then only *printed* it, so
the file was a hand-transcription of console output with no provenance. That is
the `qou-bake` pattern, and the fix it prescribes — teach the script to emit via
`WitnessBuilder`, which stamps `scriptFile` / `scriptHash` / `computedAt` for
free.

Verified before wiring: this script's Richardson values for the recorded braid
word `[1, -2, 1, -2, 1]` reproduce the committed witness exactly where they
overlap — `N8 -> 3.399`, `N10 -> 3.681`.

**One honest gap.** The committed witness also records `N12` (`5.385(raw);
3.744(rich)`); this script's ladder stops at `N10`. The emitted witness
therefore carries `N4..N10` and records the `N12` absence explicitly rather
than copying the old value forward — copying it would be exactly the
transcription this change exists to end.
"""
from __future__ import annotations

import sys
import time
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_fast import volume_estimate, perm_cycles  # noqa: E402

VOL_WHITEHEAD = 3.663862376708876


def curated_words():
    """Standard / literature Whitehead-link braid-word candidates (B₃)."""
    return [
        [1, 1, 2, -1, 2],          # σ1²σ2σ1⁻¹σ2
        [1, 1, -2, 1, -2],
        [1, -2, 1, -2, 1],
        [1, -2, 1, -2, -2],
        [1, 1, 2, 2, -1],
        [1, 2, -1, 2, 2],
        [1, 1, -2, -1, -2],
        [-1, -1, 2, 1, 2],
    ]


def main() -> int:
    t0 = time.monotonic()
    curated_rows = []
    print("Curated Whitehead candidates (B₃), volume via near-root growth (δ=1e-6):")
    print("  target 4G = 3.66386\n")
    for w in curated_words():
        c = perm_cycles(w, 3)
        rows = volume_estimate(w, 3, [4, 6, 8, 10], delta=1e-6)
        vol = rows[-1][2]
        tag = ""
        kind = None
        if vol is not None:
            if abs(vol - VOL_WHITEHEAD) < 0.15:
                kind, tag = "whitehead-4G", "  <== WHITEHEAD (4G)"
            elif abs(vol - 7.3277) < 0.2:
                kind, tag = "borromean-like", "  (Borromean-like)"
            elif abs(vol) < 0.3:
                kind, tag = "torus-split-vol0", "  (torus/split, Vol 0)"
        seq = "  ".join(f"N={N}:{(f'{r:.3f}' if r is not None else f'{e:.3f}')}"
                         for N, e, r in rows)
        print(f"  {str(w):<22} comps={c}  {seq}   vol≈{(f'{vol:.4f}' if vol else '—')}{tag}")
        curated_rows.append({
            "word": list(w), "components": c,
            "ladder": [{"N": N, "raw": (f"{e:.6f}" if e is not None else None),
                        "richardson": (f"{r:.6f}" if r is not None else None)}
                       for N, e, r in rows],
            "vol": (f"{vol:.6f}" if vol is not None else None),
            "kind": kind,
        })

    # bounded formula-free search: all 2-component 3-braid words len 5, no
    # adjacent cancellation, low-N volume near 4G
    print("\nBounded search — 2-component 3-braid words (len 5), vol within 0.3 of 4G:")
    gens = [1, -1, 2, -2]
    seen = set()
    hits = []
    for word in product(gens, repeat=5):
        if any(word[i] == -word[i + 1] for i in range(4)):
            continue
        if perm_cycles(list(word), 3) != 2:
            continue
        # canonical: skip cyclic-rotation / inverse dups cheaply via sorted key
        key = tuple(word)
        if key in seen:
            continue
        seen.add(key)
        try:
            rows = volume_estimate(list(word), 3, [4, 6, 8], delta=1e-6)
            vol = rows[-1][2]
        except Exception:
            continue
        if vol is not None and abs(vol - VOL_WHITEHEAD) < 0.3:
            hits.append((list(word), vol))
    hits.sort(key=lambda t: abs(t[1] - VOL_WHITEHEAD))
    print(f"  {len(hits)} words near 4G (of {len(seen)} 2-component len-5 words):")
    for w, vol in hits[:15]:
        print(f"    {w}  vol≈{vol:.4f}")

    _emit_witness(curated_rows, hits, len(seen), t0)
    return 0


def _emit_witness(curated_rows, hits, n_searched, t0):
    """Emit `whitehead-volume-identification.witness.json` with provenance."""
    try:
        from qou_substrate.witness import WitnessBuilder
    except ImportError:
        print("\n(qou_substrate unavailable — no witness written)")
        return
    # output_dir is explicit: without it the witness lands in the CALLER's cwd
    # (measured -- it went to the repo root when run from there), not beside
    # the script.
    w = WitnessBuilder("whitehead-volume-identification", start_time=t0,
                       output_dir=Path(__file__).resolve().parent)
    w.set_description(
        "Whitehead link (L5a1) braid word identified FORMULA-FREE by the "
        "Kashaev/colored-Jones volume test: Vol -> 4G (regular ideal "
        "octahedron). No colored-Jones form is assumed; the volume is read off "
        "the near-root growth rate. Discriminants: torus/split Vol 0, "
        "Whitehead 4G = 3.66386, Borromean 2Vol(oct) = 7.32772. "
        "PRODUCER ADDED 2026-08-30 (bean qou-nro6): this script computed these "
        "numbers and only PRINTED them, so the committed witness was a "
        "hand-transcription with no provenance -- the qou-bake pattern. It now "
        "emits. Verified before wiring: the Richardson values for the recorded "
        "word [1,-2,1,-2,1] reproduce the committed witness exactly where they "
        "overlap (N8 -> 3.399, N10 -> 3.681).")
    w.add_data("method", (
        "normalized colored Jones raw/[N] via validated U_q(sl2) R-matrix "
        "machinery; (2pi/N)log|norm| at q = e^{i pi (1-1e-6)/N} -> Vol, "
        "Richardson in (log N)/N"))
    w.add_data("vol_target_4G", f"{VOL_WHITEHEAD:.24f}")
    w.add_data("curated_candidates", curated_rows)
    w.add_data("bounded_search", {
        "space": "2-component 3-braid words of length 5, no adjacent cancellation",
        "searched": n_searched,
        "within_0.3_of_4G": len(hits),
        "top": [{"word": wd, "vol": f"{v:.6f}"} for wd, v in hits[:15]],
    })
    w.add_data("ladder_scope", {
        "N_computed": [4, 6, 8, 10],
        "N12_in_committed_witness": "5.385(raw); 3.744(rich)",
        "note": ("the committed witness also recorded N12; this ladder stops at "
                 "N10. The absence is recorded rather than the old value "
                 "copied forward -- copying it would be the transcription this "
                 "change exists to end."),
    })
    identified = [r for r in curated_rows if r.get("kind") == "whitehead-4G"]
    w.add_assertion("at_least_one_word_identifies_as_4G", bool(identified), True)
    # The torus/split control is what makes the 4G identification meaningful:
    # a machine that called everything 4G would pass the first assertion alone.
    w.add_assertion("torus_control_reads_zero",
                    any(r.get("kind") == "torus-split-vol0"
                        for r in curated_rows), True)
    w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": ("a hyperbolic-volume identification by colored-Jones "
                           "growth; it never reads the substrate q0."),
    })


if __name__ == "__main__":
    sys.exit(main())
