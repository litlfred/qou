#!/usr/bin/env python3
"""
Numerical realisation of the descent involution tau_hat_0 at A=1 (proton).

  A_0 = H_3(q_0)            -- rank-3 Iwahori-Hecke algebra (dim 6)
  Omega^1(A_0) = ker(m)     -- universal Kahler differentials (dim 30)
  A_1 = A_0 (x) Omega^1     -- jet prolongation J^1(A_0)  (dim 180)
  ell_0 : A_0 -> A_1        -- ascent (chosen connection)
  d_1   : End(A_1) -> End(A_0)   -- descent retraction
  tau_hat_0 = ell_0 . d_1   -- idempotent projector on End(A_1)

H_3(q) basis (Coxeter-reduced words for S_3):
    e_0 = 1
    e_1 = sigma_1
    e_2 = sigma_2
    e_3 = sigma_1 sigma_2
    e_4 = sigma_2 sigma_1
    e_5 = sigma_1 sigma_2 sigma_1   ( = sigma_2 sigma_1 sigma_2 )

Hecke relation: sigma_i^2 = (q - q^{-1}) sigma_i + 1.
Braid relation: sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2.

Phase A.3 of issue #522.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
# Use the 50-digit string form of q_0 (not the float64 Q) so mp.mpf
# below carries the full 50 decimal digits — passing the f64 Q would
# cap precision at ~15 digits (Gemini PR #533 review, r3178376577).
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()
Q0 = mp.mpf(Q_50_DIGIT_STR)

DIM_A0 = 6  # |S_3| = 6


# ---------------------------------------------------------------------------
# H_3(q_0) regular representation
# ---------------------------------------------------------------------------

# Reduced-word list (each is the basis element index 0..5).
# We write each as a Python tuple of generator indices in {1, 2}.
RED_WORDS = [
    (),          # e_0 = 1
    (1,),        # e_1 = sigma_1
    (2,),        # e_2 = sigma_2
    (1, 2),      # e_3 = sigma_1 sigma_2
    (2, 1),      # e_4 = sigma_2 sigma_1
    (1, 2, 1),   # e_5 = sigma_1 sigma_2 sigma_1
]


def reduce_word(word: tuple[int, ...], q):
    """Reduce a word in {sigma_1, sigma_2} to the H_3 basis using Hecke +
    braid relations.  Returns a dict {basis_index: coefficient}.
    """
    h = q - 1 / q  # (q - q^{-1})

    # Each "term" is (coefficient_mp, word_tuple).
    terms = [(mp.mpf(1), tuple(word))]
    out: dict[int, "mp.mpf"] = {i: mp.mpf(0) for i in range(DIM_A0)}

    # Repeatedly normalise terms until all reduce to one of RED_WORDS.
    pending = list(terms)
    safety = 0
    while pending:
        safety += 1
        if safety > 10000:
            raise RuntimeError("reduce_word: too many iterations")
        coef, w = pending.pop()
        # 1. Apply braid relation:  sigma_i sigma_j sigma_i with i != j
        #    Standard form for S_3 longest element: keep (1,2,1).
        #    Convert (2,1,2) -> (1,2,1).
        new_w = list(w)
        changed = True
        while changed:
            changed = False
            for k in range(len(new_w) - 2):
                if new_w[k] == 2 and new_w[k + 1] == 1 and new_w[k + 2] == 2:
                    new_w[k:k + 3] = [1, 2, 1]
                    changed = True
                    break
        # 2. Apply Hecke relation to consecutive equal generators.
        i = 0
        while i < len(new_w) - 1:
            if new_w[i] == new_w[i + 1]:
                # sigma_k^2 = h * sigma_k + 1
                # term = coef * (... sigma_k^2 ...)
                #      = coef * h * (... sigma_k ...) + coef * (... 1 ...)
                left = new_w[:i]
                right = new_w[i + 2:]
                pending.append((coef * h, tuple(left + [new_w[i]] + right)))
                pending.append((coef, tuple(left + right)))
                break
            i += 1
        else:
            # 3. The word is a reduced product.  Find its index in RED_WORDS.
            t = tuple(new_w)
            if t not in RED_WORDS:
                # Try braid -- one more pass after braid normalisation.
                # If still missing, raise.
                raise RuntimeError(
                    f"reduce_word: cannot index reduced word {t}"
                )
            idx = RED_WORDS.index(t)
            out[idx] = out[idx] + coef

    return out


def left_mult_matrix(idx: int, q) -> mp.matrix:
    """6 x 6 matrix for left multiplication by basis element e_{idx}.

    The (i, j) entry is the coefficient of e_i in e_{idx} * e_j.
    """
    M = mp.zeros(DIM_A0, DIM_A0)
    e_word = RED_WORDS[idx]
    for j in range(DIM_A0):
        prod_word = e_word + RED_WORDS[j]
        coeffs = reduce_word(prod_word, q)
        for i, c in coeffs.items():
            M[i, j] = c
    return M


def build_basis_left_mults(q) -> list[mp.matrix]:
    """List [L_{e_0}, ..., L_{e_5}] of left-multiplication matrices."""
    return [left_mult_matrix(i, q) for i in range(DIM_A0)]


# ---------------------------------------------------------------------------
# Multiplication tensor m : A_0 (x) A_0 -> A_0
# ---------------------------------------------------------------------------
def build_multiplication_matrix(q) -> mp.matrix:
    """Returns a 6 x 36 matrix M such that for x = sum a_i e_i, y = sum b_j e_j,
    the column index k = i*6 + j holds m(e_i (x) e_j) expressed in the e basis.
    """
    Lmats = build_basis_left_mults(q)
    M = mp.zeros(DIM_A0, DIM_A0 * DIM_A0)
    for i in range(DIM_A0):
        for j in range(DIM_A0):
            # m(e_i (x) e_j) = e_i * e_j = column j of L_{e_i}.
            col = i * DIM_A0 + j
            for r in range(DIM_A0):
                M[r, col] = Lmats[i][r, j]
    return M


# ---------------------------------------------------------------------------
# Kernel via mpmath SVD (column-space approach)
# ---------------------------------------------------------------------------
def kernel_basis(M: mp.matrix, *, tol: mp.mpf | float | None = None) -> mp.matrix:
    """Returns a (cols x nullity) matrix whose columns span ker(M).

    Strategy: row-reduce M to find its right-nullspace.  We use a manual
    Gaussian elimination since mpmath has no .nullspace().

    The default tolerance scales with `mp.dps` so the same routine
    behaves correctly at 50 dps (default) and at higher precisions.
    """
    if tol is None:
        # 10 digits of headroom below the working precision floor.
        tol = mp.mpf(10) ** (-(mp.mp.dps - 10))
    rows = M.rows
    cols = M.cols
    A = mp.matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            A[i, j] = M[i, j]

    # Track row operations -- we don't need them, we just need pivots.
    # Standard reduced row echelon form (RREF).
    pivot_cols: list[int] = []
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        # Find pivot in column c, rows r..rows-1.
        pivot_row = -1
        best = mp.mpf(0)
        for k in range(r, rows):
            v = abs(A[k, c])
            if v > best:
                best = v
                pivot_row = k
        if pivot_row == -1 or best < tol:
            continue
        # Swap.
        if pivot_row != r:
            for jj in range(cols):
                A[r, jj], A[pivot_row, jj] = A[pivot_row, jj], A[r, jj]
        # Eliminate.
        piv = A[r, c]
        for jj in range(cols):
            A[r, jj] = A[r, jj] / piv
        for k in range(rows):
            if k == r:
                continue
            factor = A[k, c]
            if abs(factor) < tol:
                continue
            for jj in range(cols):
                A[k, jj] = A[k, jj] - factor * A[r, jj]
        pivot_cols.append(c)
        r += 1

    free_cols = [c for c in range(cols) if c not in pivot_cols]
    # Build kernel basis.
    K = mp.zeros(cols, len(free_cols))
    for k_idx, fc in enumerate(free_cols):
        # x[fc] = 1, x[other free] = 0.
        K[fc, k_idx] = mp.mpf(1)
        # For each pivot column c with pivot in row r_c, x[c] = -A[r_c, fc].
        for r_c, pc in enumerate(pivot_cols):
            K[pc, k_idx] = -A[r_c, fc]
    return K


# ---------------------------------------------------------------------------
# Connection / ascent / descent
# ---------------------------------------------------------------------------
def universal_derivation_d1(q):
    """The universal derivation d : A_0 -> A_0 (x) A_0 sends a -> 1 (x) a - a (x) 1.
    Returns a 36 x 6 matrix expressing d(e_j) in the e_i (x) e_j basis.
    Image lies in Omega^1 = ker(m).
    """
    D = mp.zeros(DIM_A0 * DIM_A0, DIM_A0)
    for j in range(DIM_A0):
        # d(e_j) = 1 (x) e_j - e_j (x) 1
        # 1 (x) e_j -> column index 0*6 + j
        D[0 * DIM_A0 + j, j] = D[0 * DIM_A0 + j, j] + 1
        # -(e_j (x) 1) -> column index j*6 + 0
        D[j * DIM_A0 + 0, j] = D[j * DIM_A0 + 0, j] - 1
    return D


def express_in_basis(K: mp.matrix, V: mp.matrix) -> mp.matrix:
    """Given basis K (cols x dim) of a subspace W <= V_amb and vectors V (cols
    x k) lying in W, return coords (dim x k).  Uses least-squares via normal
    eqn since we're working in mpmath.
    """
    # K : amb x dim, V : amb x k.  Solve K c = V.
    # Use normal equations c = (K^T K)^{-1} K^T V.
    KT = mp.matrix(K.cols, K.rows)
    for i in range(K.rows):
        for j in range(K.cols):
            KT[j, i] = K[i, j]
    KTK = KT * K
    KTV = KT * V
    # Solve KTK c = KTV by LU.
    coords = mp.lu_solve(KTK, KTV)
    return coords


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("tau_hat_0 proton-scale numerical realisation")
    print(f"  q_0 = {Q0}   mp.mp.dps = {mp.mp.dps}")
    print("=" * 70)
    q = mp.mpf(Q0)

    # --- Step 1: H_3(q_0) regular representation ---
    print("\n[step 1] Building left-multiplication matrices for H_3(q_0)...")
    Lmats = build_basis_left_mults(q)
    print(f"  built {len(Lmats)} matrices, shape {Lmats[0].rows} x "
          f"{Lmats[0].cols}.")

    # --- Step 2: Multiplication map m : A_0 (x) A_0 -> A_0 ---
    print("\n[step 2] Building multiplication matrix m (6 x 36)...")
    M = build_multiplication_matrix(q)
    print(f"  shape: {M.rows} x {M.cols}.")

    # --- Step 3: Omega^1 = ker(m) ---
    print("\n[step 3] Computing kernel of m via row-reduction...")
    K_omega = kernel_basis(M)
    dim_omega1 = K_omega.cols
    print(f"  dim Omega^1 = {dim_omega1}  "
          f"(expected 30 = 36 - 6).")
    assert dim_omega1 == 30, f"expected dim Omega^1 = 30, got {dim_omega1}"

    # --- Step 4: A_1 dimension ---
    dim_A1 = DIM_A0 * dim_omega1
    print(f"\n[step 4] dim A_1 = dim A_0 * dim Omega^1 = "
          f"{DIM_A0} * {dim_omega1} = {dim_A1}.")

    # --- Step 5: ell_0 and d_1 ---
    # We use the universal derivation as our connection:
    #     nabla = d : A_0 -> Omega^1,   d(e_j) = 1 (x) e_j - e_j (x) 1.
    # ell_0 : A_0 -> A_1 = A_0 (x) Omega^1,  e_j -> e_j (x) d(e_0)? -- NO,
    # d(e_0) = d(1) = 0 in unital differential calc.  Use instead:
    #
    #     ell_0(a) := a (x) d(g)
    #
    # for a fixed non-vanishing element g in A_0.  Choose g = e_1 = sigma_1
    # (a non-trivial generator).  Then d(g) = 1 (x) g - g (x) 1, a non-zero
    # element of Omega^1.
    #
    # The descent retraction d_1 is the canonical pairing
    #     r_1 : A_0 (x) Omega^1 -> A_0,  a (x) omega -> phi_0(omega) * a
    # where phi_0 : Omega^1 -> C is a chosen "evaluation at the unit
    # connection" satisfying phi_0(d(g)) = 1.  We construct phi_0 so that
    # d_1 . ell_0 = id_{A_0} -- this is the splitting condition.
    print("\n[step 5] ell_0 (ascent), d_1 (descent retraction)...")
    print("   Connection: trivial / universal derivation d(a) = 1(x)a - a(x)1.")
    print("   ell_0(a) := a (x) d(sigma_1)  (sigma_1 = generator).")

    D = universal_derivation_d1(q)            # 36 x 6
    d_sigma1 = D[:, 1]                        # column for sigma_1 (e_1)
    # Express d(sigma_1) in the Omega^1 basis K_omega (cols).
    # d(sigma_1) is 36-dim; want coords in K_omega's 30 columns.
    coords_dsigma1 = express_in_basis(K_omega, d_sigma1)
    print(f"   d(sigma_1) coords in Omega^1: {coords_dsigma1.rows}-vector "
          f"(expect 30).")
    # ell_0 as a (180 x 6) matrix:
    # ell_0(e_a) = e_a (x) d(sigma_1).  In the ordered basis
    # of A_1 = (e_a (x) omega_b),   index = a * 30 + b,
    # we have ell_0(e_a)_{a*30 + b} = (coords_dsigma1)_b, others 0.
    L0 = mp.zeros(dim_A1, DIM_A0)
    for a in range(DIM_A0):
        for b in range(dim_omega1):
            L0[a * dim_omega1 + b, a] = coords_dsigma1[b, 0]

    # Build phi_0 : Omega^1 -> C with phi_0(d(sigma_1)) = 1.
    # We pick phi_0 as the linear functional dual to coords_dsigma1
    # (i.e., projection onto its 1d span, normalised).
    norm2 = mp.mpf(0)
    for b in range(dim_omega1):
        norm2 = norm2 + coords_dsigma1[b, 0] * coords_dsigma1[b, 0]
    phi0 = mp.zeros(1, dim_omega1)
    for b in range(dim_omega1):
        phi0[0, b] = coords_dsigma1[b, 0] / norm2

    # r_1 as a 6 x 180 matrix:
    # r_1(e_a (x) omega_b) = phi_0(omega_b) * e_a.
    R1 = mp.zeros(DIM_A0, dim_A1)
    for a in range(DIM_A0):
        for b in range(dim_omega1):
            R1[a, a * dim_omega1 + b] = phi0[0, b]

    # Sanity: d_1 . ell_0 = id on A_0?  i.e., R1 * L0 == I_6.
    check = R1 * L0
    err_id = mp.mpf(0)
    for i in range(DIM_A0):
        for j in range(DIM_A0):
            target = mp.mpf(1) if i == j else mp.mpf(0)
            err_id = max(err_id, abs(check[i, j] - target))
    print(f"   ||R1 . L0 - I_6||_inf = {mp.nstr(err_id, 5)}  "
          f"(splitting condition).")
    assert err_id < mp.mpf("1e-30"), \
        f"R1 . L0 != I_6 (err {err_id}) -- splitting condition fails"

    # --- Step 6: tau_hat_0 on End(A_1) ---
    # End(A_1) ~= A_1 (x) A_1^*  =  matrices of size dim_A1 x dim_A1.
    # That's 180^2 = 32400 entries.  Acting on End by:
    #     d_1(phi) = R1 phi L0           (output: 6 x 6 matrix)
    #     ell_0(psi) = L0 psi R1         (input from 6 x 6 matrix)
    #     tau_hat_0(phi) = L0 R1 phi L0 R1
    # i.e., tau_hat_0 = (L0 R1) phi (L0 R1) -- two-sided multiplication
    # by P := L0 R1 (a rank-6 projection on A_1).
    print("\n[step 6] tau_hat_0 on End(A_1)...")
    print(f"   End(A_1) has dim {dim_A1}^2 = {dim_A1 ** 2}.")
    print("   tau_hat_0(phi) = P phi P  with  P := L0 . R1  (180 x 180 "
          "rank-6 idempotent).")

    P = L0 * R1                                # 180 x 180

    # Verify P^2 = P (it should, since R1 L0 = I).
    P2 = P * P
    err_P = mp.mpf(0)
    for i in range(dim_A1):
        for j in range(dim_A1):
            err_P = max(err_P, abs(P2[i, j] - P[i, j]))
    print(f"   ||P^2 - P||_inf = {mp.nstr(err_P, 5)}.")
    assert err_P < mp.mpf("1e-30"), \
        f"P is not idempotent (err {err_P})"

    rank_P = DIM_A0  # by construction
    print(f"   rank(P) = {rank_P}.")

    # tau_hat_0 acts on the 32400-dim space End(A_1) as a Kronecker
    # product:   tau_hat_0 = P (x) P^T   (matrix on vec(phi)).
    # rank(tau_hat_0) = rank(P) * rank(P^T) = 36.
    # Therefore:
    #   dim(im tau_hat_0)  =  dim(descended)  = 36
    #   dim(ker tau_hat_0) =  dim(transient) = 32400 - 36 = 32364

    rank_tau_hat = rank_P * rank_P
    dim_descended = rank_tau_hat
    dim_transient = dim_A1 * dim_A1 - rank_tau_hat
    print(f"\n[step 7] Eigenspace split:")
    print(f"   dim End(A_1)            = {dim_A1 ** 2}")
    print(f"   dim(descended) = im     = rank(P)^2 = "
          f"{rank_P}^2 = {dim_descended}")
    print(f"   dim(transient) = ker    = {dim_transient}")

    # --- Step 7: Verify tau_hat_0^2 = tau_hat_0 (idempotence) ---
    # On a representative basis of End(A_1) we check phi -> P phi P:
    # apply twice and compare.  We sample a few phi to bound the error.
    print("\n[verify] tau_hat_0 idempotence on sample endomorphisms...")
    err_tau = mp.mpf(0)
    n_samples = 5
    mp.rand_seed = 12345
    for s in range(n_samples):
        phi = mp.matrix(dim_A1, dim_A1)
        for i in range(dim_A1):
            for j in range(dim_A1):
                phi[i, j] = mp.mpf((i * 7 + j * 11 + s) % 97 - 48) / 100
        t1 = P * phi * P
        t2 = P * t1 * P
        for i in range(dim_A1):
            for j in range(dim_A1):
                err_tau = max(err_tau, abs(t2[i, j] - t1[i, j]))
    print(f"   ||tau_hat_0(tau_hat_0(phi)) - tau_hat_0(phi)||_inf "
          f"<= {mp.nstr(err_tau, 5)}   (over {n_samples} samples).")

    # ------------------------------------------------------------------
    # Witness output
    # ------------------------------------------------------------------
    witness = {
        "computation": "tau-hat-n-proton-realisation",
        "description": (
            "Numerical realisation of the descent involution "
            "tau_hat_0 = ell_0 . d_1 acting on End_C(A_1) at A=1 "
            "(proton scale).  A_0 = H_3(q_0); Omega^1 = ker(m); "
            "A_1 = A_0 (x) Omega^1.  Phase A.3 of issue #522."
        ),
        "phase": "A.3",
        "blocks_audited": [
            "lifting-and-descent/descent-involution",
            "lifting-and-descent/descent-lemma",
            "lifting-and-descent/descent-lemma-proof",
        ],
        "verdict": "full-realisation",
        "stage": "complete",
        "parameters": {
            "q0": float(Q0),
            "mp_dps": mp.mp.dps,
            "A": 1,
        },
        "dimensions": {
            "dim_A0": DIM_A0,
            "dim_Omega1": dim_omega1,
            "dim_A1": dim_A1,
            "dim_End_A1": dim_A1 * dim_A1,
            "dim_descended": dim_descended,
            "dim_transient": dim_transient,
            "rank_P": rank_P,
        },
        "checks": {
            "splitting_R1_L0_eq_I_inf_norm_err": mp.nstr(err_id, 12),
            "P_idempotent_inf_norm_err": mp.nstr(err_P, 12),
            "tau_hat_idempotent_sample_inf_norm_err": mp.nstr(err_tau, 12),
            "tau_hat_idempotent_n_samples": n_samples,
        },
        "construction": {
            "A0_basis": "H_3(q_0) on the 6 reduced words of S_3.",
            "multiplication_m_shape": [DIM_A0, DIM_A0 * DIM_A0],
            "kernel_method": "Gaussian elimination (RREF) in mpmath.",
            "connection_choice": (
                "Trivial / universal derivation d(a) = 1 (x) a - a (x) 1; "
                "ell_0(a) := a (x) d(sigma_1) (sigma_1 = e_1, generator)."
            ),
            "descent_phi0": (
                "phi_0 chosen as the dual functional to d(sigma_1) within "
                "Omega^1, normalised so that phi_0(d(sigma_1)) = 1.  "
                "This is the splitting condition d_1 . ell_0 = id_{A_0}."
            ),
            "tau_hat_0_form": (
                "P := L0 R1 (180 x 180 rank-6 idempotent).  "
                "tau_hat_0(phi) = P phi P, hence tau_hat_0 = P (x) P "
                "on End(A_1) ~= A_1 (x) A_1^*."
            ),
        },
        "math_gaps": [
            "ell_0 / d_1 are not uniquely specified by the content blocks: "
            "the descent-lemma-proof.md describes an object-level Frobenius "
            "restriction r_n = epsilon (x) id, but Omega^1 has no canonical "
            "unit element (the universal Kahler differential is split-exact "
            "but not as a unital A-bimodule).  Realising (ell_0, d_1) "
            "requires a chosen connection nabla : A_0 -> Omega^1.  This "
            "witness uses the trivial / universal connection.",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    out = Path(__file__).parent / "tau-hat-n-proton-realisation.witness.json"
    witness["lean_uniqueness_ref"] = lean_uniqueness_ref("proton")
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n[witness] -> {out}")


if __name__ == "__main__":
    main()
