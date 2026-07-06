#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic transfer matrix engine for nuclear computations, exact in q.

All quantities are sympy expressions in Symbol('q', positive=True).
No floating point until final evaluation at q0.

The transfer matrix formalism:
  T(c, d) = [[c*(q - q^{-1}) + d,  c],
              [c,                   d]]

Three nuclear crossing types (Hecke convention):
  pp  (proton-proton):   c = 1,   d = 0
  nn  (neutron-neutron): c = 1,   d = -(q - q^{-1})       = -HA
  mix (proton-neutron):  c = 1,   d = -(q - q^{-1})/2     = -HA/2

Markov-traced volume at generator sigma_i:
  V_hat_i(q) = z * M_i[0,0] + M_i[1,0]
  where z = 1/(q^{1/2} + q^{-1/2})

Nuclear Skein polynomial:
  P_N(q) = prod_i V_hat_i(q)

Universal beta decay matrix:
  Delta_beta(q) = T_mix - T_nn
                = T(0, HA/2)  (pure diagonal shift)

Connection to Gröbner--Shirshov NF: each V_hat_i in the transfer matrix
corresponds to one generator sigma_i in the Iwahori--Hecke algebra NF.
The transfer matrix computes the SAME quantity as the Gröbner--Shirshov
reduction but via matrix products instead of word reduction.

Usage:
    cd computations
    python3 transfer_matrix_symbolic.py

    # As a library:
    from transfer_matrix_symbolic import (
        SymbolicTransferMatrix, NucleusTransferMatrix,
        T_pp, T_nn, T_mix, Delta_beta,
        beta_decay_qvalue,
    )
"""

import math
import sys
from pathlib import Path

import sympy as sp
from sympy import sqrt, Rational, log, simplify, expand, Matrix

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import (
    Q_TRITIUM_MEV, Q_C14_MEV, Q_CO60_MEV,
    Q_SR90_MEV, Q_CS137_MEV, Q_BI210_MEV,
    M_P_MEV,
)
from q_parameter import Q as Q0

# -- Symbolic ring: exact in q ------------------------------------------

q = sp.Symbol('q', positive=True)
q_inv = 1 / q
q_half = sqrt(q)
q_half_inv = 1 / sqrt(q)

# Fundamental quantities
ha = q - q_inv                        # q - q^{-1}  (Hecke coefficient)
HA = ha                               # Hecke amplitude q - q⁻¹ (crossing convention)
s_skein = q_half - q_half_inv         # q^{1/2} - q^{-1/2}  (Skein amplitude, used in Delta_beta verification)
z_markov = 1 / (q_half + q_half_inv)  # Markov parameter

# Substrate parameter Q0 imported from q_parameter (single source of truth).

# Threshold: for A <= SYMBOLIC_THRESHOLD, keep the full Skein
# polynomial symbolic AND per-generator volumes symbolic.
# For larger nuclei, construction and evaluation use numeric
# fast paths to avoid sympy expression blowup.
SYMBOLIC_THRESHOLD = 6


# -- Numeric fast path for large nuclei ---------------------------------
# Pre-compute numeric crossing coefficients and matrix ops at q0
# so that large nuclei (A > SYMBOLIC_THRESHOLD) run in milliseconds.

def _numeric_ha(q_val):
    return q_val - 1.0 / q_val

def _numeric_s(q_val):
    return q_val**0.5 - q_val**(-0.5)

def _numeric_z(q_val):
    return 1.0 / (q_val**0.5 + q_val**(-0.5))

def _numeric_crossing_coeffs(ti, tj, q_val):
    """Return numeric (c, d) for nucleon types at given q."""
    ha_val = _numeric_ha(q_val)
    if ti == 'p' and tj == 'p':
        return 1.0, 0.0
    elif ti == 'n' and tj == 'n':
        return 1.0, -ha_val
    else:
        return 1.0, -ha_val / 2

def _numeric_T(c, d, ha_val):
    """Build numeric 2x2 transfer matrix."""
    return [[c * ha_val + d, c], [c, d]]

def _numeric_mat_mul(A, B):
    """Multiply two numeric 2x2 matrices."""
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]],
    ]

def _numeric_traced_vol(M, z_val):
    """Numeric Markov-traced volume."""
    return z_val * M[0][0] + M[1][0]

def _numeric_skein(Z_count, N_count, q_val, ordering=None):
    """Compute P_N(q) and per-generator volumes numerically.

    Returns (volumes_list, log_P, sign).
    """
    A = Z_count + N_count
    if ordering is None:
        ordering = ['p'] * Z_count + ['n'] * N_count
    ha_val = _numeric_ha(q_val)
    z_val = _numeric_z(q_val)

    volumes = []
    log_P = 0.0
    sign = 1

    for i in range(A - 1):
        M = [[1, 0], [0, 1]]  # identity
        for j in range(i + 1, A):
            c, d = _numeric_crossing_coeffs(ordering[i], ordering[j], q_val)
            T = _numeric_T(c, d, ha_val)
            M = _numeric_mat_mul(M, T)
        V = _numeric_traced_vol(M, z_val)
        volumes.append(V)
        if V < 0:
            sign *= -1
            log_P += math.log(-V)
        elif V > 0:
            log_P += math.log(V)
        else:
            return volumes, float('-inf'), 0

    return volumes, log_P, sign


def skein_ln_numeric(Z, N, q_val):
    """Compute ln|P_N(q)| using pure float arithmetic (no sympy).

    This is the public API for numeric-only Skein magnitude computation.
    Use this instead of NucleusTransferMatrix for large nuclei to avoid
    sympy expression blowup.

    Args:
        Z: proton count
        N: neutron count
        q_val: numeric value of the substrate parameter q

    Returns:
        (ln_abs_P, sign) where sign is +1 or -1 (or 0 if P=0).
    """
    if Z + N < 1:
        return (float('-inf'), 0)
    _, log_P, sign = _numeric_skein(Z, N, q_val)
    return (log_P, sign)


# ========================================================================
# 1. SymbolicTransferMatrix -- wraps a 2x2 sympy Matrix
# ========================================================================

class SymbolicTransferMatrix:
    """A 2x2 transfer matrix with symbolic entries in q.

    Constructed from crossing coefficients (c, d):
        T(c, d) = [[c*(q - q^{-1}) + d,  c],
                    [c,                   d]]

    Supports composition (matrix multiplication), Markov trace
    extraction, determinant, eigenvalues, and numeric evaluation.
    """

    def __init__(self, c=None, d=None, matrix=None):
        """Create from (c, d) coefficients or a raw 2x2 Matrix.

        Args:
            c: coefficient of sigma (sympy expression in q)
            d: constant term (sympy expression in q)
            matrix: explicit 2x2 sympy Matrix (overrides c, d)
        """
        if matrix is not None:
            self.mat = Matrix(matrix)
        elif c is not None and d is not None:
            self.mat = Matrix([
                [expand(c * ha + d), c],
                [c,                  d],
            ])
        else:
            raise ValueError("Provide either (c, d) or matrix")

        # Store c, d if provided (useful for inspection)
        self._c = c
        self._d = d

    @staticmethod
    def identity():
        """The 2x2 identity matrix."""
        return SymbolicTransferMatrix(matrix=sp.eye(2))

    @staticmethod
    def zero():
        """The 2x2 zero matrix."""
        return SymbolicTransferMatrix(matrix=sp.zeros(2))

    def compose(self, other):
        """Matrix multiplication: self * other (left-to-right chain)."""
        return SymbolicTransferMatrix(matrix=self.mat * other.mat)

    def __mul__(self, other):
        """Alias for compose."""
        return self.compose(other)

    def __add__(self, other):
        """Matrix addition."""
        return SymbolicTransferMatrix(matrix=self.mat + other.mat)

    def __sub__(self, other):
        """Matrix subtraction."""
        return SymbolicTransferMatrix(matrix=self.mat - other.mat)

    def scale(self, scalar):
        """Scalar multiplication."""
        return SymbolicTransferMatrix(matrix=scalar * self.mat)

    def markov_trace(self):
        """Markov-traced volume: V_hat = z * M[0,0] + M[1,0].

        Returns a sympy expression in q.
        """
        return expand(z_markov * self.mat[0, 0] + self.mat[1, 0])

    def det(self):
        """Determinant of the 2x2 matrix."""
        return simplify(self.mat.det())

    def eigenvalues(self):
        """Eigenvalues of the 2x2 matrix (dict {eigenvalue: multiplicity})."""
        return self.mat.eigenvals()

    def trace(self):
        """Matrix trace (not Markov trace)."""
        return simplify(self.mat.trace())

    def evaluate(self, q_val):
        """Evaluate all entries at q = q_val. Returns a numeric 2x2 list."""
        return [[float(self.mat[i, j].subs(q, q_val))
                 for j in range(2)] for i in range(2)]

    def markov_trace_at(self, q_val):
        """Evaluate the Markov-traced volume at q = q_val."""
        return float(self.markov_trace().subs(q, q_val))

    def __repr__(self):
        return f"SymbolicTransferMatrix(\n  {self.mat}\n)"

    def show(self, name="T"):
        """Pretty-print the matrix with symbolic entries."""
        print(f"{name} =")
        for i in range(2):
            row = [simplify(self.mat[i, j]) for j in range(2)]
            print(f"  [{row[0]},  {row[1]}]")


# ========================================================================
# 2. Pre-built matrices
# ========================================================================

# Crossing coefficients (Hecke convention: c=1 for all, d uses HA = q - q⁻¹)
C_PP, D_PP = sp.Integer(1), sp.Integer(0)
C_NN, D_NN = sp.Integer(1), -HA
C_MIX, D_MIX = sp.Integer(1), -HA / 2

# The three nuclear transfer matrices
T_pp = SymbolicTransferMatrix(c=C_PP, d=D_PP)
T_nn = SymbolicTransferMatrix(c=C_NN, d=D_NN)
T_mix = SymbolicTransferMatrix(c=C_MIX, d=D_MIX)

# Universal beta decay matrix: Delta_beta = T_mix - T_nn = T(0, HA/2)
Delta_beta = T_mix - T_nn

# Electromagnetic vertex (electron capture / pair production)
# T_gamma_e: the electron crossing is a Hopf link (c=1, d=0), same as T_pp
T_gamma_e = SymbolicTransferMatrix(c=sp.Integer(1), d=sp.Integer(0))


def crossing_coeffs(ti, tj):
    """Return symbolic (c, d) for a crossing between nucleon types.

    Args:
        ti, tj: 'p' (proton) or 'n' (neutron)

    Returns:
        (c, d) as sympy expressions
    """
    if ti == 'p' and tj == 'p':
        return C_PP, D_PP
    elif ti == 'n' and tj == 'n':
        return C_NN, D_NN
    else:  # mixed (pn or np)
        return C_MIX, D_MIX


def crossing_matrix(ti, tj):
    """Return the SymbolicTransferMatrix for a crossing between nucleon types."""
    c, d = crossing_coeffs(ti, tj)
    return SymbolicTransferMatrix(c=c, d=d)


# ========================================================================
# 3. NucleusTransferMatrix -- builds the full transfer chain
# ========================================================================

class NucleusTransferMatrix:
    """Transfer matrix chain for a nucleus N(Z, N).

    Builds an ordering of Z protons followed by N neutrons,
    computes per-generator transfer matrix products, extracts
    Markov-traced volumes V_hat_i(q), and computes the Skein
    polynomial P_N(q) = prod_i V_hat_i(q).

    Per-generator volumes are always symbolic (exact in q).
    The full Skein polynomial is kept symbolic only for small
    nuclei (A <= SYMBOLIC_THRESHOLD); for larger nuclei, only
    numeric evaluation is available via skein_at().
    """

    def __init__(self, Z, N, ordering=None):
        """Build the transfer matrix chain for nucleus (Z, N).

        Args:
            Z: proton count
            N: neutron count
            ordering: list of 'p'/'n' for each nucleon position.
                      Default: Z protons then N neutrons.
        """
        self.Z = Z
        self.N = N
        self.A = Z + N

        if ordering is not None:
            if len(ordering) != self.A:
                raise ValueError(
                    f"Ordering length {len(ordering)} != A = {self.A}")
            self.ordering = list(ordering)
        else:
            self.ordering = ['p'] * Z + ['n'] * N

        # For small A: build symbolic per-generator chains.
        # For large A: only build on demand (volumes are computed
        # numerically via _numeric_skein for performance).
        self._generator_matrices = None  # lazy: built on first access
        self._volumes = None             # lazy: built on first access
        self._skein_symbolic = None

        if self.A <= SYMBOLIC_THRESHOLD:
            self._build_symbolic()

    def _build_symbolic(self):
        """Build symbolic per-generator matrices and volumes.

        Called automatically for small nuclei. Can be called
        manually for larger ones if symbolic expressions are needed
        (at the cost of computation time).
        """
        self._generator_matrices = []
        self._volumes = []

        for i in range(self.A - 1):
            M = SymbolicTransferMatrix.identity()
            for j in range(i + 1, self.A):
                T = crossing_matrix(self.ordering[i], self.ordering[j])
                M = M * T
            self._generator_matrices.append(M)
            self._volumes.append(M.markov_trace())

        # Full Skein polynomial: symbolic product
        self._skein_symbolic = sp.Integer(1)
        for v in self._volumes:
            self._skein_symbolic = expand(self._skein_symbolic * v)

    @property
    def n_generators(self):
        """Number of braid generators = A - 1."""
        return self.A - 1

    def generator_matrix(self, i):
        """Return the composed transfer matrix at generator sigma_i.

        Requires symbolic build (A <= SYMBOLIC_THRESHOLD or manual
        call to _build_symbolic).
        """
        if self._generator_matrices is None:
            raise RuntimeError(
                f"Symbolic matrices not built for A={self.A}. "
                f"Call _build_symbolic() explicitly or use numeric methods.")
        return self._generator_matrices[i]

    def volume(self, i):
        """Return V_hat_i(q) = z * M_i[0,0] + M_i[1,0] (symbolic).

        Requires symbolic build.
        """
        if self._volumes is None:
            raise RuntimeError(
                f"Symbolic volumes not built for A={self.A}. "
                f"Call _build_symbolic() or use volume_at(i, q_val).")
        return self._volumes[i]

    def volumes(self):
        """Return all per-generator volumes as a list of sympy expressions.

        Requires symbolic build.
        """
        if self._volumes is None:
            raise RuntimeError(
                f"Symbolic volumes not built for A={self.A}. "
                f"Use volumes_at(q_val) for numeric evaluation.")
        return list(self._volumes)

    def skein_polynomial(self):
        """Return P_N(q) = prod_i V_hat_i(q) as a symbolic expression.

        Only available for small nuclei (A <= SYMBOLIC_THRESHOLD).
        For larger nuclei, use skein_at(q_val) for numeric evaluation.
        """
        if self._skein_symbolic is None:
            raise RuntimeError(
                f"Full symbolic Skein polynomial not available for A={self.A} "
                f"(exceeds threshold {SYMBOLIC_THRESHOLD}). "
                f"Use skein_at(q_val) for numeric evaluation.")
        return self._skein_symbolic

    def skein_at(self, q_val):
        """Evaluate P_N(q) = prod_i V_hat_i(q) at q = q_val.

        Works for any nucleus size. Uses the numeric fast path
        for large nuclei.
        """
        if self._volumes is not None:
            # Symbolic path: evaluate each expression
            product = 1.0
            for v in self._volumes:
                product *= float(v.subs(q, q_val))
            return product
        else:
            # Numeric fast path
            vols, log_P, sign = _numeric_skein(
                self.Z, self.N, q_val, self.ordering)
            return sign * math.exp(log_P) if log_P != float('-inf') else 0.0

    def log_skein_at(self, q_val):
        """Evaluate ln|P_N(q)| at q = q_val.

        More numerically stable than log(skein_at) for large nuclei.
        Returns (log_abs_P, sign).
        """
        if self._volumes is not None:
            log_sum = 0.0
            sign = 1
            for v in self._volumes:
                vi = float(v.subs(q, q_val))
                if vi < 0:
                    sign *= -1
                    log_sum += math.log(-vi)
                elif vi > 0:
                    log_sum += math.log(vi)
                else:
                    return float('-inf'), 0
            return log_sum, sign
        else:
            _, log_P, sign = _numeric_skein(
                self.Z, self.N, q_val, self.ordering)
            return log_P, sign

    def volume_at(self, i, q_val):
        """Evaluate V_hat_i at q = q_val.

        Works for any nucleus size.
        """
        if self._volumes is not None:
            return float(self._volumes[i].subs(q, q_val))
        else:
            vols, _, _ = _numeric_skein(
                self.Z, self.N, q_val, self.ordering)
            return vols[i]

    def volumes_at(self, q_val):
        """Evaluate all per-generator volumes at q = q_val.

        Works for any nucleus size. Preferred over volume_at()
        when you need all volumes (avoids recomputation for large A).
        """
        if self._volumes is not None:
            return [float(v.subs(q, q_val)) for v in self._volumes]
        else:
            vols, _, _ = _numeric_skein(
                self.Z, self.N, q_val, self.ordering)
            return vols

    def compare(self, daughter):
        """Compare this nucleus (parent) with a daughter nucleus.

        Returns a dict with symbolic and numeric results.
        For large nuclei, symbolic ratio is omitted.
        """
        result = {
            'per_generator': [],
        }

        # Symbolic per-generator comparison only when available
        if self._volumes is not None and daughter._volumes is not None:
            n = min(self.n_generators, daughter.n_generators)
            for i in range(n):
                result['per_generator'].append(
                    (self._volumes[i], daughter._volumes[i]))

        # Full symbolic ratio only for small nuclei
        if (self._skein_symbolic is not None
                and daughter._skein_symbolic is not None):
            ratio = expand(
                daughter.skein_polynomial() / self.skein_polynomial())
            result['ratio_sym'] = ratio
            result['ln_ratio_sym'] = log(ratio)

        return result

    def __repr__(self):
        return (f"NucleusTransferMatrix(Z={self.Z}, N={self.N}, "
                f"A={self.A}, ordering={''.join(self.ordering)})")


# ========================================================================
# 4. beta_decay_qvalue -- Q-value computation
# ========================================================================

def beta_decay_qvalue(Z_par, N_par, q_val=Q0, label=""):
    """Compute the Q-value for beta-minus decay N(Z,N) -> N(Z+1,N-1).

    Builds parent (Z, N) and daughter (Z+1, N-1) nuclei, computes
    ln(P_dau / P_par) symbolically (for small A) and numerically
    at q_val.

    Args:
        Z_par: proton number of parent
        N_par: neutron number of parent
        q_val: numeric value of q for evaluation (default Q0)
        label: human-readable label for the nucleus

    Returns:
        dict with symbolic (when available) and numeric results
    """
    parent = NucleusTransferMatrix(Z_par, N_par)
    daughter = NucleusTransferMatrix(Z_par + 1, N_par - 1)

    # Numeric evaluation via per-generator product (works for any A)
    ln_par, sgn_par = parent.log_skein_at(q_val)
    ln_dau, sgn_dau = daughter.log_skein_at(q_val)
    ln_ratio_num = ln_dau - ln_par

    # For large nuclei, ln|P| can exceed float range (~709).
    # Keep log-space quantities; only exponentiate when safe.
    def _safe_exp(log_val, sgn):
        if log_val == float('-inf'):
            return 0.0
        if abs(log_val) < 700:
            return sgn * math.exp(log_val)
        return sgn * float('inf')

    P_par_num = _safe_exp(ln_par, sgn_par)
    P_dau_num = _safe_exp(ln_dau, sgn_dau)

    if P_par_num != 0 and math.isfinite(P_par_num) and math.isfinite(P_dau_num):
        ratio_num = P_dau_num / P_par_num
    else:
        # Use log-space ratio (always well-defined)
        ratio_num = sgn_par * sgn_dau * math.exp(
            max(min(ln_ratio_num, 700), -700))

    result = {
        'label': label or f"N({Z_par},{N_par})",
        'Z_par': Z_par,
        'N_par': N_par,
        'A': Z_par + N_par,
        'P_par_num': P_par_num,
        'P_dau_num': P_dau_num,
        'ratio_num': ratio_num,
        'ln_ratio_num': ln_ratio_num,
        'parent': parent,
        'daughter': daughter,
    }

    # Add symbolic results for small nuclei
    A = Z_par + N_par
    if A <= SYMBOLIC_THRESHOLD:
        result['P_par_sym'] = parent.skein_polynomial()
        result['P_dau_sym'] = daughter.skein_polynomial()
        ratio_sym = simplify(
            daughter.skein_polynomial() / parent.skein_polynomial())
        result['ratio_sym'] = ratio_sym

    return result


# ========================================================================
# 5. Verification (__main__)
# ========================================================================

if __name__ == '__main__':

    print("=" * 72)
    print("SYMBOLIC TRANSFER MATRIX ENGINE -- verification")
    print(f"All computations exact in q, evaluated at q0 = {Q0}")
    print("=" * 72)

    # -- 5a. Verify Delta_beta universality ------------------------------
    print()
    print("--- Universality of Delta_beta ---")
    print()

    D1 = T_mix - T_nn       # partner is neutron
    D2 = T_pp - T_mix       # partner is proton

    # Check all four entries are equal
    universal = True
    for i in range(2):
        for j in range(2):
            diff = simplify(D1.mat[i, j] - D2.mat[i, j])
            if diff != 0:
                universal = False
                print(f"  MISMATCH at ({i},{j}): {diff}")

    if universal:
        print("  T_mix - T_nn == T_pp - T_mix   [VERIFIED]")
    else:
        print("  UNIVERSALITY FAILED!")

    # Verify the decomposition: Delta_beta = T(0, HA/2)
    Delta_check = SymbolicTransferMatrix(c=sp.Integer(0), d=HA / 2)

    decomp_ok = True
    for i in range(2):
        for j in range(2):
            diff = simplify(Delta_beta.mat[i, j] - Delta_check.mat[i, j])
            if diff != 0:
                decomp_ok = False
                print(f"  DECOMPOSITION MISMATCH at ({i},{j}): {diff}")

    if decomp_ok:
        print("  Delta_beta = T(0, HA/2)   [VERIFIED]")
    print()

    # Show the matrices at q0
    print("--- Transfer matrices at q0 ---")
    print()
    T_pp.show("T_pp")
    print(f"  at q0: {T_pp.evaluate(Q0)}")
    print()
    T_nn.show("T_nn")
    print(f"  at q0: {T_nn.evaluate(Q0)}")
    print()
    T_mix.show("T_mix")
    print(f"  at q0: {T_mix.evaluate(Q0)}")
    print()
    Delta_beta.show("Delta_beta")
    print(f"  at q0: {Delta_beta.evaluate(Q0)}")
    print()

    # Determinants (symbolic)
    print("--- Determinants (symbolic) ---")
    print(f"  det(T_pp)  = {simplify(T_pp.det())}")
    print(f"  det(T_nn)  = {simplify(T_nn.det())}")
    print(f"  det(T_mix) = {simplify(T_mix.det())}")
    print(f"  det(Delta) = {simplify(Delta_beta.det())}")
    print()

    # -- 5b. Tritium worked example (symbolic) ---------------------------
    print("--- Tritium: 3H(1,2) -> 3He(2,1) [fully symbolic] ---")
    print()

    parent_H3 = NucleusTransferMatrix(1, 2)
    daughter_He3 = NucleusTransferMatrix(2, 1)

    print(f"  Parent  3H  ordering: {''.join(parent_H3.ordering)}")
    print(f"  Daughter 3He ordering: {''.join(daughter_He3.ordering)}")
    print()

    for i in range(parent_H3.n_generators):
        v_par = parent_H3.volume(i)
        v_dau = daughter_He3.volume(i)
        print(f"  sigma_{i}:")
        print(f"    V_hat^par = {simplify(v_par)}")
        print(f"    V_hat^dau = {simplify(v_dau)}")
        print(f"    at q0: V_par = {parent_H3.volume_at(i, Q0):.10f}, "
              f"V_dau = {daughter_He3.volume_at(i, Q0):.10f}")
        print()

    P_par = parent_H3.skein_polynomial()
    P_dau = daughter_He3.skein_polynomial()
    print(f"  P_3H(q)  = {simplify(P_par)}")
    print(f"  P_3He(q) = {simplify(P_dau)}")
    print(f"  at q0: P_3H  = {parent_H3.skein_at(Q0):.10f}")
    print(f"  at q0: P_3He = {daughter_He3.skein_at(Q0):.10f}")

    ln_r = math.log(abs(daughter_He3.skein_at(Q0)
                        / parent_H3.skein_at(Q0)))
    print(f"  ln(P_dau/P_par) = {ln_r:.10f}")
    print()

    # -- 5c. Q-values for all 6 benchmark nuclei -------------------------
    print("=" * 72)
    print("Q-VALUE COMPARISON (transfer matrix vs experiment)")
    print("=" * 72)
    print()

    nuclei = [
        (1,   2,   "3H",     Q_TRITIUM_MEV),
        (6,   8,   "14C",    Q_C14_MEV),
        (27,  33,  "60Co",   Q_CO60_MEV),
        (38,  52,  "90Sr",   Q_SR90_MEV),
        (55,  82,  "137Cs",  Q_CS137_MEV),
        (83,  127, "210Bi",  Q_BI210_MEV),
    ]

    # Header
    print(f"  {'Nucleus':>8s}  {'Z':>3s}  {'N':>3s}  {'A':>4s}  "
          f"{'ln(Pd/Pp)':>12s}  {'Q_exp (MeV)':>12s}  {'sym?':>4s}")
    print(f"  {'--------':>8s}  {'---':>3s}  {'---':>3s}  {'----':>4s}  "
          f"{'------------':>12s}  {'------------':>12s}  {'----':>4s}")

    results = []
    for Z_par, N_par, label, Q_exp in nuclei:
        res = beta_decay_qvalue(Z_par, N_par, q_val=Q0, label=label)
        ln_r = res['ln_ratio_num']
        sym = "yes" if 'P_par_sym' in res else "no"
        print(f"  {label:>8s}  {Z_par:3d}  {N_par:3d}  {Z_par+N_par:4d}  "
              f"{ln_r:+12.6f}  {Q_exp:12.5f}  {sym:>4s}")
        res['Q_exp_MeV'] = Q_exp
        results.append(res)

    print()
    print("  Notes:")
    print("  - ln(P_dau/P_par) is the raw Skein polynomial log-ratio")
    print("  - Conversion to MeV requires the energy scale E_cross * mu_0")
    print("  - The SIGN of ln(ratio) encodes exothermicity")
    print(f"  - 'sym?' = yes means full symbolic polynomial available "
          f"(A <= {SYMBOLIC_THRESHOLD})")
    print()

    # -- 5d. Connection to Gröbner--Shirshov NF -----------------------------------
    print("=" * 72)
    print("GROEBNER NF <-> TRANSFER MATRIX CORRESPONDENCE")
    print("=" * 72)
    print()
    print("  Each V_hat_i(q) in the transfer matrix corresponds to one")
    print("  generator sigma_i in the Iwahori--Hecke algebra NF.")
    print()
    print("  Transfer matrix: V_hat_i = z * M_i[0,0] + M_i[1,0]")
    print("    where M_i = product of T(c_k, d_k) for all crossings "
          "at gen i")
    print()
    print("  Gröbner--Shirshov NF: the reduced element in H_n has basis words.")
    print("    The Markov trace processes generators right-to-left,")
    print("    extracting the SAME z * (coeff of sigma_i) + (constant)")
    print("    at each step.")
    print()
    print("  When generators COMMUTE (|i-j| >= 2), both methods agree "
          "exactly.")
    print("  When generators are ADJACENT (|i-j| = 1), interleaved "
          "crossings")
    print("  require the full Hecke reduction; the transfer matrix "
          "factored")
    print("  form is an approximation.")
    print()

    # Verify for tritium (small enough for symbolic Gröbner--Shirshov)
    print("  Tritium verification "
          "(A=3, generators sigma_0 and sigma_1):")
    print(f"    Transfer matrix P_3H  = "
          f"{parent_H3.skein_at(Q0):.10f}")
    print(f"    Transfer matrix P_3He = "
          f"{daughter_He3.skein_at(Q0):.10f}")
    print()
    print("  To verify against Gröbner--Shirshov NF, run:")
    print("    python3 hecke_symbolic.py   (for protium NF)")
    print("    python3 groebner-beta-decay.py   (for tritium NF)")
