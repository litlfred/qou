#!/usr/bin/env python3
"""
B_3-BAND SCANNER for atomic braid Markov sub-folding.

Diagnosis from DB-extension agent: the chirality-residue framework
finds 0 std-channel matches for A≥2 because:
  - All knots in DB are B_3 (use only σ_1, σ_2 = ±1, ±2)
  - Atomic braid for A≥2 uses σ_3, σ_4, ..., σ_{3A-1} for
    inter-nucleon couplings
  - Knot matches can only occur inside the 9-letter B_3 prefix

Solution (option 2): scan B_3-BANDS within the atomic braid.

A "B_3-band" at position i is the maximal consecutive sub-word
using only generators σ_i and σ_{i+1}.  After relabeling
(σ_i → σ_1, σ_{i+1} → σ_2), the band IS a B_3 word; its closure
is a knot/link that may match our database.

This is a partial Markov-reduction: we don't fold the entire braid,
but extract sub-regions that happen to live in some B_{i,i+1}
two-strand band.

Algorithm:
  1. For each band-anchor i = 1, 2, ..., n_strands - 2:
     Extract maximal contiguous runs of letters using only
     gen i and gen i+1.
  2. Relabel: gen i → 1, gen i+1 → 2.
  3. Scan each relabeled band against the 56-knot B_3 database.
  4. Tag matches by (band_anchor, band_position, knot, channel).

Compare with original chirality-residue: the B_3 prefix matches
are all at band_anchor = 1.  This scanner ALSO finds matches at
band_anchor = 4, 7, 10, ... (between-nucleon bands) and 2, 3, ...
(across-shift bands) which may include knot ideals encoding
inter-nucleon physics.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hyperbolic_knot_db_extended import get_extended_knots
EXTENDED_KNOTS = get_extended_knots()
from hecke_core import _step_chain_generic

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))
H_A = Q0 - QI
h_val = float(H_A)


def q_pochhammer(n):
    out = mp.mpf(1)
    for k in range(1, n+1):
        out *= (1 - Q0**k)
    return out


def atomic_braid_word(Z, N):
    """Build atomic braid as signed-int list (1-indexed gens)."""
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    word = []
    for k in range(A):
        chain = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain:
            cf = float(c); df = float(d)
            gen_1idx = g + 1
            if abs(cf - 1.0) < 1e-10 and abs(df) < 1e-10:
                word.append(gen_1idx)
            elif abs(cf - 1.0) < 1e-10 and abs(df + h_val) < 1e-10:
                word.append(-gen_1idx)
            else:
                word.append(gen_1idx)  # ud as positive (mixed)
    return word


def cyclic_shifts(word):
    n = len(word)
    return [tuple(word[i:] + word[:i]) for i in range(n)]


def reversed_word(word):
    return tuple(reversed(word))


def closure_class(word):
    classes = set()
    for shift in cyclic_shifts(word):
        classes.add(shift)
        classes.add(reversed_word(shift))
    return classes


def extract_b3_bands(word, anchors):
    """Find maximal contiguous runs using only gens in {anchor, anchor+1}.

    Returns list of (start, length, sub_word_relabeled, anchor).
    Each band's sub_word uses only ±1, ±2 (relabeled).
    """
    bands = []
    for anchor in anchors:
        i = 0
        n = len(word)
        while i < n:
            # Skip if not in band
            if abs(word[i]) not in (anchor, anchor + 1):
                i += 1
                continue
            # Start of a band
            start = i
            sub = []
            while i < n and abs(word[i]) in (anchor, anchor + 1):
                # Relabel: anchor → 1, anchor+1 → 2
                sign = 1 if word[i] > 0 else -1
                old_gen = abs(word[i])
                new_gen = 1 if old_gen == anchor else 2
                sub.append(sign * new_gen)
                i += 1
            length = i - start
            if length >= 4:  # min knot length
                bands.append((start, length, tuple(sub), anchor))
    return bands


def find_knot_matches_in_band(band_subword, knot_db, min_len=4):
    """Match band subword + cyclic-reversal closure against DB."""
    n = len(band_subword)
    matches = []
    for length in range(min_len, n + 1):
        for start in range(n - length + 1):
            sub = tuple(band_subword[start:start + length])
            for entry in knot_db:
                # entry = (name, braid_word, crossings, vol, [channel])
                if len(entry) < 4:
                    continue
                name = entry[0]
                kw = entry[1]
                vol = entry[3]
                channel = entry[4] if len(entry) > 4 else 0
                if length != len(kw):
                    continue
                if sub in closure_class(kw):
                    matches.append({
                        'sub_start': start, 'sub_length': length,
                        'knot': name, 'volume': vol, 'channel': channel,
                        'subword': list(sub),
                    })
                    break  # one match per (start, length)
    return matches


def main():
    print("=" * 100)
    print("B_3-BAND SCANNER for atomic braid Markov sub-folding")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  |EXTENDED_KNOTS| = {len(EXTENDED_KNOTS)}")
    print()

    isotopes = [
        ('p (1H)', 1, 0),
        ('n',       0, 1),
        ('D',       1, 1),
        ('T',       1, 2),
        ('3He',     2, 1),
        ('4He',     2, 2),
    ]

    rows = []
    for name, Z, N in isotopes:
        word = atomic_braid_word(Z, N)
        A = Z + N
        n_strands = 3 * A
        # Anchors: 1, 2, ..., n_strands - 1 (each pair of adjacent gens)
        anchors = list(range(1, max(2, n_strands)))
        bands = extract_b3_bands(word, anchors)

        all_matches = []
        for start, length, sub, anchor in bands:
            mtches = find_knot_matches_in_band(sub, EXTENDED_KNOTS)
            for m in mtches:
                m['band_anchor'] = anchor
                m['band_start'] = start
                m['band_length'] = length
                all_matches.append(m)

        # Aggregate by channel
        n_sym = sum(1 for m in all_matches if m['channel'] == 0)
        n_std = sum(1 for m in all_matches if m['channel'] == 1)
        n_alt = sum(1 for m in all_matches if m['channel'] == 2)
        # Σ chirality residue (std channel only)
        sum_chir = mp.mpf(0)
        for m in all_matches:
            if m['channel'] != 1:
                continue
            r = m['band_start'] + m['sub_start']  # absolute position
            qpr = q_pochhammer(r) if r >= 1 else mp.mpf(1)
            contrib = me * mp.mpf(str(m['volume'])) * mp.fabs(qpr)
            sum_chir += contrib
        sum_chir_MeV = float(sum_chir)

        print(f"  {name:<8} (Z={Z}, N={N}, 3A={n_strands}, |word|={len(word)}):")
        print(f"    bands extracted: {len(bands)}")
        print(f"    matches: sym={n_sym}, std={n_std}, alt={n_alt}")
        print(f"    Σ_chir (std channel) = {sum_chir_MeV:+.6f} MeV")
        if n_std > 0:
            print(f"    std matches:")
            for m in all_matches:
                if m['channel'] == 1:
                    print(f"      anchor={m['band_anchor']}, abs_pos={m['band_start']+m['sub_start']}, "
                          f"knot={m['knot']}, vol={m['volume']:.3f}")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'n_bands': len(bands),
            'n_sym_matches': n_sym,
            'n_std_matches': n_std,
            'n_alt_matches': n_alt,
            'sum_chir_MeV': sum_chir_MeV,
            'std_matches': [m for m in all_matches if m['channel'] == 1],
        })
        print()

    # Save witness
    witness = {
        'computation': 'atomic-braid-b3-band-scanner',
        'description': (
            'Markov sub-folding scan: extract every contiguous run of '
            '(σ_anchor, σ_anchor+1) letters from the atomic braid, '
            'relabel as B_3 word (1, 2), and scan against the 56-knot '
            'extended database.  Captures inter-nucleon B_3-band knot '
            'ideals not visible to the original prefix-only scan.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'n_knots_in_db': len(EXTENDED_KNOTS),
        'isotopes': rows,
    }
    out = Path(__file__).parent / "atomic-braid-b3-band-scanner.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {out}")


if __name__ == "__main__":
    main()
