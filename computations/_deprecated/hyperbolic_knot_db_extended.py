#!/usr/bin/env python3
"""
EXTENDED HYPERBOLIC KNOT DATABASE — B_3 representatives through 10 crossings.

Provides EXTENDED_KNOTS: a list of (name, B_3 braid word, crossings,
hyperbolic volume, dominant Wedderburn channel) for use by the
chirality-residue framework (all_isotopes_chirality_residue.py).

The database is built by:
  1. Hardcoding well-known B_3 representatives for 4-7 crossing
     hyperbolic knots (matching the existing in-line list in
     all_isotopes_chirality_residue.py).
  2. Querying SnapPy for 8- and 10-crossing prime knots, filtering
     to braid_idx == 3 and vol > 0.01 (excludes torus knots).
  3. For each braid word, computing characters χ_(3), χ_(2,1),
     χ_(1,1,1) at q_0 via Hoefsmit seminormal matrices (n=3 strands)
     and picking the partition with max |χ| as the channel:
         channel 0 = symmetric  (3)
         channel 1 = standard   (2,1)
         channel 2 = alternating (1,1,1)

Note on 9-crossing knots:  SnapPy's stored braid words for prime
9-crossing knots have braid index ≥ 4 (4, 6, or 8); none come back
as B_3 from SnapPy's `Link.braid_word()` API. The Knot Atlas /
KnotInfo do list some 9-crossing knots with braid index 3, but
verifying the published B_3 words against SnapPy volumes failed
(volume mismatch).  We therefore omit 9-crossing knots from the
extended database — partial extension is still valuable per task
guidance, and the resulting 8/10-crossing entries are exact.
"""
from __future__ import annotations
import sys, math, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))


# ── Hardcoded 4-7 crossing B_3 knots (matches existing inline table) ──
# (name, braid_word, crossings, volume)
KNOWN_4_TO_7 = [
    ("4_1",  (1, -2, 1, -2),                    4, 2.0298832),
    ("5_2",  (1, 1, 1, -2, 1, -2),              5, 2.8281220),
    ("6_1",  (1, 1, -2, 1, -2, -2),             6, 3.1639633),
    ("6_2",  (1, 1, 1, -2, 1, -2, -2),          6, 4.4015175),
    ("6_3",  (1, 1, -2, 1, -2, 1, -2),          6, 5.6927297),
    ("7_2",  (1, 1, 1, 1, 1, -2, 1, -2),        7, 3.3317442),
    ("7_3",  (1, 1, 1, 1, -2, 1, 1, -2),        7, 4.5921326),
    ("7_4",  (1, 1, -2, 1, -2, -2, -2),         7, 5.1379412),
    ("7_5",  (1, 1, 1, 1, -2, 1, 1, 1, -2),     7, 6.4439185),
    ("7_6",  (1, 1, 1, -2, 1, -2, -2, -2),      7, 7.0846178),
    ("7_7",  (1, 1, -2, 1, -2, 1, -2, -2),      7, 7.6433568),
]


def build_8_10_via_snappy():
    """Enumerate 8- and 10-crossing prime knots, filter to B_3 hyperbolic.
    Returns list of (name, braid_word, crossings, volume).
    """
    import snappy
    out = []
    ranges = {8: 21, 10: 165}
    for c, mx in ranges.items():
        for i in range(1, mx + 1):
            name = f"{c}_{i}"
            try:
                M = snappy.Manifold(name)
                v = float(M.volume())
                link = snappy.Link(name)
                bw = link.braid_word()
                if not bw:
                    continue
                bn = max(abs(g) for g in bw) + 1
                if bn == 3 and v > 0.01:
                    out.append((name, tuple(bw), c, v))
            except Exception:
                pass
    return out


# ══════════════════════════════════════════════════════════════════
#  Channel assignment: compute χ_λ for λ ⊢ 3 via Hoefsmit on B_3
# ══════════════════════════════════════════════════════════════════

def _build_b3_seminormal(q):
    """Build seminormal matrices for σ_1, σ_2 in each irrep of H_3(q).

    Three irreps: λ=(3) sym 1-dim, λ=(2,1) std 2-dim, λ=(1,1,1) alt 1-dim.
    Generator eigenvalues: q (in row-residue) and -q^{-1} (col-residue).

    Returns dict[partition] = (sigma1, sigma2, dim).
    """
    qi = 1.0 / q
    h = q - qi

    # λ=(3): 1-dim, both σ_1, σ_2 act by q (all entries in same row).
    sym = (
        [[q]],     # σ_1
        [[q]],     # σ_2
        1
    )
    # λ=(1,1,1): 1-dim, both σ_1, σ_2 act by -q^{-1}.
    alt = (
        [[-qi]],   # σ_1
        [[-qi]],   # σ_2
        1
    )
    # λ=(2,1): 2-dim seminormal basis, two SYTs:
    #   T1 = [[1,2],[3]]:   contents axis distance ρ(σ_1)=+1, ρ(σ_2)=-2
    #   T2 = [[1,3],[2]]:   contents axis distance ρ(σ_1)=-2, ρ(σ_2)=+1
    # Hoefsmit formula for 2x2 block:
    #   a_ρ = h / (1 - q^{-2ρ})
    # σ_1 acts as a 2x2 block on (T1, T2) with ρ(σ_1)=+1 for T1, -2 for T2.
    # Since T1 and T2 are NOT related by σ_1 swap (σ_1 swaps entries 1<->2;
    # T1's 1,2 are in same row, T2's 1,2 are in different rows).
    #
    # Standard result for 2-dim std irrep of H_3: σ_1 has eigenvalues q, -q^{-1}.
    # Concretely (Hoefsmit normalization):
    #   σ_1 = [[q, 0], [0, -q^{-1}]]  (T1 in symmetric, T2 in antisym channel)
    #   σ_2 = block with axial dist; mixes T1, T2.
    #
    # For ease, use the matrix form from any standard reference (e.g.
    # Mathas, "Iwahori-Hecke Algebras and Schur Algebras" §3):
    # In std basis where σ_1 is diagonal:
    #   σ_1 = diag(q, -q^{-1})
    #   σ_2 = [[a, b], [c, d]]  satisfying braid relation σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2
    #         and Hecke relation σ_2² = h σ_2 + 1.
    # The construction below uses Hoefsmit content distances.
    #
    # T1 has 1 at (0,0), 2 at (0,1), 3 at (1,0).
    #   σ_1 swaps entries 1<->2: (0,0)<->(0,1) — same row, no swap of cells.
    #     Axial distance for σ_1 in T1: content(cell of 2) - content(cell of 1) = 1 - 0 = 1.
    #     Action: a_1 = h/(1 - q^{-2}) = q (since (q-q^{-1})/(1-q^{-2}) = q).
    #     1x1 block, eigenvalue q.
    #   σ_2 swaps entries 2<->3: (0,1)<->(1,0).
    #     ρ = content(cell of 3 in T1) - content(cell of 2 in T1) = -1 - 1 = -2.
    #     Swap gives T2 (after relabeling). 2x2 block with T2.
    #     a = h/(1 - q^{-2*(-2)}) = h/(1 - q^4)
    #     a' = h/(1 - q^{2*(-2)}) = h/(1 - q^{-4})  (i.e. a_{+2})
    # T2 has 1 at (0,0), 2 at (1,0), 3 at (0,1).
    #   σ_1 swaps 1<->2: (0,0)<->(1,0), different rows, content shift -1.
    #     ρ = -1, a = h/(1 - q^2). 1x1 block? No — σ_1 swap maps T2 -> ... wait.
    #     Actually, σ_1 in T2 swaps entries 1 and 2; T2 has them in cells (0,0) and (1,0).
    #     Swapping gives 2 at (0,0), 1 at (1,0): NOT a valid SYT (1 must come first).
    #     So σ_1 acts with 1x1 block: ρ = content(2)-content(1) = -1-0 = -1.
    #     a = h/(1 - q^{-2*(-1)}) = h/(1 - q^2) = -q^{-1}.
    #   σ_2 swaps 2<->3 in T2: (1,0)<->(0,1), content shift +2.
    #     This swap maps T2 -> T1, so 2x2 block (already counted from T1 side).
    #
    # Final: σ_1 in std basis (T1, T2):
    #   σ_1 = [[q, 0], [0, -q^{-1}]]
    # σ_2 in std basis (T1, T2): 2x2 block from ρ=-2 swap T1<->T2:
    #   On T1 (ρ=-2): a = h/(1 - q^4); on T2 (ρ=+2): a' = h/(1 - q^{-4})
    #   b² = a·a' + 1
    #   σ_2 = [[a, b], [b, a']]
    a = h / (1.0 - q**4)
    a_prime = h / (1.0 - q**(-4))
    b_sq = a * a_prime + 1.0
    b = math.sqrt(abs(b_sq))
    sigma1_std = [[q, 0.0], [0.0, -qi]]
    sigma2_std = [[a, b], [b, a_prime]]
    std = (sigma1_std, sigma2_std, 2)

    return {(3,): sym, (2,1): std, (1,1,1): alt}


def _matmul(A, B, dim):
    out = [[0.0]*dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            s = 0.0
            for k in range(dim):
                s += A[i][k]*B[k][j]
            out[i][j] = s
    return out


def _matinv2(M):
    """2x2 inverse."""
    a, b = M[0]
    c, d = M[1]
    det = a*d - b*c
    return [[d/det, -b/det], [-c/det, a/det]]


def _matinv1(M):
    return [[1.0/M[0][0]]]


def _trace(M, dim):
    return sum(M[i][i] for i in range(dim))


def _eye(dim):
    return [[1.0 if i==j else 0.0 for j in range(dim)] for i in range(dim)]


def _word_matrix(braid_word, sigma1, sigma2, dim):
    """Multiply matrices for braid word; positive g -> sigma_g, negative -> inverse."""
    if dim == 1:
        # Scalar product
        s1 = sigma1[0][0]
        s2 = sigma2[0][0]
        prod = 1.0
        for g in braid_word:
            if g == 1:
                prod *= s1
            elif g == -1:
                prod *= 1.0/s1
            elif g == 2:
                prod *= s2
            elif g == -2:
                prod *= 1.0/s2
        return [[prod]]
    # dim 2
    s1_inv = _matinv2(sigma1)
    s2_inv = _matinv2(sigma2)
    prod = _eye(dim)
    for g in braid_word:
        if g == 1:
            prod = _matmul(prod, sigma1, dim)
        elif g == -1:
            prod = _matmul(prod, s1_inv, dim)
        elif g == 2:
            prod = _matmul(prod, sigma2, dim)
        elif g == -2:
            prod = _matmul(prod, s2_inv, dim)
        else:
            raise ValueError(f"Bad generator {g}")
    return prod


def compute_channel(braid_word, q):
    """Compute χ_(3), χ_(2,1), χ_(1,1,1) for braid word at q.
    Return (channel_idx, char_dict) where channel_idx is partition with
    max |χ|: 0=sym (3), 1=std (2,1), 2=alt (1,1,1)."""
    irreps = _build_b3_seminormal(q)
    chars = {}
    for shape, (s1, s2, dim) in irreps.items():
        M = _word_matrix(braid_word, s1, s2, dim)
        chars[shape] = _trace(M, dim)
    abs_vals = [abs(chars[(3,)]), abs(chars[(2,1)]), abs(chars[(1,1,1)])]
    channel = max(range(3), key=lambda i: abs_vals[i])
    return channel, chars


# ══════════════════════════════════════════════════════════════════
#  Build EXTENDED_KNOTS
# ══════════════════════════════════════════════════════════════════

def build_database(verbose=True):
    """Build EXTENDED_KNOTS list with channel annotation."""
    from q_parameter import Q as Q0_FLOAT
    q0 = Q0_FLOAT

    raw = list(KNOWN_4_TO_7)
    if verbose:
        print(f"Hardcoded 4-7 crossing knots: {len(raw)}")

    # SnapPy 8 + 10 crossing
    try:
        snappy_knots = build_8_10_via_snappy()
        if verbose:
            print(f"SnapPy 8/10-crossing B_3 hyperbolic knots: {len(snappy_knots)}")
        raw.extend(snappy_knots)
    except Exception as e:
        if verbose:
            print(f"SnapPy enumeration failed: {e}")

    # Channel-annotate every knot
    out = []
    for name, bw, c, v in raw:
        try:
            channel, chars = compute_channel(bw, q0)
            chars_serial = {f"({','.join(str(x) for x in shape)})": float(val)
                            for shape, val in chars.items()}
            out.append({
                'name': name, 'braid_word': list(bw), 'crossings': c,
                'volume': v, 'channel': channel,
                'channel_label': ['sym', 'std', 'alt'][channel],
                'characters': chars_serial,
            })
        except Exception as e:
            if verbose:
                print(f"  channel computation failed for {name}: {e}")
    return out


# Public list — name, braid word, volume, channel  (matching existing format)
def to_chirality_format(db):
    """Convert to (name, word, vol, channel) tuples for chirality-residue."""
    return [(d['name'], tuple(d['braid_word']), d['volume'], d['channel'])
            for d in db]


# Module-level cache: built lazily
_DB_CACHE = None

def get_extended_knots():
    """Return cached EXTENDED_KNOTS in (name, word, vol, channel) format."""
    global _DB_CACHE
    if _DB_CACHE is None:
        db = build_database(verbose=False)
        _DB_CACHE = to_chirality_format(db)
    return _DB_CACHE


EXTENDED_KNOTS = None  # set on import; populated below


def main():
    print("=" * 100)
    print("HYPERBOLIC KNOT DATABASE — EXTENDED (B_3 through 10 crossings)")
    print("=" * 100)

    db = build_database(verbose=True)
    print(f"\n  Total: {len(db)} knots")

    by_c = {}
    by_chan = {0: 0, 1: 0, 2: 0}
    for d in db:
        by_c.setdefault(d['crossings'], []).append(d['name'])
        by_chan[d['channel']] += 1

    print(f"\n  By crossing number:")
    for c in sorted(by_c):
        print(f"    {c}-crossing: {len(by_c[c])} knots")
    print(f"\n  By channel:")
    print(f"    sym (channel 0):  {by_chan[0]}")
    print(f"    std (channel 1):  {by_chan[1]}")
    print(f"    alt (channel 2):  {by_chan[2]}")

    # Verify volumes via SnapPy where available
    try:
        import snappy
        print(f"\n  Volume verification (SnapPy):")
        max_err = 0.0
        for d in db:
            try:
                M = snappy.Manifold(d['name'])
                v_snappy = float(M.volume())
                err = abs(v_snappy - d['volume'])
                if err > 1e-3:
                    print(f"    {d['name']}: stored={d['volume']:.5f}, "
                          f"snappy={v_snappy:.5f}, err={err:.2e}  *MISMATCH*")
                max_err = max(max_err, err)
            except Exception:
                pass
        print(f"    Max volume error vs SnapPy: {max_err:.2e}")
    except ImportError:
        print("  (SnapPy not available — skipping volume verification)")

    # Save witness
    from q_parameter import Q as Q0_FLOAT
    witness = {
        'computation': 'hyperbolic-knot-db-extended',
        'description': (
            'Extended database of B_3-representable hyperbolic knots '
            'through 10 crossings, with Wedderburn channel annotation '
            'computed from H_3(q_0) seminormal-matrix characters.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'count': len(db),
        'by_crossing': {str(c): len(v) for c, v in sorted(by_c.items())},
        'by_channel': {'sym': by_chan[0], 'std': by_chan[1], 'alt': by_chan[2]},
        'knots': db,
    }
    out = Path(__file__).parent / "hyperbolic-knot-db-extended.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
