#!/usr/bin/env python3
"""
Iterative shell closure — reuse previous Z computation.

Instead of rebuilding from scratch for each Z:
  NF(Z+1) = NF(Z) × (new nucleon) × (new inter-nucleon crossings) × (new electron)

Each step adds O(A) crossings instead of O(A²) from scratch.
Combined with block-diagonal Hoefsmit, this gives O(d × A) per step.

Total: O(d × Σ A) = O(d × Z²/2) instead of O(d × Σ A²) = O(d × Z³/3).
~Z/3 ≈ 10× speedup for Z=30.

Usage:
    python3 shell_closure_iterative.py --kmax 12 --zmax 32
"""
import math, sys, time, json, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from level_k_binding import seminormal_matrix, standard_young_tableaux, content_of
from hoefsmit_witness import load_witness
from q_parameter import Q as q0, Q_INV as qi, HA
from witness_base import WitnessBuilder


def extract_blocks(shape, gen):
    """Direct block extraction from SYT — no dense matrix. O(d) memory."""
    tabs = standard_young_tableaux(shape)
    d = len(tabs)
    if d == 0:
        return None

    a, b = gen + 1, gen + 2
    tab_index = {T: i for i, T in enumerate(tabs)}

    diag = np.zeros(d)
    sing = np.ones(d, dtype=bool)
    blocks = []
    processed = set()

    for i, T in enumerate(tabs):
        if i in processed:
            continue
        rho = content_of(T, b) - content_of(T, a)
        if rho == 0:
            continue
        same_row = any(a in row and b in row for row in T)
        if same_row:
            diag[i] = q0; processed.add(i); continue
        same_col = False
        for c_idx in range(max(len(row) for row in T)):
            col_vals = [T[r][c_idx] for r in range(len(T)) if c_idx < len(T[r])]
            if a in col_vals and b in col_vals:
                same_col = True
        if same_col:
            diag[i] = -qi; processed.add(i); continue
        T_swap = tuple(tuple(b if v == a else (a if v == b else v) for v in row) for row in T)
        j = tab_index.get(T_swap)
        if j is None or j == i:
            diag[i] = q0 if rho > 0 else -qi; processed.add(i); continue
        qr = (q0**rho - qi**rho) / HA
        dv = HA / qr
        od = (1.0 - dv**2)**0.5 if 1.0 - dv**2 > 0 else 0.0
        blocks.append((i, j, dv, od, od, HA - dv))
        sing[i] = sing[j] = False
        processed.add(i); processed.add(j)

    return diag, blocks, sing, d


class PartitionState:
    """Tracks per-generator state for one partition across Z iterations."""

    def __init__(self, shape):
        self.shape = shape
        self.g0 = extract_blocks(shape, 0)
        self.g1 = extract_blocks(shape, 1)
        if self.g0 is None:
            self.dim = 0; return
        self.dim = self.g0[3]

        # Gen 0: diagonal state (eigenvalue products per SYT)
        self.state0 = np.ones(self.dim)
        # Gen 1: singleton scalars + 2×2 block matrices
        self.sing1_state = np.ones(self.dim)
        self.block1_states = [np.eye(2) for _ in self.g1[1]]

    def apply_gen0(self, ct):
        """Apply one gen-0 crossing to diagonal state."""
        diag = self.g0[0]
        if ct == 'pp': self.state0 *= diag
        elif ct == 'nn': self.state0 *= (diag - HA)
        elif ct == 'pn': self.state0 *= (diag - HA/2)

    def apply_gen1(self, ct):
        """Apply one gen-1 crossing to block state."""
        diag1, blocks1, sing1, dim = self.g1
        shift = 0 if ct == 'pp' else (-HA if ct == 'nn' else -HA/2)

        for idx in range(dim):
            if sing1[idx]:
                self.sing1_state[idx] *= (diag1[idx] + shift)

        for bi, (i,j,a,b,c,d) in enumerate(blocks1):
            C = np.array([[a+shift, b], [c, d+shift]])
            self.block1_states[bi] = self.block1_states[bi] @ C

    def trace(self):
        """Current trace = tr(gen0 product) + tr(gen1 product)."""
        tr0 = np.sum(self.state0)
        tr1 = 0.0
        _, blocks1, sing1, dim = self.g1
        for idx in range(dim):
            if sing1[idx]:
                tr1 += self.sing1_state[idx]
        for bi, _ in enumerate(blocks1):
            tr1 += self.block1_states[bi][0,0] + self.block1_states[bi][1,1]
        return tr0 + tr1

    def add_nucleon(self, nuc_type):
        """Add one nucleon: B₃ crossings + quark crossings."""
        # B₃: 3× σ₀ (pp), 3× σ₁⁻¹ (nn)
        for _ in range(3):
            self.apply_gen0('pp')
            self.apply_gen1('nn')

        if nuc_type == 'p':
            self.apply_gen0('pp')   # uu
            self.apply_gen0('pp')   # uu
            self.apply_gen1('pn')   # ud
        else:
            self.apply_gen0('pn')   # ud
            self.apply_gen0('pn')   # ud
            self.apply_gen1('nn')   # dd

    def add_inter_nucleon(self, ti, tj):
        """Add one inter-nucleon crossing on gen 0."""
        if ti == 'p' and tj == 'p': self.apply_gen0('pp')
        elif ti == 'n' and tj == 'n': self.apply_gen0('nn')
        else: self.apply_gen0('pn')

    def add_electron(self):
        """Add one electron crossing on gen 1."""
        self.apply_gen1('nn')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kmax', type=int, default=12)
    parser.add_argument('--zmax', type=int, default=32)
    args = parser.parse_args()

    witness_data = load_witness()
    MAGIC = {2, 8, 20, 28, 50, 82, 126}

    results = {}

    for k in range(3, args.kmax + 1):
        level = witness_data['levels'].get(str(k), [])
        if not level: continue

        t0 = time.time()
        max_dim = max(e['dim'] for e in level)

        # Initialize partition states
        states = []
        for entry in level:
            shape = tuple(entry['shape'])
            w = entry['w']
            ps = PartitionState(shape)
            if ps.dim > 0:
                states.append((ps, w))

        # Build ITERATIVELY: Z=1, then extend to Z=2, Z=3, ...
        ordering = []  # tracks nucleon types added so far
        per_Z = {}

        for Z in range(1, args.zmax + 1):
            N = Z  # Z=N nuclei
            A = Z + N

            # Determine which nucleon to add at this step
            # Ordering: interleaved p/n
            if Z == 1:
                # First two nucleons: p, n
                for ps, w in states:
                    ps.add_nucleon('p')
                ordering.append('p')
                for ps, w in states:
                    ps.add_nucleon('n')
                    # Inter-nucleon with previous
                    ps.add_inter_nucleon('p', 'n')
                ordering.append('n')
                # 1 electron
                for ps, w in states:
                    ps.add_electron()
            else:
                # Add 2 more nucleons (one p, one n) for Z→Z+1
                new_p_idx = len(ordering)
                for ps, w in states:
                    ps.add_nucleon('p')
                    for prev_idx, prev_type in enumerate(ordering):
                        ps.add_inter_nucleon(prev_type, 'p')
                ordering.append('p')

                new_n_idx = len(ordering)
                for ps, w in states:
                    ps.add_nucleon('n')
                    for prev_idx, prev_type in enumerate(ordering):
                        ps.add_inter_nucleon(prev_type, 'n')
                ordering.append('n')

                # 1 more electron (Z increases by 1)
                for ps, w in states:
                    ps.add_electron()

            # Compute weighted ln|χ| at this Z
            total = 0.0
            for ps, w in states:
                chi = ps.trace()
                ln_chi = math.log(abs(chi)) if abs(chi) > 1e-300 else 0
                total += w * ln_chi
            per_Z[Z] = total

        results[k] = per_Z
        elapsed = time.time() - t0
        print(f"k={k:>2d}: {len(states):>3d} partitions, "
              f"max_dim={max_dim:>5d}, {elapsed:.1f}s")

    # Forward δ²
    K = args.kmax
    cum = {}
    for Z in range(1, args.zmax + 1):
        cum[Z] = sum(results.get(kk, {}).get(Z, 0) for kk in range(3, K+1))

    d1 = {Z: cum[Z] - cum[Z-1] for Z in range(2, args.zmax + 1)}
    fwd_d2 = {Z: d1[Z] - d1[Z-1] for Z in range(3, args.zmax + 1)}

    print(f"\nForward δ²(cumulative k=3..{K}):")
    print(f"{'Z':>3s} {'δ²':>10s} {'magic':>6s}")
    print("─" * 25)
    for Z in range(3, args.zmax):
        m = " ★" if Z in MAGIC else ""
        print(f"{Z:>3d} {fwd_d2.get(Z, 0):>+10.4f}{m}")

    # Witness
    w = WitnessBuilder("shell-closure", engine="python")
    w.set_description(f"Iterative shell closure k=3..{K}. Block-diagonal + reuse.")
    w.add_parameter("kmax", K)
    w.add_data("forward_delta2",
               {str(Z): round(fwd_d2.get(Z, 0), 10) for Z in range(3, args.zmax)})
    w.save()


if __name__ == "__main__":
    main()
